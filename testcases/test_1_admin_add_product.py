"""
======================
Author: 柠檬班-小简
Time: 2022/7/19 15:28
Project: day8_PO_v3
Company: 湖南零檬信息技术有限公司
======================
"""
import pytest
from loguru import logger

from pageobjects.admin_manager.admin_login_page import AdminLoginPage
from pageobjects.admin_manager.common_action import CommonAction
from pageobjects.admin_manager.product_manager import ProductManager

from testdatas.common_datas import admin_accout,verify_code
from testdatas.add_product_datas import add_prod_datas

@pytest.mark.usefixtures("admin_manage_broswer")
class TestAdminAddProduct:
    logger.info("================== 正向用例：添加产品成功  =======================")
    def test_add_product_success(self,admin_manage_broswer):
        driver = admin_manage_broswer
        # 1、登录
        AdminLoginPage(driver).admin_login(*admin_accout, verify_code)
        # 2、切换导航到产品管理
        CommonAction(driver).switch_first_nav_by_name("产品管理").switch_second_nav("产品管理")
        # 3、添加产品。
        ProductManager(driver).add_product_action(**add_prod_datas)
        # 4、断言
        assert ProductManager(driver).prod_name_is_in_prod_lists(add_prod_datas.get("prod_cn_name"))
