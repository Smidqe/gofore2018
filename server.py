import json
import flask

from flask import request
from recipebook import RecipeBook

#setup the necessary variables
app = flask.Flask(__name__)
book = RecipeBook()
book.load()

'''
    Very simplistic flask server, handles the GET requests coming to /search address

    Required query params for /search:
        - ingredient: string
'''


@app.route('/search', methods=['GET'])
def search():
    result = None
    #could have some checks about headers here?

    #check if the ingredient is in the query parameters
    if ('ingredient' in request.args):
        result = book.search('ingredient', request.args['ingredient'])

    #jsonify the response and send it to the requester
    return flask.jsonify(result)

@app.route('/recipes', methods=['GET', 'POST'])
def recipes():
    return None
