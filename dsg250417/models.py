from google.appengine.ext import ndb

class ToDo(ndb.Model):
    title = ndb.StringProperty(required=True)
    author = ndb.StringProperty()
    text = ndb.TextProperty()
    deadline = ndb.DateTimeProperty()
    keyword = ndb.StringProperty(repeated=True)

