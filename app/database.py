from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, MetaData
from databases import Database

DATABASE_URL = "mysql+aiomysql://username:password@localhost/database_name"

database = Database(DATABASE_URL)
metadata = MetaData()
Base = declarative_base()

engine = create_engine(
    DATABASE_URL.replace("aiomysql", "pymysql"),  
    echo=True
)