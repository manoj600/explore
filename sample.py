from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import pandas as pd
from selenium.webdriver.common.action_chains import ActionChains

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
driver.maximize_window()


driver.get('https://www.justdial.com/Vizag/hospitals')
address = []
name = []
lst = driver.find_elements_by_class_name('store-details')
for idx,each in enumerate(lst):
    name.append(each.find_element_by_tag_name('h2').text)
    phn = each.find_element_by_class_name('contact-info').text
    print(name,phn)
    ele = driver.find_element_by_id('morehvr_add'+str(idx))
    builder = ActionChains(driver)    
    builder.move_to_element(ele).perform()
    address.append(driver.find_element_by_id('morehvr_add_cont'+str(idx)).text)
    
pd.DataFrame(['Hospital Name':name,'Address':phn])