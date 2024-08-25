import praw
from praw import Reddit
import sys
import os
import pandas as pd
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.constants import POST_FIELDS

#returns connection_object to reddit
def connect_reddit(client_id, client_secret, user_agent):
    try:
        reddit = praw.Reddit(client_id=client_id,
                             client_secret=client_secret,
                             user_agent=user_agent)
        print('connected to reddit')
        return reddit
    except Exception as e:
        print(e)
        sys.exit(1) #function terminates a program. The exit status code you provide. A non-zero value (like 1) indicates that the program ended with an error or an abnormal condition. Zero (0) generally indicates successful execution.


#return value of 'connect_reddit' is 'reddit_instance'
#Extractions
def extract_posts(reddit_instance: Reddit, subreddit: str, time_filter: str, limit=None):
    subreddit = reddit_instance.subreddit(subreddit)
    posts = subreddit.top(time_filter=time_filter, limit=limit)

    post_lists = []

    for post in posts:
        post_dict = vars(post)
        
        post = {key: post_dict[key] for key in POST_FIELDS}
        post_lists.append(post)
    
    return post_lists

#Transformations
def transform_data(post_df: pd.DataFrame):
    post_df['created_utc'] = pd.to_datetime(post_df['created_utc'], unit='s')
    post_df['over_18'] = np.where((post_df['over_18'] == True), True, False)
    post_df['author'] = post_df['author'].astype(str)
    edited_mode = post_df['edited'].mode()
    post_df['edited'] = np.where(post_df['edited'].isin([True, False]),
                                 post_df['edited'], edited_mode).astype(bool)
    post_df['num_comments'] = post_df['num_comments'].astype(int)
    post_df['score'] = post_df['score'].astype(int)
    # post_df['upvote_ratio'] = post_df['upvote_ratio'].astype(int)
    # post_df['selftext'] = post_df['selftext'].astype(str)
    post_df['title'] = post_df['title'].astype(str)

    return post_df

#Load
def load_data_to_csv(data: pd.DataFrame, path:str):
    data.to_csv(path, index=False)

