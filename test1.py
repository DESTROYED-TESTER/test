import requests
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 13; SM-G960N Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4361.104 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/399.0.0.24.93]'
}

# Step 1: GET login page
url = "https://m.facebook.com/login"
res = requests.get(url, headers=headers)
html = res.text

# Step 2: Regex extraction
def extract_token(name):
    pattern = rf'name=["\']{name}["\'] value=["\'](.*?)["\']'
    match = re.search(pattern, html)
    return match.group(1) if match else None

# Step 3: Tokens
tokens = {
    'rev': extract_token('__rev'),
    's': extract_token('__s'),
    'hsi': extract_token('__hsi'),
    'dyn': extract_token('__dyn'),
}

# Output
for key, value in tokens.items():
    print(f"{key}: {value}")
