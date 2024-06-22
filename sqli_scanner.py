import requests
import argparse
from urllib.parse import urlparse, parse_qsl, urlencode, urlunparse

def check_sqli(url):
    print(f"[*] Testing {url} for basic SQL Injection vulnerabilities...")
    
    # Common SQL Injection error strings
    errors = [
        "you have an error in your sql syntax",
        "warning: mysql",
        "unclosed quotation mark after the character string",
        "quoted string not properly terminated",
        "sql pattern syntax error"
    ]
    
    parsed = urlparse(url)
    params = parse_qsl(parsed.query)
    
    if not params:
        print("[-] No URL parameters found to test. URL should look like http://example.com/page?id=1")
        return
        
    vulnerable = False
    
    for i in range(len(params)):
        # Create a payload by appending a single quote
        test_params = list(params)
        key, value = test_params[i]
        test_params[i] = (key, value + "'")
        
        test_query = urlencode(test_params)
        test_url = urlunparse((parsed.scheme, parsed.netloc, parsed.path, parsed.params, test_query, parsed.fragment))
        
        try:
            response = requests.get(test_url, timeout=5)
            content = response.text.lower()
            
            for error in errors:
                if error in content:
                    print(f"[!] Vulnerability suspected within parameter '{key}'")
                    print(f"    Payload URL: {test_url}")
                    vulnerable = True
                    break
        except requests.exceptions.RequestException:
            pass
            
    if not vulnerable:
        print("[+] No basic SQL Injection vulnerabilities found.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Basic SQL Injection Scanner")
    parser.add_argument("url", help="Target URL with parameters (e.g., http://example.com/page?id=1)")
    args = parser.parse_args()
    
    check_sqli(args.url)
