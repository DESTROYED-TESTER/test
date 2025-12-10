import requests
import time
import random
import uuid
import json
import urllib.parse


def instagram_login(username, password):

    Session = requests.Session()

    # INITIAL HEADERS (valid mobile Instagram Android request)
    Session.headers.update({
        "User-Agent": "Instagram 289.0.0.22.45 Android",
        "Accept-Language": "en-US",
        "X-IG-App-ID": "567067343352427",
        "X-IG-Device-ID": str(uuid.uuid4()),
        "X-IG-Family-Device-ID": str(uuid.uuid4()),
        "X-IG-Android-ID": "android-" + uuid.uuid4().hex[:16],
        "X-Bloks-Version-Id": "7b4ecdd5f3ef5373b73011c4af55d31f",
        "X-Pigeon-Rawclienttime": str(time.time()),
        "X-IG-Bandwidth-Speed-KBPS": str(random.randint(100, 300)),
        "X-IG-Bandwidth-TotalBytes-B": str(random.randint(600000, 900000)),
        "X-IG-Bandwidth-TotalTime-MS": str(random.randint(300, 9000)),
    })

    family = Session.headers["X-IG-Family-Device-ID"]
    android = Session.headers["X-IG-Android-ID"]
    bloks = Session.headers["X-Bloks-Version-Id"]

    # REAL JSON PARAMS (NOT PYTHON DICT FORMAT)
    DataRec = {
        'params': json.dumps({
            "client_input_params": {
                "contact_point": '7029868180',
                "password": f"#PWD_INSTAGRAM:0:{int(time.time())}:{'sumon@12M'}",
                "login_step": "PASSWORD",
                "flow": "LOGIN",
                "family_device_id": session.headers['x-ig-family-device-id'],
                "device_id": session.headers['x-ig-android-id'],
                "machine_id": session.headers.get('x-mid', ''),
                "login_attempt_count": 1,
                "should_upgrade_password": False,
                "secure_device_id": "",
                "device_emails": [],
                "encrypted_msisdn": ""
            },

            "server_params": {
                "credential_type": "password",
                "server_login_source": "device_based_login",
                "is_platform_login": False,
                "is_from_logged_out": False,
                "login_source": "LoginRequest",
                "family_device_id": session.headers['x-ig-family-device-id'],
                "waterfall_id": str(uuid.uuid4()),
                "should_trigger_2fa": False,
                "should_trigger_success_action": True
            }
        }),

        'bk_client_context': json.dumps({
            "bloks_version": session.headers['x-bloks-version-id'],
            "styles_id": "instagram"
        }),

        'bloks_versioning_id': session.headers['x-bloks-version-id']
    }

    Query = (
        "params=%s&bk_client_context=%s&bloks_versioning_id=%s"
        % (
            urllib.parse.quote(DataRec['params']),
            urllib.parse.quote(DataRec['bk_client_context']),
            DataRec['bloks_versioning_id']
        )
    )
    # SEND REQUEST
    res = s.post(
        "https://b.i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.login.async.send_login_request/",
        data=Query
    )

    txt = res.text.replace("\\", "")

    # LOGIN CHECK
    if "logged_in_user" in txt:
        print("✅ LOGIN SUCCESS\n")

        ck = s.cookies.get_dict()
        print("ds_user_id:", ck.get("ds_user_id"))
        print("sessionid :", ck.get("sessionid"))

    else:
        print("❌ LOGIN FAILED")
        print(res.text)


# RUN
instagram_login("7029868180", "sumon@12M")
