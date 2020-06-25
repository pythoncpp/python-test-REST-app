from flask import Flask, request, jsonify
from database import Database

app = Flask(__name__)


@app.route('/', methods=['GET'])
def root():
    return '<h1>welcome to my REST App<h1>'


@app.route('/product', methods=['GET'])
def get_products():
    db = Database()
    query = "select id, title, price from product"
    result = db.select(query)
    products = []
    for (id, title, price) in result:
        products.append({
            "id": id,
            "title": title,
            "price": price
        })

    return jsonify(products)


@app.route('/product', methods=['POST'])
def post_product():
    title = request.form.get('title')
    price = request.form.get('price')

    db = Database()
    statement = f"insert into product (title, price) values ('{title}', {price})"
    db.execute(statement)

    return {"status": "success"}


@app.route('/product', methods=['PUT'])
def put_product():
    title = request.form.get('title')
    price = request.form.get('price')
    id = request.args.get('id')

    db = Database()
    statement = f"update product set title = '{title}', price = {price} where id = {id}"
    db.execute(statement)

    return {"status": "success"}


@app.route('/product', methods=['DELETE'])
def delete_product():
    id = request.args.get('id')

    db = Database()
    statement = f"delete from product where id = {id}"
    db.execute(statement)

    return {"status": "success"}


app.run(host='0.0.0.0', port=4000)
