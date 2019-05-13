from sqlalchemy import Column, String, Integer

from seiya.db.base import Base


class JobModel(Base):
    """租房数据 Model

    """
    __tablename__ = 'house'

    id = Column(Integer, primary_key=True)
    address = Column(String(32))
    house_type = Column(String(32))
    area = Column(Integer)
    rent = Column(Integer)
