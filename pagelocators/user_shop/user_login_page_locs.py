"""
商城用户登录框页面元素
"""

from selenium.webdriver.common.by import By


#点击登录，弹出登录框
click_login=(By.XPATH,'//a[@class="link-a" and text()="登录"]')
#输入账号
input_uesr=(By.XPATH,'//input[@placeholder="请输入手机号/用户名"]')
#输入密码
input_passwd=(By.XPATH,'//input[@placeholder="请输入密码"]')
#点击登录按钮
login_button=(By.XPATH,'//a[@class="login-button"]')