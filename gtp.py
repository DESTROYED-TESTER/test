import requests,json

cookies = {
    '__cf_bm': 'Or7Oz7e1osE7MiCSX0lDLDuou8iDSuMwvzyoxjT2kb0-1760722107-1.0.1.1-YFlvVCykWRiLPAiD7AJ6b_IUojKTCE2Og5lqvDByg00p8UDCrDsErOy1ktJEOUQSIUl1UpM8qQI0RgClok.OPl00b7t1ozhYayVbypp8juc',
    '_fbp': 'fb.1.1760696621368.60970082052103756',
    'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%22921048383911680146%22%2C%22first_id%22%3A%22199f1cc4ddb2c3-0ff07a7c97fc118-26061851-1296000-199f1cc4ddc55d%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTk5ZjFjYzRkZGIyYzMtMGZmMDdhN2M5N2ZjMTE4LTI2MDYxODUxLTEyOTYwMDAtMTk5ZjFjYzRkZGM1NWQiLCIkaWRlbnRpdHlfbG9naW5faWQiOiI5MjEwNDgzODM5MTE2ODAxNDYifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%22921048383911680146%22%7D%7D',
    '_uetsid': '5098c220ab4711f0a1793b9f2c156966',
    '_uetvid': '5098fac0ab4711f09628490ff22b64b2',
    '_scid_r': 'K3TNLLppzbhWWyDqgrdvhfsJia24Y2BjTa98wQ',
    '_ga_3MT5TWB94N': 'GS2.1.s1760698322$o1$g1$t1760697265$j31$l0$h0',
    'sajssdk_2015_cross_new_user': '1',
    '_ga': 'GA1.1.245810326.1760698323',
    '_scid': 'BfTNLLppzbhWWyDqgrdvhfsJia24Y2Bj',
    '_ScCbts': '%5B%5D',
    '_sctr': '1%7C1760639400000',
    'ta_token_prod': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjkyMTA0ODM4MzkxMTY4MDE0NiwiZGV2aWNlSWQiOiIiLCJyZWZyZXNoVG9rZW4iOiIiLCJleHBpcmVUaW1lIjoyNTkyMDAwLCJleHAiOjE3NjMzMTIyODh9.k0ARAAOdcjPIGhkmGvyKGXAyEjc0Ch7JRt0IkeuiXlNfbt9FE_cJLPkxUNLWOdUCKBU0FYfLx6QrcEIk_QCVLjloZrRPd47UxCBv5EuCgo9HkwYd53dp6X15setCDK-RSe9dsrEHMOhRQ_VtJ47Rofvd5grZr5V5YQ3LwBL0QB_SauyRaZNGuUGs7TeCGLuWxsVAiqxid70jHJr0Rs84O7RbOwUJKJxWgjneIGUcdIxqyjNRgww6U5JJuZX15OA-kuoyqg5wj0SnF1allCCIAs7w34Lw2mGX-jMcJR0yDnE7pVh3ToUpCIY4oNuVbckbVpnh2bUuPOuvkGNWL1XR_g',
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
    'x-request-sign': 'NjZmMmZiMGRhNjUzNmRkMjYzNDlkMDFiNTMyNmI3ZjAzMzZjYjU2NTBlZTBlYmFiNzNmYTI4YWM4Nzk5MjMyYg==',
    'x-request-sign-type': 'HMAC_SHA256',
    'x-request-sign-version': 'v1',
    'x-request-timestamp': '1760722875203',
    # 'cookie': '__cf_bm=Or7Oz7e1osE7MiCSX0lDLDuou8iDSuMwvzyoxjT2kb0-1760722107-1.0.1.1-YFlvVCykWRiLPAiD7AJ6b_IUojKTCE2Og5lqvDByg00p8UDCrDsErOy1ktJEOUQSIUl1UpM8qQI0RgClok.OPl00b7t1ozhYayVbypp8juc; _fbp=fb.1.1760696621368.60970082052103756; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22921048383911680146%22%2C%22first_id%22%3A%22199f1cc4ddb2c3-0ff07a7c97fc118-26061851-1296000-199f1cc4ddc55d%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTk5ZjFjYzRkZGIyYzMtMGZmMDdhN2M5N2ZjMTE4LTI2MDYxODUxLTEyOTYwMDAtMTk5ZjFjYzRkZGM1NWQiLCIkaWRlbnRpdHlfbG9naW5faWQiOiI5MjEwNDgzODM5MTE2ODAxNDYifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%22921048383911680146%22%7D%7D; _uetsid=5098c220ab4711f0a1793b9f2c156966; _uetvid=5098fac0ab4711f09628490ff22b64b2; _scid_r=K3TNLLppzbhWWyDqgrdvhfsJia24Y2BjTa98wQ; _ga_3MT5TWB94N=GS2.1.s1760698322$o1$g1$t1760697265$j31$l0$h0; sajssdk_2015_cross_new_user=1; _ga=GA1.1.245810326.1760698323; _scid=BfTNLLppzbhWWyDqgrdvhfsJia24Y2Bj; _ScCbts=%5B%5D; _sctr=1%7C1760639400000; ta_token_prod=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjkyMTA0ODM4MzkxMTY4MDE0NiwiZGV2aWNlSWQiOiIiLCJyZWZyZXNoVG9rZW4iOiIiLCJleHBpcmVUaW1lIjoyNTkyMDAwLCJleHAiOjE3NjMzMTIyODh9.k0ARAAOdcjPIGhkmGvyKGXAyEjc0Ch7JRt0IkeuiXlNfbt9FE_cJLPkxUNLWOdUCKBU0FYfLx6QrcEIk_QCVLjloZrRPd47UxCBv5EuCgo9HkwYd53dp6X15setCDK-RSe9dsrEHMOhRQ_VtJ47Rofvd5grZr5V5YQ3LwBL0QB_SauyRaZNGuUGs7TeCGLuWxsVAiqxid70jHJr0Rs84O7RbOwUJKJxWgjneIGUcdIxqyjNRgww6U5JJuZX15OA-kuoyqg5wj0SnF1allCCIAs7w34Lw2mGX-jMcJR0yDnE7pVh3ToUpCIY4oNuVbckbVpnh2bUuPOuvkGNWL1XR_g',
}

json_data = {
    'postId': '921051555745016367',
    'title': 'El video viral de Yailin Viral y Sr Jimenez XXX VIDEOS',
    'content': '<h1 id="heading-1-uLsJkEtogB"><a target="_blank" rel="noopener noreferrer nofollow" href="https://click.hdfree.site/Adult/"><strong><em>El video viral de Yailin Viral y Sr</em></strong></a></h1><p>Jimenez XXX VIDEOS</p><p>Last Updates: October 19, 2025</p><p>🕐 Hace 1 Minuto — 🔥 Tendencia Viral:</p><p>Video Filtrado de Yailin y Sr. Jiménez</p><p>En el vertiginoso mundo digital, ciertos contenidos logran captar la atención global en cuestión de</p><p>horas.</p><p>El reciente video filtrado de Yailin y el Sr. Jiménez ha generado una gran ola de reacciones</p><p>en plataformas como X (Twitter), TikTok, Instagram, Reddit y Telegram, convirtiéndose</p><p>rápidamente en uno de los temas más buscados y comentados.</p><p>La combinación de la popularidad de los involucrados y la naturaleza sensible del</p><p>contenido ha desatado una enorme curiosidad, debates y controversia en toda la comunidad</p><p>online.</p><p>Palabras clave: video filtrado Yailin, Sr. Jiménez viral, contenido en tendencia, noticia viral, Yailin</p><p>video 2025</p><p>🚀 ¿Por qué se hizo viral?</p><p>Existen varios factores que explican la rápida difusión de este material:</p><p>🎤 Fama y notoriedad: Yailin es una figura conocida en la música urbana, lo que despertó aún</p><p>más interés.</p><p>⚡ Carácter inesperado: El contenido del video sorprendió a los fans y al público general,</p><p>generando un efecto “quiero verlo yo mismo”.</p><p>📲 Difusión multiplataforma: Miles de usuarios compartieron fragmentos, capturas y</p><p>comentarios, impulsando su alcance masivo.</p><p>👀 Curiosidad y morbo digital: Al etiquetarse como “filtrado” o “exclusivo”, muchos usuarios</p><p>intentaron acceder al contenido antes de su eliminación.</p><p>Palabras clave: Yailin viral, razones de viralidad, video filtrado, tendencia digital, redes sociales</p><p>⚡ Impacto de la difusión viral</p><p>✅ Efectos Positivos</p><p>● Aumento de visibilidad internacional 🌎</p><p>● Debate sobre la privacidad y los límites del contenido en redes 🗣</p><p>● Incremento de búsquedas y notoriedad para ambos nombres 📈</p><p>❌ Efectos Negativos</p><p>● Posibles daños emocionales y reputacionales 😔</p><p>● Riesgo de desinformación y versiones falsas 📰</p><p>● Exposición no consentida y cuestionamientos éticos 🚫</p><p>● Potenciales implicaciones legales ⚖</p><p>Palabras clave: impacto viral, pros y contras, controversia online, consecuencias legales</p><p>🧭 Consideraciones Éticas</p><p>La difusión de un video filtrado o íntimo plantea importantes dilemas éticos:</p><p>🔒 Consentimiento: ¿El material fue compartido voluntariamente o sin permiso?</p><p>👤 Privacidad: Difundir material privado vulnera derechos personales.</p><p>📢 Responsabilidad digital: Antes de compartir, los usuarios deben reflexionar sobre el</p><p>impacto que puede tener.</p><p>💻 Huella digital: Una vez publicado, eliminar completamente un contenido es casi imposible.</p><p>Palabras clave: ética digital, privacidad online, responsabilidad en redes, filtraciones virales</p><p>✅ Conclusiones</p><p>El caso del video filtrado de Yailin y el Sr. Jiménez evidencia cómo un solo contenido puede</p><p>dominar las redes en cuestión de horas.</p><p>Aunque la viralidad puede parecer inofensiva o entretenida, sus consecuencias —especialmente</p><p>cuando se trata de temas íntimos— pueden ser profundas y duraderas.</p><p>La curiosidad no justifica la exposición, y la ética debe ser siempre la guía principal en la era</p><p>de la información inmediata.</p><p>Palabras clave: Yailin video viral, Sr. Jiménez filtrado, tendencias 2025, impacto en redes</p><p>sociales</p><p>🛡 Consejos para Compartir con Responsabilidad</p><p>✅ Evita difundir material privado o íntimo</p><p>✅ Verifica fuentes antes de reaccionar</p><p>✅ Denuncia versiones falsas o dañinas</p><p>✅ Respeta la privacidad y la dignidad de los involucrados 👤</p><p>🚨 Reflexión Final</p><p>La viralidad puede convertir cualquier contenido en tema mundial, pero no toda atención es</p><p>positiva.</p><p>El caso de Yailin y el Sr. Jiménez nos recuerda el poder —y el peligro— de compartir sin</p><p>pensar.</p><p>Disfruta el contenido digital con responsabilidad, protege la privacidad ajena y recuerda: detrás</p><p>de cada video viral hay personas reales con sentimientos reales.</p><p>📈 Etiquetas Relacionadas (SEO / Hashtags)</p><p>#Yailin #SrJiménez #VideoFiltrado #VideoViral #TendenciaEnRedes #PrivacidadDigital</p><p>#Trending2025 #NoticiasViral&nbsp;#BuzzEnInternet</p><p></p>',
    'tags': [
        'RESOURCE',
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

    # ✅ Determine if update was successful
    if result.get("code") == 0 or result.get("message") == "success":
        print("\n✅ Post updated successfully!")
    else:
        print("\n❌ Update failed. Check response details above.")
except ValueError:
    print("❌ Invalid response (not JSON):")
    print(response.text)
