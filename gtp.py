import time, io, struct, base64, requests
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_v1_5
from Crypto.Random import get_random_bytes

class Encrypt_PWD_Web:
    def __init__(self):
        pass

    def PWD_BROWSER(self, password, public_key=None, key_id="5"):
        """
        Generate a #PWD_BROWSER token for Facebook web login.
        Returns: '#PWD_BROWSER:5:<timestamp>:<base64_blob>'
        """
        if public_key is None:
            try:
                pwd_key_fetch = 'https://b-graph.facebook.com/pwd_key_fetch'
                params = {
                    'version': '2',
                    'flow': 'CONTROLLER_INITIALIZATION',
                    'method': 'GET',
                    'fb_api_req_friendly_name': 'pwdKeyFetch',
                    'fb_api_caller_class': 'com.facebook.auth.login.AuthOperations',
                    'access_token': '438142079694454|fc0a7caa49b192f64f6f5a6d9643bb28'
                }
                response = requests.post(pwd_key_fetch, params=params, timeout=10).json()
                public_key = response.get('public_key')
                key_id = str(response.get('key_id', key_id))
                if not public_key:
                    return "Failed to fetch public_key"
            except Exception as e:
                return f"API: {str(e)}"

        try:
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
            cipher_aes.update(str(current_time).encode("utf-8"))
            encrypted_passwd, auth_tag = cipher_aes.encrypt_and_digest(password.encode("utf-8"))

            # Assemble payload: [1, key_id] + IV + RSA key len + RSA key + auth tag + ciphertext
            buf = io.BytesIO()
            buf.write(bytes([1, int(key_id)]))
            buf.write(iv)
            buf.write(struct.pack("<H", len(encrypted_rand_key)))  # unsigned short
            buf.write(encrypted_rand_key)
            buf.write(auth_tag)
            buf.write(encrypted_passwd)

            encoded = base64.b64encode(buf.getvalue()).decode("utf-8")

            # Web token version 5
            return f"#PWD_BROWSER:5:{current_time}:{encoded}"

        except Exception as e:
            return str(e).title()


password = "12345678"
web_encryptor = Encrypt_PWD_Web()
web_token = web_encryptor.PWD_BROWSER(password)
print("Generated web #PWD_BROWSER token:", web_token)
