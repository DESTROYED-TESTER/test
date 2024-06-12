'https://www.facebook.com/login/'

{
    'jazoest': re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
    'lsd': re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
    'email': idf,
    'login_source': 'comet_headerless_login',
    'next': '',
    'encpass': '#PWD_BROWSER:0:{}:{}'.format(re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1), ps) }
