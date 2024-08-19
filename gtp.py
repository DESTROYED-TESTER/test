###-------[IMPORT MODULES]-----------####
 
import os
import sys
import time
import uuid
import json
import string
import random
import requests
from requests.exceptions import ConnectionError
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime 


session = requests.Session()
free_fb = session.get(f'https://www.instagram.com').text
cookies = {'csrftoken': re.search('name="csrftoken" value="(.*?)"', str(free_fb)).group(1),}
print(f"{cookies}")






