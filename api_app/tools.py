from opengraphio import OpenGraphIO
import os
from dotenv import load_dotenv
from uuid import uuid4
from sqlalchemy.orm import Session
from urllib import parse
from .models import *


load_dotenv()

# para leer los tags Opengraph estamos usando opengraphio, que es una biblioteca
# de paga pero deja un uso gratis limitado, en un futuro a buscar una mas libre.
key = os.getenv('OPENGRAPHIO')
opengraph = OpenGraphIO({"app_id":key})

def get_og_data(url: str):
    if not url:
        return
    
    metadata = opengraph.get_site_info(url)
    og = metadata.get('openGraph')

    return og

def fake_url_generator(db: Session, title:str):
    ''' Devuelve una tupla con un numero aleatorio no existente en la bd y el titulo sanitizado para html'''
    random_address = str(uuid4())[:8]
    fake_url = parse.quote(f'{random_address}/{title}.html')
    db_link = db.query(Link).filter(Link.fake_url == fake_url).first()
    while db_link :
        random_address = str(uuid4())[:8]
        fake_url = parse.quote(f'{random_address}/{title}.html')
        db_link = db.query(Link).filter(Link.fake_url == fake_url).first()

    return fake_url


    
    


