from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from webtim.model import Base, ReceivedFile, ReceivedDir, Study
from webtim.handlers import FsEventHandler
from watchdog.events import FileSystemEvent
from pathlib import PurePosixPath
import pytest


@pytest.fixture
def database():
    engine = create_engine('sqlite://')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session


def test_directory(database):
    session  = database()
    study = Study()
    study.name = 'STUDY'
    session.add(study)
    session.commit()
    test_path = '/test/STUDY/dir'
    handler = FsEventHandler(database, '/test')
    event = FileSystemEvent(test_path)
    event.is_directory = True
    handler.on_created(event)
    f = session.query(ReceivedDir).filter_by(dirname=test_path).one()
    assert f.dirname == test_path
    assert f.study.name == 'STUDY'


def test_file(database):
    session  = database()
    study = Study()
    study.name = 'STUDY'
    session.add(study)
    new_dir = ReceivedDir()
    new_dir.dirname = '/test/STUDY/dir'
    new_dir.study = study
    session.add(new_dir)
    session.commit()
    test_path = '/test/STUDY/dir/file'
    handler = FsEventHandler(database, '/test')
    event = FileSystemEvent(test_path)
    handler.on_created(event)
    f = session.query(ReceivedFile).filter_by(filename=test_path).one()
    assert f.filename == test_path
    assert f.directory.dirname == '/test/STUDY/dir'
    assert f.study.name == 'STUDY'
