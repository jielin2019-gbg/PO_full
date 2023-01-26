"""
======================
Author: 柠檬班-小简
Time: 2022/7/15 20:05
Project: py49_web
Company: 湖南零檬信息技术有限公司
======================
"""
from loguru import logger

"""
作用域、前置代码，后置代码，返回
"""
import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def manage_broswer():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://mall.lemonban.com:3344/")
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def refresh_page(manage_broswer):
    manage_broswer.refresh()


@pytest.fixture(scope="class")
def admin_manage_broswer():
    driver = webdriver.Chrome()
    logger.info("访问网址：http://mall.lemonban.com/admin/#/login")
    driver.get("http://mall.lemonban.com/admin/#/login")
    driver.maximize_window()
    yield driver
    driver.quit()
