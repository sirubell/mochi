from flask import Flask, request
import json

app = Flask(__name__)


@app.route('/')
def main():
    res = {
		 "student_list":
        [
            {"id": 1, "name": "Jay", "email": "Jay@gmail.com", "password": "123456"},
            {"id": 2, "name": "Briton","email": "Briton@gmail.com", "password": "123456"},
            {"id": 4, "name": "Tony", "email": "Tony@gmail.com", "password": "123456"},
			{"id": 5, "name": "jeff", "email": "Tony@gmail.com", "password": "46546"}
        ]
    }
    return json.dumps(res)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000)
