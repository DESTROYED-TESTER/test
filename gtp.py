import os
import time

def run_command(command):
    """Helper function to execute shell commands."""
    os.system(command)

def main():
    # Update and install necessary packages
    run_command('apt update')
    run_command('pkg update')
    run_command('pkg install git')
    run_command('pkg install python')
    run_command('pip install requests bs4 rich python-cfonts')

    # Install additional packages
    run_command('pkg install curl')

    # Clone and build pycdc
    run_command('git clone https://github.com/zrax/pycdc')
    os.chdir('pycdc')
    run_command('chmod 777 pycdc')
    run_command('cmake .')
    run_command('make')
    run_command('mv pycdc $PREFIX/bin')
    run_command('mv pycdas $PREFIX/bin')

    # Clear the screen and display logo
    os.system('clear')
    print(' TOOLS STARTING....')
    time.sleep(5)
    
    logo = '''
========================================
|███████╗ █████╗      ██╗██╗   ██╗
|██╔════╝██╔══██╗     ██║██║   ██║
|███████╗███████║     ██║██║   ██║
|╚════██║██╔══██║██   ██║██║   ██║
|███████║██║  ██║╚█████╔╝╚██████╔╝
|╚══════╝╚═╝  ╚═╝ ╚════╝  ╚═════╝
========================================
[TOOLS     =    FREE]
[MAKING    =    TEAM ERROR OFC]
[CODING    =    ARIYAN SAJU]
[DECODER >byte code<  TOOLS ALL IN ONE ]
========================================
    '''
    print(logo)
    os.system("xdg-open https://t.me/DARK_TEAM_LMNx9")

    # Download required files
    run_command('curl -O https://raw.githubusercontent.com/i4mMino/pycdc/main/pycdc')
    run_command('curl -O https://raw.githubusercontent.com/i4mMino/pycdc/main/pycdas')
    run_command('curl -O https://raw.githubusercontent.com/i4mMino/pycdc/main/minopyc.py')

    # Move and set permissions for downloaded files
    run_command('mv pycdc /data/data/com.termux/files/usr/bin/')
    run_command('mv pycdas /data/data/com.termux/files/usr/bin/')
    run_command('mv minopyc.py /data/data/com.termux/files/usr/lib/python3.11/')
    run_command('chmod 777 /data/data/com.termux/files/usr/lib/python3.11/minopyc.py')
    run_command('chmod 777 /data/data/com.termux/files/usr/bin/pycdc')
    run_command('chmod 777 /data/data/com.termux/files/usr/bin/pycdas')

    # Process the file
    file = input('ENTER FILE NAME : ')
    
    try:
        with open(file, 'r') as f:
            pass
    except FileNotFoundError:
        print('FILE NOT FOUND')
        return

    run_command(f'cp {file} .b.py')
    run_command('pycdc .b.py > .a.py')

    with open('.a.py', 'r') as f:
        files = f.read()

    if 'exec(str(chr' in files:
        c = files.split(']')[0] + "]\nprint(''.join([chr(i) for i in _]))"
        with open('.a.py', 'w') as f:
            f.write(c)
        run_command('python3 .a.py > .b.py')

    run_command('mv .a.py .b.py')
    print('SAJU x - TRY DECOD JUST A MIN...')
    print('====================================================')

    with open('.b.py', 'r') as f:
        file_content = f.read()

    # Decode based on patterns
    if "(__import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(b" in file_content:
        filer = file_content.split('exec(')[1]
        with open('.b.py', 'w') as f:
            f.write('import minopyc,marshal\ncode =(' + filer + "\nminopyc.dump_to_pyc(code, '.a.py')")
        run_command('python3 .b.py;pycdc .a.py > .b.py')

    if "(__import__('marshal').loads(__import__('marshal').loads(__import__('marshal').loads(" in file_content:
        filer = file_content.split('exec(')[1]
        with open('.b.py', 'w') as f:
            f.write('import minopyc,marshal\ncode =(' + filer + "\nminopyc.dump_to_pyc(code, '.a.py')")
        run_command('python3 .b.py;pycdc .a.py > .b.py')

    if 'exec(_(' in file_content:
        c = file_content.split('exec(_(')[1]
        l = 'import marshal,zlib,base64,minopyc\nx = ((' + c + "\ny = x[:: -1]\nb = marshal.loads(zlib.decompress(base64.b64decode(y)))\nminopyc.dump_to_pyc(b,'.a.py') "
        with open('.b.py', 'w') as f:
            f.write(l)
        run_command('python .b.py')
        run_command('pycdc .a.py > .b.py')

    if 'exec((_)(' in file_content:
        c = file_content.split('exec((_)(')[1]
        l = 'import marshal,zlib,base64,minopyc\nx = ((' + c + "\ny = x[:: -1]\nb = marshal.loads(zlib.decompress(base64.b64decode(y)))\nminopyc.dump_to_pyc(b,'.a.py') "
        with open('.b.py', 'w') as f:
            f.write(l)
        run_command('python .b.py')
        run_command('pycdc .a.py > .b.py')

    if 'exec(marshal.loads' in file_content:
        filer = file_content.replace('exec(', 'code=(')
        with open('.b.py', 'w') as f:
            f.write('import minopyc,marshal\n' + filer + "\nminopyc.dump_to_pyc(code, '.a.py')")
        run_command('python3 .b.py;pycdc .a.py > .b.py')

    if 'exec((lambda __,' in file_content:
        filer = file_content.replace('exec(', 'print(')
        with open('.a.py', 'w') as f:
            f.write(filer)
        run_command('python2 .a.py > .b.py')

    # Final output handling
    with open('.b.py', 'r') as f:
        c = f.read()

    if c == '':
        print('THE TOOL CAN JUST DECODE DATA')
        print('===============================')
        save = input('ENTER PATH TO SAVE FROM : ')
        run_command(f'pycdas .a.py > {save}')
        run_command('rm .a.py;rm .b.py')
    elif 'WARNING: Decompyle incomplete' in c:
        print('THE TOOL CAN JUST DECODE DATA')
        save = input('ENTER PATH TO SAVE FROM : ')
        run_command(f'pycdas .a.py > {save}')
    else:
        print('DECOD DONE ✔️')
        save = input('ENTER PATH TO SAVE FROM : ')
        with open(save, 'w') as f:
            f.write(c)

    run_command('rm .a.py')
    run_command('rm .b.py')
    print('THANKS FOR USING🤍')

if __name__ == '__main__':
    main()
