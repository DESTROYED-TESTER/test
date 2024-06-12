import requests

# Define the URL of the Facebook endpoint you want to request
url = "https://www.facebook.com"

# Define browser-like headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.5",
    # Add any other headers you may need
}

# Make the GET request with browser-like headers
response = requests.get(url, headers=headers)

# Print the status code and headers
print("Status Code:", response.status_code)
print("Headers:", response.headers)
