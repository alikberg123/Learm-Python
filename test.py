import requests
import aiohttp

url = "https://alikberg123.github.io/android-store/"
r = requests.get(url)
u = aiohttp.get_payload(url)

print(r.url)
