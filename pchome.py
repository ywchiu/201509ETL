# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import  time, re
from bs4 import BeautifulSoup

driver = webdriver.Firefox()
driver.implicitly_wait(3)

driver.get('http://24h.pchome.com.tw/prod/DRAA0C-A90067G2U')
driver.implicitly_wait(1)
soup = BeautifulSoup(driver.page_source)
print soup.select('#PriceTotal')[0].text
driver.close()
