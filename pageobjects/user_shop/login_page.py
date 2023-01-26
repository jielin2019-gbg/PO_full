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


class LoginPage:

    # 用户名输入框
    user_input = (By.XPATH, '//input[@placeholder="请输入手机号/用户名"]')
    # 密码输入框
    passwd_input = (By.XPATH, '//input[@placeholder="请输入密码"]')
    # 登录按钮
    login_button = (By.XPATH, '//a[@class="login-button"]')
    # 错误提示信息元素 - 用户名或者密码错误的
    error_msg_p = (By.XPATH, '//div[@role="alert"]//p')

    def __init__(self,driver: WebDriver,timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)

    # 登录操作
    def login(self,user,passwd):
        self.wait.until(EC.visibility_of_element_located(self.login_button))
        self.driver.find_element(*self.user_input).send_keys(user)
        self.driver.find_element(*self.passwd_input).send_keys(passwd)
        self.driver.find_element(*self.login_button).click()

    # 获取异常操作下的页面提示信息
    def get_error_message(self):
        self.wait.until(EC.visibility_of_element_located(self.error_msg_p))
        return self.driver.find_element(*self.error_msg_p).text
