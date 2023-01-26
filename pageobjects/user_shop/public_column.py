"""
菜单栏
"""
import time

from selenium.webdriver.remote.webdriver import WebDriver
from tools.basepage import Basepage
from pagelocators.user_shop import public_column_locs as locs


class TotalColumns:

    def __init__(self, driver: WebDriver, timeout=10):
        self.bp = Basepage(driver, timeout)

    def switch_columns(self,column):
        locs.menu_bar[1]=locs.menu_bar[1].format(column)
        time.sleep(2)
        self.bp.click_ele(locs.menu_bar, "切换菜单栏目")





