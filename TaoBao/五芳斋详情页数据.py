import openpyxl
import requests
import re
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# from selenium.webdriver.chrome.options import Options
# options = Options()
# prefs = {
#     'profile.default_content_setting_values': {
#         'images': 2,
#         'permissions.default.stylesheet': 2,
#         # 'javascript': 2
#     }
# }
# options.add_experimental_option('prefs', prefs)

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 2}
chrome_options.add_experimental_option("prefs", prefs)


# 读取表格
wb = openpyxl.load_workbook("五芳斋.xlsx")
# 获取所有工作表名
names = wb.sheetnames
# wb.get_sheet_by_name(name) 已经废弃,使用wb[name] 获取指定工作表
wb1 = wb[names[0]]

product_url_list = list()
# print(sheet.iter_rows())
for one_column_data in wb1.iter_rows():
    result = one_column_data[4].value
    product_url_list.append(result)
    print(result)

driver = webdriver.Chrome(chrome_options=chrome_options)
for product_url in product_url_list[47:]:
    num = product_url_list.index(product_url)
    print(num)
    if num == 47:
        print("进入判断")
        driver.get(product_url)
        # time.sleep(2)
        driver.switch_to.frame("sufei-dialog-content")
        time.sleep(1)
        driver.find_element_by_xpath("""//*[@id="fm-login-id"]""").send_keys("18168580698")
        driver.find_element_by_xpath("""//*[@id="fm-login-password"]""").send_keys("ctlove199443")
        time.sleep(1)
        driver.find_element_by_xpath("""//*[@id="login-form"]/div[4]/button""").click()
        # driver.find_element_by_class_name("sufei-dialog-close").click()
        driver.switch_to.default_content()
        time.sleep(2)
    else:
        print("请求页面")
        driver.get(product_url)

        # 月销量
    try:
        # 显性等待 DyListCover-hot class 加载出来20秒，每0.5秒检查一次
        WebDriverWait(driver, 2, 0.5).until(EC.presence_of_element_located((By.CLASS_NAME, "tm-count")))
        count_list = driver.find_elements_by_class_name("tm-count")

        count = count_list[0].text
        print(count)
        if num > 1:
            wb1.cell(row=num + 1, column=6, value=count)
        else:
            wb1.cell(row=1, column=6, value="商品月销量")
            wb1.cell(row=num + 1, column=6, value=count)
    except:
        wb1.cell(row=num + 1, column=6, value="没有显示月销")

    # 配送时间
    try:
        # 显性等待 DyListCover-hot class 加载出来20秒，每0.5秒检查一次
        WebDriverWait(driver, 2, 0.5).until(EC.presence_of_element_located((By.CLASS_NAME, "signText")))
        send_time = driver.find_element_by_class_name("signText").text
        print(send_time)
        if num > 1:
            wb1.cell(row=num + 1, column=7, value=send_time)
        else:
            wb1.cell(row=1, column=7, value="配送时间")
            wb1.cell(row=num + 1, column=7, value=send_time)
    except:
        print("没有显示配送时间")
        if num > 1:
            wb1.cell(row=num + 1, column=7, value="没有显示配送时间")
        else:
            wb1.cell(row=1, column=7, value="配送时间")
            wb1.cell(row=num + 1, column=7, value="没有显示配送时间")

    wb.save("五芳斋.xlsx")
    print("已完成{}条销量纪录".format(num))
    # time.sleep(1)

driver.quit()
