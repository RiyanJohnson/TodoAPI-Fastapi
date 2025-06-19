from sqlalchemy import Table, Column, Integer, String, Boolean
from .database import metadata

items_table = Table(
    "items",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("text", String(255)),
    Column("is_done", Boolean, default=False),
    Column("description", String(255), nullable=True)
)
