#!/usr/bin/env python3
import time
import io
import struct
import base64
import requests
import urllib.parse

from Crypto.Cipher import AES, PKCS1_v1_5
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes

# ---------- Config ----------
PWD_FETCH_URL = "https://b-graph.facebook.com/pwd_key_fetch"
PWD_FETCH_PARAMS = {
    'version': '2',
    'flow': 'CONTROLLER_INITIALIZATION',
    'method': 'GET',
    'fb_api_req_friendly_name': 'pwdKeyFetch',
    'fb_api_caller_class': 'com.facebook.auth.login.AuthOperations',
    'access_token': '438142079694454|fc0a7caa49b192f64f6f5a6d9643bb28'
}

LOGIN_URL = "https://limited.facebook.com/login/device-based/login/async/"

# ---------- Helpers ----------
def fetch_public_key(timeout=10):
    """Return (pem, key_id) or (None, None) on failure."""
    try:
        r = requests.post(PWD_FETCH_URL, params=PWD_FETCH_PARAMS, timeout=timeout)
        r.raise_for_status()
        j = r.json()
        return j.get("public_key"), int(j.get("key_id", 5))
    except Exception as e:
        print("fetch_public_key failed:", e)
        return None, None


class EncryptPWD:
    """Generate #PWD_BROWSER tokens compatible with Facebook web login."""

    @staticmethod
    def generate_pwd_browser(password: str, public_key_pem: str, key_id: int = 5,
                             header_version: int = 5, aad_ts: int = None) -> str:
        """
        Return '#PWD_BROWSER:<header_version>:<timestamp>:<base64_payload>'
        - If aad_ts is None, current time is used for AAD and header timestamp.
        - header_version default 5 (standard). For local testing you may set header_version=0 and aad_ts=0.
        """
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

        # AES-GCM encrypt password with ts as AAD (ASCII bytes)
        aes = AES.new(aes_key, AES.MODE_GCM, nonce=iv)
        aes.update(str(ts).encode())
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
        return f"#PWD_BROWSER:{int(header_version)}:{ts}:{payload_b64}"


# ---------- Main example flow ----------
if __name__ == "__main__":
    # choose password you want to encrypt
    password_to_use = "748918"   # change as needed

    # 1) try to auto-fetch public key & key_id
    pem, kid = fetch_public_key()
    if pem is None:
        print("Could not fetch public key automatically. Paste PEM into `pem` variable or ensure network access.")
        # Optionally: set pem = """-----BEGIN PUBLIC KEY-----\n...\n-----END PUBLIC KEY-----"""
        raise SystemExit(1)

    print("Fetched public key (len):", len(pem))
    print("Using key_id:", kid)

    # 2) generate encpass token (#PWD_BROWSER)
    encpass_token = EncryptPWD.generate_pwd_browser(password_to_use, pem, key_id=kid, header_version=5)
    print("\nGenerated encpass token:")
    print(encpass_token)

    # 3) prepare POST data for login (requests will urlencode dict)
    url_params = {
        "m_ts": 1758859976,
        "li": "yBLWaNo3yCbGoJgrOxFDDjjk",
        "try_number": 0,
        "unrecognized_tries": 0,
        "email": "100056503155212",
        "prefill_contact_point": "100056503155212",
        "prefill_source": "browser_dropdown",
        "prefill_type": "password",
        "first_prefill_source": "browser_dropdown",
        "first_prefill_type": "contact_point",
        "had_cp_prefilled": True,
        "had_password_prefilled": True,
        "is_smart_lock": False,
        "bi_xrwh": 92004344361786634,
        "encpass": encpass_token,
        "fb_dtsg": "NAfup2Me3JHXJFN2yxBY35qKn-1LtNpMqJhQzaJ3AqYbs8PMFOvFhGw:0:0",
        "jazoest": 24862,
        "lsd": "AdEVi-OFg_s",
        "_dyn": "1KQdAG1mws8-t0BBBzEnwuo98nwgU2owpUuwcC4o1nEhw23E52q1ew6ywaq1Jw20Ehw73wGwcq0RE1u81x82ew5fw5NyE1582ZwrU2pw4swSw7zwde0UE",
        "req": 1,
        "fmt": 1,
        "a": "AYrzCMozrxxEkLpLMe4Y2HjtqtsmVGwYzrN5JRYYClldhdPtYgFp1Jf_aTSnrZs9GEMJRGEqpBnp7Yr7bbjZFjK5_l3XCV2rjhwTOtu5o4lWwg",
        "_user": 0
    }

    # Some endpoints expect keys without boolean, but requests will stringify values.
    session = requests.Session()
    headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 13; V2060 Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.155 Mobile Safari/537.36',
    # 'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Content-Type': 'application/x-www-form-urlencoded',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Android WebView";v="140"',
    'x-response-format': 'JSONStream',
    'sec-ch-ua-mobile': '?1',
    'x-asbd-id': '359341',
    'x-fb-lsd': 'AdEVi-OFg_s',
    'x-requested-with': 'XMLHttpRequest',
    'origin': 'https://limited.facebook.com',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://limited.facebook.com/login.php?skip_api_login=1&api_key=1393952984244777&kid_directed_site=0&app_id=1393952984244777&signed_next=1&next=https://m.facebook.com/v16.0/dialog/oauth?app_id=1393952984244777&cbt=1758859215730&channel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Dfedd56e5da955addb%26domain%3Dwww.boomplay.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.boomplay.com%252Ff8911011906172fa2%26relation%3Dopener&client_id=1393952984244777&display=touch&domain=www.boomplay.com&e2e=%7B%7D&fallback_redirect_uri=https%3A%2F%2Fwww.boomplay.com%2Fsongs%2F216051730&locale=en_US&logger_id=fb5ecf6aa44bb1de3&origin=2&redirect_uri=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df9bf310860cbd212d%26domain%3Dwww.boomplay.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.boomplay.com%252Ff8911011906172fa2%26relation%3Dopener%26frame%3Dfb8a321b81d3ff397&response_type=token%2Csigned_request%2Cgraph_domain&sdk=joey&version=v16.0&ret=login&fbapp_pres=0&tp=unspecified&cancel_url=https://staticxx.facebook.com/x/connect/xd_arbiter/?version=46',
    'accept-language': 'en-US,en;q=0.9',
    'priority': 'u=1, i',
    # 'Cookie': 'datr=7DnMaEaBSi1euh0ZrTxnFPXZ; sb=7DnMaMKotlR75LUbGLYU-TYB; m_pixel_ratio=2.4749999046325684; ps_l=1; ps_n=1; pas=100056503155212%3AfxOzQdbFmo; dpr=2.4749999046325684; wd=437x973; fr=02n8peqk75hF9D13g.AWcYnHXf1GZF8b7MXvQBW4q05cEXwaTcJhJCnUnlt93z2xfY_YY.BozDns..AAA.0.0.Bo1hLI.AWcm2HkPoopHsJCgNGiCAIgqHgw',
}   
    session.headers.update(headers)

    # optional: preload cookies if you have them
    # session.cookies.update({...})

    print("\nPosting login request to:", LOGIN_URL)
    resp = session.post(LOGIN_URL, data=url_params, timeout=30, allow_redirects=True)

    cookies_after = session.cookies.get_dict()
    if "c_user" in cookies_after:
        print("\nLogin appears SUCCESSFUL")
        print("c_user:", cookies_after.get("c_user"))
        print("xs:", cookies_after.get("xs"))
        print("Cookie header:", "; ".join([f"{k}={v}" for k, v in cookies_after.items()]))
    else:
        print("\nLogin does NOT appear successful.")
        print("HTTP status:", resp.status_code)
        # small preview for debugging
        preview = resp.text[:1500].replace("\n", " ")
        print("Response preview:", preview)
        print("Cookies received:", cookies_after)
