import random
import ast
import json
from selenium import webdriver
import time
import requests

with open('datas-url海鲜水产.txt', 'r') as f:
    result = f.read()
datas_list = ast.literal_eval(result)
# datas_list = result

# datas_list = json.loads(result)
# print(datas_list)
# time.sleep(60)

driver = webdriver.Chrome()

# # 测试地址
# url = 'http://yr-stage.yurun.com/mall-sys-stage/#/login'
# 生产地址
url = 'https://p.yurun.com/#/index'
# 打开登录页面
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(5)
time.sleep(2)
username = driver.find_element_by_xpath('''//*[@id="app"]/div/form/div[1]/div/div/input''')
username.clear()
username.send_keys('abcd')
password = driver.find_element_by_xpath('''//*[@id="app"]/div/form/div[2]/div/div/input''')
password.clear()
password.send_keys('a123456')
driver.find_element_by_xpath('''//*[@id="app"]/div/form/div[3]/div/div[1]/input''').click()
time.sleep(10)
# 点击登录按钮
# //*[@id="app"]/div/form/div[4]/div/button
driver.find_element_by_xpath('''//*[@id="app"]/div/form/div[4]/div/button/span/span''').click()
time.sleep(4)
# 登录成功
# 点击商品管理
# //*[@id="app"]/div/div[1]/div[2]/div[1]/div/ul/div[3]/li/div
driver.find_element_by_xpath('''//*[@id="app"]/div/div[1]/div[2]/div[1]/div/ul/div[3]/li/div''').click()
# 进入商品列表
driver.find_element_by_xpath('''//*[@id="app"]/div/div[1]/div[2]/div[1]/div/ul/div[3]/li/ul/div[3]/a/li''').click()
time.sleep(5)
num = 1
header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
}

for data_list in datas_list[21:-1]:

    # 进入发布页面
    driver.find_element_by_xpath('''//*[@id="app"]/div/div[2]/section/div/form/div[9]/div/button[2]''').click()
    time.sleep(2)
    # 商品品类
    driver.find_element_by_xpath('''//*[@id="app"]/div/div[2]/section/div/form/div[1]/div/div/div/input''').click()
    # 选择分类1
    ul1 = driver.find_element_by_xpath('''//*[@class="el-popper el-cascader__dropdown"]/div[1]/div[1]/div[1]/ul''')
    lis_list = ul1.find_elements_by_xpath('li')
    lis_list[0].click()
    # 选择分类2
    ul2 = driver.find_element_by_xpath('''//*[@class="el-popper el-cascader__dropdown"]/div[1]/div[2]/div[1]/ul''')
    lis_list = ul2.find_elements_by_xpath('li')
    lis_list[0].click()
    # 选择分类3
    ul3 = driver.find_element_by_xpath('''//*[@class="el-popper el-cascader__dropdown"]/div[1]/div[3]/div[1]/ul''')
    lis_list = ul3.find_elements_by_xpath('li')
    lis_list[0].click()

    # 输入商品标题
    product_title = data_list[0]
    # print(product_title)
    driver.find_element_by_xpath('''//*[@id="app"]/div/div[2]/section/div/form/div[2]/div/div/input''').send_keys(
        product_title)

    # 输入商品副标题
    commodity_subtitle = data_list[0]
    driver.find_element_by_xpath('''//*[@id="app"]/div/div[2]/section/div/form/div[3]/div/div/input''').send_keys(
        commodity_subtitle)

    # 选择定价标准
    driver.find_element_by_xpath(
        '''//*[@id="app"]/div/div[2]/section/div/form/div[4]/div/div/label[2]/span[1]/span''').click()

    # 添加商品图片
    for image_url in data_list[1:6]:
        try:
            response = requests.get(image_url, headers=header)
            random_number_pic = ''.join(str(random.choice(range(10))) for _ in range(5))
            pic_name = str(random_number_pic) + '.jpg'
            url_path = '/Users/caoting/PycharmProjects/pyproject02/' + pic_name
            # print(url_path)
            with open(pic_name, 'wb') as f:
                f.write(response.content)
            time.sleep(1)
            driver.find_element_by_name('file').send_keys(url_path)
            time.sleep(1)
        except:
            continue

    # 添加商品属性
    driver.find_element_by_xpath(
        '''//*[@id="app"]/div/div[2]/section/div/form/div[6]/div/div[2]/div/div/input''').send_keys(data_list[6])
    driver.find_element_by_xpath('''//*[@id="app"]/div/div[2]/section/div/form/div[6]/div/div[2]/div/button''').click()
    time.sleep(1)

    # 添加商品税率
    commodity_tax_rate = data_list[7]
    driver.find_element_by_xpath('''//*[@id="app"]/div/div[2]/section/div/form/div[7]/div/div/input''').send_keys(
        commodity_tax_rate)

    # 添加分类编码
    # random_number = ''.join(str(random.choice(range(10))) for _ in range(19))
    # # print(random_number)
    # classification_code = str(random_number)
    classification_code = '1030107019900000000'
    driver.find_element_by_xpath('''//*[@id="app"]/div/div[2]/section/div/form/div[8]/div/div/input''').send_keys(
        classification_code)

    # //*[@id="app"]/div/div[2]/section/div/form/div[13]/div[2]/div/div[3]/table/tbody/tr/td[3]/div/div[1]/input
    # //*[@id="app"]/div/div[2]/section/div/form/div[13]/div[2]/div/div[3]/table/tbody/tr/td[2]/div/div[1]/input

    # 添加商品划线价格
    crossed_commodity_price = data_list[9]
    driver.find_element_by_xpath(
        '''//*[@id="app"]/div/div[2]/section/div/form/div[9]/div[2]/div/div[3]/table/tbody/tr/td[2]/div/div[1]/input''').send_keys(
        crossed_commodity_price)

    # 添加商品销售价格
    selling_price_of_goods = data_list[8]
    driver.find_element_by_xpath(
        '''//*[@id="app"]/div/div[2]/section/div/form/div[9]/div[2]/div/div[3]/table/tbody/tr/td[3]/div/div[1]/input''').send_keys(
        selling_price_of_goods)

    # 添加商品图片
    response = requests.get(data_list[1], headers=header)
    random_number_pic1 = ''.join(str(random.choice(range(10))) for _ in range(5))
    pic_name1 = str(random_number_pic1) + '.jpg'
    url_path1 = '/Users/caoting/PycharmProjects/pyproject02/' + pic_name1
    # print(url_path1)
    with open(pic_name1, 'wb') as f:
        f.write(response.content)
    time.sleep(1)
    driver.find_element_by_xpath(
        '''//*[@id="app"]/div/div[2]/section/div/form/div[9]/div[2]/div/div[3]/table/tbody/tr/td[4]/div/div/div/input''').send_keys(
        url_path1)
    time.sleep(1)

    # 商品详情
    # response = requests.get('http://imgservice.suning.cn/uimg1/b2c/atmosphere/X16WcIA5puMQ7_1Pst9aYA.jpg_800w_800h_4e')
    driver.find_element_by_xpath(
        '''//*[@id="app"]/div/div[2]/section/div/form/div[10]/div/div[1]/div[2]/div[2]/div[1]''').send_keys(
        data_list[0])
    time.sleep(2)
    # print(driver.find_element_by_xpath(
    #     '''//*[@id="app"]/div/div[2]/section/div/form/div[14]/div/div[1]/div[2]/div[2]/div[1]''').text)

    # 点击提交
    driver.find_element_by_xpath('''//*[@id="app"]/div/div[2]/section/div/form/div[11]/div/div/button''').click()

    print('已添加第{}个商品'.format(num))
    num += 1
    time.sleep(5)

driver.quit()

# //*[@id="app"]/div/div[2]/section/div/form/div[13]/div[2]
# //*[@id="app"]/div/div[2]/section/div/form/div[13]/div[2]/div/div[3]/table/tbody/tr/td[1]/div/div[1]/input
