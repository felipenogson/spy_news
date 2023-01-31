from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.responses import RedirectResponse, HTMLResponse
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

    # Este codigo es para ver si existe la entrada en la bd
    # db_link = crud.get_link_by_url(db, url=link.url)
    getting_link = crud.create_link(db=db, link=link)
    if not getting_link: 
        raise HTTPException(status_code=400, detail="Can't get url info")
    return getting_link

@app.get('/links/', response_model=list[schemas.Link])
def read_links(skip: int = 0, limit: int = 0, db : Session = Depends(get_db)):
    links = crud.get_links(db, skip=skip, limit=limit)
    return links

@app.get("/news/{fake_url:path}")
def create_click_for_link( fake_url: str, request:Request ,db: Session = Depends(get_db)):
    print(f'Eureka: {fake_url}')
    from pdb import set_trace; set_trace()
    # click = schemas.Click()
    # db_click = crud.create_link_click(db=db,click=click, fake_url=fake_url)
    return RedirectResponse('https://pi.nogson.com')

@app.get("/clicks/", response_model=list[schemas.Click])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    clicks = crud.get_clicks(db, skip=skip, limit=limit)
    return clicks