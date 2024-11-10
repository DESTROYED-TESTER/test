import random

def UBI_():
    application_version = str(random.randint(111, 555)) + '.0.0.' + str(random.randrange(9, 49)) + str(random.randint(111, 555))
    application_version_code = str(random.randint(000000000, 999999999))
    android_version = str(random.randrange(6, 13))
    numbr = f'{random.randint(111111, 999999)}.{random.randint(111, 999)}'
    build = random.choice([
        "SP1A.", "TP2A.", "SP1A.", "SP1A.", "TP1A.", "TP1A.", "SP1A.", "TP1A.", 
        "RKQ1.", "TP1A.", "TP1A.", "RP1A.", "RP1A.", "RKQ1.", "TQ3A.", "TD2A.", 
        "TD4A.", "TQ3A.", "TP1A.", "TP1A.", "SP2A.", "SD2A.", "SQ3A.", "RD2A.", 
        "RQ3A.", "RP1A.", "QD4A.", "QQ3A.", "QP1A.", "PQ3B.", "PD2A.", "PPR2.", 
        "PPR1.", "OPM8.", "OPR6."
    ])
    fbs = random.choice([
        "com.facebook.adsmanager", "com.facebook.lite", "com.facebook.orca", 
        "com.facebook.katana", "com.facebook.mlite"
    ])
    
    user_agents = [
        f'Davik/2.1.0 (Linux; U; Android {android_version}.0.0; Oppo J793V Build/{build}{numbr}) [FBAN/FB4A;FBAV/{application_version};FBBV/{application_version_code};FBRV/{application_version_code};FBPN/{fbs};FBLC/en_US;FBMF/Oppo;FBBD/Oppo;FBDV/Oppo J793V;FBSV/9;FBCA/armeabi-v7a:armeabi;FBDM={{density=2.0,width=720,height=1440}};FB_FW/1;]',
        f'Davik/2.1.0 (Linux; U; Android {android_version}.0.0; ASUS_X00RD Build/{build}{numbr}) [FBAN/FB4A;FBAV/{application_version};FBBV/{application_version_code};FBDM={{density=2.0,width=720,height=1352}};FBLC/en_US;FBRV/{application_version_code};FBCR/banglalink;FBMF/asus;FBBD/asus;FBPN/{fbs};FBDV/ASUS_X00RD;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]',
        f'Davik/2.1.0 (Linux; U; Android {android_version}.0.0; moto z4 Build/{build}{numbr}) [FBAN/FB4A;FBAV/{application_version};FBBV/{application_version_code};FBDM={{density=3.0,width=1080,height=2120}};FBLC/en_US;FBRV/{application_version_code};FBCR/Verizon;FBMF/motorola;FBBD/motorola;FBPN/{fbs};FBDV/moto z4;FBSV/9;FBOP/1;FBCA/arm64-v8a;]',
        f'Davik/2.1.0 (Linux; U; Android {android_version}.0.0; motorola one macro Build/{build}{numbr}) [FBAN/FB4A;FBAV/{application_version};FBBV/{application_version_code};FBDM={{density=2.25,width=720,height=1393}};FBLC/en_US;FBRV/{application_version_code};FBCR/AT&FBMF/motorola;FBBD/motorola;FBPN/{fbs};FBDV/motorola one macro;FBSV/9;FBOP/1;FBCA/arm64-v8a;]',
        f'Davik/2.1.0 (Linux; U; Android {android_version}.0.0; SM-G973U Build/{build}{numbr}) [FBAN/FB4A;FBAV/{application_version};FBBV/{application_version_code};FBDM={{density=3.0,width=1080,height=2024}};FBLC/en_US;FBRV/{application_version_code};FBCR/Sprint;FBMF/samsung;FBBD/samsung;FBPN/{fbs};FBDV/SM-G973U;FBSV/10;FBOP/19;FBCA/arm64-v8a;]',
        f'Davik/2.1.0 (Linux; U; Android {android_version}.0.0; motorola one macro Build/{build}{numbr}) [FBAN/FB4A;FBAV/{application_version};FBBV/{application_version_code};FBDM={{density=2.25,width=720,height=1393}};FBLC/en_US;FBRV/{application_version_code};FBCR/grameenphone;FBMF/motorola;FBBD/motorola;FBPN/{fbs};FBDV/motorola one macro;FBSV/9;FBOP/1;FBCA/arm64-v8a;]',
        f'Davik/2.1.0 (Linux; U; Android {android_version}.0.0; HUAWEI VNS-L21 Build/{build}{numbr}) [FBAN/FB4A;FBAV/{application_version};FBBV/{application_version_code};FBDM={{density=3.0,width=1080,height=1812}};FBLC/en_US;FBRV/{application_version_code};FBCR/Vodafone UA;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/{fbs};FBDV/HUAWEI VNS-L21;FBSV/7.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]',
        f'Davik/2.1.0 (Linux; U; Android {android_version}.0.0; PRA-LX1 Build/{build}{numbr}) [FBAN/FB4A;FBAV/{application_version};FBBV/{application_version_code};FBDM={{density=3.0,width=1080,height=1794}};FBLC/en_US;FBRV/{application_version_code};FBCR/AT&FBMF/HUAWEI;FBBD/HUAWEI;FBPN/{fbs};FBDV/PRA-LX1;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]',
        f'Davik/2.1.0 (Linux; U; Android {android_version}.0.0; GREEN 2020 Build/{build}{numbr}) [FBAN/FB4A;FBAV/{application_version};FBBV/{application_version_code};FBDM={{density=2.0,width=720,height=1456}};FBLC/en_US;FBRV/{application_version_code};FBCR/robi;FBMF/Green;FBBD/Green;FBPN/{fbs};FBDV/GREEN 2020;FBSV/11;FBOP/1;FBCA/arm64-v8a;]'
    ]
    
    return random.choice(user_agents)

# Call the function and print a random user agent
print(UBI_())
