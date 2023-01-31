from sqlalchemy import Boolean, Column, ForeignKey, Integer, String 
from sqlalchemy.orm import relationship

from .database import Base

class Link(Base):
    __tablename__ = "links"

    id = Column(Integer, primary_key=True, index=True)
    fake_url = Column(String, unique=True)
    email = Column(String)
    is_active = Column(Boolean, default=True)

    # Meta tags
    title = Column(String)
    url = Column(String)
    type = Column(String)
    description = Column(String)
    image = Column(String)
    site_name = Column(String)


    clicks = relationship('Click', back_populates='owner')

    def __repr__(self):
        return f'id: {self.id}, fake_url = {self.fake_url}'


class Click(Base):
    __tablename__ = 'clicks'
    id = Column(Integer, primary_key=True, index=True)
    ip = Column(String)
    geo = Column(String)
    browser = Column(String)
    owner_id = Column(Integer, ForeignKey('links.id'))

    owner = relationship('Link', back_populates="clicks")

    def __repr__(self):
        return f'click for: {self.owner.fake_url}'