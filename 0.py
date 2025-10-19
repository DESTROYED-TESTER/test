import requests

url = "https://www.facebook.com/login/device-based/regular/login/?login_attempt=1"

headers = {
    "authority": "www.facebook.com",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "max-age=0",
    "content-type": "application/x-www-form-urlencoded",
    "cookie": "fr=0yNyOdBia7SurAz5e..Bo9J-7..AAA.0.0.Bo9J-7.AWcpcPtzmuPsw5P6FNpwX8Zx-Tw; sb=u5_0aFF51EbifVBDoEnsi9Ut; datr=u5_0aCroimhveeODthgePFtZ; dpr=2.4749999046325684; wd=980x1146",
    "origin": "https://www.facebook.com",
    "referer": "https://www.facebook.com/Facebookids",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
}

data = {
    "email": "100075835494521",
    "cuid": "",
    "guid": "f0a5a0c737fcfe167",
    "lgnjs": "1760862174",
    "lgnrnd": "012253_q6Bs",
    "locale": "en_GB",
    "login_source": "comet_login_header",
    "next": "https://www.facebook.com/Facebookids",
    "skstamp": "",
    "timezone": "-330",
    "prefill_contact_point": "",
    "prefill_source": "",
    "lsd": "AdFiLirodjc",
    "jazoest": "21051",
    "lgndim": '{"w":437,"h":973,"aw":437,"ah":973,"c":24}',
    "encpass": "#PWD_BROWSER:5:1760862597:AYFQAPJk/Ku98wxYP+NENCgrufR2Q6BgEykOumuNAhlLuYpyU8RPwONshbq6ts3NRm2/wZaj+Sd2/1rDr9A+/pogd+QQHuVyCyXisIR8DCbfMmtXVETkBZgt4rQjkpvxBasT1XhxN938Pw==",
}

response = requests.post(url, headers=headers, data=data)
print(response.text)
