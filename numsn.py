import os
import random
import re
import sys
import time
import platform
import webbrowser
import json
import certifi
import threading
import requests
import base64
from concurrent.futures import ThreadPoolExecutor as threadpol
import ssl
import socket
from datetime import datetime, timezone, timedelta
import hashlib
import subprocess
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import itertools

if getattr(sys, 'frozen', False):
    os.chdir(os.path.dirname(sys.executable))

WHITE = '\x1b[1;97m'
GREEN = '\x1b[1;92m'
RED = '\x1b[1;91m'
DARK_GREEN = '\x1b[1;32m'
LIGHT_GRAY = '\x1b[1;37m'
CYAN = '\x1b[1;96m'
YELLOW = '\x1b[1;93m'
BLUE = '\x1b[1;94m'
MAGENTA = '\x1b[1;95m'
ORANGE = '\x1b[38;5;208m'
GOLD = '\x1b[38;5;220m'
VIOLET = '\x1b[38;5;141m'
TOXIC = '\x1b[38;2;170;200;0m'
PURPLE = '\x1b[38;2;150;80;200m'

opt_labels = [f"{GREEN}[{RED}{str(i).zfill(2)}{GREEN}]" for i in range(1, 8)]

l0 = f"{GREEN}[{RED}00{GREEN}]"
EKL = f"{CYAN}:{WHITE}"
LINE = f"{CYAN}•━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━•"

SERVER_MAP = {
    1: 'm.facebook.com',
    2: 'mbasic.facebook.com',
    3: 'touch.facebook.com',
    4: 'free.facebook.com',
    5: 'm.alpha.facebook.com',
    6: 'm.beta.facebook.com',
    7: 'x.facebook.com'
}

print_lock = threading.Lock()
counter_lock = threading.Lock()

total_checked = 0
total_success = 0
total_failed = 0
total_error = 0
PROXIES = None
CURRENT_LOCALE = 'en_US'

# SDCARD paths for Termux
SDCARD_PATH = '/sdcard'
NUMBER_LIST_PATH = '/sdcard/Number_List.txt'
SETTINGS_PATH = '/sdcard/Setting.json'
ERROR_LOGS_DIR = '/sdcard/Error_Logs'

def make_request(url):
    if url.startswith('https://'):
        url = url[8:]
    elif url.startswith('http://'):
        url = url[7:]
    
    if '/' in url:
        host, path = url.split('/', 1)
        path = '/' + path
    else:
        host, path = url, ''
    
    context = ssl.create_default_context(cafile=certifi.where())
    context.check_hostname = True
    context.verify_mode = ssl.CERT_REQUIRED
    
    try:
        with socket.create_connection((host, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=host) as ssock:
                request = f"GET {path} HTTP/1.1\r\n"
                request += f"Host: {host}\r\n"
                request += "User-Agent: Python-Socket\r\n"
                request += "Accept: */*\r\n"
                request += "Connection: close\r\n\r\n"
                
                ssock.sendall(request.encode())
                
                response = b''
                while True:
                    data = ssock.recv(4096)
                    if not data:
                        break
                    response += data
                    
    except Exception:
        return None

    try:
        header_data, body_data = response.split(b'\r\n\r\n', 1)
        headers = header_data.decode('ignore', errors='ignore').split('\r\n')
        status_line = headers[0]
        status_code = int(status_line.split()[1])
        
        headers_dict = {}
        cookies = {}
        
        for header in headers[1:]:
            key, value = header.split(':', 1)
            headers_dict[key.strip()] = value.strip()
            
            if key.lower() == 'set-cookie':
                cookie_parts = value.split(';')[0].split('=')
                cookies[cookie_parts[0].strip()] = cookie_parts[1].strip()
        
        response_text = body_data.decode('ignore', errors='ignore')
        
        try:
            response_json = json.loads(response_text)
        except json.JSONDecodeError:
            response_json = None
            
        return {
            'status_code': status_code,
            'text': response_text,
            'json': response_json,
            'headers': headers_dict,
            'cookies': cookies
        }
    except Exception:
        return None

SECRET_KEY = b'LHANKLRTOLUMCDCK'
SECRET_KEY2 = b'GTRMAREAMLXUDWDJ'

def dec_rq(sxrreqq):
    dec_base4 = base64.urlsafe_b64decode(sxrreqq.encode('utf-8'))
    cipher = AES.new(SECRET_KEY, AES.MODE_ECB)
    dec_cryoto = unpad(cipher.decrypt(dec_base4), AES.block_size).decode('utf-8')
    jsn_dta = json.loads(dec_cryoto)
    return jsn_dta

def dec_rq2(keyid):
    c_base4 = base64.urlsafe_b64decode(keyid.encode('utf-8'))
    ciphr = AES.new(SECRET_KEY2, AES.MODE_ECB)
    c_cryoto = unpad(ciphr.decrypt(c_base4), AES.block_size).decode('utf-8')
    return c_cryoto

def get_safe_cmd(cmd):
    try:
        return subprocess.check_output(cmd, shell=True, stderr=subprocess.DEVNULL).decode('ignore', errors='ignore').strip()
    except:
        return None

def get_android_device_id():
    unique_factors = []
    
    # Try to get Android ID or device-specific info
    try:
        # Try to get Android ID (requires termux-api package)
        android_id = get_safe_cmd('termux-telephony-deviceinfo 2>/dev/null | grep device_id | cut -d: -f2')
        if android_id:
            unique_factors.append(android_id.strip())
    except:
        pass
    
    # Try to get IMEI (requires termux-api and permissions)
    try:
        imei = get_safe_cmd('termux-telephony-deviceinfo 2>/dev/null | grep imei | head -1 | cut -d: -f2')
        if imei:
            unique_factors.append(imei.strip())
    except:
        pass
    
    # Get device model and hardware info
    try:
        model = get_safe_cmd('getprop ro.product.model 2>/dev/null')
        brand = get_safe_cmd('getprop ro.product.brand 2>/dev/null')
        device = get_safe_cmd('getprop ro.product.device 2>/dev/null')
        if model and brand and device:
            unique_factors.append(f"{brand}_{model}_{device}".upper())
    except:
        pass
    
    # Get serial number if available
    try:
        serial = get_safe_cmd('getprop ro.serialno 2>/dev/null')
        if serial:
            unique_factors.append(serial.strip().upper())
    except:
        pass
    
    # Get Android build fingerprint
    try:
        fingerprint = get_safe_cmd('getprop ro.build.fingerprint 2>/dev/null')
        if fingerprint:
            unique_factors.append(fingerprint.strip())
    except:
        pass
    
    # If no device-specific info found, use user and system info
    if not unique_factors:
        try:
            user = os.getlogin() if hasattr(os, 'getlogin') else os.getenv('USER', 'TERMUX_USER')
            unique_factors.append(user.upper())
        except:
            unique_factors.append('TERMUX_USER')
        
        # Add system info
        sys_info = f"{platform.system()}_{platform.release()}_{platform.machine()}"
        unique_factors.append(sys_info.upper())
    
    raw_id = ''.join(unique_factors).replace(' ', '').replace('-', '').replace('_', '').upper()
    hashed_id = hashlib.sha256(raw_id.encode()).hexdigest().upper()
    return hashed_id[:32]

def apvv():
    try:
        sxrreq = make_request('https://mrsxrtools.pythonanywhere.com/apv')
        if sxrreq['status_code'] == 200:
            import re
            match = re.search('id="srv-verification" value="(.*?)"', sxrreq['text'])
            if match:
                sxrreqq = match.group(1)
                data = dec_rq(sxrreqq)
            else:
                sxrreqq = sxrreq['text']
                data = dec_rq(sxrreqq)
            
            # Use Android device ID for Termux
            devisid = get_android_device_id()
            
            for flinf in data:
                keyid = flinf['Device_ID']
                dvs = dec_rq2(keyid)
                if dvs == devisid:
                    global user_nm, expr
                    user_nm = flinf['User_Name']
                    expr = flinf['End_date']
                    
                    nw_tm = datetime.now(timezone.utc)
                    expirs = datetime.strptime(expr, '%Y-%m-%d %H:%M').replace(tzinfo=timezone.utc)
                    
                    if nw_tm >= expirs:
                        clear_logo()
                        print(f" {WHITE}Device ID {EKL} {GREEN}{devisid}\n\n {GREEN}UserName {EKL} {user_nm}\n {RED}Expired {EKL} {expr} (Utc)\n{LINE}\n {RED}Your access has expired.")
                        input(f" {WHITE}Press enter to buy the tool again")
                        webbrowser.open('https://t.me/yeasin_hossain018')
                        sys.exit(0)
                        os._exit(1)
                    
                    if len(data) < 5:
                        os.system('clear')
                        input('Hi, Amar Nola Sele')
                        exit()
                    
                    if expirs >= nw_tm + timedelta(days=35):
                        os.system('clear')
                        input('Hi, Amar Nola Sele')
                        exit()

                    sxr_main()
            
            clear_logo()
            print(f" {GREEN}Device ID {EKL} {devisid}")
            print(f" {RED}Your Device ID is not registered. Please contact the owner to get access.\n")
            input(f" {WHITE}Press enter to contact owner")
            webbrowser.open('https://t.me/mrsxrtool')
            time.sleep(2)
            sys.exit(0)
            os._exit(1)
        
        else:
            time.sleep(4)
            apvv()

    except Exception as e:
        print(f"{RED} Approval Error: {e}...\n")
        time.sleep(4)
        apvv()

def parse_proxy(proxy_str):
    if '://' not in proxy_str:
        parts = proxy_str.split(':')
        if len(parts) == 4:
            ip, port, user, pwd = parts
            proxy_url = f"http://{user}:{pwd}@{ip}:{port}"
        elif len(parts) == 2:
            ip, port = parts
            proxy_url = f"http://{ip}:{port}"
        else:
            return None
    else:
        proxy_url = proxy_str
    
    return {'http': proxy_url, 'https': proxy_url}

def test_proxy(proxies, server_domain):
    try:
        r = requests.get(f"https://{server_domain}", proxies=proxies, timeout=10)
        return r.status_code == 200
    except:
        return False

COUNTRY_TO_LOCALE = {
    'AD': 'ca_ES', 'AE': 'ar_AR', 'AF': 'fa_IR', 'AG': 'en_US', 'AI': 'en_US', 'AL': 'sq_AL',
    'AM': 'hy_AM', 'AO': 'pt_PT', 'AQ': 'en_US', 'AR': 'es_LA', 'AS': 'en_US', 'AT': 'de_DE',
    'AU': 'en_GB', 'AW': 'nl_NL', 'AX': 'sv_SE', 'AZ': 'az_AZ', 'BA': 'bs_BA', 'BB': 'en_US',
    'BD': 'bn_IN', 'BE': 'nl_BE', 'BF': 'fr_FR', 'BG': 'bg_BG', 'BH': 'ar_AR', 'BI': 'fr_FR',
    'BJ': 'fr_FR', 'BL': 'fr_FR', 'BM': 'en_US', 'BN': 'ms_MY', 'BO': 'es_LA', 'BQ': 'nl_NL',
    'BR': 'pt_BR', 'BS': 'en_US', 'BT': 'dz_BT', 'BV': 'en_GB', 'BW': 'en_GB', 'BY': 'ru_RU',
    'BZ': 'en_US', 'CA': 'en_US', 'CC': 'en_GB', 'CD': 'fr_FR', 'CF': 'fr_FR', 'CG': 'fr_FR',
    'CH': 'de_DE', 'CI': 'fr_FR', 'CK': 'en_US', 'CL': 'es_LA', 'CM': 'fr_FR', 'CN': 'zh_CN',
    'CO': 'es_LA', 'CR': 'es_LA', 'CU': 'es_LA', 'CV': 'pt_PT', 'CW': 'nl_NL', 'CX': 'en_GB',
    'CY': 'el_GR', 'CZ': 'cs_CZ', 'DE': 'de_DE', 'DJ': 'fr_FR', 'DK': 'da_DK', 'DM': 'en_US',
    'DO': 'es_LA', 'DZ': 'ar_AR', 'EC': 'es_LA', 'EE': 'et_EE', 'EG': 'ar_AR', 'EH': 'ar_AR',
    'ER': 'ti_ET', 'ES': 'es_ES', 'ET': 'am_ET', 'FI': 'fi_FI', 'FJ': 'en_US', 'FK': 'en_GB',
    'FM': 'en_US', 'FO': 'da_DK', 'FR': 'fr_FR', 'GA': 'fr_FR', 'GB': 'en_GB', 'GD': 'en_US',
    'GE': 'ka_GE', 'GF': 'fr_FR', 'GG': 'en_GB', 'GH': 'en_GB', 'GI': 'en_GB', 'GL': 'da_DK',
    'GM': 'en_GB', 'GN': 'fr_FR', 'GP': 'fr_FR', 'GQ': 'es_ES', 'GR': 'el_GR', 'GS': 'en_GB',
    'GT': 'es_LA', 'GU': 'en_US', 'GW': 'pt_PT', 'GY': 'en_US', 'HK': 'zh_HK', 'HM': 'en_US',
    'HN': 'es_LA', 'HR': 'hr_HR', 'HT': 'fr_FR', 'HU': 'hu_HU', 'ID': 'id_ID', 'IE': 'en_GB',
    'IL': 'he_IL', 'IM': 'en_GB', 'IN': 'hi_IN', 'IO': 'en_GB', 'IQ': 'ar_AR', 'IR': 'fa_IR',
    'IS': 'is_IS', 'IT': 'it_IT', 'JE': 'en_GB', 'JM': 'en_US', 'JO': 'ar_AR', 'JP': 'ja_JP',
    'KE': 'en_GB', 'KG': 'ru_RU', 'KH': 'km_KH', 'KI': 'en_US', 'KM': 'fr_FR', 'KN': 'en_US',
    'KP': 'ko_KR', 'KR': 'ko_KR', 'KW': 'ar_AR', 'KY': 'en_US', 'KZ': 'ru_RU', 'LA': 'lo_LA',
    'LB': 'ar_AR', 'LC': 'en_US', 'LI': 'de_DE', 'LK': 'si_LK', 'LR': 'en_US', 'LS': 'en_GB',
    'LT': 'lt_LT', 'LU': 'fr_FR', 'LV': 'lv_LV', 'LY': 'ar_AR', 'MA': 'ar_AR', 'MC': 'fr_FR',
    'MD': 'ro_RO', 'ME': 'sr_RS', 'MF': 'fr_FR', 'MG': 'fr_FR', 'MH': 'en_US', 'MK': 'mk_MK',
    'ML': 'fr_FR', 'MM': 'my_MM', 'MN': 'mn_MN', 'MO': 'zh_TW', 'MP': 'en_US', 'MQ': 'fr_FR',
    'MR': 'ar_AR', 'MS': 'en_US', 'MT': 'en_GB', 'MU': 'en_GB', 'MV': 'dv_MV', 'MW': 'en_GB',
    'MX': 'es_MX', 'MY': 'ms_MY', 'MZ': 'pt_PT', 'NA': 'en_GB', 'NC': 'fr_FR', 'NE': 'fr_FR',
    'NF': 'en_GB', 'NG': 'en_GB', 'NI': 'es_LA', 'NL': 'nl_NL', 'NO': 'nb_NO', 'NP': 'ne_NP',
    'NR': 'en_US', 'NU': 'en_US', 'NZ': 'en_GB', 'OM': 'ar_AR', 'PA': 'es_LA', 'PE': 'es_LA',
    'PF': 'fr_FR', 'PG': 'en_US', 'PH': 'tl_PH', 'PK': 'ur_PK', 'PL': 'pl_PL', 'PM': 'fr_FR',
    'PN': 'en_GB', 'PR': 'es_LA', 'PS': 'ar_AR', 'PT': 'pt_PT', 'PW': 'en_US', 'PY': 'es_LA',
    'QA': 'ar_AR', 'RE': 'fr_FR', 'RO': 'ro_RO', 'RS': 'sr_RS', 'RU': 'ru_RU', 'RW': 'fr_FR',
    'SA': 'ar_AR', 'SB': 'en_US', 'SC': 'fr_FR', 'SD': 'ar_AR', 'SE': 'sv_SE', 'SG': 'en_GB',
    'SH': 'en_GB', 'SI': 'sl_SI', 'SJ': 'nb_NO', 'SK': 'sk_SK', 'SL': 'en_GB', 'SM': 'it_IT',
    'SN': 'fr_FR', 'SO': 'so_SO', 'SR': 'nl_NL', 'SS': 'en_GB', 'ST': 'pt_PT', 'SV': 'es_LA',
    'SX': 'nl_NL', 'SY': 'ar_AR', 'SZ': 'en_GB', 'TC': 'en_US', 'TD': 'fr_FR', 'TF': 'fr_FR',
    'TG': 'fr_FR', 'TH': 'th_TH', 'TJ': 'tg_TJ', 'TK': 'en_US', 'TL': 'pt_PT', 'TM': 'ru_RU',
    'TN': 'ar_AR', 'TO': 'en_US', 'TR': 'tr_TR', 'TT': 'en_US', 'TV': 'en_US', 'TW': 'zh_TW',
    'TZ': 'sw_KE', 'UA': 'uk_UA', 'UG': 'en_GB', 'UM': 'en_US', 'US': 'en_US', 'UY': 'es_LA',
    'UZ': 'uz_UZ', 'VA': 'it_IT', 'VC': 'en_US', 'VE': 'es_LA', 'VG': 'en_GB', 'VI': 'en_US',
    'VN': 'vi_VN', 'VU': 'en_US', 'WF': 'fr_FR', 'WS': 'en_US', 'YE': 'ar_AR', 'YT': 'fr_FR',
    'ZA': 'en_GB', 'ZM': 'en_GB', 'ZW': 'en_GB'
}

def get_locale_code(country_code):
    return COUNTRY_TO_LOCALE.get(country_code.upper(), 'en_US')

def get_ip_info(proxies=None):
    try:
        r = requests.get("http://ip-api.com/json/", proxies=proxies, timeout=10)
        if r.status_code == 200:
            data = r.json()
            return {
                'country': data.get('country', 'Unknown'),
                'countryCode': data.get('countryCode', 'US'),
                'timezone': data.get('timezone', 'Unknown')
            }
    except:
        pass
    return {'country': 'Unknown', 'countryCode': 'US', 'timezone': 'Unknown'}

def load_settings():
    try:
        # Try to load from sdcard first
        if os.path.exists(SETTINGS_PATH):
            with open(SETTINGS_PATH, 'r') as f:
                return json.load(f)
        # Fallback to current directory
        elif os.path.exists('Setting.json'):
            with open('Setting.json', 'r') as f:
                return json.load(f)
        else:
            return {}
    except:
        return {}

def get_status_line():
    return f"\r{GREEN}[{WHITE}Mr-SxR{GREEN}] {WHITE}CHECKED:-{total_checked}{CYAN}|{GREEN}SUCCESS:-{total_success}{CYAN}|{YELLOW}FAILED:-{total_failed}{CYAN}|{RED}ERROR:-{total_error}"

def safe_print(text):
    with print_lock:
        sys.stdout.write('\r                                                                                \r')
        try:
            sys.stdout.write(str(text) + '\n')
        except UnicodeEncodeError:
            sys.stdout.write(str(text).encode('utf-8', 'ignore').decode('utf-8') + '\n')
        sys.stdout.write(get_status_line())
        sys.stdout.flush()

def update_counter(status, number=None, message=None, color=None, html_content=None):
    global total_success, total_failed, total_error, total_checked
    
    with counter_lock:
        if status == 'success':
            total_success += 1
        elif status == 'failed':
            total_failed += 1
        elif status == 'error':
            total_error += 1
            if html_content:
                save_error_html(message if message else "Unknown Error", html_content)
        
        total_checked += 1
    
    if message and number:
        if not color: color = WHITE
        safe_print(f"{color} {message} {number}")
        return
    
    if message:
        if not color: color = WHITE
        safe_print(f"{color} {message}")
        return

    with print_lock:
        sys.stdout.write(get_status_line())
        sys.stdout.flush()

SAVE_ERROR_LOGS = 'off'

def reset_counters():
    global total_checked, total_success, total_failed, total_error
    total_checked = 0
    total_success = 0
    total_failed = 0
    total_error = 0

def save_error_html(message, html_content):
    if SAVE_ERROR_LOGS.lower() != 'on':
        return

    try:
        if not os.path.exists(ERROR_LOGS_DIR):
            os.makedirs(ERROR_LOGS_DIR)
            
        safe_msg = re.sub(r'[\\/*?:"<>|]', '', message)
        safe_msg = safe_msg.replace(' ', '_')
        safe_msg = safe_msg[:50]
        
        base_filename = f"{ERROR_LOGS_DIR}/{safe_msg}.html"
        filename = base_filename
        counter = 1
        
        while os.path.exists(filename):
            filename = f"{ERROR_LOGS_DIR}/{safe_msg}_{counter}.html"
            counter += 1
            
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"<!-- Error: {message} -->\n")
            f.write(html_content)
    except Exception as e:
        safe_print(f"{RED} Failed to save error log: {e}")

def clear_logo():
    os.system('clear')
        
    print(''.join([GREEN, "\n      .d8888.  db    db  d8888b. \n      88'  YP  `8b  d8'  88  `8D \n      `8bo.     `8bd8'   88oobY' \n        `Y8b.   .dPYb.   88`8b   \n      db   8D  .8P  Y8.  88 `88. \n      `8888Y'  YP    YP  88   YD   ", ORANGE, 'V-3.6\n', LINE, '\n ', GREEN, '[', RED, '●', GREEN, '] TOOL OWNER   ', CYAN, ':', GREEN, ' @yeasin_hossain018\n ', GREEN, '[', RED, '●', GREEN, '] TOOL         ', CYAN, ':', GREEN, ' FORGET FB\n ', GREEN, '[', RED, '●', GREEN, '] TOOL STATUS  ', CYAN, ':', GREEN, ' PAID\n', LINE]))

def sxr_main():
    clear_logo()
    print(f" {GREEN}UserName {EKL} {user_nm}\n {RED}Expired {EKL} {expr} (Utc)\n{LINE}")
    print(f" {opt_labels[0]} FB FORGET\n {opt_labels[1]} NUMBER FILTER\n {opt_labels[2]} CONFIRM ACCOUNT\n {opt_labels[3]} JOIN TELEGRAM\n{LINE}")
    
    chic_opsn = input(f"{GREEN} [{RED}●{GREEN}] CHOOSE OPTION {EKL} ")
    
    if chic_opsn in ('1', '01', 'A', 'a'):
        file_inp()
        return
    elif chic_opsn in ('2', '02', 'B', 'b'):
        print(f"{RED} Windows .exe files cannot run on Termux.")
        print(f"{WHITE} Please use the text file option instead.")
        time.sleep(2)
        sxr_main()
        return
    elif chic_opsn in ('3', '03', 'C', 'c'):
        print(f"{RED} Windows .exe files cannot run on Termux.")
        print(f"{WHITE} Please use the text file option instead.")
        time.sleep(2)
        sxr_main()
        return
    elif chic_opsn in ('4', '04', 'D', 'd'):
        webbrowser.open('https://t.me/mrsxrtools')
        return
    else:
        print(f"\n{RED} You have selected the wrong option..")
        time.sleep(3)
        sxr_main()
        return

def file_inp():
    clear_logo()
    
    print(f"{CYAN} Looking for Number_List.txt in SD Card...")
    
    # Check if sdcard is accessible
    if not os.path.exists(SDCARD_PATH):
        print(f"{RED} SD Card not accessible!")
        print(f"{YELLOW} Make sure Termux has storage permission:")
        print(f"{WHITE} 1. Run: termux-setup-storage")
        print(f"{WHITE} 2. Grant permission when prompted")
        input(f"{WHITE} Press Enter to continue...")
        sxr_main()
        return
    
    # Check for Number_List.txt in sdcard
    if os.path.exists(NUMBER_LIST_PATH):
        try:
            with open(NUMBER_LIST_PATH, 'r', encoding='utf-8', errors='ignore') as f:
                numbers = [line.strip() for line in f if line.strip()]
            
            if numbers:
                print(f"{GREEN} [{RED}●{GREEN}] Found File {EKL} {NUMBER_LIST_PATH}")
                print(f"{GREEN} [{RED}●{GREEN}] Total Numbers {EKL} {len(numbers)}")
                input(f"{WHITE} Press Enter to Start Forgetting {len(numbers)} Numbers...")
                autom_main()
                return
            else:
                print(f"{WHITE} 'Number_List.txt' file is empty.")
                print(f"{WHITE} Please add phone numbers to {NUMBER_LIST_PATH}")
                input(f"{WHITE} Press Enter to return to main menu...")
                sxr_main()
                return
        except Exception as e:
            print(f"{RED} Error reading file: {e}")
            input(f"{WHITE} Press Enter to return...")
            sxr_main()
            return
    else:
        print(f"{YELLOW} File not found: {NUMBER_LIST_PATH}")
        print(f"{WHITE} Please create 'Number_List.txt' in your SD Card")
        print(f"{WHITE} with phone numbers (one per line)")
        print(f"{CYAN} Example location: /sdcard/Number_List.txt")
        input(f"{WHITE} Press Enter to return to main menu...")
        sxr_main()
        return

def get_proxy_list(settings_key, prompt_label):
    settings = load_settings()
    proxy_set = settings.get(settings_key, {})
    ask_proxy = proxy_set.get('ask_for_proxy', True)
    def_proxy = proxy_set.get('default_proxy', '')
    
    server_set = settings.get('server_settings', {})
    server_id = server_set.get('tools_server_id', 1)
    server_domain = SERVER_MAP.get(server_id, 'm.facebook.com')
    
    ask_proxy_final = ask_proxy
    PROXY_LIST = []
    
    if def_proxy:
        if isinstance(def_proxy, list):
            print(f"{WHITE} Testing {len(def_proxy)} Default {prompt_label}...")
            for p in def_proxy:
                parsed = parse_proxy(p)
                if parsed and test_proxy(parsed, server_domain):
                    nfo = get_ip_info(parsed)
                    loc = get_locale_code(nfo['countryCode'])
                    PROXY_LIST.append({'proxy': parsed, 'locale': loc, 'country': nfo['country']})
                    print(f"{GREEN} [{RED}●{GREEN}] {prompt_label} Location {EKL} {nfo['country']}")
                    print(f"{GREEN} [{RED}●{GREEN}] Locale      {EKL} {loc}")
                else:
                    print(f"{RED} Default {prompt_label} Connection Failed: {p}")
        else:
            parsed_proxies = parse_proxy(def_proxy)
            if parsed_proxies:
                print(f"{WHITE} Testing Default {prompt_label}...")
                if test_proxy(parsed_proxies, server_domain):
                    nfo = get_ip_info(parsed_proxies)
                    loc = get_locale_code(nfo['countryCode'])
                    PROXY_LIST.append({'proxy': parsed_proxies, 'locale': loc, 'country': nfo['country']})
                    print(f"{GREEN} [{RED}●{GREEN}] {prompt_label} Location {EKL} {nfo['country']}")
                    print(f"{GREEN} [{RED}●{GREEN}] Locale      {EKL} {loc}")
                else:
                    print(f"{RED} Default {prompt_label} Connection Failed!")
            else:
                print(f"{RED} Invalid Default {prompt_label} Format!")
                
        if def_proxy and not PROXY_LIST:
            print(f"{RED} All Default {prompt_label} Failed!")
            ask_proxy_final = True
            
    if PROXY_LIST and ask_proxy:
        ask_proxy_final = False
        
    if ask_proxy_final:
        while True:
            try:
                proxy_input = input(f"{GREEN} [{RED}●{GREEN}] Enter {prompt_label} (or 'y' for multiple) [Enter to Skip] {EKL} ").strip()
                if proxy_input.lower() == 'y':
                    cnt_in = input(f"{GREEN} [{RED}●{GREEN}] How many {prompt_label}? {EKL} ")
                    if cnt_in.strip():
                        cnt = int(cnt_in)
                        for i in range(cnt):
                            p_in = input(f"{WHITE} [{RED}●{WHITE}] Enter {prompt_label} [{i+1}/{cnt}] {EKL} ").strip()
                            if p_in:
                                print(f"{WHITE} Testing {prompt_label}...")
                                parsed = parse_proxy(p_in)
                                if parsed and test_proxy(parsed, server_domain):
                                    nfo = get_ip_info(parsed)
                                    loc = get_locale_code(nfo['countryCode'])
                                    print(f"{GREEN} [{RED}●{GREEN}] {prompt_label} Location {EKL} {nfo['country']}")
                                    print(f"{GREEN} [{RED}●{GREEN}] Locale      {EKL} {loc}")
                                    PROXY_LIST.append({'proxy': parsed, 'locale': loc, 'country': nfo['country']})
                                else:
                                    print(f"{RED} Connection Failed or Invalid Format!")
                        break
                    else:
                        print(f"{RED} Invalid Number!")
                        break

                if proxy_input:
                    parsed_proxies = parse_proxy(proxy_input)
                    if parsed_proxies:
                        print(f"{WHITE} Testing {prompt_label}...")
                        if test_proxy(parsed_proxies, server_domain):
                            nfo = get_ip_info(parsed_proxies)
                            loc = get_locale_code(nfo['countryCode'])
                            print(f"{GREEN} [{RED}●{GREEN}] {prompt_label} Location {EKL} {nfo['country']}")
                            print(f"{GREEN} [{RED}●{GREEN}] Locale      {EKL} {loc}")
                            PROXY_LIST.append({'proxy': parsed_proxies, 'locale': loc, 'country': nfo['country']})
                            break
                        else:
                            print(f"{RED} {prompt_label} Connection Failed!")
                    else:
                        print(f"{RED} Invalid {prompt_label} Format!")
                
                if PROXY_LIST or not ask_proxy_final:
                    break
                    
            except:
                print(f"{RED} Invalid Input")
                
    return PROXY_LIST

def autom_main():
    while True:
        clear_logo()
        try:
            # Read from sdcard
            with open(NUMBER_LIST_PATH, 'r', encoding='utf-8', errors='ignore') as f:
                numbers = [line.strip() for line in f if line.strip()]
            
            if not numbers:
                print(f"{RED} No numbers found in {NUMBER_LIST_PATH}")
                print(f"{WHITE} Please add phone numbers to the file")
                input(f"{WHITE} Press Enter to return...")
                sxr_main()
                return
            break
        except Exception as e:
            print(f"{RED} Error reading file {EKL} {e}")
            input(f"{WHITE} Press Enter to return...")
            sxr_main()
            return

    settings = load_settings()
    server_set = settings.get('server_settings', {})
    server_id = server_set.get('tools_server_id', 1)
    server_domain = SERVER_MAP.get(server_id, 'm.facebook.com')

    print(f"{WHITE} Setting up Main Proxy System...")
    PROXY_LIST = get_proxy_list('proxy_settings', 'Main Proxy')
    
    PROXY_ITERATOR = itertools.cycle(PROXY_LIST) if PROXY_LIST else None
    
    if
