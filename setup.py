import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = [
    'pyramid',
    'SQLAlchemy',
    'transaction',
    'pyramid_tm',
    'pyramid_debugtoolbar',
    'zope.sqlalchemy',
    'waitress',
    'fedmsg',
    ]

setup(name='FUSSy',
      version='0.0',
      description='Fedora User Stream System',
      long_description=README + '\n\n' +  CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pylons",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='Ross Delinger',
      author_email='rossdylan@csh.rit.edu',
      url='https://github.com/rossdylan/FUSSy',
      keywords='web wsgi bfg pylons pyramid',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='fedora_user_streams',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = fedora_user_streams:main
      [console_scripts]
      initialize_fedora_user_streams_db = fedora_user_streams.scripts.initializedb:main
      """,
      )

