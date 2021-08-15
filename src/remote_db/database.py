from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from . import secret

aws_db_url = f"postgresql://{secret.username}:{secret.password}@{secret.endpoint}:{secret.port}/{secret.dbname}"

engine = create_engine(aws_db_url, echo=True, future=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
