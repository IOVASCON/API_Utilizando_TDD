from sqlalchemy import Column, Integer, String, Float
from store.core.database import Base

class Retirement(Base):
    __tablename__ = "retirement"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    details = Column(String)
    age_limit = Column(Integer)
    monthly_contribution = Column(Float)
