# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json,pymongo
class MyprojectPipeline(object):
    def process_item(self, item, spider):
        with open('猫眼.txt','a',encoding = 'utf-8')as f:
            json.dump(dict(item),f,ensure_ascii = False)
            f.write('\n')
        return item

class Tencent(object):
    def process_item(self, item, spider):
        with open('腾讯招聘.txt','a',encoding = 'utf-8')as f:
            json.dump(dict(item),f,ensure_ascii = False)
            f.write('\n')
        return item

#连接MongoDB数据库
class MeiJu(object):
    def __init__(self):
        self.client = pymongo.MongoClient('localhost')
        self.db = self.client['meiju']
        self.mj = self.db['mj']
    def process_item(self, item, spider):
        self.mj.insert(dict(item))
        return item