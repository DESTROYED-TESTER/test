import requests

cookies = {
    'datr': 'Z1hMaIrIfVNAp27gtWl_jtL1',
    'sb': 'Z1hMaKlrQMZu6pNj3IH-tWgs',
    'ps_l': '1',
    'ps_n': '1',
    'fr': '029IlyRZmpwIAbBNq..Bo1FYF..AAA.0.0.BpaTvn.AWd1mkS91mFpI7Ttg-VO4Ke0D9I',
    'wd': '682x773',
    'sfiu': 'AYhaeBZ-JN1zNIWJ9eSV-PS1Z232o2m30DNuAsZgCXXJjZ4LZNyrsFqutKwZqaRj21YdMypPVvwwBw87S5UxWBhDlAurGNAzlUpr3GCUWq0ezJeEI9yC-eakUX4Z6YXn_0iBq46EMkYO1xiKWaGgQQiw65fkFxSqgRP2LFN0cS5CA5C09RoisWJ3iUNutEW6Ss1mlZgQIGDb2xb-2Fq4AVA0GlU6K-PMIeFrKm2TlOytEQ',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,bn;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://www.facebook.com',
    'priority': 'u=1, i',
    'referer': 'https://www.facebook.com/recover/initiate/?ldata=AWf1GdMFBgc1jRR9u6WBO2FljEEMRQowP5PFbDkzjWMDd-igO1nER80ESDw9veLaUmd5SJKpfjgInKoMlnAu5Y3rMoh_SpFTCDMzTqIUicdOViWG6Ba2JfnHlhTmVY7u3fOiopfc9bLyKtIKTR74GXohPFmfVP9nZL5hATkkAXkR8LrdlFHur-y5ZskK0jJlAqLdlh72wC0wJLOSPZj_dZ3IlE4bzkzhxm2_k22RP33mjkw9o88GfGbtPbGL5ZFkW5vqvWgx_gt-GxoFMup2yVoC',
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
    'x-fb-lsd': 'AdGpHjOQwtk',
    # 'cookie': 'datr=Z1hMaIrIfVNAp27gtWl_jtL1; sb=Z1hMaKlrQMZu6pNj3IH-tWgs; ps_l=1; ps_n=1; fr=029IlyRZmpwIAbBNq..Bo1FYF..AAA.0.0.BpaTvn.AWd1mkS91mFpI7Ttg-VO4Ke0D9I; wd=682x773; sfiu=AYhaeBZ-JN1zNIWJ9eSV-PS1Z232o2m30DNuAsZgCXXJjZ4LZNyrsFqutKwZqaRj21YdMypPVvwwBw87S5UxWBhDlAurGNAzlUpr3GCUWq0ezJeEI9yC-eakUX4Z6YXn_0iBq46EMkYO1xiKWaGgQQiw65fkFxSqgRP2LFN0cS5CA5C09RoisWJ3iUNutEW6Ss1mlZgQIGDb2xb-2Fq4AVA0GlU6K-PMIeFrKm2TlOytEQ',
}

params = {
    'lara': '0',
}

data = {
    'jazoest': '21028',
    'lsd': 'AdGpHjOQwtk',
    'openid_provider_id': '',
    'openid_provider_name': '',
    'recover_method': 'send_sms:AYhvWv2A_QIO3ohZ51k9JJ9DXXu090mL0qyuOYIk0fNRAc_9KvXNvXkQ5bvmKrljooWDJd-tXVgjVMTURgqjxaeI5mejzcAHPD8j4HeH-CjGXIsN4mDgmwYG3gMSJyvp-X4',
    'reset_action': '1',
    '__aaid': '0',
    '__user': '0',
    '__a': '1',
    '__req': 'c',
    '__hs': '20468.BP:DEFAULT.2.0...0',
    'dpr': '1',
    '__ccg': 'GOOD',
    '__rev': '1032045955',
    '__s': 'h5mk28:my7aaa:u9di7w',
    '__hsi': '7595668256911418246',
    '__dyn': '7xeUmwkHgmwn8yEbFp41twWwIxu13wqovzEdEc8uxa0z8S2Sawba1DwUx60GE1J9E4W0qa321Rw8G11wBz81s8hwGwQw4iwBgao6C0Mo2swaOfK0zEkxe3C0D85a1qwqUW4-5o4q3y1Sx-0ma2-azo7u0zk0z8c86-bwno5B0bK1Iwqo5u1Zxm2OufxyEbbwqEy2-2K0UE620XEG223a11w',
    '__hsdp': 'gIMghs528CF1AkD4a8ghU_hRJIB9QkPHdKmFk79A8pkugC761a5J1TCzO1q4k661xx6cwzxK48kl2f9p4UhtwxxW8HwkUhgxmbxN0BicdrCByaQbRuC8wPxlqsn4GI6Ql28ggf5BxSegaE623W1cxx1Z8Yhp5Xw04g2w',
    '__hblp': '0UwbK7Ee83pwaa0vK2e0Go2xwVwJw2jE2nz80lQw7Mw3fU3Qwl83mw12m0sa08iw2VU1oU0GW0xE3ywyws8aU3rxW0mW0yEbE528zo2tw9-1_AwvU6-09-w58w9q22qi0jm1Owi86y0G83twgo18o1cEb8G0j-0Io6612K3K1GwsqqDwBQu1QwvEvy9y0-w8y5U2LxuewbC3u1wwsK3C0gW0a5wBw4jxOmsw2TgvwgFE2ux64Ueokx23C0kW2S1pwaBwAw8aayE5i',
    '__spin_r': '1032045955',
    '__spin_b': 'trunk',
    '__spin_t': '1768504329',
}

response = requests.post(
    'https://www.facebook.com/ajax/recover/initiate/',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
)
print(response.text)
