#!/usr/bin/env python3
import time
import io
import struct
import base64
import requests
from Crypto.Cipher import AES, PKCS1_v1_5
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes

PWD_FETCH_URL = "https://b-graph.facebook.com/pwd_key_fetch"
PWD_FETCH_PARAMS = {
    'version': '2',
    'flow': 'CONTROLLER_INITIALIZATION',
    'method': 'GET',
    'fb_api_req_friendly_name': 'pwdKeyFetch',
    'fb_api_caller_class': 'com.facebook.auth.login.AuthOperations',
    # public app token used by many client implementations
    'access_token': '438142079694454|fc0a7caa49b192f64f6f5a6d9643bb28'
}


def fetch_public_key_and_kid(timeout=10):
    """
    Fetch the public key PEM and key_id from Facebook's pwd_key_fetch endpoint.
    Returns (public_key_pem, key_id) or (None, None) on failure.
    """
    try:
        resp = requests.post(PWD_FETCH_URL, params=PWD_FETCH_PARAMS, timeout=timeout)
        resp.raise_for_status()
        j = resp.json()
        pub = j.get("public_key")
        kid = j.get("key_id", 5)
        if not pub:
            return None, None
        return pub, int(kid)
    except Exception as e:
        # caller can decide how to handle failure
        return None, None


def generate_encpass(password: str, public_key_pem: str, key_id: int = 5) -> str:
    """
    Build a #PWD_BROWSER:5:<timestamp>:<base64_payload> token.
    Steps:
      - generate random 32-byte AES key and 12-byte IV (nonce)
      - RSA-encrypt AES key with the provided public key (PKCS1 v1.5)
      - AES-GCM encrypt the password using timestamp (as AAD)
      - assemble payload: [version_byte=1, key_id_byte] + IV + rsa_len(2-le) + rsa_encrypted_key + auth_tag + ciphertext
      - base64 payload and return with timestamp
    """
    # AES key + IV
    aes_key = get_random_bytes(32)
    iv = get_random_bytes(12)

    # RSA encrypt AES key (PKCS1 v1.5)
    pub = RSA.import_key(public_key_pem)
    rsa_cipher = PKCS1_v1_5.new(pub)
    encrypted_aes = rsa_cipher.encrypt(aes_key)

    # AES-GCM encrypt password with timestamp as AAD
    ts = int(time.time())
    aes = AES.new(aes_key, AES.MODE_GCM, nonce=iv)
    aes.update(str(ts).encode())  # AAD is ASCII timestamp
    ciphertext, tag = aes.encrypt_and_digest(password.encode())

    # assemble payload
    buf = io.BytesIO()
    buf.write(bytes([1, int(key_id)]))                 # version byte (1) + key_id byte
    buf.write(iv)                                      # 12 bytes
    buf.write(struct.pack("<H", len(encrypted_aes)))  # 2-byte little-endian length
    buf.write(encrypted_aes)                           # RSA-encrypted AES key
    buf.write(tag)                                     # 16-byte AES-GCM auth tag
    buf.write(ciphertext)                              # remaining: ciphertext

    b64 = base64.b64encode(buf.getvalue()).decode()
    return f"#PWD_BROWSER:5:{ts}:{b64}"


def parse_encpass(token: str):
    """
    Parse an existing #PWD_BROWSER token into its components.
    Returns dict with keys: token_version, timestamp, version_byte, key_id, iv, rsa_len,
    encrypted_aes, auth_tag, ciphertext
    """
    if not token.startswith("#PWD_BROWSER:"):
        raise ValueError("Not a PWD_BROWSER token")
    parts = token.split(":", 3)
    _, ver, ts, payload_b64 = parts
    payload = base64.b64decode(payload_b64)

    buf = io.BytesIO(payload)
    version_byte = buf.read(1)[0]
    key_id = buf.read(1)[0]
    iv = buf.read(12)
    rsa_len = struct.unpack("<H", buf.read(2))[0]
    encrypted_aes = buf.read(rsa_len)
    auth_tag = buf.read(16)
    ciphertext = buf.read()

    return {
        "token_version": ver,
        "timestamp": int(ts),
        "version_byte": version_byte,
        "key_id": key_id,
        "iv": iv,
        "rsa_len": rsa_len,
        "encrypted_aes": encrypted_aes,
        "auth_tag": auth_tag,
        "ciphertext": ciphertext,
    }


if __name__ == "__main__":
    # Example usage
    password = "989898989"   # change to any password you want
    pub, kid = fetch_public_key_and_kid()
    if not pub:
        print("Failed to fetch public key from pwd_key_fetch. Paste a PEM public key or check network/endpoint.")
    else:
        token = generate_encpass(password, pub, key_id=kid)
        print("Generated encpass:")
        print(token)

        # optional: parse and show hex-inspected components
        parsed = parse_encpass(token)
        print("\nParsed payload components (hex):")
        print("version_byte:", parsed["version_byte"])
        print("key_id:", parsed["key_id"])
        print("iv:", parsed["iv"].hex())
        print("rsa_len:", parsed["rsa_len"])
        print("encrypted_aes:", parsed["encrypted_aes"].hex()[:200] + "..." )
        print("auth_tag:", parsed["auth_tag"].hex())
        print("ciphertext:", parsed["ciphertext"].hex()[:200] + "...")
