from selenium import *
from helium import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# URL = "27.79.245.84:3000"
URL = "http://192.168.2.170:3000/"
driver = start_chrome(URL)
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "message"))
)
element = driver.find_element_by_xpath('//input[@class="message_input"]')
element.send_keys("max flow")
click("Send")
time.sleep(2)
element.send_keys("15")
click("Send")
time.sleep(2)
element.send_keys("0 40 35 35 40 35 0 0 0 0 0 0 0 0 0")
click("Send")
time.sleep(2)
element.send_keys("0 0 0 0 0 0 29 0 27 0 0 0 0 0 0")
click("Send")
time.sleep(2)
element.send_keys("0 0 0 0 0 0 20 0 0 0 0 0 0 0 0")
click("Send")
time.sleep(2)
element.send_keys("0 0 0 0 0 0 0 0 19 0 0 0 0 0 0")
click("Send")
time.sleep(2)
element.send_keys("0 0 0 0 0 0 0 0 0 27 0 0 0 0 0")
click("Send")
time.sleep(2)
element.send_keys("0 0 0 0 0 0 0 0 14 0 16 0 0 0 0")
click("Send")
time.sleep(2)
element.send_keys("0 0 0 0 0 0 0 0 0 0 0 18 0 0 0")
click("Send")
time.sleep(2)
element.send_keys("0 0 0 0 0 0 0 0 0 0 0 0 23 0 0")
click("Send")
time.sleep(2)
element.send_keys("0 0 0 0 0 0 0 0 0 0 0 0 14 0 0")
click("Send")
time.sleep(2)
element.send_keys("0 0 0 0 0 0 0 0 0 0 0 0 0 18 0")
click("Send")
time.sleep(2)
element.send_keys("0 0 0 0 0 0 0 0 0 0 0 0 10 0 0")
click("Send")
time.sleep(2)
element.send_keys("0 0 0 0 0 0 0 0 0 0 0 0 0 0 24")
click("Send")
time.sleep(2)
element.send_keys("0 0 0 0 0 0 0 0 0 0 0 0 0 0 10")
click("Send")
time.sleep(2)
element.send_keys("0 0 0 0 0 0 0 0 0 0 0 0 0 0 35")
click("Send")
time.sleep(2)
element.send_keys("0 0 0 0 0 0 0 0 0 0 0 0 0 0 0")
click("Send")