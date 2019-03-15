from flask import *
from flask_restful import *
from flask_restful import reqparse
from flask import jsonify
from database import *
#..python.exe -m pip install flask
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
        db = Database.get_instance()
        result, message = db.insert_new_product(args['product_name'], args['year'])
        return jsonify({"result": result, "message": message})
    """PUT = update an existing record"""
    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument('product_id', type=int)
        parser.add_argument('product_name')
        parser.add_argument('year', type=int)
        args = parser.parse_args()
        Database.get_instance().update_product(args['product_id'],\
                    args['product_name'],args['year'])
        print("args PUT = "+str(args))
        result = {"result": "ok", "message": "Update a product successfully"}
        return jsonify(result)
    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument('product_id')
        args = parser.parse_args()
        print("args DELETE = "+str(args))
        result, message = Database.get_instance().delete_product(str(args['product_id']))
        return jsonify({"result": result, "message": message})
