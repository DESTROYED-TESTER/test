import os
import sys
import re
import time
import json
import random
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

# --- Anti-Detection Headers ---
def get_random_headers():
    """Generate random headers to avoid detection."""
    chrome_version = f"{random.randint(120, 124)}.0.{random.randint(6000, 7000)}.{random.randint(100, 299)}"
    sec_ch_ua = f'"Google Chrome";v="{random.randint(120, 124)}", "Chromium";v="{random.randint(120, 124)}", "Not?A_Brand";v="99"'
    
    return {
        'User-Agent': get_mobile_ua(),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': random.choice(['en-US,en;q=0.9', 'en-GB,en;q=0.9', 'en-IN,en;q=0.9']),
        'Accept-Encoding': 'gzip, deflate, br',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Sec-Ch-Ua': sec_ch_ua,
        'Sec-Ch-Ua-Mobile': '?1',
        'Sec-Ch-Ua-Platform': '"Android"',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'X-Requested-With': random.choice(['mark.via.gp', 'com.facebook.katana', 'com.facebook.orca']),
        'viewport-width': str(random.randint(360, 420)),
        'dpr': str(random.choice(['1.5', '2.0', '2.5', '3.0']))
    }

def get_mobile_ua():
    """Generate realistic mobile user-agent."""
    chrome = f'{random.choice(["120", "121", "122", "123", "124"])}.0.{random.randint(6000, 7000)}.{random.randint(100, 299)}'
    android = random.choice(["10", "11", "12", "13", "14"])
    
    phones = [
        "SM-G998B", "SM-G991B", "SM-G990B", "SM-A525F", "SM-N986B", 
        "Pixel 6", "Pixel 7", "Pixel 8", "OnePlus 9", "OnePlus 10",
        "Redmi Note 11", "Redmi Note 10", "Realme 8", "Realme 9",
        "Xiaomi 12", "Xiaomi 13", "Vivo V23", "Oppo Reno 8"
    ]
    model = random.choice(phones)
    
    return f'Mozilla/5.0 (Linux; Android {android}; {model}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome} Mobile Safari/537.36'

def get_desktop_ua():
    """Generate realistic desktop user-agent."""
    chrome = f'{random.choice(["120", "121", "122", "123", "124"])}.0.{random.randint(6000, 7000)}.{random.randint(100, 299)}'
    return f'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome} Safari/537.36'

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
            # Try different email APIs
            if 'temp-mail' in domain or 'fakemail' in domain:
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
                            match = re.search(r'(\d{5,7})', combined)
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
                            match = re.search(r'(\d{5,7})', combined)
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
                            match = re.search(r'(\d{5,7})', combined)
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
                            match = re.search(r'(\d{5,7})', combined)
                            if match:
                                return match.group(1)
            
            time.sleep(wait)
        except Exception:
            time.sleep(wait)
    
    return None

# --- Name & Password ---
def fake_name():
    fake = Faker()
    return fake.first_name(), fake.last_name()

def fake_password():
    """Generate realistic password."""
    first, last = fake_name()
    special = random.choice(['!', '@', '#', '$', '%', '&', '*'])
    number = random.randint(1000, 9999)
    
    # Randomize password format
    formats = [
        f"{first}{last}{number}{special}",
        f"{first}{number}{last}{special}",
        f"{first.capitalize()}{last.capitalize()}{number}{special}",
        f"{first}{special}{last}{number}",
        f"{first}{number}{special}{last}"
    ]
    
    return random.choice(formats)

# --- Facebook Registration ---
def create_facebook_account():
    """Create Facebook account with anti-detection."""
    global Ok, Cp
    
    # Random delay to avoid detection
    time.sleep(random.uniform(1, 3))
    
    session = requests.Session()
    
    try:
        print(Panel("[bold white] 🔄 INITIALIZING REGISTRATION...", style="bold magenta2"))
        
        # Step 1: Get registration page with random headers
        headers = get_random_headers()
        response = session.get('https://touch.facebook.com/reg/', headers=headers, timeout=15)
        
        if response.status_code != 200:
            print(Panel("[bold red] ❌ FAILED TO ACCESS REGISTRATION", style="bold magenta2"))
            return False
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Step 2: Extract all tokens
        tokens = {}
        for inp in soup.find_all('input', type='hidden'):
            name = inp.get('name')
            value = inp.get('value')
            if name and value:
                tokens[name] = value
        
        # Extract from JavaScript
        js_match = re.search(r'requireLazy\(\["Bootloader"\], function\(\)\s*{\s*Bootloader\.setResourceMap\((.*?)\);\s*}\)', response.text, re.DOTALL)
        if js_match:
            try:
                data = json.loads(js_match.group(1))
                for key, value in data.items():
                    if 'fb_dtsg' in key:
                        tokens['fb_dtsg'] = value
                    elif 'lsd' in key:
                        tokens['lsd'] = value
            except:
                pass
        
        # Fallback extraction
        if 'fb_dtsg' not in tokens:
            dtsg_match = re.search(r'"fb_dtsg":"([^"]+)"', response.text)
            if dtsg_match:
                tokens['fb_dtsg'] = dtsg_match.group(1)
        
        if 'lsd' not in tokens:
            lsd_match = re.search(r'"lsd":"([^"]+)"', response.text)
            if lsd_match:
                tokens['lsd'] = lsd_match.group(1)
        
        if 'jazoest' not in tokens:
            jazoest_match = re.search(r'"jazoest":"([^"]+)"', response.text)
            if jazoest_match:
                tokens['jazoest'] = jazoest_match.group(1)
        
        if not tokens.get('fb_dtsg'):
            print(Panel("[bold red] ❌ FAILED TO GET REGISTRATION TOKENS", style="bold magenta2"))
            return False
        
        # Step 3: Generate user data
        firstname, lastname = fake_name()
        email = generate_email()
        custom_pass = fake_password()
        
        print(Panel(f"[bold white] 📧 Email: {email}", style="bold magenta2"))
        print(Panel(f"[bold white] 👤 Name: {firstname} {lastname}", style="bold magenta2"))
        
        # Step 4: Prepare registration payload
        payload = {
            'reg_instance': tokens.get('reg_instance', ''),
            'submission_request': 'true',
            'helper': '',
            'reg_impression_id': tokens.get('reg_impression_id', ''),
            'ns': '1',
            'zero_header_af_client': '',
            'app_id': '103',
            'logger_id': tokens.get('logger_id', ''),
            'field_names[0]': 'firstname',
            'firstname': firstname,
            'lastname': lastname,
            'field_names[1]': 'birthday_wrapper',
            'birthday_day': str(random.randint(1, 28)),
            'birthday_month': str(random.randint(1, 12)),
            'birthday_year': str(random.randint(1992, 2005)),
            'field_names[2]': 'reg_email__',
            'reg_email__': email,
            'field_names[3]': 'sex',
            'sex': random.choice(['1', '2']),
            'field_names[4]': 'reg_passwd__',
            'reg_passwd__': custom_pass,
            'name_suggest_elig': 'false',
            'was_shown_name_suggestions': 'false',
            'did_use_suggested_name': 'false',
            'use_custom_gender': 'false',
            'guid': '',
            'pre_form_step': '',
            'encpass': f'#PWD_BROWSER:0:{int(time.time())}:{custom_pass}',
            'submit': 'Sign Up',
            'fb_dtsg': tokens.get('fb_dtsg', ''),
            'jazoest': tokens.get('jazoest', ''),
            'lsd': tokens.get('lsd', '')
        }
        
        # Step 5: Submit registration with random delay
        print(Panel("[bold white] ⏳ SUBMITTING REGISTRATION...", style="bold magenta2"))
        time.sleep(random.uniform(0.5, 1.5))
        
        submit_headers = {
            'Host': 'm.facebook.com',
            'User-Agent': get_mobile_ua(),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language': random.choice(['en-US,en;q=0.9', 'en-GB,en;q=0.9']),
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://m.facebook.com',
            'Referer': 'https://m.facebook.com/reg/',
            'Upgrade-Insecure-Requests': '1',
            'X-Requested-With': random.choice(['mark.via.gp', 'com.facebook.katana']),
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1'
        }
        
        response = session.post('https://m.facebook.com/reg/submit/', 
                               data=payload, headers=submit_headers, 
                               allow_redirects=True, timeout=30)
        
        # Step 6: Check registration result
        if "c_user" in session.cookies:
            uid = session.cookies.get("c_user")
            print(Panel(f"[bold green] ✅ ACCOUNT CREATED! UID: {uid}", style="bold magenta2"))
            
            # Step 7: Wait for verification code
            print(Panel("[bold white] 📨 WAITING FOR VERIFICATION CODE...", style="bold magenta2"))
            code = get_email_code(email)
            
            if code:
                print(Panel(f"[bold green] ✅ CODE RECEIVED: {code}", style="bold magenta2"))
                
                # Step 8: Confirm email
                if confirm_email_mobile(session, email, uid, code):
                    # Step 9: Save account
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
            # Check for checkpoint
            if "checkpoint" in response.text.lower() or "login_save_device" in response.text.lower():
                print(Panel("[bold red] ❌ ACCOUNT HIT CHECKPOINT - SKIPPING", style="bold magenta2"))
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

def confirm_email_mobile(session, email, uid, code):
    """Confirm email using mobile flow."""
    try:
        time.sleep(random.uniform(1, 3))
        
        # Get fresh tokens
        headers = get_random_headers()
        response = session.get('https://m.facebook.com/confirmemail.php?next=https%3A%2F%2Fm.facebook.com%2F%3Fdeoia%3D1&soft=hjk', 
                              headers=headers, timeout=15)
        
        tokens = {}
        soup = BeautifulSoup(response.text, 'html.parser')
        
        for inp in soup.find_all('input', type='hidden'):
            name = inp.get('name')
            value = inp.get('value')
            if name and value:
                tokens[name] = value
        
        if 'fb_dtsg' not in tokens:
            dtsg_match = re.search(r'"fb_dtsg":"([^"]+)"', response.text)
            if dtsg_match:
                tokens['fb_dtsg'] = dtsg_match.group(1)
        
        if 'lsd' not in tokens:
            lsd_match = re.search(r'"lsd":"([^"]+)"', response.text)
            if lsd_match:
                tokens['lsd'] = lsd_match.group(1)
        
        if 'jazoest' not in tokens:
            jazoest_match = re.search(r'"jazoest":"([^"]+)"', response.text)
            if jazoest_match:
                tokens['jazoest'] = jazoest_match.group(1)
        
        # Confirmation payload
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
            'X-Requested-With': random.choice(['mark.via.gp', 'com.facebook.katana']),
            'Origin': 'https://m.facebook.com',
            'Referer': 'https://m.facebook.com/confirmemail.php?next=https%3A%2F%2Fm.facebook.com%2F%3Fdeoia%3D1&soft=hjk',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': random.choice(['en-US,en;q=0.9', 'en-GB,en;q=0.9']),
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1'
        }
        
        response = session.post('https://m.facebook.com/confirmation_cliff/', 
                               data=payload, headers=confirm_headers, 
                               allow_redirects=True, timeout=30)
        
        # Check if confirmation was successful
        if "checkpoint" in response.url:
            print(Panel("[bold red] ❌ CONFIRMATION HIT CHECKPOINT", style="bold magenta2"))
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
    ║     🤖 FACEBOOK ACCOUNT CREATOR - ANTI-DETECTION               ║
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
    ║  [3] 🔍 GET PROFILE INFORMATION                                ║
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

# --- Profile Info ---
def get_facebook_profile_info(username):
    try:
        headers = {'User-Agent': get_desktop_ua()}
        response = requests.get(f'https://www.facebook.com/{username}', headers=headers, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            title = soup.find('title')
            if title:
                return title.text.strip()
        return "PROFILE NOT FOUND"
    except:
        return "ERROR FETCHING PROFILE"

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
        if delay < 10:
            delay = 10
        
        banner()
        print(Panel("[bold yellow] ⚡ STARTING ACCOUNT CREATION...", style="bold magenta2"))
        
        for i in range(num_accounts):
            print(Panel(f"[bold cyan] 📊 PROGRESS: {i+1}/{num_accounts}", style="bold magenta2"))
            
            if create_facebook_account():
                print(Panel("[bold green] ✅ ACCOUNT CREATED", style="bold magenta2"))
            else:
                print(Panel("[bold red] ❌ ACCOUNT FAILED", style="bold magenta2"))
            
            if i < num_accounts - 1:
                # Random delay to avoid pattern detection
                random_delay = delay + random.randint(0, 10)
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
        elif choice in ["3", "03"]:
            banner()
            username = input("[bold white] Enter Facebook username/ID: ")
            if username:
                profile = get_facebook_profile_info(username)
                print(Panel(f"[bold white] PROFILE: {profile}", style="bold magenta2"))
            input("[bold white] Press Enter to continue...")
        elif choice in ["0", "00"]:
            print(Panel("[bold green] 👋 GOODBYE!", style="bold magenta2"))
            break
        else:
            print(Panel("[bold red] ❌ INVALID OPTION", style="bold magenta2"))
            time.sleep(1)
