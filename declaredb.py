import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String,Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from datetime import datetime
from sqlalchemy.orm import sessionmaker


#Base class inherited by the class models used in mapping to sql 
Base = declarative_base()

class Items(Base):
    __tablename__ = 'items'
    #columns for the table items
    id = Column(Integer, primary_key=True)
    itemname = Column(String(50), nullable=False)
    description=Column(String(250),nullable=False)
    available_amount=Column(Integer,nullable=False)
    price=Column(Integer,nullable=False)
    date_added=Column(DateTime, nullable=False)
    status=Column(Boolean,nullable=False)

 
class Logs(Base):
    __tablename__ = 'logs'
    # columns for the table logs.    
    id = Column(Integer, primary_key=True)
    item_id = Column(Integer, ForeignKey('items.id'))
    status = Column(Boolean)
    date = Column(DateTime)    
    item_number = relationship(Items)
 
# Create an engine that stores data in the local directory
engine = create_engine('sqlite:///inventory.db')
 
# Create all tables in the engine
Base.metadata.create_all(engine)
