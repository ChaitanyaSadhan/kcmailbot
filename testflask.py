from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello():
    strhello = "hello world"
    return jsonify({'data':strhello})


if __name__ == '__main__':
    app.run()