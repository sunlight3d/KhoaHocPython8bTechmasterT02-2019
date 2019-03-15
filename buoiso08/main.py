"""
python -m pip install flask_restful 
python -m pip install flask
"""
from flask import *
from flask_restful import *
#from flask import jsonify
from product import ProductApi

PORT = '5000'

app = Flask(__name__)
api = Api(app)
"""Router"""
"""
Test: Send request to: SEND USING Postman
http://localhost:5000/products
"""
api.add_resource(ProductApi, "/products")
"""Start server in port - 5000"""
app.run(port=PORT, debug=True)