from flask import Flask
from flask import render_template, request, redirect, url_for
from sqllite import *
import json

app = Flask(__name__)

@app.route('/Products', methods = ['GET', 'POST'])
def getproduct():
    conn = sqlite3.connect('Products.db')

    if request.method == 'GET':
        results = get_all_Products(conn)

        # turn the list into json
        json_results = []
        for emp in results:
            json_results.append(json.dumps(emp.__dict__))
        return json.dumps(json_results)

    if request.method == 'POST':
        print(request.get_json())
        obj = request.get_json()
        e = Products(obj['id'], obj['name'], obj['price'], obj['quantity'])
        insert_into_Products_table(conn, e)
        return '{ "result": "inserted" }'

@app.route('/Products/<int:id>', methods=['GET', 'DELETE', 'PUT'])
def getproduct_with_id(id):
    conn = sqlite3.connect('Products.db')

    if request.method == 'GET':
        result = get_Products_by_id(conn, id)
        # turn the item into json
        return json.dumps(result.__dict__)

    if request.method == 'DELETE':
        delete_Products(conn, id)
        return '{ "result": "deleted" }'

    if request.method == 'PUT':
        obj = request.get_json()
        e = Products(obj['id'], obj['name'], obj['price'], obj['quantity'])
        update_Products(conn, e, id)
        return '{ "result": "updated" }'

app.run()