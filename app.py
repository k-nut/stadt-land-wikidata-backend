from flask import Flask, request, jsonify
from flask_cors import CORS

from controller import check_city, check_river, check_country, example_river, example_city, example_country


app = Flask(__name__)
CORS(app)


def check(function, value):
    result = function(value)
    return jsonify({'data': result})

@app.route("/city")
def city():
    return check(check_city, request.args['name'])


@app.route("/river")
def river():
    return check(check_river, request.args['name'])


@app.route("/country")
def country():
    return check(check_country, request.args['name'])


@app.route("/river_examples")
def river_examples():
    result = example_river(request.args['letter'])
    if result:
        return jsonify({'data': result})
    else:
        return jsonify({'data': None})


@app.route("/city_examples")
def city_examples():
    result = example_city(request.args['letter'])
    if result:
        return jsonify({'data': result})
    else:
        return jsonify({'data': None})


@app.route("/country_examples")
def country_examples():
    result = example_country(request.args['letter'])
    if result:
        return jsonify({'data': result})
    else:
        return jsonify({'data': None})


if __name__ == "__main__":
    app.run()