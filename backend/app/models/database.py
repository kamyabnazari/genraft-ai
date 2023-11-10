from sqlalchemy import MetaData, Table, Column, Integer, String

metadata = MetaData()

projects = Table(
    "projects",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("idea_initial", String, nullable=False),
    Column("idea_final", String, nullable=False),
    Column("chat_history_idea", String, nullable=False)
)

def create_tables(engine):
    metadata.create_all(bind=engine)