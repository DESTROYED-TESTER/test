import requests,time

uid = '100077421650959'
password = '976317'
web_encryptor = Encrypt_PWD_Web()
web_token = web_encryptor.PWD_BROWSER(password)
# --- (use your existing headers/cookies/params/data) ---
cookies = {
    'datr': '7DnMaEaBSi1euh0ZrTxnFPXZ',
    'sb': '7DnMaMKotlR75LUbGLYU-TYB',
    'm_pixel_ratio': '2.4749999046325684',
    'ps_l': '1',
    'ps_n': '1',
    'dpr': '2.4749999046325684',
    'wd': '437x973',
    'fr': '02n8peqk75hF9D13g.AWcYnHXf1GZF8b7MXvQBW4q05cEXwaTcJhJCnUnlt93z2xfY_YY.BozDns..AAA.0.0.Bo1hLI.AWcm2HkPoopHsJCgNGiCAIgqHgw',
}  # keep your dict as in your snippet
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 13; V2060 Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.155 Mobile Safari/537.36',
    # 'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Content-Type': 'application/x-www-form-urlencoded',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Android WebView";v="140"',
    'x-response-format': 'JSONStream',
    'sec-ch-ua-mobile': '?1',
    'x-asbd-id': '359341',
    'x-fb-lsd': 'AdEVi-OFg_s',
    'x-requested-with': 'XMLHttpRequest',
    'origin': 'https://limited.facebook.com',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://limited.facebook.com/login.php?skip_api_login=1&api_key=1393952984244777&kid_directed_site=0&app_id=1393952984244777&signed_next=1&next=https://m.facebook.com/v16.0/dialog/oauth?app_id=1393952984244777&cbt=1758859215730&channel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Dfedd56e5da955addb%26domain%3Dwww.boomplay.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.boomplay.com%252Ff8911011906172fa2%26relation%3Dopener&client_id=1393952984244777&display=touch&domain=www.boomplay.com&e2e=%7B%7D&fallback_redirect_uri=https%3A%2F%2Fwww.boomplay.com%2Fsongs%2F216051730&locale=en_US&logger_id=fb5ecf6aa44bb1de3&origin=2&redirect_uri=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df9bf310860cbd212d%26domain%3Dwww.boomplay.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.boomplay.com%252Ff8911011906172fa2%26relation%3Dopener%26frame%3Dfb8a321b81d3ff397&response_type=token%2Csigned_request%2Cgraph_domain&sdk=joey&version=v16.0&ret=login&fbapp_pres=0&tp=unspecified&cancel_url=https://staticxx.facebook.com/x/connect/xd_arbiter/?version=46',
    'accept-language': 'en-US,en;q=0.9',
    'priority': 'u=1, i',
    # 'Cookie': 'datr=7DnMaEaBSi1euh0ZrTxnFPXZ; sb=7DnMaMKotlR75LUbGLYU-TYB; m_pixel_ratio=2.4749999046325684; ps_l=1; ps_n=1; pas=100056503155212%3AfxOzQdbFmo; dpr=2.4749999046325684; wd=437x973; fr=02n8peqk75hF9D13g.AWcYnHXf1GZF8b7MXvQBW4q05cEXwaTcJhJCnUnlt93z2xfY_YY.BozDns..AAA.0.0.Bo1hLI.AWcm2HkPoopHsJCgNGiCAIgqHgw',
}   # same as your snippet
params = {
    'api_key': '1393952984244777',
    'auth_token': '3ea524ab821dcb9e2140fbe35e5e09fd',
    'skip_api_login': '1',
    'signed_next': '1',
    'next': 'https://m.facebook.com/v16.0/dialog/oauth?app_id=1393952984244777&cbt=1758859978311&logger_id=2fb35fb5-cdb2-46af-8dc4-996548b0ec0b',
    'refsrc': 'deprecated',
    'app_id': '1393952984244777',
    'cancel': 'https://staticxx.facebook.com/x/connect/xd_arbiter/?version=46',
    'lwv': '100',
}
    # same as your snippet
data = {
    'm_ts': '1758859976',
    'li': 'yBLWaNo3yCbGoJgrOxFDDjjk',
    'try_number': '0',
    'unrecognized_tries': '0',
    'email': uid,
    'prefill_contact_point': uid,
    'prefill_source': 'browser_dropdown',
    'prefill_type': 'password',
    'first_prefill_source': 'browser_dropdown',
    'first_prefill_type': 'contact_point',
    'had_cp_prefilled': 'true',
    'had_password_prefilled': 'true',
    'is_smart_lock': 'false',
    'bi_xrwh': '92004344361786634',
    'encpass': web_token,
    'fb_dtsg': 'NAfup2Me3JHXJFN2yxBY35qKn-1LtNpMqJhQzaJ3AqYbs8PMFOvFhGw:0:0',
    'jazoest': '24862',
    'lsd': 'AdEVi-OFg_s',
    '_dyn': '1KQdAG1mws8-t0BBBzEnwuo98nwgU2owpUuwcC4o1nEhw23E52q1ew6ywaq1Jw20Ehw73wGwcq0RE1u81x82ew5fw5NyE1582ZwrU2pw4swSw7zwde0UE',
    'csr': '',
    'hsdp': '',
    'hblp': '',
    'sjsp': '',
    'req': '1',
    'fmt': '1',
    'a': 'AYrzCMozrxxEkLpLMe4Y2HjtqtsmVGwYzrN5JRYYClldhdPtYgFp1Jf_aTSnrZs9GEMJRGEqpBnp7Yr7bbjZFjK5_l3XCV2rjhwTOtu5o4lWwg',
    '_user': '0',}
url = "https://free.facebook.com/login/device-based/login/async/"

# --- Do the POST using a Session so cookies persist ---
session = requests.Session()
# set headers on the session (helps keep them for redirects)
session.headers.update(headers)

# preload client-side cookies (optional; requests will send them)
for k, v in cookies.items():
    session.cookies.set(k, v, domain=".facebook.com")

# perform the request
resp = session.post(url, params=params, data=data, allow_redirects=True, timeout=30)

# extract cookies from the session
cookies_after = session.cookies.get_dict()

# check for typical FB login cookies (most reliable: 'c_user' and 'xs')
if "c_user" in cookies_after:
    print("Login appears SUCCESSFUL.")
    # Build a cookie header string you can re-use in subsequent requests:
    cookie_header = "; ".join([f"{k}={v}" for k, v in cookies_after.items()])
    print("Cookie header to reuse:")
    print(cookie_header)
    # If you want individual pieces:
    print("c_user:", cookies_after.get("c_user"))
    print("xs:", cookies_after.get("xs"))
else:
    print("Login does NOT appear successful.")
    print("HTTP status:", resp.status_code)
    # show a short resp preview to help debugging
    preview = resp.text[:1500].replace("\n", " ")
    print("Response preview:", preview)
    print("Cookies received:", cookies_after)


class Encrypt_PWD_Web:
    def __init__(self):
        pass

    def PWD_BROWSER(self, password, public_key=None, key_id="5"):
        """
        Generate a #PWD_BROWSER token for Facebook web login.
        Returns: '#PWD_BROWSER:5:<timestamp>:<base64_blob>'
        """
        if public_key is None:
            try:
                pwd_key_fetch = 'https://b-graph.facebook.com/pwd_key_fetch'
                params = {
                    'version': '2',
                    'flow': 'CONTROLLER_INITIALIZATION',
                    'method': 'GET',
                    'fb_api_req_friendly_name': 'pwdKeyFetch',
                    'fb_api_caller_class': 'com.facebook.auth.login.AuthOperations',
                    'access_token': '438142079694454|fc0a7caa49b192f64f6f5a6d9643bb28'
                }
                response = requests.post(pwd_key_fetch, params=params, timeout=10).json()
                public_key = response.get('public_key')
                key_id = str(response.get('key_id', key_id))
                if not public_key:
                    return "Failed to fetch public_key"
            except Exception as e:
                return f"API: {str(e)}"

        try:
            # AES key + IV
            rand_key = get_random_bytes(32)
            iv = get_random_bytes(12)

            # RSA encrypt AES key
            pubkey = RSA.import_key(public_key)
            cipher_rsa = PKCS1_v1_5.new(pubkey)
            encrypted_rand_key = cipher_rsa.encrypt(rand_key)

            # AES-GCM encrypt password using timestamp as AAD
            cipher_aes = AES.new(rand_key, AES.MODE_GCM, nonce=iv)
            current_time = int(time.time())
            cipher_aes.update(str(current_time).encode("utf-8"))
            encrypted_passwd, auth_tag = cipher_aes.encrypt_and_digest(password.encode("utf-8"))

            # Assemble payload: [1, key_id] + IV + RSA key len + RSA key + auth tag + ciphertext
            buf = io.BytesIO()
            buf.write(bytes([1, int(key_id)]))
            buf.write(iv)
            buf.write(struct.pack("<H", len(encrypted_rand_key)))  # unsigned short
            buf.write(encrypted_rand_key)
            buf.write(auth_tag)
            buf.write(encrypted_passwd)

            encoded = base64.b64encode(buf.getvalue()).decode("utf-8")

            # Web token version 5
            return f"#PWD_BROWSER:5:{current_time}:{encoded}"

        except Exception as e:
            return str(e).title()
