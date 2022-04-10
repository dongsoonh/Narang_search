
import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv
import re
from time import sleep
import urllib.request


url = "https://eng.lottedfs.com/kr/display/category/first?dispShopNo1=10031769&treDpth=1"

s=Service(ChromeDriverManager().install())
# executable_path=r'/Users/dongsoon/Downloads/narangsearch/chromedriver', options = options, 
driver = webdriver.Chrome(service=s)
driver.get(url)
driver.implicitly_wait(10)


for page in range(1,6):
    driver.execute_script("fn_movePage({0}, 'GOODS', 'searchShopPrdList')".format(page))
    driver.implicitly_wait(50)
    try:
        brand = driver.find_element_by_css_selector("div.unit_info > span.brand > i").text
        name = driver.find_element_by_css_selector("div.unit_info > span.name").text
        img_url = driver.find_element(By.CSS_SELECTOR, "#productDetail > div > div.thumb-info > div > div > img").get_attribute("src")
        img = "=image(\""+img_url+"\")"
        price = driver.find_element_by_css_selector("div.unit_price > strong.price02").text
        review = driver.find_element_by_css_selector("div.unit_price > div > span.total").text
    except:
        pass
    product_info = [brand, name, price, review]
    print(product_info)