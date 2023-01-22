from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()

@app.post("/links/", response_model=schemas.Link)
def create_link(link: schemas.LinkCreate, db: Session = Depends(get_db)):
    db_link = crud.get_link_by_url(db, url=link.url)
    if db_link:
        raise HTTPException(status_code=400, detail='Email already registered')
    return crud.create_link(db=db, link=link)

@app.get('/links/', response_model=list[schemas.Link])
def read_links(skip: int = 0, limit: int = 0, db : Session = Depends(get_db)):
    links = crud.get_links(db, skip=skip, limit=limit)
    return links

@app.post("/clicks/{link_id}/clicks/", response_model=schemas.Click)
def create_click_for_link( link_id: int, click: schemas.ClickCreate, db: Session = Depends(get_db)):
    return crud.create_link_click(db=db, click=click, link_id=link_id)

@app.get("/clicks/", response_model=list[schemas.Click])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    clicks = crud.get_clicks(db, skip=skip, limit=limit)
    return clicks