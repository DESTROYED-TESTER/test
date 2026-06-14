import requests
import sys

def fetch_indian_proxies(proxy_type="all", timeout=5000, ssl="all", anonymity="all"):
    """
    Fetch Indian proxies from ProxyScrape API.
    
    Parameters:
    - proxy_type: "http", "socks4", "socks5", or "all"
    - timeout: timeout in milliseconds
    - ssl: "yes", "no", or "all"
    - anonymity: "elite", "anonymous", "transparent", or "all"
    """
    # ProxyScrape API endpoint for free proxies [citation:1][citation:4]
    url = "https://api.proxyscrape.com/v4/free-proxy-list/get"
    
    params = {
        "request": "display_proxies",
        "proxy_format": "protocolipport",
        "format": "text",
        "country": "in",  # India only [citation:1]
    }
    
    # Add optional filters
    if proxy_type != "all":
        params["protocol"] = proxy_type
    if ssl != "all":
        params["ssl"] = ssl
    if anonymity != "all":
        params["anonymity"] = anonymity
    if timeout:
        params["timeout"] = str(timeout)
    
    try:
        print(f"Fetching Indian proxies from ProxyScrape...")
        response = requests.get(url, params=params, timeout=30)
        response.raise_for_status()
        
        proxies = response.text.strip().split('\n')
        # Filter out empty lines
        proxies = [p.strip() for p in proxies if p.strip()]
        
        print(f"✅ Retrieved {len(proxies)} Indian proxies")
        return proxies
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching proxies: {e}")
        return []

def test_proxy(proxy, test_url="http://httpbin.org/ip", timeout=10):
    """
    Test if a proxy works.
    """
    proxy_dict = {
        "http": f"http://{proxy}",
        "https": f"http://{proxy}"
    }
    
    try:
        response = requests.get(
            test_url,
            proxies=proxy_dict,
            timeout=timeout
        )
        if response.status_code == 200:
            return True, response.json()
        return False, None
    except:
        return False, None

def save_proxies_to_file(proxies, filename="indian_proxies.txt"):
    """
    Save proxies to a text file.
    """
    with open(filename, 'w') as f:
        for proxy in proxies:
            f.write(f"{proxy}\n")
    print(f"💾 Saved {len(proxies)} proxies to {filename}")

def main():
    print("=" * 50)
    print("ProxyScrape - Indian Proxy Fetcher")
    print("=" * 50)
    
    # Fetch Indian proxies
    proxies = fetch_indian_proxies(
        proxy_type="all",  # Change to "http", "socks4", "socks5" as needed
        timeout=5000,      # 5 seconds timeout
        ssl="all",
        anonymity="all"
    )
    
    if not proxies:
        print("No proxies retrieved. Exiting.")
        sys.exit(1)
    
    # Display first 10 proxies
    print("\n📋 Sample proxies (first 10):")
    for i, proxy in enumerate(proxies[:10], 1):
        print(f"  {i}. {proxy}")
    
    # Save to file
    print("\n")
    save_proxies_to_file(proxies)
    
    # Optional: Test a few proxies
    print("\n🔍 Testing first 5 proxies...")
    working_proxies = []
    for proxy in proxies[:5]:
        success, result = test_proxy(proxy)
        if success:
            working_proxies.append(proxy)
            print(f"  ✅ {proxy} - Working (IP: {result.get('origin', 'Unknown')})")
        else:
            print(f"  ❌ {proxy} - Failed")
    
    if working_proxies:
        save_proxies_to_file(working_proxies, "working_indian_proxies.txt")

if __name__ == "__main__":
    main()
