import random
import socket

def generate_random_ipv6():
    # Generate a random IPv6 address
    segments = []
    for _ in range(8):
        segment = random.randint(0, 0xFFFF)  # Each segment can be from 0 to 65535
        segments.append(f"{segment:04x}")  # Format as four hexadecimal digits
    return ":".join(segments)

def check_ipv6(ip):
    try:
        socket.inet_pton(socket.AF_INET6, ip)
        return True
    except socket.error:
        return False

def generate_working_ipv6(count):
    working_ips = set()
    while len(working_ips) < count:
        ip = generate_random_ipv6()
        if check_ipv6(ip):
            working_ips.add(ip)
    return list(working_ips)

# Generate 10 valid random IPv6 addresses
random_ipv6 = generate_working_ipv6(10)
print(random_ipv6)
