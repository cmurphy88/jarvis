from flask import Flask, jsonify

app = Flask(__name__);


@app.route('/login', methods=['POST'])
def login_user():
    return jsonify({'result': 'user logged in successfully'})


app.run()
