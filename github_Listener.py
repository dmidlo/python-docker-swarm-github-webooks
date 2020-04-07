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
    return json.dumps(request.json)

if __name__== '__main__':
  app.run (debug=True)
