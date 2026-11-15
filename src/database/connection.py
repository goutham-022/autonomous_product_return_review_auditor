from sqlalchemy import text, create_engine
from sqlalchemy.orm import sessionmaker, Session
from src.utils.configs import settings
from src.database.models import Base

db_url = settings.DATABASE_URL

engine = create_engine(settings.DATABASE_URL, echo=False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db():
    import src.database.models  # noqa: F401 (registers models with Base.metadata)
    with engine.begin() as conn:
        conn.execute(text("CREATE EXTENSION IF NOT EXISTS vector;"))
        Base.metadata.create_all(bind=conn)

if __name__ == "__main__":
    from sqlalchemy import inspect

    print("Connecting to PostgreSQL and initializing schema...")
    init_db()
    inspector = inspect(engine)
    print("✅ Active Tables in PostgreSQL:", inspector.get_table_names())