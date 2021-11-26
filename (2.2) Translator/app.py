import os
import uuid
import requests
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify

load_dotenv()

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def dict_page():
    return render_template('dict.html')


@app.route('/translate', methods=['POST'])
def index_post():
    data = request.get_json()
    original_text = data['translate']
    from_language = data['from']
    to_language = data['to']

    key = os.environ['KEY']
    endpoint = os.environ['ENDPOINT']
    location = os.environ['LOCATION']
    path = '/translate?api-version=3.0&'
    target_language_parameter = 'from=' + from_language + '&to=' + to_language
    constructed_url = endpoint + path + target_language_parameter

    headers = {
        'Ocp-Apim-Subscription-Key': key,
        'Ocp-Apim-Subscription-Region': location,
        'X-ClientTraceId': str(uuid.uuid4())
    }
    body = [{'text': original_text}]

    translator_response = requests.post(constructed_url, headers=headers, json=body)
    return jsonify(translator_response.json())


if __name__ == '__main__':
    app.run()
