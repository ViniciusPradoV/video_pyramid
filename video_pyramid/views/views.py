from pyramid.view import view_config, view_defaults
from pymongo import MongoClient

@view_defaults(renderer='templates/layout.jinja2')
class Views:
    def __init__(self, request):
        self.request = request

    def home(self):
        return{'name': 'Home View'}
