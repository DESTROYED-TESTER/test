import os
import json
import time
import csv
import requests
from datetime import datetime
from typing import Dict, List, Tuple
import pickle
from pathlib import Path
import random
from fake_useragent import UserAgent

class InstagramChecker:
    def __init__(self, input_file: str = "accounts.txt"):
        """
        Initialize Instagram checker with input file
        Format in accounts.txt: number|password|cookie
        """
        self.input_file = input_file
        self.session = requests.Session()
        self.ua = UserAgent()
        self.session.headers.update({
            'User-Agent': self.ua.random,
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Host': 'www.instagram.com',
            'Origin': 'https://www.instagram.com',
            'Referer': 'https://www.instagram.com/',
            'X-Requested-With': 'XMLHttpRequest'
        })
        
    def read_accounts(self) -> List[Dict]:
        """Read accounts from text file"""
        accounts = []
        if not os.path.exists(self.input_file):
            print(f"File {self.input_file} not found!")
            return accounts
            
        with open(self.input_file, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, 1):
                line = line.strip()
                if line and not line.startswith('#'):
                    parts = line.split('|')
                    if len(parts) >= 3:
                        account = {
                            'number': parts[0].strip(),
                            'password': parts[1].strip(),
                            'cookie': parts[2].strip(),
                            'line_number': line_num
                        }
                        accounts.append(account)
                    else:
                        print(f"Invalid format at line {line_num}: {line}")
        return accounts
    
    def parse_cookie_string(self, cookie_str: str) -> Dict:
        """Parse cookie string into dictionary"""
        cookies = {}
        for item in cookie_str.split(';'):
            item = item.strip()
            if '=' in item:
                key, value = item.split('=', 1)
                cookies[key] = value
        return cookies
    
    def login_with_cookie(self, account: Dict) -> Tuple[bool, str]:
        """Login to Instagram using cookie"""
        try:
            # Parse cookies
            cookies = self.parse_cookie_string(account['cookie'])
            
            # Update session with cookies
            self.session.cookies.update(cookies)
            
            # Test if login is valid by accessing profile page
            response = self.session.get(
                'https://www.instagram.com/api/v1/users/web_profile_info/',
                headers={
                    'X-IG-App-ID': '936619743392459',  # Instagram web app ID
                },
                timeout=10
            )
            
            if response.status_code == 200:
                data = response.json()
                username = data.get('data', {}).get('user', {}).get('username', 'Unknown')
                return True, f"Login successful! Username: {username}"
            else:
                return False, f"Login failed with status code: {response.status_code}"
                
        except requests.exceptions.RequestException as e:
            return False, f"Request error: {str(e)}"
        except json.JSONDecodeError:
            return False, "Invalid JSON response"
        except Exception as e:
            return False, f"Unexpected error: {str(e)}"
    
    def get_followers_following(self, account: Dict) -> Dict:
        """Get followers and following counts"""
        try:
            # Get user info
            response = self.session.get(
                'https://www.instagram.com/api/v1/users/web_profile_info/',
                headers={
                    'X-IG-App-ID': '936619743392459',
                },
                timeout=10
            )
            
            if response.status_code == 200:
                data = response.json()
                user_data = data.get('data', {}).get('user', {})
                
                followers = user_data.get('edge_followed_by', {}).get('count', 0)
                following = user_data.get('edge_follow', {}).get('count', 0)
                
                return {
                    'success': True,
                    'followers': followers,
                    'following': following,
                    'username': user_data.get('username', 'Unknown'),
                    'full_name': user_data.get('full_name', ''),
                    'is_private': user_data.get('is_private', False),
                    'is_verified': user_data.get('is_verified', False)
                }
            else:
                return {
                    'success': False,
                    'error': f"Failed to get data: {response.status_code}"
                }
                
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
    
    def save_results(self, results: List[Dict], filename: str = "results.csv"):
        """Save results to CSV file"""
        try:
            with open(filename, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                # Write header
                writer.writerow([
                    'Line', 'Number', 'Login Status', 'Message', 
                    'Username', 'Followers', 'Following', 
                    'Private', 'Verified', 'Full Name', 'Timestamp'
                ])
                
                # Write data
                for result in results:
                    writer.writerow([
                        result['line_number'],
                        result['number'],
                        result['login_status'],
                        result['message'],
                        result.get('username', 'N/A'),
                        result.get('followers', 'N/A'),
                        result.get('following', 'N/A'),
                        result.get('is_private', 'N/A'),
                        result.get('is_verified', 'N/A'),
                        result.get('full_name', 'N/A'),
                        result.get('timestamp', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                    ])
            print(f"Results saved to {filename}")
            
        except Exception as e:
            print(f"Error saving results: {e}")
    
    def save_valid_accounts(self, results: List[Dict], filename: str = "valid_accounts.txt"):
        """Save valid accounts to text file"""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                for result in results:
                    if result['login_status'] == 'SUCCESS':
                        f.write(f"{result['number']}|{result.get('password', 'N/A')}|"
                               f"Username: {result.get('username', 'N/A')}|"
                               f"Followers: {result.get('followers', 'N/A')}|"
                               f"Following: {result.get('following', 'N/A')}\n")
            print(f"Valid accounts saved to {filename}")
            
        except Exception as e:
            print(f"Error saving valid accounts: {e}")
    
    def run_check(self, delay: float = 2.0):
        """Main function to check all accounts"""
        print("=" * 60)
        print("Instagram Account Checker")
        print("=" * 60)
        
        # Read accounts
        accounts = self.read_accounts()
        if not accounts:
            print("No accounts found to check.")
            return
        
        print(f"Found {len(accounts)} accounts to check")
        print("-" * 60)
        
        results = []
        
        for i, account in enumerate(accounts, 1):
            print(f"\n[{i}/{len(accounts)}] Checking account: {account['number']}")
            
            # Random delay to avoid rate limiting
            if i > 1:
                time.sleep(delay + random.uniform(1, 3))
            
            # Try login
            login_success, login_message = self.login_with_cookie(account)
            
            result = {
                'line_number': account['line_number'],
                'number': account['number'],
                'password': account['password'],
                'login_status': 'SUCCESS' if login_success else 'FAILED',
                'message': login_message,
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
            
            if login_success:
                print(f"  ✓ {login_message}")
                
                # Get followers/following data
                print("  Fetching followers/following data...")
                time.sleep(1)
                
                stats = self.get_followers_following(account)
                if stats['success']:
                    result.update({
                        'username': stats['username'],
                        'followers': stats['followers'],
                        'following': stats['following'],
                        'is_private': stats['is_private'],
                        'is_verified': stats['is_verified'],
                        'full_name': stats['full_name']
                    })
                    print(f"  Username: @{stats['username']}")
                    print(f"  Followers: {stats['followers']}")
                    print(f"  Following: {stats['following']}")
                else:
                    print(f"  ✗ Failed to get stats: {stats.get('error', 'Unknown error')}")
            else:
                print(f"  ✗ {login_message}")
            
            results.append(result)
            
            # Save intermediate results every 5 accounts
            if i % 5 == 0:
                self.save_results(results, f"results_intermediate_{i}.csv")
        
        # Save final results
        print("\n" + "=" * 60)
        print("Saving results...")
        self.save_results(results)
        self.save_valid_accounts(results)
        
        # Summary
        successful = sum(1 for r in results if r['login_status'] == 'SUCCESS')
        failed = len(results) - successful
        
        print("\n" + "=" * 60)
        print("CHECK COMPLETED")
        print("=" * 60)
        print(f"Total accounts checked: {len(results)}")
        print(f"Successful logins: {successful}")
        print(f"Failed logins: {failed}")
        print(f"Success rate: {(successful/len(results)*100):.1f}%")
        print("=" * 60)

def main():
    """Main function"""
    print("Instagram Account Checker")
    print("=" * 40)
    print("Instructions:")
    print("1. Create accounts.txt file with format: number|password|cookie")
    print("2. Each line should contain one account")
    print("3. Lines starting with # are ignored")
    print("=" * 40)
    
    # Create sample file if it doesn't exist
    if not os.path.exists("accounts.txt"):
        with open("accounts.txt", "w", encoding="utf-8") as f:
            f.write("# Format: phone_number|password|cookie\n")
            f.write("# Example:\n")
            f.write("1234567890|mypassword|cookie1=value1; cookie2=value2\n")
        print("\nCreated sample accounts.txt file. Please edit it with your accounts.")
        return
    
    # Run checker
    checker = InstagramChecker("accounts.txt")
    
    try:
        # Ask for delay between checks
        delay = input("\nEnter delay between checks in seconds (default: 2): ").strip()
        delay = float(delay) if delay else 2.0
        
        checker.run_check(delay)
        
    except KeyboardInterrupt:
        print("\n\nScript interrupted by user")
    except Exception as e:
        print(f"\nError: {e}")

if __name__ == "__main__":
    main()
