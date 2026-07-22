from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/user/<username>')
def user(username):
    return {"username": username, "lastname": "Doe", "age": 30}

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)