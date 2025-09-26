# save as gen_encpass.py and run: python gen_encpass.py
import re, time, io, struct, base64, requests
from Crypto.Cipher import AES, PKCS1_v1_5
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes

PASSWORD = "989898989"

# --- utilities to fetch/parse public key from facebook pages/js ---
def fetch_url_text(url, timeout=10):
    r = requests.get(url, timeout=timeout)
    r.raise_for_status()
    return r.text

def find_public_key_in_text(text):
    """
    Try several common patterns:
    - PEM block embedded
    - "pub_key":"<PEM or base64>"
    - modulus/exponent JSON-like fields
    Returns either a PEM string or dict {'mod':..., 'exp':...} or None.
    """
    # 1) PEM block
    m = re.search(r"(-----BEGIN PUBLIC KEY-----.+?-----END PUBLIC KEY-----)", text, re.DOTALL)
    if m:
        return m.group(1)

    # 2) JSON-ish pub_key (escaped)
    m = re.search(r'"pub_key"\s*:\s*"(.*?)"', text)
    if m:
        # unescape common JS escapes
        candidate = m.group(1).encode('utf-8').decode('unicode_escape')
        # if it already looks like PEM, return; else return raw
        if "-----BEGIN" in candidate:
            return candidate
        return candidate

    # 3) modulus / exponent (hex or decimal)
    mod = re.search(r'"mod"\s*:\s*"(0x[0-9a-fA-F]+|[0-9a-fA-F]+)"', text)
    exp = re.search(r'"exp"\s*:\s*"(0x[0-9a-fA-F]+|[0-9a-fA-F]+)"', text)
    if mod and exp:
        return {'mod': mod.group(1), 'exp': exp.group(1)}

    return None

def modexp_to_pem(mod_str, exp_str):
    if isinstance(mod_str, str) and mod_str.startswith("0x"):
        mod_str = mod_str[2:]
    if isinstance(exp_str, str) and exp_str.startswith("0x"):
        exp_str = exp_str[2:]
    n = int(mod_str, 16)
    e = int(exp_str, 16)
    rsa_key = RSA.construct((n, e))
    return rsa_key.export_key().decode()

# --- encpass generation ---
def generate_encpass(password, public_key_pem, key_id=5):
    """
    Return '#PWD_BROWSER:5:<timestamp>:<base64_payload>'
    """
    # AES key and IV
    aes_key = get_random_bytes(32)
    iv = get_random_bytes(12)

    # RSA encrypt AES key with PKCS1_v1_5
    pub = RSA.import_key(public_key_pem)
    rsa_cipher = PKCS1_v1_5.new(pub)
    encrypted_aes = rsa_cipher.encrypt(aes_key)

    # AES-GCM encrypt password with timestamp as AAD
    ts = int(time.time())
    aes = AES.new(aes_key, AES.MODE_GCM, nonce=iv)
    aes.update(str(ts).encode())
    ciphertext, tag = aes.encrypt_and_digest(password.encode())

    # assemble payload: [version_byte=1, key_id_byte] + iv + rsa_len(2 le) + rsa + tag + ciphertext
    buf = io.BytesIO()
    buf.write(bytes([1, int(key_id)]))
    buf.write(iv)
    buf.write(struct.pack("<H", len(encrypted_aes)))
    buf.write(encrypted_aes)
    buf.write(tag)
    buf.write(ciphertext)

    b64 = base64.b64encode(buf.getvalue()).decode()
    return f"#PWD_BROWSER:5:{ts}:{b64}"

# --- main driver: try to auto-fetch public key, else ask user to paste PEM ---
def main():
    # Try common FB sources (you may need to update or add other URLs)
    fb_urls = [
        "https://www.facebook.com/login",
        "https://www.facebook.com/",
        # CDN JS resources (some may 404 or be blocked)
        "https://static.xx.fbcdn.net/rsrc.php/v4/y3/r/9-Ccc804IY2.js",
    ]

    pem = None
    for url in fb_urls:
        try:
            print("Fetching", url)
            txt = fetch_url_text(url)
            found = find_public_key_in_text(txt)
            if found:
                if isinstance(found, str) and "-----BEGIN" in found:
                    pem = found
                    print("Found PEM in", url)
                    break
                elif isinstance(found, str):
                    # maybe base64 encoded PEM or raw; try to see if it starts with 'MI' (base64 pkcs1)
                    if found.strip().startswith("MI"):
                        # try assemble PEM
                        pem = "-----BEGIN PUBLIC KEY-----\n" + "\n".join([found[i:i+64] for i in range(0,len(found),64)]) + "\n-----END PUBLIC KEY-----\n"
                        print("Found base64 key in", url)
                        break
                    else:
                        # raw not recognizable
                        print("Found candidate pub_key string but not PEM; continuing")
                elif isinstance(found, dict):
                    pem = modexp_to_pem(found['mod'], found['exp'])
                    print("Constructed PEM from mod/exp in", url)
                    break
        except Exception as e:
            print("Fetch/parse failed for", url, ":", str(e))

    if pem is None:
        print("\nCould not auto-extract public key from the pages/scripts. Two options:")
        print("1) Paste the PEM public key now (beginning with '-----BEGIN PUBLIC KEY-----').")
        print("2) Paste modulus & exponent in hex if the JS returns them.")
        print("\nIf you want me to generate the token, paste the PEM here. Otherwise, run this script after retrieving the PEM locally.")
        return

    # If we have PEM, generate encpass
    token = generate_encpass(PASSWORD, pem, key_id=5)
    print("\nGenerated encpass for password:", PASSWORD)
    print(token)

if __name__ == "__main__":
    main()
