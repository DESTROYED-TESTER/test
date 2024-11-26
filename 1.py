#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ FULL SCRIPT ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
#Gift script :- https://t.me/KGF_TERMUX_TEAMl 
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ IMPORT MODULES ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
import os, sys, re, requests, bs4, time, random, json, string
from bs4 import BeautifulSoup
from datetime import datetime
try:
    import requests
except ImportError:
    os.system('pip install requests > /dev/null')
try:
    import bs4
except ImportError:
    print ('\n [×] Modul Bs4 Not installed!...\n')
    os.system('pip install bs4')
def convert(cok):
    __for = 'datr=' + cok['datr'] + ';' + ('sb=' + cok['sb']) + ';' + ('fr=' + cok['fr']) + ';' + ('c_user=' + cok['c_user']) + ';' + ('xs=' + cok['xs'])
    return __for
def inbox(session):
    time.sleep(1)
    ses = requests.Session()
    __ = str(time.time()).replace('.', '')[:13]
    data = ses.get(f"https://10minutemail.net/address.api.php?sessionid={session}&_={str(__)}").json()
    if len(data["mail_list"]) !=1:
        address = data["mail_list"][0]["subject"]
        session = address.replace('FB-', '').replace('is your Facebook confirmation code', '')
        return session
ugen=[]
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ UA ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
for x in range(5000):
    aa='Mozilla/5.0 (Linux; Android'
    b=random.choice(['6','7','8','9','10','11','12'])
    c='K)'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ LINEX ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
def clear():os.system('clear')
def linex():print(f'{R}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ COLOUR ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
BU= '\033[1;34m';A = '\x1b[1;97m';R = '\x1b[38;5;196m';Y = '\033[1;33m';G = '\x1b[38;5;46m';B = '\x1b[38;5;46m';G1 = '\x1b[38;5;48m';G2 = '\x1b[38;5;47m';G3 = '\x1b[38;5;48m';G4 = '\x1b[38;5;49m';G5 = '\x1b[38;5;50m';X = '\33[1;34m';X1 = '\x1b[38;5;14m';X2 = '\x1b[38;5;123m';X3 = '\x1b[38;5;122m';X4 = '\x1b[38;5;86m';X5 = '\x1b[38;5;121m';S = '\x1b[1;96m';M = '\x1b[38;5;205m'
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ LOGO ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ NAME ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
boy = ["Ashraful ahmed","Arif Rahman","Asif Ahmed","Bashir Chowdhury","Binod Sarker","Rafiq Miah","Mohammad Khan","Mahmud Ali","Mahin Islam","Masud Hossain","Mustafa Uddin","Mohiuddin Bhuiyan","Noor Khan","Nasir Ahmed","Nurul Haque","Rajib Siddique","Rezaul Islam","Riyad Rahman","Sabbir Mia","Sadik Chowdhury","Samsuddin Mollah","Selim Sarker","Shahid Hossain","Shafik Ahmed","Shams Uddin","Shahin Alam","Tanveer Khan","Touhid Hossain","Iqbal Rahman","Jafar Mia","Jewel Siddique","Ziaur Islam"]
girl = ["Ayesha Sultana","Momena Begum","Rokeya Sultana","Fatema Anwar","Sultana Kamal","Jahanara Alam","Ruma Akter","Farzana Yasmin","Salma Begum","Nusrat Jahan","Shaheen Akter","Sabrina Sultana","Purnima Roy","Shirin Akter","Jannatul Ferdous","Mousumi Parveen","Rina Begum","Laila Islam","Rubina Sultana","Nigar Sultana","Shamima Nasrin","Dilruba Sultana","Khatun Begum","Fariha Rahman","Kazi Rupa","Mariam Begum","Selina Akter","Nabila Rahman","Sadia Islam","Rumana Akter","Sumi Akter","Hena Sultana"]
ok = []
cp = []
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ MENU ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
class create:	
    def __init__(self):
        self.loop = 0
        self.gender = []
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ SEIF ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#        
    def start(self):
        os.system('clear')
        linex()
        namee = input(f'{A}[{R}={A}] Masukan Nama Depan Dan Belakang :{G} ')
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ EXAMPLE ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
        palxd = input(f'{A}[{R}={A}] Masukan Password Untuk Akun :{G} ')
        xxnd = input(f'{A}[{R}={A}] Hasil Akun Di simpan Di mna CONTOH (/sdcard/xxnx.txt) :{G} ')
        lim = 5000
        os.system('clear')
        agent = random.choice(ugen)
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ FULL METHOD ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#        
        headers = {
            'authority': 'm.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
            'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"11.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': agent,
            'viewport-width': '980',}
        headers1 = {
            'authority': 'm.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
            'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"11.0.0"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'upgrade-insecure-requests': '1',
            'user-agent': agent,}
        OO = '\033[0;97m'
        for x in range(lim):
            self.loop += 1
            sys.stdout.write(f'\r\r{A}[{G}RUNNING{A}] >> {A}[{R}{self.loop}{A}]{R} >> {A}[{G}OK{A}•{G}{len(ok)}{A}]')
            sys.stdout.flush()
            try:
                ses = requests.Session()
                buildses = user = "".join(random.SystemRandom().choice("qwertyuiopasdfghjklzxcvbnm0987654321") for i in range(26))
                create = ses.get(f"https://10minutemail.net/address.api.php?new=1&sessionid={buildses}&_={int(datetime.now().timestamp() * 1000)}").json()
                mail = {"mail": create["permalink"]["mail"], "session": create["session_id"]}
                email = mail['mail']
                session = mail['session']
                ttl_tgl = str(random.randrange(1,29))
                ttl_bln = str(random.randrange(1,13))
                ttl_thn = str(random.randrange(1970,2001))
            except KeyError:
                pass
            except requests.exceptions.ConnectionError:
                time.sleep(1)
                pass
            except Exception as e:
                pass
            #passw = name[0]+name[1]+str(random.randint(111,999))
            passw = palxd
            name = namee
            try:
                self.ses = requests.Session()
                a = self.ses.get('https://m.facebook.com/reg?_fb_noscript', headers=headers)
                loger = re.search('name="logger_id" value="(.*?)"', str(a.text)).group(1)
                ref = BeautifulSoup(a.text, 'html.parser').find('form', {'action': True, "id":"mobile-reg-form", "method":"post"})
                bl = ['lsd', 'jazoest', 'cpp', 'reg_instance', 'submission_request']
                bz = ['reg_impression_id', 'ns']
                self.data = {}
                for v in ref('input'):
                    if v.get('name') in bl:
                        try:
                            self.data.update({v.get('name'):v.get('value')})
                        except:
                            pass
                self.data.update({'helper': ''})
                for v in ref('input'):
                    if v.get('name') in bz:
                        try:
                            self.data.update({v.get('name'):v.get('value')})
                        except:
                            pass
                self.data.update({
                    "zero_header_af_client": "",
                    "app_id": "103",
                    "logger_id": re.search('name="logger_id" value="(.*?)"', str(a.text)).group(1),
                    "field_names[0]": "firstname",
                    "firstname": name,
                    "field_names[1]": "birthday_wrapper",
                    "birthday_day": ttl_tgl,
                    "birthday_month": ttl_bln,
                    "birthday_year": ttl_thn,
                    "age_step_input": "",
                    "did_use_age": "",
                    "field_names[2]": "reg_email__",
                    "reg_email__": email,
                    "field_names[3]": "sex",
                    "sex": '1',
                    "preferred_pronoun": "",
                    "custom_gender": "",
                    "field_names[]": "reg_passwd__",
                    "reg_passwd__": passw,
                    "submit": "Sign Up",
                    "name_suggest_elig": "false",
                    "was_shown_name_suggestions": "false",
                    "did_use_suggested_name": "false",
                    "use_custom_gender": "",
                    "guid": "",
                    "pre_form_step": "",})
                gett = self.ses.post('https://m.facebook.com'+ref['action'], headers=headers1, data=self.data)
                getts = self.ses.get('https://m.facebook.com/login/save-device/?login_source=account_creation&logger_id='+loger+'&app_id=103', headers=headers1)
                data1 = {}
                data2 = {}
                data3 = {}
                cok = self.ses.cookies.get_dict()
                if 'checkpoint' in getts.url:
                    cp.append(email+passw)
                dbl = ['fb_dtsg', 'jazoest', 'flow', 'next', 'nux_source']
                for x in BeautifulSoup(getts.text, 'html.parser').find_all('form', {'method': 'post'}):
                    if '/login/device-based/update-nonce/' in str(x):
                        for v in x('input'):
                            if v.get('name') in dbl:
                                try:
                                    data1.update({v.get('name'):v.get('value')})
                                except:
                                    pass
                        data1.update({'submit': 'OK'})
                        po = self.ses.post('https://m.facebook.com'+x.get('action'), headers=headers1, data=data1)
                        for x in BeautifulSoup(po.text, 'html.parser').find_all('form', {'method': 'post'}):
                            if 'confirmation_event_location=cliff' in str(x):
                                for v in x('input'):
                                    if v.get('name') in dbl:
                                        try:
                                            data2.update({v.get('name'):v.get('value')})
                                        except:
                                            pass
                                code = inbox(session)
                                data2.update({'c': code, 'submit': 'Confirm'})
                                rex = self.ses.post('https://m.facebook.com'+x.get('action'), headers=headers1, data=data2)
                                if 'checkpoint' in rex.url:
                                    cok = self.ses.cookies.get_dict()
                                    print(f'\r{Y} CP '+cok['c_user']+' | '+passw+'')
                                    cp.append(email+passw)
                                else:
                                    coki = (";").join([ "%s=%s" % (key, value) for key, value in self.ses.cookies.get_dict().items() ])
                                    cok = self.ses.cookies.get_dict()
                                    print(f'\r{G} OK '+cok['c_user']+' | '+passw+'')
                                    print(f'\r{R}[{G}COOKIE{R}]{G}━{R}>{BU} '+coki)
                                    linex()
                                    open("/sdcard/"+xxnd+"","a").write(cok['c_user']+"|"+passw+"|"+coki+"\n")
                                    ok.append(email+passw)
            except requests.exceptions.ConnectionError:
                pass
            except Exception as e:
                pass
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ CRACKED ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#                
        print ('')
        linex()
        print (f'{A}[{R}={A}] {G}TOTAL OK ID {R}:{G} '+str(len(ok)))
        print (f'{A}[{R}={A}] {G}TOTAL CP ID {R}: '+str(len(cp)))
        linex()
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ EXIT ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#        
create().start()
