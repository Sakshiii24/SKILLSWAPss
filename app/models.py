from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    skills_offered = Column(String)
    skills_wanted = Column(String)
    location = Column(String)
    availability = Column(String)

class SwapOffer(Base):
    __tablename__ = 'swap_offers'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    skill_offered = Column(String)
    skill_wanted = Column(String)
    status = Column(String)
    user = relationship("User")
