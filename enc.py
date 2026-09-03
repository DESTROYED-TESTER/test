#!/usr/bin/env python3
# enc_script.py - Multi-layer Python file encryption using various methods

import marshal
import base64
import os
import sys
import zlib
import hashlib
import json
import random
import string
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

class MultiEncryptor:
    def __init__(self):
        self.encryption_methods = {
            '1': ('Base64 Only', self.encrypt_base64_only),
            '2': ('Base64 + Zlib Compression', self.encrypt_base64_zlib),
            '3': ('Base64 + Marshal + Zlib', self.encrypt_marshal_zlib),
            '4': ('Fernet Symmetric Encryption', self.encrypt_fernet),
            '5': ('XOR Cipher', self.encrypt_xor),
            '6': ('Reverse + Base64', self.encrypt_reverse_base64),
            '7': ('Multi-layer Base64 (5x)', self.encrypt_multi_base64),
            '8': ('Base64 + Marshal + XOR', self.encrypt_marshal_xor),
            '9': ('Fernet + Marshal', self.encrypt_fernet_marshal),
            '10': ('Custom Obfuscation', self.encrypt_custom_obfuscation),
            '11': ('ALL Methods Combined', self.encrypt_all_combined)
        }

    def generate_key(self, password=None):
        """Generate a Fernet key from password or random"""
        if password:
            password = password.encode()
            salt = b'salt_123456789_'
            kdf = PBKDF2HMAC(
                algorithm=hashes.SHA256(),
                length=32,
                salt=salt,
                iterations=100000,
            )
            key = base64.urlsafe_b64encode(kdf.derive(password))
            return key
        return Fernet.generate_key()

    def encrypt_base64_only(self, source_code):
        """Method 1: Simple Base64 encoding"""
        encoded = base64.b64encode(source_code.encode()).decode()
        wrapper = f'''#!/usr/bin/env python3
import base64
exec(base64.b64decode("{encoded}").decode())
'''
        return wrapper

    def encrypt_base64_zlib(self, source_code):
        """Method 2: Base64 + Zlib compression"""
        compressed = zlib.compress(source_code.encode())
        encoded = base64.b64encode(compressed).decode()
        wrapper = f'''#!/usr/bin/env python3
import base64, zlib
exec(zlib.decompress(base64.b64decode("{encoded}")).decode())
'''
        return wrapper

    def encrypt_marshal_zlib(self, source_code):
        """Method 3: Marshal + Zlib + Base64"""
        compiled = compile(source_code, '<string>', 'exec')
        marshaled = marshal.dumps(compiled)
        compressed = zlib.compress(marshaled)
        encoded = base64.b64encode(compressed).decode()
        wrapper = f'''#!/usr/bin/env python3
import marshal, base64, zlib
exec(marshal.loads(zlib.decompress(base64.b64decode("{encoded}"))))
'''
        return wrapper

    def encrypt_fernet(self, source_code):
        """Method 4: Fernet symmetric encryption"""
        key = self.generate_key()
        f = Fernet(key)
        encrypted = f.encrypt(source_code.encode())
        encoded = base64.b64encode(encrypted).decode()
        key_b64 = base64.b64encode(key).decode()
        wrapper = f'''#!/usr/bin/env python3
from cryptography.fernet import Fernet
import base64
key = base64.b64decode("{key_b64}")
f = Fernet(key)
exec(f.decrypt(base64.b64decode("{encoded}")).decode())
'''
        return wrapper

    def encrypt_xor(self, source_code):
        """Method 5: XOR cipher with random key"""
        key = random.randint(1, 255)
        data = source_code.encode()
        encrypted_data = bytes([b ^ key for b in data])
        encoded = base64.b64encode(encrypted_data).decode()
        wrapper = f'''#!/usr/bin/env python3
import base64
key = {key}
data = base64.b64decode("{encoded}")
exec(bytes([b ^ key for b in data]).decode())
'''
        return wrapper

    def encrypt_reverse_base64(self, source_code):
        """Method 6: Reverse string + Base64"""
        reversed_code = source_code[::-1]
        encoded = base64.b64encode(reversed_code.encode()).decode()
        wrapper = f'''#!/usr/bin/env python3
import base64
exec(base64.b64decode("{encoded}").decode()[::-1])
'''
        return wrapper

    def encrypt_multi_base64(self, source_code):
        """Method 7: Multi-layer Base64 (5 times)"""
        data = source_code.encode()
        for _ in range(5):
            data = base64.b64encode(data)
        encoded = data.decode()
        wrapper = f'''#!/usr/bin/env python3
import base64
data = "{encoded}"
for _ in range(5):
    data = base64.b64decode(data)
exec(data.decode())
'''
        return wrapper

    def encrypt_marshal_xor(self, source_code):
        """Method 8: Marshal + XOR + Base64"""
        compiled = compile(source_code, '<string>', 'exec')
        marshaled = marshal.dumps(compiled)
        key = random.randint(1, 255)
        encrypted_data = bytes([b ^ key for b in marshaled])
        encoded = base64.b64encode(encrypted_data).decode()
        wrapper = f'''#!/usr/bin/env python3
import marshal, base64
key = {key}
data = base64.b64decode("{encoded}")
decrypted = bytes([b ^ key for b in data])
exec(marshal.loads(decrypted))
'''
        return wrapper

    def encrypt_fernet_marshal(self, source_code):
        """Method 9: Fernet + Marshal"""
        compiled = compile(source_code, '<string>', 'exec')
        marshaled = marshal.dumps(compiled)
        key = self.generate_key()
        f = Fernet(key)
        encrypted = f.encrypt(marshaled)
        encoded = base64.b64encode(encrypted).decode()
        key_b64 = base64.b64encode(key).decode()
        wrapper = f'''#!/usr/bin/env python3
import marshal, base64
from cryptography.fernet import Fernet
key = base64.b64decode("{key_b64}")
f = Fernet(key)
exec(marshal.loads(f.decrypt(base64.b64decode("{encoded}"))))
'''
        return wrapper

    def encrypt_custom_obfuscation(self, source_code):
        """Method 10: Custom obfuscation with variable renaming"""
        # Simple obfuscation: rename variables and add junk code
        lines = source_code.split('\n')
        obfuscated_lines = []
        var_map = {}
        counter = 0
        
        for line in lines:
            if '=' in line and not line.strip().startswith('#'):
                parts = line.split('=', 1)
                if len(parts) == 2 and parts[0].strip().isidentifier():
                    var_name = parts[0].strip()
                    if var_name not in var_map:
                        var_map[var_name] = f'_{counter}_'
                        counter += 1
                    line = line.replace(var_name, var_map[var_name])
            obfuscated_lines.append(line)
        
        obfuscated_code = '\n'.join(obfuscated_lines)
        encoded = base64.b64encode(obfuscated_code.encode()).decode()
        
        # Add junk code
        junk = f'__junk_{random.randint(1000,9999)}__'
        wrapper = f'''#!/usr/bin/env python3
import base64
{junk}=lambda x:x
exec(base64.b64decode("{encoded}").decode())
'''
        return wrapper

    def encrypt_all_combined(self, source_code):
        """Method 11: ALL methods combined for maximum security"""
        # Layer 1: Custom obfuscation
        lines = source_code.split('\n')
        var_map = {}
        counter = 0
        obfuscated_lines = []
        for line in lines:
            if '=' in line and not line.strip().startswith('#'):
                parts = line.split('=', 1)
                if len(parts) == 2 and parts[0].strip().isidentifier():
                    var_name = parts[0].strip()
                    if var_name not in var_map:
                        var_map[var_name] = f'_{counter}_'
                        counter += 1
                    line = line.replace(var_name, var_map[var_name])
            obfuscated_lines.append(line)
        code = '\n'.join(obfuscated_lines)
        
        # Layer 2: Reverse
        code = code[::-1]
        
        # Layer 3: XOR
        key1 = random.randint(1, 255)
        data = code.encode()
        code = bytes([b ^ key1 for b in data])
        
        # Layer 4: Marshal
        compiled = compile(code, '<string>', 'exec')
        code = marshal.dumps(compiled)
        
        # Layer 5: Zlib compression
        code = zlib.compress(code)
        
        # Layer 6: Fernet
        key2 = self.generate_key()
        f = Fernet(key2)
        code = f.encrypt(code)
        
        # Layer 7: Base64 (5 times)
        for _ in range(5):
            code = base64.b64encode(code)
        
        encoded = code.decode()
        key2_b64 = base64.b64encode(key2).decode()
        
        wrapper = f'''#!/usr/bin/env python3
import base64, zlib, marshal
from cryptography.fernet import Fernet

# Decryption layers (reverse order)
data = "{encoded}"
key2 = base64.b64decode("{key2_b64}")
key1 = {key1}

# Layer 7: Decode Base64 5 times
for _ in range(5):
    data = base64.b64decode(data)

# Layer 6: Fernet decrypt
f = Fernet(key2)
data = f.decrypt(data)

# Layer 5: Zlib decompress
data = zlib.decompress(data)

# Layer 4: Unmarshal
data = marshal.loads(data)

# Layer 3: XOR decrypt
data = bytes([b ^ key1 for b in data])

# Layer 2: Reverse
data = data[::-1]

# Layer 1: Execute
exec(data.decode())
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
            return True

        except Exception as e:
            print(f"❌ Error during encryption: {str(e)}")
            return False

    def display_menu(self):
        """Display encryption methods menu"""
        print("=" * 60)
        print("🔒 Python Multi-Layer File Encryptor")
        print("=" * 60)
        print("\n📋 Available Encryption Methods:")
        print("-" * 60)
        for key, (name, _) in self.encryption_methods.items():
            print(f"  {key}. {name}")
        print("-" * 60)
        print("  0. Exit")
        print("=" * 60)

def main():
    encryptor = MultiEncryptor()
    
    while True:
        encryptor.display_menu()
        
        # Get method choice
        choice = input("\n🔧 Select encryption method (0-11): ").strip()
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
        print("\n⏳ Encrypting...")
        
        encryptor.encrypt_file(input_file, output_file, choice)
        print("\n" + "=" * 60 + "\n")

if __name__ == "__main__":
    main()
