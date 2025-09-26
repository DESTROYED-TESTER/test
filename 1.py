import time, io, struct, base64, requests
from Crypto.Cipher import AES, PKCS1_v1_5
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes


class Encrypt_PWD:
    def __init__(self):
        pass

    def PWD_FB4A(self, password, public_key=None, key_id="25"):
        # fetch live public key if not provided
        if public_key is None:
            try:
                pwd_key_fetch = 'https://b-graph.facebook.com/pwd_key_fetch'
                pwd_key_fetch_data = {
                    'version': '2',
                    'flow': 'CONTROLLER_INITIALIZATION',
                    'method': 'GET',
                    'fb_api_req_friendly_name': 'pwdKeyFetch',
                    'fb_api_caller_class': 'com.facebook.auth.login.AuthOperations',
                    'access_token': '438142079694454|fc0a7caa49b192f64f6f5a6d9643bb28'
                }
                response = requests.post(pwd_key_fetch, params=pwd_key_fetch_data).json()
                public_key = response.get('public_key')
                key_id = str(response.get('key_id', key_id))
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

            # Assemble payload
            buf = io.BytesIO()
            buf.write(bytes([1, int(key_id) & 0xFF]))          # version, key_id
            buf.write(iv)                                      # nonce
            buf.write(struct.pack("<H", len(encrypted_rand_key)))  # unsigned short length
            buf.write(encrypted_rand_key)                      # RSA encrypted AES key
            buf.write(auth_tag)                                # AES-GCM auth tag
            buf.write(encrypted_passwd)                        # AES-GCM ciphertext

            encoded = base64.b64encode(buf.getvalue()).decode("utf-8")
            return f"#PWD_FB4A:2:{current_time}:{encoded}"

        except Exception as e:
            return f"Error: {str(e)}"

enc = Encrypt_PWD()
print(enc.PWD_FB4A(""))
