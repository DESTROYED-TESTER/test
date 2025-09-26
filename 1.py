import requests

url = "https://password-enc-api-instagram-facebook.p.rapidapi.com/api/pass_enc/"

querystring = {"p":"Password123 ","v":"11","m":"fbweb"}

headers = {
	"x-rapidapi-key": "5b5179b509msh1ba72c98ba4d120p1e1335jsn6eb28abafc48",
	"x-rapidapi-host": "password-enc-api-instagram-facebook.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
