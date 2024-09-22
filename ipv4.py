import random
import socket

def generate_random_ip():
    # Indian public IP address ranges (some common ranges)
    first_octet = random.choice([152])
    second_octet = random.randint(56, 59)
    third_octet = random.randint(130, 199)
    fourth_octet = random.randint(130, 199)  # Avoid 0 and 255 for valid hosts
    return f"{first_octet}.{second_octet}.{third_octet}.{fourth_octet}"

def check_ip(ip):
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False

def working_ips():
        ip = generate_random_ip()
        if check_ip(ip):
            working_ips.add(ip)
    return list(working_ips)

# Generate 10 valid random Indian IPs
random_ips = working_ips()
print(random_ips)
