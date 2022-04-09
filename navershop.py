import requests
import re
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv
import urllib.request
import time



url = "https://shopping.naver.com/home/p/index.naver"

s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.get(url)
driver.implicitly_wait(10)

#검색할 제품명 입력 
pdn = "zoom h1n" 

element = driver.find_element_by_name('query')
element.send_keys(pdn)
driver.find_element(By.CSS_SELECTOR, "#autocompleteWrapper > a.co_srh_btn._search.N\=a\:SNB\.search").click()

#네이버 리뷰수 많은 순 
driver.find_element(By.CSS_SELECTOR, "div > div.subFilter_sort_box__1r06j > a:nth-child(7)").click()

#제품정보 스크래핑.제품명,가격,배송비,구매사이트 링크, 리뷰수,구매건수. 

for i in range(1,11):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        
        # 에외처리시에 문제점. 제품 정보는 크게 3가지 블럭으로 구성되어 있는데 네이버쇼핑몰이 아닌 외부 몰일경우 mall_area에 있는 배송비, 리뷰수, 구매건수 정보가 없어서 에러가 발생 예외처리 코드를 이용했더니 없는 정보가 그 이전 정보를 가져옴.데이터가 없는경우 "None"으로 표시하고 싶음.  
        
        try: 
            product = driver.find_element(By.CSS_SELECTOR, "ul > div > div:nth-child({0}) > li > div > div.basicList_info_area__17Xyo > div.basicList_title__3P9Q7 > a".format(i)).get_attribute("title")
            price = driver.find_element(By.CSS_SELECTOR, "ul > div > div:nth-child({0}) > li > div > div.basicList_info_area__17Xyo > div.basicList_price_area__1UXXR > strong > span ".format(i)).text
            logi = driver.find_element(By.CSS_SELECTOR, " ul > div > div:nth-child({0}) > li > div > div.basicList_mall_area__lIA7R > ul > li:nth-child(2) > em".format(i)).text[4:-1]
            url = driver.find_element(By.CSS_SELECTOR, "div > div:nth-child({0}) > li > div > div.basicList_info_area__17Xyo > div.basicList_title__3P9Q7 > a".format(i)).get_attribute("href")
            review = driver.find_element(By.CSS_SELECTOR, "ul > div > div:nth-child({0}) > li > div > div.basicList_info_area__17Xyo > div.basicList_etc_box__1Jzg6 > a > em".format(i)).text
            sold = driver.find_element(By.CSS_SELECTOR, "ul > div > div:nth-child({0}) > li > div > div.basicList_info_area__17Xyo > div.basicList_etc_box__1Jzg6 > a:nth-child(2) > em".format(i)).text
        
        except :
            pass
            
        print(product,url,price,logi,review,sold)
 