"""
用户操作
"""
import time
import requests

from selenium.webdriver.remote.webdriver import WebDriver
from tools.basepage import Basepage
from pagelocators.user_shop import action_page_locs as locs

class OperationPage:

    def __init__(self, driver: WebDriver, timeout=10):
        self.headers = {'locale': 'zh_CN'}
        self.bp = Basepage(driver, timeout)


    def operation_page(self,product_name,name,phone,city_list,address):
        # 1、搜索商品下单购买
        self._order_goods(product_name)
        # 2、添加收件人信息
        #self._add_address(name,phone,city_list,address)
        # 3、提交订单并支付
        self._submit_order_and_pay()

    #1、搜索商品下单购买
    def _order_goods(self,product_name):
        self.bp.input_text(locs.search_box,"搜索商品名称",product_name)
        self.bp.click_ele(locs.click_search,"点击搜索按钮")
        locs.select_product[1]=locs.select_product[1].format(product_name)
        self.bp.click_ele(locs.select_product, "点击要购买的商品")
        self.bp.click_ele(locs.click_to_buy,"点击立即购买")

    #2、添加收件人信息
    def _add_address(self,name,phone,city_list,address):
        self.bp.click_ele(locs.add_address,"点击添加地址+")
        self.bp.input_text(locs.addressee,"输入收件人名字",name)
        self.bp.input_text(locs.phone_number,"输入收件人手机号码",phone)
        self._province_and_city(city_list)#省市区
        self.bp.input_text(locs.detailed_address,"输入详细地址",address)
        self.bp.click_ele(locs.click_save_button, "点击保存")

    #2.1、省市区
    def _province_and_city(self,city_list):
        eles=self.bp.get_elements(locs.province_and_city,"查找省市区输入框")
        locs.province[1]=locs.province[1].format(city_list[0])
        locs.city[1]=locs.city[1].format(city_list[1])
        locs.area[1]=locs.area[1].format(city_list[2])
        for i in eles:
            i.click()
            time.sleep(1)
            if i==eles[0]:
                self.bp.click_ele(locs.province,"选择省级")
            elif i==eles[1]:
                self.bp.click_ele(locs.city, "选择市级")
            else:
                self.bp.click_ele(locs.area, "选择区级")

    #3、提交订单并支付
    def _submit_order_and_pay(self):
        self.bp.click_ele(locs.place_order,"提交订单")
        self.bp.click_ele(locs.wechat_payment, "选择微信支付")
        self.bp.click_ele(locs.pay_immediately, "点击立即支付")

    #4、获取订单号
    def get_order_number(self):
        self.bp.click_ele(locs.personal_center,"打点击个人中心")
        self.bp.click_ele(locs.my_order,"点击我的订单")
        self.bp.click_ele(locs.to_be_paid,"选择待支付")
        ele=self.bp.get_element(locs.order_num,"获取订单号")
        setattr(OperationPage,"order_num",ele.text)
        return ele.text
    #5、支付回调
    def payment_callback(self):
        url="http://mall.lemonban.com:8107/notice/pay/3"
        data={
                "payNo":"{}".format(getattr(OperationPage,"order_num")),
                "bizPayNo":str(int(time.time() * 1000)),
                "isPaySuccess": True
                }
        res=requests.post(url=url,json=data,headers=self.headers)
        print("支付回调:",res.text)

    #订单号是否存在待发货
    def whether_the_order_exists(self,ele):
        self.bp.click_ele(locs.to_be_shipped,"选择待发货")
        locs.verify_order_number[1]=locs.verify_order_number[1].format(ele)
        return self.bp.page_is_contains_ele(locs.verify_order_number,"待发货存在该订单号")








