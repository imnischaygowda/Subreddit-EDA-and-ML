


# PRAW package
import praw,requests,re
import urllib
import pandas as pd
from pyspark.sql import SparkSession
from pyspark.sql.types import *

reddit_auth = praw.Reddit(client_id='ZlNjwoTR2LuZNk0ifQvF-g', client_secret='ZaF5NJUmzI1ZDoicXqz_IPErRYQ-qw', user_agent='my_web_scrapper')

# create empty spark session.
spark_session = SparkSession.builder.appName('Empty_Dataframe').getOrCreate()

# create an empty RDD
emp_RDD = spark_session.sparkContext.emptyRDD()


# create empty schema.
columns = StructType([])

# Create an empty RDD with empty schema
main_data = spark_session.createDataFrame(data = emp_RDD, schema = columns)

# get post data from subreddit.
posts = reddit_auth.subreddit('askreddit').hot(limit = 500000)

data_post = []
for post in posts:
    
    data_post.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])
    
posts = pd.DataFrame(posts,columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'created'])

main_data_1 = spark_session.createDataFrame(data = emp_RDD, schema = columns)


# print(posts)
    
    # # for post in hot_posts:
    # post.display_name
    # # Output: redditdev
    # post.title
    # # Output: reddit development
    # post.description




