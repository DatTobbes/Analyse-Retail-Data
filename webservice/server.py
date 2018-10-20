from flask import request
import numpy as np
import flask
from flask_cors import cross_origin


from data_aggregation.aggregate import DataFrameReader
from data_aggregation.retailer_data import RetailerData

device_data_reader = DataFrameReader()
retailer = RetailerData()

app = flask.Flask(__name__)
model = None

@app.route("/devicedata", methods=["POST"])
@cross_origin()
def get_all_device_data():
    if flask.request.method == "POST":
        device = request.json.get('data')
        print(device)
        device_data = device_data_reader.create_device_data(device)

        result = flask.jsonify(device_data)

    return result

@app.route("/getInventory", methods=["GET"])
@cross_origin()
def get_retailer_inventory():
    if flask.request.method == "GET":
        inventory = retailer.get_inventory()
        result = inventory.to_json()

    return result


@app.route("/getDeviceFromInventory", methods=["POST"])
@cross_origin()
def get_device_from_inventory():
    if flask.request.method == "POST":

        device = request.json.get('data')
        print(device)
        device_data = retailer.get_device_from_inventory(device)
        result = device_data.to_json()

    return result


@app.route("/getDeviceAndNeighbours", methods=["POST"])
@cross_origin()
def get_device_and_neighbours():
    if flask.request.method == "POST":

        device = request.json.get('data')
        device_data = retailer.get_neighbours_from_device(device)
        result = device_data.to_json()

    return result

@app.route("/getDeviceList", methods=["GET"])
@cross_origin()
def get_device_list():
    if flask.request.method == "GET":

        device_data = retailer.get_device_list()
        result = device_data.to_json()

    return result


if __name__ == "__main__":
    print("")

    app.run(use_reloader=False, debug=True)
