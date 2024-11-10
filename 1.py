import uuid
import requests

data = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'email': '9641367634',
                'password': '964136',
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
                'locale': 'en_GB',
                'client_country_code': 'GB',
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                'api_key': '62f8ce9f74b12f84c123cc23437a4a32',
                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
            }

head = {
                'User-Agent': "[FBAN/FB4A;FBAV/365.0.0.44.118;FBBV/310204222;FBDM/{density=3.0,width=1080,height=2400};FBLC/ru_RU;FBRV/315309999;FBCR/MegaFon;FBMF/Realme;FBBD/Realme;FBPN/com.facebook.katana;FBDV/Realme 7 Pro;FBSV/10;FBOP/1;FBCA/arm64-v8a:]",
                'Accept-Encoding': 'gzip, deflate',
                'Connection': 'close',
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-FB-Net-HNI': str(random.randint(20000,40000)),
                'X-FB-SIM-HNI': str(random.randint(20000,40000)),
                'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'X-FB-Connection-Type': 'WIFI',
                'X-FB-device-group': str(random.randint(2000, 4000)),
                'X-Tigon-Is-Retry': 'False',
                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
                'x-fb-device-group': '5120',
                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32',
            }

# Sending the POST request
po = requests.post('https://b-graph.facebook.com/auth/login', data=data, headers=head).json()

# Printing the response
print(po)
