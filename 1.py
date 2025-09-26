import requests
resp = requests.get("https://password-enc-api-instagram-facebook.p.rapidapi.com/api/pass_enc/",
                    headers={"x-rapidapi-key":"5b5179b509msh1ba72c98ba4d120p1e1335jsn6eb28abafc48","x-rapidapi-host":"password-enc-api-instagram-facebook.p.rapidapi.com"},
                    params={"p":"Password123 ","v":"5","m":"fbweb"}).json()
encpass = f'"{resp.get("pass") or resp.get("encpass") or resp.get("result") or next(iter(resp.values()))}"'

print(encpass)
