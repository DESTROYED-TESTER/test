from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import json
import re

# Your credentials
pw = "9382852655"
uid = "9382852655"

def facebook_login_selenium(uid, password):
    """
    Login to Facebook using Selenium with mobile user agent
    Returns: dict with status and cookies if successful
    """
    
    # Setup Chrome options for mobile emulation
    chrome_options = Options()
    
    # Mobile user agent matching your original script
    mobile_user_agent = 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36'
    chrome_options.add_argument(f'user-agent={mobile_user_agent}')
    
    # Additional options to avoid detection
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    
    # Headless mode (uncomment if you don't want to see the browser)
    # chrome_options.add_argument('--headless')
    
    # Initialize driver
    driver = webdriver.Chrome(options=chrome_options)
    
    # Execute script to hide webdriver property
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    
    try:
        print("🌐 Navigating to Facebook mobile login...")
        
        # Go to mobile Facebook login page
        driver.get('https://m.facebook.com/login')
        
        # Wait for page to load
        wait = WebDriverWait(driver, 15)
        
        # Find and fill email/phone field
        try:
            email_field = wait.until(EC.presence_of_element_located((By.ID, 'm_login_email')))
            email_field.clear()
            email_field.send_keys(uid)
            print(f"✅ Entered UID: {uid}")
        except TimeoutException:
            # Try alternative selector
            email_field = wait.until(EC.presence_of_element_located((By.NAME, 'email')))
            email_field.clear()
            email_field.send_keys(uid)
            print(f"✅ Entered UID: {uid}")
        
        # Find and fill password field
        try:
            password_field = driver.find_element(By.ID, 'm_login_password')
            password_field.clear()
            password_field.send_keys(password)
            print("✅ Entered password")
        except:
            password_field = driver.find_element(By.NAME, 'pass')
            password_field.clear()
            password_field.send_keys(password)
            print("✅ Entered password")
        
        # Click login button
        try:
            login_button = driver.find_element(By.NAME, 'login')
            login_button.click()
            print("🔄 Clicked login button...")
        except:
            # Try alternative login button selector
            login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
            login_button.click()
            print("🔄 Clicked login button...")
        
        # Wait for response
        time.sleep(3)
        
        # Check for various login outcomes
        current_url = driver.current_url
        print(f"📍 Current URL: {current_url}")
        
        # Check for 2FA/Checkpoint
        if 'checkpoint' in current_url:
            print("⚠️ STATUS: CHECKPOINT REQUIRED")
            print("📋 Account needs verification or 2FA")
            
            # Try to detect what type of checkpoint
            page_source = driver.page_source
            if 'Confirm your identity' in page_source or 'Security Check' in page_source:
                print("🔐 Security checkpoint - needs verification")
            elif 'Enter the code' in page_source or 'Two-factor authentication' in page_source:
                print("📱 2FA required - needs authentication code")
            elif 'Review your login' in page_source:
                print("👀 Login review required - check your notifications")
            
            # Return checkpoint info
            return {
                'status': 'checkpoint_required',
                'url': current_url,
                'cookies': {cookie['name']: cookie['value'] for cookie in driver.get_cookies()}
            }
        
        # Check if login was successful
        if 'c_user' in [cookie['name'] for cookie in driver.get_cookies()]:
            # Get all cookies
            cookies_dict = {cookie['name']: cookie['value'] for cookie in driver.get_cookies()}
            
            # Try to get user ID from cookies
            user_id = cookies_dict.get('c_user', 'Unknown')
            
            print(f"✅ LOGIN SUCCESSFUL!")
            print(f"👤 User ID: {user_id}")
            print(f"🍪 Cookies: {cookies_dict}")
            
            return {
                'status': 'success',
                'user_id': user_id,
                'cookies': cookies_dict,
                'url': current_url
            }
        
        # Check for login error messages
        page_source = driver.page_source
        
        if 'Invalid username or password' in page_source or 'incorrect password' in page_source.lower():
            print("❌ STATUS: INVALID CREDENTIALS")
            return {'status': 'error', 'reason': 'Invalid username or password'}
        
        if 'account is disabled' in page_source.lower():
            print("❌ STATUS: ACCOUNT DISABLED")
            return {'status': 'error', 'reason': 'Account disabled'}
        
        if 'too many attempts' in page_source.lower():
            print("❌ STATUS: TOO MANY ATTEMPTS")
            return {'status': 'error', 'reason': 'Too many login attempts'}
        
        # If we got here, something else happened
        print("⚠️ STATUS: UNKNOWN RESPONSE")
        print(f"📄 Page title: {driver.title}")
        print(f"🔗 Current URL: {current_url}")
        
        # Try to extract any error message
        error_elements = driver.find_elements(By.XPATH, "//*[contains(@class, 'error') or contains(@class, 'alert')]")
        if error_elements:
            print(f"⚠️ Error messages found: {[elem.text for elem in error_elements[:3]]}")
        
        return {
            'status': 'unknown',
            'url': current_url,
            'cookies': {cookie['name']: cookie['value'] for cookie in driver.get_cookies()}
        }
    
    except Exception as e:
        print(f"❌ ERROR: {str(e)}")
        return {'status': 'exception', 'error': str(e)}
    
    finally:
        # Wait a moment before closing
        time.sleep(2)
        driver.quit()

# Execute the login
print("=" * 50)
print("🔐 STARTING FACEBOOK LOGIN")
print("=" * 50)

result = facebook_login_selenium(uid, pw)

print("\n" + "=" * 50)
print("📊 RESULT SUMMARY")
print("=" * 50)
print(f"Status: {result.get('status')}")

if result.get('status') == 'success':
    print(f"User ID: {result.get('user_id')}")
    print(f"Cookies Count: {len(result.get('cookies', {}))}")
    print("\n🍪 Session Cookies:")
    for key, value in result.get('cookies', {}).items():
        print(f"  {key}: {value[:30]}..." if len(value) > 30 else f"  {key}: {value}")
    
    # Save cookies for future use
    with open('facebook_cookies.json', 'w') as f:
        json.dump(result['cookies'], f, indent=2)
    print("\n💾 Cookies saved to facebook_cookies.json")

elif result.get('status') == 'checkpoint_required':
    print("\n⚠️ Manual intervention required:")
    print("1. Check your Facebook account for verification requests")
    print("2. Complete the verification process in the browser")
    print("3. Then you can export cookies for future use")

elif result.get('status') == 'error':
    print(f"\n❌ Login failed: {result.get('reason', 'Unknown reason')}")

elif result.get('status') == 'unknown':
    print(f"\n⚠️ Unknown status. URL: {result.get('url')}")
    print("The login process may have been redirected or blocked.")

print("\n=" * 50)
