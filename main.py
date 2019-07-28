import webapp2
import os
import jinja2

from models import Meme

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class HomeHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(welcome_template.render(meme_data))
    def post(self):
        self.response.write(welcome_template.render(meme_data))
class ScheduleHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(welcome_template.render(meme_data))
    def post(self):
        self.response.write(welcome_template.render(meme_data))
class NewEventHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(welcome_template.render(meme_data))
    def post(self):
        self.response.write(welcome_template.render(meme_data))
class ConnectionsHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(welcome_template.render(meme_data))
    def post(self):
        self.response.write(welcome_template.render(meme_data))


app = webapp2.WSGIApplication([
    ('/', HomeHandler),
    ('/schedule_page', ScheduleHandler),
    ('/new_event_page', NewEventHandler),
    ('/connections_page', ConnectionsHandler)

], debug=True)
