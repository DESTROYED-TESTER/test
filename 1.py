# run locally: pip install requests pycryptodome
import time, io, struct, base64, requests
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
    'access_token': '438142079694454|fc0a7caa49b192f64f6f5a6d9643bb28'
}

def fetch_public_key(timeout=10):
    """Return (pem, key_id) or (None, None) on failure."""
    try:
        r = requests.post(PWD_FETCH_URL, params=PWD_FETCH_PARAMS, timeout=timeout)
        r.raise_for_status()
        j = r.json()
        return j.get("public_key"), int(j.get("key_id", 5))
    except Exception:
        return None, None

def generate_encpass(password: str, public_key_pem: str, key_id: int = 5,
                     header_version: int = 5, aad_ts: int = None) -> str:
    """
    Generate #PWD_BROWSER:<header_version>:<timestamp>:<base64_payload>
    - If aad_ts is None we use current time as AAD and timestamp in header.
    - If aad_ts is provided, it's used as AAD; the same value is placed in the header timestamp
      so payload AAD and header timestamp match.
    - To create a "#PWD_BROWSER:0" style token set header_version=0 and aad_ts=0
      (payload will be encrypted with AAD==b'0').
    """
    if public_key_pem is None:
        raise ValueError("public_key_pem is required")

    # AES key + IV
    aes_key = get_random_bytes(32)
    iv = get_random_bytes(12)

    # RSA encrypt AES key (PKCS1 v1.5)
    pub = RSA.import_key(public_key_pem)
    rsa_cipher = PKCS1_v1_5.new(pub)
    encrypted_aes = rsa_cipher.encrypt(aes_key)

    # AAD / timestamp
    if aad_ts is None:
        ts = int(time.time())
    else:
        ts = int(aad_ts)

    # AES-GCM encrypt password with ts as AAD (ASCII bytes)
    aes = AES.new(aes_key, AES.MODE_GCM, nonce=iv)
    aes.update(str(ts).encode())        # **this must match the header timestamp**
    ciphertext, tag = aes.encrypt_and_digest(password.encode())

    # assemble payload: [1, key_id] + iv + rsa_len(2 le) + rsa + tag + ciphertext
    buf = io.BytesIO()
    buf.write(bytes([1, int(key_id) & 0xFF]))
    buf.write(iv)
    buf.write(struct.pack("<H", len(encrypted_aes)))
    buf.write(encrypted_aes)
    buf.write(tag)
    buf.write(ciphertext)
    payload_b64 = base64.b64encode(buf.getvalue()).decode()

    # header timestamp must equal the AAD used above
    return f"#PWD_BROWSER:{int(header_version)}:{ts}:{payload_b64}"

# Example usage:
if __name__ == "__main__":
    password = "989898989"

    # Option A: Auto-fetch Facebook public key (may fail if endpoint blocked)
    pem, kid = fetch_public_key()
    if pem is None:
        print("Couldn't fetch public key; paste PEM into 'pem' variable to continue.")
    else:
        # 1) Standard valid-style token:
        token = generate_encpass(password, pem, key_id=kid)
        print("Standard token (version 5):", token)

        # 2) Make a self-consistent token with header_version 0 and AAD timestamp 0
        token_zero = generate_encpass(password, pem, key_id=kid, header_version=0, aad_ts=0)
        print("Self-consistent token with header 0 (for testing only):", token_zero)
