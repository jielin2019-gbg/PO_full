import pytest
from loguru import logger

from pageobjects.user_shop.action_page import OperationPage
from pageobjects.user_shop.public_column import TotalColumns
from pageobjects.user_shop.user_login_page import Userlogin

from testdatas.common_datas import user_accout
from testdatas.add_product_datas import user_order_datas


@pytest.mark.usefixtures('manage_broswer')
class TestPurchasesGoods:
    logger.info("================== 正向用例：添加产品成功  =======================")
    def test_purchases_goods(self,manage_broswer):
        driver=manage_broswer
        #1、登陆商城用户端
        Userlogin(driver).user_login(*user_accout)
        #2、选择商品列表栏目
        TotalColumns(driver).switch_columns("商品列表")
        #3、选择商品下单支付
        OperationPage(driver).operation_page(**user_order_datas)
        # 4、获取订单号
        ele=OperationPage(driver).get_order_number()
        # 5、支付回调
        OperationPage(driver).payment_callback()
        #6、断言
        assert OperationPage(driver).whether_the_order_exists(ele)








