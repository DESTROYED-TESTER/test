import requests
import re
import time

# Initialize a session
session = requests.Session()

# Fetch the Facebook login page
login_page = session.get('https://m.facebook.com').text

# Extract necessary values using regular expressions
guid_pattern = r'name="guid" value="(.*?)"'
lgnrnd_pattern = r'name="lgnrnd" value="(.*?)"'
lgndim_pattern = r'name="lgndim" value="(.*?)"'
lsd_pattern = r'name="lsd" value="(.*?)"'
jazoest_pattern = r'name="jazoest" value="(.*?)"'

guid = re.search(guid_pattern, login_page).group(1)
lgnrnd = re.search(lgnrnd_pattern, login_page).group(1)
lgndim = re.search(lgndim_pattern, login_page).group(1)
lsd = re.search(lsd_pattern, login_page).group(1)
jazoest = re.search(jazoest_pattern, login_page).group(1)

# Generate lgnjs (current timestamp)
lgnjs = str(int(time.time()))

# Now you can use these values as needed
print(f"guid: {guid}, lgnrnd: {lgnrnd}, lgndim: {lgndim}, lsd: {lsd}, jazoest: {jazoest}, lgnjs: {lgnjs}")
