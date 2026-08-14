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

# --- Date & Time ---
bulan = {'1': 'January', '2': 'February', '3': 'March', '4': 'April', '5': 'May', '6': 'June',
         '7': 'July', '8': 'August', '9': 'September', '10': 'October', '11': 'November', '12': 'December'}
tgl = datetime.now().day
bln = bulan[str(datetime.now().month)]
thn = datetime.now().year
tanggal = f"{tgl} {bln} {thn}"
waktu = strftime('%H:%M:%S')
hari = datetime.now().strftime("%A")

# --- Global Variables ---
Ok, Cp = 0, 0
passw = ""
ua = UserAgent()

# --- Email: fakemail.net API (Improved) ---
def get_fakemail_email():
    """
    Creates a new temporary email using fakemail.net API with retry mechanism.
    """
    for attempt in range(3):
        try:
            response = requests.post('https://api.fakemail.net/email/create', 
                                    timeout=15,
                                    headers={'User-Agent': ua.random})
            if response.status_code == 200:
                data = response.json()
                email = data.get('email')
                if email:
                    return email
            time.sleep(2)
        except Exception:
            continue
    return None

def get_fakemail_code(email, max_attempts=15, wait=3):
    """
    Waits for verification code from fakemail.net with improved detection.
    """
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
                    
                    # Try different patterns
                    patterns = [
                        r'\b(\d{6})\b',           # 6 digits
                        r'FB-(\d{6})',            # FB-123456
                        r'code[:\s]*(\d{6})',      # code: 123456
                        r'verification[:\s]*(\d{6})', # verification: 123456
                        r'(\d{5,7})'               # 5-7 digits
                    ]
                    
                    for pattern in patterns:
                        match = re.search(pattern, combined)
                        if match:
                            code = match.group(1)
                            if len(code) >= 5:
                                return code
            time.sleep(wait)
        except Exception:
            time.sleep(wait)
    return None

# --- Enhanced User-Agent Generator ---
def get_facebook_ua():
    """Generate realistic Facebook mobile user-agent."""
    chrome = f'{random.choice(["110", "111", "112", "113", "114", "115", "116", "117", "118", "119", "120"])}.0.{random.randint(5000, 7000)}.{random.randint(100, 299)}'
    android = random.choice(["10", "11", "12", "13", "14"])
    model = random.choice(["SM-G998B", "SM-G991B", "SM-G990B", "SM-A525F", "SM-A536B", 
                          "Redmi Note 11", "Redmi Note 10", "M2101K7BG", "M2103K19G",
                          "Pixel 6", "Pixel 7", "Pixel 8", "OnePlus 9", "OnePlus 10"])
    
    return f'Mozilla/5.0 (Linux; Android {android}; {model}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome} Mobile Safari/537.36'

def get_desktop_ua():
    """Generate realistic desktop user-agent."""
    chrome = f'{random.choice(["110", "111", "112", "113", "114", "115"])}.0.{random.randint(5000, 7000)}.{random.randint(100, 299)}'
    return f'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome} Safari/537.36'

# --- Name & Password Generators ---
def fake_name():
    fake = Faker()
    return fake.first_name(), fake.last_name()

def fake_password():
    first, last = fake_name()
    special = random.choice(['!', '@', '#', '$', '%', '&', '*'])
    return f"{first}{last}{random.randint(1000, 9999)}{special}"

# --- Loading Animation ---
def loading_animation(word):
    frames = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]",
              "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]",
              "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
    for _ in range(3):
        for frame in frames:
            sys.stdout.write(f'\r{word} {frame}')
            sys.stdout.flush()
            time.sleep(0.05)

# --- Extract Form Data ---
def extract_form_data(html):
    """Extract all form inputs and hidden values."""
    soup = BeautifulSoup(html, "html.parser")
    data = {}
    
    # Get all input fields
    for inp in soup.find_all("input"):
        name = inp.get("name")
        value = inp.get("value", "")
        if name:
            data[name] = value
    
    # Get all hidden input values from forms
    for form in soup.find_all("form"):
        for inp in form.find_all("input", type="hidden"):
            name = inp.get("name")
            value = inp.get("value", "")
            if name and name not in data:
                data[name] = value
    
    # Extract additional meta data
    for meta in soup.find_all("meta"):
        name = meta.get("name")
        content = meta.get("content")
        if name and content:
            data[f"meta_{name}"] = content
    
    return data

# --- Get Facebook DTSG ---
def get_fb_dtsg(session, url):
    """Extract fb_dtsg from page."""
    try:
        response = session.get(url, timeout=15, headers={'User-Agent': get_desktop_ua()})
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Try to find fb_dtsg in multiple ways
        patterns = [
            r'"fb_dtsg"\s*:\s*"([^"]+)"',
            r'name="fb_dtsg"\s+value="([^"]+)"',
            r'FB_DTSG\s*=\s*"([^"]+)"',
            r'"token"\s*:\s*"([^"]+)"'
        ]
        
        for pattern in patterns:
            match = re.search(pattern, response.text)
            if match:
                return match.group(1)
        
        return "NAcMC2x5X2VrJ7jhipS0eIpYv1zLRrDsb5y2wzau2bw3ipw88fbS_9A:0:0"
    except:
        return "NAcMC2x5X2VrJ7jhipS0eIpYv1zLRrDsb5y2wzau2bw3ipw88fbS_9A:0:0"

# --- Get Registration Instance ---
def get_reg_instance(html):
    """Extract registration instance."""
    patterns = [
        r'reg_instance["\']?\s*[:=]\s*["\']([^"\']+)',
        r'name="reg_instance"\s+value="([^"]+)"',
        r'reg_instance=([^&\s]+)'
    ]
    
    for pattern in patterns:
        match = re.search(pattern, html)
        if match:
            return match.group(1)
    return ""

# --- Account Creation (Improved) ---
def create_facebook_account():
    """Main account creation function with improved success rate."""
    global Ok, Cp, passw
    
    session = requests.Session()
    
    # Step 1: Get initial registration page
    try:
        print(Panel("[bold white] INITIALIZING REGISTRATION...", style="bold magenta2"))
        resp = session.get('https://www.facebook.com/reg/?entry_point=login&next=', 
                          headers={'User-Agent': get_facebook_ua()})
        
        if resp.status_code != 200:
            print(Panel("[bold red] FAILED TO ACCESS REGISTRATION PAGE", style="bold magenta2"))
            return False
        
        form_data = extract_form_data(resp.text)
        
        # Get required tokens
        fb_dtsg = get_fb_dtsg(session, 'https://m.facebook.com/')
        reg_instance = get_reg_instance(resp.text)
        
        # Step 2: Generate user data
        firstname, lastname = fake_name()
        email = get_fakemail_email()
        
        if not email:
            print(Panel("[bold red] FAILED TO GET EMAIL", style="bold magenta2"))
            return False
        
        # Generate password
        custom_pass = fake_password()
        
        # Step 3: Prepare registration payload
        payload = {
            'ccp': '2',
            'reg_instance': reg_instance,
            'submission_request': 'true',
            'helper': '',
            'reg_impression_id': form_data.get('reg_impression_id', ''),
            'ns': '1',
            'zero_header_af_client': '',
            'app_id': '103',
            'logger_id': form_data.get('logger_id', ''),
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
            'sex': random.choice(['1', '2']),  # 1=male, 2=female
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
            'fb_dtsg': fb_dtsg,
            'jazoest': form_data.get('jazoest', ''),
            'lsd': form_data.get('lsd', ''),
            '__dyn': '1ZaaAG1mxu1oz-l0BBBzEnxG6U4a2i5U4e0C8dEc8uwcC4o2fwcW4o3Bw4Ewk9E4W0pKq0FE6S0x81vohw5Owk8aE36wqEd8dE2YwbK0iC1qw8W0k-0jG3qaw4kwbS1Lw9C0le0ue0QU',
            '__csr': '',
            '__req': 'p',
            '__fmt': '1',
            '__user': '0'
        }
        
        # Step 4: Submit registration
        print(Panel(f"[bold white] CREATING ACCOUNT: {firstname} {lastname}", style="bold magenta2"))
        loading_animation("SUBMITTING...")
        
        headers = {
            'Host': 'm.facebook.com',
            'User-Agent': get_facebook_ua(),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://m.facebook.com',
            'Referer': 'https://m.facebook.com/reg/',
            'Upgrade-Insecure-Requests': '1',
            'X-Requested-With': 'mark.via.gp',
            'sec-ch-ua': '"Android WebView";v="120", "Chromium";v="120", "Not_A Brand";v="24"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
        }
        
        reg_url = 'https://m.facebook.com/reg/submit/'
        response = session.post(reg_url, data=payload, headers=headers, allow_redirects=True)
        
        # Step 5: Check if registration was successful
        if "c_user" in session.cookies:
            uid = session.cookies.get("c_user")
            print(Panel(f"[bold green] ACCOUNT CREATED! UID: {uid}", style="bold magenta2"))
            
            # Step 6: Get verification code
            print(Panel("[bold white] WAITING FOR VERIFICATION CODE...", style="bold magenta2"))
            code = get_fakemail_code(email)
            
            if code:
                print(Panel(f"[bold green] CODE RECEIVED: {code}", style="bold magenta2"))
                
                # Step 7: Confirm email
                if confirm_email(session, email, uid, code, response.text):
                    # Step 8: Save successful account
                    cookie_str = "; ".join([f"{k}={v}" for k, v in session.cookies.get_dict().items()])
                    
                    account_info = (
                        f"UID: {uid}\n"
                        f"Email: {email}\n"
                        f"Password: {custom_pass}\n"
                        f"Cookie: {cookie_str}\n"
                        f"User-Agent: {get_facebook_ua()}\n"
                        f"{'='*50}\n"
                    )
                    
                    with open(f"{FOLDER_PATH}/SUCCESS-OK-ID.txt", "a") as f:
                        f.write(f"{uid}|{email}|{custom_pass}|{cookie_str}\n")
                    
                    with open(f"{FOLDER_PATH}/ACCOUNT_INFO.txt", "a") as f:
                        f.write(account_info)
                    
                    print(Panel(
                        f"[bold green] ACCOUNT CREATED SUCCESSFULLY!\n"
                        f"[bold white] UID: {uid}\n"
                        f"[bold white] Email: {email}\n"
                        f"[bold white] Password: {custom_pass}\n"
                        f"[bold white] Saved to: {FOLDER_PATH}",
                        style="bold magenta2"
                    ))
                    
                    Ok += 1
                    return True
            else:
                print(Panel("[bold red] VERIFICATION CODE NOT RECEIVED", style="bold magenta2"))
                Cp += 1
                return False
        else:
            print(Panel("[bold red] REGISTRATION FAILED - CHECKPOINT", style="bold magenta2"))
            Cp += 1
            return False
            
    except Exception as e:
        print(Panel(f"[bold red] ERROR: {str(e)}", style="bold magenta2"))
        Cp += 1
        return False

def confirm_email(session, email, uid, code, response_text):
    """Confirm email with verification code."""
    try:
        # Get confirmation page
        confirm_url = 'https://m.facebook.com/confirmation_cliff/'
        
        # Extract required tokens
        fb_dtsg = get_fb_dtsg(session, 'https://m.facebook.com/')
        
        # Extract LSD token
        lsd_match = re.search(r'"LSD",\[\],{"token":"([^"]+)"}', response_text)
        lsd = lsd_match.group(1) if lsd_match else ''
        
        # Extract jazoest
        jazoest_match = re.search(r'"jazoest":"([^"]+)"', response_text)
        jazoest = jazoest_match.group(1) if jazoest_match else ''
        
        # Prepare confirmation payload
        payload = {
            'contact': email,
            'type': 'submit',
            'is_soft_cliff': 'false',
            'medium': 'email',
            'code': code,
            'fb_dtsg': fb_dtsg,
            'jazoest': jazoest,
            'lsd': lsd,
            '__dyn': '1ZaaAG1mxu1oz-l0BBBzEnxG6U4a2i5U4e0C8dEc8uwcC4o2fwcW4o3Bw4Ewk9E4W0pKq0FE6S0x81vohw5Owk8aE36wqEd8dE2YwbK0iC1qw8W0k-0jG3qaw4kwbS1Lw9C0le0ue0QU',
            '__csr': '',
            '__req': '4',
            '__fmt': '1',
            '__user': uid
        }
        
        headers = {
            'User-Agent': get_facebook_ua(),
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-Requested-With': 'mark.via.gp',
            'Origin': 'https://m.facebook.com',
            'Referer': 'https://m.facebook.com/confirmemail.php?next=https%3A%2F%2Fm.facebook.com%2F%3Fdeoia%3D1&soft=hjk',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
        }
        
        response = session.post(confirm_url, data=payload, headers=headers, allow_redirects=True)
        
        # Check if confirmation was successful
        if "checkpoint" in response.url:
            print(Panel("[bold red] ACCOUNT HIT CHECKPOINT", style="bold magenta2"))
            return False
        elif "home" in response.url or "welcome" in response.url:
            print(Panel("[bold green] EMAIL CONFIRMED SUCCESSFULLY!", style="bold magenta2"))
            return True
        else:
            # Check response for success indicators
            if "success" in response.text.lower() or "confirmed" in response.text.lower():
                return True
            return False
            
    except Exception as e:
        print(Panel(f"[bold red] CONFIRMATION ERROR: {str(e)}", style="bold magenta2"))
        return False

# --- Profile Info ---
def get_facebook_profile_info(username):
    """Get Facebook profile info."""
    try:
        headers = {'User-Agent': get_facebook_ua()}
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
    """Display saved account information."""
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
                uid = parts[0]
                email = parts[1] if len(parts) > 1 else "N/A"
                password = parts[2] if len(parts) > 2 else "N/A"
                
                print(Panel(
                    f"[bold white] UID: {uid}\n"
                    f"[bold white] Email: {email}\n"
                    f"[bold white] Password: {password}",
                    style="bold magenta2"
                ))
                time.sleep(0.5)
                
    except FileNotFoundError:
        print(Panel("[bold red] NO ACCOUNTS FILE FOUND", style="bold magenta2"))

# --- UI Functions ---
def banner():
    os.system("clear")
    logo = """
    ╔══════════════════════════════════════════════════════════════════╗
    ║     🤖 FACEBOOK ACCOUNT CREATOR - FAKEMAIL.NET API            ║
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
        f" ║ [bold green] ✅ SUCCESSFUL ACCOUNTS: {Ok}\n"
        f" ║ [bold red] ❌ FAILED ACCOUNTS: {Cp}\n"
        f" ║ [bold yellow] 📁 SAVED TO: {FOLDER_PATH}\n"
        f" ╚══════════════════════════════════════════════╝",
        style="bold magenta2", width=102, padding=1
    ))

# --- Main Function ---
def main():
    global Ok, Cp, passw
    
    try:
        num_accounts = int(input("[bold white] HOW MANY ACCOUNTS TO CREATE? : "))
        if num_accounts <= 0:
            print(Panel("[bold red] INVALID NUMBER", style="bold magenta2"))
            return
        
        delay = int(input("[bold white] DELAY BETWEEN REQUESTS (seconds) : "))
        if delay < 2:
            delay = 2
        
        banner()
        print(Panel("[bold yellow] ⚡ STARTING ACCOUNT CREATION...", style="bold magenta2"))
        
        for i in range(num_accounts):
            print(Panel(f"[bold cyan] 📊 PROGRESS: {i+1}/{num_accounts}", style="bold magenta2"))
            
            if create_facebook_account():
                print(Panel("[bold green] ✅ ACCOUNT CREATED SUCCESSFULLY", style="bold magenta2"))
            else:
                print(Panel("[bold red] ❌ ACCOUNT CREATION FAILED", style="bold magenta2"))
            
            if i < num_accounts - 1:
                print(Panel(f"[bold yellow] ⏳ WAITING {delay} SECONDS...", style="bold magenta2"))
                time.sleep(delay)
        
        results()
        
    except ValueError:
        print(Panel("[bold red] PLEASE ENTER VALID NUMBERS", style="bold magenta2"))
    except KeyboardInterrupt:
        print(Panel("[bold yellow] ⚠️ PROCESS INTERRUPTED BY USER", style="bold magenta2"))
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
