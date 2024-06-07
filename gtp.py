import random

# Define possible values for each part of the User-Agent string
fban_fb4a = ['FBAN/FB4A']
fbav = ['FBAV/' + str(random.randint(11, 99)) + '.0.0.' + str(random.randint(1111, 9999))]
fbbv = ['FBBV/' + str(random.randint(1111111, 9999999))]
fbdm = ['FBDM/{density=1.75,width=720,height=1515}', 'FBDM/{density=1.75,width=720,height=1478}', 'FBDM/{density=1.75,width=720,height=1421}', 'FBDM/{density=2.5,width=1080,height=2224}', 'FBDM/{density=2.7875001,width=1080,height=2165}', 'FBDM/{density=1.5,width=480,height=854}']
fblc = ['FBLC/en_US', 'FBLC/es_LA']
fbrv = ['FBRV/541211947', 'FBRV/0', 'FBRV/537275962', 'FBRV/478477801']
fbcr = ['FBCR/MTNSA TheGoodStuff', 'FBCR/Home', 'FBCR/Metro by T-Mobile', 'FBCR/Etisalat NG']
fbmf = ['FBMF/HMD Global', 'FBMF/TECNO']
fbbd = ['FBBD/Nokia', 'FBBD/N151DL', 'FBBD/N156DL', 'FBBD/Nokia G400 5G', 'FBBD/Nokia X100', 'FBBD/TECNO']
fbpn = ['FBPN/com.facebook.katana']
fbdv = ['FBDV/Nokia G10', 'FBDV/N151DL', 'FBDV/N156DL', 'FBDV/Nokia G400 5G', 'FBDV/Nokia X100', 'FBDV/TECNO-W3']
fbsv = ['FBSV/13', 'FBSV/12', 'FBSV/11', 'FBSV/6.0']
fbop = ['FBOP/1', 'FBOP/19']
fbca = ['FBCA/arm64-v8a:', 'FBCA/armeabi-v7a:armeabi;']

# Assemble the User-Agent string
user_agent = ';'.join(random.choice(part) for part in [fban_fb4a, fbav, fbbv, fban_fb4a, fbav, fbbv, fbdm, fblc, fbrv, fbcr, fbmf, fbbd, fbpn, fbdv, fbsv, fbop, fbca])

print(user_agent)
