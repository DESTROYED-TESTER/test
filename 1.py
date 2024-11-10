import uuid
import requests

data = {
    'adid': str(uuid.uuid4()),
    'format': 'json',
    'device_id': str(uuid.uuid4()),
    'family_device_id': str(uuid.uuid4()),
    'secure_family_device_id': str(uuid.uuid4()),
    'cpl': 'true',
    'try_num': '1',
    'email': '9876787687',
    'password': '987678',
    'method': 'auth.login',
    'generate_session_cookies': '1',
    'sim_serials': "['80973453345210784798']",
    'openid_flow': 'android_login',
    'openid_provider': 'google',
    'openid_emails': "['01710940017']",
    'openid_tokens': "['eyJhbGciOiJSUzI1NiIsImtpZCI6IjdjOWM3OGUzYjAwZTFiYjA5MmQyNDZjODg3YjExMjIwYzg3YjdkMjAiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiAiYWNjb3VudHMuZ29vZ2xlLmNvbSIsICJhenAiOiAiMTY5MjI5MzgyMy0xZno0cGVjOGg5N2JsYmxmd2t0ODh2NG8weWJ5Y2pseWYuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCAiYXVkIjogIjE2OTIyOTM4MjMtbDhqZDA5OGh5Y3dmd2lnZDY0NW5xMmdmeXV0YTFuZ2FoLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwgInN1YiI6ICIxMDkxMzk4NzMzNDMwNTcwMDE5NzkiLCAiZW1haWwiOiAiMTk0NUBnbWFpbC5jb20iLCAiZW1haWxfdmVyaWZpZWQiOiB0cnVlLCAicGljdHVyZSI6ICJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS0vQURfY01NUmtFY3FDcTlwcF9YMHdIYTlSb3JpR2V1a0tJa0NnLU15TjFiR2gxb3lnX1E9czk2LWMiLCAiaWF0IjogMTY5MjI5MzgyMywgImV4cCI6IDE2OTIyOTM4MjN9.oHvakCxpmVdAzYgq5jSXN5uCD6L10Bj2EhblWK4IEFhat_acn6jDPKGcYVDx8wxoj5rFRVbDP1xwzfN0eCFG6R9pTslsQHP-PrTNsqeVnhWDV1iEup77iRhPjJRClNMij5RzqQFr7rStwPtAolrQWC_q_uuFrGelW21Tg_enA36PPSrShnloTm6zt83xUYzKQvXl55brBs2zatZ2vWwftwMoOWfp6NbUkd8hliZrMGA8j_A9PTij_1-5BQZSOXSfjcxl7JtZwqx4DJN2dkI0eT6hSAjc4YUOMQHDLRJD9tY4ckYfzJ38mGjs2m5wACv2n1QLoOLpoVspfT86Ky-N4g']",
    'error_detail_type': 'button_with_disabled',
    'source': 'account_recovery',
    'locale': 'en_GB',
    'client_country_code': 'GB',
    'fb_api_req_friendly_name': 'authenticate',
    'fb_api_caller_class': 'AuthOperations$PasswordAuthOperation'
}

head = {
    'Host': 'graph.facebook.com',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
    'Priority': 'u=3, i',
    'X-Fb-Sim-Hni': '45204',
    'X-Fb-Net-Hni': '45201',
    'X-Fb-Connection-Quality': 'GOOD',
    'Zero-Rated': '0',
    'User-Agent': "[FBAN/FB4A;FBAV/54.0.0.3795;FBBV/66205985[FBAN/Orca-Android;FBAV/247.0.0.30.84;FBPN/com.facebook.orca;FBBV/410140983;FBLC/en_US;FBCA/arm64-v8a:;FBCR/Ufone;FBMF/INFINIX MOBILITY LIMITED;FBBD/Infinix;FBDV/Infinix X695;FBSV/11;FBDM/{density=2.0,width=720,height=1440};]",
    'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
    'X-Fb-Connection-Bandwidth': '24807555',
    'X-Fb-Connection-Type': 'MOBILE.LTE',
    'X-Fb-Device-Group': '5120',
    'X-Tigon-Is-Retry': 'False',
    'X-Fb-Friendly-Name': 'authenticate',
    'X-Fb-Request-Analytics-Tags': 'unknown',
    'X-Fb-Http-Engine': 'Liger',
    'X-Fb-Client-Ip': 'True',
    'X-Fb-Server-Cluster': 'True',
    'Content-Length': '847'
}

# Sending the POST request
po = requests.post('https://b-graph.facebook.com/auth/login', data=data, headers=head).json()

# Printing the response
print(po)
