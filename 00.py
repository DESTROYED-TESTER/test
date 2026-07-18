import requests
import random
import re
import time
import json
import pickle
import os
from typing import Optional, Dict, Any
from datetime import datetime, timedelta
from pathlib import Path

class FacebookLogin:
    def __init__(self, checkpoint_dir: str = "sessions"):
        self.session = requests.Session()
        self.checkpoint_dir = Path(checkpoint_dir)
        self.checkpoint_dir.mkdir(exist_ok=True)
        
        # Default headers
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
        
        self.last_login_time = None
        self.is_authenticated = False
        self.user_data = {}

    def _generate_random_headers(self) -> Dict[str, str]:
        """Generate random device and version information"""
        facebook_version = f"{random.randint(100, 450)}.0.0.{random.randint(1, 40)}.{random.randint(10, 150)}"
        bv = f"{random.randint(1111111, 7777777)}"
        versi_android = f"{random.randint(6, 14)}"
        
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
        
        carriers = ["Jio", "Airtel", "Vi", "BSNL", "MTNL"]
        fbmf = random.choice(["redmi", "samsung", "oneplus", "xiaomi", "realme"])
        fbbd = random.choice(["redmi", "samsung", "oneplus", "xiaomi", "realme"])
        model = random.choice(["Redmi Note 9 Pro", "Samsung Galaxy M31", "OnePlus 9R", 
                              "Realme 8 Pro", "POCO X3", "Nokia 6.1"])
        fbdm = f"{{density={random.choice(['2.0', '2.75', '3.0'])},width={random.choice(['1080', '1440'])},height={random.choice(['2400', '3200'])}}}"
        fbcr = random.choice(carriers)
        
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

    def _get_checkpoint_path(self, email: str) -> Path:
        """Generate checkpoint file path for a user"""
        # Create safe filename from email
        safe_email = email.replace('@', '_at_').replace('.', '_')
        return self.checkpoint_dir / f"fb_session_{safe_email}.pkl"

    def save_checkpoint(self, email: str, additional_data: Dict = None) -> bool:
        """Save session checkpoint to disk"""
        try:
            checkpoint_path = self._get_checkpoint_path(email)
            
            checkpoint_data = {
                'cookies': self.session.cookies.get_dict(),
                'headers': dict(self.session.headers),
                'timestamp': time.time(),
                'email': email,
                'is_authenticated': self.is_authenticated,
                'user_data': self.user_data,
                'additional': additional_data or {}
            }
            
            # Add cookie expiration info if available
            if 'c_user' in self.session.cookies.get_dict():
                checkpoint_data['c_user'] = self.session.cookies.get_dict().get('c_user')
                checkpoint_data['xs'] = self.session.cookies.get_dict().get('xs')
            
            with open(checkpoint_path, 'wb') as f:
                pickle.dump(checkpoint_data, f)
            
            print(f"✓ Checkpoint saved: {checkpoint_path}")
            return True
            
        except Exception as e:
            print(f"✗ Failed to save checkpoint: {e}")
            return False

    def load_checkpoint(self, email: str) -> Optional[Dict]:
        """Load session checkpoint from disk"""
        try:
            checkpoint_path = self._get_checkpoint_path(email)
            
            if not checkpoint_path.exists():
                print(f"ℹ No checkpoint found for {email}")
                return None
            
            # Check if checkpoint is expired (older than 24 hours)
            with open(checkpoint_path, 'rb') as f:
                checkpoint_data = pickle.load(f)
            
            if time.time() - checkpoint_data.get('timestamp', 0) > 86400:  # 24 hours
                print(f"⚠ Checkpoint expired (older than 24 hours)")
                return None
            
            # Restore session
            self.session.cookies.update(checkpoint_data['cookies'])
            self.session.headers.update(checkpoint_data['headers'])
            self.is_authenticated = checkpoint_data.get('is_authenticated', False)
            self.user_data = checkpoint_data.get('user_data', {})
            
            print(f"✓ Checkpoint loaded: {checkpoint_path}")
            print(f"  Session age: {self._format_time_ago(checkpoint_data['timestamp'])}")
            
            return checkpoint_data
            
        except Exception as e:
            print(f"✗ Failed to load checkpoint: {e}")
            return None

    def _format_time_ago(self, timestamp: float) -> str:
        """Format time difference"""
        diff = time.time() - timestamp
        if diff < 60:
            return f"{int(diff)} seconds ago"
        elif diff < 3600:
            return f"{int(diff/60)} minutes ago"
        elif diff < 86400:
            return f"{int(diff/3600)} hours ago"
        else:
            return f"{int(diff/86400)} days ago"

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

    def validate_session(self) -> bool:
        """Check if current session is still valid"""
        try:
            # Try to access a protected endpoint
            response = self.session.get("https://m.prod.facebook.com/", timeout=10)
            
            # Check if we're redirected to login
            if "login" in response.url or response.status_code in [302, 401, 403]:
                return False
            
            # Check for presence of user data in response
            if "c_user" in self.session.cookies.get_dict():
                return True
                
            return False
            
        except Exception:
            return False

    def login(self, email: str, password: str, use_checkpoint: bool = True) -> bool:
        """
        Attempt to login to Facebook with given credentials
        
        Args:
            email: Facebook email or phone number
            password: Facebook password
            use_checkpoint: Try to load saved session first
            
        Returns:
            Boolean indicating login success
        """
        self.last_login_time = time.time()
        
        # Try to load checkpoint if enabled
        if use_checkpoint:
            checkpoint = self.load_checkpoint(email)
            if checkpoint:
                # Validate the loaded session
                if self.validate_session():
                    print("✓ Session is valid, using existing session")
                    self.is_authenticated = True
                    return True
                else:
                    print("⚠ Session expired, performing fresh login")
        
        print("⟳ Attempting fresh login...")
        
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
                self.is_authenticated = True
                self.user_data = {
                    'user_id': cookies.get('c_user'),
                    'xs_token': cookies.get('xs'),
                    'login_time': time.time()
                }
                
                print("✓ Login successful!")
                print(f"  User ID: {cookies.get('c_user')}")
                
                # Save checkpoint
                self.save_checkpoint(email, {
                    'login_response': response.text[:200] if response.text else '',
                    'status_code': response.status_code
                })
                
                return True
            else:
                self.is_authenticated = False
                print("✗ Login failed - c_user cookie not found")
                print(f"  Response: {response.text[:200]}...")  # Show first 200 chars
                
                # Check for specific error messages
                if "checkpoint" in response.text.lower():
                    print("  ⚠ Account may require checkpoint verification")
                elif "invalid" in response.text.lower():
                    print("  ⚠ Invalid credentials")
                elif "suspicious" in response.text.lower():
                    print("  ⚠ Suspicious login attempt detected")
                    
                return False
                
        except requests.RequestException as e:
            print(f"✗ Error during login: {e}")
            return False

    def logout(self) -> bool:
        """Logout from Facebook and clear checkpoint"""
        try:
            logout_url = "https://www.facebook.com/logout.php"
            response = self.session.get(logout_url, timeout=30)
            
            # Clear session data
            self.session.cookies.clear()
            self.is_authenticated = False
            self.user_data = {}
            
            # Delete checkpoint files
            for checkpoint_file in self.checkpoint_dir.glob("fb_session_*.pkl"):
                try:
                    checkpoint_file.unlink()
                    print(f"✓ Removed checkpoint: {checkpoint_file}")
                except Exception as e:
                    print(f"⚠ Could not remove checkpoint: {e}")
            
            return response.status_code == 200
        except requests.RequestException as e:
            print(f"Error during logout: {e}")
            return False

    def get_cookies(self) -> Dict[str, str]:
        """Get current session cookies"""
        return self.session.cookies.get_dict()

    def get_session_info(self) -> Dict[str, Any]:
        """Get session information"""
        return {
            'authenticated': self.is_authenticated,
            'cookies': self.get_cookies(),
            'user_data': self.user_data,
            'last_login': self.last_login_time,
            'checkpoint_dir': str(self.checkpoint_dir)
        }

    def list_checkpoints(self) -> List[Dict[str, Any]]:
        """List all available checkpoints"""
        checkpoints = []
        for checkpoint_file in self.checkpoint_dir.glob("fb_session_*.pkl"):
            try:
                with open(checkpoint_file, 'rb') as f:
                    data = pickle.load(f)
                    checkpoints.append({
                        'file': checkpoint_file.name,
                        'email': data.get('email', 'unknown'),
                        'timestamp': data.get('timestamp', 0),
                        'age': self._format_time_ago(data.get('timestamp', 0)),
                        'has_c_user': 'c_user' in data.get('cookies', {}),
                        'file_size': checkpoint_file.stat().st_size
                    })
            except Exception:
                continue
        return sorted(checkpoints, key=lambda x: x['timestamp'], reverse=True)


def main():
    """Example usage with checkpoint support"""
    fb = FacebookLogin()
    
    # Show available checkpoints
    print("📂 Available checkpoints:")
    for cp in fb.list_checkpoints():
        print(f"  • {cp['email']} ({cp['age']}) - {cp['file_size']} bytes")
    
    print("\n" + "="*50)
    
    # Replace with your credentials
    email = "9907159211"
    password = "99071592"
    
    # Attempt login with checkpoint support
    success = fb.login(email, password, use_checkpoint=True)
    
    if success:
        print("\n✓ Session Details:")
        session_info = fb.get_session_info()
        print(f"  Authenticated: {session_info['authenticated']}")
        print(f"  User ID: {session_info['user_data'].get('user_id', 'N/A')}")
        print(f"  Cookies: {list(session_info['cookies'].keys())}")
        
        # Demonstrate checkpoint listing after login
        print("\n📂 Updated checkpoints:")
        for cp in fb.list_checkpoints():
            print(f"  • {cp['email']} ({cp['age']})")
    else:
        print("\n✗ Login failed")
    
    # Optionally logout
    # fb.logout()


if __name__ == "__main__":
    from typing import List  # Import for type hint
    main()
