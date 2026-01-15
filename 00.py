import requests

cookies = {
    'datr': 'Z1hMaIrIfVNAp27gtWl_jtL1',
    'sb': 'Z1hMaKlrQMZu6pNj3IH-tWgs',
    'ps_l': '1',
    'ps_n': '1',
    'fr': '029IlyRZmpwIAbBNq..Bo1FYF..AAA.0.0.BpaUC7.AWeK1U_dowKlORzca7lX-Nn6j2Q',
    'wd': '919x773',
    'sfiu': 'AYjdbp6OPuuwQIEVNyVP2gQLKymsMKgGkcNQL5J-0fIGxwVRTIM35KADg5dXz8JUhQEFHNOfMaYfG1qXSwvu2G1S4c7RpPNfuAff6HOs9tjzM0bXKwEVlxuP3W1ZtnoOblpxRrSVt2L8xcE2nPhdu15TzMYYU5ZXZVaHPTmFxpy3W9Dd-giFXI3d125Iy1qEX7YrYHeftoRAYG3movhrXtUBbXeD4MgIlGQXBCSMnqt6QQ',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,bn;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://www.facebook.com',
    'priority': 'u=1, i',
    'referer': 'https://www.facebook.com/login/identify/?ctx=not_my_account',
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
    'x-fb-lsd': 'AdGpHjOQEFs',
    # 'cookie': 'datr=Z1hMaIrIfVNAp27gtWl_jtL1; sb=Z1hMaKlrQMZu6pNj3IH-tWgs; ps_l=1; ps_n=1; fr=029IlyRZmpwIAbBNq..Bo1FYF..AAA.0.0.BpaUC7.AWeK1U_dowKlORzca7lX-Nn6j2Q; wd=919x773; sfiu=AYjdbp6OPuuwQIEVNyVP2gQLKymsMKgGkcNQL5J-0fIGxwVRTIM35KADg5dXz8JUhQEFHNOfMaYfG1qXSwvu2G1S4c7RpPNfuAff6HOs9tjzM0bXKwEVlxuP3W1ZtnoOblpxRrSVt2L8xcE2nPhdu15TzMYYU5ZXZVaHPTmFxpy3W9Dd-giFXI3d125Iy1qEX7YrYHeftoRAYG3movhrXtUBbXeD4MgIlGQXBCSMnqt6QQ',
}

params = {
    'ctx': 'not_my_account',
}

data = {
    'jazoest': '2940',
    'lsd': 'AdGpHjOQEFs',
    'email': '2250769450961',
    'did_submit': '1',
    '__user': '0',
    '__a': '1',
    '__req': '6',
    '__hs': '20468.BP:DEFAULT.2.0...0',
    'dpr': '1',
    '__ccg': 'EXCELLENT',
    '__rev': '1032049861',
    '__s': 'sflqtb:my7aaa:6evjim',
    '__hsi': '7595674312159156008',
    '__dyn': '7xeUmwkHg7ebwKBAg5S1Dxu13wqovzEdEc8uxa0CEbo1nEhw2nVE4W0qa0FE2awt81s8hwGwQw4iwBgao6C0Mo2swaO4U2zxe3C0D85a1qw8Xxm16wa-0raazo7u0zE2ZwrU6C0hq1Iw5lwnqwIwtU5K0UE62',
    '__hsdp': 'gIMggq8yqA7h0hp3D8py4bDyeeqKEyewQocAE7iO04Ewd63B240GGw4iw',
    '__hblp': '0TwbO1nw5Uw3iUfE4-0a6wto0lUw28E08qU0hjw2A805h60c-w3YJ0fO6oll02ZU0qPw13i0FU',
    '__spin_r': '1032049861',
    '__spin_b': 'trunk',
    '__spin_t': '1768505739',
}

response = requests.post(
    'https://www.facebook.com/ajax/login/help/identify.php',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
)
print(response.text)
