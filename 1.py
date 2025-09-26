import requests, time, io, struct, base64, re
from Crypto.Cipher import AES, PKCS1_v1_5
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes

password = '3465767567'

def PWD_BROWSER(password, public_key=None, key_id="5"):
    """
    Generate a #PWD_BROWSER token for Facebook web login.
    Returns: '#PWD_BROWSER:5:<timestamp>:<base64_blob>'
    """
    try:
        # Fetch public key from Facebook web page if not provided
        if not public_key:
            resp = requests.get("https://www.facebook.com/login", timeout=10).text
            # Look for public key in JS (may change if Facebook updates page)
            match = re.search(r'"pub_key":"(-----BEGIN PUBLIC KEY-----.*?-----END PUBLIC KEY-----)"', resp, re.DOTALL)
            if not match:
                return "Failed to fetch public_key from www.facebook.com"
            public_key = match.group(1)
            key_id = "5"

        # AES key + IV
        rand_key = get_random_bytes(32)
        iv = get_random_bytes(12)

        # RSA encrypt AES key
        pubkey = RSA.import_key(public_key)
        cipher_rsa = PKCS1_v1_5.new(pubkey)
        encrypted_rand_key = cipher_rsa.encrypt(rand_key)

        # AES-GCM encrypt password using timestamp as AAD
        cipher_aes = AES.new(rand_key, AES.MODE_GCM, nonce=iv)
        current_time = int(time.time())
        cipher_aes.update(str(current_time).encode())
        encrypted_passwd, auth_tag = cipher_aes.encrypt_and_digest(password.encode())

        # Assemble payload: [1, key_id] + IV + RSA key len + RSA key + auth tag + ciphertext
        buf = io.BytesIO()
        buf.write(bytes([1, int(key_id)]))
        buf.write(iv)
        buf.write(struct.pack("<H", len(encrypted_rand_key)))
        buf.write(encrypted_rand_key)
        buf.write(auth_tag)
        buf.write(encrypted_passwd)

        encoded = base64.b64encode(buf.getvalue()).decode()
        return f"#PWD_BROWSER:5:{current_time}:{encoded}"

    except Exception as e:
        return str(e).title()

# Generate the token
token = PWD_BROWSER(password)
print("Generated #PWD_BROWSER token:")
print(token)
