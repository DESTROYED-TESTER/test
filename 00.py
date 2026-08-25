import requests

cookies = {
    'datr': 'DTiNaqX1AXorpHDezRNgATu3',
    'wd': '1440x459',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:154.0) Gecko/20100101 Firefox/154.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
    'Referer': 'https://www.messenger.com/',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://www.messenger.com',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Priority': 'u=0, i',
}

data = {
    'jazoest': '22420',
    'lsd': 'AdRgt4koDfzsyLx4lemq3YoE238',
    'initial_request_id': 'A0BzY4agaJnZErWKom_oRAy',
    'timezone': '-330',
    'lgndim': 'eyJ3IjoxNDQwLCJoIjo5MDAsImF3IjoxNDQwLCJhaCI6ODUyLCJjIjoyNH0=',
    'lgnrnd': '233701_NBsv',
    'lgnjs': 'n',
    'email': '100090025785758',
    'pass': '#PWD_BROWSER:5:1787639841:AbZQAPgF1HTlda+Vq+0vmPBoNke8qUskJ1pvfyR32xE/SlB73JO4AUNPFEWfyjhbRpGL7qtywlaoTRcZdcbas75SyOmTqVxJazRjhOUzywts4ehlxyIdQsoXXSKAamYbCQM0TZxMQbjSgw==',
    'default_persistent': '',
}

response = requests.post('https://www.messenger.com/login/password/', cookies=cookies, headers=headers, data=data)

# Check login success using multiple methods:
print(f"Status Code: {response.status_code}")

# Method 1: Check URL redirect (successful login often redirects)
print(f"Final URL: {response.url}")

# Method 2: Check response content
if "checkpoint" in response.text.lower() or "login_approval" in response.text.lower():
    print("❌ Login failed - Security checkpoint/2FA required")
elif "invalid" in response.text.lower() or "incorrect" in response.text.lower():
    print("❌ Login failed - Invalid credentials")
elif response.url == "https://www.messenger.com/":
    print("✅ Login successful! Redirected to messenger.com")
elif "login" in response.url:
    print("❌ Login failed - Still on login page")

# Method 3: Check cookies (successful login sets more cookies)
print("\nCookies set:")
for key in response.cookies.keys():
    print(f"  - {key}")

# Method 4: Check for error messages
if "error" in response.text.lower():
    print("\n⚠️ Error detected in response")

# Method 5: Print response preview (first 500 chars)
print(f"\nResponse preview: {response.text[:500]}")

# Method 6: Look for specific success indicators
success_indicators = [
    "/login/save-device/",
    "home.php",
    "messenger.com/t/",
    "facebook.com",
]

if any(indicator in response.text for indicator in success_indicators):
    print("✅ Possible successful login detected")
