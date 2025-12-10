import requests
import time
import random
import uuid
import urllib.parse


def instagram_login(username, password):

    session = requests.Session()

    # -----------------------
    # HEADERS
    # -----------------------
    session.headers.update({
        'x-pigeon-rawclienttime': '{:.3f}'.format(time.time()),
        'x-ig-bandwidth-speed-kbps': str(random.randint(100, 300)),
        'x-ig-bandwidth-totalbytes-b': str(random.randint(500000, 900000)),
        'x-ig-bandwidth-totaltime-ms': str(random.randint(1000, 9000)),
        'user-agent': 'Instagram 290.0.0.0.56 Android',
        'x-ig-android-id': 'android-' + uuid.uuid4().hex[:16],
        'x-ig-family-device-id': str(uuid.uuid4()),
        'x-ig-device-id': str(uuid.uuid4()),
        'x-bloks-version-id': "f4a87d1dfb3f1231e56aa9a1922fc121",  # static / acceptable
    })

    android_id = session.headers['x-ig-android-id']
    family_device = session.headers['x-ig-family-device-id']
    bloks_vid = session.headers['x-bloks-version-id']

    # -----------------------
    # REQUEST BODY
    # -----------------------
    params = {
        "client_input_params": {
            "contact_point": username,
            "password": f"#PWD_INSTAGRAM:0:{int(time.time())}:{password}",
            "event_flow": "account_recovery",
            "family_device_id": family_device,
            "machine_id": "",
            "accounts_list": [],
            "has_whatsapp_installed": 0,
            "login_attempt_count": 1,
            "device_id": android_id
        },
        "server_params": {
            "credential_type": "password",
            "family_device_id": family_device,
            "waterfall_id": str(uuid.uuid4())
        }
    }

    data = {
        "params": urllib.parse.quote(str(params).replace("'", '"')),
        "bk_client_context": urllib.parse.quote(
            '{"bloks_version":"'+bloks_vid+'","styles_id":"instagram"}'
        ),
        "bloks_versioning_id": bloks_vid
    }

    final_payload = (
        f"params={data['params']}"
        f"&bk_client_context={data['bk_client_context']}"
        f"&bloks_versioning_id={data['bloks_versioning_id']}"
    )

    # -----------------------
    # SEND LOGIN REQUEST
    # -----------------------
    response = session.post(
        "https://b.i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.login.async.send_login_request/",
        data=final_payload,
        allow_redirects=True
    )

    text = response.text.replace("\\", "")

    # -----------------------
    # CHECK LOGIN SUCCESS
    # -----------------------
    if "logged_in_user" in text:
        print("\n✅ LOGIN SUCCESS\n")

        cookies = session.cookies.get_dict()

        print("ALL COOKIES:")
        for k, v in cookies.items():
            print(f"{k} = {v}")

        print("\nIMPORTANT:")
        print("ds_user_id =", cookies.get("ds_user_id"))
        print("sessionid  =", cookies.get("sessionid"))

    else:
        print("\n❌ LOGIN FAILED")
        print(text)


# -------------------------------
# RUN LOGIN
# -------------------------------
instagram_login("7029868180", "sumon@12M")
