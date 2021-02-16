import os
import json 
from flask import Flask, jsonify
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)

from pdf2image import convert_from_path

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/pdfs', methods=['GET'])
def getPDFs():
    f = open(APP_ROOT+'/static/pdfs/pdfs.json', "r")
    data = json.load(f) 
    print(data)

    response = jsonify(data)

    response.headers['Access-Control-Allow-Origin'] = '*'

    # Enable Access-Control-Allow-Origin
    
    return response

if __name__ == '__main__':
    app.run()
