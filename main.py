import webapp2
import os
import jinja2
from google.appengine.api import users
from models import SchedifyUser

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class LandingHandler(webapp2.RequestHandler):
  def get(self):
    user = users.get_current_user()
    # If the user is logged in...
    if user:
      signout_link_html = '<a href="%s">sign out</a>' % (
          users.create_logout_url('/'))
      email_address = user.nickname()
      schedify_user = SchedifyUser.query().filter(SchedifyUser.email == email_address).get()
      # If the user is registered...
      if schedify_user:
        # Enter home page here:
        # Enter the page that the user sees after they have signed in
        # Greet them with their personal information
        self.response.write('''
            ENTER HOME PAGE TEMPLATE HERE! <br>Welcome %s %s (%s)! <br> %s <br>''' % (
              schedify_user.first_name,
              schedify_user.last_name,
              email_address,
              signout_link_html))
      # If the user isn't registered...
      else:
        # Offer a registration form for a first-time visitor:
        sign_up_template = the_jinja_env.get_template('templates/sign-up.html')
        signout_link = users.create_logout_url('/')
        sign_up_data = {
            "sign_out": signout_link
        }
        self.response.write(sign_up_template.render(sign_up_data))
    else:
      # If the user isn't logged in...
      landing_template = the_jinja_env.get_template('templates/landing.html')
      login_url = users.create_login_url('/')
      landing_data = {
        "login": login_url,
      }
      # Prompt the user to sign in.
      self.response.write(landing_template.render(landing_data))

  def post(self):
    # Enter home page here:
    # Enter the page that the user sees after they have signed in
    user = users.get_current_user()
    schedify_user = SchedifyUser(
        first_name=self.request.get('first_name'),
        last_name=self.request.get('last_name'),
        email=user.nickname())
    schedify_user.put()
    home_template = the_jinja_env.get_template('templates/home.html')
    self.response.write('ENTER HOME PAGE TEMPLATE HERE! <br>Thanks for signing up, %s! <br><a href="/">Home</a>' %
        schedify_user.first_name)
    # home_template = the_jinja_env.get_template('templates/home.html')
    # self.response.write(home_template.render(landing_data))
class HomeHandler(webapp2.RequestHandler):
    def get(self):

        home_template = the_jinja_env.get_template('templates/home.html')
        self.response.write(home_template.render())
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
    ('/', LandingHandler),
    ('/home',HomeHandler),
    ('/schedule', ScheduleHandler),
    ('/new_event', NewEventHandler),
    ('/connections', ConnectionsHandler)

], debug=True)
