import requests
import json
import uuid
import re
from urllib.parse import urlencode

class FacebookLogin:
    def __init__(self):
        self.session = requests.Session()
        self.base_url = "https://m.facebook.com"
        
    def get_login_tokens(self):
        """Get initial tokens from Facebook login page"""
        headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 13; V2060 Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.7444.21 Mobile Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
        }
        
        response = self.session.get(f'{self.base_url}/login/', headers=headers)
        
        # Extract tokens from response
        tokens = {
            'fb_dtsg': re.search(r'"dtsg":{"token":"([^"]+)"', response.text),
            'lsd': re.search(r'"lsd":"([^"]+)"', response.text),
            'jazoest': re.search(r'"jazoest":"([^"]+)"', response.text),
            'hs': re.search(r'"haste_session":"([^"]+)"', response.text),
            'hsi': re.search(r'"hsi":"([^"]+)"', response.text),
        }
        
        return {k: v.group(1) if v else '' for k, v in tokens.items()}
    
    def encrypt_password(self, password):
        """
        Encrypt password in Facebook format
        Format: #PWD_BROWSER:5:timestamp:encrypted_password
        Note: This is a simplified version. Real encryption requires Facebook's public key
        """
        import time
        import base64
        
        timestamp = int(time.time())
        # This is a placeholder - real implementation needs Facebook's RSA public key
        # For now, returning the format structure
        encrypted = base64.b64encode(password.encode()).decode()
        return f"#PWD_BROWSER:5:{timestamp}:{encrypted}"
    
    def login(self, username, password):
        """
        Perform Facebook login
        
        Args:
            username: Facebook username/email/phone
            password: Facebook password
        """
        
        # Get initial tokens
        print("[*] Getting login tokens...")
        tokens = self.get_login_tokens()
        
        # Generate waterfall_id
        waterfall_id = str(uuid.uuid4())
        
        # Prepare login parameters
        params_data = {
            "server_params": {
                "credential_type": "password",
                "username_text_input_id": "684kjf:62",
                "password_text_input_id": "684kjf:63",
                "login_source": "Login",
                "login_credential_type": "none",
                "server_login_source": "login",
                "ar_event_source": "login_home_page",
                "should_trigger_override_login_success_action": 0,
                "should_trigger_override_login_2fa_action": 0,
                "is_caa_perf_enabled": 0,
                "reg_flow_source": "login_home_native_integration_point",
                "caller": "gslr",
                "is_from_landing_page": 0,
                "is_from_empty_password": 0,
                "is_from_aymh": 0,
                "is_from_password_entry_page": 0,
                "is_from_assistive_id": 0,
                "is_from_msplit_fallback": 0,
                "two_step_login_type": "one_step_login",
                "is_vanilla_password_page_empty_password": 0,
                "INTERNAL__latency_qpl_marker_id": 36707139,
                "INTERNAL__latency_qpl_instance_id": "37644722700435",
                "device_id": None,
                "family_device_id": None,
                "waterfall_id": waterfall_id,
                "offline_experiment_group": None,
                "layered_homepage_experiment_group": None,
                "is_platform_login": 0,
                "is_from_logged_in_switcher": 0,
                "is_from_logged_out": 0,
                "access_flow_version": "pre_mt_behavior"
            },
            "client_input_params": {
                "machine_id": "",
                "cloud_trust_token": None,
                "block_store_machine_id": "",
                "zero_balance_state": "",
                "contact_point": username,
                "password": self.encrypt_password(password),
                "accounts_list": [],
                "fb_ig_device_id": [],
                "secure_family_device_id": "",
                "encrypted_msisdn": "",
                "headers_infra_flow_id": "",
                "try_num": 1,
                "login_attempt_count": 1,
                "event_flow": "login_manual",
                "event_step": "home_page",
                "openid_tokens": {},
                "auth_secure_device_id": "",
                "client_known_key_hash": "",
                "has_whatsapp_installed": 0,
                "sso_token_map_json_string": "",
                "should_show_nested_nta_from_aymh": 0,
                "password_contains_non_ascii": "false",
                "has_granted_read_contacts_permissions": 0,
                "has_granted_read_phone_permissions": 0,
                "app_manager_id": "",
                "aymh_accounts": [{
                    "id": "",
                    "profiles": {
                        "id": {
                            "user_id": "",
                            "name": "",
                            "profile_picture_url": "",
                            "small_profile_picture_url": None,
                            "notification_count": 0,
                            "credential_type": "none",
                            "token": "",
                            "last_access_time": 0,
                            "is_derived": 0,
                            "username": "",
                            "password": "",
                            "has_smartlock": 0,
                            "account_center_id": "",
                            "account_source": "",
                            "credentials": [],
                            "nta_eligibility_reason": None,
                            "from_accurate_privacy_result": 0,
                            "dbln_validated": 0
                        }
                    }
                }],
                "lois_settings": {
                    "lois_token": ""
                }
            }
        }
        
        # Prepare POST data
        data = {
            'aaid': '0',
            'user': '0',
            'a': '1',
            'req': '9',
            'hs': tokens.get('hs', '20380.BP:wbloks_caa_pkg.2.0...0'),
            'dpr': '3',
            'ccg': 'GOOD',
            'rev': '1028624898',
            's': ':5q5mt2:ii9ztu',
            'hsi': tokens.get('hsi', '7562775843550382890'),
            'dyn': '0wzpawlE72fDg9ppo5S12wAxu13wqobE6u7E39x60lW4o0wW1gCwjE0AC09Mx60se2G0pS0ny0oi0zE5W0Y81soG0xo2ewbS1LwpEcE1kU1bo8Xw8S0QU3yw',
            'fb_dtsg': tokens.get('fb_dtsg', ''),
            'jazoest': tokens.get('jazoest', '25223'),
            'lsd': tokens.get('lsd', ''),
            'params': json.dumps({"params": json.dumps(params_data)})
        }
        
        # Prepare headers
        headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 13; V2060 Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.7444.21 Mobile Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, br, zstd',
            'Content-Type': 'application/x-www-form-urlencoded',
            'sec-ch-ua-full-version-list': '',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua': '"Chromium";v="142", "Android WebView";v="142", "Not_A Brand";v="99"',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua-platform-version': '""',
            'origin': 'https://m.facebook.com',
            'x-requested-with': 'mark.via.gp',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://m.facebook.com/ig/login_via/app/',
            'accept-language': 'en-US,en;q=0.9',
            'priority': 'u=1, i',
        }
        
        # Make login request
        url = 'https://m.facebook.com/async/wbloks/fetch/?appid=com.bloks.www.bloks.caa.login.async.send_login_request&type=action&bkv=95c2f471fdc717a6b79ae75e26e90a643f5613e03d463667d5b99baf34570f30'
        
        print(f"[*] Attempting login for: {username}")
        response = self.session.post(url, data=data, headers=headers)
        
        # Check response
        if response.status_code == 200:
            response_text = response.text
            
            # Check for success indicators
            if 'com.bloks.www.caa.login.save-credentials' in response_text:
                print("[+] Login successful!")
                return True, "Login successful"
            elif 'checkpoint' in response_text.lower():
                print("[-] Checkpoint required")
                return False, "Checkpoint required"
            elif 'two_factor' in response_text.lower() or '2fa' in response_text.lower():
                print("[-] Two-factor authentication required")
                return False, "2FA required"
            else:
                print("[-] Login failed")
                return False, "Invalid credentials or unknown error"
        else:
            print(f"[-] Request failed with status code: {response.status_code}")
            return False, f"HTTP {response.status_code}"
    
    def get_cookies(self):
        """Get session cookies"""
        return self.session.cookies.get_dict()


# Example usage
if __name__ == "__main__":
    fb = FacebookLogin()
    
    # Replace with actual credentials
    username = "100076124771608"
    password = "977549"
    
    success, message = fb.login(username, password)
    
    if success:
        print("\n[+] Cookies:")
        for key, value in fb.get_cookies().items():
            print(f"  {key}: {value}")
    else:
        print(f"\n[-] Login failed: {message}")
