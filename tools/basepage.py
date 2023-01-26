"""
======================
Author: 柠檬班-小简
Time: 2022/7/20 21:17
Project: day8_PO_v4
Company: 湖南零檬信息技术有限公司
======================
"""
import os
import time
from loguru import logger
from pywinauto.keyboard import SendKeys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tools.settings import page_screenshots_dir


class Basepage:

    def __init__(self, driver: WebDriver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)

    def wait_ele_visible(self, locs, page_action):
        logger.info(f"等待 {locs} 元素可见")
        try:
            self.wait.until(EC.visibility_of_element_located(locs))
        except:
            logger.exception("等待失败！请确认元素定位是否正确，是否在运行过程中发生了改变，是否在iframe当中")
            self.save_page_screenshots(page_action)
            raise

    def get_element(self, locs, page_action):
        """

        :param locs:
        :param page_action:
        :return:
        """
        logger.info(f"查找 {locs} 元素。")
        self.wait_ele_visible(locs, page_action)
        try:
            ele = self.driver.find_element(*locs)
            return ele
        except:
            logger.exception("查找元素失败！请确认元素定位是否正确，是否在运行过程中发生了改变，是否在iframe当中")
            self.save_page_screenshots(page_action)
            raise

    def get_elements(self,locs,page_action):
        logger.info(f"查找匹配 {locs} 所有的元素。")
        try:
            ele = self.driver.find_elements(*locs)
            return ele
        except:
            logger.exception("查找元素失败！请确认元素定位是否正确，是否在运行过程中发生了改变，是否在iframe当中")
            self.save_page_screenshots(page_action)
            raise

    def click_ele(self, locs, page_action):
        self.wait_ele_visible(locs, page_action)
        ele = self.get_element(locs, page_action)
        logger.info(f"对元素 {locs} 进行点击操作。")
        try:
            ele.click()
        except:
            logger.exception("点击元素失败！元素此刻可能不能点击！")
            self.save_page_screenshots(page_action)
            raise

    def input_text(self, locs, page_action, *value):
        if isinstance(locs, (list,tuple)):
            self.wait_ele_visible(locs, page_action)
            ele = self.get_element(locs, page_action)
        else:
            ele = locs
        self.wait_ele_visible(locs, page_action)
        ele = self.get_element(locs, page_action)
        logger.info(f"对元素 {locs } 输入值 {value}。")
        try:
            ele.send_keys(*value)
        except:
            logger.exception("输入失败！请确认元素是否可输入")
            self.save_page_screenshots(page_action)
            raise  TypeError("输入数据错误")

    def save_page_screenshots(self, page_action):
        cur_date = time.strftime("%Y%m%d", time.localtime())
        cur_time = time.strftime("%H%M%S", time.localtime())
        filename = "{}_{}_{}.png".format(cur_date, page_action, cur_time)
        filepath = os.path.join(page_screenshots_dir, filename)
        logger.info(f"将截图文件保存至：{filepath}")
        self.driver.save_screenshot(filepath)

    def upload_file(self,locs, page_action,file_path):
        self.click_ele(locs, page_action)
        logger.info(f"要上传的文件路径{file_path}。")
        try:
            SendKeys(fr"{file_path}")
            SendKeys('{ENTER}')
        except:
            logger.exception("文件上传失败")
            self.save_page_screenshots(page_action)

    def page_is_contains_ele(self, locs, page_action, timeout=7):
        logger.info(f"判断元素 {locs} 是否存在于页面当中。等待元素可见最大时长为：{timeout}")
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locs))
            logger.info("元素存在页面当中且可见。")
            return True
        except:
            logger.warning("元素不存在于页面当中。")
            self.save_page_screenshots(page_action)
            return False


if __name__ == '__main__':
    from selenium import webdriver
    from pagelocators.admin_manager import admin_login_page_locs as locs

    driver = webdriver.Chrome()
    bp = Basepage(driver)
    driver.get("http://mall.lemonban.com/admin/#/login")
    bp.input_text(locs.user_input, "管理员登录页面_输入用户名", "student")
    bp.input_text(locs.user_passwd, "管理员登录页面_输入密码", "123456a")
    bp.input_text(locs.verify_code, "管理员登录页面_输入万能验证码", "lemon")
    bp.click_ele(locs.login_button, "管理员登录页面_提交登录")
    time.sleep(4)
    driver.quit()