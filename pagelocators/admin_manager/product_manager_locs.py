"""
======================
Author: 柠檬班-小简
Time: 2022/7/18 21:24
Project: day8_PO_v3
Company: 湖南零檬信息技术有限公司
======================
"""
from selenium.webdriver.common.by import By


# 新增产品的按钮
add_prod_button = (By.XPATH,'//span[text()="新增"]')

# =========  新增产品弹出框当中的元素定位  ===============
# 商品+号
add_prod_image_button = (By.XPATH,'//div[@class="mul-pic-upload"]//i[@class="el-icon-plus"]')
# 选择图片选项
select_image_tab = (By.XPATH,'//div[@id="tab-pick"]')
# 搜索图片输入框
search_image_input = (By.XPATH,'//input[@placeholder="图片名称"]')
# 查询按钮
search_button = (By.XPATH,'//span[text()="查询"]')
# 选中某个图片
select_one_image = (By.XPATH,'//img[@src="http://mall.lemonban.com:8108/2022/07/b72610b8daa24c89b7b70f79a1dcba7c.jpg"]')
# 确定按钮
select_one_image_sure = (By.XPATH,'//div[@class="el-badge item"]//span[text()="确 定"]')

# 选择产品分类输入框
add_prod_category_input = (By.XPATH,'//div[@class="el-cascader"]//input[@placeholder="请选择"]')
# 选择一级菜单里的食品饮料
select_first_category = [By.XPATH,'//span[text()="{}"]']
# 选择二级类别
select_second_category = [By.XPATH,'//span[text()="{}"]']
# 选择三级类别
select_third_category = [By.XPATH,'//span[text()="{}"]']


# 选择产品分组
add_prod_group = (By.XPATH,'//label[text()="产品分组"]/following-sibling::div//input[@placeholder="请选择"]')
# 选择每日上新
select_daily_new_group = (By.XPATH,'//span[text()="每日上新"]')


# 添加商品库存、售价信息等多个输入框。
add_prod_price = (By.XPATH,'//tr//input[@class="el-input__inner"]')

# 添加运费类型
add_prod_delivery = (By.XPATH,'//button[@type="button"]/preceding-sibling::div//input')
delivery_free = (By.XPATH,'//span[text()="包邮"]')

# 商品介绍 - 中文名称
add_prod_cn_name = (By.XPATH,'//input[@placeholder="商品名称"]')
add_prod_cn_sail_feature = (By.XPATH,'//textarea[@placeholder="产品卖点"]')
# add_prod_desc =

# 确认提交产品
sure_add_prod_button = (By.XPATH,'//button[@class="el-button el-button--primary"]//span[text()="确 定"]')


# 产品列表当中，产品名称元素定位
prod_name_in_prod_list = [By.XPATH, '//tr[@class="el-table__row"]//span[text()="{}"]']