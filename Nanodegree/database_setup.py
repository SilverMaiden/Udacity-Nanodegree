import sys

from sqlalchemy import Column, ForeignKey, Integer, String

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy import create_engine

Base = declarative_base()

class Restaurant(Base):
    name = Column(
        String(80), nullable = False)

    id = Column(
        Integer, primary_key = True)



class MenuItem(Base):


#######insert at end of file #######

engine = create_engine('sqlite:///restaurantmenu.db')

Base.metadate.create_all(engine)
