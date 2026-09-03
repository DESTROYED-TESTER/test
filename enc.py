#!/usr/bin/env python3
# enc_script.py - Encrypt Python file using marshal + base64

import marshal
import base64
import os
import sys

def encrypt_file(input_file, output_file):
    """
    Encrypt a Python file using marshal and base64 encoding
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
        
        # Encode with base64
        encoded_code = base64.b64encode(marshaled_code).decode('utf-8')
        
        # Create the encrypted script wrapper
        encrypted_script = f'''#!/usr/bin/env python3
# Encrypted script - Original: {os.path.basename(input_file)}
import marshal
import base64

# Encrypted code
encrypted_code = "{encoded_code}"

# Decrypt and execute
decoded_code = base64.b64decode(encrypted_code)
unmarshaled_code = marshal.loads(decoded_code)
exec(unmarshaled_code)
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
    print("=" * 50)
    print("🔒 Python File Encryptor (Marshal + Base64)")
    print("=" * 50)
    
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
    print("\n⏳ Encrypting...")
    
    # Perform encryption
    encrypt_file(input_file, output_file)

if __name__ == "__main__":
    main()
