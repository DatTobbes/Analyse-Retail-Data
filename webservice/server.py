from flask import request
import numpy as np
import flask
from flask_cors import cross_origin


from data_aggregation.aggregate import DataFrameReader

device_data_reader = DataFrameReader()

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

if __name__ == "__main__":
    print("")

    app.run(use_reloader=False, debug=True)
