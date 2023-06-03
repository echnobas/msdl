import requests, re, uuid, os

client = requests.Session()
session = uuid.uuid4()

edition_id = 2616
sku = "16029"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    "Referer": "https://www.microsoft.com/software-download/windows11"
}

urls = [
    f"https://vlscppe.microsoft.com/fp/tags.js?org_id=y6jn8c31&session_id={session}",
    f"https://vlscppe.microsoft.com/tags?org_id=y6jn8c31&session_id={session}",
    f"https://www.microsoft.com/en-us/api/controls/contentinclude/html?pageId=cd06bda8-ff9c-4a6e-912a-b92a21f42526&host=www.microsoft.com&segments=software-download%2cwindows11&query=&action=getskuinformationbyproductedition&sdVersion=2&productEditionId={edition_id}&sessionId={session}",
    f"https://www.microsoft.com/en-us/api/controls/contentinclude/html?pageId=cfa9e580-a81e-4a4b-a846-7b21bf4e2e5b&host=www.microsoft.com&segments=software-download%2Cwindows11&query=&action=GetProductDownloadLinksBySku&sdVersion=2&skuId={sku}&sessionId={session}"
]

pattern = r'href="([^"]*)"'
hrefs = list(map(lambda x: x.replace("amp;", ""), re.findall(pattern, [client.get(url, headers=headers).text for url in urls][-1])))
for link in hrefs:
    print(f"{link}")
os.system("pause")