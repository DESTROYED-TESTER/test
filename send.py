import requests
import re
import time

cookies = {
    'datr': 'Eitnac9Jr55lMaaETcsXwk3D',
    'sb': 'EitnaZzbPfbccAsuj6eJIYfE',
    'ps_l': '1',
    'ps_n': '1',
    'wd': '885x773',
    'fr': '0DBxBjQV9WtPFwBoS..BpZysS..AAA.0.0.BpZztO.AWfGeKdmKj0jFW8rYpsnEF6YsKo',
    'sfiu': 'AYjOUOXxcNVDG70MYednwW6CvWN2h2VBqaIMfP2T6-3X5GvGdN0acJftcx-C5Ldk5jnZjyHPoBd8zeEOrE5kMLIOBvF7M_PP5sIyRjdgJZxnozPqGxDviqJGFievrk86RoDTHH1W5Lj9RVS3rpx8s7-m4tRIfmvFYXZT5uUzQ8Z46lCLurzzCdIYY-fLLpjh-bSuWa6N1OVZ5xBaZ1KPJCEDYUFR_yVX5xgK0t__VTL6jSS_L_u8OG5AYG6RcSKiexw',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'dpr': '1',
    'priority': 'u=0, i',
    'referer': 'https://www.facebook.com/recover/initiate/?ldata=AWdsKhDiSxCGeTyjPxFK9ERP8mfBJf_sE87gTpIgSj31myYIL2JUSMLVq3PgOZh5Kd-oYgFQevhglw4Keu6NPW6nCVCI3WcQSLZTJyJTeFPU8IINV5Zs_9TxsgzAW3CTvseEpRou6deUZmZPVb7e70cbWcKLrrJY81mrbDt70sugjYSHELTXNT4QIVmeOZQx4hLHf2fkCe-wGdrRQwpTPv9vg6DjIyt5tvJOdVgb0S96peFzDSQSiRaKkyw110ypl96TndhsTk6Ab8Ql8CmmOZA5',
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

def send_sms_code_request():
    """Send request to get SMS code"""
    url = 'https://www.facebook.com/recover/code/?ph[0]=%2B918101729293&rm=send_sms&cuid=AYiSW3R2b0RuCEnTZhJIOZ1kIg8w3X3kC3e9G5V61mES07ahkKWXRNYYIP8bsnYVTzEDJhYBe5RYzGXC_12f-rSDSzJaOg1t-B6C20O8Ez3iiL1F7da69Qcfhn5HRhg_MucjofyYUdHLXCK3QahStouZd2_CwNarpckNtwqtu0wnAsexDdYreXKr9cDg5P7J2ziuq8HWyXHnEwSc82bpISycWyI2s9p5p0WxNVNPSyeqbyz-kL_vFD9gWLStkRMrEFo&hash=AUa1tNWNK3-kVgxGtVU'
    
    try:
        response = requests.get(url, cookies=cookies, headers=headers)
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            # Check if SMS was sent
            if "we sent a text" in response.text.lower() or "code has been sent" in response.text.lower():
                print("✅ SMS code has been sent to +918101729293")
                print("📱 Check your phone for the code!")
                return True
            elif "enter the code" in response.text.lower():
                print("✅ Ready to enter code. Check SMS on phone.")
                return True
            else:
                print("⚠ Page loaded but SMS might not have been sent")
                return False
        else:
            print(f"❌ Request failed: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def check_for_code_entry_page(response_text):
    """Check if we're on the code entry page"""
    patterns = [
        r'Enter the code.*?sent to',
        r'We sent a text.*?\+\d+',
        r'code.*?text message',
        r'enter.*?6.*?digit.*?code',
    ]
    
    for pattern in patterns:
        if re.search(pattern, response_text, re.IGNORECASE):
            return True
    return False

def extract_code_from_page(response_text):
    """Try to extract any code from the page (for debugging)"""
    # Look for 6-digit codes
    code_patterns = [
        r'\b\d{6}\b',  # 6-digit code
        r'Code:\s*(\d{6})',
        r'code is\s*(\d{6})',
        r'Your code.*?(\d{6})',
    ]
    
    for pattern in code_patterns:
        match = re.search(pattern, response_text, re.IGNORECASE)
        if match:
            return match.group(1)
    return None

def submit_recovery_code(code):
    """Submit the received SMS code"""
    # You need to find the form submission URL from the response
    # This is an example - you'll need to adjust based on actual response
    
    submit_url = 'https://www.facebook.com/recover/code/'
    submit_data = {
        'n': code,
        'action_dialog': '0',
        'submit[Continue]': 'Continue',
        # Add other required fields from the form
    }
    
    response = requests.post(submit_url, data=submit_data, cookies=cookies, headers=headers)
    return response

def main():
    print("=" * 50)
    print("Facebook SMS Code Recovery")
    print("=" * 50)
    
    # Step 1: Send SMS request
    print("\n1. Requesting SMS code...")
    success = send_sms_code_request()
    
    if not success:
        print("\n❌ Failed to request SMS code.")
        print("Possible reasons:")
        print("1. Cookies expired (especially 'fr' and 'sfiu')")
        print("2. Phone number not associated with Facebook")
        print("3. Rate limited")
        print("4. Need CAPTCHA")
        return
    
    # Step 2: Wait for SMS
    print("\n2. Waiting for SMS code...")
    print("   Please check your phone (+918101729293)")
    print("   SMS can take 1-5 minutes to arrive")
    
    # Step 3: Ask user to enter the code
    print("\n3. Enter the 6-digit code from SMS:")
    print("   (The code will look like: 123456)")
    
    # In a real implementation, you would:
    # 1. Wait for SMS to arrive
    # 2. Extract code from SMS (requires SMS access)
    # 3. Submit the code
    
    # Since we can't access SMS directly, here's what you need to do:
    print("\n📋 MANUAL STEPS:")
    print("1. Check your phone for SMS from Facebook")
    print("2. The SMS will contain a 6-digit code")
    print("3. Enter that code in the Facebook recovery page")
    print("4. Or use the code in your recovery flow")

# Common SMS formats from Facebook:
SMS_EXAMPLES = """
Facebook SMS examples:
1. "Your Facebook code is 123456. Don't share it."
2. "123456 is your Facebook recovery code."
3. "Use 123456 to reset your Facebook password."
4. "Facebook code: 123456"
"""

if __name__ == "__main__":
    print(SMS_EXAMPLES)
    main()
