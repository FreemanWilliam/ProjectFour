import sys
from sqlalchemy import 
Column, ForeignKey, Integer, String

from sqlalchemy.ext.declarative import
declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy import create_engine

Base = declarative_base()

class Produce(Base):

	__tablename__ = 'produce'

	id = Column(Integer, primary_key=True)

class ProduceItem(Base):

	__tablename__ = 'produceItem'

engine = create_engine(
'sqlite:///producemenu.db')

Base.metadata.create_all(engine)