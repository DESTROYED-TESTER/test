import os
import sys
import re
import time
import json
import random
import uuid
import requests
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from faker import Faker
from rich import print
from rich.panel import Panel
from rich.console import Console
from fake_useragent import UserAgent

# --- Configuration ---
FOLDER_PATH = '/sdcard/AUTO-LMNx9'
os.makedirs(FOLDER_PATH, exist_ok=True)
os.system("clear")

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

# --- Phone Number Generation ---
def generate_phone():
    """Generate a valid phone number."""
    # Philippine numbers (since the curl shows PHONE type)
    prefixes = ['917', '918', '919', '920', '921', '922', '923', '924', '925', '926', '927', '928', '929',
                '930', '931', '932', '933', '934', '935', '936', '937', '938', '939',
                '940', '941', '942', '943', '944', '945', '946', '947', '948', '949',
                '950', '951', '952', '953', '954', '955', '956', '957', '958', '959',
                '960', '961', '962', '963', '964', '965', '966', '967', '968', '969',
                '970', '971', '972', '973', '974', '975', '976', '977', '978', '979',
                '980', '981', '982', '983', '984', '985', '986', '987', '988', '989']
    
    prefix = random.choice(prefixes)
    number = ''.join([str(random.randint(0, 9)) for _ in range(7)])
    return f"63{prefix}{number}"

# --- Email Generation (Fallback) ---
def generate_email():
    """Generate a temporary email."""
    first = Faker().first_name().lower()
    last = Faker().last_name().lower()
    domains = ['tempmail.com', 'temp-mail.org', 'fexbox.org', 'fexpost.com', 
               'fextemp.com', 'chitthi.in', 'guerrillamail.com', 'mailinator.com']
    return f"{first}{last}{random.randint(100, 9999)}@{random.choice(domains)}"

# --- Get Verification Code from Email ---
def get_email_code(email, max_attempts=25, wait=5):
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
            
            time.sleep(wait)
        except:
            time.sleep(wait)
    
    return None

# --- User-Agent ---
def get_ua():
    """Get realistic user-agent matching the curl."""
    return 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36'

# --- Name & Password ---
def fake_name():
    fake = Faker()
    return fake.first_name().lower(), fake.last_name().lower()

def fake_password():
    first, last = fake_name()
    special = random.choice(['!', '@', '#', '$', '%', '&', '*'])
    return f"{first.capitalize()}{last.capitalize()}{random.randint(1000, 9999)}{special}"

# --- Extract Tokens ---
def extract_tokens(html):
    """Extract all required tokens from HTML."""
    tokens = {}
    
    # Extract from hidden inputs
    soup = BeautifulSoup(html, 'html.parser')
    for inp in soup.find_all('input', type='hidden'):
        name = inp.get('name')
        value = inp.get('value')
        if name and value:
            tokens[name] = value
    
    # Extract from JavaScript
    patterns = {
        'fb_dtsg': r'"fb_dtsg":"([^"]+)"',
        'lsd': r'"lsd":"([^"]+)"',
        'jazoest': r'"jazoest":"([^"]+)"',
        'reg_instance': r'"reg_instance":"([^"]+)"',
        'reg_impression_id': r'"reg_impression_id":"([^"]+)"',
        'logger_id': r'"logger_id":"([^"]+)"'
    }
    
    for key, pattern in patterns.items():
        if key not in tokens:
            match = re.search(pattern, html)
            if match:
                tokens[key] = match.group(1)
    
    # Generate missing tokens
    if not tokens.get('fb_dtsg'):
        tokens['fb_dtsg'] = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789', k=40))
    if not tokens.get('lsd'):
        tokens['lsd'] = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789', k=20))
    if not tokens.get('jazoest'):
        tokens['jazoest'] = str(random.randint(10000, 99999))
    if not tokens.get('reg_instance'):
        tokens['reg_instance'] = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=16))
    
    return tokens

# --- Create Facebook Account ---
def create_facebook_account():
    """Create Facebook account using GraphQL API."""
    global Ok, Cp
    
    session = requests.Session()
    
    try:
        print(Panel("[bold white] 🔄 INITIALIZING REGISTRATION...", style="bold magenta2"))
        
        # Step 1: Get registration page
        headers = {
            'User-Agent': get_ua(),
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
            print(Panel("[bold red] ❌ FAILED TO ACCESS REGISTRATION", style="bold magenta2"))
            return False
        
        # Extract tokens
        tokens = extract_tokens(response.text)
        print(Panel("[bold green] ✅ TOKENS EXTRACTED", style="bold magenta2"))
        
        # Step 2: Generate user data
        firstname, lastname = fake_name()
        phone = generate_phone()
        password = fake_password()
        
        # Use phone for registration (like the curl)
        contact = phone
        
        print(Panel(f"[bold white] 📱 Phone: {contact}", style="bold magenta2"))
        print(Panel(f"[bold white] 👤 Name: {firstname} {lastname}", style="bold magenta2"))
        print(Panel(f"[bold white] 🔑 Password: {password}", style="bold magenta2"))
        
        # Step 3: Prepare GraphQL variables
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
                    "contactpoint_type": "PHONE",  # Using PHONE like the curl
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
                        "sensitive_string_value": f"#PWD_BROWSER:5:{int(time.time())}:{password}"
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
        
        # Step 4: Build complete payload (matching the curl exactly)
        payload = {
            'av': '0',
            '__user': '0',
            '__a': '1',
            '__req': str(random.randint(15, 25)),
            '__hs': '20679.HYP:comet_plat_default_pkg.2.1...0',
            'dpr': '1',
            '__ccg': 'EXCELLENT',
            '__rev': '1045209719',
            '__s': 'mc4dm2:hwj33q:xe3cih',
            '__hsi': str(random.randint(7000000000000000000, 7999999999999999999)),
            '__dyn': '7xeUmwlEnwn8K2Wmh0no6u5U4e0yoW3q32360CEbo1nEhw2nVE4W099w8G1Dz81s8hwGwQw9m1YwBgao6C0Mo2swaOfK0EUjwGzE2ZwNwmE2eUlwhE2Lw6OyES1Tw8W0Lo6-1Fw4mwr86C1nwqU8XwnqwIwtU26wbu0eowRzo',
            '__csr': 'hklbf7pqd58AlOOaRkDdkyi-yhycIyjOQZaZ-DRyFsNYGLiBuaGOuGvIwRGpkALLi8yaC_WQrhdf9KAlGhcN29vWDWoRBhXW9qSyRl5W9G8ml6RZWi4kXmCyOZuF95EJ9PERjbemFVbjyU-EJ1y2e4oKE522G1rwFK324EK9xGU4e2u3y1Oxi361MwDz84Z065w826UO1MgcqwYwvU9o15Am3G5uq1xwxxu1bw9u1ywfu3S1Yw9e0n60kCeDwn80bPo07b-00sBC01bQw3_8Hw0ADw09BR0feaU',
            '__hsdp': 'gbIa49faK9zQvCx64Cfwai0Jpo1GA0klyhE0D20oS03O-09Cw4Rw0BWw0fK607lU09Ko',
            '__hblp': '01bu0E83Ow2hU36w0FKw1am6E0Cq0QE6a0v20aow5dw7zw6-w6yw1JW022G01idw0z0w1t202qi0m-0caxG0FE3cw7Swcq02rC0ue583dwUw',
            '__sjsp': 'gbIa4ncyHyoZ7VEhx9zU2Awbmm0qF055oAq09Mw6dw',
            '__comet_req': '102',
            'lsd': tokens.get('lsd', ''),
            'jazoest': tokens.get('jazoest', ''),
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
        
        # Step 5: Submit registration
        print(Panel("[bold white] ⏳ SUBMITTING REGISTRATION...", style="bold magenta2"))
        time.sleep(random.uniform(2, 4))
        
        graphql_headers = {
            'Host': 'www.facebook.com',
            'User-Agent': get_ua(),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://www.facebook.com',
            'Referer': 'https://www.facebook.com/reg/?entry_point=aymh&next=',
            'X-FB-Friendly-Name': 'useCAARegistrationFormSubmitMutation',
            'X-ASBD-ID': '359341',
            'X-FB-LSD': tokens.get('lsd', ''),
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
        
        # Step 6: Process response
        print(Panel("[bold white] 📊 PROCESSING RESPONSE...", style="bold magenta2"))
        
        # Check if registration was successful
        if 'c_user' in session.cookies:
            uid = session.cookies.get('c_user')
            print(Panel(f"[bold green] ✅ ACCOUNT CREATED! UID: {uid}", style="bold magenta2"))
            
            # For phone verification, we need to handle differently
            # Facebook usually sends SMS for phone verification
            print(Panel("[bold yellow] ⚠️ PHONE VERIFICATION REQUIRED", style="bold magenta2"))
            print(Panel(f"[bold white] 📱 Phone: {phone}", style="bold magenta2"))
            print(Panel("[bold yellow] ℹ️ Check SMS for verification code", style="bold magenta2"))
            
            # Since we can't receive SMS, we'll save the account as-is
            cookie_str = "; ".join([f"{k}={v}" for k, v in session.cookies.get_dict().items()])
            
            account_info = (
                f"UID: {uid}\n"
                f"Phone: {phone}\n"
                f"Password: {password}\n"
                f"Cookie: {cookie_str}\n"
                f"{'='*50}\n"
            )
            
            with open(f"{FOLDER_PATH}/SUCCESS-OK-ID.txt", "a") as f:
                f.write(f"{uid}|{phone}|{password}|{cookie_str}\n")
            
            with open(f"{FOLDER_PATH}/ACCOUNT_INFO.txt", "a") as f:
                f.write(account_info)
            
            print(Panel(
                f"[bold green] ✅ ACCOUNT CREATED!\n"
                f"[bold white] UID: {uid}\n"
                f"[bold white] Phone: {phone}\n"
                f"[bold white] Password: {password}\n"
                f"[bold yellow] ⚠️ Phone verification required - Check SMS",
                style="bold magenta2"
            ))
            
            Ok += 1
            return True
        else:
            # Try to parse error
            try:
                result = response.json()
                if 'data' in result:
                    mutation = result['data'].get('useCAARegistrationFormSubmitMutation', {})
                    if 'error' in mutation:
                        error_msg = mutation['error'].get('message', 'Unknown error')
                        print(Panel(f"[bold red] ❌ ERROR: {error_msg}", style="bold magenta2"))
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

# --- UI Functions ---
def banner():
    os.system("clear")
    logo = """
    ╔══════════════════════════════════════════════════════════════════╗
    ║     🤖 FACEBOOK ACCOUNT CREATOR v4.0 - PHONE VERIFICATION     ║
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
                    f"[bold white] Phone: {parts[1]}\n"
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
        if delay < 30:
            delay = 30
        
        banner()
        print(Panel("[bold yellow] ⚡ STARTING ACCOUNT CREATION...", style="bold magenta2"))
        print(Panel("[bold yellow] ⚠️ USING PHONE VERIFICATION", style="bold magenta2"))
        
        for i in range(num_accounts):
            print(Panel(f"[bold cyan] 📊 PROGRESS: {i+1}/{num_accounts}", style="bold magenta2"))
            
            if create_facebook_account():
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
