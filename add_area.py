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
time.sleep(6)
driver.find_element_by_xpath('''//*[@id="app"]/div/form/div[4]/div/button''').click()
time.sleep(4)
# 登录成功
driver.find_element_by_xpath('''//*[@id="app"]/div/div[1]/div[2]/div[1]/div/ul/div[8]/li/div/span''').click()
# '''//*[@id="app"]/div/div[1]/div[2]/div[1]/div/ul/div[8]/li/div/span'''
time.sleep(1)
driver.find_element_by_xpath('''//*[@id="app"]/div/div[1]/div[2]/div[1]/div/ul/div[8]/li/ul/div/a/li/span''').click()
# '''//*[@id="app"]/div/div[1]/div[2]/div[1]/div/ul/div[8]/li/ul/div/a/li/span'''
time.sleep(2)
# 进入店铺列表
driver.find_element_by_xpath('''//*[@id="app"]/div/div[2]/section/div/div[1]/div/button/i''').click()



sheng = driver.find_element_by_xpath('''//*[@id="app"]/div/div[2]/section/div/form/div[11]/div/div/div/div/div[1]/div/div/label[1]/select''')
sheng_list = sheng.find_element_by_xpath('''option''')
sheng_list[0].click()

shi = driver.find_element_by_xpath('''//*[@id="app"]/div/div[2]/section/div/form/div[11]/div/div/div/div/div[1]/div/div/label[2]/select''')
shi_list = sheng.find_element_by_xpath('''option''')
shi_list[0].click()

qu = driver.find_element_by_xpath('''//*[@id="app"]/div/div[2]/section/div/form/div[11]/div/div/div/div/div[1]/div/div/label[3]/select''')
qu_list = sheng.find_element_by_xpath('''option''')
qu_list[0].click()

i = 1
while i <69:
    driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/form/div[11]/div/div/div[{}]/div/div[2]/button/span'.format(i)).click()

    sheng = driver.find_element_by_xpath(
        '''//*[@id="app"]/div/div[2]/section/div/form/div[11]/div/div/div[{}]/div/div[1]/div/div/label[1]/select'''.format(i))
    sheng_list = sheng.find_element_by_xpath('''option''')
    sheng_list[0].click()

    shi = driver.find_element_by_xpath(
        '''//*[@id="app"]/div/div[2]/section/div/form/div[11]/div/div/div/div/div[1]/div/div/label[2]/select''')
    shi_list = sheng.find_element_by_xpath('''option''')
    shi_list[0].click()

    qu = driver.find_element_by_xpath(
        '''//*[@id="app"]/div/div[2]/section/div/form/div[11]/div/div/div/div/div[1]/div/div/label[3]/select''')
    qu_list = sheng.find_element_by_xpath('''option''')
    qu_list[0].click()

    i += 1


driver.quit()

# //*[@id="app"]/div/div[2]/section/div/form/div[11]/div/div/div[1]/div/div[2]/button/span
# //*[@id="app"]/div/div[2]/section/div/form/div[11]/div/div/div[2]/div/div[2]/button/span
# //*[@id="app"]/div/div[2]/section/div/form/div[11]/div/div/div[3]/div/div[2]/button/span

