from config import web_site
import requests

web_site

res = requests.get(web_site)

print(res.status_code)
print(res.url)
if res.status_code == 200:
    print("Подкдючон успешно к", res.url)
elif "ERROR":
    print("ОШИПКА")
else:
    print("ERROR")
