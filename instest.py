import hashlib
import uuid
import time
import random
import urllib.parse
import requests


def login():
        try:
            hash = hashlib.md5()
            hash.update(username.encode('utf-8') + passwd.encode('utf-8'))
            hex = hash.hexdigest()
            hash.update(hex.encode('utf-8') + '12345'.encode('utf-8'))
            session = requests.Session()
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
                'user-agent': 'Instagram 63.0.0.17.94 Android (31/10; 360dpi; 1080x2326; Vivo; V2020CA; V1950A; qcom; id_ID; 253447817)',
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
                'x-pigeon-rawclienttime': str(round(time.time(), 3)),
                'connection': 'keep-alive'
            }

            payload = {
                'params': '{"client_input_params":{"device_id":"'+ str(headers['x-ig-android-id']) +'","lois_settings":{"lois_token":"","lara_override":""},"name":"'+str(username)+'","machine_id":"'+str(headers['x-mid'])+'","profile_pic_url":null,"contact_point":"'+str('8918354921')+'","encrypted_password":"#PWD_INSTAGRAM:0:'+str(int(time.time()))+':'+str('891835')+'"},"server_params":{"is_from_logged_out":0,"layered_homepage_experiment_group":null,"INTERNAL__latency_qpl_marker_id":36707139,"family_device_id":"'+str(headers['x-ig-family-device-id'])+'","device_id":"'+str(headers['x-ig-device-id'])+'","offline_experiment_group":null,"INTERNAL_INFRA_THEME":"harm_f","waterfall_id":"'+str(uuid.uuid4())+'","login_source":"Login","INTERNAL__latency_qpl_instance_id":73767726200338,"is_from_logged_in_switcher":0,"is_platform_login":0}}',
                'bk_client_context': '{"bloks_version":"'+ str(headers['x-bloks-version-id']) +'","styles_id":"instagram"}',
                'bloks_versioning_id': str(headers['x-bloks-version-id'])
            }

            encode = ('params=%s&bk_client_context=%s&bloks_versioning_id=%s' % (
                urllib.parse.quote(payload['params']),
                urllib.parse.quote(payload['bk_client_context']),
                payload['bloks_versioning_id']
            ))

            headers.update({
                'content-length': str(len(encode)),
                'cookie': ";".join([f"{key}={value}" for key, value in session.cookies.get_dict().items()])
            })

            response = session.post(
                'https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.login.async.send_google_smartlock_login_request/',
                data=encode,
                headers=headers,
                allow_redirects=True
            ).text

            result_ok, result_two, result_cp = Simpan_Result()

            if 'logged_in_user' in response:
                print(response)
                return True, response
            else:
                return False, response

        except Exception as e:
            return False, str(e)
