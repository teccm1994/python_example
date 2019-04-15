# -*- coding:utf-8 -*-  
__author__ = 'chen_ming'
__date__ = '2019-03-19 22:11'

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

# firefox = webdriver.firefox()
browser = webdriver.Chrome()
browser.get("http://www.taobao.com")
# print(browser.page_source)

# 元素查找
try:
    input_id = browser.find_element(By.ID, "q")
    input_css = browser.find_element_by_css_selector("#q")
    input_xpath = browser.find_element_by_xpath('//*[@id="q"]')
    print(input_id)
    print(input_css)
    print(input_xpath)
except NoSuchElementException:
    print('No element')

# 元素交互
try:
    input_str = browser.find_element_by_id('q')
    input_str.send_keys('ipad')
    time.sleep(1)
    input_str.clear()
    input_str.send_keys("MacBook pro")
    button = browser.find_element_by_class_name('btn-search')
    button.click()
except TimeoutException:
    print('Time out')
finally:
    browser.close()

