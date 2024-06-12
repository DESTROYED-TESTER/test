import requests

# Define the URL of the Facebook endpoint you want to request
url = "https://www.facebook.com"

# Define browser-like headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Referer": "https://www.facebook.com/login.php",
    "Content-Type": "application/x-www-form-urlencoded",
    "Content-Length": "632",
    "Origin": "https://www.facebook.com",
    "DNT": "1",
    "Connection": "keep-alive",
    "Cookie": "fr=0Ge9olQRX9wxG4dUG.AWUTUAwuqOhx6vVGzCzLNdVsXuU.BmQamB..AAA.0.0.BmaaFJ.AWW7oCfia6c; sb=galBZijJE3gDNJ8fh_fhANhG; datr=galBZo6ZvqtwWhtJgd_gsfBQ; ps_n=1; ps_l=1; wd=1440x402; _js_datr=galBZo6ZvqtwWhtJgd_gsfBQ",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Priority": "u=1",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache",
    "TE": "trailers"
}

# Make the GET request with browser-like headers
response = requests.get(url, headers=headers)

# Print the status code and headers
print("Status Code:", response.status_code)
print("Headers:", response.headers)
