import random
import socket

def generate_random_ip():
    return f"{random.randint(1, 223)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"

def check_ip(ip):
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False

def generate_working_ips(count):
    working_ips = []
    while len(working_ips) < count:
        ip = generate_random_ip()
        if check_ip(ip):
            working_ips.append(ip)
    return working_ips

# Generate 10 working random IPs
random_ips = generate_working_ips(10)
print(random_ips)
