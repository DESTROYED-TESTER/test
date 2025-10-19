import requests
import json
import re
import time
import random
from urllib.parse import quote

class FacebookLogin:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Linux; Android 13; V2060) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Mobile Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
        })
        
    def login(self, username, password):
        """
        Simple Facebook login using traditional method
        """
        try:
            # Step 1: Get login page
            print("[*] Accessing login page...")
            login_url = "https://m.facebook.com/login.php"
            response = self.session.get(login_url)
            
            if response.status_code != 200:
                return False, f"Failed to access login page: {response.status_code}"
            
            # Step 2: Extract form data
            print("[*] Extracting form tokens...")
            html = response.text
            
            # Extract lsd token
            lsd = re.search(r'name="lsd" value="([^"]*)"', html)
            lsd = lsd.group(1) if lsd else ""
            
            # Extract jazoest
            jazoest = re.search(r'name="jazoest" value="([^"]*)"', html)
            jazoest = jazoest.group(1) if jazoest else ""
            
            # Extract m_ts
            m_ts = re.search(r'name="m_ts" value="([^"]*)"', html)
            m_ts = m_ts.group(1) if m_ts else ""
            
            # Extract li
            li = re.search(r'name="li" value="([^"]*)"', html)
            li = li.group(1) if li else ""
            
            # Extract try_number
            try_number = re.search(r'name="try_number" value="([^"]*)"', html)
            try_number = try_number.group(1) if try_number else "0"
            
            # Extract unrecognized_tries
            unrecognized_tries = re.search(r'name="unrecognized_tries" value="([^"]*)"', html)
            unrecognized_tries = unrecognized_tries.group(1) if unrecognized_tries else "0"
            
            print(f"[*] Tokens extracted - lsd: {lsd[:20]}...")
            
            # Step 3: Prepare login data
            login_data = {
                'lsd': lsd,
                'jazoest': jazoest,
                'm_ts': m_ts,
                'li': li,
                'try_number': try_number,
                'unrecognized_tries': unrecognized_tries,
                'email': username,
                'pass': password,
                'login': 'Log In',
                'bi_xrwh': '0'
            }
            
            # Step 4: Submit login
            print(f"[*] Attempting login for: {username}")
            
            login_headers = {
                'User-Agent': 'Mozilla/5.0 (Linux; Android 13; V2060) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Mobile Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.9',
                'Accept-Encoding': 'gzip, deflate',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Origin': 'https://m.facebook.com',
                'Referer': 'https://m.facebook.com/login.php',
                'Connection': 'keep-alive',
            }
            
            response = self.session.post(
                'https://m.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100',
                data=login_data,
                headers=login_headers,
                allow_redirects=True
            )
            
            # Step 5: Check response
            response_text = response.text
            cookies = self.session.cookies.get_dict()
            
            # Check for success indicators
            if 'c_user' in cookies and 'xs' in cookies:
                print("[+] Login successful!")
                print(f"[+] User ID: {cookies['c_user']}")
                return True, "Login successful"
            
            # Check for checkpoint
            elif 'checkpoint' in response.url or 'checkpoint' in response_text:
                print("[-] Checkpoint required")
                return False, "Checkpoint required - Account needs verification"
            
            # Check for 2FA
            elif 'two_factor' in response_text or 'approvals_code' in response_text:
                print("[-] Two-factor authentication required")
                return False, "2FA required"
            
            # Check for incorrect password
            elif 'login_error' in response_text or 'error_box' in response_text:
                error_msg = re.search(r'<div[^>]*class="[^"]*error[^"]*"[^>]*>(.*?)</div>', response_text, re.DOTALL)
                if error_msg:
                    error_text = re.sub('<[^<]+?>', '', error_msg.group(1)).strip()
                    print(f"[-] Login error: {error_text}")
                    return False, error_text
                else:
                    print("[-] Invalid credentials")
                    return False, "Invalid username or password"
            
            else:
                print("[-] Login failed - Unknown error")
                # Save response for debugging
                with open('debug_response.html', 'w', encoding='utf-8') as f:
                    f.write(response_text)
                print("[*] Response saved to debug_response.html")
                return False, "Unknown error - check debug_response.html"
                
        except Exception as e:
            print(f"[-] Exception occurred: {str(e)}")
            return False, f"Exception: {str(e)}"
    
    def get_cookies(self):
        """Get session cookies"""
        return self.session.cookies.get_dict()
    
    def get_user_info(self):
        """Get basic user information"""
        cookies = self.get_cookies()
        if 'c_user' not in cookies:
            return None
        
        try:
            response = self.session.get('https://m.facebook.com/me')
            
            # Extract name
            name_match = re.search(r'<title>(.*?)</title>', response.text)
            name = name_match.group(1) if name_match else "Unknown"
            
            return {
                'user_id': cookies['c_user'],
                'name': name,
                'cookies': cookies
            }
        except:
            return {
                'user_id': cookies['c_user'],
                'cookies': cookies
            }


# Alternative method using Graph API style
class FacebookLoginV2:
    def __init__(self):
        self.session = requests.Session()
        
    def login(self, username, password):
        """
        Login using mobile API endpoint
        """
        try:
            print("[*] Attempting login via mobile API...")
            
            # Get initial cookies
            self.session.get('https://m.facebook.com/')
            
            # Prepare login data
            data = {
                'email': username,
                'pass': password,
                'login': 'Log In'
            }
            
            headers = {
                'User-Agent': 'Mozilla/5.0 (Linux; Android 13; V2060) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Mobile Safari/537.36',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Referer': 'https://m.facebook.com/',
            }
            
            # Submit login
            response = self.session.post(
                'https://m.facebook.com/login.php',
                data=data,
                headers=headers,
                allow_redirects=True
            )
            
            cookies = self.session.cookies.get_dict()
            
            if 'c_user' in cookies:
                print("[+] Login successful!")
                return True, "Success"
            elif 'checkpoint' in response.url:
                return False, "Checkpoint required"
            else:
                return False, "Invalid credentials"
                
        except Exception as e:
            return False, str(e)
    
    def get_cookies(self):
        return self.session.cookies.get_dict()


# Example usage
if __name__ == "__main__":
    print("=" * 50)
    print("Facebook Login Script")
    print("=" * 50)
    
    # Get credentials
    username = input("\n[?] Enter email/phone/username: ").strip()
    password = input("[?] Enter password: ").strip()
    
    print("\n" + "=" * 50)
    print("Method 1: Traditional Login")
    print("=" * 50)
    
    fb = FacebookLogin()
    success, message = fb.login(username, password)
    
    if success:
        print("\n[+] Login Successful!")
        print("\n[+] Cookies:")
        cookies = fb.get_cookies()
        for key, value in cookies.items():
            print(f"  {key}: {value}")
        
        # Get user info
        user_info = fb.get_user_info()
        if user_info:
            print(f"\n[+] User Info:")
            print(f"  Name: {user_info.get('name', 'N/A')}")
            print(f"  User ID: {user_info.get('user_id', 'N/A')}")
    else:
        print(f"\n[-] Login Failed: {message}")
        
        # Try alternative method
        print("\n" + "=" * 50)
        print("Trying Method 2: Mobile API")
        print("=" * 50)
        
        fb2 = FacebookLoginV2()
        success2, message2 = fb2.login(username, password)
        
        if success2:
            print("\n[+] Login Successful!")
            print("\n[+] Cookies:")
            for key, value in fb2.get_cookies().items():
                print(f"  {key}: {value}")
        else:
            print(f"\n[-] Login Failed: {message2}")
