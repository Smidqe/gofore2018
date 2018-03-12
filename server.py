import json
import flask

from flask import request
from recipebook import RecipeBook
from recipe import Recipe

app = flask.Flask(__name__)
book = RecipeBook()
book.load()

'''
    Very simplistic flask server


'''


@app.route('/search', methods=['GET'])
def search():
    result = None

    #check if the ingredient is in the query parameters
    if ('ingredient' in request.args):
        result = book.search('ingredient', request.args['ingredient'])

    return flask.jsonify(result)


