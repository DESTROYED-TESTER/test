import requests

cookies = {
    'datr': 'xJxPaKQpoJElo6Qa5Stty0z3',
    'fr': '0RBYWl1RkhYfcDKNN..BoT5zE..AAA.0.0.Bo32Wq.AWc0KrnRiyGg2jvu-bDILFD-9N8',
    'sb': 'xJxPaBlxTvSWwpAbuoUHWKCU',
    'ps_l': '1',
    'ps_n': '1',
    'wd': '1440x525',
    'locale': 'en_GB',
    'sfau': 'AYhvo7IducmvURXmxFU_-D0U8iy09ZNg3utOo4EVvMDaedAjJtpH_cSiWrQ3Bg2GbcB_sG8o7iuxeOo8iEqIEur2-nwGu1AX0UGwJAINPNwKJvpL4CNmRRU_WacROvJ0WTnGKcB4mwM3LVnHvap5FZkLBXV-0VotEPGrkHustrjIQkAMTASRnrL9tl6iXOAq1rxPUVl9-twCWuu40Rbyn8_uaIWz7Y_YhQ5ZwujY63bDRm6yh4QAEcspGjvVttE7yles7lSiNxsUoeCUtOvCNiGr',
    'sfiu': 'AYjSaOIctGXnn4TzOsp6Iow5B4kylQsMGJ4QKEUFJUjYDt8U3ModTE2EBYbMgSnTSGvinHMhUsol1RtA1hn2Yw4-t7BFUjSNvWKWOfbYzUAGay1Yb1nKiqlfx2Hd-7KoUN6K1eVMfajAA3dwHGxSJDyBf1_X0fQ8Fv3-t43vNmiFSAXXv8j2Vo-rZxVfqtw-Gld3_tKA-O6PDfA9Fb2A7MqLVtHx9t_NSPcP0gjD45tsd9jkHG4GR_t-K7ixvc2WqZ7qnhBnQm2Jtv3fIdGfQqnvr7rdnuYK3u5Q__RWrPh6wywcO_fOfJHVk05O8vyI6bVSpoTmvVtufO9HHhN6Bf6k',
}


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:143.0) Gecko/20100101 Firefox/143.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Referer': 'https://www.facebook.com/?_rdr',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://www.facebook.com',
    'DNT': '1',
    'Alt-Used': 'www.facebook.com',
    'Connection': 'keep-alive',
    # 'Cookie': 'datr=xJxPaKQpoJElo6Qa5Stty0z3; fr=0RBYWl1RkhYfcDKNN..BoT5zE..AAA.0.0.Bo32Wq.AWc0KrnRiyGg2jvu-bDILFD-9N8; sb=xJxPaBlxTvSWwpAbuoUHWKCU; ps_l=1; ps_n=1; wd=1440x525; locale=en_GB; sfau=AYhvo7IducmvURXmxFU_-D0U8iy09ZNg3utOo4EVvMDaedAjJtpH_cSiWrQ3Bg2GbcB_sG8o7iuxeOo8iEqIEur2-nwGu1AX0UGwJAINPNwKJvpL4CNmRRU_WacROvJ0WTnGKcB4mwM3LVnHvap5FZkLBXV-0VotEPGrkHustrjIQkAMTASRnrL9tl6iXOAq1rxPUVl9-twCWuu40Rbyn8_uaIWz7Y_YhQ5ZwujY63bDRm6yh4QAEcspGjvVttE7yles7lSiNxsUoeCUtOvCNiGr; sfiu=AYjSaOIctGXnn4TzOsp6Iow5B4kylQsMGJ4QKEUFJUjYDt8U3ModTE2EBYbMgSnTSGvinHMhUsol1RtA1hn2Yw4-t7BFUjSNvWKWOfbYzUAGay1Yb1nKiqlfx2Hd-7KoUN6K1eVMfajAA3dwHGxSJDyBf1_X0fQ8Fv3-t43vNmiFSAXXv8j2Vo-rZxVfqtw-Gld3_tKA-O6PDfA9Fb2A7MqLVtHx9t_NSPcP0gjD45tsd9jkHG4GR_t-K7ixvc2WqZ7qnhBnQm2Jtv3fIdGfQqnvr7rdnuYK3u5Q__RWrPh6wywcO_fOfJHVk05O8vyI6bVSpoTmvVtufO9HHhN6Bf6k',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Priority': 'u=0, i',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

data = {
    'jazoest': '2924',
    'lsd': 'AdHsL0R9suM',
    'email': '61556720024158',
    'login_source': 'comet_headerless_login',
    'next': '',
    'shared_prefs_data': 'eyIzMDAwMCI6W3sidCI6MTc1OTQ3MTAxOS44MDQsImN0eCI6eyJjbiI6Imh0dHBzOi8vd3d3LmZhY2Vib29rLmNvbS8ifSwidiI6ZmFsc2V9XSwiMzAwMDEiOlt7InQiOjE3NTk0NzEwMTkuODA0LCJjdHgiOnsiY24iOiJodHRwczovL3d3dy5mYWNlYm9vay5jb20vIn0sInYiOjV9XSwiMzAwMDIiOlt7InQiOjE3NTk0NzEwMTkuODA0LCJjdHgiOnsiY24iOiJodHRwczovL3d3dy5mYWNlYm9vay5jb20vIn0sInYiOjJ9XSwiMzAwMDMiOlt7InQiOjE3NTk0NzEwMTkuODA0LCJjdHgiOnsiY24iOiJodHRwczovL3d3dy5mYWNlYm9vay5jb20vIn0sInYiOlsiZW4tVVMiLCJlbiJdfV0sIjMwMDA0IjpbeyJ0IjoxNzU5NDcxMDE5LjgwNCwiY3R4Ijp7ImNuIjoiaHR0cHM6Ly93d3cuZmFjZWJvb2suY29tLyJ9LCJlIjp7ImVjIjozfX1dLCIzMDAwNSI6W3sidCI6MTc1OTQ3MTAxOS44MDUsImN0eCI6eyJjbiI6Imh0dHBzOi8vd3d3LmZhY2Vib29rLmNvbS8ifSwidiI6eyJ3IjoxNDQwLCJoIjo1MjV9fV0sIjMwMDA3IjpbeyJ0IjoxNzU5NDcxMDE5LjgwNSwiY3R4Ijp7ImNuIjoiaHR0cHM6Ly93d3cuZmFjZWJvb2suY29tLyJ9LCJ2IjoiZGVuaWVkIn1dLCIzMDAwOCI6W3sidCI6MTc1OTQ3MTAxOS44NDgsImN0eCI6eyJjbiI6Imh0dHBzOi8vd3d3LmZhY2Vib29rLmNvbS8ifSwidiI6ImRlbmllZCJ9XSwiMzAwMTIiOlt7InQiOjE3NTk0NzEwMTkuODA1LCJjdHgiOnsiY24iOiJodHRwczovL3d3dy5mYWNlYm9vay5jb20vIn0sInYiOiIifV0sIjMwMDEzIjpbeyJ0IjoxNzU5NDcxMDE5LjgwNSwiY3R4Ijp7ImNuIjoiaHR0cHM6Ly93d3cuZmFjZWJvb2suY29tLyJ9LCJ2IjoiNS4wIChXaW5kb3dzKSJ9XSwiMzAwMTUiOlt7InQiOjE3NTk0NzEwMTkuODA1LCJjdHgiOnsiY24iOiJodHRwczovL3d3dy5mYWNlYm9vay5jb20vIn0sInYiOiJXaW4zMiJ9XSwiMzAwMTgiOlt7InQiOjE3NTk0NzEwMTkuODA2LCJjdHgiOnsiY24iOiJodHRwczovL3d3dy5mYWNlYm9vay5jb20vIn0sInYiOjJ9XSwiMzAwMjIiOlt7InQiOjE3NTk0NzEwMTkuODE1LCJjdHgiOnsiY24iOiJodHRwczovL3d3dy5mYWNlYm9vay5jb20vIn0sInYiOnRydWV9XSwiMzAwNDAiOlt7InQiOjE3NTk0NzEwMTkuODE1LCJjdHgiOnsiY24iOiJodHRwczovL3d3dy5mYWNlYm9vay5jb20vIn0sInYiOi0zMzB9XSwiMzAwOTMiOlt7InQiOjE3NTk0NzEwMTkuODE1LCJjdHgiOnsiY24iOiJodHRwczovL3d3dy5mYWNlYm9vay5jb20vIn0sInYiOjB9XSwiMzAwOTQiOlt7InQiOjE3NTk0NzEwMTkuODE1LCJjdHgiOnsiY24iOiJodHRwczovL3d3dy5mYWNlYm9vay5jb20vIn0sInYiOiJNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0OyBydjoxNDMuMCkgR2Vja28vMjAxMDAxMDEgRmlyZWZveC8xNDMuMCJ9XSwiMzAwOTUiOlt7InQiOjE3NTk0NzEwMTkuODE1LCJjdHgiOnsiY24iOiJodHRwczovL3d3dy5mYWNlYm9vay5jb20vIn0sInYiOjR9XSwiMzAxMDYiOlt7InQiOjE3NTk0NzEwMTkuNzU1LCJjdHgiOnsiY24iOiJodHRwczovL3d3dy5mYWNlYm9vay5jb20vIn0sInYiOmZhbHNlfSx7InQiOjE3NTk0NzEwMTkuODQ3LCJjdHgiOnsiY24iOiJodHRwczovL3d3dy5mYWNlYm9vay5jb20vIn0sInYiOnRydWV9XSwiMzAxMDciOlt7InQiOjE3NTk0NzEwMTkuNzU2LCJjdHgiOnsiY24iOiJodHRwczovL3d3dy5mYWNlYm9vay5jb20vIn0sInYiOmZhbHNlfV19',
    'encpass': '#PWD_BROWSER:5:1759471040:AXFQAEuVrDY3WFW4qX0hwrgskkWI/SNPIwuqjXy06j8DStFZi6T5t5mceDUYqcvBzJNdReUdJdDX/Zp9pdyytsw99EiVwnO3X0TkRWt6pg0hOsvdvm8NKwad6FfO3M3B01JdbYa/jmOc3g==',
}

# Use a session so cookies persist
session = requests.Session()

response = session.post(
    'https://www.facebook.com/login/?privacy_mutation_token=eyJ0eXBlIjowLCJjcmVhdGlvbl90aW1lIjoxNzU5NDcxMDE4LCJjYWxsc2l0ZV9pZCI6MzgxMjI5MDc5NTc1OTQ2fQ%3D%3D&next',
    cookies=cookies,
    headers=headers,
    data=data,
    allow_redirects=True
)

if "home.php" in response.url:
    print("✅ Login successful)
elif "checkpoint" in response.url or "confirmemail.php" in response.url:
    print("⚠️ Login requires verification:", response.url)
else:
    print("❌ Login failed")
    print("Final URL:", response.url)
