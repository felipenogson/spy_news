# coding: utf-8
import praw
from opengraphio import OpenGraphIO
import requests
from dotenv import load_dotenv
import os

load_dotenv()

key = os.getenv('OPENGRAPHIO')
opengraph = OpenGraphIO({"app_id":key})

def get_reddit_client():
    reddit_client = os.getenv('REDDIT_CLIENT')
    reddit_key = os.getenv('REDDIT_API')
    reddit = praw.Reddit(
    client_id=reddit_client, client_secret=reddit_key, user_agent="my user agent")
    print( f"Cliente de reddit, read-only:  {reddit.read_only}")
    return reddit


def get_posts( reddit, subreddit : int = 'nottheonion', limit: int = 20):
    print (limit)
    subreddit = reddit.subreddit(subreddit)
    posts = [post for post in subreddit.top(limit=limit, time_filter="month")]
    return posts


if __name__ == "__main__":
        
    reddit = get_reddit_client()
    posts = get_posts()

    for p in posts:
        print(f'{p.title}\n {("=" * 20 )} \n{p.url}')
        print('=' * 20)
        metadata = opengraph.get_site_info(p.url)
        og = metadata['openGraph']
        for key, value in og.items():
            print( f' {key} : {value}')

        print('\n\n')
        input()

        
