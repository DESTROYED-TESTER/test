import random
import socket

def generate_random_ip():
    # Indian public IP address ranges (some common ranges)
    first_octet = random.choice([14, 27, 49, 59, 61, 103, 115, 117, 124, 126, 139, 164, 171, 182, 183, 202])
    second_octet = random.randint(0, 255)
    third_octet = random.randint(0, 255)
    fourth_octet = random.randint(1, 254)  # Avoid 0 and 255 for valid hosts
    return f"{first_octet}.{second_octet}.{third_octet}.{fourth_octet}"

def check_ip(ip):
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False

def generate_working_ips(count):
    working_ips = set()
    while len(working_ips) < count:
        ip = generate_random_ip()
        if check_ip(ip):
            working_ips.add(ip)
    return list(working_ips)

# Generate 10 valid random Indian IPs
random_ips = generate_working_ips(10)
print(random_ips)
