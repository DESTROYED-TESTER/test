import random
import re
import sys
import time
import hashlib
import uuid
import urllib.request
import requests
import string
import os
import time,subprocess,platform,uuid,json
import random
import base64
import string
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
uid = "61592834126178"
pw = "@123456As"
END = "[FBAN/FB4A;F"+"BAV/"+"106"+".0.0.26.68;FBBV/"+"106;F"+"BDM/{"+"density="+"3.0,wid"+"th=750"+",height=1334};FBLC/it_"+"IT;FBRV/106."+"0.0.26.6"+"8;FBCR/Etisalat"+"Afg"+"hanistan;FBMF/Infi"+"nix_"+"Note_8i;FBBD/Infi"+"nix_Note_8i;FBPN/c"+"om.facebook.katana"+";FBDV/I"+"nfinix_Note_8i_10_0;FBSV/10.0;FBOP/1;FBCA/"+"x86:armeabi-v7a;]"
Session = requests.Session()
Session.headers.update({
                'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'x-fb-sim-hni': '51009',
                'x-fb-net-hni': '51009',
                'Content-Type': 'application/x-www-form-urlencoded',
                'x-graphql-client-library': 'graphservice',
                'x-fb-friendly-name': 'FbBloksActionRootQuery-com.bloks.www.bloks.caa.login.async.send_google_smartlock_login_request',
                'x-tigon-is-retry': 'False',
                'x-fb-privacy-context': '3643298472347298',
                'x-graphql-request-purpose': 'fetch',
                'x-fb-device-group': '5530',
                'User-Agent': END,
                'x-fb-connection-type': 'WIFI',
                'x-fb-rmd': 'fail=Server:NoUrlMap,Default:INVALID_MAP;v=;ip=;tkn=;reqTime=56;recvTime=13823808',
                'x-fb-request-analytics-tags': '{"network_tags":{"product":"350685531728","purpose":"fetch","request_category":"graphql","retry_attempt":"0"},"application_tags":"graphservice"}',
                'x-fb-http-engine': 'Tigon/Liger',
                'x-fb-client-ip': 'True',
                'x-fb-server-cluster': 'True',
                })
apcb = '#PWD_FB4A:0:{}:{}'.format(str(int(time.time())), pw)
data = {
                'method': 'post',
                'pretty': False,
                'format': 'json',
                'server_timestamps': True,
                'locale': 'ja_JP',
                'purpose': 'fetch',
                'fb_api_req_friendly_name': 'FbBloksActionRootQuery-com.bloks.www.bloks.caa.login.async.send_google_smartlock_login_request',
                'fb_api_caller_class': 'graphservice',
                'client_doc_id': '11994080425603935587861051615',
                'variables': json.dumps({"params":{"params":"{\"params\":\"{\\\"client_input_params\\\":{\\\"device_id\\\":\\\"db00d712-bd44-4358-bcf2-2fe14e2885d2\\\",\\\"lois_settings\\\":{\\\"lois_token\\\":\\\"\\\",\\\"lara_override\\\":\\\"\\\"},\\\"name\\\":null,\\\"machine_id\\\":\\\"FXQ7Z_eNU42Pnt5I_CpRlzIh\\\",\\\"profile_pic_url\\\":null,\\\"contact_point\\\":\\\""+uid+"\\\",\\\"encrypted_password\\\":\\\""+apcb+"\\\"},\\\"server_params\\\":{\\\"is_from_logged_out\\\":1,\\\"layered_homepage_experiment_group\\\":null,\\\"device_id\\\":\\\"db00d712-bd44-4358-bcf2-2fe14e2885d2\\\",\\\"waterfall_id\\\":\\\"278dd0ac-58b3-46e4-aa8e-ea55021589a6\\\",\\\"INTERNAL__latency_qpl_instance_id\\\":2.9809277900605E13,\\\"login_source\\\":\\\"Login\\\",\\\"is_platform_login\\\":0,\\\"INTERNAL__latency_qpl_marker_id\\\":36707139,\\\"family_device_id\\\":\\\"db00d712-bd44-4358-bcf2-2fe14e2885d2\\\",\\\"offline_experiment_group\\\":\\\"caa_iteration_v6_perf_fb_2\\\",\\\"INTERNAL_INFRA_THEME\\\":\\\"default,default\\\",\\\"access_flow_version\\\":\\\"F2_FLOW\\\",\\\"is_from_logged_in_switcher\\\":0}}\"}","bloks_versioning_id":"3711cb070fe0ab5acd59ae663b1ae4dc75db6f0c463d26a232fd9d72a63fb3e5","app_id":"com.bloks.www.bloks.caa.login.async.send_google_smartlock_login_request"},"scale":"2","nt_context":{"using_white_navbar":True,"styles_id":"cfe75e13b386d5c54b1de2dcca1bee5a","pixel_ratio":2,"is_push_on":False,"debug_tooling_metadata_token":None,"is_flipper_enabled":False,"theme_params":[],"bloks_version":"3711cb070fe0ab5acd59ae663b1ae4dc75db6f0c463d26a232fd9d72a63fb3e5"}}),
                'fb_api_analytics_tags': '["GraphServices"]',
                'client_trace_id': 'c4663a0f-a919-4454-bf17-3d542589eafe'}
encode = urllib.parse.urlencode(data, doseq=True)
twf = "login approval"+"s are on. "+"Expect an SMS"+" shortly with "+"a code to use"+" for log in"
response = Session.post('https://graph.facebook.com/graphql', data=encode)
#print(response)
#print(response.status_code)
#print(f"Status Code: {response.status_code}")
#print(f"Response URL: {response.url}")# Check login success
if "session_key" in response.text and "uid" in response.text and "c_user" in response.text.replace('\\', '') and "access_token" in response.text:
    print(ok)
    sb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
    ckkk = ";".join(i["name"]+"="+i["value"] for i in response["session_cookies"])
    print(ckkk)
