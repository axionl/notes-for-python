#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES
# import time

driver = webdriver.PhantomJS(executable_path='')
driver.get("http://pythonscraping.com/paes/javascript/ajaxDemo.html")
try:
    element = WevDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "loadedButton"))
    )
finally:
    print(driver.find_element_by_id("content").text)
    driver.close()
