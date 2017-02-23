from flask import Flask, request, jsonify

from controller import check_city, check_river, check_country


app = Flask(__name__)

@app.route("/city")
def city():
    result = check_city(request.args['name'])
    if result:
        return jsonify({'data': {'link': result, 'correct': True}})
    else:
        return jsonify({'data': {'correct': False}})

@app.route("/river")
def river():
    result = check_river(request.args['name'])
    if result:
        return jsonify({'data': {'link': result, 'correct': True}})
    else:
        return jsonify({'data': {'correct': False}})

@app.route("/country")
def country():
    result = check_country(request.args['name'])
    if result:
        return jsonify({'data': {'link': result, 'correct': True}})
    else:
        return jsonify({'data': {'correct': False}})

if __name__ == "__main__":
    app.run()