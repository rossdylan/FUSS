from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    Unicode,
    Table,
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    relationship,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()
Base.query = DBSession.query_property()


class FASUser(Base):
    __table__ = 'users'
    id = Column(Integer, unique=True, primary_key=True)
    username = Column(Unicode(128), unique=True)
    topics = relationship("Topic", backref='fasuser')


class Topic(Base):
    __table__ = 'topics'
    name = Column(Unicode(128), unique=True)
