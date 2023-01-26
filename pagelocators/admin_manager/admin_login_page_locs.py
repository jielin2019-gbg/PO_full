"""
======================
Author: 柠檬班-小简
Time: 2022/7/18 20:54
Project: day8_PO_v3
Company: 湖南零檬信息技术有限公司
======================
"""
from selenium.webdriver.common.by import By


# 用户名输入框
user_input = (By.XPATH,'//input[@placeholder="用户名"]')
# 用户密码
user_passwd = (By.XPATH,'//input[@placeholder="密码"]')
# 验证码
verify_code = (By.XPATH,'//input[@placeholder="验证码"]')
# 登录按钮
login_button = (By.XPATH,'//input[@value="登录"]')