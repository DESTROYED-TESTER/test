import re
import random
import string

# Assuming BLACKX contains the HTML content
BLACKX = "https://m.facebook.com"

data = {
                            "lsd":re.search('name="lsd" value="(.*?)"', str(BLACKX)).group(1),
                        "jazoest":re.search('name="jazoest" value="(.*?)"', str(BLACKX)).group(1),
                        "m_ts":re.search('name="m_ts" value="(.*?)"', str(BLACKX)).group(1),
                        "li":re.search('name="li" value="(.*?)"', str(BLACKX)).group(1),
                        "try_number":"0",
                        "unrecognized_tries":"0",
                        "email":ids,
                        "pass":ps,
                        "login":"Log In"}
# Now you have your form data ready to be used
print(data)
