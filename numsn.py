import os
import random
import re
import sys
import time
import platform
import webbrowser
import json
import certifi
import threading
import requests
from concurrent.futures import ThreadPoolExecutor
import ssl
import socket
import base64
from datetime import datetime, timezone, timedelta
import hashlib
import itertools

# Color codes for Termux
WHITE = '\033[1;97m'
GREEN = '\033[1;92m'
RED = '\033[1;91m'
CYAN = '\033[1;96m'
YELLOW = '\033[1;93m'
BLUE = '\033[1;94m'
MAGENTA = '\033[1;95m'

# Server mapping
SERVER_MAP = {
    1: 'm.facebook.com',
    2: 'mbasic.facebook.com',
    3: 'touch.facebook.com',
    4: 'free.facebook.com',
    5: 'm.alpha.facebook.com',
    6: 'm.beta.facebook.com',
    7: 'x.facebook.com'
}

# Global counters
total_checked = 0
total_success = 0
total_failed = 0
total_error = 0
PROXIES = None
CURRENT_LOCALE = 'en_US'

def clear_screen():
    os.system('clear')

def print_logo():
    clear_screen()
    print(f"""{GREEN}
    ███╗   ███╗██████╗ ███████╗██╗  ██╗██████╗ 
    ████╗ ████║██╔══██╗██╔════╝╚██╗██╔╝██╔══██╗
    ██╔████╔██║██████╔╝███████╗ ╚███╔╝ ██████╔╝
    ██║╚██╔╝██║██╔══██╗╚════██║ ██╔██╗ ██╔══██╗
    ██║ ╚═╝ ██║██║  ██║███████║██╔╝ ██╗██║  ██║
    ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝
    {WHITE}Termux Version v1.0
    {CYAN}═══════════════════════════════════════════════════
    {GREEN}[{RED}●{GREEN}] Tool: Facebook Account Recovery
    {GREEN}[{RED}●{GREEN}] Platform: Termux/Android
    {CYAN}═══════════════════════════════════════════════════""")

def get_termux_device_id():
    """Generate device ID for Termux"""
    try:
        # Use Android device info
        unique_data = []
        
        # Get device serial if available
        try:
            with open('/proc/cpuinfo', 'r') as f:
                cpu_info = f.read()
                unique_data.append(cpu_info)
        except:
            pass
            
        # Get Android ID if available
        try:
            # Try to get Android ID
            import subprocess
            android_id = subprocess.check_output(
                ['settings', 'get', 'secure', 'android_id'],
                stderr=subprocess.DEVNULL
            ).decode().strip()
            if android_id:
                unique_data.append(android_id)
        except:
            pass
            
        # Fallback to system info
        if not unique_data:
            unique_data.append(platform.node())
            unique_data.append(platform.version())
            
        raw_id = ''.join(unique_data).replace(' ', '').replace('\n', '')
        hashed_id = hashlib.sha256(raw_id.encode()).hexdigest().upper()
        return hashed_id[:32]
        
    except Exception as e:
        # Final fallback
        fallback = str(os.geteuid()) + platform.node() + platform.version()
        hashed_id = hashlib.sha256(fallback.encode()).hexdigest().upper()
        return hashed_id[:32]

def load_numbers_from_file():
    """Load phone numbers from file"""
    files = [f for f in os.listdir('.') if f.endswith('.txt') and 'number' in f.lower()]
    
    if not files:
        print(f"{RED}No number file found!")
        print(f"{WHITE}Please create a file named 'numbers.txt' with one number per line")
        return []
        
    if len(files) == 1:
        filename = files[0]
    else:
        print(f"{GREEN}Found {len(files)} files:")
        for idx, f in enumerate(files, 1):
            print(f" {GREEN}[{RED}{idx}{GREEN}] {f}")
        choice = input(f"{GREEN}[{RED}●{GREEN}] Select file: {WHITE}")
        try:
            filename = files[int(choice)-1]
        except:
            filename = files[0]
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            numbers = [line.strip() for line in f if line.strip()]
        print(f"{GREEN}Loaded {len(numbers)} numbers from {filename}")
        return numbers
    except Exception as e:
        print(f"{RED}Error reading file: {e}")
        return []

def check_account(number, proxy=None):
    """Check Facebook account recovery options"""
    global total_checked, total_success, total_failed, total_error
    
    session = requests.Session()
    if proxy:
        session.proxies.update(proxy)
    
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; Mobile) AppleWebKit/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
        }
        
        # Get initial page
        url = 'https://m.facebook.com/login/identify/?ctx=recover'
        response = session.get(url, headers=headers)
        
        if response.status_code != 200:
            print(f"{RED}[ERROR] Cannot access Facebook")
            return
        
        # Extract tokens
        lsd_match = re.search('name="lsd" value="(.*?)"', response.text)
        jazoest_match = re.search('name="jazoest" value="(.*?)"', response.text)
        
        if not lsd_match or not jazoest_match:
            print(f"{YELLOW}[RETRY] Token not found for {number}")
            return
        
        lsd = lsd_match.group(1)
        jazoest = jazoest_match.group(1)
        
        # Submit phone number
        data = {
            'lsd': lsd,
            'jazoest': jazoest,
            'email': number,
            'did_submit': 'Search'
        }
        
        response = session.post(url, data=data, headers=headers)
        
        # Check result
        if 'id="login_identify_search_error_msg"' in response.text:
            print(f"{MAGENTA}[NOT FOUND] {number}")
            total_failed += 1
        elif 'contact_point_selector_form' in response.text:
            print(f"{GREEN}[SUCCESS] {number} - Recovery options available")
            total_success += 1
        else:
            print(f"{YELLOW}[UNKNOWN] {number}")
            total_failed += 1
            
        total_checked += 1
        
    except Exception as e:
        print(f"{RED}[ERROR] {number}: {str(e)[:50]}")
        total_error += 1
        total_checked += 1

def main_menu():
    """Display main menu"""
    while True:
        print_logo()
        print(f"""
    {GREEN}[{RED}01{GREEN}] Start Account Recovery Check
    {GREEN}[{RED}02{GREEN}] Load/Change Number File
    {GREEN}[{RED}03{GREEN}] Set Proxy
    {GREEN}[{RED}04{GREEN}] Settings
    {GREEN}[{RED}00{GREEN}] Exit
    {CYAN}═══════════════════════════════════════════════════""")
        
        choice = input(f"{GREEN}[{RED}●{GREEN}] Select option: {WHITE}")
        
        if choice == '01' or choice == '1':
            start_recovery()
        elif choice == '02' or choice == '2':
            load_numbers_menu()
        elif choice == '03' or choice == '3':
            set_proxy()
        elif choice == '04' or choice == '4':
            settings_menu()
        elif choice == '00' or choice == '0':
            print(f"{GREEN}Goodbye!")
            sys.exit(0)
        else:
            print(f"{RED}Invalid option!")

def start_recovery():
    """Start the recovery checking process"""
    numbers = load_numbers_from_file()
    
    if not numbers:
        input(f"{RED}No numbers to check! Press Enter to continue...")
        return
    
    print(f"\n{GREEN}Starting recovery check for {len(numbers)} numbers...")
    
    # Get thread count
    try:
        threads = int(input(f"{GREEN}[{RED}●{GREEN}] Threads (1-10): {WHITE}") or "5")
        threads = max(1, min(10, threads))
    except:
        threads = 5
    
    # Reset counters
    global total_checked, total_success, total_failed, total_error
    total_checked = total_success = total_failed = total_error = 0
    
    print(f"{CYAN}═══════════════════════════════════════════════════")
    
    # Start checking
    with ThreadPoolExecutor(max_workers=threads) as executor:
        for number in numbers:
            executor.submit(check_account, number)
    
    # Wait for completion
    executor.shutdown(wait=True)
    
    print(f"{CYAN}═══════════════════════════════════════════════════")
    print(f"{GREEN}[{WHITE}RESULTS{GREEN}]")
    print(f"{GREEN}✓ Success: {total_success}")
    print(f"{YELLOW}✗ Failed: {total_failed}")
    print(f"{RED}! Errors: {total_error}")
    print(f"{WHITE}Total: {total_checked}")
    
    input(f"\n{WHITE}Press Enter to continue...")

def load_numbers_menu():
    """Menu for loading numbers"""
    print_logo()
    
    if os.path.exists('numbers.txt'):
        with open('numbers.txt', 'r') as f:
            count = len([line for line in f if line.strip()])
        print(f"{GREEN}Current file: numbers.txt ({count} numbers)")
    else:
        print(f"{RED}No numbers.txt file found!")
    
    print(f"""
    {GREEN}[{RED}1{GREEN}] Use existing numbers.txt
    {GREEN}[{RED}2{GREEN}] Create new numbers.txt
    {GREEN}[{RED}3{GREEN}] Import from another file
    {GREEN}[{RED}0{GREEN}] Back to main menu
    """)
    
    choice = input(f"{GREEN}[{RED}●{GREEN}] Select: {WHITE}")
    
    if choice == '1':
        if os.path.exists('numbers.txt'):
            print(f"{GREEN}Using existing numbers.txt")
        else:
            print(f"{RED}File not found!")
    elif choice == '2':
        print(f"\n{WHITE}Enter phone numbers (one per line).")
        print(f"{WHITE}Type 'done' on a new line when finished:")
        print(f"{CYAN}═══════════════════════════════════════════════════")
        
        numbers = []
        while True:
            line = input().strip()
            if line.lower() == 'done':
                break
            if line:
                numbers.append(line)
        
        with open('numbers.txt', 'w') as f:
            f.write('\n'.join(numbers))
        
        print(f"{GREEN}Saved {len(numbers)} numbers to numbers.txt")
    elif choice == '3':
        files = [f for f in os.listdir('.') if f.endswith('.txt')]
        if files:
            print(f"{GREEN}Available files:")
            for f in files:
                print(f"  {f}")
            filename = input(f"{GREEN}Enter filename: {WHITE}")
            if os.path.exists(filename):
                with open(filename, 'r') as src, open('numbers.txt', 'w') as dst:
                    dst.write(src.read())
                print(f"{GREEN}File imported!")
            else:
                print(f"{RED}File not found!")
        else:
            print(f"{RED}No text files found!")
    
    input(f"\n{WHITE}Press Enter to continue...")

def set_proxy():
    """Set proxy configuration"""
    print_logo()
    print(f"{GREEN}Proxy Configuration\n")
    
    proxy = input(f"{GREEN}[{RED}●{GREEN}] Enter proxy (format: ip:port:user:pass or ip:port): {WHITE}")
    
    if proxy:
        parts = proxy.split(':')
        if len(parts) == 4:
            ip, port, user, pwd = parts
            proxy_url = f"http://{user}:{pwd}@{ip}:{port}"
        elif len(parts) == 2:
            ip, port = parts
            proxy_url = f"http://{ip}:{port}"
        else:
            print(f"{RED}Invalid proxy format!")
            return
        
        # Test proxy
        try:
            test = requests.get('http://httpbin.org/ip', 
                              proxies={'http': proxy_url, 'https': proxy_url},
                              timeout=10)
            if test.status_code == 200:
                print(f"{GREEN}✓ Proxy working!")
                global PROXIES
                PROXIES = {'http': proxy_url, 'https': proxy_url}
            else:
                print(f"{RED}✗ Proxy test failed!")
        except Exception as e:
            print(f"{RED}✗ Proxy error: {e}")
    else:
        PROXIES = None
        print(f"{GREEN}Proxy cleared!")
    
    input(f"\n{WHITE}Press Enter to continue...")

def settings_menu():
    """Settings menu"""
    print_logo()
    print(f"{GREEN}Settings\n")
    
    print(f"1. Server: {SERVER_MAP.get(1, 'm.facebook.com')}")
    print(f"2. Threads: 5")
    print(f"3. Timeout: 30 seconds")
    print(f"0. Back")
    
    choice = input(f"\n{GREEN}[{RED}●{GREEN}] Select: {WHITE}")
    
    if choice == '0':
        return
    
    input(f"\n{WHITE}Settings saved! Press Enter to continue...")

def check_requirements():
    """Check if required packages are installed"""
    required = ['requests', 'certifi']
    missing = []
    
    for package in required:
        try:
            __import__(package.replace('-', '_'))
        except ImportError:
            missing.append(package)
    
    if missing:
        print(f"{RED}Missing packages: {', '.join(missing)}")
        print(f"{WHITE}Install with: pip install {' '.join(missing)}")
        return False
    
    return True

if __name__ == "__main__":
    # Check if running on Termux/Android
    if 'ANDROID_ROOT' not in os.environ:
        print(f"{YELLOW}Warning: This script is optimized for Termux/Android")
        print(f"{WHITE}Continue anyway? (y/n): ", end='')
        if input().lower() != 'y':
            sys.exit(0)
    
    # Check requirements
    if not check_requirements():
        sys.exit(1)
    
    # Create necessary files
    if not os.path.exists('numbers.txt'):
        with open('numbers.txt', 'w') as f:
            f.write("# Add phone numbers here, one per line\n")
            f.write("# Example:\n")
            f.write("# 1234567890\n")
            f.write("# 0987654321\n")
    
    try:
        main_menu()
    except KeyboardInterrupt:
        print(f"\n{GREEN}Program stopped by user.")
        sys.exit(0)
    except Exception as e:
        print(f"{RED}Error: {e}")
        sys.exit(1)
