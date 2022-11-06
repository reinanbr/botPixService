import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#database_dir = os.path.abspath(os.path.dirname(__file__))
database_uri = f'sqlite:////tmp/ruby_news.db'

Session = sessionmaker()

engine = create_engine(database_uri)
session = Session(bind=engine)



