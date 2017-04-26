import webapp2
import json
import datetime

from models import *
from utils import *

class ToDosHandler(webapp2.RequestHandler):
    def get(self):
            query = Todo.query()
            data = [todo.to_dict() for todo in query]
            self.response.headers['Content-Type'] = 'application/json; charset=utf-8'
            self.response.write(data2json(data))
                

    def post(self):
        data = json.loads(self.request.body)
        newtodo = Todo()
        newtodo.title = data['title']
        newtodo.author = data.get('author')
        newtodo.text = data.get('text')
        deadline = data.get('deadline', datetime.datetime.now().isoformat().split(".")[0])
        newtodo.deadline = datetime.datetime.strptime(deadline, "%Y-%m-%dT%H:%M:%S")
        newtodo.put()
        self.response.write('{"iid": "%d"}' % newtodo.key.integer_id())
        self.response.set_status(201)


app = webapp2.WSGIApplication([
    ('/api/todo', ToDosHandler),
], debug=True)
