from flask import Flask,jsonify,request,abort
import os
import random
import logging

app = Flask(__name__)
app.logger.setLevel(logging.DEBUG)

@app.route('/backend')
def goods():
    data = {
        'Pod名字': os.getenv('HOSTNAME'),
        '服务版本': os.getenv('VERSION')
        }
    return jsonify(data)

@app.route('/circlebreak')
def circlebreak():
    if os.getenv('VERSION') == "v2":
        abort(500)
    return jsonify({"message":"ok"})

if __name__ == '__main__':
     app.run(host='0.0.0.0',port=80)