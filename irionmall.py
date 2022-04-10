
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

#강아지 상품 
url = "http://www.irionmall.co.kr/shop/shopbrand.html?xcode=010&type=Y"

s=Service(ChromeDriverManager().install())
# executable_path=r'/Users/dongsoon/Downloads/narangsearch/chromedriver', options = options, 
driver = webdriver.Chrome(service=s)
driver.get(url)
driver.implicitly_wait(10)

filename = "cat.csv"
f = open(filename,"w",encoding="utf-8-sig", newline="")
writer = csv.writer(f)
title = ["Brand", "Product name","Image", "Sales price","Review"]
writer.writerow(title)

# 2) 오류가 날 때 다시 시도하는 방어 코드 짜기
for page in range(1,6):
        driver.get("http://www.irionmall.co.kr/shop/shopbrand.html?type=Y&xcode=010&sort=&page={0}".format(page))
        driver.implicitly_wait(150)
        for div in range(2, 19):
            dive_1 = "div.item-wrap > div:nth-child({})".format(div)
            driver.implicitly_wait(20)
            try: 
                for i in range(1,4):
                    dive2 =  dive_1 + "> dl:nth-child({0}) > dt > a".format(str(i))
                    driver.find_element(By.CSS_SELECTOR,"{}".format(dive2)).click()
                    driver.implicitly_wait(20)

                    product = driver.find_element(By.CSS_SELECTOR, "#form1 > div > h3").text
                    brand = product.split()[0]
                    price = driver.find_element(By.CSS_SELECTOR, "#pricevalue").text
                    review = driver.find_element(By.CSS_SELECTOR, "#form1 > div > p.title-sub").text[0]

                    img_url = driver.find_element(By.CSS_SELECTOR, "#productDetail > div > div.thumb-info > div > div > img").get_attribute("src")
                    img = "=image(\""+img_url+"\")"


                    product_info = [brand, product,img, price, review]
                    print(product_info)

                    writer.writerow(product_info)
                    driver.back()
            except:
                pass