from setuptools import setup

setup(name='WebTim',
      version='0.0.1',
      description='Monitor received DICOM images',
      author='Jon Stutters',
      author_email='j.stutters@ucl.ac.uk',
      packages=[
          'scanbox'
      ],
      install_requires=[
          'watchdog',
          'sqlalchemy',
          'pathlib'
      ]
)
