import random
import socket
import subprocess
import platform

def generate_random_ip():
    # Indian public IP address ranges
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

def ping_ip(ip):
    # Determine the command based on the OS
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '1', ip]
    return subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE).returncode == 0

def check_port(ip, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1)  # Set a timeout for the connection attempt
        return s.connect_ex((ip, port)) == 0  # Returns 0 if the port is open

def generate_working_ips(max_ips=None, port=80):
    ips = set()
    while max_ips is None or len(ips) < max_ips:
        ip = generate_random_ip()
        if check_ip(ip) and ping_ip(ip) and check_port(ip, port):
            ips.add(ip)
            yield ip

# Example usage
if __name__ == "__main__":
    max_ips = 10  # Change this value as needed
    port_to_check = 80  # Specify the port you want to check
    ip_generator = generate_working_ips(max_ips, port_to_check)
    
    for ip in ip_generator:
        print(f"Working IP with port {port_to_check}: {ip}")
