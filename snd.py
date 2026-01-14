# SIMPLE VERSION - Just request SMS and wait for manual entry

import requests

def simple_sms_request():
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
    # 'cookie': 'datr=Eitnac9Jr55lMaaETcsXwk3D; sb=EitnaZzbPfbccAsuj6eJIYfE; ps_l=1; ps_n=1; wd=885x773; fr=0DBxBjQV9WtPFwBoS..BpZysS..AAA.0.0.BpZztO.AWfGeKdmKj0jFW8rYpsnEF6YsKo; sfiu=AYjOUOXxcNVDG70MYednwW6CvWN2h2VBqaIMfP2T6-3X5GvGdN0acJftcx-C5Ldk5jnZjyHPoBd8zeEOrE5kMLIOBvF7M_PP5sIyRjdgJZxnozPqGxDviqJGFievrk86RoDTHH1W5Lj9RVS3rpx8s7-m4tRIfmvFYXZT5uUzQ8Z46lCLurzzCdIYY-fLLpjh-bSuWa6N1OVZ5xBaZ1KPJCEDYUFR_yVX5xgK0t__VTL6jSS_L_u8OG5AYG6RcSKiexw',
}
    
    url = 'https://www.facebook.com/recover/code/?ph[0]=%2B918101729293&rm=send_sms&cuid=AYiSW3R2b0RuCEnTZhJIOZ1kIg8w3X3kC3e9G5V61mES07ahkKWXRNYYIP8bsnYVTzEDJhYBe5RYzGXC_12f-rSDSzJaOg1t-B6C20O8Ez3iiL1F7da69Qcfhn5HRhg_MucjofyYUdHLXCK3QahStouZd2_CwNarpckNtwqtu0wnAsexDdYreXKr9cDg5P7J2ziuq8HWyXHnEwSc82bpISycWyI2s9p5p0WxNVNPSyeqbyz-kL_vFD9gWLStkRMrEFo&hash=AUa1tNWNK3-kVgxGtVU'
    
    response = requests.get(url, cookies=cookies, headers=headers)
    
    if response.status_code == 200:
        print("✅ SMS requested successfully!")
        print("📱 Check your phone for code")
        print(f"💬 Look for SMS to +918101729293")
        print(f"🔢 Code will be 6 digits (e.g., 123456)")
        return True
    else:
        print(f"❌ Failed: {response.status_code}")
        return False

# Run it
if simple_sms_request():
    print("\nNow check your phone and enter the code when prompted.")
else:
    print("\nFailed to send SMS request. Get fresh cookies.")
