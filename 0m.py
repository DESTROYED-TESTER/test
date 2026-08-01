import requests

cookies = {
    'datr': 'WXltatd2ENUjZUyfA3yVvrhw',
    'sb': 'gXltaqNiraYlzznawgFOc3Qf',
    'locale': 'bn_IN',
    'wd': '1143x773',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,bn;q=0.8',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    'dpr': '1',
    'origin': 'https://www.messenger.com',
    'priority': 'u=0, i',
    'referer': 'https://www.messenger.com/login/',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Google Chrome";v="145", "Chromium";v="145"',
    'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Google Chrome";v="145.0.7632.5", "Chromium";v="145.0.7632.5"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36',
    'viewport-width': '1143',
    # 'cookie': 'datr=WXltatd2ENUjZUyfA3yVvrhw; sb=gXltaqNiraYlzznawgFOc3Qf; locale=bn_IN; wd=1143x773',
}

data = {
    'jazoest': '22474',
    'lsd': 'AdRRDLpqanHVfvAWy_sUXtH_OJc',
    'initial_request_id': 'A10tPfatOkwvT0WG7gWVNnY',
    'timezone': '-330',
    'lgndim': 'eyJ3IjoxNDQwLCJoIjo5MDAsImF3IjoxNDQwLCJhaCI6ODYwLCJjIjozMn0=',
    'lgnrnd': '214622_uurZ',
    'lgnjs': 'n',
    'email': '9749797453',
    'pass': '#PWD_BROWSER:5:1785559664:AZ5QAOWfT8EO2FqaVqWoHd8xdImXBZXJ4mbWDqdkbNxndqh1Zhdc2gNQ35LlRHRtpLRQ66HmREl8z9XkhNXm5vumHq7GgpetBsvVZhPwzD4N1sFDJtsq62iZ9xbKwl/MYQMt/EMOOSaRq/bA',
    'default_persistent': '',
}

response = requests.post('https://www.messenger.com/login/password/', cookies=cookies, headers=headers, data=data)
print(response.text)
