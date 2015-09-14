from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from scanbox.model import Base, ReceivedFile
from scanbox.handlers import FsEventHandler
from watchdog.events import FileSystemEvent
from pathlib import PurePosixPath
import pytest


@pytest.fixture
def database():
    engine = create_engine('sqlite://')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session


def test_filename(database):
    test_path = '/test/STUDY/file'
    handler = FsEventHandler(database, '/test')
    event = FileSystemEvent(test_path)
    handler.on_created(event)
    session  = database()
    f = session.query(ReceivedFile).filter_by(filename=test_path).one()
    assert f.filename == test_path
    assert f.study == 'STUDY'


def test_study(database):
    test_path = '/test/STUDY/file'
    handler = FsEventHandler(database, '/test')
    event = FileSystemEvent(test_path)
    handler.on_created(event)
    session  = database()
    f = session.query(ReceivedFile).filter_by(filename=test_path).one()
    assert f.study == 'STUDY'
