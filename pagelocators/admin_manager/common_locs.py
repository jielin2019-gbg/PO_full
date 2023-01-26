"""
======================
Author: 柠檬班-小简
Time: 2022/7/18 21:01
Project: day8_PO_v3
Company: 湖南零檬信息技术有限公司
======================
"""
from selenium.webdriver.common.by import By
# 左边一级导航栏
first_nav = [By.XPATH,'//div[@class="el-submenu__title"]//span[text()="{}"]']
# 一级导航下的二级导航
second_nav = [By.XPATH,'//ul[@role="menu"]//span[text()="{}"]']