from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer
import os



Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer(), primary_key=True)
    name = Column(String(50), nullable=False)
    age = Column(Integer(), nullable=False)

    def __repr__(self):
        return f'<Student name="{self.name}" age={self.age}>'
