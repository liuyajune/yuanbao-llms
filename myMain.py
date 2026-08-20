import requests

url = "https://ip9.com.cn/get"
resp = requests.get(url, timeout=5)
data = resp.json()

print("你的公网 IP 是：", data["data"]["ip"])