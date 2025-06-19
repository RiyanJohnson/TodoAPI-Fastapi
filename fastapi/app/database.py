from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, MetaData
from databases import Database

DATABASE_URL = "mysql+aiomysql://root:riyan@localhost/todo"

database = Database(DATABASE_URL)
metadata = MetaData()
Base = declarative_base()

engine = create_engine(
    DATABASE_URL.replace("aiomysql", "pymysql"),  # SQLAlchemy needs sync driver
    echo=True
)