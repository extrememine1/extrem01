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

# test data framework 1
DATA_FILE = 'test1.json'
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f)

data1 = load_data()

@app.route('/school/funnydatabase', methods=['POST', 'GET'])
def index1():
    global data1

    def get_client_ip():
        if request.headers.getlist("X-Forwarded-For"):
            return request.headers.getlist("X-Forwarded-For")[0].split(',')[0]
        return request.remote_addr
    
    if request.method == 'GET':
        payload = {
            'content': f'{get_client_ip()} has requested for the data'
        }
        requests.post(webhook, json=payload)
        
        return jsonify(data1)

    elif request.method == 'POST':
        newdata = request.get_json()
        data1 = newdata

        payload = {
            'content': f'{get_client_ip()} has changed the data to {newdata}'
        }
        requests.post(webhook, json=payload)

        return jsonify({'received': newdata}), 200

app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
save_data()
