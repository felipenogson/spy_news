from sqlalchemy import Boolean, Column, ForeignKey, Integer, String 
from sqlalchemy.orm import relationship

from .database import Base

class Link(Base):
    __tablename__ = "links"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True)
    url = Column(String, unique=True, index=True)
    fake_url = Column(String)
    is_active = Column(Boolean, default=True)

    clicks = relationship('Click', back_populates='owner')

class Click(Base):
    __tablename__ = 'clicks'
    id = Column(Integer, primary_key=True, index=True)
    ip = Column(String)
    geo = Column(String)
    browser = Column(String)
    owner_id = Column(Integer, ForeignKey('links.id'))

    owner = relationship('Link', back_populates="clicks")