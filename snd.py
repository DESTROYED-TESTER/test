import requests

cookies = {
    'datr': 'Eitnac9Jr55lMaaETcsXwk3D',
    'sb': 'EitnaZzbPfbccAsuj6eJIYfE',
    'ps_l': '1',
    'ps_n': '1',
    'wd': '885x773',
    'fr': '0DBxBjQV9WtPFwBoS..BpZysS..AAA.0.0.BpZztO.AWfGeKdmKj0jFW8rYpsnEF6YsKo',
    'sfiu': 'AYjtlEpxV13KHybxxIHV2xymDUz8VjcHTzerZyy8o9EpkdB4tZTfU4sZCJIIBu24eXWWK-C_dnKl9Vs4XX6wX2MdrXmNTgtSmHI0j2ucqFh7IOoON56UbmuZNhaEt_yAFKVZ3AeWkW7lvM5mjcyn7paO6JtEu9ZTiw5ovC_pq4MXslQ7aHapv_LFks4CDsYzngpDKx85qI8TNv3J9ouLayDC29nO6qvCP-XnzuJna3ydctqf_8RN-oCFcqDtECOlFl0',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'dpr': '1',
    'priority': 'u=0, i',
    'referer': 'https://www.facebook.com/sms/captcha/?next=%2Fajax%2Frecover%2Finitiate%2F%3Fcuid%3DAYgrIEX4eUXmcUyjJUxDVDTyon10YiK2AV4epSovB4KfRN35yeKBzRddy2kvpq-oU3B5vuVOmxI0T1giwlwRXFIslUpnSnFdAEgW9QArU6eDUe7_kgKVwVmokoCdlQVL7Y9nmA7puT5QajQU3R_5Kf7sra4SnAXiDEdopKoGkaZ5Ep8-NHKQhp6motq0lwhL8vasP18QPEW1GuX84Ad6mJy4x7ztN3BN0fDLXUpE1c7fLjDK99n3G67yTXFaEGOc0A0%26recover_method%3Dsend_sms%253AAYjxAoHgCqYWFa9QD2LhBLKKUyFmQkCBjs_fhfaELWx9d2_PEBfPDHJ96KmAFmUnEparlORdV47ApkrA3NwKRrsTJ2XaQhAwrMV_V3JjniLTf2SQz2rohTp9vkeNF6OrwCQ%26lara%3D1&next_mac=AdAH2jlH7GMdvWn8Vvtg3AP5BQR1_hEw2aiQNJKpfze65Osv',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"',
    'sec-ch-ua-full-version-list': '"Google Chrome";v="143.0.7499.170", "Chromium";v="143.0.7499.170", "Not A(Brand";v="24.0.0.0"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',
    'viewport-width': '885',
    # 'cookie': 'datr=Eitnac9Jr55lMaaETcsXwk3D; sb=EitnaZzbPfbccAsuj6eJIYfE; ps_l=1; ps_n=1; wd=885x773; fr=0DBxBjQV9WtPFwBoS..BpZysS..AAA.0.0.BpZztO.AWfGeKdmKj0jFW8rYpsnEF6YsKo; sfiu=AYjtlEpxV13KHybxxIHV2xymDUz8VjcHTzerZyy8o9EpkdB4tZTfU4sZCJIIBu24eXWWK-C_dnKl9Vs4XX6wX2MdrXmNTgtSmHI0j2ucqFh7IOoON56UbmuZNhaEt_yAFKVZ3AeWkW7lvM5mjcyn7paO6JtEu9ZTiw5ovC_pq4MXslQ7aHapv_LFks4CDsYzngpDKx85qI8TNv3J9ouLayDC29nO6qvCP-XnzuJna3ydctqf_8RN-oCFcqDtECOlFl0',
}

try:
    response = requests.get(
        'https://www.facebook.com/recover/code/?ph[0]=%2B918101729293&rm=send_sms&cuid=AYjy3FgUfZg_brTpBv2rkM4Gw-07sopq8hJ7ZJfs1ZqcAQRH89AM5iVhfGlU-5M9bq31uPfUSU8AbbtyGKWwoWoMu1oQVN1olBaxQg6XuVbmWgmnhjmSC375nTZGiGQz5WgDX7HBPHm5VXDPRYV5JedjIdOyx0r5TISTLhQccNUf5SAT1CLxlOgQQXYkzvdVTyiSLJUVj9swp2xnqrVwiVAygckE2DtelZsePCdyk7eXEMHaUeCgYSVU3MUkxxwNupU&lara=1&hash=AUZIuV5qGvneQaExBMg',
        cookies=cookies,
        headers=headers,
        timeout=10
    )
    
    print(f"Status: {response.status_code}")
    
    if response.status_code == 200:
        if "code" in response.text.lower():
            print("✓ SMS code page loaded")
            print(response.text)
        else:
            print("⚠ Different page loaded")
    else:
        print(f"✗ Failed: {response.status_code}")
        
except Exception as e:
    print(f"✗ Error: {e}")
