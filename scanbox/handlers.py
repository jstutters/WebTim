from watchdog.events import FileSystemEventHandler
from .model import ReceivedFile
import os.path
from pathlib import PurePosixPath


class FsEventHandler(FileSystemEventHandler):
    def __init__(self, Session, root):
        self.Session = Session
        self.root = root

    def on_created(self, e):
        path = PurePosixPath(e.src_path)
        new_file = ReceivedFile()
        new_file.filename = str(path)
        local_path = path.relative_to(self.root)
        new_file.study = local_path.parts[0]
        session = self.Session()
        session.add(new_file)
        session.commit()
