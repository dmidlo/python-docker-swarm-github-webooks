from flask import json
from flask import request
from flask import Flask

app = Flask(__name__)

@app.route('/')
def api_root():
  return 'Welcome Guys'

@app.route('/github', methods=['POST'])
def api_gh_wildcard():
  if request.headers['Content-Type'] == 'application/json':
    result = json.dumps(request.json)
    print(result)
    return result

@app.route('/dockerhub', methods=['POST'])
def api_dh_wildcard():
  if request.headers['Content-Type'] == 'application/json':
    result = json.dumps(request.json)
    print(result)
    return result

if __name__== '__main__':
  app.run(debug=True, host='0.0.0.0')
