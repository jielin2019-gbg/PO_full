"""
======================
Author: 柠檬班-小简
Time: 2022/7/18 20:41
Project: day8_PO_v3
Company: 湖南零檬信息技术有限公司
======================
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pagelocators.admin_manager import admin_login_page_locs as locs
from tools.basepage import Basepage


class AdminLoginPage:

    def __init__(self, driver: WebDriver, timeout=10):
        # self.driver = driver
        # self.wait = WebDriverWait(self.driver, timeout)
        self.bp=Basepage(driver,timeout)

    def admin_login(self,user,passwd,verify_code):
        # self.wait.until(EC.visibility_of_element_located(locs.login_button))
        # self.driver.find_element(*locs.user_input).send_keys(user)
        # self.driver.find_element(*locs.user_passwd).send_keys(passwd)
        # self.driver.find_element(*locs.verify_code).send_keys(verify_code)
        # self.driver.find_element(*locs.login_button).click()
        self.bp.input_text(locs.user_input, "管理员登录页面_输入用户名", "student")
        self.bp.input_text(locs.user_passwd, "管理员登录页面_输入密码", "123456a")
        self.bp.input_text(locs.verify_code, "管理员登录页面_输入万能验证码", "lemon")
        self.bp.click_ele(locs.login_button, "管理员登录页面_提交登录")