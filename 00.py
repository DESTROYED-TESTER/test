#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Instagram Cookie Tester - Fixed Version
"""

import requests
import json
import re
import time
import sys

# Color codes for terminal output
GREEN = "\033[1;92m"
RED = "\033[1;91m"
YELLOW = "\033[1;93m"
WHITE = "\033[1;97m"
CYAN = "\033[1;96m"
RESET = "\033[0m"

# User agent for requests
ua = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 instagram 360.0.0.33.104 (iPhone16,2; iOS 18.2; en_US; en; scale=3.00; 1170x2532; 510000000)'
}

def test_cookies(coki):
    """Test if cookies are still valid using multiple methods"""
    
    # Ensure coki is properly formatted
    if isinstance(coki, str):
        coki = {'cookie': coki}
    elif isinstance(coki, dict) and 'cookie' not in coki:
        # If coki is a dict without 'cookie' key, assume it's already in cookie format
        pass
    
    print(f"{YELLOW}Testing cookies...{RESET}")
    
    # Method 1: Try to get user info using the API
    try:
        cookie_str = coki.get('cookie', '') if isinstance(coki, dict) else str(coki)
        uid_match = re.search(r'ds_user_id=(\d+)', cookie_str)
        
        if uid_match:
            uid = uid_match.group(1)
            print(f"{WHITE}Found user ID: {CYAN}{uid}{RESET}")
            
            # Prepare cookies for requests
            if isinstance(coki, dict):
                cookies = coki
            else:
                cookies = {'cookie': coki}
            
            response = requests.get(
                f'https://i.instagram.com/api/v1/users/{uid}/info/',
                headers=ua,
                cookies=cookies,
                timeout=10
            )
            
            if response.status_code == 200:
                try:
                    data = response.json()
                    if 'user' in data and data['user'].get('username'):
                        print(f"{GREEN}✓ Cookies are valid!{RESET}")
                        print(f"{WHITE}  Username: {CYAN}{data['user'].get('username')}{RESET}")
                        print(f"{WHITE}  Full Name: {CYAN}{data['user'].get('full_name', 'N/A')}{RESET}")
                        print(f"{WHITE}  Followers: {CYAN}{data['user'].get('follower_count', 0)}{RESET}")
                        return True
                except json.JSONDecodeError:
                    pass
    except Exception as e:
        pass
    
    # Method 2: Try to access the login ajax endpoint
    try:
        test_session = requests.Session()
        test_session.max_redirects = 3
        
        if isinstance(coki, dict):
            cookies = coki
        else:
            cookies = {'cookie': coki}
        
        response = test_session.get(
            'https://www.instagram.com/api/v1/web/accounts/login/ajax/',
            cookies=cookies,
            timeout=10,
            allow_redirects=False
        )
        
        if response.status_code == 200:
            try:
                data = response.json()
                if 'authenticated' in data:
                    print(f"{GREEN}✓ Cookies are valid!{RESET}")
                    return True
            except:
                print(f"{GREEN}✓ Cookies are valid!{RESET}")
                return True
        elif response.status_code in [302, 401]:
            print(f"{RED}✗ Cookies may be expired! (Status: {response.status_code}){RESET}")
            return False
    except Exception as e:
        pass
    
    # Method 3: Try to get the user's profile page
    try:
        test_session = requests.Session()
        test_session.max_redirects = 3
        
        if isinstance(coki, dict):
            cookies = coki
        else:
            cookies = {'cookie': coki}
        
        response = test_session.get(
            'https://www.instagram.com/',
            cookies=cookies,
            timeout=10,
            allow_redirects=False
        )
        
        if response.status_code == 200:
            # Check if we got a login page or actual content
            if 'login' not in response.text.lower():
                print(f"{GREEN}✓ Cookies are valid!{RESET}")
                return True
            else:
                print(f"{RED}✗ Cookies may be expired! (Redirected to login){RESET}")
                return False
    except Exception as e:
        pass
    
    # Method 4: Try to get csrf token from shared_data
    try:
        if isinstance(coki, dict):
            cookies = coki
        else:
            cookies = {'cookie': coki}
            
        response = requests.get(
            'https://www.instagram.com/data/shared_data/',
            cookies=cookies,
            timeout=10
        )
        if response.status_code == 200:
            try:
                data = response.json()
                if 'config' in data and 'csrf_token' in data['config']:
                    print(f"{GREEN}✓ Cookies are valid!{RESET}")
                    return True
            except:
                pass
    except Exception as e:
        pass
    
    # Method 5: Try to access a random profile page
    try:
        test_session = requests.Session()
        test_session.max_redirects = 3
        
        if isinstance(coki, dict):
            cookies = coki
        else:
            cookies = {'cookie': coki}
        
        # Try accessing a well-known profile
        response = test_session.get(
            'https://www.instagram.com/instagram/',
            cookies=cookies,
            timeout=10,
            allow_redirects=False
        )
        
        if response.status_code == 200 and 'instagram' in response.text.lower():
            print(f"{GREEN}✓ Cookies are valid!{RESET}")
            return True
    except Exception as e:
        pass
    
    print(f"{RED}✗ All cookie validation methods failed. Cookies appear to be invalid.{RESET}")
    return False

def validate_cookie_format(cookie_str):
    """Validate if the cookie string has required fields"""
    required_fields = ['sessionid', 'ds_user_id']
    missing = []
    
    for field in required_fields:
        if field not in cookie_str:
            missing.append(field)
    
    if missing:
        print(f"{RED}✗ Cookie is missing: {', '.join(missing)}{RESET}")
        return False
    
    # Check if sessionid has valid format (should have numbers)
    session_match = re.search(r'sessionid=([^;]+)', cookie_str)
    if session_match:
        session_value = session_match.group(1)
        if not session_value or len(session_value) < 5:
            print(f"{RED}✗ Session ID appears invalid (too short){RESET}")
            return False
    
    # Check if ds_user_id is present and numeric
    user_match = re.search(r'ds_user_id=([^;]+)', cookie_str)
    if user_match:
        user_id = user_match.group(1)
        if not user_id.isdigit():
            print(f"{RED}✗ User ID appears invalid (not a number){RESET}")
            return False
    
    print(f"{GREEN}✓ Cookie format looks valid{RESET}")
    return True

def get_cookie_from_user():
    """Get cookie from user input with validation"""
    print(f"{YELLOW}Enter your Instagram cookie (should contain sessionid, ds_user_id, csrftoken){RESET}")
    print(f"{WHITE}Example: sessionid=abc123; ds_user_id=123456; csrftoken=xyz789{RESET}")
    
    cookie_input = input(f"{WHITE}[{GREEN}?{WHITE}] Cookie: {GREEN}").strip()
    
    if not cookie_input:
        print(f"{RED}No cookie entered!{RESET}")
        return None
    
    if not validate_cookie_format(cookie_input):
        print(f"{RED}Invalid cookie format! Please try again.{RESET}")
        return None
    
    return cookie_input

def main():
    """Main function to test cookies"""
    print(f"{CYAN}{'='*56}{RESET}")
    print(f"{CYAN}     🔍 INSTAGRAM COOKIE TESTER 🔍{RESET}")
    print(f"{CYAN}{'='*56}{RESET}")
    
    # Get cookie from user
    cookie_str = get_cookie_from_user()
    if not cookie_str:
        print(f"{RED}No valid cookie provided. Exiting...{RESET}")
        return
    
    # Test the cookie
    cookies = {'cookie': cookie_str}
    
    print(f"\n{WHITE}Testing cookie...{RESET}")
    
    if test_cookies(cookies):
        print(f"\n{GREEN}{'='*56}{RESET}")
        print(f"{GREEN}     ✅ COOKIE IS VALID!{RESET}")
        print(f"{GREEN}{'='*56}{RESET}")
        
        # Try to get user info
        try:
            uid_match = re.search(r'ds_user_id=(\d+)', cookie_str)
            if uid_match:
                uid = uid_match.group(1)
                response = requests.get(
                    f'https://i.instagram.com/api/v1/users/{uid}/info/',
                    headers=ua,
                    cookies=cookies,
                    timeout=10
                )
                if response.status_code == 200:
                    data = response.json()
                    if 'user' in data:
                        user = data['user']
                        print(f"\n{WHITE}📊 User Details:{RESET}")
                        print(f"  {WHITE}Username: {CYAN}{user.get('username', 'N/A')}{RESET}")
                        print(f"  {WHITE}Full Name: {CYAN}{user.get('full_name', 'N/A')}{RESET}")
                        print(f"  {WHITE}User ID: {CYAN}{user.get('id', 'N/A')}{RESET}")
                        print(f"  {WHITE}Followers: {CYAN}{user.get('follower_count', 0)}{RESET}")
                        print(f"  {WHITE}Following: {CYAN}{user.get('following_count', 0)}{RESET}")
                        print(f"  {WHITE}Posts: {CYAN}{user.get('media_count', 0)}{RESET}")
        except Exception as e:
            print(f"{YELLOW}Could not fetch additional user info: {e}{RESET}")
        
        # Save cookie to file
        try:
            os.makedirs('data', exist_ok=True)
            with open('data/cookie.txt', 'w') as f:
                f.write(cookie_str)
            print(f"\n{GREEN}✓ Cookie saved to data/cookie.txt{RESET}")
        except:
            pass
            
    else:
        print(f"\n{RED}{'='*56}{RESET}")
        print(f"{RED}     ❌ COOKIE IS INVALID!{RESET}")
        print(f"{RED}{'='*56}{RESET}")
        print(f"{YELLOW}Possible reasons:{RESET}")
        print(f"  • Cookie has expired")
        print(f"  • Cookie is missing required fields")
        print(f"  • Cookie format is incorrect")
        print(f"  • Account is logged out")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{YELLOW}Interrupted by user.{RESET}")
    except Exception as e:
        print(f"{RED}Error: {e}{RESET}")
