"""
======================
Author: 柠檬班-小简
Time: 2022/7/15 20:15
Project: py49_web
Company: 湖南零檬信息技术有限公司
======================
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:

    # 登录按钮
    login_link = (By.XPATH, '//a[text()="登录"]')
    # 用户昵称元素
    user_name_link = (By.XPATH, '//a[@class="link-name"]')

    # 为什么在这里不能用webdriver.Chrome()实例化对象。
    # webdriver.Chrome()意味着打开了一个浏览器。如果每个页面类都打开了一个浏览器，那就是多个浏览器了。
    def __init__(self,driver: WebDriver,timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)

    # 点击登录按钮，弹出登录框
    def click_to_enter_login_page(self):
        self.wait.until(EC.visibility_of_element_located(self.login_link))
        self.driver.find_element(*self.login_link).click()

    # 页面中用户名元素是否存在
    def exist_user_name(self):
        try:
            WebDriverWait(self.driver,7).until(EC.visibility_of_element_located(self.user_name_link))
            return True
        except:
            return False

















        