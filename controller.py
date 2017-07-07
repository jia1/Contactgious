from flask import Flask, request
from soccat import emeow

app = Flask(__name__)
app.config.from_pyfile('openshift.cfg')

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/connect', methods = ('POST', ))
def connect():
    data = request.get_json()
    return emeow(app, data)

@app.route('/ping', methods = ('GET', ))
def ping():
    emeow(
        app,
        {
          "enquiry":"9",
          "name":"jiayee",
          "email":"jia10@u.nus.edu",
          "message":"Help!"
        }
    )
    return 'OK'

@app.after_request
def set_headers(resp):
  resp.headers['Access-Control-Allow-Headers'] = 'Content-Type'
  resp.headers['Access-Control-Allow-Origin'] = 'http://localhost:1313'
  return resp

if __name__ == '__main__':
    app.run(debug = True)
