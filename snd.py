import requests
import re
import json

cookies = {
    'datr': 'Eitnac9Jr55lMaaETcsXwk3D',
    'sb': 'EitnaZzbPfbccAsuj6eJIYfE',
    'ps_l': '1',
    'ps_n': '1',
    'wd': '885x773',
    'fr': '0DBxBjQV9WtPFwBoS..BpZysS..AAA.0.0.BpZztO.AWfGeKdmKj0jFW8rYpsnEF6YsKo',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://www.facebook.com',
    'priority': 'u=1, i',
    'referer': 'https://www.facebook.com/login/identify/?ctx=recover&from_login_screen=0',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"',
    'sec-ch-ua-full-version-list': '"Google Chrome";v="143.0.7499.170", "Chromium";v="143.0.7499.170", "Not A(Brand";v="24.0.0.0"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',
    'x-asbd-id': '359341',
    'x-fb-lsd': 'AdEWFxxwPB8',
}

params = {
    'ctx': 'recover',
}

data = {
    'jazoest': '2952',
    'lsd': 'AdEWFxxwPB8',
    'email': '8101729293',
    'did_submit': '1',
    '__user': '0',
    '__a': '1',
    '__req': '5',
    '__hs': '20467.BP:DEFAULT.2.0...0',
    'dpr': '1',
    '__ccg': 'GOOD',
    '__rev': '1031974328',
    '__s': 'kfnkhv:t1mczh:hk6em3',
    '__hsi': '7595108429310200628',
    '__dyn': '7xeUmwkHg7ebwKBAg5S1Dxu13wqovzEdEc8uxa0CEbo1nEhw2nVE4W0qa0FE2awt81s8hwGwQw4iwBgao6C0Mo2swaO4U2zxe3C0D85a1qw8Xxm16wa-0raazo7u0zE2ZwrU6C0hq1Iw5lwnqwIwtU5K0UE62',
    '__hsdp': 'gIMggq8yqAy8F8O948QDQoKUyUYx4cyEcm7Uqg29wIym0TE2pwrQl0bfwfu',
    '__hblp': '0Uwau1kw6Pw4Uw6_wde0anwsE0uPw6Fw1N-04OAHCw0oxo2Mw1jO8VUeU0KF01s-046o1xE',
    '__spin_r': '1031974328',
    '__spin_b': 'trunk',
    '__spin_t': '1768373984',
}

response = requests.post(
    'https://www.facebook.com/ajax/login/help/identify.php',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
)

print(f"Status Code: {response.status_code}")
print("-" * 50)

# Method 1: Try to parse as JSON first
try:
    # Facebook responses often have "for (;;);" prefix
    response_text = response.text
    if response_text.startswith("for (;;);"):
        response_text = response_text[9:]  # Remove "for (;;);"
    
    data = json.loads(response_text)
    print("JSON Response Structure:")
    print(json.dumps(data, indent=2)[:1000])  # Print first 1000 chars
    
    # Look for cuid in the JSON structure
    def find_cuid_in_json(obj, path=""):
        if isinstance(obj, dict):
            for key, value in obj.items():
                current_path = f"{path}.{key}" if path else key
                if "cuid" in key.lower():
                    print(f"\nFound cuid at {current_path}: {value}")
                    return value
                elif isinstance(value, (dict, list)):
                    result = find_cuid_in_json(value, current_path)
                    if result:
                        return result
        elif isinstance(obj, list):
            for i, item in enumerate(obj):
                result = find_cuid_in_json(item, f"{path}[{i}]")
                if result:
                    return result
        return None
    
    cuid = find_cuid_in_json(data)
    if cuid:
        print(f"\n✅ Extracted cuid: {cuid}")
    else:
        print("\n⚠ cuid not found in JSON")

except json.JSONDecodeError:
    print("Response is not JSON, trying regex extraction...")
    
    # Method 2: Use regex to find cuid
    # Look for patterns like: cuid=XXXXXXXX or "cuid":"XXXXXXXX"
    cuid_patterns = [
        r'cuid["\']?\s*[:=]\s*["\']([A-Za-z0-9_-]+)["\']',  # cuid:"XXXX"
        r'cuid=([A-Za-z0-9_-]+)',  # cuid=XXXX
        r'cuid%3D([A-Za-z0-9_-]+)',  # cuid%3DXXXX (URL encoded)
        r'&cuid=([A-Za-z0-9_-]+)',  # &cuid=XXXX in URLs
    ]
    
    for pattern in cuid_patterns:
        matches = re.findall(pattern, response.text, re.IGNORECASE)
        if matches:
            print(f"\n✅ Found cuid(s) with pattern '{pattern}':")
            for match in set(matches):  # Remove duplicates
                print(f"  - {match}")
            break
    else:
        print("\n❌ No cuid found with regex patterns")
        
        # Method 3: Look for URLs containing cuid
        url_pattern = r'https?://[^\s]+cuid[^\s]+'
        url_matches = re.findall(url_pattern, response.text, re.IGNORECASE)
        if url_matches:
            print("\n📌 URLs containing 'cuid':")
            for url in url_matches:
                print(f"  - {url}")
                
                # Try to extract cuid from URL
                cuid_from_url = re.search(r'cuid=([A-Za-z0-9_-]+)', url)
                if cuid_from_url:
                    print(f"    Extracted cuid: {cuid_from_url.group(1)}")

# Method 4: Look for common Facebook response patterns
print("\n" + "="*50)
print("Checking for common Facebook response patterns...")

# Check if response contains redirect or next steps
if "redirect" in response.text.lower():
    print("⚠ Contains redirect - might need to follow it")
    
if "recover" in response.text.lower() or "reset" in response.text.lower():
    print("✓ Recovery/reset related content found")

# Check response headers for clues
if 'Location' in response.headers:
    location = response.headers['Location']
    print(f"\n📌 Redirect Location: {location}")
    # Extract cuid from redirect URL
    cuid_match = re.search(r'cuid=([A-Za-z0-9_-]+)', location)
    if cuid_match:
        print(f"✅ cuid from redirect URL: {cuid_match.group(1)}")

# Save response for debugging
with open("facebook_response.html", "w", encoding="utf-8") as f:
    f.write(response.text)
print("\n✅ Response saved to 'facebook_response.html'")

# Quick analysis
response_lower = response.text.lower()
if "no search results" in response_lower or "not found" in response_lower:
    print("\n⚠ Account/phone not found")
elif "too many attempts" in response_lower:
    print("\n⚠ Rate limited")
elif "security check" in response_lower or "captcha" in response_lower:
    print("\n⚠ Security check/CAPTCHA required")
elif "choose a way" in response_lower or "send code" in response_lower:
    print("\n✓ Recovery options presented")
