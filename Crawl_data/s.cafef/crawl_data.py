import re,sys,os
sys.path.append(r'/ChatBot_Py/Crawl_data/database')
from selenium import *
from helium import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
import time
from bs4 import BeautifulSoup
start_time = time.time()
import get_stocks_code_scafef
from db import db, cursor, Error
import sql_query

URL = 'https://s.cafef.vn/Lich-su-giao-dich-{}-1.chn'

#Insert Data
file_stock_code = open(r'/ChatBot_Py/Crawl_data/database/list_stock_code.txt','r')
list_stock_code = file_stock_code.read().split('\n')
try:
    for i in range(0,5):
        cursor.execute(sql_query.drop_table_query.format(list_stock_code[i]))
        cursor.execute(sql_query.create_table_query.format(list_stock_code[i]))
except:
    print("Error while executing query")


def crawl_data(URL,STOCK_CODE):
    try:
        driver = start_chrome(URL.format(STOCK_CODE),headless=True)
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'bobottom')))
        for e in range(1,5):
            tbody = driver.find_elements_by_tag_name('tbody')
            tr = tbody[1].find_elements_by_tag_name('tr')
            for i in range(2,len(tr)):
                try:
                    td = tr[i].find_elements_by_tag_name('td')
                    NGAY = datetime.datetime.strptime(td[0].text, "%d/%m/%Y").strftime("%Y-%m-%d")
                    GIA_DIEU_CHINH = td[1].text
                    GIA_DONG_CUA = td[2].text
                    cursor.execute(sql_query.insert_query.format(STOCK_CODE,NGAY,GIA_DIEU_CHINH,GIA_DONG_CUA))
                    print(sql_query.insert_query.format(STOCK_CODE,NGAY,GIA_DIEU_CHINH,GIA_DONG_CUA))
                except Error as err:
                    print("ERROR:",err)
                    i=i+1
            pages = tbody[2].find_elements_by_tag_name('a')
            pages[-1].click()
            time.sleep(3)
    except:
        print("An exception occurred")
    finally:
        driver.close()
if __name__ == "__main__":
    for i in range (0,5):
        crawl_data(URL, list_stock_code[i])
        time.sleep(3)
    db.commit()
    cursor.close()
    db.close()
    print(time.time()-start_time)