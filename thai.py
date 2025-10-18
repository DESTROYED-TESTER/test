
"""
SIMPLE FACEBOOK LOGIN EXAMPLE
==============================

This is the simplest way to use the Facebook login script.
Just replace the email and password with your credentials.
"""

from facebook_login import FacebookLogin

# ============================================
# STEP 1: Set your credentials
# ============================================
EMAIL = "100058660152667"      # Replace with your email or phone number
PASSWORD = "964119"        # Replace with your password

# ============================================
# STEP 2: Create login instance and login
# ============================================
fb_login = FacebookLogin()
result = fb_login.login(EMAIL, PASSWORD)

# ============================================
# STEP 3: Check if login was successful
# ============================================
if result:
    print("\
" + "="*60)
    print("\u2713 LOGIN SUCCESSFUL!")
    print("="*60)
    print(f"User ID: {result.get('user_id')}")
    print(f"Session Token: {result.get('session_token')}")
    print(f"DATR Cookie: {result.get('datr')}")
    print("="*60)
else:
    print("\
" + "="*60)
    print("\u2717 LOGIN FAILED!")
    print("="*60)
    print("Please check:")
    print("  1. Your email/password is correct")
    print("  2. Your account doesn't require 2FA")
    print("  3. Your account is not blocked")
    print("  4. You have internet connection")
    print("="*60)
