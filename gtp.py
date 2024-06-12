import requests

# Replace placeholders with actual values
fb = "m"
uuu =  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"

# Make the GET request with custom User-Agent header

# Define the headers dictionary
headers = {
    'Host': f'{fb}.facebook.com',
    'content-length': '1662',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Android WebView";v="120"',
    'sec-ch-ua-mobile': '?1',
    'user-agent': uuu,
    'x-response-format': 'JSONStream',
    'content-type': 'application/x-www-form-urlencoded',
    'x-fb-lsd': 'AVrEIFcZUZg',
    'viewport-width': '360',
    'sec-ch-ua-platform-version': "",
    'x-requested-with': 'XMLHttpRequest',
    'x-asbd-id': '129477',
    'dpr': '2',
    'sec-ch-ua-full-version-list': '',
    'sec-ch-ua-model': "",
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua-platform': '"Android"',
    'accept': '*/*',
    'origin': f'https://{fb}.facebook.com',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': f'https://{fb}.facebook.com/login/?wtsid=rdr_0HpBBBchEc4DCrXrX&refsrc=deprecated&_rdr',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-IE,en-US;q=0.9,en;q=0.8'
}

# Make an example request using the headers
response = requests.get("https://example.facebook.com", headers=headers)

# Print the response status code
print(response.status_code)
