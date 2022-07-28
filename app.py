from distutils.log import debug
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

hoteis = [
    {
        'hotel_id': 'alpha',
        'nome': 'Alpha Hotel',
        'estrelas': 4,
        'diaria': 420.45,
        'cidade': 'Rio de Janeiro'
    },
    {
        'hotel_id': 'beta',
        'nome': 'Beta Hotel',
        'estrelas': 3,
        'diaria': 349.99,
        'cidade': 'São Paulo'
    },
    {
        'hotel_id': 'gama',
        'nome': 'Gama Hotel',
        'estrelas': 5,
        'diaria': 550.49,
        'cidade': 'Fortaleza'
    }
]

class Hoteis(Resource):
    def get(self):
        return {'hoteis': hoteis}

api.add_resource(Hoteis, '/hoteis')

if __name__ == '__main__':
    app.run(debug=True)