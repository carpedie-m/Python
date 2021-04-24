import urllib.request
from bs4 import BeautifulSoup
import csv

hdr = { 'User-Agent' : 'Mozilla/5.0' }
url = 'https://www.melon.com/chart/'

req = urllib.request.Request(url, headers=hdr)
html = urllib.request.urlopen(req).read()
soup = BeautifulSoup(html, 'html.parser')

lst50 = soup.select('.lst50')



# print(lst50[0])
# print(soup)
# print(soup) : header 값 없어서 에러 406








import csv

f = open('melon_acsv.py', 'a', encoding='utf-8', newline='')
wr = csv.writer(f)
wr.writerow()