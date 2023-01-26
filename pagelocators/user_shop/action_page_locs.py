"""
用户页面操作
"""
#输入框：输入商品名称

from selenium.webdriver.common.by import By
#请输入商品名称框
search_box=(By.XPATH,'//input[@placeholder="请输入商品名称"]')
#点击搜索
click_search=(By.XPATH,'//input[@value="搜索"]')
#点击要下单的商品
select_product=[By.XPATH,'//div[text()="{}"]']
#点击立即购买
click_to_buy=(By.XPATH,'//a[text()="立即购买"]')


#点击添加地址的+，弹出收件信息框
add_address=(By.XPATH,'//div[text()="+"]')
#点击收件人输入框
addressee=(By.XPATH,'//input[@maxlength="15"]')
#点击手机号码输入框
phone_number=(By.XPATH,'//input[@maxlength="11"]')

#点击选择省、市、区
province_and_city=(By.XPATH,'//input[@class="el-input__inner"]')

province=[By.XPATH, '//li[text()="{}"]']

city=[By.XPATH, '//li[text()="{}"]']

area=[By.XPATH, '//li[text()="{}"]']
# for i in eles:
#     i.click()
#     time.sleep(1)
#     if i == eles[0]:
#         driver.find_element(By.XPATH, '//li[text()="湖南省"]').click()
#     elif i == eles[1]:
#         driver.find_element(By.XPATH, '//li[text()="长沙市"]').click()
#     else:
#         driver.find_element(By.XPATH, '//li[text()="岳麓区"]').click()


#点击详细地址输入框
detailed_address=(By.XPATH,'//input[@maxlength="50"]')
#点击保存收件人信息按钮
click_save_button=(By.XPATH, '//a[text()="保存收件人信息"]')


#点击提交订单按钮
place_order=(By.XPATH, '//a[text()="提交订单"]')
#点击微信支付

wechat_payment=(By.XPATH, '//span[text()="微信支付"]')
#点击立即支付按钮
pay_immediately=(By.XPATH, '//a[text()="立即付款"]')

#点击个人中心
personal_center=(By.XPATH, '//span[text()="个人中心"]')
#点击我的定单
my_order=(By.XPATH, '//a[text()="我的订单"]')
#点击待支付
to_be_paid=(By.XPATH,'//span[contains(text(),"待支付")]')

#获取订单号
order_num=(By.XPATH, '//span[@class="num"]')

#点击待发货
to_be_shipped=(By.XPATH,'//span[contains(text(),"待发货")]')


#验证订单号
verify_order_number=[By.XPATH, '//span[text()="{}"]']

#点单号
#//span[text()="1551002196014010368"]