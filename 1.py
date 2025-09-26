#!/usr/bin/env python3
import re, time, io, struct, base64, requests
from bs4 import BeautifulSoup
from Crypto.Cipher import AES, PKCS1_v1_5
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes

# ========== CONFIG ==========
LOGIN_PAGE = "https://touch.facebook.com/login.php"
PWD_FETCH_URL = "https://b-graph.facebook.com/pwd_key_fetch"
PWD_FETCH_PARAMS = {
    'version': '2',
    'flow': 'CONTROLLER_INITIALIZATION',
    'method': 'GET',
    'fb_api_req_friendly_name': 'pwdKeyFetch',
    'fb_api_caller_class': 'com.facebook.auth.login.AuthOperations',
    'access_token': '438142079694454|fc0a7caa49b192f64f6f5a6d9643bb28'
}
LOGIN_POST_URL = "https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100'"

EMAIL = "100056503155212"      # <-- set email
PASSWORD = "748918"            # <-- set password

# ========== HELPERS ==========
def fetch_login_page(session):
    r = session.get(LOGIN_PAGE, timeout=10)
    r.raise_for_status()
    return r.text

def extract_form_values(html):
    # try to extract lsd, jazoest, li, maybe m_ts from HTML/JS
    soup = BeautifulSoup(html, "html.parser")
    data = {}
    # try common hidden inputs
    for name in ("lsd", "jazoest", "li", "m_ts"):
        el = soup.find("input", {"name": name})
        if el and el.get("value") is not None:
            data[name] = el["value"]
    # fallback: search JS for li or m_ts
    if "li" not in data:
        m = re.search(r'li=([A-Za-z0-9_\-]+)', html)
        if m:
            data["li"] = m.group(1)
    # extract lsd as fallback regex
    if "lsd" not in data:
        m = re.search(r'"lsd"\s*:\s*"([^"]+)"', html)
        if m:
            data["lsd"] = m.group(1)
    # jazoest fallback
    if "jazoest" not in data:
        m = re.search(r'jazoest[\'"]?\s*[:=]\s*[\'"]?([0-9]+)[\'"]?', html)
        if m:
            data["jazoest"] = m.group(1)
    return data

def fetch_public_key_and_kid(session, timeout=10):
    try:
        r = session.post(PWD_FETCH_URL, params=PWD_FETCH_PARAMS, timeout=timeout)
        r.raise_for_status()
        j = r.json()
        return j.get("public_key"), int(j.get("key_id", 5))
    except Exception as e:
        print("pwd_key_fetch error:", e)
        return None, None

def generate_pwd_browser(password: str, public_key_pem: str, key_id: int = 5, aad_ts: int = None):
    if public_key_pem is None:
        raise ValueError("public_key_pem required")

    # AES key + IV
    aes_key = get_random_bytes(32)
    iv = get_random_bytes(12)

    # RSA encrypt AES key (PKCS1 v1.5)
    pub = RSA.import_key(public_key_pem)
    rsa_cipher = PKCS1_v1_5.new(pub)
    encrypted_aes = rsa_cipher.encrypt(aes_key)

    # AAD / timestamp
    ts = int(time.time()) if aad_ts is None else int(aad_ts)

    # AES-GCM encrypt password with ts as AAD
    aes = AES.new(aes_key, AES.MODE_GCM, nonce=iv)
    aes.update(str(ts).encode())        # MUST match header timestamp
    ciphertext, tag = aes.encrypt_and_digest(password.encode())

    # assemble payload: [version_byte=1, key_id_byte] + iv + rsa_len(2 le) + rsa + tag + ciphertext
    buf = io.BytesIO()
    buf.write(bytes([1, int(key_id) & 0xFF]))
    buf.write(iv)
    buf.write(struct.pack("<H", len(encrypted_aes)))
    buf.write(encrypted_aes)
    buf.write(tag)
    buf.write(ciphertext)
    payload_b64 = base64.b64encode(buf.getvalue()).decode()

    return f"#PWD_BROWSER:5:{ts}:{payload_b64}", ts, iv, encrypted_aes, tag, ciphertext

# ========== FLOW ==========
session = requests.Session()
# minimal headers to mimic browser
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Linux; Android 13; Mobile) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.155 Mobile Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
})

print("[*] Fetching login page to collect dynamic tokens...")
html = fetch_login_page(session)
vals = extract_form_values(html)
print("[*] Extracted from page:", vals)

print("[*] Fetching public key from pwd_key_fetch...")
pem, kid = fetch_public_key_and_kid(session)
if not pem:
    print("Failed to fetch public key. Aborting.")
    raise SystemExit(1)
print("[*] Got public key length:", len(pem), " key_id:", kid)

print("[*] Generating encpass (fresh) ...")
encpass, ts_used, iv, enc_aes, tag, ciphertext = generate_pwd_browser(PASSWORD, pem, key_id=kid)
print("encpass header timestamp:", ts_used)
print("encpass sample (first 120 chars):", encpass[:120], "...")

# Build POST payload dict (do NOT pre-URL-encode; requests will do it)
post_data = {
    "m_ts": int(time.time()),
    "li": vals.get("li", ""),
    "try_number": 0,
    "unrecognized_tries": 0,
    "email": EMAIL,
    "prefill_contact_point": EMAIL,
    "prefill_source": "browser_dropdown",
    "prefill_type": "password",
    "first_prefill_source": "browser_dropdown",
    "first_prefill_type": "contact_point",
    "had_cp_prefilled": True,
    "had_password_prefilled": True,
    "is_smart_lock": False,
    "bi_xrwh": "",                 # optional/skip if not known
    "encpass": encpass,
    "fb_dtsg": vals.get("lsd", ""), # sometimes fb_dtsg is in page; adjust if not
    "jazoest": vals.get("jazoest", ""),
    "lsd": vals.get("lsd", ""),
    "_dyn": "",                    # optional
    "req": 1,
    "fmt": 1,
    "a": "",
    "_user": 0
}

print("[*] Posting login request...")
resp = session.post(LOGIN_POST_URL, data=post_data, timeout=20, allow_redirects=True)

print("HTTP status:", resp.status_code)
preview = resp.text[:1200].replace("\n", " ")
print("Response preview:", preview)

cookies_after = session.cookies.get_dict()
print("Cookies received:", cookies_after)

if "c_user" in cookies_after:
    print("Login appears SUCCESSFUL! c_user:", cookies_after.get("c_user"))
else:
    print("Login FAILED. Likely causes:")
    print("- stale/incorrect public key (ensure pwd_key_fetch succeeded)")
    print("- timestamp mismatch (token must be freshly generated immediately before POST)")
    print("- server-side bot checks or other form protections")
    print("Hints: verify the printed encpass timestamp equals AAD used and that encpass length looks sane.")
    print("If still failing, paste the printed 'Response preview' and the encpass header timestamp and I'll help further.")
