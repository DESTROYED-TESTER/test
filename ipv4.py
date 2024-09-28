import random
import socket

def generate_random_ip():
    # Indian public IP address ranges (some common ranges)
    first_octet = random.choice([152])
    second_octet = random.randint(56, 59)
    third_octet = random.randint(130, 199)
    fourth_octet = random.randint(1, 254)  # Avoid 0 and 255 for valid hosts
    return f"{first_octet}.{second_octet}.{third_octet}.{fourth_octet}"

def check_ip(ip):
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False

def generate_unlimited_ips():
    ips = set()
    while True:  # Infinite loop to generate unlimited IPs
        ip = generate_random_ip()
        if check_ip(ip):
            if ip not in ips:  # Avoid duplicates
                ips.add(ip)
                return f"{ip}"
                #print(ip)  # Print or yield the IP

# Call the function to generate unlimited IPs
ipz=generate_unlimited_ips()
print(ipz)


