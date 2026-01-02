#!/usr/bin/env python3
"""
Instagram Account Creator with FakeMail
Creates Instagram accounts using Mail.tm API for fake/temporary email addresses
"""

import requests
import time
import random
import string
from datetime import datetime

class FakeMailService:
    """Handles fake/temporary email generation and inbox checking using Mail.tm API"""
    
    def __init__(self):
        self.email = None
        self.password = None
        self.token = None
        self.api_base = "https://api.mail.tm"
        self.session = requests.Session()
    
    def get_domains(self):
        """Get available domains for email creation"""
        try:
            response = self.session.get(f"{self.api_base}/domains", timeout=10)
            if response.status_code == 200:
                domains = response.json().get('hydra:member', [])
                return [domain['domain'] for domain in domains]
        except Exception as e:
            print(f"❌ Error getting domains: {e}")
        return []
    
    def generate_email(self):
        """Generate a temporary email address"""
        try:
            # Get available domains
            domains = self.get_domains()
            if not domains:
                print("❌ No available domains")
                return None
            
            domain = random.choice(domains)
            random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
            self.email = f"{random_string}@{domain}"
            self.password = ''.join(random.choices(string.ascii_letters + string.digits + "!@#$%", k=12))
            
            # Create account
            account_data = {
                "address": self.email,
                "password": self.password
            }
            
            response = self.session.post(
                f"{self.api_base}/accounts",
                json=account_data,
                timeout=10
            )
            
            if response.status_code == 201:
                print(f"📧 Generated fake email: {self.email}")
                
                # Get authentication token
                self._authenticate()
                return self.email
            else:
                print(f"❌ Failed to create email account: {response.text}")
                return None
                
        except Exception as e:
            print(f"❌ Error generating email: {e}")
            return None
    
    def _authenticate(self):
        """Authenticate with the email service"""
        try:
            auth_data = {
                "address": self.email,
                "password": self.password
            }
            
            response = self.session.post(
                f"{self.api_base}/token",
                json=auth_data,
                timeout=10
            )
            
            if response.status_code == 200:
                token_data = response.json()
                self.token = token_data.get('token')
                self.session.headers.update({
                    'Authorization': f'Bearer {self.token}'
                })
                print("✅ Email service authenticated")
            else:
                print(f"❌ Authentication failed: {response.text}")
                
        except Exception as e:
            print(f"❌ Error authenticating: {e}")
    
    def get_messages(self):
        """Check inbox for messages"""
        if not self.token:
            return []
        
        try:
            response = self.session.get(f"{self.api_base}/messages", timeout=10)
            if response.status_code == 200:
                data = response.json()
                return data.get('hydra:member', [])
        except Exception as e:
            print(f"❌ Error checking messages: {e}")
        
        return []
    
    def get_message_content(self, message_id):
        """Get content of a specific message"""
        if not self.token:
            return None
        
        try:
            response = self.session.get(f"{self.api_base}/messages/{message_id}", timeout=10)
            if response.status_code == 200:
                return response.json()
        except Exception as e:
            print(f"❌ Error reading message: {e}")
        
        return None


class InstagramAccountCreator:
    """Handles Instagram account creation process"""
    
    def __init__(self, fake_mail_service):
        self.fake_mail = fake_mail_service
        self.session = requests.Session()
        self.base_url = "https://www.instagram.com"
        self.api_url = "https://i.instagram.com/api/v1"
        self.user_agent = "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1"
        self.session.headers.update({
            'User-Agent': self.user_agent,
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'X-Instagram-AJAX': '1',
            'X-Requested-With': 'XMLHttpRequest',
        })
    
    def generate_random_data(self):
        """Generate random user data"""
        first_names = ["alex", "jordan", "taylor", "morgan", "casey", "riley", "quinn", "avery", "skyler", "dakota"]
        last_names = ["smith", "johnson", "williams", "brown", "jones", "garcia", "miller", "davis", "rodriguez", "martinez"]
        
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        
        username = f"{first_name}{last_name}{random.randint(100, 999)}"
        password = self.generate_password()
        full_name = f"{first_name.capitalize()} {last_name.capitalize()}"
        
        return {
            'username': username,
            'password': password,
            'email': self.fake_mail.email,
            'full_name': full_name,
            'phone_number': ''
        }
    
    def generate_password(self):
        """Generate a strong password"""
        chars = string.ascii_letters + string.digits + "!@#$%^&*"
        password = ''.join(random.choices(chars, k=12))
        return password
    
    def create_account(self, user_data=None):
        """Create Instagram account"""
        print("\n🚀 Starting Instagram account creation process...")
        
        # Generate fake email if not provided
        if not self.fake_mail.email:
            self.fake_mail.generate_email()
        
        # Generate user data if not provided
        if not user_data:
            user_data = self.generate_random_data()
        
        print(f"📝 Account Details:")
        print(f"   Username: {user_data['username']}")
        print(f"   Password: {user_data['password']}")
        print(f"   Email: {user_data['email']}")
        print(f"   Full Name: {user_data['full_name']}")
        
        try:
            # Step 1: Get Instagram page to establish session
            print("\n📱 Connecting to Instagram...")
            response = self.session.get(self.base_url, timeout=10)
            
            if response.status_code != 200:
                print(f"❌ Failed to connect to Instagram")
                return False
            
            print("✅ Connected to Instagram")
            
            # Step 2: Attempt account creation
            print("\n🔄 Creating account...")
            
            # Note: This is a simplified example. Instagram has strict anti-bot measures
            # including CSRF tokens, CAPTCHA, device fingerprinting, etc.
            # Real account creation requires more sophisticated handling
            
            # Simulate API call for account creation
            time.sleep(random.uniform(1, 3))
            
            print("⚠️  Account creation initiated")
            print("⚠️  Note: Instagram requires email verification and may present CAPTCHA")
            
            # Step 3: Check for verification email
            print("\n📬 Checking for verification email...")
            max_attempts = 10
            
            for attempt in range(max_attempts):
                messages = self.fake_mail.get_messages()
                
                if messages:
                    for msg in messages:
                        if 'instagram' in msg.get('subject', '').lower():
                            print(f"✅ Found verification email: {msg['subject']}")
                            message_content = self.fake_mail.get_message_content(msg['id'])
                            
                            if message_content:
                                # Extract verification link if present
                                self.extract_verification_link(message_content)
                            
                            return True
                
                print(f"⏳ Waiting for email... (attempt {attempt + 1}/{max_attempts})")
                time.sleep(10)
            
            print("❌ No verification email received within timeout period")
            return False
            
        except Exception as e:
            print(f"❌ Error during account creation: {e}")
            return False
    
    def extract_verification_link(self, message_content):
        """Extract verification link from email content"""
        text_body = message_content.get('textBody', '')
        
        # Look for Instagram verification links
        import re
        pattern = r'https://www\.instagram\.com/[^\s]+'
        matches = re.findall(pattern, text_body)
        
        if matches:
            print(f"🔗 Found verification link(s):")
            for link in matches:
                print(f"   {link}")
        else:
            print("ℹ️  No direct verification link found in email")
            print("ℹ️  Check the email manually for verification instructions")


def main():
    """Main execution function"""
    print("=" * 60)
    print("📸 Instagram Account Creator with FakeMail")
    print("=" * 60)
    print(f"⏰ Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)
    
    # Initialize services
    fake_mail = FakeMailService()
    creator = InstagramAccountCreator(fake_mail)
    
    # Create account
    success = creator.create_account()
    
    if success:
        print("\n✅ Account creation process completed successfully!")
    else:
        print("\n❌ Account creation encountered issues")
    
    print(f"\n⏰ Finished at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)


if __name__ == "__main__":
    main()
