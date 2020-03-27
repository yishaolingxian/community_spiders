# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from openpyxl import Workbook
import pymysql


class XiaoquPipeline(object):
    def process_item(self, item, spider):
        return item


class ExcelPipeline(object):
    def __init__(self):
        self.wb = Workbook()
        self.ws = self.wb.active
        self.ws.append(['省', '市', '区', '小区名', '小区详情页链接', '详细地址', '经纬度', '交通',
                        '参考价格', '物业类型', '物业费', '总建面积', '总户数', '竣工时间', '停车位', '容积率', '绿化率',
                        '物业公司', '开发商'])

    def process_item(self, item, spider):
        line = [item['province'], item['city'], item['district'], item['name'], item['url'], item['detail_address'],
                item['coord'], item['traffic'], item['price'], item['property_type'],
                item['property_fee'], item['area'], item['house_count'], item['completion_time'], item['parking_count'],
                item['plot_ratio'], item['greening_rate'], item['property_company'], item['developers']]
        self.ws.append(line)
        # keys = spider.settings.get('KEYS')
        self.wb.save('../小区' + '.xlsx')
        return item


class MysqlPipeline():
    def __init__(self, host, database, user, password, port):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            host=crawler.settings.get('MYSQL_HOST'),
            database=crawler.settings.get('MYSQL_DATABASE'),
            user=crawler.settings.get('MYSQL_USER'),
            password=crawler.settings.get('MYSQL_PASSWORD'),
            port=crawler.settings.get('MYSQL_PORT'),
        )

    def open_spider(self, spider):
        self.db = pymysql.connect(self.host, self.user, self.password, self.database, charset='utf8',
                                  port=self.port)
        self.cursor = self.db.cursor()

    def close_spider(self, spider):
        self.db.close()

    def process_item(self, item, spider):
        # print(item['raw_title'])
        data = dict(item)
        keys = ', '.join(data.keys())
        values = ', '.join(['%s'] * len(data))
        sql = 'insert into %s (%s) values (%s)' % (item.table, keys, values)
        self.cursor.execute(sql, tuple(data.values()))
        self.db.commit()
        return item
