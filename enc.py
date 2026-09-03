#!/usr/bin/env python3
# enc_script.py - Encrypt Python file with AES-256 + key file

import marshal
import base64
import os
import sys
from cryptography.fernet import Fernet

KEY_FILE = "encryption.key"

def load_or_create_key():
    """Load existing key or create a new one"""
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, 'rb') as f:
            return f.read()
    else:
        key = Fernet.generate_key()
        with open(KEY_FILE, 'wb') as f:
            f.write(key)
        print(f"🔑 New encryption key created: {KEY_FILE}")
        return key

def encrypt_file(input_file, output_file, key):
    """
    Encrypt a Python file with AES-256 encryption (no password)
    """
    try:
        # Check if input file exists
        if not os.path.exists(input_file):
            print(f"Error: Input file '{input_file}' not found!")
            return False
        
        # Read the source code
        with open(input_file, 'r', encoding='utf-8') as f:
            source_code = f.read()
        
        # Compile the source code
        compiled_code = compile(source_code, input_file, 'exec')
        
        # Marshal the compiled code
        marshaled_code = marshal.dumps(compiled_code)
        
        # Create Fernet cipher with key
        fernet = Fernet(key)
        
        # Encrypt the marshaled code
        encrypted_data = fernet.encrypt(marshaled_code)
        
        # Encode encrypted data with base64
        encrypted_b64 = base64.b64encode(encrypted_data).decode('utf-8')
        
        # Encode key for embedding
        key_b64 = base64.b64encode(key).decode('utf-8')
        
        # Create the encrypted script wrapper
        encrypted_script = f'''#!/usr/bin/env python3
# Encrypted script - Original: {os.path.basename(input_file)}
# AES-256 Encrypted (Fernet)
import marshal
import base64
from cryptography.fernet import Fernet

# Encrypted data
encrypted_data_b64 = "{encrypted_b64}"

# Encryption key (embedded)
key = base64.b64decode("{key_b64}")

def decrypt_and_execute():
    """Decrypt and execute the script"""
    try:
        # Decode encrypted data
        encrypted_data = base64.b64decode(encrypted_data_b64)
        
        # Create Fernet cipher
        fernet = Fernet(key)
        
        # Decrypt the data
        decrypted_data = fernet.decrypt(encrypted_data)
        
        # Unmarshal and execute
        unmarshaled_code = marshal.loads(decrypted_data)
        exec(unmarshaled_code)
        return True
    except Exception as e:
        print(f"❌ Decryption failed: {{str(e)}}")
        return False

if __name__ == "__main__":
    decrypt_and_execute()
'''
        
        # Write the encrypted script
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(encrypted_script)
        
        # Make it executable on Unix/Linux
        os.chmod(output_file, 0o755)
        
        print(f"✅ Success! File encrypted and saved to: {output_file}")
        print(f"📊 Original size: {os.path.getsize(input_file)} bytes")
        print(f"📊 Encrypted size: {os.path.getsize(output_file)} bytes")
        return True
        
    except Exception as e:
        print(f"❌ Error during encryption: {str(e)}")
        return False

def main():
    # Default paths
    default_input = "/sdcard/file.py"
    default_output = "/sdcard/enc-file.py"
    
    # Get input file from user
    print("=" * 60)
    print("🔒 Python File Encryptor (AES-256 + Key File)")
    print("=" * 60)
    
    # Load or create encryption key
    key = load_or_create_key()
    print(f"🔑 Using key from: {KEY_FILE}")
    
    # Ask for input file
    input_file = input(f"Enter input file path [{default_input}]: ").strip()
    if not input_file:
        input_file = default_input
    
    # Ask for output file
    output_file = input(f"Enter output file path [{default_output}]: ").strip()
    if not output_file:
        output_file = default_output
    
    print(f"\n📁 Input file: {input_file}")
    print(f"📁 Output file: {output_file}")
    print("\n⏳ Encrypting with AES-256...")
    
    # Perform encryption
    encrypt_file(input_file, output_file, key)

if __name__ == "__main__":
    # Check if cryptography is installed
    try:
        import cryptography
    except ImportError:
        print("❌ Required package 'cryptography' not found!")
        print("📦 Install it with: pip install cryptography")
        sys.exit(1)
    
    main()
