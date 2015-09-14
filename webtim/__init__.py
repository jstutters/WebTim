from watchdog.observers import Observer
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import time
import sys
from .model import Base, ReceivedFile
from .handlers import FsEventHandler


class ScanBoxMonitor(object):
    def __init__(self, db_url, monitor_path):
        engine = create_engine(db_url)
        Base.metadata.create_all(engine)
        self.Session = sessionmaker(bind=engine)
        self.handler = FsEventHandler(self.Session, monitor_path)
        self.observer = Observer()
        self.observer.schedule(self.handler, monitor_path, recursive=True)

    def run(self):
        self.observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.observer.stop()
        self.observer.join()


def make_app(config):
    app = ScanBoxMonitor(config['db_url'], config['monitor_path'])
    return app
