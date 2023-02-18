from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import re
s = Service(executable_path=r'F:\Application\python\python\chromedriver.exe')
driver = webdriver.Chrome(service=s)
# driver = webdriver.Chrome("F:\Application\python\python\chromedriver.exe")  # 这个是chormedriver的地址
driver.get('https://qzone.qq.com/')
driver.switch_to.frame('login_frame')
driver.find_element('switcher_plogin').click()
driver.find_element('u').clear()
driver.find_element('u').send_keys("QQ号")
driver.find_element('p').clear()
driver.find_element('p').send_keys("QQ密码")
driver.find_element('login_button').click()
time.sleep(2)