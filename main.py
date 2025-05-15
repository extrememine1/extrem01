from flask import *
import requests
import os

app = Flask(__name__)
webhook = 'https://discord.com/api/webhooks/1364252228671766629/Ew6SypiVloyb5UIrShLa4pNpnNPWF1fg61VNndn2Z7kGyssBNl6ktF8AUifuYtwJkp9X'

@app.route('/second_largest', methods=['POST'])
def secondLargest():
    ls = request.get_json()
    payload = {
        'content': f'The list {ls} has been posted, processing and responding the list now'
    }
    requests.post(webhook, json=payload)

    ls.sort(reverse=True)
    return jsonify(ls[1])

app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
