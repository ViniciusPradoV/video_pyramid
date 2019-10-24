from pyramid.view import view_config, view_defaults
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
        "like": 0,
        "dislike": 0,
        "total_score": 0,

        }

        self.collection.insert(video)

        return("video saved")

class Views:
    def __init__(self, request):
        self.request = request

    @view_config(route_name='home', renderer='templates/home.jinja2')
    def home(self):
        db = Database()
        if self.request.POST.get('title'):
            title = str(self.request.POST.get('title'))
            theme = str(self.request.POST.get('theme'))
            db.insert_video(title, theme)

        videos = []
        for video in db.collection.find():
            videos.append(video)
        videos = {"videos": videos}
        return videos
