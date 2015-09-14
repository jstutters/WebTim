from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class ReceivedFile(Base):
	__tablename__ = 'received_files'

	id = Column(Integer, primary_key=True)
	filename = Column(String(1024))	
        study = Column(String(32))
