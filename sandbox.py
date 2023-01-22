# coding: utf-8
import praw
from dotenv import load_dotenv
import os
import requests
from bs4 import BeautifulSoup
import urllib.parse
import ftplib
from fake_headers import  Headers

load_dotenv()

# Credenciales para Reddit
reddit_client = os.getenv('REDDIT_CLIENT')
reddit_key = os.getenv('REDDIT_API')

# Credenciales para FTP
ftp_host = os.getenv('FTP_HOST')
ftp_username = os.getenv('FTP_USERNAME')
ftp_password = os.getenv('FTP_PASSWORD')

reddit = praw.Reddit(
client_id=reddit_client, client_secret=reddit_key, user_agent="my user agent")
print( f"Cliente de reddit, read-only:  {reddit.read_only}")






subreddit = reddit.subreddit('nottheonion')

random_posts = subreddit.hot(limit=10)

for post in random_posts:
    print(post.title)
    detener = input("Detener (y): ")
    if detener == "y":
        break
    
# Aqui Hacemos el request de la pagina para poder extraer los metas

url = post.url
headers = Headers(os="mac", headers=True).generate()
r = requests.get(post.url, headers=headers)

soup = BeautifulSoup(r.text, 'html.parser')

# meta = {
# "image" : soup.find("meta", property="og:image"), 
# "description" : soup.find("meta", property="og:description"),
# "title" : soup.find("meta", property="og:title"),
# "url" : soup.find("meta", property="og:url"),
# "text_type" : soup.find("meta", property="og:type"),
# "site_name" : soup.find("meta", property="og:site_name")}

meta = soup.find_all('meta')
meta = [str(m) for m in meta if ('script' or 'style') not in  str(m)]

removestring = " %:/,.\\[]<>*?\"\'"
sourcestring = urllib.parse.quote(soup.title.string.strip())
encoded_title = ''.join( [c for c in sourcestring if c not in removestring])  + ".html"
# "".join([c for c in sourcestring if c not in removestring])

# Creando el archivo html con jinja
from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('news.html')
# import pdb; pdb.set_trace()
output_from_parsed_template = template.render(meta=meta, url = url, title = soup.title)
print(output_from_parsed_template)

filename = encoded_title
with open(filename, 'w') as fh:
    fh.write(output_from_parsed_template)

def upload_ftp():
    remote_url = "rns.rf.gd"

    ftp_server =  ftplib.FTP(ftp_host, ftp_username, ftp_password)
    ftp_server.encoding = 'utf-8'
    ftp_server.cwd('/htdocs')


    with open(filename, 'rb') as fh:
        ftp_server.storbinary(f"STOR {filename}", fh)
        
    print(ftp_server.dir())
    print(f"https://{remote_url}/{encoded_title}")

# upload_ftp()
