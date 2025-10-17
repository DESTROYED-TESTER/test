import requests,json

cookies = {
    '__cf_bm': 'qwoCilS0Bhpia4AmNczFtqx89ty4PUkGGfh6D7T_gSU-1760725346-1.0.1.1-80JNKM_Hpb7Xn57MGaNdTRfE7IwyJNaXFamdIfWdxuimoowJCQ9sRCU_2dMgDRqOGHMqiS_UpCsCoNi0i0CpCkuJDumXl_aSxcQhjAN82i8',
    '_uetsid': '5098c220ab4711f0a1793b9f2c156966',
    '_uetvid': '5098fac0ab4711f09628490ff22b64b2',
    '_scid_r': 'KHTNLLppzbhWWyDqgrdvhfsJia24Y2BjTa983Q',
    '_ga_3MT5TWB94N': 'GS2.1.s1760698322$o1$g1$t1760696490$j59$l0$h0',
    '_fbp': 'fb.1.1760696621368.60970082052103756',
    'sajssdk_2015_cross_new_user': '1',
    '_ga': 'GA1.1.245810326.1760698323',
    '_scid': 'BfTNLLppzbhWWyDqgrdvhfsJia24Y2Bj',
    '_ScCbts': '%5B%5D',
    '_sctr': '1%7C1760639400000',
    'ta_token_prod': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjkyMTA0ODM4MzkxMTY4MDE0NiwiZGV2aWNlSWQiOiIiLCJyZWZyZXNoVG9rZW4iOiIiLCJleHBpcmVUaW1lIjoyNTkyMDAwLCJleHAiOjE3NjMzMTIyODh9.k0ARAAOdcjPIGhkmGvyKGXAyEjc0Ch7JRt0IkeuiXlNfbt9FE_cJLPkxUNLWOdUCKBU0FYfLx6QrcEIk_QCVLjloZrRPd47UxCBv5EuCgo9HkwYd53dp6X15setCDK-RSe9dsrEHMOhRQ_VtJ47Rofvd5grZr5V5YQ3LwBL0QB_SauyRaZNGuUGs7TeCGLuWxsVAiqxid70jHJr0Rs84O7RbOwUJKJxWgjneIGUcdIxqyjNRgww6U5JJuZX15OA-kuoyqg5wj0SnF1allCCIAs7w34Lw2mGX-jMcJR0yDnE7pVh3ToUpCIY4oNuVbckbVpnh2bUuPOuvkGNWL1XR_g',
    'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%22921048383911680146%22%2C%22first_id%22%3A%22199f1cc4ddb2c3-0ff07a7c97fc118-26061851-1296000-199f1cc4ddc55d%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTk5ZjFjYzRkZGIyYzMtMGZmMDdhN2M5N2ZjMTE4LTI2MDYxODUxLTEyOTYwMDAtMTk5ZjFjYzRkZGM1NWQiLCIkaWRlbnRpdHlfbG9naW5faWQiOiI5MjEwNDgzODM5MTE2ODAxNDYifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%22921048383911680146%22%7D%7D',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,bn;q=0.8',
    'authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjkyMTA0ODM4MzkxMTY4MDE0NiwiZGV2aWNlSWQiOiIiLCJyZWZyZXNoVG9rZW4iOiIiLCJleHBpcmVUaW1lIjoyNTkyMDAwLCJleHAiOjE3NjMzMTIyODh9.k0ARAAOdcjPIGhkmGvyKGXAyEjc0Ch7JRt0IkeuiXlNfbt9FE_cJLPkxUNLWOdUCKBU0FYfLx6QrcEIk_QCVLjloZrRPd47UxCBv5EuCgo9HkwYd53dp6X15setCDK-RSe9dsrEHMOhRQ_VtJ47Rofvd5grZr5V5YQ3LwBL0QB_SauyRaZNGuUGs7TeCGLuWxsVAiqxid70jHJr0Rs84O7RbOwUJKJxWgjneIGUcdIxqyjNRgww6U5JJuZX15OA-kuoyqg5wj0SnF1allCCIAs7w34Lw2mGX-jMcJR0yDnE7pVh3ToUpCIY4oNuVbckbVpnh2bUuPOuvkGNWL1XR_g',
    'content-type': 'application/json',
    'origin': 'https://tensor.art',
    'priority': 'u=1, i',
    'referer': 'https://tensor.art/edit/article/921051555745016367',
    'sec-ch-ua': '"Google Chrome";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36',
    'x-echoing-env': '',
    'x-request-package-id': '3000',
    'x-request-package-sign-version': '0.0.1',
    'x-request-sign': 'MzMyMGFjYzdmMGRjNjljOGJlMmJlZWRjMjg0NmVlNDhhZGUzMmMwZjhhZWZiNTVkZDIyZmJhMjVmOTZlODI3NQ==',
    'x-request-sign-type': 'HMAC_SHA256',
    'x-request-sign-version': 'v1',
    'x-request-timestamp': '1760725671615',
    # 'cookie': '__cf_bm=qwoCilS0Bhpia4AmNczFtqx89ty4PUkGGfh6D7T_gSU-1760725346-1.0.1.1-80JNKM_Hpb7Xn57MGaNdTRfE7IwyJNaXFamdIfWdxuimoowJCQ9sRCU_2dMgDRqOGHMqiS_UpCsCoNi0i0CpCkuJDumXl_aSxcQhjAN82i8; _uetsid=5098c220ab4711f0a1793b9f2c156966; _uetvid=5098fac0ab4711f09628490ff22b64b2; _scid_r=KHTNLLppzbhWWyDqgrdvhfsJia24Y2BjTa983Q; _ga_3MT5TWB94N=GS2.1.s1760698322$o1$g1$t1760696490$j59$l0$h0; _fbp=fb.1.1760696621368.60970082052103756; sajssdk_2015_cross_new_user=1; _ga=GA1.1.245810326.1760698323; _scid=BfTNLLppzbhWWyDqgrdvhfsJia24Y2Bj; _ScCbts=%5B%5D; _sctr=1%7C1760639400000; ta_token_prod=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjkyMTA0ODM4MzkxMTY4MDE0NiwiZGV2aWNlSWQiOiIiLCJyZWZyZXNoVG9rZW4iOiIiLCJleHBpcmVUaW1lIjoyNTkyMDAwLCJleHAiOjE3NjMzMTIyODh9.k0ARAAOdcjPIGhkmGvyKGXAyEjc0Ch7JRt0IkeuiXlNfbt9FE_cJLPkxUNLWOdUCKBU0FYfLx6QrcEIk_QCVLjloZrRPd47UxCBv5EuCgo9HkwYd53dp6X15setCDK-RSe9dsrEHMOhRQ_VtJ47Rofvd5grZr5V5YQ3LwBL0QB_SauyRaZNGuUGs7TeCGLuWxsVAiqxid70jHJr0Rs84O7RbOwUJKJxWgjneIGUcdIxqyjNRgww6U5JJuZX15OA-kuoyqg5wj0SnF1allCCIAs7w34Lw2mGX-jMcJR0yDnE7pVh3ToUpCIY4oNuVbckbVpnh2bUuPOuvkGNWL1XR_g; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22921048383911680146%22%2C%22first_id%22%3A%22199f1cc4ddb2c3-0ff07a7c97fc118-26061851-1296000-199f1cc4ddc55d%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTk5ZjFjYzRkZGIyYzMtMGZmMDdhN2M5N2ZjMTE4LTI2MDYxODUxLTEyOTYwMDAtMTk5ZjFjYzRkZGM1NWQiLCIkaWRlbnRpdHlfbG9naW5faWQiOiI5MjEwNDgzODM5MTE2ODAxNDYifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%22921048383911680146%22%7D%7D',
}

json_data = {
    'postId': '921051555745016367',
    'title': 'viral de Yailin Viral y Sr Jimenez XXX VIDEOS',
    'content': '<h1 id="heading-1-DjDbBqBSMZ"><strong><em>El video </em></strong><a target="_blank" rel="noopener noreferrer nofollow" href="https://tinyurl.com/mtmk2db8"><strong><em>viral </em></strong></a><strong><em>de Yailin Viral y Sr</em></strong></h1><p>El reciente video filtrado de Yailin y el Sr. Jiménez ha generado una gran ola de reacciones</p><p></p>',
    'tags': [
        'WORKFLOWS',
    ],
    'cover': {
        'postImageId': '921051509574085469',
    },
    'postImageIds': [
        '921051509574085469',
        '921051509574085469',
    ],
}

response = requests.post('https://api.tensor.art/community-web/v1/post/update', cookies=cookies, headers=headers, json=json_data)

# ✅ Check the result
print("Status Code:", response.status_code)

try:
    result = response.json()
    print(json.dumps(result, indent=4, ensure_ascii=False))

except ValueError:
    print("❌ Invalid response (not JSON):")
    print(response.text)
