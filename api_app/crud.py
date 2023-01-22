from sqlalchemy.orm import Session

from . import models, schemas

def get_link(db: Session, link_id: int):
    return db.query(models.Link).filter(models.Link.id == link_id).first()

def get_link_by_url(db: Session, url: str):
    return db.query(models.Link).filter(models.Link.url == url).first()

def get_links(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Link).offset(skip).limit(limit).all()

def create_link(db: Session, link : schemas.LinkCreate):
    db_link = models.Link(email=link.email, url = link.url)
    db.add(db_link)
    db.commit()
    db.refresh(db_link)
    return db_link

def get_clicks(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Click).offset(skip).limit(limit).all()

def create_link_click(db: Session, click: schemas.ClickCreate, link_id: int):
    db_click = models.Click(**click.dict(), owner_id=link_id)
    db.add(db_click)
    db.commit()
    db.refresh(db_click)
    return db_click