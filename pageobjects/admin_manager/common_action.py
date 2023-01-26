"""
======================
Author: 柠檬班-小简
Time: 2022/7/18 21:03
Project: day8_PO_v3
Company: 湖南零檬信息技术有限公司
======================
"""
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pagelocators.admin_manager import common_locs as locs
from tools.basepage import Basepage
class CommonAction:

    def __init__(self, driver: WebDriver, timeout=10):
        # self.driver = driver
        # self.wait = WebDriverWait(self.driver, timeout)
        self.bp = Basepage(driver, timeout)

    def switch_first_nav_by_name(self,nav_name):
        locs.first_nav[1] = locs.first_nav[1].format(nav_name)
        self.bp.click_ele(locs.first_nav,"切换产品管理一级导航")
        return self

    def switch_second_nav(self,nav_name):
        locs.second_nav[1] = locs.second_nav[1].format(nav_name)
        self.bp.click_ele(locs.second_nav, "切换产品管理二 级导航")
        return self