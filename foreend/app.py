from flask import Flask,request,jsonify, abort
import requests
import os
import time
import logging

app = Flask(__name__)
app.logger.setLevel(logging.DEBUG)
backend_service_url = os.getenv('BACKEND_SERVICE_URL')

@app.route('/')
def home():
    param_value = request.args.get('panic')
    if param_value == "1":
        abort(500)
    time.sleep(1) # 测试超时
    s = requests.Session()
    headers = dict(request.headers)
    headers['Connection'] = 'close'
    s.headers.update(headers)
    response = s.get(backend_service_url+'/backend')
    data = response.json()
    return jsonify(data), 200

@app.route('/default')
def default():
    return jsonify({"message":"default"}),200

@app.route('/circlebreak')
def circlebreak():
    times = 100
    headers = dict(request.headers)
    headers.update({'Connection': 'close'})
    times_args = request.args.get('times')
    if times_args:
        try:
            times = int(times_args)
        except ValueError:
            pass
    url = backend_service_url+'/circlebreak'
    for i in range(0,times):
        response = requests.get(url,headers=headers)
        print(url,response.status_code)
    return jsonify({"message":"circle break"}),200

if __name__ == '__main__':
     app.run(host='0.0.0.0',port=80)