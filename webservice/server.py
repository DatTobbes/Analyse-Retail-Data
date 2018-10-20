from flask import request
import numpy as np
import flask
from marshmallow import pprint
from data_aggregation.read_price_data import HistoricalPriceDataReader
from data_aggregation.recommendation_data_reader import RecomondationReader

price_data_reader = HistoricalPriceDataReader()
recommendation_reader = RecomondationReader()

price_df = price_data_reader.get_historical_data_for_device()


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



if __name__ == "__main__":
    print(("* Loading PretrainedClassifier and starting Server..."
           "please wait until Server has fully started"))

    app.run(use_reloader=False, debug=True)
