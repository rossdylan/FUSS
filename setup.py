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
    'velruse',
    ]

setup(name='fuss',
      version='0.1.0',
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
      url='https://github.com/rossdylan/fuss',
      keywords='web wsgi bfg pylons pyramid',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='fuss',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = fuss:main
      [console_scripts]
      initialize_fuss_db = fuss.scripts.initializedb:main
      """,
      )

