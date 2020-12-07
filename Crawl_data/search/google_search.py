from helium import *
from selenium import *

URL ='https://www.google.com/advanced_search'
driver = start_chrome(URL,headless=False)

all_these_words = driver.find_element_by_id('xX4UFf')
this_exact_word_or_phrase = driver.find_element_by_id('CwYCWc')
any_of_these_words = driver.find_element_by_id('mSoczb')
none_of_these_words = driver.find_element_by_id('t2dX1c')
numbers_ranging_from = driver.find_element_by_id('LK5akc')
language = driver.find_element_by_id('lr_button')
region = driver.find_element_by_id('cr_button')
last_update = driver.find_element_by_id('as_qdr_button')
site_or_domain = driver.find_element_by_id('NqEkZd')
terms_appearing = driver.find_element_by_id('as_occt_button')
SafeSearch = driver.find_element_by_id('as_safesearch_button')
file_type = driver.find_element_by_id('as_filetype_button')
usage_rights = driver.find_element_by_id('as_rights_button')
advanced_search = driver.find_elements_by_xpath("//input[@class='jfk-button jfk-button-action dUBGpe' and @type='submit']")[0]

# numbers_ranging_from.send_keys(u'\ue004 dong anh')
all_these_words.send_keys('thoi tiet')
language.click()
click('Tiếng Việt')
# site_or_domain.send_keys('vietnamnet.vn')
advanced_search.click()
# for e in all_these_words:
# print(driver.current_url)
# list_link = driver.find_elements_by_tag_name('a')
# for e in list_link:
#     if(e.get_attribute('href')!= None):
#         print(e.get_attribute('href'))
whether = driver.find_element_by_id("wob_wc").screenshot_as_png("thoitiet")
driver.quit()