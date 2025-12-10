import requests
import time
import random
import uuid
import json
import urllib.parse


def instagram_login(username, password):

    s = requests.Session()

    # INITIAL HEADERS (valid mobile Instagram Android request)
    s.headers.update({
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

    family = s.headers["X-IG-Family-Device-ID"]
    android = s.headers["X-IG-Android-ID"]
    bloks = s.headers["X-Bloks-Version-Id"]

    # REAL JSON PARAMS (NOT PYTHON DICT FORMAT)
    params_json = {
        "client_input_params": {
            "contact_point": username,
            "password": f"#PWD_INSTAGRAM:0:{int(time.time())}:{password}",
            "event_flow": "login",
            "family_device_id": family,
            "device_id": android,
            "login_attempt_count": 1
        },
        "server_params": {
            "credential_type": "password",
            "family_device_id": family,
            "waterfall_id": str(uuid.uuid4())
        }
    }

    # convert to real JSON (important!)
    params_encoded = urllib.parse.quote(json.dumps(params_json, separators=(",", ":")))

    bk_context = urllib.parse.quote(
        json.dumps({
            "bloks_version": bloks,
            "styles_id": "instagram"
        })
    )

    final_body = (
        f"params={params_encoded}"
        f"&bk_client_context={bk_context}"
        f"&bloks_versioning_id={bloks}"
    )

    # SEND REQUEST
    res = s.post(
        "https://b.i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.login.async.send_login_request/",
        data=final_body
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
