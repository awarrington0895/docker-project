from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Product(Resource):
    def get(self):
        return {
            'products': [
                'The Razor\'s Edge',
                '...And Justice For All',
                'The Sickness',
                'Highway to Hell',
                'Houses of the Holy',
                'Stiff Upper Lip',
                'Creedence Clearwater Revival'


            ]
        }

api.add_resource(Product, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
