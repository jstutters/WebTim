from watchdog.events import FileSystemEventHandler
from .model import ReceivedFile, ReceivedDir, Study
import os.path
from .pathutils import study_from_path
from pathlib import PurePosixPath


class FsEventHandler(FileSystemEventHandler):
    def __init__(self, Session, root):
        self.Session = Session
        self.root = PurePosixPath(root)

    def on_created(self, e):
        if e.is_directory:
            self.add_dir(e)
        else:
            self.add_file(e)

    def add_file(self, e):
        session = self.Session()
        new_file = ReceivedFile()
        path = PurePosixPath(e.src_path)
        new_file.filename = str(path)
        parent_dirname = str(path.parent)
        parent_dir = session.query(ReceivedDir).filter_by(dirname=parent_dirname).one()
        new_file.directory = parent_dir
        new_file.study = parent_dir.study
        session.add(new_file)
        session.commit()

    def add_dir(self, e):
        session = self.Session()
        new_dir = ReceivedDir()
        path = PurePosixPath(e.src_path)
        new_dir.dirname = str(path)
        study_name = study_from_path(self.root, path)
        parent_study = session.query(Study).filter_by(name=study_name).one()
        new_dir.study = parent_study
        session.add(new_dir)
        session.commit()
