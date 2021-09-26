from typing import Any, Dict, List

import tweepy

from secrets import ACCESS_TOKEN, ACCESS_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET
from connection import trends_collection
from constants import BRAZIL_WOE_ID
def _get_trends(woe_id: int, api: tweepy.API) -> List[Dict[str, Any]]: 
    """ Get treending topics.

    Args:
        woe_id (int): Identifier of location.

    Returns:
        List[Dict[str, Any]]: Trends List.
     """

    trends = api.trends_place(woe_id)

    print(trends)

    return trends[0]["trends"]


def get_trends_from_mongo() -> List[Dict[str, Any]]:
    trends = trends_collection.find({})
    return list(trends)


def save_trends() -> None:
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)

    trends = _get_trends(woe_id = BRAZIL_WOE_ID, api= api)
    trends_collection.insert_many(trends)