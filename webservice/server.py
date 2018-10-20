from flask import request
import numpy as np
import flask

from data_aggregation.read_price_data import HistoricalPriceDataReader
from data_aggregation.recommendation_data_reader import RecomondationReader
from data_aggregation.aggregate import DataFrameReader

price_data_reader = HistoricalPriceDataReader()
recommendation_reader = RecomondationReader()
price_df = price_data_reader.get_historical_data_for_device()

device_data_reader = DataFrameReader()

app = flask.Flask(__name__)
model = None


@app.route("/get_minprices", methods=["GET"])
def get_minprice():
    """
    :return: returns all classnames to Client
    """

    if flask.request.method == "GET":
        return flask.jsonify(price_df['min_price'])


@app.route("/prices_for", methods=["POST"])
def get_min_price_for_device():
    if flask.request.method == "POST":
        device = request.json.get('data')
        df = price_data_reader.get_historical_data_for_device(device)

        result = flask.jsonify(df['min_price'])

    return flask.jsonify(result)


@app.route("/recommendations", methods=["POST"])
def get_recommendations_for_device():
    if flask.request.method == "POST":
        device = request.json.get('data')
        df = price_data_reader.get_historical_data_for_device(device)

        result = flask.jsonify(df['min_price'])

    return flask.jsonify(result)

@app.route("/devicedata", methods=["POST"])
def get_all_device_data():
    if flask.request.method == "POST":
        device = request.json.get('data')
        device_data = device_data_reader.create_device_data(device)

        result = flask.jsonify(device_data)

    return flask.jsonify(result)

if __name__ == "__main__":
    print("")

    app.run(use_reloader=False, debug=True)
