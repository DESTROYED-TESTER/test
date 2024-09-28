import random
import socket
import requests

def generate_random_ip():
    first_octet = random.choice([152])
    second_octet = random.randint(56, 59)
    third_octet = random.randint(130, 199)
    fourth_octet = random.randint(1, 254)  # Avoid 0 and 255 for valid hosts
    return f"{first_octet}.{second_octet}.{third_octet}.{fourth_octet}"

def check_proxy(ip, port=80):
    proxy_url = f"http://{ip}:{port}"
    try:
        response = requests.get("http://httpbin.org/ip", proxies={"http": proxy_url, "https": proxy_url}, timeout=3)
        return response.status_code == 200
    except Exception as e:
        return False

def find_working_proxies(count=5):
    working_proxies = []
    while len(working_proxies) < count:
        ip = generate_random_ip()
        if check_proxy(ip):
            working_proxies.append(ip)
    return working_proxies

# Find working proxies
working_proxies = find_working_proxies(5)
for ip in working_proxies:
    print(f"Working proxy: {ip}")
