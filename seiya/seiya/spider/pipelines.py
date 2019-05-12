# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re
#from sqlalchemy.orm import sessionmaker
from seiya.db import engine,JobModel,Session
from seiya.spider.items import JobItem

class SeiyaPipeline(object):
    # 持久化数据 Pipline
    def open_spider(self,spider):
        #self.session = sessionmaker(bind=engine)()
        self.session = Session()

    def close_spider(self,spider):
        self.session.commit()
        self.session.close()
    def process_item(self, item, spider):
        if isinstance(item,JobItem):
            return self._process_job_item(item)
        else:
            return item

    def _process_job_item(self,item):
        city = item['city'].split('')[0]

        salary_lower,salary_upper = 0,0
        tmp = re.match(r'[^\d]*(\d+)k-(\d+)k',item['salary'])
        if tmp is not None:
            salary_lower,salary_upper = int(tmp.group(1)),int(tmp.group(2))
                
        experience_lower,experience_upper = 0,0
        tmp = re.match(r'[^\d]*(\d+)-(\d+)',item['experience'])
        if tmp is not None:
            experience_lower,experience_upper = int(tmp.group(1)),int(tmp.group(2))

        tags = ' '.join(item['tags'])

        model = JobModel(
                title = item['title'],
                city = city,
                salary_lower = salary_lower,
                salary_upper = salary_upper,
                experience_lower = experience_lower,
                experience_upper = experience_upper,
                education = item['education'],
                tags = tags,
                company = item['company'],
                )
        
        self.session.add(model)

        return item
