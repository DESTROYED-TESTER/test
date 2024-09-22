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
def generate_random_port():
    return random.randint(1, 65535)  # Generate a random port number

def check_port(ip, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1)  # Set a timeout for the connection attempt
        return s.connect_ex((ip, port)) == 0  # Returns 0 if the port is open

def generate_unlimited_ips_and_ports():
    ips = set()
    while True:  # Infinite loop to generate unlimited IPs and ports
        ip = generate_unlimited_ips()
        if check_ip(ip):
            if ip not in ips:  # Avoid duplicates
                ips.add(ip)
                port = generate_random_port()  # Generate a random port
                yield ip, port  # Yield the IP and port

# Example usage:
ip_port_generator = generate_unlimited_ips_and_ports()
# Call the function to generate unlimited IPs
print(ipz)
print(ip_port_generator)

