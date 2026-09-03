#!/usr/bin/env python3
"""
Python File Encoder using Marshal + Base64
Usage: python enc.py /sdcard/file.py /sdcard/enc-file.py
"""

import marshal
import base64
import sys
import os
import zlib  # Optional: for compression

def encode_python_file(input_file, output_file, compress=True):
    """
    Encode a Python file using marshal + base64
    
    Args:
        input_file: Path to source Python file
        output_file: Path to output encoded file
        compress: Whether to compress before encoding (optional)
    """
    
    try:
        # Read the source file
        with open(input_file, 'r', encoding='utf-8') as f:
            source_code = f.read()
        
        print(f"[+] Read source file: {input_file}")
        print(f"[+] Original size: {len(source_code)} bytes")
        
        # Compile the source code to code object
        code_object = compile(source_code, '<string>', 'exec')
        print("[+] Compiled to code object")
        
        # Marshal the code object
        marshaled = marshal.dumps(code_object)
        print(f"[+] Marshaled size: {len(marshaled)} bytes")
        
        # Optional: Compress with zlib
        if compress:
            marshaled = zlib.compress(marshaled, level=9)
            print(f"[+] Compressed size: {len(marshaled)} bytes")
        
        # Encode with base64
        encoded = base64.b64encode(marshaled).decode('ascii')
        print(f"[+] Base64 encoded size: {len(encoded)} bytes")
        
        # Create the decoder script
        decoder_script = f'''#!/usr/bin/env python3
# Auto-generated decoder script
import marshal
import base64
import zlib

# Encoded data
encoded_data = """{encoded}"""

# Decode and execute
try:
    # Decode from base64
    decoded = base64.b64decode(encoded_data)
    
    # Try decompressing (if compression was used)
    try:
        decoded = zlib.decompress(decoded)
    except zlib.error:
        pass  # Not compressed
    
    # Unmarshal and execute
    code_obj = marshal.loads(decoded)
    exec(code_obj)
    
except Exception as e:
    print(f"Error executing encoded file: {{e}}")
    raise
'''
        
        # Write the encoded file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(decoder_script)
        
        # Make executable on Unix-like systems
        if sys.platform != 'win32':
            os.chmod(output_file, 0o755)
        
        print(f"[+] Successfully created: {output_file}")
        print(f"[+] Encoded file size: {len(decoder_script)} bytes")
        
        # Show compression ratio
        if compress:
            ratio = (len(decoder_script) / len(source_code)) * 100
            print(f"[+] Compression ratio: {ratio:.1f}% of original")
        
        return True
        
    except FileNotFoundError:
        print(f"[-] Error: Input file not found: {input_file}")
        return False
    except SyntaxError as e:
        print(f"[-] Error: Syntax error in source file: {e}")
        return False
    except Exception as e:
        print(f"[-] Error: {e}")
        return False

def main():
    # Check arguments
    if len(sys.argv) != 3:
        print("Usage: python enc.py <input_file> <output_file>")
        print("Example: python enc.py /sdcard/file.py /sdcard/enc-file.py")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    # Validate input file
    if not input_file.endswith('.py'):
        print("[-] Warning: Input file doesn't have .py extension")
    
    print("=" * 50)
    print("Python File Encoder (Marshal + Base64)")
    print("=" * 50)
    
    # Encode the file
    success = encode_python_file(input_file, output_file, compress=True)
    
    if success:
        print("\n[+] Encoding completed successfully!")
        print(f"[+] You can run the encoded file with: python {output_file}")
    else:
        print("\n[-] Encoding failed!")
        sys.exit(1)

if __name__ == "__main__":
    main()
