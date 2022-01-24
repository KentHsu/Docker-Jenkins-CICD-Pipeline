import os
from pymongo import MongoClient


def connect_to_mongodb():
    username = os.environ["MONGO_GRAPHQL_USERNAME"]
    password = os.environ["MONGO_GRAPHQL_PASSWORD"]
    database = os.environ["MONGO_GRAPHQL_DATABASE"]

    mongo_client = MongoClient(
        "mongodb://mongodb:27017",
        username=username,
        password=password,
        authSource=database
    )
    db = mongo_client[database]

    return db

