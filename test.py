import random

from selenium import webdriver
import time
import requests

driver = webdriver.Chrome()

url = 'http://yr-stage.yurun.com/mall-sys-stage/#/login?redirect=%2Findex'
# 打开登录页面
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(5)
time.sleep(2)
username = driver.find_element_by_xpath('''//*[@id="app"]/div/form/div[1]/div/div/input''')
username.clear()
username.send_keys('shanghuct')
password = driver.find_element_by_xpath('''//*[@id="app"]/div/form/div[2]/div/div/input''')
password.clear()
password.send_keys('123456')
driver.find_element_by_xpath('''//*[@id="app"]/div/form/div[3]/div/div[1]/input''').click()
time.sleep(10)
driver.find_element_by_xpath('''//*[@id="app"]/div/form/div[4]/div/button''').click()
time.sleep(4)
# 登录成功
driver.find_element_by_xpath('''//*[@id="app"]/div/div[1]/div[2]/div[1]/div/ul/div[3]/li/div''').click()
# 进入商品列表
driver.find_element_by_xpath('''//*[@id="app"]/div/div[1]/div[2]/div[1]/div/ul/div[3]/li/ul/div[3]/a/li''').click()
time.sleep(30)
# 进入发布页面
driver.find_element_by_xpath('''//*[@id="app"]/div/div[2]/section/div/form/div[9]/div/button[2]''').click()
time.sleep(2)

# 商品详情
response = requests.get('http://imgservice.suning.cn/uimg1/b2c/atmosphere/X16WcIA5puMQ7_1Pst9aYA.jpg_800w_800h_4e')
driver.find_element_by_xpath(
    '''//*[@id="app"]/div/div[2]/section/div/form/div[9]/div/div[1]/div[2]/div[2]/div[1]''').send_keys(response.content.decode())
time.sleep(2)
print(driver.find_element_by_xpath(
    '''//*[@id="app"]/div/div[2]/section/div/form/div[14]/div/div[1]/div[2]/div[2]/div[1]''').text)

# 点击提交
driver.find_element_by_xpath('''//*[@id="app"]/div/div[2]/section/div/form/div[15]/div/div/button''').click()

time.sleep(5)

driver.quit()
