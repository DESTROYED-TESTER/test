import requests
import re
import time

# Initialize a session
session = requests.Session()

   lgnjs = str(int(time.time()))
   free_fb = session.get('https://m.facebook.com').text
   log_data ={
    'email': idf,
    'pass': ps,
    'guid': re.search(r'name="guid" value="(.*?)"', free_fb).group(1),
    'lgnrnd': re.search(r'name="lgnrnd" value="(.*?)"', free_fb).group(1),
    'lgndim': re.search(r'name="lgndim" value="(.*?)"', free_fb).group(1),
    'lsd': re.search(r'name="lsd" value="(.*?)"', free_fb).group(1),
    'jazoest': re.search(r'name="jazoest" value="(.*?)"', free_fb).group(1),
    'lgnjs': lgnjs,
    'locale': 'en_GB',
    'login_source': 'comet_headerless_login',
    'login': 'Log In'}

# Now you can use these values as needed
print(f"guid: {guid}, lgnrnd: {lgnrnd}, lgndim: {lgndim}, lsd: {lsd}, jazoest: {jazoest}, lgnjs: {lgnjs}")
