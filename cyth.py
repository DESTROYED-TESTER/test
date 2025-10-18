import requests
import re
import random
import uuid
import json
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_v1_5
from Crypto.Random import get_random_bytes
import base64
import struct
import io
import time



class Encrypt_PWD:
    def PWD_FB4A(self, password, public_key=None, key_id="25"):
        """Encrypt password for Facebook"""
        if public_key is None:
            pwd_key_fetch = 'https://b-graph.facebook.com/pwd_key_fetch'
            pwd_key_fetch_data = {
                'version': '2',
                'flow': 'CONTROLLER_INITIALIZATION',
                'method': 'GET',
                'fb_api_req_friendly_name': 'pwdKeyFetch',
                'fb_api_caller_class': 'com.facebook.auth.login.AuthOperations',
                'access_token': '438142079694454|fc0a7caa49b192f64f6f5a6d9643bb28'
            }
            try:
                response = requests.post(pwd_key_fetch, params=pwd_key_fetch_data, timeout=10).json()
                public_key = response.get('public_key')
                key_id = str(response.get('key_id', key_id))
            except:
                pass
        
        rand_key = get_random_bytes(32)
        iv = get_random_bytes(12)
        pubkey = RSA.import_key(public_key)
        cipher_rsa = PKCS1_v1_5.new(pubkey)
        encrypted_rand_key = cipher_rsa.encrypt(rand_key)
        cipher_aes = AES.new(rand_key, AES.MODE_GCM, nonce=iv)
        current_time = int(time.time())
        cipher_aes.update(str(current_time).encode("utf-8"))
        encrypted_passwd, auth_tag = cipher_aes.encrypt_and_digest(password.encode("utf-8"))
        
        buf = io.BytesIO()
        buf.write(bytes([1, int(key_id)]))
        buf.write(iv)
        buf.write(struct.pack("<h", len(encrypted_rand_key)))
        buf.write(encrypted_rand_key)
        buf.write(auth_tag)
        buf.write(encrypted_passwd)
        encoded = base64.b64encode(buf.getvalue()).decode("utf-8")
        
        return f"#PWD_FB4A:2:{current_time}:{encoded}"

class FacebookLogin:
    def __init__(self):
        self.session = requests.Session()
        self.encryptor = Encrypt_PWD()
    
    def generate_useragent(self):
        """Generate random user agent"""
        android_versions = ['10', '11', '12', '13']
        chrome_version = f'{random.randint(110, 138)}.0.{random.randint(5000, 6000)}.{random.randint(100, 200)}'
        devices = ['SM-G973F', 'SM-G991B', 'SM-A525F', 'Pixel 6', 'OnePlus 9']
        
        return f"Mozilla/5.0 (Linux; Android {random.choice(android_versions)}; {random.choice(devices)}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version} Mobile Safari/537.36"
    
    def check_login_success(self, response):
        """Check if login was successful"""
        
        response_text = response.text.replace('\\', '')
        
        # Success indicators
        success_patterns = [
            'com.bloks.www.caa.login.save-credentials',
            'save_credentials_success',
            'login_success',
            'c_user',
            'xs='
        ]
        
        # Error indicators
        error_patterns = [
            'checkpoint_required',
            'login_error',
            'incorrect_password',
            'invalid_email',
            'rate_limit',
            'temporarily_blocked',
            'account_disabled'
        ]
        
        # Check for success
        for pattern in success_patterns:
            if pattern in response_text:
                return 'success', pattern
        
        # Check for errors
        for pattern in error_patterns:
            if pattern in response_text:
                return 'error', pattern
        
        # Check cookies
        cookies = self.session.cookies.get_dict()
        if 'c_user' in cookies and cookies['c_user']:
            return 'success', 'c_user_cookie'
        
        return 'unknown', 'no_clear_indicator'
    
    def extract_user_info(self):
        """Extract user information from cookies"""
        cookies = self.session.cookies.get_dict()
        
        user_info = {
            'user_id': cookies.get('c_user', None),
            'session_token': cookies.get('xs', None),
            'datr': cookies.get('datr', None),
            'fr': cookies.get('fr', None),
            'sb': cookies.get('sb', None)
        }
        
        return user_info
    
    def login(self, username, password):
        """Login to Facebook"""
        
        print("="*60)
        print("FACEBOOK TOUCH LOGIN")
        print("="*60)
        
        # Step 1: Get login page
        head = {
            "accept": "*/*",
            "user-agent": self.generate_useragent(),
            "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
            "accept-encoding": "gzip, deflate",
            "accept-language": "en-US,en;q=0.9",
            "x-requested-with": "XMLHttpRequest",
            "priority": "u=1, i"
        }
        
        print(f"\n→ Username: {username}")
        print("→ Getting login page...")
        
        try:
            resp = self.session.get('https://touch.facebook.com/login.php', headers=head, timeout=15)
        except Exception as e:
            print(f"✗ Connection error: {e}")
            return None
        
        if resp.status_code != 200:
            print(f"✗ Failed to get login page: {resp.status_code}")
            return None
        
        # Extract tokens
        try:
            haste_session = re.search(r'"haste_session":"(.*?)"', resp.text).group(1)
            hsi = re.search(r'"hsi":"(\d+)"', resp.text).group(1)
            fb_dtsg = re.search(r'"dtsg":{"token":"(.*?)"', resp.text).group(1)
            lsd = re.search(r'"lsd":"(.*?)"', resp.text).group(1)
            
            print(f"✓ Extracted tokens successfully")
            
        except AttributeError as e:
            print(f"✗ Failed to extract tokens: {e}")
            return None
        
        # Step 2: Encrypt password
        print("→ Encrypting password...")
        try:
            encrypted_password = self.encryptor.PWD_FB4A(password)
            print(f"✓ Password encrypted")
        except Exception as e:
            print(f"✗ Encryption failed: {e}")
            return None
        
        # Step 3: Prepare login request
        waterfall_id = str(uuid.uuid4())
        
        params_data = {
            "server_params": {
                "credential_type": "password",
                "username_text_input_id": "8v2bez:61",
                "password_text_input_id": "8v2bez:62",
                "login_source": "Login",
                "login_credential_type": "none",
                "server_login_source": "login",
                "ar_event_source": "login_home_page",
                "waterfall_id": waterfall_id,
                "access_flow_version": "pre_mt_behavior"
            },
            "client_input_params": {
                "contact_point": username,
                "password": encrypted_password,
                "try_num": 1,
                "login_attempt_count": 1,
                "event_flow": "login_manual",
                "event_step": "home_page",
                "password_contains_non_ascii": "false"
            }
        }
        
        body = {
            "__aaid": "0",
            "__user": "0",
            "__a": "1",
            "__req": str(random.randint(1, 9)),
            "__hs": haste_session,
            "dpr": "2",
            "__ccg": "EXCELLENT",
            "__rev": "1026809190",
            "__hsi": hsi,
            "__dyn": "0wzpawlE72fDg9ppo5S12wAxu13wqobE6u7E39x60lW4o0wW1gCwjE0AC09Mx60se2G0pS0ny0oi0zE5W0Y81soG0xo2ewbS1LwpEcE1kU1bo8Xw8S0QU3yw",
            "fb_dtsg": fb_dtsg,
            "jazoest": "25247",
            "lsd": lsd,
            "params": json.dumps({"params": json.dumps(params_data)})
        }
        
        head1 = {
            "host": "touch.facebook.com",
            "sec-ch-ua": f'"Not;A=Brand";v="99", "Chromium";v="{random.randint(110, 138)}"',
            "sec-ch-ua-mobile": "?1",
            "sec-ch-ua-platform": '"Android"',
            "user-agent": self.generate_useragent(),
            "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
            "accept": "*/*",
            "origin": "https://touch.facebook.com",
            "sec-fetch-site": "same-origin",
            "sec-fetch-mode": "cors",
            "sec-fetch-dest": "empty",
            "x-fb-lsd": lsd,
            "referer": "https://touch.facebook.com/login/",
            "accept-encoding": "gzip, deflate",
            "accept-language": "en-US,en;q=0.9",
            "priority": "u=1, i",
            "x-fb-dtsg-token": fb_dtsg,
            "cookie": "; ".join([f"{k}={v}" for k, v in self.session.cookies.get_dict().items()])
        }
        
        print("→ Sending login request...")
        
        try:
            response = self.session.post(
                'https://touch.facebook.com/async/wbloks/fetch/?appid=com.bloks.www.bloks.caa.login.async.send_login_request&type=action&__bkv=702c2f684e5cb91415ff73ea04c6b82d5580487fbd0a90975765b0adee500940',
                data=body,
                headers=head1,
                timeout=30
            )
        except Exception as e:
            print(f"✗ Request failed: {e}")
            return None
        
        print(f"✓ Response received: {response.status_code}")
        
        # Check login success
        status, indicator = self.check_login_success(response)
        
        print("\n" + "="*60)
        print("LOGIN RESULT")
        print("="*60)
        
        if status == 'success':
            print(f"✓ LOGIN SUCCESSFUL!")
            print(f"  Indicator: {indicator}")
            
            # Extract user info
            user_info = self.extract_user_info
