from pyramid.view import view_config, view_defaults
from models import Database

class Views:
    def __init__(self, request):
        self.request = request

    @view_config(route_name='home', renderer='templates/home.jinja2')
    def home(self):
        db = Database()

        if self.request.POST.get('title') and self.request.POST.get('theme'):
            print("a")
            title = str(self.request.POST.get('title'))
            theme = str(self.request.POST.get('theme'))
            db.insert_video(title, theme)

        if self.request.POST.get('like') == "1" and self.request.POST.get('title'):
            print("b")
            title = str(self.request.POST.get('title'))
            self.like_video(title)

        if self.request.POST.get('dislike')== "2" and self.request.POST.get('title'):
            print(str(self.request.POST.get('title')))
            title = str(self.request.POST.get('title'))
            self.dislike_video(title)


        videos = []
        videos = db.query_videos()
        videos = {"videos": videos}
        return videos

    def like_video(self, title):
        db = Database()
        title = {"title": title}
        increment_like = {"$inc": {"likes": 1}}
        db.collection.update(title, increment_like)

    def dislike_video(self, title):
        db = Database()
        title = {"title": title}
        increment_dislike = {"$inc": {"dislikes": 1}}
        db.collection.update(title, increment_dislike)

    @view_config(route_name='themes', renderer='templates/themes.jinja2')
    def themes(self):
        db = Database()
        if self.request.POST.get('value'):
            title = str(self.request.POST.get('title'))
            theme = str(self.request.POST.get('theme'))
            db.insert_video(title, theme)
