import configparser
import os
 

parser = configparser.ConfigParser()
parser.read(os.path.join(os.path.dirname(__file__), '../config/config.conf'))

SECRET = parser.get('api_keys', 'reddit_secret_key')
CLIENT_ID = parser.get('api_keys', 'reddit_client_id')

DATABASE_HOST = parser.get('database', 'database_host')
DATABASE_NAME = parser.get('database', 'database_name')
DATABASE_PORT = parser.get('database', 'database_port')
DATABASE_USERNAME = parser.get('database', 'database_username')
DATABASE_PASSWORD = parser.get('database', 'database_password')

#AWS
AWS_ACCESS_KEY_ID = parser.get('aws', 'aws_access_key_id')
AWS_SECRET_ACCESS_KEY = parser.get('aws', 'aws_secret_access_key')
# AWS_SESSION_TOKEN = parser.get('aws', 'aws_session_token')
AWS_REGION = parser.get('aws', 'aws_region')
AWS_BUCKET_NAME = parser.get('aws', 'aws_bucket_name')



INPUT_PATH = parser.get('file_paths', 'input_path')
OUTPUT_PATH = parser.get('file_paths', 'output_path')

POST_FIELDS = (
    'id',
    'title',
    'score',
    'num_comments',
    'author',
    'created_utc',
    'url',
    'over_18',
    'edited',
    'spoiler',
    'stickied'
)
#[2024-08-11, 17:16:08 UTC] {logging_mixin.py:151} INFO - {'comment_limit': 2048, 'comment_sort': 'confidence', '_reddit': <praw.reddit.Reddit object at 0x7fb8de8c2be0>, 'approved_at_utc': None, 'subreddit': Subreddit(display_name='dataengineering'), 'selftext': 'Couchbase? MongoDB? or something else?', 'author_fullname': 't2_4d3ypyd63', 'saved': False, 'mod_reason_title': None, 'gilded': 0, 'clicked': False, 'title': 'Which databases are you currently using in your work?', 'link_flair_richtext': [], 'subreddit_name_prefixed': 'r/dataengineering', 'hidden': False, 'pwls': 6, 'link_flair_css_class': '', 'downs': 0, 'thumbnail_height': None, 'top_awarded_type': None, 'hide_score': False, 'name': 't3_1epl3j7', 'quarantine': False, 'link_flair_text_color': 'light', 'upvote_ratio': 0.9, 'author_flair_background_color': None, 'subreddit_type': 'public', 'ups': 28, 'total_awards_received': 0, 'media_embed': {}, 'thumbnail_width': None, 'author_flair_template_id': None, 'is_original_content': False, 'user_reports': [], 'secure_media': None, 'is_reddit_media_domain': False, 'is_meta': False, 'category': None, 'secure_media_embed': {}, 'link_flair_text': 'Career', 'can_mod_post': False, 'score': 28, 'approved_by': None, 'is_created_from_ads_ui': False, 'author_premium': False, 'thumbnail': 'self', 'edited': False, 'author_flair_css_class': None, 'author_flair_richtext': [], 'gildings': {}, 'content_categories': None, 'is_self': True, 'mod_note': None, 'created': 1723383747.0, 'link_flair_type': 'text', 'wls': 6, 'removed_by_category': None, 'banned_by': None, 'author_flair_type': 'text', 'domain': 'self.dataengineering', 'allow_live_comments': False, 'selftext_html': '<!-- SC_OFF --><div class="md"><p>Couchbase? MongoDB? or something else?</p>\n</div><!-- SC_ON -->', 'likes': None, 'suggested_sort': None, 'banned_at_utc': None, 'view_count': None, 'archived': False, 'no_follow': False, 'is_crosspostable': False, 'pinned': False, 'over_18': False, 'all_awardings': [], 'awarders': [], 'media_only': False, 'link_flair_template_id': '069dd614-a7dc-11eb-8e48-0e90f49436a3', 'can_gild': False, 'spoiler': False, 'locked': False, 'author_flair_text': None, 'treatment_tags': [], 'visited': False, 'removed_by': None, 'num_reports': None, 'distinguished': None, 'subreddit_id': 't5_36en4', 'author_is_blocked': False, 'mod_reason_by': None, 'removal_reason': None, 'link_flair_background_color': '#349e48', 'id': '1epl3j7', 'is_robot_indexable': True, 'report_reasons': None, 'author': Redditor(name='DZoneCommunity'), 'discussion_type': None, 'num_comments': 82, 'send_replies': True, 'whitelist_status': 'all_ads', 'contest_mode': False, 'mod_reports': [], 'author_patreon_flair': False, 'author_flair_text_color': None, 'permalink': '/r/dataengineering/comments/1epl3j7/which_databases_are_you_currently_using_in_your/', 'parent_whitelist_status': 'all_ads', 'stickied': False, 'url': 'https://www.reddit.com/r/dataengineering/comments/1epl3j7/which_databases_are_you_currently_using_in_your/', 'subreddit_subscribers': 203729, 'created_utc': 1723383747.0, 'num_crossposts': 0, 'media': None, 'is_video': False, '_fetched': False, '_additional_fetch_params': {}, '_comments_by_id': {}}
