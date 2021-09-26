import tweepy
from typing import Any, Dict, List
from fastapi import FastAPI

from services import get_trends_from_mongo, save_trends
from responses import TrendItem
from constants import BRAZIL_WOE_ID

app = FastAPI()

@app.get("/trends", response_model= List[TrendItem])
def get_trends_route():
    return get_trends_from_mongo()

if __name__ == "__main__":
    trends = get_trends_from_mongo()

    if not trends:
        save_trends()

