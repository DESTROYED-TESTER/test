import random
import socket
import subprocess

def generate_random_ip():
    first_octet = random.choice([152])
    second_octet = random.randint(56, 59)
    third_octet = random.randint(130, 199)
    fourth_octet = random.randint(1, 254)  # Avoid 0 and 255 for valid hosts
    return f"{first_octet}.{second_octet}.{third_octet}.{fourth_octet}"

def is_live_ip(ip):
    # Ping the IP address
    try:
        # Use 'ping' command based on the operating system
        output = subprocess.run(
            ["ping", "-c", "1", ip],  # Use "-n" instead of "-c" for Windows
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        return output.returncode == 0
    except Exception as e:
        return False

def generate_live_ips():
    ips = set()
    while True:
        ip = generate_random_ip()
        if ip not in ips:  # Avoid duplicates
            ips.add(ip)
            if is_live_ip(ip):
                print(f"Live IP: {ip}")

# Call the function to generate and print live IPs
generate_live_ips()
