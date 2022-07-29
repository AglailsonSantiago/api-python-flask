from flask_restful import Resource, reqparse

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

class Hotel(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome')
    argumentos.add_argument('estrelas')
    argumentos.add_argument('diaria')
    argumentos.add_argument('cidade')

    def find_hotel(hotel_id):
        for hotel in hoteis:
            if(hotel['hotel_id'] == hotel_id):
                return hotel
        return None

    def get(self, hotel_id):
        hotel = Hotel.find_hotel(hotel_id)

        if hotel:
            return hotel
        return {'message': 'Hotel not found.'}, 404

    def post(self, hotel_id):
        dados = Hotel.argumentos.parse_args()

        novo_hotel = {'hotel_id': hotel_id, **dados}

        hoteis.append(novo_hotel)
        return novo_hotel, 200

    def put(self, hotel_id):
        dados = Hotel.argumentos.parse_args()

        novo_hotel = {'hotel_id': hotel_id, **dados}

        hotel = Hotel.find_hotel(hotel_id)

        if hotel:
            hotel.update(novo_hotel)
            return novo_hotel, 200 #ok
        hoteis.append(novo_hotel)
        return novo_hotel, 201 #criando novo hotel

    def delete(self, hotel_id):
        global hoteis
        hoteis = [hotel for hotel in hoteis if hotel['hotel_id'] != hotel_id]
        return {'message': 'Hotel deletado.'}