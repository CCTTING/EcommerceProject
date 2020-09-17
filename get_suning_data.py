from selenium import webdriver
import ast

file_url_list = ['url健康禽蛋.txt', 'url新鲜水果.txt', 'url海鲜水产.txt', 'url牛奶乳品.txt', 'url精选肉类.txt', 'url速冻冷饮.txt']

driver = webdriver.Chrome()

datas_list = list()

url_list = list()
for file_url in file_url_list[3:-1]:
    print(file_url)
    with open(file_url, 'r') as f:
        result = f.read()
    url = ast.literal_eval(result)
    print(url)

    for i in url:
        # 打开登录页面
        driver.get(i)
        driver.implicitly_wait(5)
        phone_list = list()

        # 商品标题
        a = driver.find_element_by_xpath('''//*[@id="itemDisplayName"]''').text
        # print(a)
        phone_list.append(a)

        # print(phone_list)

        # 商品图片5张
        # 第一张
        image = driver.find_element_by_xpath('''//*[@id="bigImg"]/img''').get_attribute('src')
        phone_list.append(image)
        try:
            # 第二张
            driver.find_element_by_xpath('''//*[@id="imgZoom"]/div[2]/div/ul/li[2]/a/img''').click()
            image = driver.find_element_by_xpath('''//*[@id="bigImg"]/img''').get_attribute('src')
            phone_list.append(image)
            # 第三张
            driver.find_element_by_xpath('''//*[@id="imgZoom"]/div[2]/div/ul/li[3]/a/img''').click()
            image = driver.find_element_by_xpath('''//*[@id="bigImg"]/img''').get_attribute('src')
            phone_list.append(image)
            # 第四张
            driver.find_element_by_xpath('''//*[@id="imgZoom"]/div[2]/div/ul/li[4]/a/img''').click()
            image = driver.find_element_by_xpath('''//*[@id="bigImg"]/img''').get_attribute('src')
            phone_list.append(image)
            # 第五张
            driver.find_element_by_xpath('''//*[@id="imgZoom"]/div[2]/div/ul/li[5]/a/img''').click()
            image = driver.find_element_by_xpath('''//*[@id="bigImg"]/img''').get_attribute('src')
            phone_list.append(image)
        except:
            for i in range(4):
                phone_list.append(image)

        # print(phone_list)

        # 商品属性
        sx = '50g'
        phone_list.append(sx)
        # 商品税率
        sl = '9'
        phone_list.append(sl)
        # # '''//*[@id="mainPrice"]/dl[1]/dd/span[1]'''
        # '''//*[@id="mainPrice"]/dl[1]/dd/span[1]'''
        # '''//*[@id="mainPrice"]/dl[2]/dd/span[1]'''
        # 商品划线价格
        try:
            price = driver.find_element_by_xpath('''//*[@id="mainPrice"]/dl[1]/dd/span[1]''').text
            price = price[1:-3]
            # print(price)
            phone_list.append(price)
        except:
            price = driver.find_element_by_xpath('''//*[@id="mainPrice"]/dl[2]/dd/span[1]''').text
            price = price[1:-3]
            # print(price)
            phone_list.append(price)

        # 商品销售价格
        mail_price = int(price) + 10
        phone_list.append(mail_price)

        for num in range(0, len(url)):
            if url[num] == i:
                print('目前是第{}个商品信息'.format(num))

        datas_list.append(phone_list)

        # 保存数据到datas.text
        file_name = file_url.split('.')
        # print(file_name[0])
        with open('datas-'+file_name[0]+'.txt', 'w') as f:
            f.write(str(datas_list))

    print(datas_list)

    driver.quit()
