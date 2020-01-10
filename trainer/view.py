import flask
from flask_restful import Resource

class TrainerReciver(Resource):
    def post(self):
        data = flask.request.json
        self.capitalize(data)
        return data
    
    def capitalize(self, data):
        # return [{"name":"Aname"}, {"name": "Anothername"}]
        for name in data:
            name['name'] = name['name'].capitalize()
        
        return data
    
    
