from selenium import *
from helium import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains
import sys,time

start_time = time.time()

file_company_name = open(r'/ChatBot_Py/Crawl_data/s.cafef/list_company_name.txt','w+', encoding="utf-8")
list_company_name = file_company_name.read().split('\n')
URL = 'http://liveboard.cafef.vn/'
# print(list_stock_code)

def check_code(label,list):
    if label in list:
        return False
    return True
        
def crawl_data(URL):
    try:
        driver = start_chrome(URL,headless=True)
        action = ActionChains(driver)
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'fixedHeader')))
        tbody = driver.find_elements_by_xpath("//tbody[@role='alert'][@aria-live='polite'][@aria-relevant='all']")
        tr = tbody[0].find_elements_by_tag_name('tr')
        for i in tr:
            label = i.find_element_by_tag_name('td').find_element_by_tag_name('label')
            action.move_to_element(label).perform()
            # time.sleep(1)
            label = label.get_attribute('title')
            print(label)
            if(check_code(label,list_company_name)):
                list_company_name.append(label)
                file_company_name.write(label+'\n')

    except TimeoutException:
        print("An exception occurred:",TimeoutException)
    except NoSuchElementException:
        print("An exception occurred:",NoSuchElementException)
    finally:
        driver.quit()
        file_company_name.close()

print("Get company name")
crawl_data(URL)
print(time.time()-start_time)