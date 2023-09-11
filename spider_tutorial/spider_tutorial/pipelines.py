# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import logging
import pymongo


class MongodbPipeline:
    collection_name = 'transcripts'

    def open_spider(self, spider):
        logging.warning("Spider Opened - Pipeline")
        self.client = pymongo.MongoClient(
            "mongodb+srv://shoetify:shoetify@cluster0.i0m1ot4.mongodb.net/?retryWrites=true&w=majority")
        self.db = self.client['My_Database']

    def close_spider(self, spider):
        logging.warning("Spider Closed - Pipeline")
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.collection_name].insert_one(item)
        return item
