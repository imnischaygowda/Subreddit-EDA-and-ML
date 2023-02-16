'''
Author: Nischay Gowda nischaygowda105@gmail.com
Date: 2023-01-17 23:36:11
LastEditors: Nischay Gowda nischaygowda105@gmail.com
LastEditTime: 2023-02-15 21:14:27
FilePath: \Subreddit-EDA-and-ML\reddit_data_scraping.py
'''

import requests
import pandas as pd
import warnings
warnings.filterwarnings("ignore")
from collections import defaultdict

import datetime, time
# importing timezone from pytz module
from pytz import timezone


# fetch data using reddit url.
def get_subreddit_data(subreddit, listing, limit, timeframe):
    # without Authemticator
    try:
        base_url = f'https://www.reddit.com/r/{subreddit}/{listing}.json?limit={limit}&t={timeframe}'
        request = requests.get(base_url, headers = {'User-agent': 'web_scarpe_bot'})
    except:
        print('An Error Occured')
    return request.json()

def get_data_in_dataframe(r_data):
    
    # create a dataframe
    data_dict = defaultdict()
    for post in r_data['data']['children']:
        
        # Data points available for a reddit post.
        # ['approved_at_utc', 'subreddit', 'selftext', 'author_fullname', 'saved', 'mod_reason_title', 'gilded', 'clicked', 'title', 
        # 'link_flair_richtext', 'subreddit_name_prefixed', 'hidden', 'pwls', 'link_flair_css_class', 'downs', 'top_awarded_type', 
        # 'hide_score', 'name', 'quarantine', 'link_flair_text_color', 'upvote_ratio', 'author_flair_background_color', 'subreddit_type', 
        # 'ups', 'total_awards_received', 'media_embed', 'author_flair_template_id', 'is_original_content', 'user_reports', 'secure_media', 
        # 'is_reddit_media_domain', 'is_meta', 'category', 'secure_media_embed', 'link_flair_text', 'can_mod_post', 'score', 'approved_by', 
        # 'is_created_from_ads_ui', 'author_premium', 'thumbnail', 'edited', 'author_flair_css_class', 'author_flair_richtext', 'gildings', 
        # 'content_categories', 'is_self', 'mod_note', 'created', 'link_flair_type', 'wls', 'removed_by_category', 'banned_by', 'author_flair_type', 
        # 'domain', 'allow_live_comments', 'selftext_html', 'likes', 'suggested_sort', 'banned_at_utc', 'view_count', 'archived', 'no_follow', 
        # 'is_crosspostable', 'pinned', 'over_18', 'all_awardings', 'awarders', 'media_only', 'can_gild', 'spoiler', 'locked', 'author_flair_text', 
        # 'treatment_tags', 'visited', 'removed_by', 'num_reports', 'distinguished', 'subreddit_id', 'author_is_blocked', 'mod_reason_by', 'removal_reason', 
        # 'link_flair_background_color', 'id', 'is_robot_indexable', 'report_reasons', 'author', 'discussion_type', 'num_comments', 'send_replies', 'whitelist_status', 
        # 'contest_mode', 'mod_reports', 'author_patreon_flair', 'author_flair_text_color', 'permalink', 'parent_whitelist_status', 'stickied', 'url', 'subreddit_subscribers', 
        # 'created_utc', 'num_crossposts', 'media', 'is_video']
        
        data_dict[post['data']['title']] = {'id':post['data']['id'],'created_date_utc':post['data']['created_utc'],'subreddit_id':post['data']['subreddit_id'],'title':post['data']['title'], 
                                            'body':post['data']['selftext'], 'url':post['data']['url'],'score':post['data']['score'],'comments':post['data']['num_comments']}
    
    main_df = pd.DataFrame.from_dict(data_dict, orient='index')
    return main_df
    
subreddit = 'askreddit'
limit = 1000
timeframe = 'all'
listing = 'top'


if __name__ == '__main__':
    r = get_subreddit_data(subreddit, listing, limit, timeframe)
    main_data = get_data_in_dataframe(r)
    print(main_data.head())
    
#     # giving the format of datetime
#     format = "%Y-%m-%d"

#     # convert float UTC to Date.
#     main_data['created_date'] = datetime.datetime.fromtimestamp(main_data['created_date_utc'][0]).strftime(format)
#     main_data = main_data[['id', 'created_date_utc', 'created_date', 'subreddit_id', 'title', 'body', 'url','score', 'comments']]
#     print(main_data.head())