from selenium import *
from helium import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from bs4 import BeautifulSoup
import sys,time

start_time = time.time()

file_stock_code = open(r'/ChatBot_Py/Crawl_data/database/list_stock_code.txt','r+')
list_stock_code = file_stock_code.read().split('\n')
URL = 'http://liveboard.cafef.vn/'
# print(list_stock_code)

def check_code(stock_code,list):
    if stock_code in list:
        return False
    return True
        
def crawl_data(URL):
    try:
        driver = start_chrome(URL,headless=True)
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'fixedHeader')))
        tbody = driver.find_elements_by_xpath("//tbody[@role='alert'][@aria-live='polite'][@aria-relevant='all']")
        tr = tbody[0].find_elements_by_tag_name('tr')
        for i in tr:
            stock_code = i.get_attribute('id')
            if(check_code(stock_code,list_stock_code)):
                list_stock_code.append(stock_code)
                file_stock_code.write(stock_code+'\n')
    except TimeoutException:
        print("An exception occurred:",TimeoutException)
    except NoSuchElementException:
        print("An exception occurred:",NoSuchElementException)
    finally:
        driver.quit()
        file_stock_code.close()
print("Get stock code")
crawl_data(URL)
print(time.time()-start_time)