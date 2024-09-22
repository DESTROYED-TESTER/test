import random
import socket

def generate_random_ip():
    # Common Indian IP ranges: 14.0.0.0 to 14.255.255.255, 27.0.0.0 to 27.255.255.255, etc.
    first_octet = random.choice([14, 27, 49, 59, 61, 103, 115, 117, 124, 126, 139, 164, 171, 182, 183])
    return f"{first_octet}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"

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
