# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from .settings import *


class MtgPipeline(object):
    def process_item(self, item, spider):
        print(item['name'],item['price'],item['stock'])

        return item


class MtgMysqlPipeline(object):

    def open_spider(self,spider):
        self.db = pymysql.connect(
            host=Mysql_host,
            user=Mysql_user,
            password=Mysql_pwd,
            database=Mysql_db,
            charset=Charset
        )
        self.cursor = self.db.cursor()
        print('open')

    def process_item(self,item,spider):

        ins = 'insert into Mtg (name,price,stock) values (%s,%s,%s)'
        L = [
            item['name'],
            item['price'],
            item['stock']
        ]
        self.cursor.execute(ins,L)
        self.db.commit()

        return item

    def close_spider(self,spider):
        self.cursor.close()
        self.db.close()
        print('close')

class MtgMongoPipeline(object):
    def procees_item(self,item,spider):
        return item