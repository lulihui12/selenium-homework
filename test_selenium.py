'''
使用复用浏览器技术获取企业微信的cookie，点击添加成员
'''
import json
from typing import List, Dict

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By


class Testchat:
    def setup(self):
        # 声明一个变量，设置为chromeoptions
        chrome_opts = webdriver.ChromeOptions()
        # 设置chrome debugging代理，端口号保持一致 ：Google\ Chrome -remote-debugging-port=9222
        chrome_opts.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=chrome_opts)
        self.driver.get("https://work.weixin.qq.com/")
        # 隐式等待
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_chat(self):
        # 获取cookies并给到变量
        cookies = self.driver.get_cookies()
        # 保存到文件  注：open之后，才可以读写
        with open("cookies.txt", 'w') as f:
            json.dump(cookies, f)
        # 读取文件
        with open("cookies.txt", 'r') as f:
            cookies: List[Dict] = json.load(f)
        for cookie in cookies:
            if "expiry" in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.find_element(By.CSS_SELECTOR, '.index_service_cnt_item_title').click()
        self.driver.find_element(By.CSS_SELECTOR, "#username").send_keys("tester")
        self.driver.find_element(By.CSS_SELECTOR, "#memberAdd_acctid").send_keys('12323232323')
        self.driver.find_element(By.CSS_SELECTOR, "#memberAdd_phone").send_keys('13381037751')
        self.driver.find_element(By.CSS_SELECTOR, "#memberAdd_telephone").send_keys('021-9898383')
        self.driver.find_element(By.CSS_SELECTOR, "#memberAdd_mail").send_keys('12343555@qq.com')
        self.driver.find_element(By.CSS_SELECTOR, "#memberEdit_address").send_keys("北京海淀的呀呀呀呀呀")
        self.driver.find_element(By.CSS_SELECTOR, "#memberAdd_title").send_keys("技术总监")
