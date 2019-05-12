from seiya.db.base import engine, Base, Session

Base.metadata.create_all(engine)
