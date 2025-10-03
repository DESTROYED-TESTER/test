import time
import base64
import requests
from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA

def get_facebook_pubkey():
    """Fetch Facebook's login public key."""
    url = 'https://b-graph.facebook.com/pwd_key_fetch'
    resp = requests.get(url)
    data = resp.json()
    pubkey_b64 = data['key']
    key_id = data['id']
    pubkey_der = base64.b64decode(pubkey_b64)
    pubkey = RSA.importKey(pubkey_der)
    return pubkey, key_id

def generate_encpass(password):
    pubkey, key_id = get_facebook_pubkey()
    timestamp = int(time.time())
    cipher = PKCS1_v1_5.new(pubkey)
    encrypted = cipher.encrypt(password.encode('utf-8'))
    enc_blob = base64.b64encode(encrypted).decode('utf-8')
    encpass = f"#PWD_BROWSER:{key_id}:{timestamp}:{enc_blob}"
    return encpass

# Example usage
password = "Password123"
encpass = generate_encpass(password)
print(encpass)
