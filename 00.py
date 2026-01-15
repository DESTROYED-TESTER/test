import requests

cookies = {
    'datr': 'Z1hMaIrIfVNAp27gtWl_jtL1',
    'sb': 'Z1hMaKlrQMZu6pNj3IH-tWgs',
    'ps_l': '1',
    'ps_n': '1',
    'wd': '919x773',
    'fr': '029IlyRZmpwIAbBNq..Bo1FYF..AAA.0.0.BpaUUa.AWfZWcfcYse7Zb02qMdcf2LAh9I',
    'sfiu': 'AYj2lsDI4RgV_ATFq3p7kK4n_Ob-fb6YHfUnFi-k1tssUCTRBk3e1OBkKrjfvRAd4uqwM3Al32rlc6G4uU6PYOMH2RW5fZfgY4aUa6KKpIJotMp3h7TMVnY8CaPgWTXsO021_lGcUgZteL6VdKw3370FYZmt1WVhdlvbo1XdoERdhefpPOOOpe741GJptFEwNZ5vrNC_E5xHAfTPNYqrNzb97aRVHwyE-q-qcDAeHEXmmg',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,bn;q=0.8',
    'dpr': '1',
    'priority': 'u=0, i',
    'referer': 'https://www.facebook.com/recover/initiate/?is_from_lara_screen=1',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"',
    'sec-ch-ua-full-version-list': '"Google Chrome";v="143.0.7499.170", "Chromium";v="143.0.7499.170", "Not A(Brand";v="24.0.0.0"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',
    'viewport-width': '919',
    # 'cookie': 'datr=Z1hMaIrIfVNAp27gtWl_jtL1; sb=Z1hMaKlrQMZu6pNj3IH-tWgs; ps_l=1; ps_n=1; wd=919x773; fr=029IlyRZmpwIAbBNq..Bo1FYF..AAA.0.0.BpaUUa.AWfZWcfcYse7Zb02qMdcf2LAh9I; sfiu=AYj2lsDI4RgV_ATFq3p7kK4n_Ob-fb6YHfUnFi-k1tssUCTRBk3e1OBkKrjfvRAd4uqwM3Al32rlc6G4uU6PYOMH2RW5fZfgY4aUa6KKpIJotMp3h7TMVnY8CaPgWTXsO021_lGcUgZteL6VdKw3370FYZmt1WVhdlvbo1XdoERdhefpPOOOpe741GJptFEwNZ5vrNC_E5xHAfTPNYqrNzb97aRVHwyE-q-qcDAeHEXmmg',
}

response = requests.get(
    'https://www.facebook.com/recover/code/?ph[0]=%2B2250769453355&rm=send_sms&cuid=AYi9DHgy7W7OHInly78VDyNgy5zQMOhPkQtx8ObEltJ7QdwirOm3CmK8nTTvP0vWObYozULhhY_70GDxLQqIjzdNBCAZeuFe5mu0SPaWiOioMnHZVdPdZ6ZAw1Z8wR1DQW_bt3be8AtRDiRSd2e2gzo1urqoHwzlayQYStLQWYpj9g0Fa0Y_nJQ-iueD5_Z8ujqMuCndYvUeghtCQCd9hC5RHSgd4zyBNQPi3vMq2Yyr2A&lara=1&hash=AUbnHlUBVqP8uQhLN9w',
    cookies=cookies,
    headers=headers,
)
print(response.text)
