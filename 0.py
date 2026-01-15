import requests
import time
import re
import os
import sys
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, Style, init

init(autoreset=True)

# রিপোর্ট গণনার জন্য ভেরিয়েবল
stats = {
    "total": 0,
    "success": 0,
    "no_id": 0,
    "no_sms": 0,
    "error": 0
}

def banner():
    os.system('clear' if os.name == 'posix' else 'cls')
    # রঙিন স্টাইলিশ ASCII ব্যানার
    print(f"{Fore.RED}{Style.BRIGHT}" + r"""
  ______ ____    ______ ____  _____   ______   ________ 
 |  ____|  _ \  |  ____/ __ \|  __ \ / ____ \ |__    __|
 | |__  | |_) | | |__ | |  | | |__) | |    | |   |  |   
 |  __| |  _ <  |  __|| |  | |  _  /| |    | |   |  |   
 | |    | |_) | | |   | |__| | | \ \| |____| |   |  |   
 |_|    |____/  |_|    \____/|_|  \_\\______/    |_|   
                                                        """)
    print(f"{Fore.MAGENTA}{Style.BRIGHT}         >>>> FB FORGOT TOOLS v2.0 <<<<")
    print(f"{Fore.CYAN}{'='*60}")
    print(f"{Fore.YELLOW}{Style.BRIGHT}   Developer : Mir Rifat | WhatsApp : 01826420296")
    print(f"{Fore.GREEN}{Style.BRIGHT}   Version: 2.0 | Android/Termux Optimized")
    print(f"{Fore.CYAN}{'='*60}")
    
    # লাইভ রিপোর্ট বক্স
    print(f"{Fore.WHITE}{Style.BRIGHT} [ LIVE REPORT ]")
    print(f" {Fore.BLUE}Total: {stats['total']} | {Fore.GREEN}Sent: {stats['success']} | {Fore.RED}No ID: {stats['no_id']}")
    print(f" {Fore.YELLOW}No SMS: {stats['no_sms']} | {Fore.MAGENTA}Error: {stats['error']}")
    print(f"{Fore.CYAN}{'='*60}\n")

def get_file_paths():
    """Get file paths from user or use default"""
    print(f"{Fore.YELLOW}📁 FILE LOCATION OPTIONS:")
    print(f"{Fore.CYAN}1. Current Directory")
    print(f"{Fore.CYAN}2. /sdcard/ Directory")
    print(f"{Fore.CYAN}3. Custom Path")
    choice = input(f"{Fore.WHITE}Select option (1/2/3): ").strip()
    
    if choice == '1':
        return {
            'numbers': 'numbers.txt',
            'success': 'success_sent.txt'
        }
    elif choice == '2':
        return {
            'numbers': '/sdcard/numbers.txt',
            'success': '/sdcard/success_sent.txt'
        }
    elif choice == '3':
        base_path = input(f"{Fore.WHITE}Enter custom directory path: ").strip()
        if not base_path.endswith('/'):
            base_path += '/'
        return {
            'numbers': base_path + 'numbers.txt',
            'success': base_path + 'success_sent.txt'
        }
    else:
        print(f"{Fore.RED}Invalid choice. Using /sdcard/")
        return {
            'numbers': '/sdcard/numbers.txt',
            'success': '/sdcard/success_sent.txt'
        }

def load_numbers(filename):
    """Load numbers from file with multiple fallback locations"""
    
    # Define possible file locations
    possible_locations = [
        filename,  # User specified path
        '/sdcard/numbers.txt',
        '/sdcard/phone_numbers.txt',
        '/sdcard/number.txt',
        '/storage/emulated/0/numbers.txt',
        'numbers.txt',
        'phone_numbers.txt',
        'number.txt'
    ]
    
    # Try each location
    for file_path in possible_locations:
        try:
            if os.path.exists(file_path):
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    data = [line.strip() for line in f if line.strip()]
                    if data:
                        print(f"{Fore.GREEN}✓ Loaded {len(data)} numbers from: {file_path}")
                        return data, file_path
        except Exception as e:
            continue
    
    # If no file found, return empty list
    print(f"{Fore.YELLOW}⚠ No numbers file found in any location")
    return [], ""

def process_number(any_number, selected_ua, success_file):
    session = requests.Session()
    headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,bn;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://www.facebook.com',
    'priority': 'u=1, i',
    'referer': 'https://www.facebook.com/login/identify/?ctx=recover&ars=facebook_login&from_login_screen=0',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"',
    'sec-ch-ua-full-version-list': '"Google Chrome";v="143.0.7499.170", "Chromium";v="143.0.7499.170", "Not A(Brand";v="24.0.0.0"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',
    'x-asbd-id': '359341',
    'x-fb-lsd': 'AdGpHjOQTt8',
    # 'cookie': 'datr=Z1hMaIrIfVNAp27gtWl_jtL1; sb=Z1hMaKlrQMZu6pNj3IH-tWgs; ps_l=1; ps_n=1; fr=029IlyRZmpwIAbBNq..Bo1FYF..AAA.0.0.BpaTni.AWecAdEFy_psnwyYwlsWl_ewsqs; wd=1036x773',
}
    cookies = {
    'datr': 'Z1hMaIrIfVNAp27gtWl_jtL1',
    'sb': 'Z1hMaKlrQMZu6pNj3IH-tWgs',
    'ps_l': '1',
    'ps_n': '1',
    'fr': '029IlyRZmpwIAbBNq..Bo1FYF..AAA.0.0.BpaUC7.AWeK1U_dowKlORzca7lX-Nn6j2Q',
    'wd': '919x773',
    'sfiu': 'AYjdbp6OPuuwQIEVNyVP2gQLKymsMKgGkcNQL5J-0fIGxwVRTIM35KADg5dXz8JUhQEFHNOfMaYfG1qXSwvu2G1S4c7RpPNfuAff6HOs9tjzM0bXKwEVlxuP3W1ZtnoOblpxRrSVt2L8xcE2nPhdu15TzMYYU5ZXZVaHPTmFxpy3W9Dd-giFXI3d125Iy1qEX7YrYHeftoRAYG3movhrXtUBbXeD4MgIlGQXBCSMnqt6QQ',
}
    params = {
    'ctx': 'not_my_account',
}
    try:
        # Step 1: Search for account
        payload = {
    'jazoest': '2940',
    'lsd': 'AdGpHjOQEFs',
    'email': any_number,
    'did_submit': '1',
    '__user': '0',
    '__a': '1',
    '__req': '6',
    '__hs': '20468.BP:DEFAULT.2.0...0',
    'dpr': '1',
    '__ccg': 'EXCELLENT',
    '__rev': '1032049861',
    '__s': 'sflqtb:my7aaa:6evjim',
    '__hsi': '7595674312159156008',
    '__dyn': '7xeUmwkHg7ebwKBAg5S1Dxu13wqovzEdEc8uxa0CEbo1nEhw2nVE4W0qa0FE2awt81s8hwGwQw4iwBgao6C0Mo2swaO4U2zxe3C0D85a1qw8Xxm16wa-0raazo7u0zE2ZwrU6C0hq1Iw5lwnqwIwtU5K0UE62',
    '__hsdp': 'gIMggq8yqA7h0hp3D8py4bDyeeqKEyewQocAE7iO04Ewd63B240GGw4iw',
    '__hblp': '0TwbO1nw5Uw3iUfE4-0a6wto0lUw28E08qU0hjw2A805h60c-w3YJ0fO6oll02ZU0qPw13i0FU',
    '__spin_r': '1032049861',
    '__spin_b': 'trunk',
    '__spin_t': '1768505739',
}
        
        response = session.post('https://www.facebook.com/ajax/login/help/identify.php', params=params, cookies=cookies, headers=headers, data=payload)
        
        # Update banner with live stats
        stats['total'] = max(stats['total'], 1)
        os.system('clear' if os.name == 'posix' else 'cls')
        banner()
        
        # Check response
        response_text = response.text.lower()
        if "identify_search_error_title" in response_text or "no search results" in response_text:
            stats['no_id'] += 1
            print(f"{Fore.RED}[-] {any_number} : No Account Found")
            return
        print(f"{Fore.GREEN}[✓] {any_number} : Account Found!")
        
        # Step 3: Extract recovery options
        print(f"{Fore.CYAN}[~] {any_number} : Looking for recovery options...")
        
        # Method 1: Look for data-store attribute (Facebook's new format)
        recovery_method = None
        contact_index = "0"
        
        # Try to find recovery method in data-store
        data_store_pattern = r'data-store=["\'][^"\']*recover_method["\'][^"\']*["\']'
        data_store_matches = re.findall(data_store_pattern, search_response.text, re.IGNORECASE)
        
        for match in data_store_matches:
            # Extract recover_method value
            method_match = re.search(r'recover_method["\']:["\']([^"\']+)["\']', match)
            if method_match:
                recovery_method = method_match.group(1)
                # Extract contact_index if available
                index_match = re.search(r'contact_index["\']:["\']([^"\']+)["\']', match)
                if index_match:
                    contact_index = index_match.group(1)
                break
        
        # Method 2: Look for input fields with name="recover_method"
        if not recovery_method:
            input_pattern = r'<input[^>]*name=["\']recover_method["\'][^>]*value=["\']([^"\']+)["\'][^>]*>'
            input_matches = re.findall(input_pattern, search_response.text, re.IGNORECASE)
            if input_matches:
                recovery_method = input_matches[0]
        
        # Method 3: Look for send_sms in any input field
        if not recovery_method:
            sms_pattern = r'<input[^>]*value=["\'][^"\']*send_sms[^"\']*["\'][^>]*>'
            sms_matches = re.findall(sms_pattern, search_response.text, re.IGNORECASE)
            for sms_match in sms_matches:
                value_match = re.search(r'value=["\']([^"\']+)["\']', sms_match)
                if value_match and 'send_sms' in value_match.group(1).lower():
                    recovery_method = value_match.group(1)
                    break
        
        # Method 4: Look for SMS in the response text (last resort)
        if not recovery_method:
            text_pattern = r'send_sms(?:_\w+)?'
            text_matches = re.findall(text_pattern, search_response.text, re.IGNORECASE)
            if text_matches:
                recovery_method = text_matches[0]
        
        if recovery_method:
            print(f"{Fore.CYAN}[~] {any_number} : Found recovery method: {recovery_method}")
            
            # Step 4: Send SMS request
            print(f"{Fore.CYAN}[~] {any_number} : Sending OTP...")
            
            # Get new lsd token for the send request
            send_lsd_match = re.search(r'["\']lsd["\']\s*value=["\']([^"\']+)["\']', search_response.text)
            if send_lsd_match:
                send_lsd = send_lsd_match.group(1)
            else:
                send_lsd = lsd_token
            
            sms_payload = {
                'lsd': send_lsd,
                'jazoest': '2940',
                'recover_method': recovery_method,
                'contact_index': contact_index,
                'did_submit': 'Continue',
                'fbp': 'fb.1.1698765432101.1234567890',  # Generic fbp value
                '__user': '0',
                '__a': '1',
                '__req': '1',
                '__hs': '19560.BP:DEFAULT.2.0...0',
                'dpr': '1',
                '__ccg': 'EXCELLENT',
                '__rev': '1000000000',
                '__s': 'sflqtb:my7aaa:6evjim',
                '__hsi': '1234567890123456789',
                '__dyn': '7xeUjG1mxu1syUbFp41nzU5W2O0V8S5UbFp41nzU5W2O0V8S5UbFp41nzU5W2O0V8S',
                '__csr': '',
                '__comet_req': '0',
                'fb_dtsg': 'NA',
                '__spin_r': '1000000000',
                '__spin_b': 'trunk',
                '__spin_t': '1698765432',
            }
            
            try:
                # Try different endpoints
                endpoints = [
                    'https://www.facebook.com/ajax/login/help/identify.php?ctx=recover',
                    'https://www.facebook.com/recover/code/',
                    'https://www.facebook.com/recover/initiate/',
                    'https://www.facebook.com/recover/code/send/'
                ]
                
                sms_sent = False
                for endpoint in endpoints:
                    try:
                        send_response = session.post(
                            endpoint,
                            data=sms_payload,
                            headers=headers,
                            cookies=session.cookies.get_dict(),
                            timeout=30,
                            allow_redirects=True
                        )
                        
                        # Check response
                        response_text = send_response.text.lower()
                        
                        # Success indicators
                        success_indicators = [
                            'code sent',
                            'enter code',
                            'confirmation code',
                            'verification code',
                            'sent to your phone',
                            'check your phone',
                            'recover/code',
                            'security code'
                        ]
                        
                        # Check URL
                        current_url = send_response.url.lower()
                        
                        if any(indicator in response_text for indicator in success_indicators) or 'code' in current_url:
                            stats['success'] += 1
                            print(f"{Fore.GREEN}[✓] {any_number} : OTP Sent Successfully!")
                            
                            # Save to success file
                            try:
                                with open(success_file, 'a', encoding='utf-8') as f:
                                    f.write(f"{any_number}\n")
                            except:
                                # Try alternative location
                                alt_file = '/sdcard/success_sent.txt' if success_file != '/sdcard/success_sent.txt' else 'success_sent.txt'
                                with open(alt_file, 'a', encoding='utf-8') as f:
                                    f.write(f"{any_number}\n")
                            
                            sms_sent = True
                            break
                            
                    except Exception as endpoint_error:
                        continue
                
                if not sms_sent:
                    # If no endpoint worked, check if we got any response
                    stats['error'] += 1
                    print(f"{Fore.YELLOW}[!] {any_number} : SMS Send Failed")
            
            except Exception as send_error:
                stats['error'] += 1
                print(f"{Fore.MAGENTA}[?] {any_number} : Send Error - {str(send_error)[:50]}")
        
        else:
            stats['no_sms'] += 1
            print(f"{Fore.YELLOW}[!] {any_number} : No SMS Recovery Option Available")
            
            # Debug: Save response for analysis
            debug_filename = f"/sdcard/debug_{any_number}.html"
            try:
                with open(debug_filename, 'w', encoding='utf-8') as f:
                    f.write(search_response.text)
                print(f"{Fore.CYAN}[~] Debug info saved to: {debug_filename}")
            except:
                pass
    
    except requests.exceptions.Timeout:
        stats['error'] += 1
        print(f"{Fore.MAGENTA}[?] {any_number} : Timeout Error")
    except requests.exceptions.ConnectionError:
        stats['error'] += 1
        print(f"{Fore.MAGENTA}[?] {any_number} : Connection Error")
    except Exception as e:
        stats['error'] += 1
        print(f"{Fore.MAGENTA}[?] {any_number} : Error - {str(e)[:50]}")

def main():
    banner()
    
    # Get file paths
    file_paths = get_file_paths()
    
    # Load numbers
    print(f"\n{Fore.CYAN}Loading files...")
    numbers, numbers_file = load_numbers(file_paths['numbers'])
    
    if not numbers:
        print(f"{Fore.RED}No numbers found! Please create {file_paths['numbers']}")
        print(f"{Fore.YELLOW}File format: One phone number per line")
        print(f"{Fore.YELLOW}Example:")
        print(f"{Fore.WHITE}01826420296")
        print(f"{Fore.WHITE}+8801826420296")
        print(f"{Fore.WHITE}8801826420296")
        return
    
    stats['total'] = len(numbers)
    
    # Get thread count
    try:
        t_count = int(input(f"\n{Fore.WHITE}Enter Threads (1-50, recommended 5-15): "))
        t_count = max(1, min(50, t_count))
    except ValueError:
        t_count = 5
        print(f"{Fore.YELLOW}Using default: 5 threads")
    
    # User agent selection
    print(f"\n{Fore.CYAN}Select User Agent:")
    print(f"{Fore.WHITE}1. Android Mobile (Default)")
    print(f"{Fore.WHITE}2. iPhone")
    print(f"{Fore.WHITE}3. Desktop Chrome")
    ua_choice = input(f"{Fore.WHITE}Select (1/2/3): ").strip()
    
    if ua_choice == '2':
        ua = "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1"
    elif ua_choice == '3':
        ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    else:
        ua = "Mozilla/5.0 (Linux; Android 13; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36"
    
    print(f"\n{Fore.GREEN}Starting Automation...")
    print(f"{Fore.CYAN}{'='*60}")
    print(f"{Fore.WHITE}Numbers: {len(numbers)}")
    print(f"{Fore.WHITE}Threads: {t_count}")
    print(f"{Fore.WHITE}Success file: {file_paths['success']}")
    print(f"{Fore.YELLOW}⚠ Note: Running without proxies. Be careful with rate limiting!")
    print(f"{Fore.CYAN}{'='*60}")
    
    time.sleep(2)
    
    # Process numbers
    with ThreadPoolExecutor(max_workers=t_count) as executor:
        for num in numbers:
            executor.submit(process_number, num, ua, file_paths['success'])
            time.sleep(1)  # Increased delay to avoid rate limiting
    
    # Final report
    banner()
    print(f"{Fore.GREEN}{Style.BRIGHT}   WORK COMPLETED SUCCESSFULLY!")
    print(f"{Fore.CYAN}{'='*60}")
    print(f"{Fore.WHITE}Final Report:")
    print(f"{Fore.GREEN}Success: {stats['success']}")
    print(f"{Fore.RED}No Account: {stats['no_id']}")
    print(f"{Fore.YELLOW}No SMS Option: {stats['no_sms']}")
    print(f"{Fore.MAGENTA}Errors: {stats['error']}")
    print(f"{Fore.CYAN}Total Processed: {stats['total']}")
    print(f"{Fore.CYAN}{'='*60}")
    
    if stats['success'] > 0:
        print(f"{Fore.GREEN}✓ Success numbers saved to: {file_paths['success']}")
    
    # Ask if user wants to continue
    cont = input(f"\n{Fore.YELLOW}Process more numbers? (y/n): ").strip().lower()
    if cont == 'y':
        stats['total'] = stats['success'] = stats['no_id'] = stats['no_sms'] = stats['error'] = 0
        main()

def check_requirements():
    """Check if required modules are installed"""
    try:
        import requests
        import colorama
        print(f"{Fore.GREEN}✓ All requirements are installed")
        return True
    except ImportError as e:
        print(f"{Fore.RED}✗ Missing module: {e.name}")
        print(f"{Fore.YELLOW}Install with: pip install {e.name}")
        return False

if __name__ == "__main__":
    try:
        if check_requirements():
            main()
        else:
            print(f"{Fore.RED}Please install missing modules and try again.")
            input(f"{Fore.YELLOW}Press Enter to exit...")
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}Program interrupted by user.")
        print(f"{Fore.CYAN}Final stats:")
        print(f"{Fore.WHITE}Success: {stats['success']} | Failed: {stats['no_id'] + stats['no_sms'] + stats['error']}")
    except Exception as e:
        print(f"{Fore.RED}Unexpected error: {e}")
        input(f"{Fore.YELLOW}Press Enter to exit...")
