import requests,time
from pprint import pprint
import json

Session = requests.Session()

# Your existing headers and data...
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://www.facebook.com',
    'Referer': 'https://www.facebook.com/facebook/',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
    'dpr': '1',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
    'sec-ch-ua-full-version-list': '"Not;A=Brand";v="99.0.0.0", "Google Chrome";v="139.0.7258.139", "Chromium";v="139.0.7258.139"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'viewport-width': '1136',
}

params = {
    'login_attempt': '1',
}

data = {
    'email': '100069814779091',
    'cuid': '',
    'guid': 'fe7c9ad27486757c4',
    'lgnjs': '1772949169',
    'lgnrnd': '215248_5sPy',
    'locale': 'en_GB',
    'login_source': 'comet_login_header',
    'next': 'https://www.facebook.com/facebook/',
    'skstamp': '',
    'timezone': '-330',
    'prefill_contact_point': '',
    'prefill_source': '',
    'lsd': 'AdR3xKrdycBYAeO3Mdb7UwKg9AY',
    'jazoest': '22301',
    'lgndim': 'eyJ3IjoxNDQwLCJoIjo5MDAsImF3IjoxNDQwLCJhaCI6ODYwLCJjIjoyNH0=',
    'ab_test_data': 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA',
    'encpass':  "#PWD_BROWSER:0:{}:{}".format(str(time.time()).split('.')[0],'57273200'),
}

print("=" * 60)
print("FACEBOOK LOGIN ATTEMPT DIAGNOSTICS")
print("=" * 60)

# Make the request
response = Session.post('https://x.facebook.com/login/device-based/regular/login/', 
                       params=params, headers=headers, data=data)

print(f"\n📊 RESPONSE STATUS: {response.status_code} - {response.reason}")

# Check all cookies
cookies_dict = Session.cookies.get_dict()
print(f"\n🍪 COOKIES RECEIVED ({len(cookies_dict)} total):")
for cookie_name, cookie_value in cookies_dict.items():
    preview = cookie_value[:30] + "..." if len(cookie_value) > 30 else cookie_value
    print(f"  • {cookie_name}: {preview}")

# Check for checkpoint specifically
print("\n🔍 CHECKPOINT ANALYSIS:")
if "checkpoint" in cookies_dict:
    print("  ✅ 'checkpoint' cookie FOUND!")
    print(f"  📝 Checkpoint value: {cookies_dict['checkpoint']}")
    
    # Try to determine checkpoint type
    if "https" in cookies_dict.get('checkpoint', ''):
        print("  ⚠️  This appears to be a security checkpoint URL")
else:
    print("  ❌ No 'checkpoint' cookie found")

# Check for other security-related cookies
security_cookies = ['c_user', 'xs', 'fr', 'sb', 'datr', 'spin', 'wd']
print("\n🛡️  SECURITY COOKIES CHECK:")
for sec_cookie in security_cookies:
    status = "✅ Present" if sec_cookie in cookies_dict else "❌ Missing"
    print(f"  • {sec_cookie}: {status}")

# Response Headers Analysis
print("\n📋 IMPORTANT RESPONSE HEADERS:")
important_headers = ['Location', 'Content-Type', 'X-FB-Debug', 'X-FB-Rev']
for header in important_headers:
    if header in response.headers:
        print(f"  • {header}: {response.headers[header][:100]}...")

# Check if redirected
if response.history:
    print(f"\n🔄 REDIRECT CHAIN ({len(response.history)} redirects):")
    for i, redirect in enumerate(response.history, 1):
        print(f"  {i}. {redirect.url} -> Status: {redirect.status_code}")
    print(f"  Final URL: {response.url}")
else:
    print(f"\n📍 Final URL: {response.url}")

# Response content analysis
print("\n📄 RESPONSE CONTENT PREVIEW:")
content_preview = response.text[:500].replace('\n', ' ').replace('\r', '')
print(content_preview + "...")

# Look for specific checkpoint indicators in HTML
checkpoint_indicators = [
    'checkpoint', 'approvals_code', 'captcha', 'twofactor', '2FA',
    'security check', 'confirm identity', 'verify', 'suspicious'
]

print("\n🔎 CHECKPOINT INDICATORS IN HTML:")
found_indicators = []
for indicator in checkpoint_indicators:
    if indicator.lower() in response.text.lower():
        found_indicators.append(indicator)
        print(f"  ✅ Found: '{indicator}'")

if not found_indicators:
    print("  ❌ No checkpoint indicators found in HTML")

# Parse URL for checkpoint parameters
from urllib.parse import urlparse, parse_qs
parsed_url = urlparse(response.url)
url_params = parse_qs(parsed_url.query)
if url_params:
    print("\n🔧 URL PARAMETERS:")
    for param, values in url_params.items():
        if any(ind in param.lower() for ind in checkpoint_indicators):
            print(f"  ⚠️  {param}: {values}")
        else:
            print(f"  • {param}: {values}")

# Final verdict
print("\n" + "=" * 60)
print("📌 FINAL VERDICT:")
if "checkpoint" in cookies_dict: #or any(ind in response.text.lower() for ind in checkpoint_indicators)
    print("❌ LOGIN BLOCKED - Checkpoint/security challenge detected")
    print("   Facebook has detected this as a suspicious login attempt")
    print("   You would need to:")
    print("   • Solve a CAPTCHA")
    print("   • Verify via email/SMS")
    print("   • Confirm identity through security questions")
elif 'c_user' in cookies_dict and 'xs' in cookies_dict:
    print("✅ POSSIBLE SUCCESS - Login cookies detected!")
    print("   However, this might still require additional verification")
else:
    print("⚠️ INCONCLUSIVE - No clear success or failure indicators")
    print("   The login attempt likely failed silently")

print("=" * 60)
