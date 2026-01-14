import requests

cookies = {
    'datr': 'Eitnac9Jr55lMaaETcsXwk3D',
    'sb': 'EitnaZzbPfbccAsuj6eJIYfE',
    'fr': '0DBxBjQV9WtPFwBoS..BpZysS..AAA.0.0.BpZyux.AWdI9d7fUqkKfXfIiHoCaksZnFM',
    'ps_l': '1',
    'ps_n': '1',
    'sfiu': 'AYgxaHatHEl-032fJR1oikeYk4Fdy6TaDFbWWnNMlvMK-X0IAJVhHRyjoHef7Gty8TkiAgWVenEEEvx9YgL-xjzsQQi-06fwdxVoLC8Wbtxqg54dzGTuc27nfsU-FII0JryPspXZmlZqauacziW5GrM08DIg84QLYA6rHoHvqbA4-4FyRS162Aocga61gvjihvc8KL2tg_4CjT_1UME1dR2b1c6sPLJdK3VbpqnKACIMUQ',
    'wd': '885x773',
}

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'referer': 'https://www.facebook.com/',
}

try:
    response = requests.get(
        'https://www.facebook.com/recover/code/?ph[0]=%2B918101729293&rm=send_sms&cuid=AYghRTMq79g5bK4BaxmW3aXnGG7RDEotWd0UvhGo9pJSAOc4nnDkQ2xs1xSZG5Y5efgONAo--BrLTPgGtMru_ywWEWvKBsA9WxZ6ud_AzdbwApMJVFsTW4J4v3xUG7yK9lVRbwdDb0kgTIgp5iQrn8N8XwjZZ9sLh_fdV3s-snrpRILJWjKlMPR1glamygeVK7pTeJ2HaFUZJmNw6ZgCOOvjqN7E_YCqXHKvqSjR2jkIWQ&hash=AUbElx_iXHc74Px-v2M',
        cookies=cookies,
        headers=headers,
        timeout=10
    )
    
    print(f"Status: {response.status_code}")
    
    if response.status_code == 200:
        if "code" in response.text.lower():
            print("✓ SMS code page loaded")
            print("Check your phone for the code!")
        else:
            print("⚠ Different page loaded")
    else:
        print(f"✗ Failed: {response.status_code}")
        
except Exception as e:
    print(f"✗ Error: {e}")
