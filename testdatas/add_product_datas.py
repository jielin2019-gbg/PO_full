"""
======================
Author: 柠檬班-小简
Time: 2022/7/19 15:00
Project: day8_PO_v3
Company: 湖南零檬信息技术有限公司
======================
"""
from faker import Faker

add_prod_datas = {
    # 上传图片的路径
    # 产品图片
    "image_name":"my_dog",
    # 产品类别
    "prod_category_list": ["食品饮料", "食品", "休闲食品"],
    # 市场价、销售价、库存、商品编码、商品重量、商品体积
    "sku_info_list":["120", "100", "100", Faker().random_int(min=1000000000, max=9999999999), "10", "20"],
    # 产品中文名称
    "prod_cn_name": "py49UI自动化-{}".format(Faker().pystr(min_chars=5,max_chars=10)),
    # 产品卖点
    "prod_cn_sail_feature":"每当学习犯困时，吃一口，瞬间清醒"
    # 产品详细描述
}

user_order_datas={
    "product_name":"测试衣服1",
    "name":"柠檬班",
    "phone":"15116660400",
    "city_list":["湖南省","长沙市","岳麓区"],
    "address":"文轩路27号麓谷钰园F3栋13楼1303室"

}