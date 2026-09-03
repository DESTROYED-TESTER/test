#!/usr/bin/env python3
# enc_script.py - Encrypt Python file using marshal + base64 + zlib

import marshal
import base64
import zlib
import os
import sys
import hashlib
import time

def encrypt_file(input_file, output_file, compress_level=9, password=None):
    """
    Encrypt a Python file using marshal, zlib compression, and base64 encoding
    
    Args:
        input_file: Source Python file
        output_file: Output encrypted file
        compress_level: zlib compression level (0-9)
        password: Optional password for basic XOR obfuscation
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
        
        # Compress with zlib
        compressed_code = zlib.compress(marshaled_code, compress_level)
        
        # Encode with base64
        encoded_code = base64.b64encode(compressed_code).decode('utf-8')
        
        # Add optional password protection (XOR obfuscation)
        if password:
            password_bytes = password.encode('utf-8')
            encoded_bytes = encoded_code.encode('utf-8')
            xored = bytearray()
            for i, byte in enumerate(encoded_bytes):
                xored.append(byte ^ password_bytes[i % len(password_bytes)])
            encoded_code = base64.b64encode(bytes(xored)).decode('utf-8')
        
        # Calculate checksum for integrity
        checksum = hashlib.sha256(encoded_code.encode()).hexdigest()
        
        # Create the encrypted script wrapper
        encrypted_script = f'''#!/usr/bin/env python3
# Encrypted script - Original: {os.path.basename(input_file)}
# Encrypted on: {time.strftime('%Y-%m-%d %H:%M:%S')}

import marshal
import base64
import zlib
import hashlib
import sys
import os

# Encrypted code
encrypted_code = """{encoded_code}"""

# Checksum for integrity verification
expected_checksum = "{checksum}"

# Optional password (modify or remove if not used)
password = {repr(password) if password else None}

def decrypt_and_execute():
    try:
        # Decode from base64
        if password:
            # XOR decryption
            password_bytes = password.encode('utf-8')
            decoded_bytes = base64.b64decode(encrypted_code.encode('utf-8'))
            xored = bytearray()
            for i, byte in enumerate(decoded_bytes):
                xored.append(byte ^ password_bytes[i % len(password_bytes)])
            code = xored.decode('utf-8')
        else:
            code = encrypted_code
        
        # Verify integrity
        actual_checksum = hashlib.sha256(code.encode()).hexdigest()
        if actual_checksum != expected_checksum:
            raise Exception("Checksum verification failed! The file may be corrupted.")
        
        # Decode, decompress and execute
        decoded_code = base64.b64decode(code)
        decompressed_code = zlib.decompress(decoded_code)
        unmarshaled_code = marshal.loads(decompressed_code)
        exec(unmarshaled_code)
        
    except Exception as e:
        print(f"Decryption error: {{e}}")
        sys.exit(1)

if __name__ == "__main__":
    decrypt_and_execute()
'''
        
        # Write the encrypted script
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(encrypted_script)
        
        # Make it executable on Unix/Linux
        if os.name == 'posix':
            os.chmod(output_file, 0o755)
        
        # Print statistics
        print(f"✅ Success! File encrypted and saved to: {output_file}")
        print(f"📊 Original size: {os.path.getsize(input_file):,} bytes")
        print(f"📊 Encrypted size: {os.path.getsize(output_file):,} bytes")
        print(f"📊 Compression ratio: {(1 - os.path.getsize(output_file)/os.path.getsize(input_file)) * 100:.1f}%")
        print(f"🔑 Checksum: {checksum[:16]}...")
        if password:
            print(f"🔒 Password protection: Enabled")
        return True
        
    except Exception as e:
        print(f"❌ Error during encryption: {str(e)}")
        return False

def main():
    # Default paths
    default_input = "/sdcard/file.py"
    default_output = "/sdcard/enc-file.py"
    
    print("=" * 60)
    print("🔒 Python File Encryptor (Marshal + zlib + Base64)")
    print("=" * 60)
    
    # Get input file
    input_file = input(f"Enter input file path [{default_input}]: ").strip()
    if not input_file:
        input_file = default_input
    
    # Get output file
    output_file = input(f"Enter output file path [{default_output}]: ").strip()
    if not output_file:
        output_file = default_output
    
    # Get compression level
    compress_input = input("Enter compression level (0-9, default 9): ").strip()
    compress_level = 9 if not compress_input else int(compress_input)
    compress_level = max(0, min(9, compress_level))
    
    # Ask for password protection
    password = input("Enter password for extra protection (optional): ").strip()
    if not password:
        password = None
    
    print(f"\n📁 Input file: {input_file}")
    print(f"📁 Output file: {output_file}")
    print(f"🔧 Compression level: {compress_level}")
    print(f"🔒 Password: {'Enabled' if password else 'Disabled'}")
    print("\n⏳ Encrypting...")
    
    # Perform encryption
    start_time = time.time()
    encrypt_file(input_file, output_file, compress_level, password)
    elapsed = time.time() - start_time
    print(f"⏱️  Time elapsed: {elapsed:.2f} seconds")

if __name__ == "__main__":
    main()
