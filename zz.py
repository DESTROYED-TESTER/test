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
passw = ""
ua = UserAgent()

# --- Multiple Email Providers ---
def get_temp_email():
    """Get temporary email from multiple providers."""
    providers = [
        get_fakemail_email,
        get_temp_mail_email,
        get_guerrilla_email,
        get_temp_plus_email
    ]
    
    for provider in providers:
        try:
            email = provider()
            if email:
                return email
        except:
            continue
    return None

def get_temp_mail_email():
    """Get email from temp-mail.io"""
    try:
        response = requests.post('https://api.internal.temp-mail.io/api/v3/email/new', 
                                timeout=10,
                                headers={'User-Agent': ua.random})
        if response.status_code == 200:
            data = response.json()
            return data.get('email')
    except:
        pass
    return None

def get_guerrilla_email():
    """Get email from guerrillamail.com"""
    try:
        response = requests.get('https://api.guerrillamail.com/ajax.php?f=get_email_address',
                               timeout=10)
        if response.status_code == 200:
            data = response.json()
            email = data.get('email_addr')
            if email:
                return email
    except:
        pass
    return None

def get_fakemail_email():
    """Get email from fakemail.net"""
    try:
        response = requests.post('https://api.fakemail.net/email/create', 
                                timeout=10,
                                headers={'User-Agent': ua.random})
        if response.status_code == 200:
            data = response.json()
            return data.get('email')
    except:
        pass
    return None

def get_temp_plus_email():
    """Generate a temporary email using tempmail.plus"""
    try:
        name = Faker().first_name().lower()
        domain = random.choice(['fexbox.org', 'fexpost.com', 'fextemp.com', 'chitthi.in'])
        email = f"{name}{random.randint(100, 999)}@{domain}"
        return email
    except:
        pass
    return None

# --- Email Code Retrieval ---
def get_email_code(email, max_attempts=25, wait=5):
    """Get verification code from email with multiple providers."""
    try:
        # Detect email provider
        domain = email.split('@')[1].lower()
        
        if 'temp-mail' in domain or 'fakemail' in domain:
            return get_temp_mail_code(email, max_attempts, wait)
        elif 'guerrillamail' in domain:
            return get_guerrilla_code(email, max_attempts, wait)
        elif 'fexbox' in domain or 'fexpost' in domain or 'fextemp' in domain or 'chitthi' in domain:
            return get_temp_plus_code(email, max_attempts, wait)
        else:
            return get_fakemail_code(email, max_attempts, wait)
    except:
        return None

def get_temp_mail_code(email, max_attempts, wait):
    """Get code from temp-mail.io"""
    for attempt in range(max_attempts):
        try:
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
                        match = re.search(r'FB-?(\d{5,7})', combined)
                        if match:
                            return match.group(1)
            time.sleep(wait)
        except:
            time.sleep(wait)
    return None

def get_guerrilla_code(email, max_attempts, wait):
    """Get code from guerrillamail.com"""
    sid = email.split('@')[0]
    for attempt in range(max_attempts):
        try:
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
                        match = re.search(r'FB-?(\d{5,7})', combined)
                        if match:
                            return match.group(1)
            time.sleep(wait)
        except:
            time.sleep(wait)
    return None

def get_temp_plus_code(email, max_attempts, wait):
    """Get code from tempmail.plus"""
    session = requests.Session()
    session.cookies.set('email', email)
    
    for attempt in range(max_attempts):
        try:
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
                        match = re.search(r'FB-?(\d{5,7})', combined)
                        if match:
                            return match.group(1)
            time.sleep(wait)
        except:
            time.sleep(wait)
    return None

def get_fakemail_code(email, max_attempts, wait):
    """Get code from fakemail.net"""
    local_part = email.split('@')[0]
    
    for attempt in range(max_attempts):
        try:
            url = f'https://api.fakemail.net/mail/{local_part}'
            response = requests.get(url, timeout=10,
                                  headers={'User-Agent': ua.random})
            
            if response.status_code == 200:
                data = response.json()
                messages = data.get('messages', [])
                
                for msg in messages:
                    subject = msg.get('subject', '')
                    body = msg.get('body', '')
                    html = msg.get('html', '')
                    
                    combined = f"{subject} {body} {html}"
                    
                    patterns = [
                        r'\b(\d{6})\b',
                        r'FB-(\d{6})',
                        r'code[:\s]*(\d{6})',
                        r'verification[:\s]*(\d{6})',
                        r'(\d{5,7})'
                    ]
                    
                    for pattern in patterns:
                        match = re.search(pattern, combined, re.IGNORECASE)
                        if match:
                            code = match.group(1)
                            if len(code) >= 5:
                                return code
            time.sleep(wait)
        except Exception:
            time.sleep(wait)
    return None

# --- User-Agent Generators ---
def get_desktop_ua():
    """Generate realistic desktop user-agent."""
    chrome = f'{random.choice(["120", "121", "122", "123", "124"])}.0.{random.randint(6000, 7000)}.{random.randint(100, 299)}'
    return f'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome} Safari/537.36'

def get_mobile_ua():
    """Generate realistic mobile user-agent."""
    chrome = f'{random.choice(["120", "121", "122", "123"])}.0.{random.randint(6000, 7000)}.{random.randint(100, 299)}'
    android = random.choice(["10", "11", "12", "13", "14"])
    model = random.choice(["SM-G998B", "SM-G991B", "SM-A525F", "Pixel 6", "Pixel 7", "OnePlus 9"])
    return f'Mozilla/5.0 (Linux; Android {android}; {model}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome} Mobile Safari/537.36'

# --- Name & Password Generators ---
def fake_name():
    fake = Faker()
    return fake.first_name(), fake.last_name()

def fake_password():
    first, last = fake_name()
    special = random.choice(['!', '@', '#', '$', '%', '&', '*'])
    return f"{first}{last}{random.randint(1000, 9999)}{special}"

# --- Extract Form Data ---
def extract_form_data(html):
    """Extract all form inputs and hidden values."""
    soup = BeautifulSoup(html, "html.parser")
    data = {}
    
    for inp in soup.find_all("input"):
        name = inp.get("name")
        value = inp.get("value", "")
        if name:
            data[name] = value
    
    for form in soup.find_all("form"):
        for inp in form.find_all("input", type="hidden"):
            name = inp.get("name")
            value = inp.get("value", "")
            if name and name not in data:
                data[name] = value
    
    return data

# --- Get Facebook Tokens ---
def get_fb_tokens(session, url):
    """Extract Facebook tokens from page."""
    try:
        headers = {
            'User-Agent': get_desktop_ua(),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cache-Control': 'max-age=0',
            'Sec-Ch-Ua': '"Not:A-Brand";v="99", "Google Chrome";v="145", "Chromium";v="145"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Platform': '"Windows"',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1'
        }
        
        response = session.get(url, headers=headers, timeout=15)
        
        # Extract tokens
        tokens = {}
        
        # fb_dtsg
        dtsg_match = re.search(r'"fb_dtsg"\s*:\s*"([^"]+)"', response.text)
        if dtsg_match:
            tokens['fb_dtsg'] = dtsg_match.group(1)
        else:
            dtsg_match = re.search(r'name="fb_dtsg"\s+value="([^"]+)"', response.text)
            if dtsg_match:
                tokens['fb_dtsg'] = dtsg_match.group(1)
        
        # lsd
        lsd_match = re.search(r'"LSD",\[\],{"token":"([^"]+)"}', response.text)
        if lsd_match:
            tokens['lsd'] = lsd_match.group(1)
        else:
            lsd_match = re.search(r'name="lsd"\s+value="([^"]+)"', response.text)
            if lsd_match:
                tokens['lsd'] = lsd_match.group(1)
        
        # jazoest
        jazoest_match = re.search(r'"jazoest":"([^"]+)"', response.text)
        if jazoest_match:
            tokens['jazoest'] = jazoest_match.group(1)
        else:
            jazoest_match = re.search(r'name="jazoest"\s+value="([^"]+)"', response.text)
            if jazoest_match:
                tokens['jazoest'] = jazoest_match.group(1)
        
        # reg_instance
        reg_match = re.search(r'name="reg_instance"\s+value="([^"]+)"', response.text)
        if reg_match:
            tokens['reg_instance'] = reg_match.group(1)
        
        # reg_impression_id
        impression_match = re.search(r'name="reg_impression_id"\s+value="([^"]+)"', response.text)
        if impression_match:
            tokens['reg_impression_id'] = impression_match.group(1)
        
        # logger_id
        logger_match = re.search(r'name="logger_id"\s+value="([^"]+)"', response.text)
        if logger_match:
            tokens['logger_id'] = logger_match.group(1)
        
        return tokens, response.text
    except Exception as e:
        print(f"Error getting tokens: {e}")
        return {}, ""

# --- Create Facebook Account ---
def create_facebook_account():
    """Main account creation function."""
    global Ok, Cp
    
    session = requests.Session()
    
    try:
        print(Panel("[bold white] 🔄 INITIALIZING REGISTRATION...", style="bold magenta2"))
        
        # Step 1: Get registration page
        reg_url = 'https://www.facebook.com/reg/?entry_point=login&next='
        tokens, html_content = get_fb_tokens(session, reg_url)
        
        if not tokens:
            print(Panel("[bold red] ❌ FAILED TO GET REGISTRATION PAGE", style="bold magenta2"))
            return False
        
        # Step 2: Generate user data
        firstname, lastname = fake_name()
        
        # Try to get email from multiple providers
        email = None
        for attempt in range(3):
            email = get_temp_email()
            if email:
                break
            print(Panel(f"[bold yellow] ⚠️ Email attempt {attempt+1}/3 failed, retrying...", style="bold magenta2"))
            time.sleep(2)
        
        if not email:
            print(Panel("[bold red] ❌ FAILED TO GET EMAIL FROM ALL PROVIDERS", style="bold magenta2"))
            return False
        
        custom_pass = fake_password()
        
        print(Panel(f"[bold white] 📧 Email: {email}", style="bold magenta2"))
        print(Panel(f"[bold white] 👤 Name: {firstname} {lastname}", style="bold magenta2"))
        
        # Step 3: Prepare registration payload
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
            'lsd': tokens.get('lsd', ''),
            '__dyn': '1ZaaAG1mxu1oz-l0BBBzEnxG6U4a2i5U4e0C8dEc8uwcC4o2fwcW4o3Bw4Ewk9E4W0pKq0FE6S0x81vohw5Owk8aE36wqEd8dE2YwbK0iC1qw8W0k-0jG3qaw4kwbS1Lw9C0le0ue0QU',
            '__csr': '',
            '__req': 'p',
            '__fmt': '1',
            '__user': '0'
        }
        
        # Step 4: Submit registration
        print(Panel("[bold white] ⏳ SUBMITTING REGISTRATION...", style="bold magenta2"))
        
        headers = {
            'Host': 'www.facebook.com',
            'User-Agent': get_desktop_ua(),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://www.facebook.com',
            'Referer': 'https://www.facebook.com/reg/?entry_point=login&next=',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Ch-Ua': '"Not:A-Brand";v="99", "Google Chrome";v="145", "Chromium";v="145"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Platform': '"Windows"',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1'
        }
        
        submit_url = 'https://www.facebook.com/reg/submit/'
        response = session.post(submit_url, data=payload, headers=headers, allow_redirects=True)
        
        # Step 5: Check registration result
        if "c_user" in session.cookies:
            uid = session.cookies.get("c_user")
            print(Panel(f"[bold green] ✅ ACCOUNT CREATED! UID: {uid}", style="bold magenta2"))
            
            # Step 6: Get verification code
            print(Panel("[bold white] 📨 WAITING FOR VERIFICATION CODE...", style="bold magenta2"))
            code = get_email_code(email)
            
            if code:
                print(Panel(f"[bold green] ✅ CODE RECEIVED: {code}", style="bold magenta2"))
                
                # Step 7: Confirm email
                if confirm_email(session, email, uid, code):
                    # Step 8: Save account
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
            print(Panel("[bold red] ❌ REGISTRATION FAILED", style="bold magenta2"))
            Cp += 1
            return False
            
    except Exception as e:
        print(Panel(f"[bold red] ❌ ERROR: {str(e)}", style="bold magenta2"))
        Cp += 1
        return False

# --- Confirm Email ---
def confirm_email(session, email, uid, code):
    """Confirm email with verification code."""
    try:
        confirm_url = 'https://www.facebook.com/confirmation_cliff/'
        
        # Get new tokens for confirmation
        tokens, _ = get_fb_tokens(session, 'https://www.facebook.com/')
        
        payload = {
            'contact': email,
            'type': 'submit',
            'is_soft_cliff': 'false',
            'medium': 'email',
            'code': code,
            'fb_dtsg': tokens.get('fb_dtsg', ''),
            'jazoest': tokens.get('jazoest', ''),
            'lsd': tokens.get('lsd', ''),
            '__dyn': '1ZaaAG1mxu1oz-l0BBBzEnxG6U4a2i5U4e0C8dEc8uwcC4o2fwcW4o3Bw4Ewk9E4W0pKq0FE6S0x81vohw5Owk8aE36wqEd8dE2YwbK0iC1qw8W0k-0jG3qaw4kwbS1Lw9C0le0ue0QU',
            '__csr': '',
            '__req': '4',
            '__fmt': '1',
            '__user': uid
        }
        
        headers = {
            'User-Agent': get_desktop_ua(),
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://www.facebook.com',
            'Referer': 'https://www.facebook.com/',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
        }
        
        response = session.post(confirm_url, data=payload, headers=headers, allow_redirects=True)
        
        if "checkpoint" in response.url:
            print(Panel("[bold red] ❌ ACCOUNT HIT CHECKPOINT", style="bold magenta2"))
            return False
        elif "home" in response.url or "welcome" in response.url:
            print(Panel("[bold green] ✅ EMAIL CONFIRMED!", style="bold magenta2"))
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
    ║     🤖 FACEBOOK ACCOUNT CREATOR - MULTI EMAIL PROVIDER        ║
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

# --- Main Function ---
def main():
    global Ok, Cp
    
    try:
        num_accounts = int(input("[bold white] HOW MANY ACCOUNTS? : "))
        if num_accounts <= 0:
            print(Panel("[bold red] INVALID NUMBER", style="bold magenta2"))
            return
        
        delay = int(input("[bold white] DELAY (seconds) : "))
        if delay < 3:
            delay = 3
        
        banner()
        print(Panel("[bold yellow] ⚡ STARTING ACCOUNT CREATION...", style="bold magenta2"))
        
        for i in range(num_accounts):
            print(Panel(f"[bold cyan] 📊 PROGRESS: {i+1}/{num_accounts}", style="bold magenta2"))
            
            if create_facebook_account():
                print(Panel("[bold green] ✅ ACCOUNT CREATED", style="bold magenta2"))
            else:
                print(Panel("[bold red] ❌ ACCOUNT FAILED", style="bold magenta2"))
            
            if i < num_accounts - 1:
                print(Panel(f"[bold yellow] ⏳ WAITING {delay}s...", style="bold magenta2"))
                time.sleep(delay)
        
        results()
        
    except ValueError:
        print(Panel("[bold red] PLEASE ENTER VALID NUMBERS", style="bold magenta2"))
    except KeyboardInterrupt:
        print(Panel("[bold yellow] ⚠️ PROCESS INTERRUPTED", style="bold magenta2"))
    except Exception as e:
        print(Panel(f"[bold red] ERROR: {str(e)}", style="bold magenta2"))

# --- Get Profile Info ---
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
