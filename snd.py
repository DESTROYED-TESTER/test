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
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'dpr': '1',
    'priority': 'u=0, i',
    'referer': 'https://www.facebook.com/sms/captcha/?next=%2Fajax%2Frecover%2Finitiate%2F%3Fcuid%3DAYgUDz3EM1R8G3A82SfE_5N4B5g-9vdqTMe4VkWvpcPjmAIhFdbzMy0DJqr9RSoaxJblxtgnCJ51Ov46x0CWHzIphkpWvzrVp_lQEUSB4fB7Cx9aDmrLbUaXZKVt2s7b6qGKsByiRLBOaWiu-lJ6ObznCu9NKJdBpL6xv7JozImJxoT74VZtMiPypCJjcXBpk22W6xkX3dT1coJ4ONID_GwNBuOhNPSTJGJ7IrcoBpwC0w%26recover_method%3Dsend_sms%253AAYihGClGR3w9iNQRqYG045XxqnmaeHGaylRfHeOX33W1WzyNq3XlAbmobRuApsAkYwyNIOf_D7wzys0VtXEENjbrlP5Ciy8m5f6NDfZ_hAS3VBfrvOrDFe0j_-jVNgBf9_0%26lara%3D0&next_mac=AdDI9pZ5wvbC6EKg543H3pIh92QvC8sALvJjt7G-qWmrUHN5',
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
    # 'cookie': 'datr=Eitnac9Jr55lMaaETcsXwk3D; sb=EitnaZzbPfbccAsuj6eJIYfE; fr=0DBxBjQV9WtPFwBoS..BpZysS..AAA.0.0.BpZyux.AWdI9d7fUqkKfXfIiHoCaksZnFM; ps_l=1; ps_n=1; sfiu=AYgxaHatHEl-032fJR1oikeYk4Fdy6TaDFbWWnNMlvMK-X0IAJVhHRyjoHef7Gty8TkiAgWVenEEEvx9YgL-xjzsQQi-06fwdxVoLC8Wbtxqg54dzGTuc27nfsU-FII0JryPspXZmlZqauacziW5GrM08DIg84QLYA6rHoHvqbA4-4FyRS162Aocga61gvjihvc8KL2tg_4CjT_1UME1dR2b1c6sPLJdK3VbpqnKACIMUQ; wd=885x773',
}

response = requests.get(
    'https://www.facebook.com/recover/code/?ph[0]=%2B918101729293&rm=send_sms&cuid=AYghRTMq79g5bK4BaxmW3aXnGG7RDEotWd0UvhGo9pJSAOc4nnDkQ2xs1xSZG5Y5efgONAo--BrLTPgGtMru_ywWEWvKBsA9WxZ6ud_AzdbwApMJVFsTW4J4v3xUG7yK9lVRbwdDb0kgTIgp5iQrn8N8XwjZZ9sLh_fdV3s-snrpRILJWjKlMPR1glamygeVK7pTeJ2HaFUZJmNw6ZgCOOvjqN7E_YCqXHKvqSjR2jkIWQ&hash=AUbElx_iXHc74Px-v2M',
    cookies=cookies,
    headers=headers,
)
if response.status_code == 200:
   print("Request successful!")




