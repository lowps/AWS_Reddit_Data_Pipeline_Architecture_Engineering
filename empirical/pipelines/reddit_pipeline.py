from praw import Reddit
import praw
import sys
import os
import pandas as pd


sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from etls.reddit_etl import (connect_reddit,
                             extract_posts,
                             transform_data,
                             load_data_to_csv
                             )                    
from utils.constants import (CLIENT_ID, 
                             SECRET, 
                             OUTPUT_PATH
                             )
 


#pipeline- ETL pipeline, a collection of functions executed sequentially 
def reddit_pipeline(file_name: str, subreddit: str, time_filter='day', limit=None):
    # connecting to reddit instance
    instance = connect_reddit(CLIENT_ID, SECRET, 'Airscholar Agent')
    # extraction
    posts = extract_posts(instance, subreddit, time_filter, limit)
    post_df = pd.DataFrame(posts)
    #transformation
    post_df = transform_data(post_df)
    #load
    file_path = f'{OUTPUT_PATH}/{file_name}.csv'
    load_data_to_csv(post_df, file_path)

    return file_path



 
