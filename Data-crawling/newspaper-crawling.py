from bs4 import BeautifulSoup
import requests


url = "https://news.v.daum.net/v/20210326194417713"

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')
name = soup.find_all("h3", {"class" : "tit_view"})
print(name)
