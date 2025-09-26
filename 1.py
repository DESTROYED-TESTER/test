#!/usr/bin/env python3
import re, time, io, struct, base64, requests
from bs4 import BeautifulSoup
from Crypto.Cipher import AES, PKCS1_v1_5
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes

# --------- Configuration ----------
EMAIL = "100056503155212"   # replace
PASSWORD = "748918"  # replace

LOGIN_PAGE = "https://touch.facebook.com"   # login page to scrape tokens
LOGIN_POST_URL = "https://limited.facebook.com/login/device-based/login/async/"

PWD_FETCH_URL = "https://b-graph.facebook.com/pwd_key_fetch"
PWD_FETCH_PARAMS = {
    'version': '2',
    'flow': 'CONTROLLER_INITIALIZATION',
    'method': 'GET',
    'fb_api_req_friendly_name': 'pwdKeyFetch',
    'fb_api_caller_class': 'com.facebook.auth.login.AuthOperations',
    'access_token': '438142079694454|fc0a7caa49b192f64f6f5a6d9643bb28'
}

# --------- Helpers ----------
def fetch_login_page(session, url=LOGIN_PAGE):
    r = session.get(url, timeout=10)
    r.raise_for_status()
    return r.text

def extract_tokens(html):
    vals = {}
    # quick regex attempt
    for name in ("lsd","jazoest","li","m_ts"):
        m = re.search(r'name="%s" value="(.*?)"' % re.escape(name), html)
        if m:
            vals[name] = m.group(1)
    # bs4 fallback
    soup = BeautifulSoup(html, "html.parser")
    for name in ("lsd","jazoest","li","m_ts"):
        if name not in vals:
            el = soup.find("input", {"name": name})
            if el and el.get("value"):
                vals[name] = el["value"]
    return vals

def post_login(session, data):
    """Post login and return (resp, cookies_dict)"""
    resp = session.post(LOGIN_POST_URL, data=data, timeout=20, allow_redirects=True)
    return resp, session.cookies.get_dict()

def fetch_public_key(session, timeout=10):
    try:
        r = session.post(PWD_FETCH_URL, params=PWD_FETCH_PARAMS, timeout=timeout)
        r.raise_for_status()
        j = r.json()
        return j.get("public_key"), int(j.get("key_id", 5))
    except Exception as e:
        print("pwd_key_fetch failed:", e)
        return None, None

def generate_encpass(password, public_key_pem, key_id=5):
    """Return '#PWD_BROWSER:5:<ts>:<payload>'"""
    if public_key_pem is None:
        raise ValueError("public_key_pem required")

    # AES key + IV
    aes_key = get_random_bytes(32)
    iv = get_random_bytes(12)

    # RSA encrypt AES key (PKCS1 v1.5)
    pub = RSA.import_key(public_key_pem)
    rsa_cipher = PKCS1_v1_5.new(pub)
    encrypted_aes = rsa_cipher.encrypt(aes_key)

    # timestamp (AAD)
    ts = int(time.time())

    # AES-GCM encrypt password with timestamp as AAD
    aes = AES.new(aes_key, AES.MODE_GCM, nonce=iv)
    aes.update(str(ts).encode())
    ciphertext, tag = aes.encrypt_and_digest(password.encode())

    # assemble payload
    buf = io.BytesIO()
    buf.write(bytes([1, int(key_id) & 0xFF]))
    buf.write(iv)
    buf.write(struct.pack("<H", len(encrypted_aes)))
    buf.write(encrypted_aes)
    buf.write(tag)
    buf.write(ciphertext)
    payload_b64 = base64.b64encode(buf.getvalue()).decode()
    return f"#PWD_BROWSER:5:{ts}:{payload_b64}"

# --------- Main flow ----------
def attempt_login_with_plain_then_enc():
    session = requests.Session()
    session.headers.update({
        "User-Agent":"Mozilla/5.0 (Linux; Android 13; Mobile) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140 Mobile Safari/537.36"
    })

    # 1) fetch login page tokens
    print("[*] Fetching login page...")
    html = fetch_login_page(session)
    tokens = extract_tokens(html)
    print("[*] Extracted tokens:", {k: bool(v) for k,v in tokens.items()})

    # 2) Try plaintext login
    post_plain = {
        "email": EMAIL,
        "pass": PASSWORD,
        "prefill_contact_point": EMAIL,
        "prefill_type": "password",
        "first_prefill_type": "contact_point",
        "had_cp_prefilled": "true",
        "had_password_prefilled": "true",
        "is_smart_lock": "false",
        "lsd": tokens.get("lsd",""),
        "jazoest": tokens.get("jazoest",""),
        "li": tokens.get("li",""),
        "m_ts": tokens.get("m_ts",""),
        "_user": 0
    }
    print("[*] Attempting plaintext login...")
    resp, cookies = post_login(session, post_plain)
    if "c_user" in cookies:
        print("[+] Plaintext login SUCCESS")
        return True

    # quick heuristic: check for "Incorrect password" message in response
    preview = resp.text[:2000].replace("\n"," ")
    if "Incorrect password" in preview or '"m_login_password":{"error":true' in preview or '"m_login_notice"' in preview:
        print("[-] Plaintext login rejected as incorrect. Will generate encpass and retry.")
    else:
        print("[-] Plaintext login did not succeed (no c_user). Will attempt encpass retry.")

    # 3) Fetch public key and generate encpass
    print("[*] Fetching public key...")
    pub, kid = fetch_public_key(session)
    if not pub:
        print("! Could not fetch public key — cannot generate encpass. Aborting.")
        return False
    print("[*] Got public key len:", len(pub), " key_id:", kid)

    encpass = generate_encpass(PASSWORD, pub, key_id=kid)
    print("[*] Generated encpass header ts (embedded):", encpass.split(":",3)[2][:10], "...")

    # 4) Retry login using encpass (fresh tokens from page might be needed)
    # Re-fetch page tokens just before retry to be safe
    html2 = fetch_login_page(session)
    tokens2 = extract_tokens(html2)
    post_enc = {
        "email": EMAIL,
        "encpass": encpass,
        "prefill_contact_point": EMAIL,
        "prefill_type": "password",
        "first_prefill_type": "contact_point",
        "had_cp_prefilled": "true",
        "had_password_prefilled": "true",
        "is_smart_lock": "false",
        "lsd": tokens2.get("lsd",""),
        "jazoest": tokens2.get("jazoest",""),
        "li": tokens2.get("li",""),
        "m_ts": tokens2.get("m_ts",""),
        "_user": 0
    }
    print("[*] Attempting encpass login...")
    resp2, cookies2 = post_login(session, post_enc)
    preview2 = resp2.text[:2000].replace("\n"," ")
    if "c_user" in cookies2:
        print("[+] Encpass login SUCCESS")
        return True
    else:
        print("[-] Encpass login FAILED.")
        print("HTTP status:", resp2.status_code)
        print("Response preview:", preview2)
        print("Cookies received:", cookies2)
        return False

if __name__ == "__main__":
    ok = attempt_login_with_plain_then_enc()
    print("Done. Success =", ok)
