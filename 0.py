import requests
import json
import re
import time

req=requests.Session()
uid='61555629843961'  # Replace with your actual username (email or phone number)
pw='787996'  # Replace with your actual password
free_fb=req.get('https://touch.facebook.com').text
data = {
'email': uid,
'cuid': '',
'guid': 'f7d923be260ada3ea',
'lgnjs': '1733767601',
'lgnrnd': '100640_NiY9',
'locale': 'en_GB',
'login_source': 'comet_login_header',
'next': 'https://www.facebook.com/gfgd',
'skstamp': '',
'timezone': '-330',
'prefill_contact_point': '',
'prefill_source': '',
'lsd': re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
'jazoest': re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
'lgndim': 'eyJ3IjoxNDQwLCJoIjo5MDAsImF3IjoxNDQwLCJhaCI6ODYwLCJjIjoyNH0=',
'ab_test_data': '^%^2F^%^2FAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPf^%^2FfPAPPBFAC',
'encpass': "#PWD_BROWSER:0:{}:{}".format(str(time.time()).split('.')[0], pw),}
cookies = {
'datr': '9VEvZ9JBwP-qDedVPM0RiFU2',
'fr': '0s2vxnm2t0jH8elbM..BnL1H1..AAA.0.0.BnVzGp.AWUAJfrpnro',
'sb': '9VEvZ6aV778dZuTY2EWKGHcM',
'wd': '1440x402',
'ps_l': '1',
'ps_n': '1',}
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Language': 'en-US,en;q=0.5',
'Content-Type': 'application/x-www-form-urlencoded',
'Origin': 'https://www.facebook.com',
'DNT': '1',
'Alt-Used': 'www.facebook.com',
'Connection': 'keep-alive',
'Referer': 'https://www.facebook.com/gfgd',
'Upgrade-Insecure-Requests': '1',
'Sec-Fetch-Dest': 'document',
'Sec-Fetch-Mode': 'navigate',
'Sec-Fetch-Site': 'same-origin',
'Sec-Fetch-User': '?1',
'Priority': 'u=0, i',
'Pragma': 'no-cache',
'Cache-Control': 'no-cache',}
url='https://www.facebook.com/login/device-based/regular/login/?login_attempt=1'
response=req.post(url, data=data, cookies=cookies, headers=headers, allow_redirects=False).text
# Step 7: Handle the response
response=req.cookies.get_dict().keys()
if "c_user" in response:
    print(f"(ATOM-OK){uid}|{pw}")
else:
    print(f"Login failed for {uid}. Please check credentials.")
