from selenium import webdriver
import time
import scroll_to_bottom

def get_urls():
    keyword = ['牛奶乳品']
    url = 'https://search.suning.com/{}/'
    driver = webdriver.Chrome()

    driver.get(url.format(keyword[0]))

    # driver.find_element_by_xpath('''//*[@id="pop418"]/a''').click()
    time.sleep(1)

    # ————————————————————————————————————————————————
    # 自动滑动滚轮到底部
    # 执行这段代码，会获取到当前窗口总高度
    js = "return action=document.body.scrollHeight"
    # 初始化现在滚动条所在高度为0
    height = 0
    # 当前窗口总高度
    new_height = driver.execute_script(js)

    while height < new_height:
        # 将滚动条调整至页面底部
        for i in range(height, new_height, 100):
            driver.execute_script('window.scrollTo(0, {})'.format(i))
            time.sleep(0.5)
        height = new_height
        time.sleep(2)
        new_height = driver.execute_script(js)
    # ——————————————————————————————————————————————————————————————————
    print('来到底部')
    time.sleep(2)

    ul = driver.find_element_by_xpath('''//*[@id="product-list"]/ul''')
    li_list = ul.find_elements_by_xpath('li')
    print(li_list)
    url_list = list()
    for i in li_list:
        a = i.find_element_by_xpath('./div/div/div/div/a')
        href = a.get_attribute('href')
        url_list.append(href)
        print(href)
    print(url_list)

    with open('url'+keyword[0]+'.txt','w') as f:
        f.write(str(url_list))

    driver.quit()

get_urls()

