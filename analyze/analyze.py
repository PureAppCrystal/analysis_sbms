import json
import re

from konlpy.tag import Twitter
from collections import Counter


def json_to_str(filename, key):
    jsonfile = open(filename, 'r', encoding='utf-8')
    json_string = jsonfile.read()
    jsondata = json.loads(json_string)

    data = ''
    for item in jsondata:
        value = item.get(key)
        if value is None:
            continue

        # ^\w -> 화이트 스페이스
        data += re.sub(r'[^\w]', '',  value)

    return data


def count_wordfreq(data):
    twitter = Twitter()
    nouns = twitter.nouns(data)

    count = Counter(nouns)
    return count
