from flask import request, jsonify
from stadt_land_wikidata import app
from stadt_land_wikidata.controller import check_city, check_river, check_country, example_river, example_city, example_country
from stadt_land_wikidata import controller

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


@app.route("/profession")
def profession():
    return check(controller.check_profession, request.args['name'])


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


@app.route("/profession_examples")
def profession_examples():
    result = controller.example_profession(request.args['letter'])
    if result:
        return jsonify({'data': result})
    else:
        return jsonify({'data': None})