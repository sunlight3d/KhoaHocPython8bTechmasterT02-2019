from flask import *
from flask_restful import *
from flask_restful import reqparse
from flask import jsonify

#import json
class ProductApi(Resource):
    """GET"""
    """
    List products by paging
    http://localhost:5000/products?page_number=1&number_of_records=25
    """
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('page_number', type=int)
        parser.add_argument('number_of_records', type=int)
        args = parser.parse_args()
        print("args = "+str(args))
        products = {"products": [{"name": "iphone X", "year": 2017},{"name": "iphone 5", "year": 2015}]} 
        #JSON = Javascript Object Notation
        return jsonify(products)
    """Insert a new record"""
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('product_name')
        parser.add_argument('year', type=int)
        args = parser.parse_args()
        print("args = "+str(args))
        result = {"result": "ok", "message": "Insert new product successfully"}
        return jsonify(result)
    """PUT = update an existing record"""
    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument('product_id', type=int)
        parser.add_argument('product_name')
        parser.add_argument('year', type=int)
        args = parser.parse_args()
        print("args PUT = "+str(args))
        result = {"result": "ok", "message": "Update a product successfully"}
        return jsonify(result)
    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument('product_id', type=int)
        args = parser.parse_args()
        print("args DELETE = "+str(args))
        result = {"result": "ok", "message": "Delete a product successfully"}
        return jsonify(result)
