"""
用户登录
"""
from selenium.webdriver.remote.webdriver import WebDriver
from tools.basepage import Basepage
from pagelocators.user_shop import user_login_page_locs as locs

class Userlogin:

    def __init__(self, driver: WebDriver, timeout=10):
        self.bp = Basepage(driver, timeout)

    def user_login(self,uesr_name,pass_wd):
        self.bp.click_ele(locs.click_login,"点击登录，弹出登录框")
        self.bp.input_text(locs.input_uesr,"输入用户名",uesr_name)
        self.bp.input_text(locs.input_passwd,"输入密码",pass_wd)
        self.bp.click_ele(locs.login_button,"点击登录按钮")