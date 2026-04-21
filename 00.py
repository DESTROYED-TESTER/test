import re
import requests
import json

# Start a session to handle cookies automatically
session = requests.Session()
response = session.get('https://www.facebook.com/login')

# 1. Extract the main LSD token
lsd_match = re.search(r'name="lsd" value="(.*?)"', response.text)
if lsd_match:
    lsd_value = lsd_match.group(1)
else:
    raise ValueError("Could not find LSD token")

# 2. Extract jazoest (another common required field)
jazoest_match = re.search(r'name="jazoest" value="(.*?)"', response.text)
jazoest_value = jazoest_match.group(1) if jazoest_match else ""

# 3. Setup your payload
data = {
    'lsd': lsd_value,
    'jazoest': jazoest_value,
    'email': 'YOUR_EMAIL',
    'pass': 'YOUR_PASSWORD',
    # Some modern FB logins use a nested JSON structure in 'variables'
    'variables': json.dumps({
        "input": {
            "caa_login_request_extra_info": {
                "lsd": lsd_value  # Update the nested LSD here
            }
        }
    })
}

print(f"LSD Extracted: {lsd_value}")
# Proceed with session.post to https://www.facebook.com/login/device-based/regular/login/
