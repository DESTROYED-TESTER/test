import random

def UBI_():
    application_version = str(random.randint(111, 555)) + '.0.0.' + str(random.randrange(9, 49)) + str(random.randint(111, 555))
    application_version_code = str(random.randint(000000000, 999999999))
    android_version = str(random.randrange(6, 13))
    numbr = f'{random.randint(111111, 999999)}.{random.randint(111, 999)}'
    fbs = random.choice([
        "com.facebook.adsmanager", "com.facebook.lite", "com.facebook.orca", 
        "com.facebook.katana", "com.facebook.mlite"
    ])
    
    user_agents = [
        f'Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-A720F Build/R16NW) [FBAN/Orca-Android;FBAV/{application_version};FBPN/com.facebook.orca;FBLC/th_TH;FBBV/{application_version_code};FBCR/AIS;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{{density=3.0,width=1080,height=1920};FB_FW/1;]',
    ]
    
    return random.choice(user_agents)

# Call the function and print a random user agent
print(UBI_())
