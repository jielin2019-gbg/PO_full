"""
======================
Author: 柠檬班-小简
Time: 2022/7/18 21:43
Project: day8_PO_v3
Company: 湖南零檬信息技术有限公司
======================
"""
import time

from faker import Faker
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pagelocators.admin_manager import product_manager_locs as locs
from tools.basepage import Basepage

class ProductManager:

    def __init__(self, driver: WebDriver, timeout=10):
        self.bp = Basepage(driver, timeout)

    def add_product_action(self,image_name,prod_category_list,sku_info_list,prod_cn_name,prod_cn_sail_feature):
        """
        :param image_name:
        :param prod_category_list:
        :param sku_info_list:
        :param prod_cn_name:
        :param prod_cn_sail_feature:
        :return:
        """
        # 0、点击添加产品按钮，弹出添加页面。
        # self.wait.until(EC.visibility_of_element_located(locs.add_prod_button))
        # self.driver.find_element(*locs.add_prod_button).click()
        self.bp.click_ele(locs.add_prod_button,"点击新增按钮，弹出弹出添加页面")
        # 1、添加图片
        self._add_product_image(image_name)
        # 2、选择产品分类
        self._set_product_category(*prod_category_list)
        # 3、选择产品分组
        self._set_product_group()
        # 4、设置价格、库存、编码、大小、重量
        self._set_product_sku_info(sku_info_list)
        # 5、设置运费模式
        self._set_product_devivery()
        # 6、设置产品中文名称、卖点
        # self.driver.find_element(*locs.add_prod_cn_name).send_keys(prod_cn_name)
        # self.driver.find_element(*locs.add_prod_cn_sail_feature).send_keys(prod_cn_sail_feature)
        self.bp.input_text(locs.add_prod_cn_name,"设置产品名称",prod_cn_name)
        self.bp.input_text(locs.add_prod_cn_sail_feature, "设置产品卖点", prod_cn_sail_feature)
        # 7、提交添加操作。
        # self.driver.find_element(*locs.sure_add_prod_button).click()
        self.bp.click_ele(locs.sure_add_prod_button,"点击确定添加产品")

    def prod_name_is_in_prod_lists(self, prod_name):
        locs.prod_name_in_prod_list[1] = locs.prod_name_in_prod_list[1].format(prod_name)
        return self.bp.page_is_contains_ele(locs.prod_name_in_prod_list, "产品管理_产品列表_产品名称是否存在于第一个")

    def _add_product_image(self,image_name):
        self.bp.click_ele(locs.add_prod_image_button,"点击添加商品图品+号")
        self.bp.click_ele(locs.select_image_tab, "点击选中图片选项")
        self.bp.input_text(locs.search_image_input, "搜索框输入图片名称",image_name)
        self.bp.click_ele(locs.search_button, "点击搜索按钮")
        self.bp.click_ele(locs.select_one_image,"点击选中图片")
        self.bp.click_ele(locs.select_one_image_sure, "确定选择图片")

    def _set_product_group(self,group_name="每日上新"):
        self.bp.click_ele(locs.add_prod_group,'点击产品分组输入框')
        self.bp.click_ele(locs.select_daily_new_group, '点击每日上新')

    def _set_product_devivery(self,delivery_mode="包邮"):
        self.bp.click_ele(locs.add_prod_delivery, '点击运费设置输入框')
        self.bp.click_ele(locs.delivery_free, '点击选择包邮')

    def _set_product_sku_info(self,sku_info_list):
        """
        输入商品的 市场价、销售价、库存、商品编码、商品重量、商品体积
        :param sku_info_list:
        :return:
        """
        eles =self.bp.get_elements(locs.add_prod_price, "添加产品_获取市场价+销售价+库存+商品编码+商品重量+商品体积输入框")
        for index, i in enumerate(eles):
            i.clear()
            time.sleep(1)
            i.send_keys(sku_info_list[index])

    def _set_product_category(self,first_category_name, second_category_name,third_category_name):
        """
        选择产品的分类 -- 一级分类，二级分类，三级分类。
        :param first_category_name:
        :param second_category_name:
        :param third_category_name:
        :return:
        """
        locs.select_first_category[1] = locs.select_first_category[1].format(first_category_name)
        locs.select_second_category[1] = locs.select_second_category[1].format(second_category_name)
        locs.select_third_category[1] = locs.select_third_category[1].format(third_category_name)

        self.bp.click_ele(locs.add_prod_category_input,"点击产品分类输入框")
        self.bp.click_ele(locs.select_first_category, "点击选择产品一级分类")
        self.bp.click_ele(locs.select_second_category, "点击选择产品二级分类")
        self.bp.click_ele(locs.select_third_category, "点击选择产品三级分类")
        # 收起分类
        # self.driver.find_element(*locs.add_prod_category_input).click()
        self.bp.click_ele(locs.add_prod_category_input,"点击收起产品分类输入框")
