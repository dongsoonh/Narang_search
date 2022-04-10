
import requests
import re
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv
from time import sleep
import urllib.request
import time


# 1) 사이트에서 카테고리 코드 뽑기
options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36")

catagories ={"skincare"}
sub_cat = "10031769"
makeup_1= []
makeup_face_Foundation = "10032503"
makeup_eye = "10031885"


url = "https://eng.lottedfs.com/kr/display/category/first?dispShopNo1=10031769&treDpth=1"

s=Service(ChromeDriverManager().install())
# executable_path=r'/Users/dongsoon/Downloads/narangsearch/chromedriver', options = options, 
driver = webdriver.Chrome(service=s)
driver.get(url)
driver.implicitly_wait(2)

filename = "Makeup_All.csv"
f = open(filename,"w",encoding="utf-8-sig", newline="")
writer = csv.writer(f)
title = ["Brand", "Product name", "Image","Sales price","Review"]
writer.writerow(title)


# 2) 오류가 날 때 다시 시도하는 방어 코드 짜기
for page in range(1, 96):
    driver.execute_script("fn_movePage({0}, 'GOODS', 'searchShopPrdList')".format(page))
    driver.implicitly_wait(200)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    products = len(driver.find_elements(By.CSS_SELECTOR, ".unit_info > span.brand > i"))
    for i, num in enumerate(range(1, products+1)):
        driver.implicitly_wait(200)
    
        try:
            brand = driver.find_element(By.CSS_SELECTOR, "li:nth-child({0}) > a > div.unit_info > span.brand > i".format(str(num))).text
            name = driver.find_element(By.CSS_SELECTOR, "li:nth-child({0}) > a > div.unit_info > span.name".format(str(num))).text

            img_url = driver.find_element(By.CSS_SELECTOR, "li:nth-child({0}) > a > div.unit_img > img".format(str(num))).get_attribute("src")
            #urllib.request.urlretrieve(img, name+".jpg")
            img = "=image(\""+img_url+"\")"

            sp = driver.find_element(By.CSS_SELECTOR, "li:nth-child({0}) > a > div.unit_price > strong.price02".format(str(num))).text
            review = driver.find_element(By.CSS_SELECTOR, "li:nth-child({0}) > a > div.unit_price > div > span.total".format(str(num))).text[1]
            product_info = [brand, name, img, sp, review]

            print(product_info)
            writer.writerow(product_info)
        
        except:
            pass
 
        
