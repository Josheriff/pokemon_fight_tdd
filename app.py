from flask import Flask
from flask_restful import Resource, Api

from trainer.view import TrainerReciver


app = Flask(__name__)
api = Api(app)

api.add_resource(TrainerReciver, '/trainer')

if __name__ == '__main__':
    # Debug mode should never be used in a production environment!
    app.run()