import re
import random
import string

# Assuming BLACKX contains the HTML content
session = requests.Session()
BLACKX = session.get('https://x.facebook.com').text

# Assuming ids and ps are defined somewhere
ids = "example@example.com"
ps = "example_password"

# Regular expressions to extract values from HTML content
regex_patterns = {
    'jazoest': r'name="jazoest" value="(.*?)"',
    'lsd': r'name="lsd" value="(.*?)"',
    'return_session': r'name="return_session" value="(.*?)"',
    'signed_next': r'name="signed_next" value="(.*?)"',
    'lgndim': r'name="lgndim" value="(.*?)"',
    'lgnrnd': r'name="lgnrnd" value="(.*?)"',
    'lgnjs': r'name="lgnjs" value="(.*?)"',
    'ab_test_data': r'name="ab_test_data" value="(.*?)"',
}

# Initialize form data dictionary
form_data = {}

# Extract values from HTML content using regular expressions
for key, pattern in regex_patterns.items():
    match = re.search(pattern, BLACKX)
    if match:
        form_data[key] = match.group(1)
    else:
        # Handle case where regex pattern doesn't match
        form_data[key] = None

# Generate random values for other fields
form_data['display'] = random.choice(['', 'touch', 'mobile'])
form_data['isprivate'] = random.choice(['', 'false', 'true'])
form_data['skip_api_login'] = random.choice(['', '1'])
form_data['trynum'] = str(random.randint(1, 10))
form_data['timezone'] = str(random.randint(-720, 720))
form_data['encpass'] = '#PWD_BROWSER:0:' + ''.join(random.choices(string.digits, k=10)) + ':' + ps

# Add email and pass
form_data['email'] = ids
form_data['pass'] = ps
form_data['prefill_contact_point'] = ids

# Generate random choices for prefill_source and prefill_type
form_data['prefill_source'] = random.choice(['browser_dropdown', 'browser_saved', 'messenger_code'])
form_data['prefill_type'] = random.choice(['password', 'contact_point'])
form_data['first_prefill_source'] = random.choice(['browser_dropdown', 'browser_saved', 'messenger_code'])
form_data['first_prefill_type'] = random.choice(['password', 'contact_point'])
form_data['had_cp_prefilled'] = random.choice(['true', 'false'])
form_data['had_password_prefilled'] = random.choice(['true', 'false'])

# Now you have your form data ready to be used
print(form_data)
