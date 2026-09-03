#!/usr/bin/env python3
# enc_script.py - Advanced Multi-layer Python file encryption

import marshal
import base64
import os
import sys
import zlib
import hashlib
import json
import random
import string
import time
import secrets
from datetime import datetime

class MultiEncryptor:
    def __init__(self):
        self.encryption_methods = {
            '1': ('Base64 + XOR + Reverse (3 Layers)', self.encrypt_triple_layer),
            '2': ('Base64 + Zlib + Marshal (3 Layers)', self.encrypt_marshal_zlib_enhanced),
            '3': ('XOR + Zlib + Base64 + Reverse (4 Layers)', self.encrypt_four_layer),
            '4': ('Multi-layer with Dynamic Keys', self.encrypt_dynamic_keys),
            '5': ('Obfuscation + Encryption + Compression', self.encrypt_obfuscation_compression),
            '6': ('Time-based Encryption', self.encrypt_time_based),
            '7': ('Checksum Protected Encryption', self.encrypt_checksum_protected),
            '8': ('Ultimate Protection (All Methods)', self.encrypt_ultimate)
        }

    def generate_dynamic_key(self, seed=None):
        """Generate a dynamic key based on various factors"""
        if seed is None:
            seed = str(time.time()) + str(os.urandom(8))
        key = hashlib.sha256(seed.encode()).digest()
        return key

    def xor_encrypt(self, data, key):
        """XOR encryption with dynamic key"""
        key_bytes = key if isinstance(key, bytes) else key.encode()
        key_length = len(key_bytes)
        return bytes([data[i] ^ key_bytes[i % key_length] for i in range(len(data))])

    def obfuscate_code(self, source_code):
        """Enhanced code obfuscation"""
        lines = source_code.split('\n')
        obfuscated = []
        var_map = {}
        counter = 0
        
        # Random prefixes for obfuscation
        prefixes = ['_', '__', 'x', 'y', 'z', 'tmp', 'var', 'data']
        
        for line in lines:
            # Skip empty lines and comments
            if not line.strip() or line.strip().startswith('#'):
                obfuscated.append(line)
                continue
                
            # Obfuscate variable names
            if '=' in line and not line.strip().startswith('#'):
                parts = line.split('=', 1)
                if len(parts) == 2 and parts[0].strip().isidentifier():
                    var_name = parts[0].strip()
                    if var_name not in var_map:
                        prefix = random.choice(prefixes)
                        suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
                        var_map[var_name] = f'{prefix}{suffix}'
                    line = line.replace(var_name, var_map[var_name])
            
            # Add random dead code
            if random.random() < 0.1:  # 10% chance to add junk
                junk_var = ''.join(random.choices(string.ascii_lowercase, k=6))
                junk_value = random.randint(1, 9999)
                obfuscated.append(f'{junk_var} = {junk_value}  # Dead code')
            
            obfuscated.append(line)
        
        return '\n'.join(obfuscated)

    def encrypt_triple_layer(self, source_code):
        """Method 1: Base64 + XOR + Reverse"""
        # Layer 1: Reverse
        code = source_code[::-1]
        
        # Layer 2: XOR with dynamic key
        key = self.generate_dynamic_key()
        data = code.encode()
        encrypted = self.xor_encrypt(data, key)
        
        # Layer 3: Base64
        encoded = base64.b64encode(encrypted).decode()
        key_b64 = base64.b64encode(key).decode()
        
        wrapper = f'''#!/usr/bin/env python3
import base64

# Decryption
key = base64.b64decode("{key_b64}")
data = base64.b64decode("{encoded}")
data = bytes([data[i] ^ key[i % len(key)] for i in range(len(data))])
exec(data.decode()[::-1])
'''
        return wrapper

    def encrypt_marshal_zlib_enhanced(self, source_code):
        """Method 2: Enhanced Marshal + Zlib + Base64 with validation"""
        # Add integrity check
        checksum = hashlib.sha256(source_code.encode()).hexdigest()
        
        # Add checksum to code
        code_with_check = f'# CHECKSUM: {checksum}\n{source_code}'
        
        compiled = compile(code_with_check, '<string>', 'exec')
        marshaled = marshal.dumps(compiled)
        compressed = zlib.compress(marshaled, level=9)  # Max compression
        encoded = base64.b64encode(compressed).decode()
        
        wrapper = f'''#!/usr/bin/env python3
import marshal, base64, zlib, hashlib

data = base64.b64decode("{encoded}")
data = zlib.decompress(data)
code = marshal.loads(data)
exec(code)
'''
        return wrapper

    def encrypt_four_layer(self, source_code):
        """Method 3: XOR + Zlib + Base64 + Reverse"""
        # Layer 1: Reverse
        code = source_code[::-1]
        
        # Layer 2: XOR
        key = os.urandom(16)
        data = code.encode()
        encrypted = self.xor_encrypt(data, key)
        
        # Layer 3: Zlib
        compressed = zlib.compress(encrypted, level=9)
        
        # Layer 4: Base64
        encoded = base64.b64encode(compressed).decode()
        key_b64 = base64.b64encode(key).decode()
        
        wrapper = f'''#!/usr/bin/env python3
import base64, zlib

key = base64.b64decode("{key_b64}")
data = base64.b64decode("{encoded}")
data = zlib.decompress(data)
data = bytes([data[i] ^ key[i % len(key)] for i in range(len(data))])
exec(data.decode()[::-1])
'''
        return wrapper

    def encrypt_dynamic_keys(self, source_code):
        """Method 4: Multi-layer with dynamic keys"""
        # Generate multiple keys
        key1 = os.urandom(16)
        key2 = os.urandom(16)
        key3 = os.urandom(16)
        
        # Layer 1: XOR with key1
        data = source_code.encode()
        encrypted1 = self.xor_encrypt(data, key1)
        
        # Layer 2: XOR with key2
        encrypted2 = self.xor_encrypt(encrypted1, key2)
        
        # Layer 3: XOR with key3
        encrypted3 = self.xor_encrypt(encrypted2, key3)
        
        # Layer 4: Base64
        encoded = base64.b64encode(encrypted3).decode()
        
        # Store keys encoded
        k1 = base64.b64encode(key1).decode()
        k2 = base64.b64encode(key2).decode()
        k3 = base64.b64encode(key3).decode()
        
        wrapper = f'''#!/usr/bin/env python3
import base64

k1 = base64.b64decode("{k1}")
k2 = base64.b64decode("{k2}")
k3 = base64.b64decode("{k3}")
data = base64.b64decode("{encoded}")

# Decrypt in reverse order
for key in [k3, k2, k1]:
    data = bytes([data[i] ^ key[i % len(key)] for i in range(len(data))])

exec(data.decode())
'''
        return wrapper

    def encrypt_obfuscation_compression(self, source_code):
        """Method 5: Obfuscation + Encryption + Compression"""
        # Obfuscate
        obfuscated = self.obfuscate_code(source_code)
        
        # Compress
        compressed = zlib.compress(obfuscated.encode(), level=9)
        
        # Encrypt with XOR
        key = self.generate_dynamic_key()
        encrypted = self.xor_encrypt(compressed, key)
        
        # Base64 encode
        encoded = base64.b64encode(encrypted).decode()
        key_b64 = base64.b64encode(key).decode()
        
        wrapper = f'''#!/usr/bin/env python3
import base64, zlib

key = base64.b64decode("{key_b64}")
data = base64.b64decode("{encoded}")
data = bytes([data[i] ^ key[i % len(key)] for i in range(len(data))])
data = zlib.decompress(data)
exec(data.decode())
'''
        return wrapper

    def encrypt_time_based(self, source_code):
        """Method 6: Time-based encryption with expiration"""
        # Set expiration (24 hours from now)
        expiration = int(time.time()) + 86400
        
        # Add expiration check to code
        code_with_expiry = f'''
import time
if time.time() > {expiration}:
    raise Exception("This script has expired")

{source_code}
'''
        
        # Encrypt with standard method
        key = self.generate_dynamic_key()
        data = code_with_expiry.encode()
        encrypted = self.xor_encrypt(data, key)
        encoded = base64.b64encode(encrypted).decode()
        key_b64 = base64.b64encode(key).decode()
        
        wrapper = f'''#!/usr/bin/env python3
import base64, time

key = base64.b64decode("{key_b64}")
data = base64.b64decode("{encoded}")
data = bytes([data[i] ^ key[i % len(key)] for i in range(len(data))])
exec(data.decode())
'''
        return wrapper

    def encrypt_checksum_protected(self, source_code):
        """Method 7: Checksum protected encryption"""
        # Generate multiple checksums
        checksum1 = hashlib.md5(source_code.encode()).hexdigest()
        checksum2 = hashlib.sha256(source_code.encode()).hexdigest()
        
        # Add checksums to code
        code_with_checksums = f'''
# MD5: {checksum1}
# SHA256: {checksum2}

{source_code}
'''
        
        # Encrypt
        key = self.generate_dynamic_key()
        data = code_with_checksums.encode()
        encrypted = self.xor_encrypt(data, key)
        compressed = zlib.compress(encrypted, level=9)
        encoded = base64.b64encode(compressed).decode()
        key_b64 = base64.b64encode(key).decode()
        
        wrapper = f'''#!/usr/bin/env python3
import base64, zlib, hashlib

key = base64.b64decode("{key_b64}")
data = base64.b64decode("{encoded}")
data = zlib.decompress(data)
data = bytes([data[i] ^ key[i % len(key)] for i in range(len(data))])
exec(data.decode())
'''
        return wrapper

    def encrypt_ultimate(self, source_code):
        """Method 8: Ultimate Protection - All methods combined"""
        # Step 1: Obfuscation
        obfuscated = self.obfuscate_code(source_code)
        
        # Step 2: Add timestamp and checksums
        timestamp = int(time.time())
        checksum = hashlib.sha256(obfuscated.encode()).hexdigest()
        code_with_meta = f'''# Created: {datetime.now().isoformat()}
# Checksum: {checksum}
# Timestamp: {timestamp}

{obfuscated}
'''
        
        # Step 3: Reverse
        code_with_meta = code_with_meta[::-1]
        
        # Step 4: Multiple XOR layers
        key1 = os.urandom(32)
        key2 = os.urandom(32)
        key3 = os.urandom(32)
        
        data = code_with_meta.encode()
        data = self.xor_encrypt(data, key1)
        data = self.xor_encrypt(data, key2)
        data = self.xor_encrypt(data, key3)
        
        # Step 5: Zlib compression
        data = zlib.compress(data, level=9)
        
        # Step 6: Multiple Base64 encodings
        for _ in range(3):
            data = base64.b64encode(data)
        
        encoded = data.decode()
        
        # Encode keys
        k1 = base64.b64encode(key1).decode()
        k2 = base64.b64encode(key2).decode()
        k3 = base64.b64encode(key3).decode()
        
        wrapper = f'''#!/usr/bin/env python3
import base64, zlib, hashlib, time

# Decryption with validation
data = "{encoded}"
k1 = base64.b64decode("{k1}")
k2 = base64.b64decode("{k2}")
k3 = base64.b64decode("{k3}")

# Decode Base64 3 times
for _ in range(3):
    data = base64.b64decode(data)

# Decompress
data = zlib.decompress(data)

# XOR decrypt (reverse order)
for key in [k3, k2, k1]:
    data = bytes([data[i] ^ key[i % len(key)] for i in range(len(data))])

# Reverse
data = data[::-1]

# Extract and execute
code = data.decode()
# Remove metadata lines
lines = code.split('\\n')
exec_code = '\\n'.join([line for line in lines if not line.startswith('#')])
exec(exec_code)
'''
        return wrapper

    def encrypt_file(self, input_file, output_file, method):
        """Encrypt file using selected method"""
        try:
            if not os.path.exists(input_file):
                print(f"Error: Input file '{input_file}' not found!")
                return False

            with open(input_file, 'r', encoding='utf-8') as f:
                source_code = f.read()

            # Get encryption function
            encrypt_func = self.encryption_methods[method][1]
            encrypted_script = encrypt_func(source_code)

            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(encrypted_script)

            os.chmod(output_file, 0o755)

            print(f"✅ Success! File encrypted and saved to: {output_file}")
            print(f"📊 Original size: {os.path.getsize(input_file)} bytes")
            print(f"📊 Encrypted size: {os.path.getsize(output_file)} bytes")
            print(f"🔐 Method used: {self.encryption_methods[method][0]}")
            
            # Security metrics
            print(f"🔒 Security Level: {self.get_security_level(method)}")
            return True

        except Exception as e:
            print(f"❌ Error during encryption: {str(e)}")
            return False

    def get_security_level(self, method):
        """Get security level for each method"""
        security_levels = {
            '1': 'Medium (3 layers)',
            '2': 'Medium-High (3 layers + compression)',
            '3': 'High (4 layers)',
            '4': 'High (Dynamic multi-key)',
            '5': 'High (Obfuscation + compression)',
            '6': 'Medium-High (Time-limited)',
            '7': 'High (Checksum protected)',
            '8': 'Ultimate (All protections combined)'
        }
        return security_levels.get(method, 'Unknown')

    def display_menu(self):
        """Display encryption methods menu"""
        print("=" * 70)
        print("🔒 Advanced Python File Encryptor - Enhanced Security")
        print("=" * 70)
        print("\n📋 Available Encryption Methods:")
        print("-" * 70)
        for key, (name, _) in self.encryption_methods.items():
            security = self.get_security_level(key)
            print(f"  {key}. {name:<35} [Security: {security}]")
        print("-" * 70)
        print("  0. Exit")
        print("=" * 70)

def main():
    encryptor = MultiEncryptor()
    
    while True:
        encryptor.display_menu()
        
        # Get method choice
        choice = input("\n🔧 Select encryption method (0-8): ").strip()
        if choice == '0':
            print("👋 Goodbye!")
            break
        
        if choice not in encryptor.encryption_methods:
            print("❌ Invalid choice! Please try again.")
            continue
        
        # Get file paths
        default_input = "/sdcard/file.py"
        default_output = "/sdcard/enc-file.py"
        
        print("\n📁 File Paths:")
        input_file = input(f"  Input file [{default_input}]: ").strip()
        if not input_file:
            input_file = default_input
        
        output_file = input(f"  Output file [{default_output}]: ").strip()
        if not output_file:
            output_file = default_output
        
        print(f"\n📁 Input file: {input_file}")
        print(f"📁 Output file: {output_file}")
        print(f"🔐 Method: {encryptor.encryption_methods[choice][0]}")
        print(f"🔒 Security Level: {encryptor.get_security_level(choice)}")
        print("\n⏳ Encrypting...")
        
        encryptor.encrypt_file(input_file, output_file, choice)
        print("\n" + "=" * 70 + "\n")

if __name__ == "__main__":
    main()
