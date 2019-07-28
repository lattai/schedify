import webapp2
import os
import jinja2

from models import Meme

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)














app = webapp2.WSGIApplication([
    ('/', HomeHandler),
    ('/schedule_page', ScheduleHandler),
    ('/new_event_page', NewEventHandler),
    ('/connections_page', ConnectionsHandler)

], debug=True)
