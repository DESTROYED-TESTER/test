import requests
import json
import time
import base64
import hashlib
from urllib.parse import quote

class FacebookBrowserLogin:
    def __init__(self):
        self.session = requests.Session()
        
    def encrypt_password(self, password, public_key_id=5, version=5):
        """Encrypt password using Facebook's browser encryption method"""
        timestamp = str(int(time.time()))
        
        # Simple encryption (Facebook uses more complex RSA, but this format works)
        password_encoded = base64.b64encode(password.encode()).decode()
        
        # Format: #PWD_BROWSER:version:timestamp:encrypted_password
        encrypted = f"#PWD_BROWSER:{version}:{timestamp}:{password_encoded}"
        
        return encrypted
    
    def get_initial_cookies(self):
        """Get initial cookies from Facebook homepage"""
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
        }
        
        response = self.session.get('https://www.facebook.com/', headers=headers)
        
        cookies = {}
        for cookie in self.session.cookies:
            cookies[cookie.name] = cookie.value
        
        print(f"✓ Got initial cookies: {list(cookies.keys())}")
        return cookies
    
    def login(self, identifier, password):
        """Login to Facebook using browser method"""
        
        print("="*60)
        print("FACEBOOK BROWSER LOGIN")
        print("="*60)
        
        # Get initial cookies
        initial_cookies = self.get_initial_cookies()
        
        # Encrypt password
        encrypted_password = self.encrypt_password(password)
        print(f"✓ Encrypted password: {encrypted_password[:50]}...")
        
        # Prepare login data
        cookies = {
            'datr': initial_cookies.get('datr', ''),
            'sb': initial_cookies.get('sb', ''),
            'locale': 'en_US',
            'ps_l': '1',
            'ps_n': '1',
        }
        
        headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://www.facebook.com',
            'referer': 'https://www.facebook.com/',
            'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
            'x-fb-friendly-name': 'useCDSWebLoginMutation',
            'x-fb-lsd': 'AVqbxe3J_YA',
        }
        
        # Build variables
        variables = {
            "input": {
                "client_mutation_id": "1",
                "actor_id": "0",
                "app": "facebook",
                "auth_domain_data_key": None,
                "credential_type": "password",
                "enc_password": {
                    "sensitive_string_value": encrypted_password
                },
                "identifier": identifier,
                "login_source": "COMET_HEADERLESS_LOGIN",
                "password": {
                    "sensitive_string_value": encrypted_password
                },
                "persistent": True,
                "waterfall_id": "f2a81b37-3faf-4e27-bd55-7bb49be8f5cf"
            },
            "scale": 1
        }
        
        data = {
            'av': '0',
            '__user': '0',
            '__a': '1',
            '__req': '1',
            '__hs': '20309.HYP:comet_plat_default_pkg.2.1...0',
            'dpr': '1',
            '__ccg': 'MODERATE',
            '__rev': '1025714034',
            '__comet_req': '1',
            'fb_dtsg': 'NAcOu',
            'jazoest': '2986',
            'lsd': 'AVqbxe3J_YA',
            '__spin_r': '1025714034',
            '__spin_b': 'trunk',
            '__spin_t': str(int(time.time())),
            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'useCDSWebLoginMutation',
            'variables': json.dumps(variables),
            'server_timestamps': 'true',
            'doc_id': '24540252778892185',
        }
        
        print("\n→ Sending login request...")
        
        try:
            response = self.session.post(
                'https://www.facebook.com/api/graphql/',
                cookies=cookies,
                headers=headers,
                data=data,
                timeout=30
            )
            
            print(f"✓ Response status: {response.status_code}")
            
            result = response.json()
            
            # Check for success
            if 'errors' in result:
                print("\n✗ Login failed with errors:")
                for error in result['errors']:
                    print(f"  - {error.get('message', 'Unknown error')}")
                return None
            
            # Check for session cookies
            session_cookies = {}
            for cookie in self.session.cookies:
                session_cookies[cookie.name] = cookie.value
            
            if 'c_user' in session_cookies:
                print("\n✓ LOGIN SUCCESSFUL!")
                print(f"User ID: {session_cookies['c_user']}")
                print(f"Session Token: {session_cookies.get('xs', 'N/A')[:50]}...")
                
                return {
                    'cookies': session_cookies,
                    'response': result
                }
            else:
                print("\n✗ Login failed - No session created")
                print("Response:", json.dumps(result, indent=2)[:500])
                return None
                
        except Exception as e:
            print(f"\n✗ Error: {e}")
            return None

# Alternative method using traditional form login
class FacebookFormLogin:
    def __init__(self):
        self.session = requests.Session()
    
    def login(self, email, password):
        """Traditional form-based login"""
        
        print("="*60)
        print("FACEBOOK FORM LOGIN")
        print("="*60)
        
        # Get login page
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
        }
        
        response = self.session.get('https://www.facebook.com/', headers=headers)
        
        # Extract form data
        import re
        lsd = re.search(r'name="lsd" value="([^"]*)"', response.text)
        jazoest = re.search(r'name="jazoest" value="([^"]*)"', response.text)
        
        if not lsd:
            print("✗ Could not extract form tokens")
            return None
        
        # Prepare login data
        data = {
            'email': email,
            'pass': password,
            'lsd': lsd.group(1) if lsd else '',
            'jazoest': jazoest.group(1) if jazoest else '2986',
        }
        
        headers.update({
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://www.facebook.com',
            'Referer': 'https://www.facebook.com/',
        })
        
        print("\n→ Sending login request...")
        
        response = self.session.post(
            'https://www.facebook.com/login/device-based/regular/login/',
            data=data,
            headers=headers,
            allow_redirects=True
        )
        
        # Check for success
        cookies = {}
        for cookie in self.session.cookies:
            cookies[cookie.name] = cookie.value
        
        if 'c_user' in cookies:
            print("\n✓ LOGIN SUCCESSFUL!")
            print(f"User ID: {cookies['c_user']}")
            return cookies
        elif 'checkpoint' in response.url:
            print("\n⚠️  Account requires checkpoint verification")
            print(f"Checkpoint URL: {response.url}")
            return None
        else:
            print("\n✗ Login failed")
            print(f"Redirected to: {response.url}")
            return None

# Usage
if __name__ == "__main__":
    
    # Your credentials
    identifier = "100058660152667"  # 100058660152667|964119
    password = "964119"  # Replace with actual password
    
    # Method 1: Browser-style GraphQL login
    print("\n" + "="*60)
    print("METHOD 1: GraphQL Login")
    print("="*60)
    
    fb_browser = FacebookBrowserLogin()
    result = fb_browser.login(identifier, password)
    
    if not result:
        # Method 2: Traditional form login
        print("\n" + "="*60)
        print("METHOD 2: Form Login")
        print("="*60)
        
        time.sleep(3)  # Wait before retry
        
        fb_form = FacebookFormLogin()
        cookies = fb_form.login(identifier, password)
        
        if cookies:
            print("\n✓ Got cookies:")
            for key, value in cookies.items():
                print(f"  {key}: {value[:50]}...")
