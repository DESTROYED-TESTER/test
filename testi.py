# -*- coding=utf-8 -*-
from sys import stdout
import subprocess as sp
import os, sys, time, random, base64, marshal, getpass, re, zlib
m = '\x1b[1;91m'
u = '\x1b[1;95m'
h = '\x1b[1;92m'
p = '\x1b[1;37m'
k = '\x1b[1;33m'
b = '\x1b[1;34m'
bm = '\x1b[96m'

try:
    from uncompyle6.main import decompile
except Exception as e:
    sp.call('pip2 install uncompyle6', shell=True, stderr=sp.STDOUT)
red   = '\x1b[31m'
green = '\x1b[32m'
yellow = '\x1b[33m'
blue  = '\x1b[34m'
magenta = '\x1b[35m'
cyan  = '\x1b[36m'
white = '\x1b[37m'
reset = '\x1b[39m'
brblack = '\x1b[90m'
R = '\x1b[91m'
brgreen = '\x1b[92m'
k = '\x1b[93m'
brblue = '\x1b[94m'
brmgnt = '\x1b[95m'
brcyan = '\x1b[96m'
G = '\x1b[97m'

def jalan(z, t):
    for e in z:
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(t)

def load(word):
    lix = ['/', '-', '╲', '|']
    for i in range(5):
        for x in range(len(lix)):
            sys.stdout.write('\r{}{}'.format(word, lix[x]))
            time.sleep(0.2)
            sys.stdout.flush()

def banner_dec():
    banner = '{}'.format(m)
    print(banner)
    os.system('figlet -f slant "DECRYPT"')

def banner_enc():
    banner = '{}'.format(m)
    print(banner)
    os.system('figlet -f slant "ENCRYPT"')

def running(s):
    try:
        for c in s + '\n':
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.001)
    except (KeyboardInterrupt,EOFError):
        run('Exit!')

def run(x):
    pt = '\x1b[1;37m'
    rd = '\x1b[1;37m\x1b[1;31m'
    rg = '\x1b[6;32m'
    try:
        num = 0
        while num < 1:
            for i, char in enumerate(x):
                if i == 0:
                    print('\r{}{}{}{}'.format(rg, char.lower(), rd, x[1:]), end='')
                    sys.stdout.flush()
                else:
                    if i == 1:
                        okklah = x[0].lower()
                        print('\r{}{}{}{}{}{}'.format(rd, okklah, pt, char.lower(), rg, x[2:]), end='')
                        sys.stdout.flush()
                    elif i == i:
                        okklah = x[0:i].lower()
                        print('\r{}{}{}{}{}{}'.format(rd, okklah, pt, char.lower(), rg, x[i + 1:]), end='')
                        sys.stdout.flush()
                    time.sleep(0.07)
            num += 1
    except:
        exit()

def clr():
    os.system('clear')

def logo():
    banner_enc()

def b_menu():
    jalan("""-----------.        .-----------
  ------    \  __  /    ------
    -----    \(  )/    -----
       ---   ' \/ `   ---
         --- :    : ---
           --`    '--
           `/`/..\`\
        ====UU====UU====
            '//||\\`
              ''``
        Dec/Enc Python
""",0.001)

def menu():
    clr()
    b_menu()
    running('\n{}[{}1{}]{} Encrypt\n{}[{}2{}]{} Decrypt\n'.format(m,p,m,p,m,p,m,p,m,p,m,p,m,p,m,p,m,p,m,p))
    asww = input('{}[{}?{}]{} Choose {}>> {}'.format(m,p,m,p,k,p))
    if asww == '1' or asww == '01':
        load('Running...')
        menu_enc()
    elif asww == '2' or asww == '02':
        load('Running...')
        menu_dec()
    elif asww == '':
        run('Huh?')
        menu()
    else:
        run('Please check number options!')
        menu()

def menu_enc():
    clr()
    banner_enc()
    running('{}[{}01{}]{} Encrypt Base16'.format(m,p,m,k))
    running('{}[{}02{}]{} Encrypt Base32'.format(m,p,m,k))
    running('{}[{}03{}]{} Encrypt Base64'.format(m,p,m,k))
    running('{}[{}04{}]{} Encrypt Hex'.format(m,p,m,k))
    running('{}[{}05{}]{} Encrypt Marshal'.format(m,p,m,k))
    running('{}[{}06{}]{} Compile py > pyc'.format(m,p,m,k))
    running('{}[{}07{}]{} Encrypt Marshal Zlib Base64'.format(m,p,m,k))
    running('{}[{}08{}]{} Encrypt Zlib '.format(m,p,m,k))
    running('{}[{}00{}]{} Exit'.format(m,p,m,k))
    running('')
    try:
        inp = input('{}[{}??{}]{} Choose {}>>{} '.format(m,p,m,k,h,p))
    except (KeyboardInterrupt,EOFError):
        run ('Disable!!')
        menu()
    if inp == '1' or inp == '01':
        clr()
        Satu()
    elif inp == '2' or inp == '02':
        clr()
        Dua()
    elif inp == '3' or inp == '03':
        clr()
        Tiga()
    elif inp == '4' or inp == '04':
        clr()
        Empat()
    elif inp == '5' or inp == '05':
        clr()
        Lima()
    elif inp == '6' or inp == '06':
        clr()
        pyc()
    elif inp == '7' or inp == '07':
        clr()
        emzb()
    elif inp == '8' or inp == '08':
        clr()
        ezl()
    elif inp == '':
        run ('Input your choice!')
        time.sleep(2)
        menu_enc()
    elif inp == '0' or inp == '00':
        exit()
    else:
        run ('Wrong!, Please input your choice')
        time.sleep(2)
        menu_enc()

def menu_dec():
    clr()
    banner_dec()
    running('{}[{}01{}]{} Decrypt base16'.format(m,p,m,k))
    running('{}[{}02{}]{} Decrypt base32'.format(m,p,m,k))
    running('{}[{}03{}]{} Decrypt base64'.format(m,p,m,k))
    running('{}[{}04{}]{} Decrypt Hex'.format(m,p,m,k))
    running('{}[{}05{}]{} Decrypt Marshal'.format(m,p,m,k))
    running('{}[{}06{}]{} Uncompyle6 pyc > py'.format(m,p,m,k))
    running('{}[{}07{}]{} Decrypt Marshal,Zlib,Base64'.format(m,p,m,k))
    running('{}[{}08{}]{} Decrypt Zlib'.format(m,p,m,k))
    running('{}[{}00{}]{} Exit'.format(m,p,m,k))
    running('')
    try:
        inp = input('{}[{}??{}]{} Choose {}>>{} '.format(m,p,m,k,h,p))
    except (KeyboardInterrupt,EOFError):
        run ('Disable!!')
        menu()
    if inp == '1' or inp == '01':
        clr()
        Enam()
    elif inp == '2' or inp == '02':
        clr()
        Tujuh()
    elif inp == '3' or inp == '03':
        clr()
        Delapan()
    elif inp == '4' or inp == '04':
        clr()
        Sembilan()
    elif inp == '5' or inp == '05':
        clr()
        unmarsh()
    elif inp == '6' or inp == '06':
        clr()
        unpyc()
    elif inp == '7' or inp == '07':
        clr()
        mzb()
    elif inp == '8' or inp == '08':
        clr()
        zl()
    elif inp == '':
        run ('Input number!')
        time.sleep(2)
        menu_dec()
    elif inp == '0' or inp == '00':
        exit()
    else:
        run ('Wrong, Input your choice!')
        time.sleep(2)
        menu_dec()

def Satu():
    clr()
    logo()
    try:
        f = input('Filenames: ')
    except:
        exit()

    try:
        bk = open(f, 'r').read()
    except:
        run('file %s not found!' % f)
        time.sleep(1.7)
        Satu()
    else:
        jalan('Load')
        try:
            b = base64.b16encode(bk)
        except:
            pass
        else:
            with open('Hasil/base16.txt', 'w') as f:
                f.write(b.decode('utf-8'))
                f.close()
                run('saved in base16.txt')
                time.sleep(1.5)

    inp = input('try again? (y/n): ')
    if inp == 'y' or inp == 'Y':
        Satu()
    elif inp == 'n' or inp == 'N':
        exit()

def Dua():
    clr()
    logo()
    try:
        f = input('Filenames: ')
    except:
        exit()

    try:
        bk = open(f, 'r').read()
    except:
        run('file %s not found!' % f)
        time.sleep(1.7)
        Dua()
    else:
        jalan('Load')
        try:
            b = base64.b32encode(bk)
        except:
            pass
        else:
            with open('Hasil/base32.txt', 'w') as f:
                f.write(b.decode('utf-8'))
                f.close()
                run('saved in base32.txt')
                time.sleep(1.5)

    inp = input('try again? (y/n): ')
    if inp == 'y' or inp == 'Y':
        Dua()
    elif inp == 'n' or inp == 'N':
        exit()

def Tiga():
    clr()
    logo()
    try:
        f = input('Filenames: ')
    except:
        exit()

    try:
        bk = open(f, 'r').read()
    except:
        run('file %s not found!' % f)
        time.sleep(1.7)
        Tiga()
    else:
        jalan('Load')
        try:
            b = base64.b64encode(bk)
        except:
            pass
        else:
            with open('Hasil/base64.txt', 'w') as f:
                f.write(b.decode('utf-8'))
                f.close()
                run('saved in base64.txt')
                time.sleep(1.5)

    inp = input('try again? (y/n): ')
    if inp == 'y' or inp == 'Y':
        Tiga()
    elif inp == 'n' or inp == 'N':
        exit()

def Empat():
    clr()
    logo()
    try:
        f = input('Filenames: ')
    except:
        exit()

    try:
        bk = open(f, 'r').read()
    except:
        run('file %s not found!' % f)
        time.sleep(1.7)
        Empat()
    else:
        jalan('Load')
        try:
            b = bk.encode('hex')
        except:
            pass
        else:
            with open('Hasil/hex.txt', 'w') as f:
                f.write(b.decode('utf-8'))
                f.close()
                run('saved in hex.txt')
                time.sleep(1.5)

    inp = input('try again? (y/n): ')
    if inp == 'y' or inp == 'Y':
        Empat()
    elif inp == 'n' or inp == 'N':
        exit()

def Lima():
    clr()
    logo()
    try:
        f = input('Filenames: ')
    except:
        exit()

    try:
        bk = open(f, 'r').read()
    except:
        run('file %s not found!' % f)
        time.sleep(1.7)
        Lima()
    else:
        jalan('Load')
        try:
            b = marshal.dumps(bk)
        except:
            pass
        else:
            with open('Hasil/marshal.txt', 'w') as f:
                f.write(b.decode('utf-8'))
                f.close()
                run('saved in marshal.txt')
                time.sleep(1.5)

    inp = input('try again? (y/n): ')
    if inp == 'y' or inp == 'Y':
        Lima()
    elif inp == 'n' or inp == 'N':
        exit()

def pyc():
    clr()
    logo()
    try:
        f = input('Filenames: ')
    except:
        exit()

    try:
        bk = open(f, 'r').read()
    except:
        run('file %s not found!' % f)
        time.sleep(1.7)
        pyc()
    else:
        jalan('Load')
        try:
            b = compile(bk, '', 'exec')
        except:
            pass
        else:
            with open('Hasil/pyc.pyc', 'wb') as f:
                f.write(b)
                f.close()
                run('saved in pyc.pyc')
                time.sleep(1.5)

    inp = input('try again? (y/n): ')
    if inp == 'y' or inp == 'Y':
        pyc()
    elif inp == 'n' or inp == 'N':
        exit()

def emzb():
    clr()
    logo()
    try:
        f = input('Filenames: ')
    except:
        exit()

    try:
        bk = open(f, 'r').read()
    except:
        run('file %s not found!' % f)
        time.sleep(1.7)
        emzb()
    else:
        jalan('Load')
        try:
            b = marshal.dumps(bk)
            a = zlib.compress(b)
            h = base64.b64encode(a)
        except:
            pass
        else:
            with open('Hasil/emzblb.txt', 'w') as f:
                f.write(h.decode('utf-8'))
                f.close()
                run('saved in emzblb.txt')
                time.sleep(1.5)

    inp = input('try again? (y/n): ')
    if inp == 'y' or inp == 'Y':
        emzb()
    elif inp == 'n' or inp == 'N':
        exit()

def ezl():
    clr()
    logo()
    try:
        f = input('Filenames: ')
    except:
        exit()

    try:
        bk = open(f, 'r').read()
    except:
        run('file %s not found!' % f)
        time.sleep(1.7)
        ezl()
    else:
        jalan('Load')
        try:
            b = zlib.compress(bk.encode('utf-8'))
        except:
            pass
        else:
            with open('Hasil/zlib.txt', 'wb') as f:
                f.write(b)
                f.close()
                run('saved in zlib.txt')
                time.sleep(1.5)

    inp = input('try again? (y/n): ')
    if inp == 'y' or inp == 'Y':
        ezl()
    elif inp == 'n' or inp == 'N':
        exit()

def Enam():
    clr()
    banner_dec()
    try:
        f = input('Filenames: ')
    except:
        exit()

    try:
        bk = open(f, 'r').read()
    except:
        run('file %s not found!' % f)
        time.sleep(1.7)
        Enam()
    else:
        jalan('Load')
        try:
            b = base64.b16decode(bk)
        except:
            pass
        else:
            with open('Hasil/enbase16.txt', 'w') as f:
                f.write(b.decode('utf-8'))
                f.close()
                run('saved in enbase16.txt')
                time.sleep(1.5)

    inp = input('try again? (y/n): ')
    if inp == 'y' or inp == 'Y':
        Enam()
    elif inp == 'n' or inp == 'N':
        exit()

def Tujuh():
    clr()
    banner_dec()
    try:
        f = input('Filenames: ')
    except:
        exit()

    try:
        bk = open(f, 'r').read()
    except:
        run('file %s not found!' % f)
        time.sleep(1.7)
        Tujuh()
    else:
        jalan('Load')
        try:
            b = base64.b32decode(bk)
        except:
            pass
        else:
            with open('Hasil/enbase32.txt', 'w') as f:
                f.write(b.decode('utf-8'))
                f.close()
                run('saved in enbase32.txt')
                time.sleep(1.5)

    inp = input('try again? (y/n): ')
    if inp == 'y' or inp == 'Y':
        Tujuh()
    elif inp == 'n' or inp == 'N':
        exit()

def Delapan():
    clr()
    banner_dec()
    try:
        f = input('Filenames: ')
    except:
        exit()

    try:
        bk = open(f, 'r').read()
    except:
        run('file %s not found!' % f)
        time.sleep(1.7)
        Delapan()
    else:
        jalan('Load')
        try:
            b = base64.b64decode(bk)
        except:
            pass
        else:
            with open('Hasil/enbase64.txt', 'w') as f:
                f.write(b.decode('utf-8'))
                f.close()
                run('saved in enbase64.txt')
                time.sleep(1.5)

    inp = input('try again? (y/n): ')
    if inp == 'y' or inp == 'Y':
        Delapan()
    elif inp == 'n' or inp == 'N':
        exit()

def Sembilan():
    clr()
    banner_dec()
    try:
        f = input('Filenames: ')
    except:
        exit()

    try:
        bk = open(f, 'r').read()
    except:
        run('file %s not found!' % f)
        time.sleep(1.7)
        Sembilan()
    else:
        jalan('Load')
        try:
            b = bk.decode('hex')
        except:
            pass
        else:
            with open('Hasil/enhex.txt', 'w') as f:
                f.write(b.decode('utf-8'))
                f.close()
                run('saved in enhex.txt')
                time.sleep(1.5)

    inp = input('try again? (y/n): ')
    if inp == 'y' or inp == 'Y':
        Sembilan()
    elif inp == 'n' or inp == 'N':
        exit()

def unmarsh():
    clr()
    banner_dec()
    try:
        f = input('Filenames: ')
    except:
        exit()

    try:
        bk = open(f, 'r').read()
    except:
        run('file %s not found!' % f)
        time.sleep(1.7)
        unmarsh()
    else:
        jalan('Load')
        try:
            b = marshal.loads(bk)
        except:
            pass
        else:
            with open('Hasil/enmarshal.txt', 'w') as f:
                f.write(b.decode('utf-8'))
                f.close()
                run('saved in enmarshal.txt')
                time.sleep(1.5)

    inp = input('try again? (y/n): ')
    if inp == 'y' or inp == 'Y':
        unmarsh()
    elif inp == 'n' or inp == 'N':
        exit()

def unpyc():
    clr()
    banner_dec()
    try:
        f = input('Filenames: ')
    except:
        exit()

    try:
        bk = open(f, 'rb').read()
    except:
        run('file %s not found!' % f)
        time.sleep(1.7)
        unpyc()
    else:
        jalan('Load')
        try:
            b = decompile(bk)
        except:
            pass
        else:
            with open('Hasil/unpyc.py', 'w') as f:
                f.write(b.decode('utf-8'))
                f.close()
                run('saved in unpyc.py')
                time.sleep(1.5)

    inp = input('try again? (y/n): ')
    if inp == 'y' or inp == 'Y':
        unpyc()
    elif inp == 'n' or inp == 'N':
        exit()

def mzb():
    clr()
    banner_dec()
    try:
        f = input('Filenames: ')
    except:
        exit()

    try:
        bk = open(f, 'r').read()
    except:
        run('file %s not found!' % f)
        time.sleep(1.7)
        mzb()
    else:
        jalan('Load')
        try:
            b = base64.b64decode(bk)
            a = zlib.decompress(b)
            h = marshal.loads(a)
        except:
            pass
        else:
            with open('Hasil/enmzblb.txt', 'w') as f:
                f.write(h.decode('utf-8'))
                f.close()
                run('saved in enmzblb.txt')
                time.sleep(1.5)

    inp = input('try again? (y/n): ')
    if inp == 'y' or inp == 'Y':
        mzb()
    elif inp == 'n' or inp == 'N':
        exit()

def zl():
    clr()
    banner_dec()
    try:
        f = input('Filenames: ')
    except:
        exit()

    try:
        bk = open(f, 'rb').read()
    except:
        run('file %s not found!' % f)
        time.sleep(1.7)
        zl()
    else:
        jalan('Load')
        try:
            b = zlib.decompress(bk)
        except:
            pass
        else:
            with open('Hasil/enzlib.txt', 'w') as f:
                f.write(b.decode('utf-8'))
                f.close()
                run('saved in enzlib.txt')
                time.sleep(1.5)

    inp = input('try again? (y/n): ')
    if inp == 'y' or inp == 'Y':
        zl()
    elif inp == 'n' or inp == 'N':
        exit()

def masuk():
    try:
        os.mkdir('Hasil')
    except:
        pass

def main():
    masuk()
    menu()
main()
