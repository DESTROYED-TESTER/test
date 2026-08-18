import os
import re
import time
import requests
import json

# Color definitions (add these if not defined elsewhere)
RED = '\033[91m'
WHITE = '\033[97m'
CYAN = '\033[96m'
BLUE = '\033[94m'
YELLOW = '\033[93m'
GREEN = '\033[92m'

# Global variables
Uuid = []
xx = 0

def find_res():
    # Placeholder function - implement as needed
    return None

def prints(text, style=""):
    print(text)

def panel(text, style=""):
    return text

def MetodeType():
    # Placeholder function - implement as needed
    pass

def Aset_Ig():
    os.system('clear')
    coki = {}
    if os.path.isfile('data/cookie.txt'):
        cookie_str = open('data/cookie.txt', 'r').read().strip()
        if cookie_str:
            coki = {'cookie': cookie_str}
    if not coki:
        print(f"{RED}[{WHITE}+{RED}] {CYAN}Please enter your instagram account cookie. Make sure to use a throwaway account!")
        cookie_input = input(f"\n{RED}[{WHITE}+{RED}] {BLUE}Cookie :{YELLOW} ").strip()
        if cookie_input.lower() == 'res':
            cookie_str = find_res()
            if not cookie_str:
                print(f"{RED}Failed to load backup cookie, please enter manually.")
                cookie_input = input(f"\n{RED}[{WHITE}+{RED}] {BLUE}Cookie :{YELLOW} ").strip()
                coki = {'cookie': cookie_input}
            else:
                coki = {'cookie': cookie_str}
        else:
            coki = {'cookie': cookie_input}
    
    try:
        uid = re.search('ds_user_id=(\d+)', str(coki['cookie'])).group(1)
        ua = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
        resp = requests.get(f'https://i.instagram.com/api/v1/users/{uid}/info/', headers=ua, cookies=coki)
        resp.raise_for_status()
        user_data = resp.json().get('user', {})
        full_name = user_data.get('full_name', 'Name Unknown')
        follower_count = user_data.get('follower_count', 0)
        open('data/cookie.txt', 'w').write(coki['cookie'])
        return coki, full_name, follower_count
    except Exception as e:
        print(f"{RED}Invalid cookies or error: {e}")
        os.system('rm -rf data/cookie.txt')
        time.sleep(2)
        return Aset_Ig()

def dumps(cintil, typess):
    global Uuid, xx
    Uuid = []  # Reset Uuid for new dump
    xx = 0
    
    xyz = []
    if 'csrftoken' not in str(cintil):
        try:
            memek = requests.get('https://www.instagram.com/data/shared_data/', cookies=cintil).json()
            token = memek['config']['csrf_token']
            cintil['cookie'] += ';csrftoken=%s;' % token
        except Exception as e:
            os.system('rm -rf data/cookie.txt')
            exit(f'\n{WHITE}[{YELLOW}!{WHITE}] Csrftoken not available, dump will not run: {e}')
    
    prints(panel(f"\n{CYAN}Enter instagram usernames, use commas for mass cracking", style="Purple"))
    users = input(f"{RED}[{WHITE}+{RED}] {BLUE}Username :{YELLOW} ").split(',')
    
    try:
        for y in users:
            y = y.strip()
            if not y:  # Skip empty usernames
                continue
            req = requests.get(f'https://www.instagram.com/{y}/', cookies=cintil).text
            uid = re.search('"user_id":"(\\d+)"', str(req))
            if uid:
                uid = uid.group(1)
                if uid not in xyz:
                    xyz.append(uid)
    except Exception as e:
        print(f"{RED}Error fetching user IDs: {e}")
        pass
    
    # Process each user ID
    for kintil in xyz:
        if typess:
            Graphql(True, kintil, cintil['cookie'], '')
        else:
            Graphql(False, kintil, cintil['cookie'], '')
    
    # Save the collected data to file
    if Uuid:
        try:
            # Create data directory if it doesn't exist
            os.makedirs('data', exist_ok=True)
            
            # Save with username|name format
            with open('data/dump.txt', 'w') as f:
                for item in Uuid:
                    f.write(item + '\n')
            
            print(f"\n{GREEN}✓ Successfully saved {len(Uuid)} entries to data/dump.txt")
            print(f"{GREEN}File format: username|name")
        except Exception as e:
            print(f"{RED}Error saving dump file: {e}")
    else:
        print(f"\n{RED}No data collected. Check if the users exist or are public.")
    
    print("")
    MetodeType()

def Graphql(typess, userid, cokie, after):
    global Uuid, xx
    
    api = "https://www.instagram.com/graphql/query/"
    csr = 'variables={"id":"%s","first":24,"after":"%s"}' % (userid, after)
    
    # Use correct query hashes
    if typess:  # followers
        mek = "query_hash=37479f2b8209594dde7facb0d904896a&{}".format(csr)
    else:  # following
        mek = "query_hash=58712303d941c6855d4e888c5f0cd22f&{}".format(csr)
    
    try:
        ptk = {
            "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 18_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 instagram 360.0.0.33.104",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "cookie": cokie
        }
        req = requests.get(api, params=mek, headers=ptk).json()
        
        # Check for login requirement
        if 'require_login' in req:
            if len(Uuid) == 0:
                print(f'\n{WHITE}[{YELLOW}!{WHITE}] Invalid Cookie or rate limited')
                return
        
        # Determine which edge to use
        khm = 'edge_followed_by' if typess else 'edge_follow'
        
        # Validate data structure exists
        if 'data' in req and 'user' in req['data'] and req['data']['user'] is not None:
            if khm in req['data']['user']:
                # Process each user in the response
                for xyz in req['data']['user'][khm]['edges']:
                    username = xyz['node']['username']
                    full_name = xyz['node'].get('full_name', 'Unknown')
                    # Format: username|name
                    xy = f"{username}|{full_name}"
                    if xy not in Uuid:
                        xx += 1
                        Uuid.append(xy)
                        # Fixed print with proper formatting
                        print(f'\r{WHITE}Collecting Uid {RED}{len(Uuid)}{WHITE}                            ', end='', flush=True)
                        time.sleep(0.0009)
                
                # Check for next page
                end = req['data']['user'][khm]['page_info']['has_next_page']
                if end:
                    after = req['data']['user'][khm]['page_info']['end_cursor']
                    Graphql(typess, userid, cokie, after)
            else:
                print(f"\n{YELLOW}User may be private or has no {khm}")
        else:
            print(f"\n{YELLOW}No data found for user ID: {userid}")
            
    except Exception as e:
        # Silent fail for individual users, but allow the loop to continue
        pass

# Example usage
if __name__ == "__main__":
    try:
        # Set up cookies
        coki, full_name, follower_count = Aset_Ig()
        
        # Dump followers (True) or following (False)
        dumps(coki, True)  # True for followers, False for following
    except KeyboardInterrupt:
        print(f"\n{YELLOW}Operation cancelled by user")
    except Exception as e:
        print(f"{RED}Error: {e}")
