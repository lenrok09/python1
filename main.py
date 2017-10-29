import requests
from bs4 import BeautifulSoup

b = requests.get('https://ark.intel.com/pl/search?q=i5-6200U')

parsed = BeautifulSoup(b.text, "html5lib")

search_resut = parsed.find_all("h4",attrs={"class" : "result-title"})[0]

try:
    part_url = search_resut.contents[0]['href']
    c = requests.get('https://ark.intel.com' + part_url)
except:
    print('fe')
    

parser_res = BeautifulSoup(c.text, "html5lib")
search_specs = parser_res.find_all("ul",attrs={"class" : "specs-list"}) 
specs = search_specs[1].find("li",attrs={"class" : "CoreCount"}).text    
#tab-blade-1-0-1 > div > ul > li.CoreCount > span.label > a
print(b.text)
