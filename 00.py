import requests
import json
import time
import base64

def generate_encrypted_password(password, timestamp=None):
    """
    Generate Facebook's password encryption format
    #PWD_BROWSER:version:timestamp:encrypted_password
    """
    if timestamp is None:
        timestamp = int(time.time())
    
    # Facebook uses base64 encoding for the password
    encoded = base64.b64encode(password.encode()).decode()
    return f"#PWD_BROWSER:5:{timestamp}:{encoded}"

# ============== SET YOUR CREDENTIALS HERE ==============
PHONE_NUMBER = "9907071441"  # Your phone number
ACTUAL_PASSWORD = "your_actual_password_here"  # <-- CHANGE THIS TO YOUR REAL PASSWORD!
# ======================================================

# Generate encrypted password
encrypted_password = generate_encrypted_password(ACTUAL_PASSWORD)

cookies = {
    'datr': '9vhZalHGJl4wqFsO-ktnTCPO',
    'fr': '0AHYCzZvY1zDGFbT7..BqWfj2..AAA.0.0.BqWfoF.AWcWgNs6zxC7us5LKeylW8T1R_w',
    'sb': '9vhZaqT8BEFlcFGMioJbP2ay',
    'wd': '1440x459',
    'checkpoint': '%7B%22u%22%3A100065963493022%2C%22t%22%3A1784281507%2C%22step%22%3A0%2C%22n%22%3A%22Mpso5QCLmk4%3D%22%2C%22inst%22%3A1298420665700038%2C%22f%22%3A465803052217681%2C%22st%22%3A%22c%22%2C%22aid%22%3Anull%2C%22ca%22%3Anull%2C%22la%22%3A%22%22%2C%22ta%22%3A%221784281514.ch.s%3An619%3Apw.9zBFAiEA1ogZCv-9Exu3f9BHjwKjA-HWjnfvRhDpjhhPdApejS0CIAaHKsbz84a7RD_iPZMEuq9dpNI2WFAqrIIGiSS59kNI%22%2C%22tfvaid%22%3Anull%2C%22tfvasec%22%3Anull%2C%22sat%22%3Anull%2C%22idg%22%3Afalse%2C%22cidue%22%3A%22%22%2C%22tfuln%22%3Anull%2C%22tfvri%22%3Anull%2C%22ct%22%3A%22AWSJF4D9mjvdmjyeARsA7yoDuPTFjymI-C8p56SdRq9Bsl96VEiUDlS98AsvU2NJwSaxfjQ0eOvxkyztJQyRb8qaxzARmYkZQbtlcNmc-5HqxdPrNjLlGqQgve9emTOQI_AdRHUqA9F8AqkL3rxTgfTeS02W5KkKDIv_JqK7_CoWjm8o6TQC3jsFatEg8kOShfZ4D3unQL-hG2gzJ2kYIkstHQT_5_O7eVMKea38ZJc1Gg8VoS1s8Mrl5FRmBOkcaaWqRTUxnrqorlMH3ug53epBZth5Fh93qXDyEeLHzlEvgHB0kOYR02v6dpr9L8Yepdpb9twVI9BJYdZYfD3Nxcz2ugLxWNsliVHogo16TNddyEfUeeqZPOmq83QBXOWlQviZX6qpsMFlvexax1AWHJQaPjhA6N0tF0c%22%2C%22aads%22%3Anull%2C%22s%22%3A%22AWaR3cpMmmUtaDcesuQ%22%2C%22cs%22%3A%5B%5D%2C%22ssp%22%3A1%7D',
    'locale': 'en_GB',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:152.0) Gecko/20100101 Firefox/152.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Content-Type': 'application/x-www-form-urlencoded',
    'X-FB-Friendly-Name': 'useCDSWebLoginMutation',
    'X-FB-LSD': 'wkEB6DkikroblzgG--A07m',
    'X-ASBD-ID': '359341',
    'Origin': 'https://www.facebook.com',
    'Alt-Used': 'www.facebook.com',
    'Connection': 'keep-alive',
    'Referer': 'https://www.facebook.com/login.php?skip_api_login=1&api_key=2036793259884297&kid_directed_site=0&app_id=2036793259884297&signed_next=1&next=https%3A%2F%2Fwww.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D2036793259884297%26redirect_uri%3Dhttps%253A%252F%252Fauth.garena.com%252Funiversal%252Foauth%252Ffacebook%26response_type%3Dtoken%26scope%3Dpublic_profile%252Cemail%252Cuser_friends%252Cuser_link%26state%3D94e81a8bc7c546639f1bd76c25fe3bd6-platform%253D3%2526response_type%253Dcode%2526client_id%253D100067%2526redirect_uri%253Dhttps%25253A%25252F%25252Fzdauth.garena.com%25252Flogin%25253Freturn_to%25253Dhttps%25253A%25252F%25252Fffsupport.garena.com%25252Fhc%25252Fen-us%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D86af918c-a25d-49f6-94f0-f090c83ee33e%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fauth.garena.com%2Funiversal%2Foauth%2Ffacebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D94e81a8bc7c546639f1bd76c25fe3bd6-platform%253D3%2526response_type%253Dcode%2526client_id%253D100067%2526redirect_uri%253Dhttps%25253A%25252F%25252Fzdauth.garena.com%25252Flogin%25253Freturn_to%25253Dhttps%25253A%25252F%25252Fffsupport.garena.com%25252Fhc%25252Fen-us%23_%3D_&display=page&locale=en_GB&pl_dbl=0&is_business_login=0',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
}

# Define the variables as a dictionary
variables_dict = {
    "input": {
        "actor_id": "0",
        "client_mutation_id": "7",
        "access_flow_version": "pre_mt_behavior",
        "app": "facebook",
        "auth_domain_data_key": None,
        "caa_login_request_extra_info": {
            "ab_test_data": "/AAAAAAAAAAAAAAAAAAAfAAAAAAAAAAAAAAAAAAAAAAAVVVA/ABAAG",
            "shared_prefs_data": "eyIzMDAwMCI6W3sidCI6MTc4NDI4MTYwNy4zNiwiY3R4Ijp7ImNuIjoiaHR0cHM6Ly93d3cuZmFjZWJvb2suY29tL2xvZ2luLnBocCJ9LCJ2IjpmYWxzZX1dLCIzMDAwMSI6W3sidCI6MTc4NDI4MTYwNy4zNiwiY3R4Ijp7ImNuIjoiaHR0cHM6Ly93d3cuZmFjZWJvb2suY29tL2xvZ2luLnBocCJ9LCJ2Ijo1fV0sIjMwMDAyIjpbeyJ0IjoxNzg0MjgxNjA3LjM2LCJjdHgiOnsiY24iOiJodHRwczovL3d3dy5mYWNlYm9vay5jb20vbG9naW4ucGhwIn0sInYiOjJ9XSwiMzAwMDMiOlt7InQiOjE3ODQyODE2MDcuMzYsImN0eCI6eyJjbiI6Imh0dHBzOi8vd3d3LmZhY2Vib29rLmNvbS9sb2dpbi5waHAifSwidiI6WyJlbi1VUyIsImVuIl19XSwiMzAwMDQiOlt7InQiOjE3ODQyODE2MDcuMzYsImN0eCI6eyJjbiI6Imh0dHBzOi8vd3d3LmZhY2Vib29rLmNvbS9sb2dpbi5waHAifSwiZSI6eyJlYyI6M319XSwiMzAwMDUiOlt7InQiOjE3ODQyODE2MDcuMzYxLCJjdHgiOnsiY24iOiJodHRwczovL3d3dy5mYWNlYm9vay5jb20vbG9naW4ucGhwIn0sInYiOnsidyI6MTQ0MCwiaCI6Nzc1fX1dLCIzMDAwNyI6W3sidCI6MTc4NDI4MTYwNy4zNjEsImN0eCI6eyJjbiI6Imh0dHBzOi8vd3d3LmZhY2Vib29rLmNvbS9sb2dpbi5waHAifSwidiI6ImRlZmF1bHQifV0sIjMwMDA4IjpbeyJ0IjoxNzg0MjgxNjA3LjQ3MywiY3R4Ijp7ImNuIjoiaHR0cHM6Ly93d3cuZmFjZWJvb2suY29tL2xvZ2luLnBocCJ9LCJ2IjoicHJvbXB0In1dLCIzMDAxMiI6W3sidCI6MTc4NDI4MTYwNy4zNjEsImN0eCI6eyJjbiI6Imh0dHBzOi8vd3d3LmZhY2Vib29rLmNvbS9sb2dpbi5waHAifSwidiI6IiJ9XSwiMzAwMTMiOlt7InQiOjE3ODQyODE2MDcuMzYxLCJjdHgiOnsiY24iOiJodHRwczovL3d3dy5mYWNlYm9vay5jb20vbG9naW4ucGhwIn0sInYiOiI1LjAgKFdpbmRvd3MpIn1dLCIzMDAxNSI6W3sidCI6MTc4NDI4MTYwNy4zNjEsImN0eCI6eyJjbiI6Imh0dHBzOi8vd3d3LmZhY2Vib29rLmNvbS9sb2dpbi5waHAifSwidiI6IldpbjMyIn1dLCIzMDAxOCI6W3sidCI6MTc4NDI4MTYwNy4zNjEsImN0eCI6eyJjbiI6Imh0dHBzOi8vd3d3LmZhY2Vib29rLmNvbS9sb2dpbi5waHAifSwidiI6Mn1dLCIzMDAyMiI6W3sidCI6MTc4NDI4MTYwNy4zNjYsImN0eCI6eyJjbiI6Imh0dHBzOi8vd3d3LmZhY2Vib29rLmNvbS9sb2dpbi5waHAifSwidiI6dHJ1ZX1dLCIzMDA0MCI6W3sidCI6MTc4NDI4MTYwNy4zNjYsImN0eCI6eyJjbiI6Imh0dHBzOi8vd3d3LmZhY2Vib29rLmNvbS9sb2dpbi5waHAifSwidiI6LTMzMH1dLCIzMDA5MyI6W3sidCI6MTc4NDI4MTYwNy4zNjYsImN0eCI6eyJjbiI6Imh0dHBzOi8vd3d3LmZhY2Vib29rLmNvbS9sb2dpbi5waHAifSwidiI6MH1dLCIzMDA5NCI6W3sidCI6MTc4NDI4MTYwNy4zNjYsImN0eCI6eyJjbiI6Imh0dHBzOi8vd3d3LmZhY2Vib29rLmNvbS9sb2dpbi5waHAifSwidiI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQ7IHJ2OjE1Mi4wKSBHZWNrby8yMDEwMDEwMSBGaXJlZm94LzE1Mi4wIn1dLCIzMDA5NSI6W3sidCI6MTc4NDI4MTYwNy4zNjYsImN0eCI6eyJjbiI6Imh0dHBzOi8vd3d3LmZhY2Vib29rLmNvbS9sb2dpbi5waHAifSwidiI6NX1dLCIzMDEwNiI6W3sidCI6MTc4NDI4MTYwNy4yMzEsImN0eCI6eyJjbiI6Imh0dHBzOi8vd3d3LmZhY2Vib29rLmNvbS9sb2dpbi5waHAifSwidiI6ZmFsc2V9LHsidCI6MTc4NDI4MTYwNy43MzUsImN0eCI6eyJjbiI6Imh0dHBzOi8vd3d3LmZhY2Vib29rLmNvbS9sb2dpbi5waHAifSwidiI6dHJ1ZX1dLCIzMDEwNyI6W3sidCI6MTc4NDI4MTYwNy4yMzIsImN0eCI6eyJjbiI6Imh0dHBzOi8vd3d3LmZhY2Vib29rLmNvbS9sb2dpbi5waHAifSwidiI6ZmFsc2V9XSwiMzAxMDkiOlt7InQiOjE3ODQyODE2MDcuNjU0LCJjdHgiOnsiY24iOiJodHRwczovL3d3dy5mYWNlYm9vay5jb20vbG9naW4ucGhwIn0sInYiOiI1YmM0OGQ5Y2I2YjgzMWI0NmZhZDQ1Yzg5NTg0MGY5YjA0MDcwMzNlOTI5ZTAyMzk3NTUxMWQ1YWRmZGIzZTYyIn1dfQ==",
            "cuid": "",
            "guid": "f63fae21b3e54614c",
            "jazoest": "21021",
            "lgndim": "eyJ3IjoxNDQwLCJoIjo5MDAsImF3IjoxNDQwLCJhaCI6ODUyLCJjIjoyNH0=",
            "lgnjs": "1784281607",
            "lgnrnd": "024645_zDUr",
            "locale": "en_GB",
            "login_source": "comet_headerless_login",
            "lsd": "Mpso5QCLmk4=",
            "next": "https://www.facebook.com/dialog/oauth?client_id=2036793259884297&redirect_uri=https%253A%252F%252Fauth.garena.com%252Funiversal%252Foauth%252Ffacebook&response_type=token&scope=public_profile%252Cemail%252Cuser_friends%252Cuser_link&state=94e81a8bc7c546639f1bd76c25fe3bd6-platform%253D3%2526response_type%253Dcode%2526client_id%253D100067%2526redirect_uri%253Dhttps%25253A%25252F%25252Fzdauth.garena.com%25252Flogin%25253Freturn_to%25253Dhttps%25253A%25252F%25252Fffsupport.garena.com%25252Fhc%25252Fen-us&ret=login&fbapp_pres=0&logger_id=86af918c-a25d-49f6-94f0-f090c83ee33e&tp=unspecified",
            "prefill_contact_point": "",
            "prefill_source": "",
            "prefill_type": "",
            "skstamp": "",
            "timezone": "-330"
        },
        "credential_type": "password",
        "dyi_job_id": "",
        "enc_password": {
            "sensitive_string_value": encrypted_password  # Using the generated encrypted password
        },
        "event_request_id": "e42c01d8-3326-4e5b-affe-6a6ee78d21ff",
        "identifier": PHONE_NUMBER,  # Using the phone number variable
        "ig_web_device_id": None,
        "initial_request_id": "1",
        "lids": None,
        "login_source": "LOGIN",
        "next": "https://www.facebook.com/dialog/oauth?client_id=2036793259884297&redirect_uri=https%3A%2F%2Fauth.garena.com%2Funiversal%2Foauth%2Ffacebook&response_type=token&scope=public_profile%2Cemail%2Cuser_friends%2Cuser_link&state=94e81a8bc7c546639f1bd76c25fe3bd6-platform%3D3%26response_type%3Dcode%26client_id%3D100067%26redirect_uri%3Dhttps%253A%252F%252Fzdauth.garena.com%252Flogin%253Freturn_to%253Dhttps%253A%252F%252Fffsupport.garena.com%252Fhc%252Fen-us&ret=login&fbapp_pres=0&logger_id=86af918c-a25d-49f6-94f0-f090c83ee33e&tp=unspecified",
        "passkey_payload": None,
        "password": {
            "sensitive_string_value": encrypted_password  # Using the generated encrypted password
        },
        "persistent": True,
        "query_params": "{\"skip_api_login\":\"1\",\"api_key\":\"2036793259884297\",\"kid_directed_site\":\"0\",\"app_id\":\"2036793259884297\",\"signed_next\":\"1\",\"next\":\"https://www.facebook.com/dialog/oauth?client_id=2036793259884297&redirect_uri=https%3A%2F%2Fauth.garena.com%2Funiversal%2Foauth%2Ffacebook&response_type=token&scope=public_profile%2Cemail%2Cuser_friends%2Cuser_link&state=94e81a8bc7c546639f1bd76c25fe3bd6-platform%3D3%26response_type%3Dcode%26client_id%3D100067%26redirect_uri%3Dhttps%253A%252F%252Fzdauth.garena.com%252Flogin%253Freturn_to%253Dhttps%253A%252F%252Fffsupport.garena.com%252Fhc%252Fen-us&ret=login&fbapp_pres=0&logger_id=86af918c-a25d-49f6-94f0-f090c83ee33e&tp=unspecified\",\"cancel_url\":\"https://auth.garena.com/universal/oauth/facebook?error=access_denied&error_code=200&error_description=Permissions+error&error_reason=user_denied&state=94e81a8bc7c546639f1bd76c25fe3bd6-platform%3D3%26response_type%3Dcode%26client_id%3D100067%26redirect_uri%3Dhttps%253A%252F%252Fzdauth.garena.com%252Flogin%253Freturn_to%253Dhttps%253A%252F%252Fffsupport.garena.com%252Fhc%252Fen-us#_=_\",\"display\":\"page\",\"locale\":\"en_GB\",\"pl_dbl\":\"0\",\"is_business_login\":\"0\"}",
        "trusted_device_records": "{}",
        "use_uid_to_login": False,
        "waterfall_id": "092132d4-2843-4c3e-ac53-41472756ef2c"
    },
    "scale": 1
}

# Convert variables to JSON string
variables_json = json.dumps(variables_dict)

data = {
    'av': '0',
    '__aaid': '0',
    '__user': '0',
    '__a': '1',
    '__req': 'd',
    '__hs': '20651.HYP:comet_loggedout_pkg.2.1...0',
    'dpr': '1',
    '__ccg': 'EXCELLENT',
    '__rev': '1043351526',
    '__s': 'to81iy:a2bbzy:c9lktc',
    '__hsi': '7663431141814762144',
    '__dyn': '7xeUmwlE7ibwKBAg5S1Dxu13w8CewSwMwNw9G2S0lW4o0B-q1ew6ywaq0yE7i0n24oaEd86a3a1YwBgao6C0Mo2swaO4U2zxe2GewbS361qw8Xxm16wa-0raazo7u0zE2ZwrU6qE15E6O1FwlA1HGp1yU5Oi2K1Tw8q0JUhw5yw66w9O3mdw',
    '__csr': 'shs2wzYBNl4EhGXhmDQimrykKcUyq6d6-Hh9E-WLiCKp3Kmy95ypJup4CiSayWoZvhWVGpHRWz9UG13xe15wHDxNabCxK7ER1aewNDwJxS3xeEqgy4UK3K3x0xG221ZDU5u5A5Q8w7Jw5nwbG0z8S024W2S780d9k13hQt00YxhQ2ahw1y20eBw3XUJkywgpU3dwe60qq01ZFw0u9o0xesw0mPw0GhxB1O06Do0xZ017204HUBO018K0fZo1Ui0dN00A9g0zF2o19200hBFE0s9wEp80nkAwaN00LMBAm0SXBAw',
    '__hsdp': 'gc-g5IbN5Aw11y1gw2ZU6q2a01axw3qE0Ae',
    '__hblp': '0bm0ffwlU520bTwpE8E3Qw8Kdw3ro1K80Ma02dGdw3qE0Ae5EdU5q7839w25E3zwca08lwgE26xe0XE1Ho76',
    '__sjsp': 'gc-gaNcr2Yhp80hFw',
    '__comet_req': '15',
    'locale': 'en_GB',
    'fb_dtsg': 'Mpso5QCLmk4=',
    'jazoest': '21021',
    'lsd': 'wkEB6DkikroblzgG--A07m',
    '__spin_r': '1043351526',
    '__spin_b': 'trunk',
    '__spin_t': '1784281605',
    'qpl_active_flow_ids': '516759801',
    'fb_api_caller_class': 'RelayModern',
    'fb_api_req_friendly_name': 'useCDSWebLoginMutation',
    'server_timestamps': 'true',
    'variables': variables_json,
    'doc_id': '9807605492696448',
    'fb_api_analytics_tags': '["qpl_active_flow_ids=516759801"]',
}

response = requests.post('https://www.facebook.com/api/graphql/', cookies=cookies, headers=headers, data=data)

print("Status Code:", response.status_code)
print("\nResponse:")
try:
    result = response.json()
    print(json.dumps(result, indent=2))
    
    # Check for errors
    if 'data' in result and 'caa_login_web' in result['data']:
        login_data = result['data']['caa_login_web']
        if 'error_code' in login_data:
            error_msg = login_data.get('error_message', {}).get('text', 'Unknown error')
            print(f"\n❌ Login Failed: {error_msg}")
        elif 'redirect_uri' in login_data:
            print(f"\n✅ Login Successful! Redirect URI: {login_data.get('redirect_uri')}")
        else:
            print("\n✅ Login Successful!")
except json.JSONDecodeError:
    print(response.text)
