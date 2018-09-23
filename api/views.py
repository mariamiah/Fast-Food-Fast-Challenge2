from flask import request, jsonify, json
from api.models import Order
from api import app


orders = []


@app.route('/api/v1/orders', methods=['POST'])
def create_order():
    special_chars = ["!", "@", "#", "$", "%", "^", "&", "*", "~", "|"]
    data = request.get_json()

    if data['order_name'] == "":
        return jsonify({'message': "Enter order_name"}), 400

    if data['order_type'] == "":
        return jsonify({"message": "Please add the order_type"}), 400

    if data['user_name'] == "":
        return jsonify({'message': 'Username cannot be blank'}), 400

    for letter in data['order_name']:
        if letter in special_chars:
            return jsonify({
                'Message': "OrderName cannot contain special characters"}), 400

    for letter in data['order_type']:
        if letter in special_chars:
            return jsonify({
                'message': 'ordertype cannot contain special characters'}), 400

    for letter in data['user_name']:
        if letter in special_chars:
            return jsonify({
                'message': 'user name cannot contain special characters'}), 400
    try:
        if isinstance(data['order_name'], str) and \
           isinstance(data['order_type'], str):
            order_id = len(orders)
            order_id += 1
            order = Order(order_id, data['order_name'], data['order_type'],
                          data['user_name'])
            orders.append(order)
        return jsonify({"Message": "Order successfully placed!"}), 201
    except ValueError:
        return jsonify({"Message": "Invalid fields"}), 400


@app.route('/api/v1/orders', methods=['GET'])
def fetch_all_orders():
    Orders = [order.get_dict() for order in orders]
    return jsonify({'message': Orders}), 200


@app.route('/api/v1/orders/<int:order_id>', methods=['GET'])
def get_order_id(order_id):
    single_order = []
    if order_id == 0 or order_id > len(orders):
        return jsonify({"message": "Index out of range"}), 400

    if order_id != 0 and order_id <= len(orders):
        order = orders[order_id - 1]
        single_order.append(order.get_dict())
        return jsonify({'Order': single_order, 'status': 'Succeeded'}), 200


@app.route('/api/v1/orders/<int:order_id>', methods=['PUT'])
def update_specific_order(order_id):
    pass
