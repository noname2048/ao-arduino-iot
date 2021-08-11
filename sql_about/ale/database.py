from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import secret

db_url = "postgresql://postgres:example@localhost:15001/iot"
engine = create_engine(db_url, echo=True, future=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

aws_db_url = f"postgresql://{secret.username}:{secret.password}@{secret.endpoint}:{secret.port}/{secret.dbname}"
