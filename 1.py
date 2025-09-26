import requests
resp = requests.get("https://password-enc-api-instagram-facebook.p.rapidapi.com/api/pass_enc/",
                    headers={"x-rapidapi-key":"5b5179b509msh1ba72c98ba4d120p1e1335jsn6eb28abafc48","x-rapidapi-host":"password-enc-api-instagram-facebook.p.rapidapi.com"},
                    params={"p":"Password123 ","v":"5","m":"fbweb"}).json()
print(resp.get('pass') or resp.get('password') or resp.get('enc') or resp.get('encpass') or resp.get('result') or (resp[0] if isinstance(resp, list) and resp else (next(iter(resp.values())) if isinstance(resp, dict) and resp else resp)))
