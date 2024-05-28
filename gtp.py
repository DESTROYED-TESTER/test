import requests
from bs4 import BeautifulSoup

def login_to_facebook(email, password):
    login_url = "https://www.facebook.com/login/device-based/regular/login/"
    
    payload = {
        'jazoest': '2952',
        'lsd': 'AVqCpzNGPMQ',
        'email': email,
        'pass': password,
        'login_source': 'comet_headerless_login',
        'next': ''
    }
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Referer': 'https://www.facebook.com/'
    }
    
    with requests.Session() as session:
        try:
            response = session.post(login_url, data=payload, headers=headers)
            response.raise_for_status()  # Raise an exception for HTTP errors
            
            # Parse the response content
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Check for specific elements that are only present when logged in
            if soup.find('div', {'id': 'profile_pic_header_123456789'}):
                print("Login successful!")
                return True
            else:
                print("Login failed!")
                # Optionally, print the response content for debugging
                print("Response content:", response.text)
                return False

        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return False

if __name__ == "__main__":
    # Replace these with your actual Facebook credentials
    email = 8250886169
    password = 'sumon@@@'
    login_success = login_to_facebook(email, password)
    print("Login success:", login_success)
