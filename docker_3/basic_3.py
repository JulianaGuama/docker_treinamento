import os
import logging
from flask import Flask, request, jsonify

app = Flask('basic_3')

logging.basicConfig(level=logging.DEBUG)


@app.route('/', methods=['GET', 'POST', 'PUT'])
def main():
    body = request.get_json()

    if request.method == 'GET':
        app.logger.info(' method is GET')
        return jsonify(method='GET', pyEnviron=os.environ.get('myVar')) #->
    if request.method == 'POST':
        app.logger.info(' method is POST')
        app.logger.warning(' not a GET')
        return jsonify(method='POST', pyEnviron=os.environ.get('myVar')) #->
    else:
        app.logger.error(' method is PUT')
        return 'erro', 500


if __name__ == '__main__':
      app.run(debug=True, host='0.0.0.0', port=5000)

