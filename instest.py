import hashlib
import uuid
import time
import urllib.parse
import random
import requests

class InstagramLogin:
    def __init__(self):
        self.session = requests.Session()
        
    def login(self, username, password):
        """Login to Instagram account"""
        
        # Generate device ID and other required IDs
        device_id = f"android-{uuid.uuid4().hex[:16]}"
        family_device_id = str(uuid.uuid4())
        
        # First hash for username+password
        first_hash = hashlib.md5()
        first_hash.update(username.encode('utf-8') + password.encode('utf-8'))
        first_hex = first_hash.hexdigest()
        
        # Second hash with salt for device ID
        second_hash = hashlib.md5()
        second_hash.update(first_hex.encode('utf-8') + '12345'.encode('utf-8'))
        android_id_hash = second_hash.hexdigest()[:16]
        
        # Generate user agent
        useragent = "Instagram 309.0.0.28.114 Android (29/10; 380dpi; 1080x2080; OnePlus; GM1903; OnePlus7; qcom; en_US; 439209455)"
        
        # Headers
        headers = {
            'host': 'i.instagram.com',
            'x-ig-app-locale': 'in_ID',
            'x-ig-device-locale': 'in_ID',
            'x-ig-mapped-locale': 'id_ID',
            'x-pigeon-session-id': f'UFS-{str(uuid.uuid4())}-3',
            'x-pigeon-rawclienttime': f'{time.time():.3f}',
            'x-bloks-version-id': 'c55a52bd095e76d9a88e2142eaaaf567c093da6c0c7802e7a2f101603d8a7d49',
            'x-ig-www-claim': '0',
            'x-bloks-is-prism-enabled': 'false',
            'x-bloks-is-layout-rtl': 'false',
            'x-ig-device-id': device_id,
            'x-ig-family-device-id': family_device_id,
            'x-ig-android-id': f'android-{android_id_hash}',
            'x-fb-connection-type': 'MOBILE.LTE',
            'x-ig-connection-type': 'MOBILE(LTE)',
            'x-ig-capabilities': '3brTv10=',
            'priority': 'u=3',
            'user-agent': useragent,
            'accept-language': 'id-ID, en-US',
            'x-mid': '',
            'ig-intended-user-id': '0',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'x-fb-http-engine': 'Liger',
            'x-fb-client-ip': 'True',
            'x-fb-server-cluster': 'True',
            'x-ig-bandwidth-speed-kbps': str(random.randint(100, 300)),
            'x-ig-bandwidth-totalbytes-b': str(random.randint(500000, 900000)),
            'x-ig-bandwidth-totaltime-ms': str(random.randint(1000, 9000)),
            'x-ig-app-id': '3419628305025917',
            'connection': 'keep-alive'
        }
        
        # Generate timestamp for password
        timestamp = int(time.time())
        
        # URL encode username and password
        encoded_username = urllib.parse.quote(username)
        encoded_password = urllib.parse.quote(password)
        
        # Generate encrypted password format
        encrypted_password = f'#PWD_INSTAGRAM:0:{timestamp}:{encoded_password}'
        
        # Prepare the encoded data
        params_dict = {
            "client_input_params": {
                "device_id": f"android-{android_id_hash}",
                "login_attempt_count": 1,
                "secure_family_device_id": "",
                "machine_id": "",
                "accounts_list": [],
                "auth_secure_device_id": "",
                "password": encrypted_password,
                "family_device_id": family_device_id,
                "fb_ig_device_id": [],
                "device_emails": [],
                "try_num": 3,
                "event_flow": "login_manual",
                "event_step": "home_page",
                "openid_tokens": {},
                "client_known_key_hash": "",
                "contact_point": encoded_username,
                "encrypted_msisdn": ""
            },
            "server_params": {
                "username_text_input_id": "p5hbnc:46",
                "device_id": f"android-{android_id_hash}",
                "should_trigger_override_login_success_action": 0,
                "server_login_source": "login",
                "waterfall_id": str(uuid.uuid4()),
                "login_source": "Login",
                "INTERNAL__latency_qpl_instance_id": 152086072800150,
                "reg_flow_source": "login_home_native_integration_point",
                "is_platform_login": 0,
                "is_caa_perf_enabled": 0,
                "credential_type": "password",
                "family_device_id": family_device_id,
                "INTERNAL__latency_qpl_marker_id": 36707139,
                "offline_experiment_group": "caa_iteration_v3_perf_ig_4",
                "INTERNAL_INFRA_THEME": "harm_f",
                "password_text_input_id": "p5hbnc:47",
                "ar_event_source": "login_home_page"
            }
        }
        
        # Convert params to JSON string and URL encode
        import json
        params_json = json.dumps(params_dict)
        encoded_params = urllib.parse.quote(params_json)
        
        # Prepare the complete encoded string
        encode = f'params={encoded_params}&bk_client_context=%7B%22bloks_version%22%3A%225f56efad68e1edec7801f630b5c122704ec5378adbee6609a448f105f34a9c73%22%2C%22styles_id%22%3A%22instagram%22%7D&bloks_versioning_id=c55a52bd095e76d9a88e2142eaaaf567c093da6c0c7802e7a2f101603d8a7d49'
        
        # Update content-length in headers
        headers['content-length'] = str(len(encode))
        
        # Send login request
        url = 'https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.login.async.send_login_request/'
        
        try:
            response = self.session.post(
                url, 
                data=encode, 
                headers=headers, 
                allow_redirects=True
            )
            
            # Check if login was successful
            if 'logged_in_user' in response.text:
                cookies = self.session.cookies.get_dict()
                print("✓ Login successful!")
                print(cookies)
                # Extract user ID from response (simplified)
                import json
                try:
                    response_data = json.loads(response.text)
                    if 'logged_in_user' in response_data:
                        user_id = response_data['logged_in_user'].get('pk', 'Unknown')
                        print(f"✓ User ID: {user_id}")
                except:
                    print("✓ Login successful (could not parse user ID)")
                
                # Save cookies for future requests
                cookies = self.session.cookies.get_dict()
                print(f"✓ Session cookies saved" cookies)
                return True, response
            else:
                print("✗ Login failed")
                print(f"Response: {response.text[:200]}...")  # Print first 200 chars
                return False, response
                
        except Exception as e:
            print(f"✗ Error during login: {str(e)}")
            return False, None
    
    def save_result(self, response):
        """Save login result and handle different scenarios"""
        # This is a placeholder for your Simpan_Result method
        # You can implement your own logic here
        result_ok = False
        result_two = False  # 2FA result
        result_cp = False   # Checkpoint result
        
        if response and 'logged_in_user' in response.text:
            result_ok = True
        elif response and 'two_factor_required' in response.text:
            result_two = True
        elif response and 'checkpoint_required' in response.text:
            result_cp = True
            
        return result_ok, result_two, result_cp

# Usage example
if __name__ == "__main__":
    # Create login instance
    instagram = InstagramLogin()
    
    # Your credentials (replace with actual credentials)
    username = "8918168736"
    password = "891816"
    
    # Try to login
    print(f"Attempting to login as: {username}")
    success, response = instagram.login(username, password)
    
    if success:
        # You can now use the session for other API calls
        print("Ready to make authenticated requests!")
        
        # Example: Get user profile
        # profile_response = instagram.session.get('https://i.instagram.com/api/v1/users/self/info/')
        # print(f"Profile: {profile_response.json()}")
    else:
        print("Login failed. Please check your credentials.")
