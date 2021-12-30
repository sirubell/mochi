from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/ping')
def ping():
    return 'pong'

@app.route('/problem', methods=['GET'])
def problem_table():
    for item in request.args:
        print(item, request.args.get(item))
    return request.args;
    
@app.route('/register', methods=['POST'])
def signup():
    return "OK"

if __name__ == '__main__':
    app.run()
