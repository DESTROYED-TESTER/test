import requests
from pprint import pprint
import json
from urllib.parse import urlparse, parse_qs, urljoin

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
    'email': '100069889795658',
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
    'encpass': '#PWD_BROWSER:5:1772949202:AQ1QAC3SoMlbwtWK6vcSjXsRD6T8bZZ4wNYVbgxP+KQVKapai2iiDNhBwQyt/vhx9zh6T2ENqY31N0unRP4SRSfReTpeGW0X7EgQzwRRfAHT+g6wB2a3JgPKakdR28YSUkcOvUzUlPJgXaMg',
}

print("=" * 60)
print("FACEBOOK LOGIN ATTEMPT - NEXT URL DETECTION")
print("=" * 60)

# Make the request
response = Session.post('https://www.facebook.com/login/device-based/regular/login/', 
                       params=params, headers=headers, data=data, allow_redirects=False)

print(f"\n📊 INITIAL RESPONSE STATUS: {response.status_code} - {response.reason}")

# METHOD 1: Check Location header (most common for redirects)
if 'Location' in response.headers:
    next_url = response.headers['Location']
    print(f"\n🔀 REDIRECT URL (from Location header):")
    print(f"   ➡️  {next_url}")
    
    # Parse the redirect URL
    parsed = urlparse(next_url)
    print(f"\n   📍 Redirect details:")
    print(f"      • Path: {parsed.path}")
    print(f"      • Domain: {parsed.netloc}")
    if parsed.query:
        print(f"      • Query params: {parsed.query}")
        
        # Check if it's a checkpoint URL
        if 'checkpoint' in parsed.path.lower() or 'checkpoint' in parsed.query.lower():
            print(f"      ⚠️  This appears to be a CHECKPOINT/security URL!")
        
        # Extract specific params
        query_params = parse_qs(parsed.query)
        for key, value in query_params.items():
            if key in ['next', 'redirect_uri', 'return_to', 'ref']:
                print(f"      • {key}: {value[0]}")
else:
    print("\n❌ No Location header found in response")

# METHOD 2: Follow redirects and get final URL
print("\n" + "-" * 40)
print("FOLLOWING REDIRECTS TO GET FINAL URL:")
print("-" * 40)

# Create a new session to follow redirects
follow_session = requests.Session()
follow_response = follow_session.post('https://www.facebook.com/login/device-based/regular/login/', 
                                     params=params, headers=headers, data=data, allow_redirects=True)

print(f"\n📊 FINAL RESPONSE STATUS: {follow_response.status_code}")
print(f"📍 FINAL URL: {follow_response.url}")

# Parse the final URL
final_parsed = urlparse(follow_response.url)
print(f"\n   Final URL breakdown:")
print(f"      • Full URL: {follow_response.url}")
print(f"      • Path: {final_parsed.path}")
print(f"      • Domain: {final_parsed.netloc}")
if final_parsed.query:
    print(f"      • Query: {final_parsed.query}")
    
    # Extract important parameters
    final_params = parse_qs(final_parsed.query)
    for key in ['next', 'redirect', 'return_to', 'ref', 'checkpoint_id']:
        if key in final_params:
            print(f"      • {key}: {final_params[key][0]}")

# METHOD 3: Check for next URL in HTML content
print("\n" + "-" * 40)
print("SEARCHING FOR NEXT URL IN HTML CONTENT:")
print("-" * 40)

# Look for next URL patterns in HTML
import re

# Pattern for meta refresh
meta_refresh = re.search(r'<meta[^>]*url=([^"\']+)[^>]*>', response.text, re.IGNORECASE)
if meta_refresh:
    next_url = meta_refresh.group(1)
    print(f"📱 Meta refresh URL found: {next_url}")

# Pattern for form actions with next parameter
form_actions = re.findall(r'<form[^>]*action=["\']([^"\']+)["\'][^>]*>', response.text)
for i, action in enumerate(form_actions[:3]):  # Limit to first 3
    if 'checkpoint' in action or 'login' in action:
        print(f"📝 Form {i+1} action: {action}")
        # Check if it's a relative URL and make it absolute
        if not action.startswith('http'):
            absolute_url = urljoin(response.url, action)
            print(f"      Absolute URL: {absolute_url}")

# Look for next URL in JavaScript
js_next = re.findall(r'["\'](next|redirect_uri|return_url)["\']\s*:\s*["\']([^"\']+)["\']', response.text)
for key, value in js_next[:3]:
    print(f"🔧 JavaScript {key}: {value}")

# Look for checkpoint URLs specifically
checkpoint_urls = re.findall(r'(https?://[^"\'\s]+checkpoint[^"\'\s]*)', response.text)
for url in checkpoint_urls[:3]:
    print(f"⚠️  Checkpoint URL found: {url}")

# METHOD 4: Extract next parameter from the original request
print("\n" + "-" * 40)
print("NEXT URL FROM ORIGINAL REQUEST:")
print("-" * 40)
print(f"📤 Original 'next' parameter: {data.get('next', 'Not provided')}")

# METHOD 5: Check cookies for redirect information
print("\n" + "-" * 40)
print("COOKIE-BASED REDIRECT INFO:")
print("-" * 40)

cookies_dict = Session.cookies.get_dict()
redirect_cookies = [c for c in cookies_dict.keys() if 'redirect' in c.lower() or 'next' in c.lower()]
for cookie in redirect_cookies:
    print(f"🍪 {cookie}: {cookies_dict[cookie]}")

# Check for checkpoint cookie
if 'checkpoint' in cookies_dict:
    print(f"\n🔐 CHECKPOINT COOKIE DETECTED!")
    print(f"   Value: {cookies_dict['checkpoint']}")
    
    # The checkpoint cookie often contains the next URL
    if 'http' in cookies_dict['checkpoint']:
        print(f"   This appears to be a checkpoint URL: {cookies_dict['checkpoint']}")

# METHOD 6: Try to reconstruct the next URL flow
print("\n" + "-" * 40)
print("COMPLETE REDIRECT FLOW:")
print("-" * 40)

if response.history:
    print("Redirect chain:")
    for i, redirect in enumerate(response.history, 1):
        print(f"  {i}. {redirect.url} -> Status: {redirect.status_code}")
        
        # Check if any redirect had a Location header we missed
        if 'Location' in redirect.headers:
            print(f"     Location: {redirect.headers['Location']}")
    
    print(f"  Final. {response.url}")
else:
    # If no redirects but we have a checkpoint cookie, construct the likely URL
    if 'checkpoint' in cookies_dict:
        checkpoint_value = cookies_dict['checkpoint']
        if checkpoint_value.startswith('https://'):
            print(f"🔄 Likely next URL from checkpoint cookie: {checkpoint_value}")
        else:
            print(f"🔄 Likely next URL: https://www.facebook.com/checkpoint/?next={checkpoint_value}")

# SUMMARY
print("\n" + "=" * 60)
print("📌 NEXT URL SUMMARY:")
print("=" * 60)

# Determine the most likely next URL
next_url_candidates = []

# From Location header
if 'Location' in response.headers:
    next_url_candidates.append(("Location header", response.headers['Location']))

# From final URL after redirects
if response.url != 'https://www.facebook.com/login/device-based/regular/login/':
    next_url_candidates.append(("Final URL", response.url))

# From checkpoint cookie
if 'checkpoint' in cookies_dict:
    checkpoint_val = cookies_dict['checkpoint']
    if checkpoint_val.startswith('http'):
        next_url_candidates.append(("Checkpoint cookie", checkpoint_val))
    else:
        next_url_candidates.append(("Checkpoint cookie", f"https://www.facebook.com/checkpoint/?next={checkpoint_val}"))

# From HTML forms
if form_actions:
    for action in form_actions[:1]:  # Just the first one
        if not action.startswith('http'):
            action = urljoin(response.url, action)
        next_url_candidates.append(("Form action", action))

print("\nTop next URL candidates:")
for i, (source, url) in enumerate(next_url_candidates, 1):
    print(f"{i}. [{source}] {url}")

# Determine if it's a checkpoint
checkpoint_indicators = ['checkpoint', 'twofactor', '2fa', 'captcha', 'verify', 'confirm']
is_checkpoint = any(ind in url.lower() for _, url in next_url_candidates for ind in checkpoint_indicators)

print(f"\n🔍 Analysis:")
print(f"   • Checkpoint detected: {'✅ YES' if is_checkpoint else '❌ NO'}")
if is_checkpoint:
    print(f"   • Facebook is blocking this login with a security checkpoint")
    print(f"   • Manual intervention required (CAPTCHA, 2FA, etc.)")

print("=" * 60)
