import os
import browser_cookie3
import requests

url = "https://www.github.com"

cj = browser_cookie3.firefox()
r = requests.get(url, cookies=cj)
print(cj)

"""
    The proxy url forwards your connection requests to a randomly rotating IP address in a pool of proxies before reaching the target website. 
    https://crawlbase.com/docs/smart-proxy/?utm_source=github_ad&utm_medium=social&utm_campaign=bard_api
    couldnt get rotating proxy to work 
"""
crawlbase_key = os.getenv("CRAWLBASE_KEY")
proxy_url = f"http://{crawlbase_key}:@smartproxy.crawlbase.com:8012"
proxies = {"http": proxy_url, "https": proxy_url}

print(f"proxies: {proxies}")