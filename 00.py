import requests
r = requests.get("https://api.telegram.org/bot{token}/getMe".format(token="7495165574:AAEsmwWrR5DAhFFDRzeCptgTVEVCgYxG3n4"))
print(r.json())
