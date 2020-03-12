"""
Set up the virtual env with python3
pip3 install twitterscrapper
create a folder name twitter_user_history
to run file: python3 for_one_user.py --uth user_name
EG: python3 for_one_user.py --uth _themessier
"""

import twitterscraper
import json
from datetime import date, datetime
import argparse
import os

parser = argparse.ArgumentParser(description='User Tweeter History.')
parser.add_argument('--uth', help='user_name')

args = parser.parse_args()
FOLDERNAME = "twitter_user_history"

def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError ("Type %s not serializable" % type(obj))
"""
WHILE READING USER_OBJECT

def object_hook(obj):
    _isoformat = obj.get('_isoformat')
    if _isoformat is not None:
        return datetime.fromisoformat(_isoformat)
    return obj

USEAGE:
import json
from datetime import date, datetime

json.loads(filename, object_hook=object_hook)
"""
class ForOneUser():
    def __init__(self, username):
        self.username = username
        self.history_object = []

    def scrape_history(self):
        try:
            history_scraped = twitterscraper.query_tweets_from_user(
                self.username)
            for each_obj in history_scraped:
                save_json = {}
                save_json["screen_name"] = each_obj.screen_name
                save_json["username"] = each_obj.username
                save_json["user_id"] = each_obj.user_id
                save_json["tweet_id"] = each_obj.tweet_id
                save_json["tweet_url"] = each_obj.tweet_url
                save_json["timestamp"] = each_obj.timestamp
                save_json["timestamp_epochs"] = each_obj.timestamp_epochs
                save_json["text"] = each_obj.text
                save_json["text_html"] = each_obj.text_html
                save_json["links"] = each_obj.links
                save_json["hashtags"] = each_obj.hashtags
                save_json["has_media"] = each_obj.has_media
                save_json["img_urls"] = each_obj.img_urls
                save_json["video_url"] = each_obj.video_url
                save_json["likes"] = each_obj.likes
                save_json["retweets"] = each_obj.retweets
                save_json["replies"] = each_obj.replies
                save_json["is_replied"] = each_obj.is_replied
                save_json["is_reply_to"] = each_obj.is_reply_to
                save_json["parent_tweet_id"] = each_obj.parent_tweet_id
                save_json["reply_to_users"] = each_obj.reply_to_users
                self.history_object.append(save_json)
            self.save_history()

        except Exception as e:
            print("Error Occured for user = {} ".format(self.username))
            raise e

    def save_history(self):
        with open(os.path.join(FOLDERNAME, self.username + ".json"), "w") as f:
            json.dump(self.history_object, f, indent=True, default=json_serial)

    def execute(self):
        self.scrape_history()
        self.save_history()

if __name__ == "__main__":
    if args.uth:
        for_user_obj = ForOneUser(args.uth)
        for_user_obj.execute()
    else:
        print("user name not provided.")