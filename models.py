
from google.appengine.ext import ndb

# Change to user
class SchedifyUser(ndb.Model):
    first_name = ndb.StringProperty()
    last_name = ndb.StringProperty()
    username = ndb.StringProperty()
    email = ndb.StringProperty()
    friends = ndb.KeyProperty(kind="SchedifyUser", repeated=True)
    requests = ndb.KeyProperty(kind="SchedifyUser", repeated=True)

    def add_request(self, key):
        self.requests.append(key)
        self.put()

    def remove_request(self, key):
        self.requests.remove(key)
        self.put()

    def add_friend(self, key):
        self.friends.append(key)
        self.put()

    def remove_friend(self, key):
        self.friends.remove(key)
        self.put()
        # searches through the friend list and removes friend

# not implemented yet
# do not even need
class Connect(ndb.Model):
    user_one = ndb.KeyProperty(SchedifyUser)
    user_two = ndb.KeyProperty(SchedifyUser)
    # set that holds the key for both users
    # can you call Graph.connections?
    # if you can then appengine will store a list/dict (check)
    #   of sets (of user keys)
    # this will make graph ultimately a set of two user keys.

    # dict that holds several connections
    # if you call a dictionary of sets,

    # maybe make a function where you create a set and
    # return a set

class Event(ndb.Model):
    owner = ndb.KeyProperty(SchedifyUser)
    title = ndb.StringProperty()
    summary = ndb.StringProperty()
    # property where if empty then this event will be shared with all
    #   friends, if it has elements then this will only be shared with those
    #   users
    exclusives = ndb.KeyProperty(SchedifyUser, repeated=True)
    attending = ndb.KeyProperty(SchedifyUser, repeated=True)
    not_attending = ndb.KeyProperty(SchedifyUser, repeated=True)


# do not even need
class Attendance(ndb.Model):
    user = ndb.KeyProperty(SchedifyUser)
    event = ndb.KeyProperty(Event)
