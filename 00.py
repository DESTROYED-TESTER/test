import requests
import requests
import re
from urllib.parse import urlparse, parse_qs
cookies = {
    'dpr': '2.75',
    'datr': 'oWfoaeauiueomlq-ugFOiKXV',
    'sb': 'oWfoaVmWeJL2ZK-FJh10HwPF',
    'm_pixel_ratio': '2.75',
    'sfiu': 'AYgOrnBeVhhsX_Wn6vjeVPJ-FvPbUjk1RJwYW0pYQnZP6wUw_UllrJlcBBz692fwYd17qxZ4e0YUa_QflxfgWGzlkkLn9cB-hwyyWiDsDhz4V0SAXxm_vXqqQSB21tbHbPF9Y-PELqlXv3_Z3hAcgUpmAQhSi3MMIQW9bsofO1VNOqZPiHtVnOixj2U8f8tTqwoQKU87k0x_Rmqcp9SbCrKp',
    'fr': '0l6GkRcNaQETy01XX..Bp6Geh..AAA.0.0.Bp6Ggd.AWdWENmmwLNzUMztM12F8KpOYac',
    'wd': '980x1159',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 12; M2010J19SI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Content-Type': 'application/x-www-form-urlencoded',
    'cache-control': 'max-age=0',
    'dpr': '2.75',
    'viewport-width': '980',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"12.0.0"',
    'sec-ch-ua-model': '"M2010J19SI"',
    'sec-ch-ua-full-version-list': '".Not/A)Brand";v="99.0.0.0", "Google Chrome";v="103.0.5060.129", "Chromium";v="103.0.5060.129"',
    'sec-ch-prefers-color-scheme': 'light',
    'upgrade-insecure-requests': '1',
    'origin': 'https://m.facebook.com',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://m.facebook.com/login/account_recovery/name_search/?cuid=AYhaW2jE160GrPZZadtVI3XEJb24ljXxgwZhyDx4U1qaHtgyvDQjI9k8Iv6RY624CdmLGuY6rHl3ig158v9NO3ExcBneJ9WXdbwzYNRbBkYhwQ9lbTr6wBVv5dAOA9-6dpOrUq6wpiZxw_49J8KyiOmvfO7JDvkVvst4XMcrYdouX9aMpkSxx-bi_MYr87WRed6rUXp0DZC-dZ0GRhkiKrZQ&flow=initiate_view&ls=initiate_view&wtsid=rdr_0ifoacwtYE059HQ11&refsrc=deprecated&_rdr',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'Cookie': 'dpr=2.75; datr=oWfoaeauiueomlq-ugFOiKXV; sb=oWfoaVmWeJL2ZK-FJh10HwPF; m_pixel_ratio=2.75; sfiu=AYgOrnBeVhhsX_Wn6vjeVPJ-FvPbUjk1RJwYW0pYQnZP6wUw_UllrJlcBBz692fwYd17qxZ4e0YUa_QflxfgWGzlkkLn9cB-hwyyWiDsDhz4V0SAXxm_vXqqQSB21tbHbPF9Y-PELqlXv3_Z3hAcgUpmAQhSi3MMIQW9bsofO1VNOqZPiHtVnOixj2U8f8tTqwoQKU87k0x_Rmqcp9SbCrKp; fr=0l6GkRcNaQETy01XX..Bp6Geh..AAA.0.0.Bp6Ggd.AWdWENmmwLNzUMztM12F8KpOYac; wd=980x1159',
}

params = {
    'flow': 'initiate_view',
    'ls': 'initiate_view',
}

data = {
    'lsd': 'AdRI_jsCbwbquOXwCTLBVuY4Q7w',
    'jazoest': '22426',
    'cuid': 'AYhaW2jE160GrPZZadtVI3XEJb24ljXxgwZhyDx4U1qaHtgyvDQjI9k8Iv6RY624CdmLGuY6rHl3ig158v9NO3ExcBneJ9WXdbwzYNRbBkYhwQ9lbTr6wBVv5dAOA9-6dpOrUq6wpiZxw_49J8KyiOmvfO7JDvkVvst4XMcrYdouX9aMpkSxx-bi_MYr87WRed6rUXp0DZC-dZ0GRhkiKrZQ',
    'flow': 'initiate_view',
    'pass': 'sumon@12B',
}

response = requests.post(
    'https://m.facebook.com/login/account_recovery/name_search/',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
)

# Check login success
def check_facebook_login_success(response):
    """Check if Facebook login was successful"""
    
    print(f"Response Status Code: {response.status_code}")
    print(f"Response URL: {response.url}")
    
    # Check for success indicators
    success_indicators = [
        'home.php',
        'facebook.com/home',
        'facebook.com/?sk=welcome',
        'save-device',
        'login_success',
        'checkpoint',
        'two_factor'
    ]
    
    # Check for failure indicators
    failure_indicators = [
        'login/account_recovery',
        'login.php',
        'error',
        'invalid',
        'wrong_password'
    ]
    
    # Check URL for success
    url = response.url
    is_success = any(indicator in url for indicator in success_indicators)
    is_failure = any(indicator in url for indicator in failure_indicators)
    
    # Check response content
    response_text = response.text.lower()
    
    if 'checkpoint' in url or 'checkpoint' in response_text:
        print("⚠️ Login requires checkpoint verification (2FA or security check)")
        return 'checkpoint_required'
    elif 'home.php' in url or 'facebook.com/home' in url:
        print("✅ Login successful! Redirected to home page")
        return 'success'
    elif 'save-device' in url:
        print("✅ Login successful! Save device prompt")
        return 'success'
    elif 'login/account_recovery' in url and response.status_code == 200:
        print("❌ Login failed - Still on recovery page")
        return 'failed'
    elif 'wrong_password' in response_text or 'invalid' in response_text:
        print("❌ Login failed - Invalid credentials")
        return 'failed'
    else:
        print("⚠️ Unknown status - Check response manually")
        return 'unknown'
