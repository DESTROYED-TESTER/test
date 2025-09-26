password = "12345678"

# --- Generate ---
# Option A: fetch key (needs network)
# pwd_token = generate_pwd_browser(password, public_key=None, key_id="5", fetch_public_key=True)

# Option B: test with your own PEM
PUBLIC_PEM = """-----BEGIN PUBLIC KEY-----
... your key ...
-----END PUBLIC KEY-----"""
pwd_token = generate_pwd_browser(password, public_key=PUBLIC_PEM, key_id="5", fetch_public_key=False)

print("Generated token:")
print(pwd_token)

# --- Inspect ---
info = inspect_pwd_browser(pwd_token)
print("\nInspection result:")
for k, v in info.items():
    print(f"{k:30} {v}")
