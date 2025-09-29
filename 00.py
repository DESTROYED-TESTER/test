import requests
r = requests.get("https://api.telegram.org/bot{token}/getMe".format(token="7858153099:AAGO1QR21zy2sqVW9K8hIlnPz7vxQ1LzqHg"))
print(r.json())
