from flask import *
import os

app = Flask(__name__)

@app.route('/second_largest', methods=['POST'])
def secondLargest():
    ls = request.get_json()

    ls.sort(reverse=True)
    return jsonify(ls[1])

app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
