import requests
from bs4 import BeautifulSoup
# try: 
# from BeautifulSoup4 import BeautifulSoup
# except ImportError:
#     from bs4 import BeautifulSoup
b = requests.get('https://ark.intel.com/pl/products/88193/Intel-Core-i5-6200U-Processor-3M-Cache-up-to-2_80-GHz')
# urllib.request.urlopen
parsed = BeautifulSoup(b.text, "html5lib")
parsed.find_all("ul", attrs={"": "view-modal info-modal","data-modal": "tt-CoreCount"})
# parsed.

#tab-blade-1-0-1 > div > ul > li.CoreCount > span.label > a
print(b.text)
