#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from core.analysis import Analysis
from flask import Flask, request, abort
from flask_cors import CORS
import json

app = Flask(__name__)
app.config.from_pyfile('config/server.cfg')
CORS(app)


@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    return 'hello'


@app.route('/analysis', methods=['POST'])
def analysis_text():
    if not request.json:
        abort(400)
    data = request.json
    analysis = run_analysis(data['row_text'])
    return json.dumps(analysis.out())


def run_analysis(term: str):
    analysis = Analysis(term)
    analysis.run()
    return analysis


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
