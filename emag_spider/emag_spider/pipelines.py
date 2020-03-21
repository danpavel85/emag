# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import mysql.connector
import MySQLdb
from emag_spider.items import EmagSpiderItem

class EmagSpiderPipeline(object):
    def __init__(self):
        self.connection = MySQLdb.connect('localhost', 'root', 'parola123', 'emag')
        self.cursor = self.connection.cursor()
        
        self.connection.set_character_set('utf8')
        self.cursor.execute('SET NAMES utf8;')
        self.cursor.execute('SET CHARACTER SET utf8;')
        self.cursor.execute('SET character_set_connection=utf8;')

    def process_item(self, item, spider):
        self.cursor.execute("""INSERT IGNORE INTO products (id, nme, current_price, initial_price, absolute_disc, percent_disc, url, part_number) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""", 
        (item['id'], item['name'], item['current_price'], item['initial_price'], item['absolute_disc'], item['percent_disc'], item['url'], item['part_number']))
        self.connection.commit()
        return item