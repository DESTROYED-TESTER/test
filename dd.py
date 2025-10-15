import requests

cookies = {
    'fr': '03FkyNUH8Xs9BzEhq..Bol1P1..AAA.0.0.Bol1Qn.AWdeEfvDYB6IBgOppR3qjKJYAMc',
    'sb': '9VOXaIC7uKaEAUBNMFwz6Rab',
    'wd': '1161x773',
    'datr': '9VOXaIU6dreqR00c2_K1j5aS',
    'checkpoint': '%7B%22u%22%3A61577619472768%2C%22t%22%3A1754747927%2C%22step%22%3A0%2C%22n%22%3A%222QYdRwatT74%3D%22%2C%22inst%22%3A122117129318920649%2C%22f%22%3A190115151632257%2C%22st%22%3A%22c%22%2C%22aid%22%3Anull%2C%22ca%22%3Anull%2C%22la%22%3A%22%22%2C%22ta%22%3A%221754747930.ch.s%3Apw.tDBGAiEAl3dnEy8gpzix6rGXM1q9AmlGwjcTMB-suwCKJJg90gsCIQDLlzNqRpceY33VkqDNBZ0a7l5j9G9XPZCm86kHkBzLBw%22%2C%22tfvaid%22%3Anull%2C%22tfvasec%22%3Anull%2C%22sat%22%3Anull%2C%22idg%22%3Afalse%2C%22cidue%22%3A%22%22%2C%22tfuln%22%3Anull%2C%22tfvri%22%3Anull%2C%22ct%22%3Anull%2C%22s%22%3A%22AWVsLuFggZ5iVevaiys%22%2C%22cs%22%3A%5B%5D%2C%22ssp%22%3A1%7D',
    'locale': 'en_US',
    'ps_l': '1',
    'ps_n': '1',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://www.facebook.com',
    'priority': 'u=1, i',
    'referer': 'https://www.facebook.com/',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    'sec-ch-ua-full-version-list': '"Not)A;Brand";v="8.0.0.0", "Chromium";v="138.0.7204.184", "Google Chrome";v="138.0.7204.184"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
    'x-asbd-id': '359341',
    'x-fb-friendly-name': 'useCDSWebLoginMutation',
    'x-fb-lsd': 'mswwoOE3q42hfqz6UqOVF9',
}

data = {
    'av': '0',
    '__user': '0',
    '__a': '1',
    '__req': 'q',
    '__hs': '20309.HYP:comet_plat_default_pkg.2.1...0',
    'dpr': '1',
    '__ccg': 'MODERATE',
    '__rev': '1025714034',
    '__s': '88msk0:1sipzk:9u9t17',
    '__hsi': '7536585028377713169',
    '__dyn': '7xeUmwlEnwn8K2Wmh0no6u5U4e0yoW3q32360CEbo1nEhw2nVE4W0qa0FE2awpUO0n24oaEd82lwv89k2C1Fwc60D82IzXwae4UaEW0Loco5G0zK5o4q0HU1IEGdwtU2ewbS1Lwqo15E6O1FwlU6KaxyU5N90HwtU5K0UEhwjE',
    '__csr': 'gMz9iYTSbFJmDKP2AFUK8yXQAVk4uchGFR8lW9XBWQZAXLpi4iWGZvypqKidrHgowIxa7898nCCwyx-7U7a1gVoO1lwh8yi5E4K2C15wXxCfwjU6y0Z82JwUwywlUrwbq487e0EE761owv85e07YUfp2U04F2m0c2ixy03z2U03_mm0_U0311wfW01nFxuhw0kGoG0fHg1b8',
    '__hsdp': 'g-gk6FA4mjOlxyFFOyFp8wkp4AgN5gK2yufxy3fBzU7C3B2U0GV5wci3GEcAa5ZKEsxHgfE2ng2Pw4ww47xO19w1bi05lo6a06Bk0K81Co1N1g0Rq02BG08Cw2vo0Ma0rO07RU1Zo0rqw2W8',
    '__hblp': '01UC05180Le02vK0ccw3po0dIU1i83tw2vo0Ma0rO0hi0a9w3TU5y1YwZwso28wzxK0SU14Ey0Ko2sw3v8W0xE0C61Hwey',
    '__sjsp': 'g-gk6FA4mjOk6GCDaaBAy1hAih34l2Ua9U-68c-mfwuoekbw2HAm0N8eGwOyNvpEsxHgfE2nwbi0i20gu784C02wG1yw1Fl02kE1N1g0Rq',
    '__comet_req': '1',
    'fb_dtsg': '2QYdRwatT74=',
    'jazoest': '2986',
    'lsd': 'mswwoOE3q42hfqz6UqOVF9',
    '__spin_r': '1025714034',
    '__spin_b': 'trunk',
    '__spin_t': '1754747943',
    'fb_api_caller_class': 'RelayModern',
    'fb_api_req_friendly_name': 'useCDSWebLoginMutation',
    'variables': '{"input":{"client_mutation_id":"2","actor_id":"0","app":"facebook","identifier":"100051096438777","credential_type":"password","enc_password":{"sensitive_string_value":"#PWD_BROWSER:0:1754601235:630133"},"persistent":true,"trusted_device_records":"{}"}}',
    'server_timestamps': 'true',
    'doc_id': '24540252778892185',
}

response = requests.post(
    'https://www.facebook.com/api/graphql/',
    cookies=cookies,
    headers=headers,
    data=data,
)

print("HTTP status:", response.status_code)
print("Response headers:", dict(response.headers))
# If the body is JSON, this will print it; otherwise it will show the raw text (trimmed)
try:
    j = response.json()
    import json
    print("JSON response (pretty):\n", json.dumps(j, indent=2)[:4000])  # trim long output
except ValueError:
    print("Response text (trimmed):\n", response.text[:4000])

# Inspect cookies set by the server
print("Response cookies:", response.cookies.get_dict())

# Quick heuristics (not definitive):
if response.status_code in (200, 302):
    print("Status looks like OK (200/302).")
else:
    print("Non-OK HTTP status; likely failure or block.")

# Heuristic checks:
if 'c_user' in response.cookies.get_dict():
    print("c_user cookie present — likely a logged-in session (but not guaranteed).")
if isinstance(j, dict) and j.get('errors'):
    print("GraphQL returned errors:", j.get('errors'))
