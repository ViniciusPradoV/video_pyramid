from pymongo import MongoClient

class Database(object):

    def __init__(self):
        self.client = MongoClient()
        self.db = self.client["videos"]
        self.collection = self.db["videos"]

    def insert_video(self, title, theme):
        video = {
        "title": title,
        "theme": theme,
        "likes": 0,
        "dislikes": 0,
        "total_score": 0,

        }

        self.collection.insert(video)

        return("video saved")

    def query_videos(self):
        videos = []
        for video in self.collection.find():
            videos.append(video)
        return videos
