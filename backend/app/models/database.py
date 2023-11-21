from sqlalchemy import MetaData, Table, Column, Integer, String, DateTime
from sqlalchemy import ForeignKey

metadata = MetaData()

projects = Table(
    "projects",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("idea_initial", String, nullable=False),
    Column("idea_final", String, nullable=False),
    Column("company_goal", String, nullable=False),
    Column("folder_path", String, nullable=False),
    Column("created_at", DateTime, nullable=False),
    Column("current_phase", String, nullable=True),
    Column("current_stage", String, nullable=True)
)

chats = Table(
    "chats",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("chat_name", String, nullable=False),
    Column("chat_assistant_primary", String, nullable=False),
    Column("chat_assistant_secondary", String, nullable=False),
    Column("chat_messages", String, nullable=True),
    Column("created_at", DateTime, nullable=False)
)

threads = Table(
    "threads",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("thread_id", String, nullable=False),  # ID returned by OpenAI API
    Column("thread_name", String, nullable=False),
    Column("created_at", DateTime, nullable=False)
)

assistants = Table(
    "assistants",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("assistant_id", String, nullable=False),  # ID returned by OpenAI API
    Column("assistant_name", String, nullable=False),
    Column("assistant_type", String, nullable=False),
    Column("assistant_instructions", String, nullable=False),
    Column("assistant_model", String, nullable=False),
    Column("created_at", DateTime, nullable=False)
)

project_assistant_association = Table(
    "project_assistant_association",
    metadata,
    Column("project_id", Integer, ForeignKey("projects.id"), primary_key=True),
    Column("assistant_id", Integer, ForeignKey("assistants.id"), primary_key=True)
)

project_chat_association = Table(
    "project_chat_association",
    metadata,
    Column("project_id", Integer, ForeignKey("projects.id"), primary_key=True),
    Column("chat_id", Integer, ForeignKey("chats.id"), primary_key=True)
)

chat_thread_association = Table(
    "chat_thread_association",
    metadata,
    Column("chat_id", Integer, ForeignKey("chats.id"), primary_key=True),
    Column("thread_id", Integer, ForeignKey("threads.id"), primary_key=True)
)

def create_tables(engine):
    metadata.create_all(bind=engine)