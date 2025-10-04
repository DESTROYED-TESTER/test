import requests
r = requests.get("https://api.telegram.org/bot{token}/getMe".format(token="8301704871:AAGbBRYqENld4lERHxK5G3DjIOdAWIZqBbY"))
print(r.json())
