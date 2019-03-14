from sqlalchemy.orm import sessionmaker
from shiyanlou.models import Course,engine,User
from datetime import datetime
from .items import CourseItem,UserItem


class ShiyanlouPipeline(object):
    
    def process_item(self, item, spider):
        if isinstance(item, CourseItem):
            self._process_course_item(item)
        else:
            self._process_user_item(item)

    def _process_course_item(self,item):
        item['students'] = int(item['students'])
        if item['students'] < 1000:
            raise DropItem('Course students less than 1000.')
        else:
            self.session.add(Course(**item))

    def _process_user_item(self,item):
        item['level'] = int(item['level'][1:])
        item['join_date'] = datetime.strptime(item['join_date'].split()[0], '%Y-%m-%d')
        item['learn_courses_num'] = int(item['learn_courses_num'])
        self.session.add(User(**item))
        print('---------------------------------', item.get('name'))

    def open_spider(self,spider):
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def close_spider(self,spider):
        self.session.commit()
        self.session.close()
