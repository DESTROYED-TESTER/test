import requests
import base64
import struct
import io
import time
import json
import re
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_v1_5
from Crypto.Random import get_random_bytes

def PWD_FB4A(password, public_key=None, key_id="25"):
    if public_key is None:
        resp = requests.post(
            "https://b-graph.facebook.com/pwd_key_fetch",
            params={
                "version": "2",
                "flow": "CONTROLLER_INITIALIZATION",
                "method": "GET",
                "fb_api_req_friendly_name": "pwdKeyFetch",
                "fb_api_caller_class": "com.facebook.auth.login.AuthOperations",
                "access_token": "438142079694454|fc0a7caa49b192f64f6f5a6d9643bb28",
            },
        ).json()
        public_key = resp.get("public_key")
        key_id = str(resp.get("key_id", key_id))

    rand_key = get_random_bytes(32)
    iv = get_random_bytes(12)
    pubkey = RSA.import_key(public_key)
    cipher_rsa = PKCS1_v1_5.new(pubkey)
    encrypted_rand_key = cipher_rsa.encrypt(rand_key)
    cipher_aes = AES.new(rand_key, AES.MODE_GCM, nonce=iv)
    current_time = int(time.time())
    cipher_aes.update(str(current_time).encode("utf-8"))
    encrypted_passwd, auth_tag = cipher_aes.encrypt_and_digest(password.encode("utf-8"))

    buf = io.BytesIO()
    buf.write(bytes([1, int(key_id)]))
    buf.write(iv)
    buf.write(struct.pack("<h", len(encrypted_rand_key)))
    buf.write(encrypted_rand_key)
    buf.write(auth_tag)
    buf.write(encrypted_passwd)
    encoded = base64.b64encode(buf.getvalue()).decode("utf-8")

    return f"#PWD_FB4A:2:{current_time}:{encoded}"

def facebook_login(uid, password):
    session = requests.Session()

    headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://www.facebook.com',
    'Referer': 'https://www.facebook.com/?stype=lo&flo=1&deoia=1&jlou=Afi33CVi9aSFnvUb391F5-qlmBdkDydfWor_r096lWwevRPeU25CXbhD3Lu2vAKsAmolO1g11BrRAPV91IVkN8RM2lH1tSLE5rEyJ4LRALngow&smuh=25331&lh=Ac_MV4aD9PHN0himQIs',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36',
    'dpr': '1',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Google Chrome";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
    'sec-ch-ua-full-version-list': '"Google Chrome";v="141.0.7390.108", "Not?A_Brand";v="8.0.0.0", "Chromium";v="141.0.7390.108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'viewport-width': '862',
}

    # Fetch login page to get hidden tokens
    login_page = session.get("https://touch.facebook.com/login.php", headers=headers)
    lsd = re.search(r'name="lsd" value="(.*?)"', login_page.text)
    jazoest = re.search(r'name="jazoest" value="(.*?)"', login_page.text)
    if not (lsd and jazoest):
        print("✗ Could not extract login tokens.")
        return None

    encpass = PWD_FB4A(password)

    data = {
        'lsd': lsd.group(1),
        'jazoest': jazoest.group(1),
        'email': uid,
        'encpass': encpass,
        'login_source': 'login_bluebar',
    }

    resp = session.post("https://www.facebook.com/login/device-based/regular/login/",
                        headers=headers, data=data, allow_redirects=True)

    if "c_user" in session.cookies:
        print("✓ Login successful!")
        return session.cookies.get_dict()
    else:
        print("✗ Login failed!")
        print("Page title:", re.search(r"<title>(.*?)</title>", resp.text))
        return None

if __name__ == "__main__":
    uid = "6301109484"
    password = "630110"
    facebook_login(uid, password)
