import httpx
import base64

username = "azzip"
password = "qwer1234"
proxy_host = "127.0.0.1"
proxy_port = 8899

# Base64 encode username:password for Proxy-Authorization
proxy_auth = base64.b64encode(f"{username}:{password}".encode()).decode()
proxy_url = f"http://{proxy_host}:{proxy_port}"

# Custom Proxy with headers for CONNECT stage
proxies = {
    "http://": f"http://{username}:{password}@{proxy_host}:{proxy_port}",
    "https://": f"http://{username}:{password}@{proxy_host}:{proxy_port}"
}

# Test HTTPS via proxy with auth
with httpx.Client(proxies=proxies, verify=False) as client:
    r = client.get("https://httpbin.org/ip")
    print(r.text)
