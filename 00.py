import requests
import random
import re
import time
from typing import Optional, Dict

class FacebookLogin:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
            'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1'
        })

    def _generate_random_headers(self) -> Dict[str, str]:
        """Generate random device and version information"""
        facebook_version = f"{random.randint(100, 450)}.0.0.{random.randint(1, 40)}.{random.randint(10, 150)}"
        bv = f"{random.randint(1111111, 7777777)}"
        versi_android = f"{random.randint(6, 14)}"
        
        # Random device selection
        devices = ["Nokia 2.4", "TA-1277", "TA-1357", "Nokia C30", "Nokia C12 Pro", 
                   "TA-1339", "Nokia C12", "Nokia 3.4", "Nokia G20", "Nokia 6", 
                   "Nokia C22", "Nokia G22", "Nokia G10", "Nokia C31", "TA-1499", 
                   "TA-1418", "Nokia C32"]
        
        deevice = random.choice(["2312DRAABG", "2201117TG", "M2101K6G", "Redmi Note 14", 
                                "2404ARN45A", "22111317I", "23053RN02A", "M2101K7AI", 
                                "22101316C", "23129RAA4G", "Redmi Note 9 Pro", "Redmi Note 10 Pro"])
        
        device = random.choice(["M910x", "D10i", "2PXH3", "D830x", "U-2u", "M910x", 
                               "2PXH3", "HTC_Desire_S_S510e", "HTC_0P3P5", 
                               "HTC_DesireHD_X315e", "HTC_C715c", "HTC_D616w"])
        
        # Random mobile carriers
        carriers = ["Jio", "Airtel", "Vi", "BSNL", "MTNL"]
        fbmf = random.choice(["redmi", "samsung", "oneplus", "xiaomi", "realme"])
        fbbd = random.choice(["redmi", "samsung", "oneplus", "xiaomi", "realme"])
        model = random.choice(["Redmi Note 9 Pro", "Samsung Galaxy M31", "OnePlus 9R", 
                              "Realme 8 Pro", "POCO X3", "Nokia 6.1"])
        fbdm = f"{{density={random.choice(['2.0', '2.75', '3.0'])},width={random.choice(['1080', '1440'])},height={random.choice(['2400', '3200'])}}}"
        fbcr = random.choice(carriers)
        
        # Build user agent
        us = f"[FBAN/FB4A;FBAV/{facebook_version};FBPN/com.facebook.katana;FBLC/bn_IN;FBBV/{bv};FBCR/{fbcr};FBMF/{fbmf};FBBD/{fbbd};FBDV/{model};FBSV/{versi_android};FBCA/arm64-v8a:null;FBDM/{fbdm};FB_FW/1]"
        
        return {
            'user-agent': us,
            'fban': 'FB4A',
            'fbav': facebook_version,
            'fbbv': bv,
            'fbcr': fbcr,
            'fbmf': fbmf,
            'fbbd': fbbd,
            'fbdv': model,
            'fbsv': versi_android,
            'device': device,
            'deevice': deevice
        }

    def get_login_page(self) -> Optional[requests.Response]:
        """Get initial login page to extract required tokens"""
        headers = self._generate_random_headers()
        url = "https://m.prod.facebook.com/"
        
        try:
            response = self.session.get(url, headers=headers, timeout=30)
            if response.status_code == 200:
                return response
            else:
                print(f"Failed to get login page: {response.status_code}")
                return None
        except requests.RequestException as e:
            print(f"Error fetching login page: {e}")
            return None

    def extract_tokens(self, response_text: str) -> Optional[Dict[str, str]]:
        """Extract required tokens from the HTML response"""
        try:
            tokens = {
                'm_ts': re.search(r'name="m_ts" value="(.*?)"', response_text).group(1),
                'li': re.search(r'name="li" value="(.*?)"', response_text).group(1),
                'jazoest': re.search(r'name="jazoest" value="(.*?)"', response_text).group(1),
                'lsd': re.search(r'name="lsd" value="(.*?)"', response_text).group(1)
            }
            return tokens
        except AttributeError as e:
            print(f"Failed to extract tokens: {e}")
            return None

    def login(self, email: str, password: str) -> bool:
        """
        Attempt to login to Facebook with given credentials
        
        Args:
            email: Facebook email or phone number
            password: Facebook password
            
        Returns:
            Boolean indicating login success
        """
        # Step 1: Get login page
        login_page = self.get_login_page()
        if not login_page:
            return False
        
        # Step 2: Extract tokens
        tokens = self.extract_tokens(login_page.text)
        if not tokens:
            return False
        
        # Step 3: Prepare login data
        timestamp = str(int(time.time()))
        encrypted_password = f"#PWD_BROWSER:0:{timestamp}:{password}"
        
        log_data = {
            'm_ts': tokens['m_ts'],
            'li': tokens['li'],
            'try_number': '0',
            'unrecognized_tries': '0',
            'email': email,
            'prefill_contact_point': '',
            'prefill_source': '',
            'prefill_type': '',
            'first_prefill_source': '',
            'first_prefill_type': '',
            'had_cp_prefilled': 'false',
            'had_password_prefilled': 'false',
            'is_smart_lock': 'false',
            'bi_xrwh': '0',
            'encpass': encrypted_password,
            'bi_wvdp': '',
            'fb_dtsg': '',
            'jazoest': tokens['jazoest'],
            'lsd': tokens['lsd'],
            '__dyn': '',
            '__csr': '',
            '__req': random.choice(['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']),
            '__fmt': '0',
            '__a': '',
            '__user': '0'
        }
        
        # Step 4: Prepare login headers
        login_headers = {
            'authority': 'p.facebook.com',
            'accept': '/',
            'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://p.facebook.com',
            'referer': 'https://p.facebook.com/login/',
            'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': self.session.headers.get('user-agent', ''),
            'x-asbd-id': '359341',
            'x-fb-lsd': tokens['lsd'],
            'x-requested-with': 'XMLHttpRequest',
            'x-response-format': 'JSONStream',
        }
        
        # Step 5: Perform login
        login_url = "https://p.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100"
        
        try:
            response = self.session.post(login_url, data=log_data, headers=login_headers, 
                                        allow_redirects=False, timeout=30)
            
            # Check for successful login
            cookies = self.session.cookies.get_dict()
            
            if 'c_user' in cookies:
                print("✓ Login successful!")
                print(f"User ID: {cookies.get('c_user')}")
                print(f"Session cookies: {list(cookies.keys())}")
                return True
            else:
                print("✗ Login failed - c_user cookie not found")
                print(f"Response: {response.text[:500]}...")  # Show first 500 chars
                return False
                
        except requests.RequestException as e:
            print(f"Error during login: {e}")
            return False

    def logout(self) -> bool:
        """Logout from Facebook"""
        try:
            logout_url = "https://www.facebook.com/logout.php"
            response = self.session.get(logout_url, timeout=30)
            return response.status_code == 200
        except requests.RequestException as e:
            print(f"Error during logout: {e}")
            return False

    def get_cookies(self) -> Dict[str, str]:
        """Get current session cookies"""
        return self.session.cookies.get_dict()


def main():
    """Example usage of the Facebook login script"""
    fb = FacebookLogin()
    
    # Replace with your credentials
    email = "9907159211"
    password = "99071592"
    
    # Attempt login
    success = fb.login(email, password)
    
    if success:
        print("\nSession Cookies:")
        for key, value in fb.get_cookies().items():
            print(f"  {key}: {value[:20]}...")  # Show partial cookie values for security
    
    # Optionally logout
    # fb.logout()


if __name__ == "__main__":
    main()
