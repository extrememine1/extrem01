
from flask import *
import requests
import os

app = Flask(__name__)
webhook = os.getenv('webhook') # womp womp

@app.route('/', methods=['GET'])
def iter_main_routes():
    return jsonify(['school'])

# ts for school projects
@app.route('/school', methods=['GET'])
def iter_func_school():
    return jsonify(['second_largest', 'funnydatatbase'])

@app.route('/school/second_largest', methods=['POST'])
def secondLargest():
    ls = request.get_json()
    payload = {
        'content': f'The list {ls} has been posted, processing the list now'
    }
    requests.post(webhook, json=payload)

    ls.sort(reverse=True)
    return jsonify(ls[1])

@app.route('/school/ipgrabber', methods['GET'])
def index():
    ip = request.headers.get('X-Forwarded-For', request.remote_addr).split(',')[0].strip()

    return ip

app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
