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

# --- Email Generation ---
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

# --- Email Code Retrieval ---
def get_email_code(email, max_attempts=25, wait=5):
    """Get verification code from email."""
    domain = email.split('@')[1].lower()
    
    for attempt in range(max_attempts):
        try:
            if 'temp-mail' in domain:
                response = requests.get(f'https://api.internal.temp-mail.io/api/v3/email/{email}/messages',
                                      timeout=10,
                                      headers={'User-Agent': ua.random})
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
                                     timeout=10,
                                     headers={'User-Agent': ua.random})
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
                            combined = subject
                            match = re.search(r'\b(\d{5,7})\b', combined)
                            if match:
                                return match.group(1)
            
            print(f"[bold yellow] ⏳ Waiting for code... Attempt {attempt+1}/{max_attempts}", style="bold magenta2")
            time.sleep(wait)
        except Exception:
            time.sleep(wait)
    
    return None

# --- User-Agent Generators ---
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

# --- Name & Password ---
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

# --- Generate Encrypted Password ---
def generate_encpass(password):
    """Generate encrypted password format."""
    timestamp = int(time.time())
    return f"#PWD_BROWSER:5:{timestamp}:{password}"

# --- Extract Values from Page ---
def extract_page_data(html):
    """Extract all necessary values from page."""
    data = {}
    
    # Extract from hidden inputs
    soup = BeautifulSoup(html, 'html.parser')
    
    for inp in soup.find_all('input', type='hidden'):
        name = inp.get('name')
        value = inp.get('value')
        if name and value:
            data[name] = value
    
    # Extract from JavaScript
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
    
    # Extract __dyn, __req, __csr from forms
    for form in soup.find_all('form'):
        for inp in form.find_all('input'):
            name = inp.get('name')
            value = inp.get('value')
            if name and value and name.startswith('__'):
                data[name] = value
    
    return data

# --- Facebook Registration ---
def create_facebook_account():
    """Create Facebook account."""
    global Ok, Cp
    
    # Create session with cookies
    session = requests.Session()
    
    try:
        print(Panel("[bold white] 🔄 INITIALIZING REGISTRATION...", style="bold magenta2"))
        
        # Step 1: Get registration page with proper headers
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
        
        # Get the registration page
        response = session.get('https://www.facebook.com/reg/?entry_point=aymh&next=', 
                              headers=headers, timeout=15)
        
        if response.status_code != 200:
            print(Panel("[bold red] ❌ FAILED TO ACCESS REGISTRATION PAGE", style="bold magenta2"))
            return False
        
        # Extract all data from page
        page_data = extract_page_data(response.text)
        
        # Generate any missing values
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
        
        # Step 2: Generate user data
        firstname, lastname = fake_name()
        email = generate_email()
        custom_pass = fake_password()
        
        print(Panel(f"[bold white] 📧 Email: {email}", style="bold magenta2"))
        print(Panel(f"[bold white] 👤 Name: {firstname} {lastname}", style="bold magenta2"))
        print(Panel(f"[bold white] 🔑 Password: {custom_pass}", style="bold magenta2"))
        
        # Step 3: Prepare registration data
        encpass = generate_encpass(custom_pass)
        
        # Generate UUIDs
        client_mutation_id = str(uuid.uuid4())
        waterfall_id = str(uuid.uuid4())
        
        # Prepare variables for GraphQL
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
                        "sensitive_string_value": email
                    },
                    "contactpoint_type": "EMAIL",
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
                        "sensitive_string_value": encpass
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
        
        # Build complete payload
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
        
        # Step 4: Submit registration
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
        
        # Step 5: Process response
        print(Panel("[bold white] 📊 PROCESSING RESPONSE...", style="bold magenta2"))
        
        # Check if we have cookies
        if 'c_user' in session.cookies:
            uid = session.cookies.get('c_user')
            print(Panel(f"[bold green] ✅ ACCOUNT CREATED! UID: {uid}", style="bold magenta2"))
            
            # Get verification code
            print(Panel("[bold white] 📨 WAITING FOR VERIFICATION CODE...", style="bold magenta2"))
            code = get_email_code(email)
            
            if code:
                print(Panel(f"[bold green] ✅ CODE RECEIVED: {code}", style="bold magenta2"))
                
                # Confirm email
                if confirm_email(session, email, uid, code):
                    # Save account
                    cookie_str = "; ".join([f"{k}={v}" for k, v in session.cookies.get_dict().items()])
                    
                    account_info = (
                        f"UID: {uid}\n"
                        f"Email: {email}\n"
                        f"Password: {custom_pass}\n"
                        f"Cookie: {cookie_str}\n"
                        f"{'='*50}\n"
                    )
                    
                    with open(f"{FOLDER_PATH}/SUCCESS-OK-ID.txt", "a") as f:
                        f.write(f"{uid}|{email}|{custom_pass}|{cookie_str}\n")
                    
                    with open(f"{FOLDER_PATH}/ACCOUNT_INFO.txt", "a") as f:
                        f.write(account_info)
                    
                    print(Panel(
                        f"[bold green] ✅ ACCOUNT CREATED SUCCESSFULLY!\n"
                        f"[bold white] UID: {uid}\n"
                        f"[bold white] Email: {email}\n"
                        f"[bold white] Password: {custom_pass}",
                        style="bold magenta2"
                    ))
                    
                    Ok += 1
                    return True
                else:
                    print(Panel("[bold red] ❌ EMAIL CONFIRMATION FAILED", style="bold magenta2"))
                    Cp += 1
                    return False
            else:
                print(Panel("[bold red] ❌ VERIFICATION CODE NOT RECEIVED", style="bold magenta2"))
                Cp += 1
                return False
        else:
            # Try to parse response for error
            try:
                result = response.json()
                if 'data' in result:
                    mutation = result['data'].get('useCAARegistrationFormSubmitMutation', {})
                    if 'error' in mutation:
                        error_msg = mutation['error'].get('message', 'Unknown error')
                        print(Panel(f"[bold red] ❌ REGISTRATION ERROR: {error_msg}", style="bold magenta2"))
                    else:
                        print(Panel("[bold red] ❌ REGISTRATION FAILED", style="bold magenta2"))
                else:
                    print(Panel("[bold red] ❌ REGISTRATION FAILED - INVALID RESPONSE", style="bold magenta2"))
            except:
                print(Panel("[bold red] ❌ REGISTRATION FAILED", style="bold magenta2"))
            
            Cp += 1
            return False
            
    except Exception as e:
        print(Panel(f"[bold red] ❌ ERROR: {str(e)}", style="bold magenta2"))
        Cp += 1
        return False

def confirm_email(session, email, uid, code):
    """Confirm email address."""
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
        
        # Extract tokens from confirmation page
        soup = BeautifulSoup(response.text, 'html.parser')
        tokens = {}
        
        for inp in soup.find_all('input', type='hidden'):
            name = inp.get('name')
            value = inp.get('value')
            if name and value:
                tokens[name] = value
        
        # Extract missing tokens
        dtsg_match = re.search(r'"fb_dtsg":"([^"]+)"', response.text)
        if dtsg_match:
            tokens['fb_dtsg'] = dtsg_match.group(1)
        
        lsd_match = re.search(r'"lsd":"([^"]+)"', response.text)
        if lsd_match:
            tokens['lsd'] = lsd_match.group(1)
        
        # Prepare confirmation payload
        payload = {
            'contact': email,
            'type': 'submit',
            'is_soft_cliff': 'false',
            'medium': 'email',
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
        
        # Check result
        if "checkpoint" in response.url:
            print(Panel("[bold red] ❌ ACCOUNT HIT CHECKPOINT", style="bold magenta2"))
            return False
        elif "home" in response.url or "welcome" in response.url:
            print(Panel("[bold green] ✅ EMAIL CONFIRMED!", style="bold magenta2"))
            return True
        elif "success" in response.text.lower() or "confirmed" in response.text.lower():
            return True
        
        return False
        
    except Exception as e:
        print(Panel(f"[bold red] ❌ CONFIRMATION ERROR: {str(e)}", style="bold magenta2"))
        return False

# --- UI Functions ---
def banner():
    os.system("clear")
    logo = """
    ╔══════════════════════════════════════════════════════════════════╗
    ║     🤖 FACEBOOK ACCOUNT CREATOR v3.0                          ║
    ║     ⚡ OPEN SOURCED BY - LMNx9 & XVSOULX                      ║
    ║     📱 TELEGRAM - t.me/TEAM_LMNx9                            ║
    ╚══════════════════════════════════════════════════════════════════╝
    """
    print(Panel(logo, style="bold magenta2", width=102, padding=1))

def show_menu():
    banner()
    menu = """
    ╔══════════════════════════════════════════════════════════════════╗
    ║  [1] 🤖 CREATE FACEBOOK ACCOUNTS                               ║
    ║  [2] 📊 VIEW ACCOUNT STATISTICS                                ║
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
                    f"[bold white] Email: {parts[1]}\n"
                    f"[bold white] Password: {parts[2]}",
                    style="bold magenta2"
                ))
                time.sleep(0.5)
                
    except FileNotFoundError:
        print(Panel("[bold red] NO ACCOUNTS FILE FOUND", style="bold magenta2"))

# --- Main Function ---
def main():
    global Ok, Cp
    
    try:
        num_accounts = int(input("[bold white] HOW MANY ACCOUNTS? : "))
        if num_accounts <= 0:
            print(Panel("[bold red] INVALID NUMBER", style="bold magenta2"))
            return
        
        delay = int(input("[bold white] DELAY (seconds) : "))
        if delay < 20:
            delay = 20
        
        banner()
        print(Panel("[bold yellow] ⚡ STARTING ACCOUNT CREATION...", style="bold magenta2"))
        print(Panel("[bold yellow] ⚠️ USING 20+ SECOND DELAYS TO AVOID DETECTION", style="bold magenta2"))
        
        for i in range(num_accounts):
            print(Panel(f"[bold cyan] 📊 PROGRESS: {i+1}/{num_accounts}", style="bold magenta2"))
            
            if create_facebook_account():
                print(Panel("[bold green] ✅ ACCOUNT CREATED", style="bold magenta2"))
            else:
                print(Panel("[bold red] ❌ ACCOUNT FAILED", style="bold magenta2"))
            
            if i < num_accounts - 1:
                random_delay = delay + random.randint(0, 20)
                print(Panel(f"[bold yellow] ⏳ WAITING {random_delay}s...", style="bold magenta2"))
                time.sleep(random_delay)
        
        results()
        
    except ValueError:
        print(Panel("[bold red] PLEASE ENTER VALID NUMBERS", style="bold magenta2"))
    except KeyboardInterrupt:
        print(Panel("[bold yellow] ⚠️ PROCESS INTERRUPTED", style="bold magenta2"))
    except Exception as e:
        print(Panel(f"[bold red] ERROR: {str(e)}", style="bold magenta2"))

# --- Main Loop ---
if __name__ == "__main__":
    while True:
        choice = show_menu()
        
        if choice in ["1", "01"]:
            main()
        elif choice in ["2", "02"]:
            banner()
            GetInfoProfile()
            input("[bold white] Press Enter to continue...")
        elif choice in ["0", "00"]:
            print(Panel("[bold green] 👋 GOODBYE!", style="bold magenta2"))
            break
        else:
            print(Panel("[bold red] ❌ INVALID OPTION", style="bold magenta2"))
            time.sleep(1)
