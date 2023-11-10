from sqlalchemy import MetaData, Table, Column, Integer, String

metadata = MetaData()

messages = Table(
    "messages",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("message", String, nullable=False)
)

def create_tables(engine):
    metadata.create_all(bind=engine)