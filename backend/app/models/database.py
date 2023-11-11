from sqlalchemy import MetaData, Table, Column, Integer, String, DateTime
from sqlalchemy.sql import func

metadata = MetaData()

projects = Table(
    "projects",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("idea_initial", String, nullable=False),
    Column("idea_final", String, nullable=False),
    Column("created_at", DateTime, default=func.now())
)

def create_tables(engine):
    metadata.create_all(bind=engine)