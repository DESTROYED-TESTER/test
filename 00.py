import requests
r = requests.get("https://api.telegram.org/bot{token}/getMe".format(token="YOUR_TOKEN"))
print(r.json())
