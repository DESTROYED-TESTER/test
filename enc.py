#!/usr/bin/env python3
"""
File Encryptor using Marshal and Base64
For Termux - Encrypts Python files
Usage: python encrypt.py /sdcard/file.py /sdcard/enc-file.py
"""

import marshal
import base64
import zlib
import os
import sys
import py_compile
import importlib.util

def encrypt_python_file(input_file, output_file):
    """
    Encrypt a Python file using marshal + base64 + compression
    """
    try:
        # Check if input file exists
        if not os.path.exists(input_file):
            print(f"[!] Error: Input file '{input_file}' not found!")
            return False
        
        # Read the source code
        with open(input_file, 'r', encoding='utf-8') as f:
            source_code = f.read()
        
        # Compile the source code to code object
        code_obj = compile(source_code, input_file, 'exec')
        
        # Marshal the code object
        marshalled = marshal.dumps(code_obj)
        
        # Compress with zlib
        compressed = zlib.compress(marshalled, level=9)
        
        # Encode with base64
        b64_encoded = base64.b64encode(compressed).decode('ascii')
        
        # Create the wrapper script
        wrapper_script = f'''#!/usr/bin/env python3
# Encrypted Python Script
# Original file: {os.path.basename(input_file)}
import marshal
import base64
import zlib

# Encrypted code
encrypted_code = """{b64_encoded}"""

# Decrypt and execute
try:
    decoded = base64.b64decode(encrypted_code.encode('ascii'))
    decompressed = zlib.decompress(decoded)
    code_obj = marshal.loads(decompressed)
    exec(code_obj)
except Exception as e:
    print(f"[!] Error executing encrypted script: {{e}}")
    print("[!] The script might be corrupted or modified")
'''
        
        # Write the encrypted file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(wrapper_script)
        
        # Make it executable on Unix-like systems
        os.chmod(output_file, 0o755)
        
        print(f"[+] Success! Encrypted file saved to: {output_file}")
        print(f"[+] Original file: {input_file}")
        print(f"[+] Encrypted size: {os.path.getsize(output_file)} bytes")
        return True
        
    except Exception as e:
        print(f"[!] Error: {str(e)}")
        return False

def main():
    # Check arguments
    if len(sys.argv) < 3:
        print("="*60)
        print("Python File Encryptor - Marshal + Base64")
        print("="*60)
        print("\nUsage:")
        print("  python encrypt.py <input_file> <output_file>")
        print("  python encrypt.py /sdcard/file.py /sdcard/enc-file.py")
        print("\nExample:")
        print("  python encrypt.py /sdcard/myscript.py /sdcard/encrypted.py")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    # Validate input file extension
    if not input_file.endswith('.py'):
        print("[!] Warning: Input file doesn't have .py extension")
    
    # Ensure output file has .py extension
    if not output_file.endswith('.py'):
        print("[!] Warning: Output file doesn't have .py extension")
        output_file += '.py'
        print(f"[+] Added .py extension: {output_file}")
    
    # Encrypt the file
    success = encrypt_python_file(input_file, output_file)
    
    if success:
        print("\n[+] Encryption completed successfully!")
    else:
        print("\n[!] Encryption failed!")
        sys.exit(1)

if __name__ == "__main__":
    main()
