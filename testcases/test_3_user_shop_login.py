"""
======================
Author: 柠檬班-小简
Time: 2022/7/11 21:56
Project: py49_web
Company: 湖南零檬信息技术有限公司
======================
"""
import time

"""
用例： 前置、步骤、结果
功能用例跟自动化用例有什么区别？？
执行的时候区别：
    手工点点点的时候，你的数据是随机的，临时制造。前置没有就临时去造。
    自动化点点的时候：数据一定要是现成的可用的！！前置环境也是要现成的准备好的！！数据是要多次重复执行！！

断言：如何从手工的角度，转换成代码角度，一定要具体化，期望的页面效果。
自动化测试的帐号/环境：都是可以独立的。

"""
import pytest
from pageobjects.user_shop.home_page import HomePage
from pageobjects.user_shop.login_page import LoginPage

error_data = [
    {"user":("18684720553","123456789"),"check":"账号或密码不正确"},
    {"user":("186847205","123456789"),"check":"账号或密码不正确"}
]

class TestLogin:

    @pytest.mark.usefixtures("manage_broswer")
    @pytest.mark.usefixtures("refresh_page")
    @pytest.mark.parametrize("case",error_data)
    def test_login_failed_wrong_passwd(self,manage_broswer,case):
        driver = manage_broswer
        # 步骤是什么,涉及到的数据是什么？ 输入用户名和密码，点登录。帐号是数据。
        # 首页 - 点击登录按钮，进入登录小页面。
        # 登录页面 - 输入用户名密码，点击登录。
        HomePage(driver).click_to_enter_login_page()
        LoginPage(driver).login(*case["user"])
        # 期望的结果是什么 -- 登录成功？从代码角度而言什么是登录成功？？ -- 用户名元素可见于页面。
        error_message = LoginPage(driver).get_error_message()
        assert error_message == case["check"]
        time.sleep(5)

    # @pytest.mark.usefixtures("manage_broswer")
    # def test_login_failed_wrong_user(self, manage_broswer):
    #     driver = manage_broswer
    #     # 步骤是什么,涉及到的数据是什么？ 输入用户名和密码，点登录。帐号是数据。
    #     # 首页 - 点击登录按钮，进入登录小页面。
    #     # 登录页面 - 输入用户名密码，点击登录。
    #     HomePage(driver).click_to_enter_login_page()
    #     LoginPage(driver).login("18684720", "123456789")
    #     # 期望的结果是什么 -- 登录成功？从代码角度而言什么是登录成功？？ -- 用户名元素可见于页面。
    #     error_message = LoginPage(driver).get_error_message()
    #     assert error_message == "账号或密码不正确"