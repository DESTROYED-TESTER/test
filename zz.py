import os
import sys
import re
import time
import json
import random
import uuid
import hashlib
import requests
from datetime import datetime
from time import sleep, strftime
from bs4 import BeautifulSoup
from faker import Faker
from rich import print
from rich.panel import Panel
from rich.console import Console
from fake_useragent import UserAgent

# Try to import receivesms
try:
    from receivesms import SMSClient
    RECEIVESMS_AVAILABLE = True
except ImportError:
    RECEIVESMS_AVAILABLE = False
    print(Panel("[bold red] ❌ receivesms not installed. Install with: pip install receivesms", style="bold magenta2"))

# --- Configuration ---
FOLDER_PATH = '/sdcard/AUTO-LMNx9'
os.makedirs(FOLDER_PATH, exist_ok=True)

# --- Color Definitions ---
R = "[bold red]"
G = "[bold green]"
Y = "[bold yellow]"
B = "[bold blue]"
M = "[bold magenta]"
P = "[bold violet]"
C = "[bold cyan]"
W = "[bold white]"

# --- Global Variables ---
Ok, Cp = 0, 0
ua = UserAgent()

# ============================================================================
# SMS VERIFICATION WITH RECEIVESMS.ME (FREE)
# ============================================================================

class FreeSMSVerification:
    """Free SMS verification using receivesms.me API."""
    
    def __init__(self):
        self.client = None
        self.number = None
        self.country = None
        self.operator = None
        
        if RECEIVESMS_AVAILABLE:
            try:
                self.client = SMSClient()
                print(Panel("[bold green] ✅ SMS Client initialized", style="bold magenta2"))
            except Exception as e:
                print(Panel(f"[bold red] ❌ Failed to initialize SMS Client: {e}", style="bold magenta2"))
    
    def get_number(self, country='US', operator='any'):
        """Get a free phone number for SMS verification."""
        if not self.client:
            print(Panel("[bold red] ❌ SMS Client not available", style="bold magenta2"))
            return None
        
        try:
            # Get available countries
            countries = self.client.get_countries()
            
            # If specified country not available, use first available
            if country not in countries:
                country = list(countries.keys())[0]
            
            self.country = country
            self.operator = operator
            
            # Get a number
            number = self.client.get_number(country=country, operator=operator)
            
            if number:
                self.number = number
                print(Panel(f"[bold green] ✅ Phone Number: {number}", style="bold magenta2"))
                return number
            else:
                print(Panel("[bold red] ❌ Failed to get number", style="bold magenta2"))
                return None
                
        except Exception as e:
            print(Panel(f"[bold red] ❌ Error getting number: {e}", style="bold magenta2"))
            return None
    
    def get_sms_code(self, phone_number, max_attempts=30, wait=10):
        """Get SMS verification code."""
        if not self.client:
            return None
        
        try:
            print(Panel(f"[bold white] 📨 Waiting for SMS to {phone_number}...", style="bold magenta2"))
            
            for attempt in range(max_attempts):
                try:
                    # Get messages
                    messages = self.client.get_messages(phone_number)
                    
                    if messages:
                        for msg in messages:
                            content = msg.get('content', '')
                            sender = msg.get('sender', '')
                            
                            # Look for Facebook verification code
                            patterns = [
                                r'\b(\d{5,7})\b',
                                r'FB-(\d{5,7})',
                                r'code[:\s]*(\d{5,7})',
                                r'verification[:\s]*(\d{5,7})'
                            ]
                            
                            for pattern in patterns:
                                match = re.search(pattern, content, re.IGNORECASE)
                                if match:
                                    code = match.group(1)
                                    if len(code) >= 5:
                                        print(Panel(f"[bold green] ✅ SMS Code Received: {code}", style="bold magenta2"))
                                        return code
                    
                    print(f"[bold yellow] ⏳ Waiting for SMS... Attempt {attempt+1}/{max_attempts}")
                    time.sleep(wait)
                    
                except Exception as e:
                    print(f"[bold yellow] ⚠️ Error checking messages: {e}")
                    time.sleep(wait)
            
            print(Panel("[bold red] ❌ SMS Code not received within timeout", style="bold magenta2"))
            return None
            
        except Exception as e:
            print(Panel(f"[bold red] ❌ Error getting SMS: {e}", style="bold magenta2"))
            return None
    
    def release_number(self, phone_number):
        """Release the phone number when done."""
        if self.client:
            try:
                self.client.release_number(phone_number)
                print(Panel("[bold yellow] ℹ️ Phone number released", style="bold magenta2"))
            except:
                pass

# ============================================================================
# EMAIL SERVICES (Fallback)
# ============================================================================

def generate_email():
    """Generate a temporary email."""
    first = Faker().first_name().lower()
    last = Faker().last_name().lower()
    
    domains = [
        'tempmail.com', 'temp-mail.org', 'fexbox.org', 'fexpost.com', 
        'fextemp.com', 'chitthi.in', 'guerrillamail.com', 
        'mailinator.com', '10minutemail.com'
    ]
    
    domain = random.choice(domains)
    number = random.randint(100, 9999)
    
    return f"{first}{last}{number}@{domain}"

def get_email_code(email, max_attempts=20, wait=5):
    """Get verification code from email."""
    domain = email.split('@')[1].lower()
    
    for attempt in range(max_attempts):
        try:
            if 'temp-mail' in domain:
                response = requests.get(f'https://api.internal.temp-mail.io/api/v3/email/{email}/messages',
                                      timeout=10, headers={'User-Agent': ua.random})
                if response.status_code == 200:
                    messages = response.json()
                    if messages:
                        for msg in messages:
                            subject = msg.get('subject', '')
                            body = msg.get('body_text', '')
                            combined = f"{subject} {body}"
                            match = re.search(r'\b(\d{5,7})\b', combined)
                            if match:
                                return match.group(1)
            
            elif 'guerrillamail' in domain:
                sid = email.split('@')[0]
                response = requests.get(f'https://api.guerrillamail.com/ajax.php?f=get_email_list&sid={sid}',
                                      timeout=10)
                if response.status_code == 200:
                    data = response.json()
                    emails = data.get('list', [])
                    if emails:
                        for msg in emails:
                            subject = msg.get('mail_subject', '')
                            body = msg.get('mail_body', '')
                            combined = f"{subject} {body}"
                            match = re.search(r'\b(\d{5,7})\b', combined)
                            if match:
                                return match.group(1)
            
            elif 'fexbox' in domain or 'fexpost' in domain or 'fextemp' in domain or 'chitthi' in domain:
                session = requests.Session()
                session.cookies.set('email', email)
                response = session.get('https://tempmail.plus/api/mails',
                                     timeout=10, headers={'User-Agent': ua.random})
                if response.status_code == 200:
                    data = response.json()
                    mails = data.get('mail_list', [])
                    if mails:
                        for msg in mails:
                            subject = msg.get('subject', '')
                            body = msg.get('body', '')
                            combined = f"{subject} {body}"
                            match = re.search(r'\b(\d{5,7})\b', combined)
                            if match:
                                return match.group(1)
            
            elif 'mailinator' in domain:
                inbox = email.split('@')[0]
                response = requests.get(f'https://api.mailinator.com/api/v2/inbox?to={inbox}',
                                      timeout=10)
                if response.status_code == 200:
                    data = response.json()
                    messages = data.get('messages', [])
                    if messages:
                        for msg in messages:
                            subject = msg.get('subject', '')
                            match = re.search(r'\b(\d{5,7})\b', subject)
                            if match:
                                return match.group(1)
            
            print(f"[bold yellow] ⏳ Waiting for email... Attempt {attempt+1}/{max_attempts}", style="bold magenta2")
            time.sleep(wait)
        except Exception:
            time.sleep(wait)
    
    return None

# ============================================================================
# USER-AGENT GENERATORS
# ============================================================================

def get_desktop_ua():
    """Generate realistic desktop user-agent."""
    versions = [
        "120.0.6099.109", "121.0.6167.85", "122.0.6261.128", 
        "123.0.6312.86", "124.0.6367.91", "125.0.6422.141",
        "145.0.7632.5"
    ]
    chrome = random.choice(versions)
    return f'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome} Safari/537.36'

def get_mobile_ua():
    """Generate realistic mobile user-agent."""
    chrome = f'{random.choice(["120", "121", "122", "123", "124"])}.0.{random.randint(6000, 7000)}.{random.randint(100, 299)}'
    android = random.choice(["10", "11", "12", "13", "14"])
    models = ["SM-G998B", "SM-G991B", "SM-A525F", "Pixel 6", "Pixel 7", "OnePlus 9"]
    return f'Mozilla/5.0 (Linux; Android {android}; {random.choice(models)}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome} Mobile Safari/537.36'

# ============================================================================
# NAME & PASSWORD GENERATORS
# ============================================================================

def fake_name():
    fake = Faker()
    return fake.first_name(), fake.last_name()

def fake_password():
    """Generate realistic password."""
    first, last = fake_name()
    special = random.choice(['!', '@', '#', '$', '%', '&', '*'])
    number = random.randint(1000, 9999)
    
    formats = [
        f"{first}{last}{number}{special}",
        f"{first}{number}{last}{special}",
        f"{first.capitalize()}{last.capitalize()}{number}{special}",
        f"{first}{special}{last}{number}",
        f"{first}{number}{special}{last}"
    ]
    
    return random.choice(formats)

# ============================================================================
# FACEBOOK REGISTRATION
# ============================================================================

def generate_encpass(password):
    """Generate encrypted password format."""
    timestamp = int(time.time())
    return f"#PWD_BROWSER:5:{timestamp}:{password}"

def extract_page_data(html):
    """Extract all necessary values from page."""
    data = {}
    
    soup = BeautifulSoup(html, 'html.parser')
    
    for inp in soup.find_all('input', type='hidden'):
        name = inp.get('name')
        value = inp.get('value')
        if name and value:
            data[name] = value
    
    js_patterns = {
        'fb_dtsg': r'"fb_dtsg":"([^"]+)"',
        'lsd': r'"lsd":"([^"]+)"',
        'jazoest': r'"jazoest":"([^"]+)"',
        'reg_instance': r'"reg_instance":"([^"]+)"',
        'reg_impression_id': r'"reg_impression_id":"([^"]+)"',
        'logger_id': r'"logger_id":"([^"]+)"'
    }
    
    for key, pattern in js_patterns.items():
        if key not in data:
            match = re.search(pattern, html)
            if match:
                data[key] = match.group(1)
    
    for form in soup.find_all('form'):
        for inp in form.find_all('input'):
            name = inp.get('name')
            value = inp.get('value')
            if name and value and name.startswith('__'):
                data[name] = value
    
    return data

def create_facebook_account(use_sms=True):
    """Create Facebook account with SMS verification."""
    global Ok, Cp
    
    session = requests.Session()
    sms_client = None
    phone_number = None
    
    try:
        print(Panel("[bold white] 🔄 INITIALIZING REGISTRATION...", style="bold magenta2"))
        
        # Get registration page
        headers = {
            'User-Agent': get_desktop_ua(),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Sec-Ch-Ua': '"Google Chrome";v="145", "Chromium";v="145", "Not:A-Brand";v="99"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Platform': '"Windows"'
        }
        
        response = session.get('https://www.facebook.com/reg/?entry_point=aymh&next=', 
                              headers=headers, timeout=15)
        
        if response.status_code != 200:
            print(Panel("[bold red] ❌ FAILED TO ACCESS REGISTRATION PAGE", style="bold magenta2"))
            return False
        
        page_data = extract_page_data(response.text)
        
        # Generate missing values
        if not page_data.get('fb_dtsg'):
            page_data['fb_dtsg'] = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789', k=40))
        if not page_data.get('lsd'):
            page_data['lsd'] = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789', k=20))
        if not page_data.get('jazoest'):
            page_data['jazoest'] = str(random.randint(10000, 99999))
        if not page_data.get('reg_instance'):
            page_data['reg_instance'] = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=16))
        if not page_data.get('reg_impression_id'):
            page_data['reg_impression_id'] = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=16))
        if not page_data.get('logger_id'):
            page_data['logger_id'] = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=16))
        
        print(Panel("[bold green] ✅ PAGE DATA EXTRACTED", style="bold magenta2"))
        
        # Generate user data
        firstname, lastname = fake_name()
        custom_pass = fake_password()
        
        # Get phone number for SMS verification
        if use_sms and RECEIVESMS_AVAILABLE:
            sms_client = FreeSMSVerification()
            phone_number = sms_client.get_number(country='US')
            
            if not phone_number:
                print(Panel("[bold yellow] ⚠️ SMS failed, falling back to email", style="bold magenta2"))
                use_sms = False
        
        if use_sms and phone_number:
            contact = phone_number
            contact_type = "PHONE"
            verification_method = "SMS"
            print(Panel(f"[bold white] 📱 Phone: {contact}", style="bold magenta2"))
        else:
            contact = generate_email()
            contact_type = "EMAIL"
            verification_method = "EMAIL"
            print(Panel(f"[bold white] 📧 Email: {contact}", style="bold magenta2"))
        
        print(Panel(f"[bold white] 👤 Name: {firstname} {lastname}", style="bold magenta2"))
        print(Panel(f"[bold white] 🔑 Password: {custom_pass}", style="bold magenta2"))
        
        # Prepare GraphQL variables
        client_mutation_id = str(uuid.uuid4())
        waterfall_id = str(uuid.uuid4())
        
        variables = {
            "input": {
                "actor_id": "0",
                "client_mutation_id": client_mutation_id,
                "machine_id": "",
                "reg_data": {
                    "birthday_day": random.randint(1, 28),
                    "birthday_month": random.randint(1, 12),
                    "birthday_year": random.randint(1992, 2005),
                    "contactpoint": {
                        "sensitive_string_value": contact
                    },
                    "contactpoint_type": contact_type,
                    "custom_gender": "",
                    "did_use_age": False,
                    "firstname": {
                        "sensitive_string_value": firstname
                    },
                    "fullname": {
                        "sensitive_string_value": ""
                    },
                    "ig_age_block_data": None,
                    "lastname": {
                        "sensitive_string_value": lastname
                    },
                    "preferred_pronoun": None,
                    "reg_passwd__": {
                        "sensitive_string_value": generate_encpass(custom_pass)
                    },
                    "sex": random.choice(["MALE", "FEMALE"]),
                    "use_custom_gender": False,
                    "username": {
                        "sensitive_string_value": ""
                    }
                },
                "sk_pipa_consent_given": None,
                "waterfall_id": waterfall_id
            }
        }
        
        # Build payload
        payload = {
            'av': '0',
            '__user': '0',
            '__a': '1',
            '__req': str(random.randint(10, 30)),
            '__hs': '20679.HYP:comet_plat_default_pkg.2.1...0',
            'dpr': '1',
            '__ccg': random.choice(['EXCELLENT', 'GOOD']),
            '__rev': '1045209719',
            '__s': f'mc4dm2:hwj33q:xe3cih',
            '__hsi': str(random.randint(7000000000000000000, 7999999999999999999)),
            '__dyn': '7xeUmwlEnwn8K2Wmh0no6u5U4e0yoW3q32360CEbo1nEhw2nVE4W099w8G1Dz81s8hwGwQw9m1YwBgao6C0Mo2swaOfK0EUjwGzE2ZwNwmE2eUlwhE2Lw6OyES1Tw8W0Lo6-1Fw4mwr86C1nwqU8XwnqwIwtU26wbu0eowRzo',
            '__csr': 'hklbf7pqd58AlOOaRkDdkyi-yhycIyjOQZaZ-DRyFsNYGLiBuaGOuGvIwRGpkALLi8yaC_WQrhdf9KAlGhcN29vWDWoRBhXW9qSyRl5W9G8ml6RZWi4kXmCyOZuF95EJ9PERjbemFVbjyU-EJ1y2e4oKE522G1rwFK324EK9xGU4e2u3y1Oxi361MwDz84Z065w826UO1MgcqwYwvU9o15Am3G5uq1xwxxu1bw9u1ywfu3S1Yw9e0n60kCeDwn80bPo07b-00sBC01bQw3_8Hw0ADw09BR0feaU',
            '__hsdp': 'gbIa49faK9zQvCx64Cfwai0Jpo1GA0klyhE0D20oS03O-09Cw4Rw0BWw0fK607lU09Ko',
            '__hblp': '01bu0E83Ow2hU36w0FKw1am6E0Cq0QE6a0v20aow5dw7zw6-w6yw1JW022G01idw0z0w1t202qi0m-0caxG0FE3cw7Swcq02rC0ue583dwUw',
            '__sjsp': 'gbIa4ncyHyoZ7VEhx9zU2Awbmm0qF055oAq09Mw6dw',
            '__comet_req': '102',
            'lsd': page_data.get('lsd', ''),
            'jazoest': page_data.get('jazoest', ''),
            '__spin_r': '1045209719',
            '__spin_b': 'trunk',
            '__spin_t': str(int(time.time())),
            'qpl_active_flow_ids': '250359044,516759801',
            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'useCAARegistrationFormSubmitMutation',
            'server_timestamps': 'true',
            'variables': json.dumps(variables),
            'doc_id': '27029416779977343',
            'fb_api_analytics_tags': '["qpl_active_flow_ids=250359044,516759801"]'
        }
        
        # Submit registration
        print(Panel("[bold white] ⏳ SUBMITTING REGISTRATION...", style="bold magenta2"))
        time.sleep(random.uniform(2, 4))
        
        graphql_headers = {
            'Host': 'www.facebook.com',
            'User-Agent': get_desktop_ua(),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://www.facebook.com',
            'Referer': 'https://www.facebook.com/reg/?entry_point=aymh&next=',
            'X-FB-Friendly-Name': 'useCAARegistrationFormSubmitMutation',
            'X-ASBD-ID': '359341',
            'X-FB-LSD': page_data.get('lsd', ''),
            'Sec-Ch-Ua': '"Google Chrome";v="145", "Chromium";v="145", "Not:A-Brand";v="99"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Platform': '"Windows"',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1'
        }
        
        response = session.post('https://www.facebook.com/api/graphql/', 
                               data=payload, 
                               headers=graphql_headers, 
                               allow_redirects=True, 
                               timeout=30)
        
        # Check if account was created
        if 'c_user' in session.cookies:
            uid = session.cookies.get('c_user')
            print(Panel(f"[bold green] ✅ ACCOUNT CREATED! UID: {uid}", style="bold magenta2"))
            
            # Get verification code
            print(Panel(f"[bold white] 📨 WAITING FOR {verification_method} CODE...", style="bold magenta2"))
            
            code = None
            
            if verification_method == "SMS" and sms_client and phone_number:
                code = sms_client.get_sms_code(phone_number)
            else:
                code = get_email_code(contact)
            
            if code:
                print(Panel(f"[bold green] ✅ CODE RECEIVED: {code}", style="bold magenta2"))
                
                # Verify the code
                if confirm_verification(session, uid, code, contact, verification_method):
                    # Save account
                    cookie_str = "; ".join([f"{k}={v}" for k, v in session.cookies.get_dict().items()])
                    
                    account_info = (
                        f"UID: {uid}\n"
                        f"{verification_method}: {contact}\n"
                        f"Password: {custom_pass}\n"
                        f"Cookie: {cookie_str}\n"
                        f"{'='*50}\n"
                    )
                    
                    with open(f"{FOLDER_PATH}/SUCCESS-OK-ID.txt", "a") as f:
                        f.write(f"{uid}|{contact}|{custom_pass}|{cookie_str}\n")
                    
                    with open(f"{FOLDER_PATH}/ACCOUNT_INFO.txt", "a") as f:
                        f.write(account_info)
                    
                    print(Panel(
                        f"[bold green] ✅ ACCOUNT VERIFIED SUCCESSFULLY!\n"
                        f"[bold white] UID: {uid}\n"
                        f"[bold white] {verification_method}: {contact}\n"
                        f"[bold white] Password: {custom_pass}",
                        style="bold magenta2"
                    ))
                    
                    # Release SMS number if used
                    if sms_client and phone_number:
                        sms_client.release_number(phone_number)
                    
                    Ok += 1
                    return True
                else:
                    print(Panel("[bold red] ❌ VERIFICATION FAILED", style="bold magenta2"))
                    Cp += 1
                    return False
            else:
                print(Panel(f"[bold red] ❌ {verification_method} CODE NOT RECEIVED", style="bold magenta2"))
                Cp += 1
                return False
        else:
            print(Panel("[bold red] ❌ REGISTRATION FAILED", style="bold magenta2"))
            Cp += 1
            return False
            
    except Exception as e:
        print(Panel(f"[bold red] ❌ ERROR: {str(e)}", style="bold magenta2"))
        Cp += 1
        return False

def confirm_verification(session, uid, code, contact, method):
    """Confirm verification code."""
    try:
        time.sleep(random.uniform(2, 4))
        
        # Get confirmation page
        headers = {
            'User-Agent': get_mobile_ua(),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1'
        }
        
        response = session.get('https://m.facebook.com/confirmemail.php?next=https%3A%2F%2Fm.facebook.com%2F%3Fdeoia%3D1&soft=hjk',
                              headers=headers, timeout=15)
        
        soup = BeautifulSoup(response.text, 'html.parser')
        tokens = {}
        
        for inp in soup.find_all('input', type='hidden'):
            name = inp.get('name')
            value = inp.get('value')
            if name and value:
                tokens[name] = value
        
        dtsg_match = re.search(r'"fb_dtsg":"([^"]+)"', response.text)
        if dtsg_match:
            tokens['fb_dtsg'] = dtsg_match.group(1)
        
        lsd_match = re.search(r'"lsd":"([^"]+)"', response.text)
        if lsd_match:
            tokens['lsd'] = lsd_match.group(1)
        
        # Determine verification medium
        medium = "sms" if method == "SMS" else "email"
        contact_field = "contact" if medium == "email" else ""
        
        payload = {
            'contact': contact if medium == "email" else '',
            'type': 'submit',
            'is_soft_cliff': 'false',
            'medium': medium,
            'code': code,
            'fb_dtsg': tokens.get('fb_dtsg', ''),
            'jazoest': tokens.get('jazoest', ''),
            'lsd': tokens.get('lsd', ''),
            '__user': uid
        }
        
        confirm_headers = {
            'Host': 'm.facebook.com',
            'User-Agent': get_mobile_ua(),
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-Requested-With': 'mark.via.gp',
            'Origin': 'https://m.facebook.com',
            'Referer': 'https://m.facebook.com/confirmemail.php?next=https%3A%2F%2Fm.facebook.com%2F%3Fdeoia%3D1&soft=hjk',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            'Upgrade-Insecure-Requests': '1'
        }
        
        response = session.post('https://m.facebook.com/confirmation_cliff/',
                               data=payload, headers=confirm_headers,
                               allow_redirects=True, timeout=30)
        
        if "checkpoint" in response.url:
            print(Panel("[bold red] ❌ ACCOUNT HIT CHECKPOINT", style="bold magenta2"))
            return False
        elif "home" in response.url or "welcome" in response.url:
            print(Panel("[bold green] ✅ VERIFIED!", style="bold magenta2"))
            return True
        elif "success" in response.text.lower() or "confirmed" in response.text.lower():
            return True
        
        return False
        
    except Exception as e:
        print(Panel(f"[bold red] ❌ VERIFICATION ERROR: {str(e)}", style="bold magenta2"))
        return False

# ============================================================================
# UI FUNCTIONS
# ============================================================================

def banner():
    os.system("clear")
    logo = """
    ╔══════════════════════════════════════════════════════════════════╗
    ║     📱 FACEBOOK ACCOUNT CREATOR - FREE SMS VERIFICATION       ║
    ║     ⚡ OPEN SOURCED BY - LMNx9 & XVSOULX                      ║
    ║     📱 TELEGRAM - t.me/TEAM_LMNx9                            ║
    ╚══════════════════════════════════════════════════════════════════╝
    """
    print(Panel(logo, style="bold magenta2", width=102, padding=1))

def show_menu():
    banner()
    menu = """
    ╔══════════════════════════════════════════════════════════════════╗
    ║  [1] 📱 CREATE WITH SMS (Free receivesms.me)                   ║
    ║  [2] 📧 CREATE WITH EMAIL (Fallback)                          ║
    ║  [3] 📊 VIEW ACCOUNT STATISTICS                                ║
    ║  [0] ❌ EXIT                                                  ║
    ╚══════════════════════════════════════════════════════════════════╝
    """
    print(Panel(menu, style="bold magenta2", width=102, padding=1))
    return Console().input("   ╰─➤ Choose option: ")

def results():
    print(Panel(
        f"[bold white] ╔══════════════════════════════════════════════╗\n"
        f" ║ [bold green] ✅ SUCCESSFUL: {Ok}\n"
        f" ║ [bold red] ❌ FAILED: {Cp}\n"
        f" ║ [bold yellow] 📁 SAVED TO: {FOLDER_PATH}\n"
        f" ╚══════════════════════════════════════════════╝",
        style="bold magenta2", width=102, padding=1
    ))

def GetInfoProfile():
    try:
        with open(f"{FOLDER_PATH}/SUCCESS-OK-ID.txt", 'r') as file:
            accounts = file.readlines()
        
        if not accounts:
            print(Panel("[bold yellow] NO ACCOUNTS FOUND", style="bold magenta2"))
            return
        
        print(Panel(f"[bold green] TOTAL ACCOUNTS: {len(accounts)}", style="bold magenta2"))
        
        for account in accounts:
            parts = account.strip().split('|')
            if len(parts) >= 3:
                print(Panel(
                    f"[bold white] UID: {parts[0]}\n"
                    f"[bold white] Contact: {parts[1]}\n"
                    f"[bold white] Password: {parts[2]}",
                    style="bold magenta2"
                ))
                time.sleep(0.5)
                
    except FileNotFoundError:
        print(Panel("[bold red] NO ACCOUNTS FILE FOUND", style="bold magenta2"))

# ============================================================================
# MAIN FUNCTION
# ============================================================================

def main(use_sms=True):
    global Ok, Cp
    
    try:
        num_accounts = int(input("[bold white] HOW MANY ACCOUNTS? : "))
        if num_accounts <= 0:
            print(Panel("[bold red] INVALID NUMBER", style="bold magenta2"))
            return
        
        delay = int(input("[bold white] DELAY (seconds) : "))
        if delay < 30:
            delay = 30
        
        banner()
        
        if use_sms:
            print(Panel("[bold green] 📱 SMS VERIFICATION MODE (Free)", style="bold magenta2"))
        else:
            print(Panel("[bold yellow] 📧 EMAIL VERIFICATION MODE (Fallback)", style="bold magenta2"))
        
        for i in range(num_accounts):
            print(Panel(f"[bold cyan] 📊 PROGRESS: {i+1}/{num_accounts}", style="bold magenta2"))
            
            if create_facebook_account(use_sms=use_sms):
                print(Panel("[bold green] ✅ ACCOUNT CREATED", style="bold magenta2"))
            else:
                print(Panel("[bold red] ❌ ACCOUNT FAILED", style="bold magenta2"))
            
            if i < num_accounts - 1:
                random_delay = delay + random.randint(0, 30)
                print(Panel(f"[bold yellow] ⏳ WAITING {random_delay}s...", style="bold magenta2"))
                time.sleep(random_delay)
        
        results()
        
    except ValueError:
        print(Panel("[bold red] PLEASE ENTER VALID NUMBERS", style="bold magenta2"))
    except KeyboardInterrupt:
        print(Panel("[bold yellow] ⚠️ PROCESS INTERRUPTED", style="bold magenta2"))
    except Exception as e:
        print(Panel(f"[bold red] ERROR: {str(e)}", style="bold magenta2"))

# ============================================================================
# MAIN LOOP
# ============================================================================

if __name__ == "__main__":
    while True:
        choice = show_menu()
        
        if choice in ["1", "01"]:
            main(use_sms=True)
        elif choice in ["2", "02"]:
            main(use_sms=False)
        elif choice in ["3", "03"]:
            banner()
            GetInfoProfile()
            input("[bold white] Press Enter to continue...")
        elif choice in ["0", "00"]:
            print(Panel("[bold green] 👋 GOODBYE!", style="bold magenta2"))
            break
        else:
            print(Panel("[bold red] ❌ INVALID OPTION", style="bold magenta2"))
            time.sleep(1)
