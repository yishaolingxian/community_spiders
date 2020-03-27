# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class XiaoquItem(scrapy.Item):
    collection = table = 'community'
    province = scrapy.Field()  # 省
    city = scrapy.Field()  # 市
    district = scrapy.Field()  # 区
    name = scrapy.Field()  # 小区名
    url = scrapy.Field()  # 小区链接
    detail_address = scrapy.Field()  # 所属详细地址
    coord = scrapy.Field()  # 经纬度
    traffic = scrapy.Field()  # 附近交通
    price = scrapy.Field()  # 参考价格
    property_type = scrapy.Field()  # 物业类型
    property_fee = scrapy.Field()  # 物业费
    area = scrapy.Field()  # 总建面积
    house_count = scrapy.Field()  # 总户数
    completion_time = scrapy.Field()  # 竣工时间
    parking_count = scrapy.Field()  # 停车位
    plot_ratio = scrapy.Field()  # 容积率
    greening_rate = scrapy.Field()  # 绿化率
    property_company = scrapy.Field()  # 物业公司
    developers = scrapy.Field()  # 开发商

    pass
