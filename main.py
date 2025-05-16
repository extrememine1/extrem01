from flask import *
import requests
import os

app = Flask(__name__)
webhook = 'https://discord.com/api/webhooks/1364252228671766629/Ew6SypiVloyb5UIrShLa4pNpnNPWF1fg61VNndn2Z7kGyssBNl6ktF8AUifuYtwJkp9X'

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
data1 = {}

@app.route('/school/funnydatabase', methods=['POST', 'GET'])
def index1():
    global data1
    
    if request.method == 'GET':
        payload = {
            'content': f'{request.remote_addr} has requested for the data'
        }
        requests.post(webhook, json=payload)
        return jsonify(data1)

    elif request.method == 'POST':
        newdata = request.get_json()
        data1 = newdata

        payload = {
            'content': f'{request.remote_addr} has changed the data to {newdata}'
        }
        requests.post(webhook, json=payload)

        return jsonify({'received': newdata}), 200

app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
