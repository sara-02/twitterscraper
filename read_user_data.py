import json
from datetime import date, datetime
import os


def object_hook_(obj):
    _isoformat = obj.get('_isoformat')
    if _isoformat is not None:
        return datetime.fromisoformat(_isoformat)
    return obj


FOLDERNAME = "twitter_user_history"
with open(os.path.join(FOLDERNAME, "_themessier.json"), "r") as f:
    data = json.load(f, object_hook=object_hook_)
for each_obj in data:
    print(each_obj)