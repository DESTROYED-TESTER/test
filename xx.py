import requests
import time
from urllib.parse import urlparse, parse_qs
import json

class FacebookRecovery:
    def __init__(self):
        self.session = requests.Session()
        self.base_headers = {
            'authority': 'www.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'no-cache',
            'pragma': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',
        }
        
    def update_cookies(self, cookies_dict):
        """Update session cookies"""
        self.session.cookies.update(cookies_dict)
        
    def check_phone_number_status(self, phone_number):
        """Check if phone number can receive SMS"""
        # This is a placeholder - actual implementation would require
        # calling Facebook's verification endpoints
        print(f"Checking phone: {phone_number}")
        print("Note: Facebook might not send SMS if:")
        print("1. Number isn't verified on Facebook")
        print("2. Number is VoIP/Virtual")
        print("3. SMS delivery is delayed by carrier")
        print("4. Facebook's SMS service is having issues")
        
    def send_recovery_request(self, recovery_url, max_retries=2):
        """Send recovery request with retry logic"""
        
        for attempt in range(max_retries):
            print(f"\n{'='*50}")
            print(f"Attempt {attempt + 1}/{max_retries}")
            
            try:
                # Add delay between attempts
                if attempt > 0:
                    wait_time = 30 * attempt  # 30, 60 seconds
                    print(f"Waiting {wait_time} seconds before retry...")
                    time.sleep(wait_time)
                
                response = self.session.get(
                    recovery_url,
                    headers=self.base_headers,
                    timeout=30
                )
                
                print(f"Status: {response.status_code}")
                print(f"URL: {response.url}")
                
                # Save response for debugging
                with open(f"debug_response_{attempt}.html", "w", encoding="utf-8") as f:
                    f.write(response.text[:5000])  # Save first 5000 chars
                
                # Check for specific issues
                issues = self.analyze_response(response)
                
                if issues:
                    print("\n⚠ Issues detected:")
                    for issue in issues:
                        print(f"  - {issue}")
                    
                    if "rate limit" in str(issues).lower():
                        print("🔄 Rate limited. Need to wait longer or get new cookies.")
                        continue
                        
                # Check if we need to handle any forms or additional steps
                if self.check_for_form(response):
                    print("📋 Additional form/page detected")
                    # You might need to submit additional information
                    
                if response.status_code == 200 and "code" in response.text.lower():
                    print("\n✅ Recovery page loaded successfully")
                    print("📱 SMS should be sent to your phone")
                    
                    # Try alternative method if SMS doesn't arrive
                    if attempt == max_retries - 1:
                        self.suggest_alternatives()
                    
                    return True
                    
            except Exception as e:
                print(f"❌ Error on attempt {attempt + 1}: {str(e)}")
                
        return False
    
    def analyze_response(self, response):
        """Analyze response for known issues"""
        text = response.text.lower()
        issues = []
        
        check_patterns = [
            ("too many attempts", "Rate limiting detected"),
            ("temporarily blocked", "Number/IP might be blocked"),
            ("invalid phone number", "Phone number format issue"),
            ("cannot use this feature", "Feature restricted"),
            ("try another way", "SMS not available for this number"),
            ("carrier restrictions", "Mobile carrier blocking Facebook SMS"),
            ("unable to send", "Facebook SMS service issue"),
        ]
        
        for pattern, message in check_patterns:
            if pattern in text:
                issues.append(f"{message} (found: '{pattern}')")
                
        # Check for error codes in URL
        parsed_url = urlparse(response.url)
        query_params = parse_qs(parsed_url.query)
        
        if 'error' in query_params:
            issues.append(f"Error in URL parameters: {query_params['error']}")
            
        return issues
    
    def check_for_form(self, response):
        """Check if response contains forms that need submission"""
        text = response.text.lower()
        form_indicators = [
            "form",
            "input",
            "submit",
            "captcha",
            "security check"
        ]
        
        for indicator in form_indicators:
            if indicator in text:
                return True
        return False
    
    def suggest_alternatives(self):
        """Suggest alternative recovery methods"""
        print("\n" + "="*50)
        print("ALTERNATIVES TO TRY:")
        print("="*50)
        print("1. Try email recovery instead of SMS")
        print("2. Use 'Trusted Contacts' recovery if set up")
        print("3. Try from a different device/network")
        print("4. Wait 24 hours and try again")
        print("5. Contact Facebook Support")
        print("6. Use mobile app for recovery")
        print("7. Check spam folder for SMS")
        print("8. Ensure phone has signal and can receive SMS")
        
    def try_email_recovery(self, email):
        """Alternative: Try email recovery"""
        print(f"\nTrying email recovery for: {email}")
        # You would need the email recovery URL here
        # Similar structure to SMS recovery but with email parameter
        
    def verify_sms_delivery(self):
        """Suggest ways to verify SMS is being sent"""
        print("\n" + "="*50)
        print("SMS DELIVERY TROUBLESHOOTING:")
        print("="*50)
        print("1. Check phone signal and carrier")
        print("2. Ensure no SMS filtering apps are blocking Facebook")
        print("3. Try turning phone off/on")
        print("4. Test SMS reception with another service")
        print("5. Check if number can receive international SMS")
        print("6. Contact mobile carrier about SMS blocking")

# Usage
def main():
    # Your data
    cookies = {
        'datr': 'Eitnac9Jr55lMaaETcsXwk3D',
        'sb': 'EitnaZzbPfbccAsuj6eJIYfE',
        'fr': '0DBxBjQV9WtPFwBoS..BpZysS..AAA.0.0.BpZyux.AWdI9d7fUqkKfXfIiHoCaksZnFM',
        'ps_l': '1',
        'ps_n': '1',
        'sfiu': 'AYgxaHatHEl-032fJR1oikeYk4Fdy6TaDFbWWnNMlvMK-X0IAJVhHRyjoHef7Gty8TkiAgWVenEEEvx9YgL-xjzsQQi-06fwdxVoLC8Wbtxqg54dzGTuc27nfsU-FII0JryPspXZmlZqauacziW5GrM08DIg84QLYA6rHoHvqbA4-4FyRS162Aocga61gvjihvc8KL2tg_4CjT_1UME1dR2b1c6sPLJdK3VbpqnKACIMUQ',
        'wd': '885x773',
    }
    
    recovery_url = 'https://www.facebook.com/recover/code/?ph[0]=%2B918101729293&rm=send_sms&cuid=AYghRTMq79g5bK4BaxmW3aXnGG7RDEotWd0UvhGo9pJSAOc4nnDkQ2xs1xSZG5Y5efgONAo--BrLTPgGtMru_ywWEWvKBsA9WxZ6ud_AzdbwApMJVFsTW4J4v3xUG7yK9lVRbwdDb0kgTIgp5iQrn8N8XwjZZ9sLh_fdV3s-snrpRILJWjKlMPR1glamygeVK7pTeJ2HaFUZJmNw6ZgCOOvjqN7E_YCqXHKvqSjR2jkIWQ&hash=AUbElx_iXHc74Px-v2M'
    
    # Initialize and run
    fb_recovery = FacebookRecovery()
    fb_recovery.update_cookies(cookies)
    
    print("Starting Facebook SMS Recovery...")
    
    # Check phone number
    fb_recovery.check_phone_number_status("+918101729293")
    
    # Send recovery request
    success = fb_recovery.send_recovery_request(recovery_url)
    
    if success:
        print("\n✅ Request completed. Check your phone for SMS.")
        print("\nIf SMS doesn't arrive within 5 minutes:")
        fb_recovery.suggest_alternatives()
    else:
        print("\n❌ Failed to complete recovery request.")
        fb_recovery.verify_sms_delivery()

if __name__ == "__main__":
    main()
