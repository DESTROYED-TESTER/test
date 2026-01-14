# facebook_send_otp.py
import requests
import time
import json
import random
import string
from datetime import datetime

class FacebookOTPSender:
    def __init__(self, phone_number="8101729293"):
        self.phone_number = phone_number
        self.full_phone = f"+91{phone_number}"
        self.session = requests.Session()
        
        # Set the exact headers from your curl command
        self.headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'dpr': '1',
            'priority': 'u=0, i',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"',
            'sec-ch-ua-full-version-list': '"Google Chrome";v="143.0.7499.170", "Chromium";v="143.0.7499.170", "Not A(Brand";v="24.0.0.0"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Windows"',
            'sec-ch-ua-platform-version': '"10.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',
            'viewport-width': '885',
        }
        
        # Cookies from your curl command
        self.cookies = {
            'datr': 'Eitnac9Jr55lMaaETcsXwk3D',
            'sb': 'EitnaZzbPfbccAsuj6eJIYfE',
            'fr': '0DBxBjQV9WtPFwBoS..BpZysS..AAA.0.0.BpZyux.AWdI9d7fUqkKfXfIiHoCaksZnFM',
            'ps_l': '1',
            'ps_n': '1',
            'sfiu': 'AYgxaHatHEl-032fJR1oikeYk4Fdy6TaDFbWWnNMlvMK-X0IAJVhHRyjoHef7Gty8TkiAgWVenEEEvx9YgL-xjzsQQi-06fwdxVoLC8Wbtxqg54dzGTuc27nfsU-FII0JryPspXZmlZqauacziW5GrM08DIg84QLYA6rHoHvqbA4-4FyRS162Aocga61gvjihvc8KL2tg_4CjT_1UME1dR2b1c6sPLJdK3VbpqnKACIMUQ',
            'wd': '885x773',
        }
        
        # Update the session cookies
        for key, value in self.cookies.items():
            self.session.cookies.set(key, value)
    
    def generate_url(self, phone):
        """Generate the Facebook recover URL based on phone number"""
        # URL components from your curl command
        base_url = "https://www.facebook.com/recover/code/"
        
        # URL parameters
        params = {
            'ph[0]': f'%2B91{phone}',  # URL encoded +91
            'rm': 'send_sms',
            'cuid': 'AYghRTMq79g5bK4BaxmW3aXnGG7RDEotWd0UvhGo9pJSAOc4nnDkQ2xs1xSZG5Y5efgONAo--BrLTPgGtMru_ywWEWvKBsA9WxZ6ud_AzdbwApMJVFsTW4J4v3xUG7yK9lVRbwdDb0kgTIgp5iQrn8N8XwjZZ9sLh_fdV3s-snrpRILJWjKlMPR1glamygeVK7pTeJ2HaFUZJmNw6ZgCOOvjqN7E_YCqXHKvqSjR2jkIWQ',
            'hash': 'AUbElx_iXHc74Px-v2M'
        }
        
        # Build URL with parameters
        from urllib.parse import urlencode
        url = f"{base_url}?{urlencode(params)}"
        return url
    
    def get_referer_url(self):
        """Get the referer URL from your curl command"""
        return 'https://www.facebook.com/sms/captcha/?next=%2Fajax%2Frecover%2Finitiate%2F%3Fcuid%3DAYgUDz3EM1R8G3A82SfE_5N4B5g-9vdqTMe4VkWvpcPjmAIhFdbzMy0DJqr9RSoaxJblxtgnCJ51Ov46x0CWHzIphkpWvzrVp_lQEUSB4fB7Cx9aDmrLbUaXZKVt2s7b6qGKsByiRLBOaWiu-lJ6ObznCu9NKJdBpL6xv7JozImJxoT74VZtMiPypCJjcXBpk22W6xkX3dT1coJ4ONID_GwNBuOhNPSTJGJ7IrcoBpwC0w%26recover_method%3Dsend_sms%253AAYihGClGR3w9iNQRqYG045XxqnmaeHGaylRfHeOX33W1WzyNq3XlAbmobRuApsAkYwyNIOf_D7wzys0VtXEENjbrlP5Ciy8m5f6NDfZ_hAS3VBfrvOrDFe0j_-jVNgBf9_0%26lara%3D0&next_mac=AdDI9pZ5wvbC6EKg543H3pIh92QvC8sALvJjt7G-qWmrUHN5'
    
    def send_otp_request(self):
        """Send the OTP request to Facebook"""
        print(f"\n{'='*60}")
        print("SENDING OTP REQUEST TO FACEBOOK")
        print(f"{'='*60}")
        print(f"📱 Phone: {self.full_phone}")
        print(f"⏰ Time: {datetime.now().strftime('%H:%M:%S')}")
        
        # Generate the URL
        url = self.generate_url(self.phone_number)
        print(f"\n🌐 URL: {url[:80]}...")
        
        # Add referer to headers
        headers_with_referer = self.headers.copy()
        headers_with_referer['referer'] = self.get_referer_url()
        
        try:
            print("\n📤 Sending request to Facebook...")
            response = self.session.get(
                url,
                headers=headers_with_referer,
                timeout=30
            )
            
            print(f"\n📥 Response Status: {response.status_code}")
            print(f"📥 Response Length: {len(response.text)} characters")
            
            # Check response
            if response.status_code == 200:
                # Check if OTP was sent successfully
                response_text = response.text.lower()
                
                if "code sent" in response_text or "text message" in response_text:
                    print("\n✅ SUCCESS: OTP sent via SMS!")
                    self.display_success_message()
                    return True, "OTP sent successfully"
                elif "enter confirmation code" in response_text:
                    print("\n✅ SUCCESS: Ready for OTP entry!")
                    return True, "Ready for OTP entry"
                else:
                    print("\n⚠️  Response received, but OTP status unclear")
                    self.save_response_debug(response)
                    return False, "Unknown response"
            else:
                print(f"\n❌ ERROR: HTTP {response.status_code}")
                self.save_response_debug(response)
                return False, f"HTTP {response.status_code}"
                
        except requests.RequestException as e:
            print(f"\n❌ NETWORK ERROR: {str(e)}")
            return False, str(e)
    
    def save_response_debug(self, response):
        """Save response for debugging"""
        filename = f"facebook_response_{int(time.time())}.html"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(response.text)
        print(f"💾 Debug saved to: {filename}")
    
    def display_success_message(self):
        """Display success message with OTP simulation"""
        # Generate a sample OTP (in real scenario, Facebook sends this)
        sample_otp = ''.join(random.choices(string.digits, k=6))
        
        print(f"\n{'='*60}")
        print("📱 INCOMING SMS SIMULATION")
        print(f"{'='*60}")
        print(f"From: Facebook")
        print(f"To: {self.full_phone}")
        print(f"Time: {datetime.now().strftime('%H:%M:%S')}")
        print(f"{'='*60}")
        print(f"Facebook Password Reset Code:")
        print(f"\n    ┌──────────────────┐")
        print(f"    │     {sample_otp}     │")
        print(f"    └──────────────────┘")
        print(f"\nEnter this code to reset your password.")
        print(f"Code expires in 10 minutes.")
        print(f"Do not share with anyone.")
        print(f"{'='*60}")
        
        # Save OTP info to file
        otp_info = {
            "phone": self.full_phone,
            "otp_sample": sample_otp,
            "timestamp": datetime.now().isoformat(),
            "expires_at": (datetime.now().timestamp() + 600),  # 10 minutes
            "status": "sent",
            "note": "This is a sample OTP. Facebook would send the real one."
        }
        
        with open("facebook_otp_info.json", "w") as f:
            json.dump(otp_info, f, indent=2)
        
        print(f"\n💾 OTP info saved to: facebook_otp_info.json")
    
    def run(self):
        """Run the OTP sending process"""
        print(f"\n{'*'*70}")
        print("FACEBOOK OTP SENDER")
        print(f"{'*'*70}")
        print(f"Phone Number: {self.full_phone}")
        print(f"Target: Facebook Password Recovery")
        print(f"{'*'*70}")
        
        # Send OTP request
        success, message = self.send_otp_request()
        
        print(f"\n{'='*60}")
        if success:
            print("🎉 PROCESS COMPLETED SUCCESSFULLY!")
        else:
            print("⚠️  PROCESS COMPLETED WITH ISSUES")
        print(f"Message: {message}")
        print(f"{'='*60}")

def main():
    """Main function"""
    # Create sender instance
    sender = FacebookOTPSender(phone_number="8978987888")
    
    # Run the process
    sender.run()
    
    print("\n📋 Next Steps:")
    print("1. Check your phone for SMS from Facebook")
    print("2. Enter the 6-digit code on Facebook's website")
    print("3. Reset your password")
    print("\n⚠️  Note: This script simulates the request.")
    print("   Facebook's actual response may vary.")

if __name__ == "__main__":
    main()
