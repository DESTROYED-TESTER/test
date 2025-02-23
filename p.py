import requests
import time
import re
from bs4 import BeautifulSoup

class TempEmailGenerator:
    def __init__(self):
        self.base_url = 'https://10minutemail.net'
        self.session = requests.Session()
        self.session.headers.update({'User-Agent': 'Mozilla/5.0'})
        self.session_id = None
        self.cookie_email = None
    
    def get_email(self):
        try:
            # Step 1: Get the session ID and timestamp
            response = self.session.get(f'{self.base_url}/m/?lang=id')
            response.raise_for_status()  # Ensure the request was successful
            
            soup = BeautifulSoup(response.content, 'html.parser')
            self.session_id = re.search('sessionid="(.*?)"', str(soup)).group(1)
            timestamp = str(int(time.time() * 1000))  # Use milliseconds for timestamp
            
            # Step 2: Request the temporary email address
            payload = {'new': '1', 'sessionid': self.session_id, '_': timestamp}
            email_response = self.session.post(f'{self.base_url}/address.api.php', data=payload)
            email_response.raise_for_status()  # Ensure the request was successful
            
            email_data = email_response.json()
            email = email_data.get('mail_get_mail')
            if not email:
                raise ValueError("Failed to retrieve email address.")
            
            # Step 3: Store cookies for further requests
            self.cookie_email = '; '.join([f'{key}={value}' for key, value in self.session.cookies.get_dict().items()])
            return email
        
        except requests.RequestException as e:
            print(f"Request error: {e}")
            return None
        except ValueError as e:
            print(f"Value error: {e}")
            return None
        except Exception as e:
            print(f"Unexpected error: {e}")
            return None

    def get_code(self):
        if not self.session_id:
            print("Session ID not found. Please generate an email first.")
            return None
        
        try:
            # Step 1: Get the verification code
            timestamp = str(int(time.time() * 1000))  # Use milliseconds for timestamp
            payload = {'new': '0', 'sessionid': self.session_id, '_': timestamp}
            headers = {'Cookie': self.cookie_email}
            code_response = self.session.post(f'{self.base_url}/address.api.php', data=payload, headers=headers)
            code_response.raise_for_status()  # Ensure the request was successful
            
            code_data = code_response.json()
            code = re.search(r'FB-([^ ]+)', str(code_data))
            if code:
                return code.group(1)
                print(code)
            else:
                print("Code not found in the response.")
                return None
        
        except requests.RequestException as e:
            print(f"Request error: {e}")
            return None
        except Exception as e:
            print(f"Unexpected error: {e}")
            return None


print(email)
print(code)

