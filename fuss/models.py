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

association_table = Table('association', Base.metadata,
        Column('username', Unicode(128), ForeignKey('users.username')),
        Column('topic', Unicode(128), ForeignKey('topics.name')),)


class FASUser(Base):
    __tablename__ = 'users'
    id = Column(Integer, unique=True, primary_key=True)
    username = Column(Unicode(128), unique=True)
    topics = relationship("Topic",
            secondary=association_table)


class Topic(Base):
    __tablename__ = 'topics'
    name = Column(Unicode(128), unique=True, primary_key=True)
