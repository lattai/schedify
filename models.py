
from google.appengine.ext import ndb

# Change to user
class SchedifyUser(ndb.Model):
    first_name = ndb.StringProperty()
    last_name = ndb.StringProperty()
    email = ndb.StringProperty()

# not implemented yet
class Connect(ndb.Model):
    user_one = ndb.KeyProperty(SchedifyUser)
    user_two = ndb.KeyProperty(SchedifyUser)
    # set that holds the key for both users
    # can you call Graph.connections?
    # if you can then appengine will store a list/dict (check)
    #   of sets (of user keys)
    # this will make graph ultimately a set of two user keys.
    connections = {user_one, user_two}
    # dict that holds several connections
    # if you call a dictionary of sets,

    # maybe make a function where you create a set and
    # return a set

class Event(ndb.Model):
    title = ndb.StringProperty()
    summary = ndb.StringProperty()

class Attendance(ndb.Model):
    user = ndb.KeyProperty(SchedifyUser)
    event = ndb.KeyProperty(Event)
