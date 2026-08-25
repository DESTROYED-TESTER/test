import requests

# Your curl request converted to Python
response = requests.post(
    'https://www.messenger.com/login/password/',
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:154.0) Gecko/20100101 Firefox/154.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.9',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://www.messenger.com',
        'Referer': 'https://www.messenger.com/',
        # ... other headers
    },
    cookies={
        'datr': 'DTiNaqX1AXorpHDezRNgATu3',
        'wd': '1440x459',
        'sb': 'ITiNam5PFZlCIwvurO_AST3s'
    },
    data={
        'jazoest': '22573',
        'lsd': 'AdRgt4koDfzsyLx4lemq3YoEQrs',
        # ... other form data
    }
)

# Check for login issues
if "checkpoint" in response.text.lower() or "login_approval" in response.text.lower():
    print("⚠️ Additional verification required (checkpoint or login approval)")
    # Handle checkpoint/approval flow
elif "success" in response.text.lower() or response.status_code == 200:
    print("✅ Login successful")
    
    # Extract session cookies
    session_cookies = response.cookies.get_dict()
    print(f"Session cookies: {session_cookies}")
    
    # Important session cookies for Messenger
    important_cookies = {
        'c_user': session_cookies.get('c_user'),      # User ID
        'xs': session_cookies.get('xs'),              # Session token
        'fr': session_cookies.get('fr'),              # Facebook session
        'sb': session_cookies.get('sb'),              # Browser session
        'datr': session_cookies.get('datr'),          # Security cookie
    }
    print(f"Auth cookies: {important_cookies}")
