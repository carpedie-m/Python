import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
from selenium import webdriver
import time

# 메뉴
print(">>> 인스타그램 이미지 다운로드 >>> --------------------------------------------------")
urlInit = "https://www.instagram.com/explore/tags/"
urlKeyword = input("● 검색할 Image 입력 > ")
url = urlInit + urllib.parse.quote_plus(urlKeyword)

# driver
driver = webdriver.Chrome("/Users/choeseunghui/Developer/chromedriver")
driver.get(url)
time.sleep(3)

response = driver.page_source
soup = BeautifulSoup(response, "html.parser")

instagramImage = soup.select(".v1Nh3.kIKUG._bz0w")

site_change = "https://www.instagram.com/"


num = 1
for i in instagramImage:
    print(site_change + i.a["href"])
    imgUrl = i.select_one(".KL4Bh").img["src"]
    with urllib.request.urlopen(imgUrl) as imgUrl:
        with open("/Users/choeseunghui/Documents/" + urlKeyword + str(num) + ".png", "wb") as imgWrite:
            imgAll = imgUrl.read()
            imgWrite.write(imgAll)
    num += 1

driver.close()