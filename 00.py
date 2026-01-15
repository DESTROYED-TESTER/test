import requests

cookies = {
    'datr': 'Z1hMaIrIfVNAp27gtWl_jtL1',
    'sb': 'Z1hMaKlrQMZu6pNj3IH-tWgs',
    'ps_l': '1',
    'ps_n': '1',
    'fr': '029IlyRZmpwIAbBNq..Bo1FYF..AAA.0.0.BpaTvn.AWd1mkS91mFpI7Ttg-VO4Ke0D9I',
    'sfiu': 'AYhEtjW65wh_fZmdUGpXTqQmpURgen3ZxRbUPCfOa7Uau_1bKuXwFy3GzPMsimvpW9FmaGwqvKqk25IBu0I7Yn3ugIQWaI3kHqHkXL60VkYDtayIAYq-k-dEa6KnhwATRTIEq5ChnA7BSdYSfA2ujVt1qCOc_Urre6QVjfHM8AhSnPQhmsZlq29Vy-kz55CKg74A7t2ofSzsQOs74Wu6phvRs0dRpveBmcwgOMRYUTZO5g',
    'wd': '682x773',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,bn;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://www.facebook.com',
    'priority': 'u=1, i',
    'referer': 'https://www.facebook.com/login/identify/?ctx=recover&ars=facebook_login&from_login_screen=0',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"',
    'sec-ch-ua-full-version-list': '"Google Chrome";v="143.0.7499.170", "Chromium";v="143.0.7499.170", "Not A(Brand";v="24.0.0.0"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',
    'x-asbd-id': '359341',
    'x-fb-lsd': 'AdGpHjOQPyI',
    # 'cookie': 'datr=Z1hMaIrIfVNAp27gtWl_jtL1; sb=Z1hMaKlrQMZu6pNj3IH-tWgs; ps_l=1; ps_n=1; fr=029IlyRZmpwIAbBNq..Bo1FYF..AAA.0.0.BpaTvn.AWd1mkS91mFpI7Ttg-VO4Ke0D9I; sfiu=AYhEtjW65wh_fZmdUGpXTqQmpURgen3ZxRbUPCfOa7Uau_1bKuXwFy3GzPMsimvpW9FmaGwqvKqk25IBu0I7Yn3ugIQWaI3kHqHkXL60VkYDtayIAYq-k-dEa6KnhwATRTIEq5ChnA7BSdYSfA2ujVt1qCOc_Urre6QVjfHM8AhSnPQhmsZlq29Vy-kz55CKg74A7t2ofSzsQOs74Wu6phvRs0dRpveBmcwgOMRYUTZO5g; wd=682x773',
}

params = {
    'ctx': 'recover',
}

data = {
    'jazoest': '2960',
    'lsd': 'AdGpHjOQPyI',
    'email': '2250769455873',
    'did_submit': '1',
    '__user': '0',
    '__a': '1',
    '__req': '5',
    '__hs': '20468.BP:DEFAULT.2.0...0',
    'dpr': '1',
    '__ccg': 'GOOD',
    '__rev': '1032045955',
    '__s': 'd7q969:my7aaa:223ytn',
    '__hsi': '7595668200809741113',
    '__dyn': '7xeUmwkHg7ebwKBAg5S1Dxu13wqovzEdEc8uxa0CEbo1nEhw2nVE4W0qa0FE2awt81s8hwGwQw4iwBgao6C0Mo2swaO4U2zxe3C0D85a1qw8Xxm16wa-0raazo7u0zE2ZwrU6C0hq1Iw5lwnqwIwtU5K0UE62',
    '__hsdp': 'gIMggq8yqA6hisXy44U_hRK8UZXG8z8d63lwury60i60CU6t240Fk0k2',
    '__hblp': '0UwbK1nw5Yw3qUeobo0AW0BU0m1w7Mw0J9w1fG018Zw1nG0fFQ0-Ua9y03ve063U0hgw8a',
    '__spin_r': '1032045955',
    '__spin_b': 'trunk',
    '__spin_t': '1768504316',
}

response = requests.post(
    'https://www.facebook.com/ajax/login/help/identify.php',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
)
print(response.text)
