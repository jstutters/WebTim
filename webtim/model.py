from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref

Base = declarative_base()

class Study(Base):
    __tablename__ = 'studies'

    id = Column(Integer, primary_key=True)
    name = Column(String(32))

class ReceivedDir(Base):
    __tablename__ = 'received_dirs'

    id = Column(Integer, primary_key=True)
    dirname = Column(String(1024))
    study_id = Column(Integer, ForeignKey('studies.id'))

    study = relationship(Study, backref=backref('dirs', order_by=id))


class ReceivedFile(Base):
    __tablename__ = 'received_files'

    id = Column(Integer, primary_key=True)
    filename = Column(String(1024))
    study_id = Column(Integer, ForeignKey('studies.id'))
    directory_id = Column(Integer, ForeignKey('received_dirs.id'))

    study = relationship(Study, backref=backref('files', order_by=id))
    directory = relationship(ReceivedDir, backref=backref('files', order_by=filename))


