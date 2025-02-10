from sqlalchemy import Column, Integer, ForeignKey, Table
from app.database import Base

# Since this is a pure join table, we can use Table instead of a class
word_groups = Table(
    'word_groups',
    Base.metadata,
    Column('word_id', Integer, ForeignKey('words.id'), primary_key=True),
    Column('group_id', Integer, ForeignKey('groups.id'), primary_key=True)
)