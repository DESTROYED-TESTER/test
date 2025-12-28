import hashlib
import uuid
import time
import requests
import random
import urllib.parse
username = '8918224528'
passwd = '891822'
useragent = 'Mozilla/5.0 (Linux; Android 12; SKY PAD10 Build/S00812; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/141.0.7390.122 Safari/537.36 Instagram 406.0.0.58.159 Android (31/12; 200dpi; 1280x740; Sky Devices/SKY; SKY PAD10; SKY_PAD10; ums312_2h10; en_US; 822917963; IABMV/1)'
## Create an MD5 hash for the username and password
session = requests.Session()
hash = hashlib.md5()
hash.update(username.encode('utf-8') + passwd.encode('utf-8'))
hex = hash.hexdigest()
    ## Further update the hash with the hex value and a static string
hash.update(hex.encode('utf-8') + '12345'.encode('utf-8'))

    ## Construct HTTP headers for the Instagram request
headers = {
'host': 'i.instagram.com',
'x-ig-app-locale': 'in_ID',
'x-ig-device-locale': 'in_ID',
'x-ig-mapped-locale': 'id_ID',
'x-pigeon-session-id': f'UFS-{str(uuid.uuid4())}-3',
'x-pigeon-rawclienttime': '{:.3f}'.format(time.time()),
'x-bloks-version-id': 'c55a52bd095e76d9a88e2142eaaaf567c093da6c0c7802e7a2f101603d8a7d49',
'x-ig-www-claim': '0',
'x-bloks-is-prism-enabled': 'false',
'x-bloks-is-layout-rtl': 'false',
'x-ig-device-id': str(uuid.uuid4()),
'x-ig-family-device-id': str(uuid.uuid4()),
'x-ig-android-id': f'android-{hash.hexdigest()[:16]}',
'x-fb-connection-type': 'MOBILE.LTE',
'x-ig-connection-type': 'MOBILE(LTE)',
'x-ig-capabilities': '3brTv10=',
'priority': 'u=3',
'user-agent': useragent,
'accept-language': 'id-ID, en-US',
'x-mid': '',
'ig-intended-user-id': '0',
'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
'x-fb-http-engine': 'Liger',
'x-fb-client-ip': 'True',
'x-fb-server-cluster': 'True',
'x-ig-bandwidth-speed-kbps': str(random.randint(100, 300)),
'x-ig-bandwidth-totalbytes-b': str(random.randint(500000, 900000)),
'x-ig-bandwidth-totaltime-ms': str(random.randint(1000, 9000)),
'x-ig-app-id': '3419628305025917',
'connection': 'keep-alive'
    }

    ## Create the payload for the login request
payload = {
'params': '{"client_input_params":{"device_id":"'+ str(headers['x-ig-android-id']) +'","lois_settings":{"lois_token":"","lara_override":""},"name":"'+str(username)+'","machine_id":"'+str(headers['x-mid'])+'","profile_pic_url":null,"contact_point":"'+str(username)+'","encrypted_password":"#PWD_INSTAGRAM:0:'+str(int(time.time()))+':'+str(passwd)+'"},"server_params":{"is_from_logged_out":0,"login_source":"Login"}}',
'bk_client_context': '{"bloks_version":"'+ str(headers['x-bloks-version-id']) +'","styles_id":"instagram"}',
'bloks_versioning_id': str(headers['x-bloks-version-id'])
    }

    ## URL encode the parameters for the request
encode = ('params=%s&bk_client_context=%s&bloks_versioning_id=%s' % 
      (urllib.parse.quote(payload['params']), 
       urllib.parse.quote(payload['bk_client_context']),
       payload['bloks_versioning_id']))

    ## Update headers with content length and cookies
headers.update({'content-length': str(len(encode)), 
    'cookie': (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])})

    ## Send the POST request to Instagram API
response = session.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.login.async.send_google_smartlock_login_request/', 
  data=encode, headers=headers, allow_redirects=True).text

    ## Check if login was successful
wanted = ["ds_user_id", "sessionid"]
all_cookies = session.cookies.get_dict()
extracted = {k: all_cookies[k] for k in wanted if k in all_cookies}
cookie_str = "; ".join(f"{k}={v}" for k, v in extracted.items())
print("Cookies:", cookie_str)
