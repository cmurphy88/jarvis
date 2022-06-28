from flask import Flask, jsonify

app = Flask(__name__);


@app.route('/users', methods=['GET'])
def get_users():
  return jsonify([
        {'id': 546, 'username': 'John'},
        {'id': 894, 'username': 'Mary'},
        {'id': 326, 'username': 'Jane'}
    ])


@app.route('/users', methods=['DELETE'])
def delete_user():
    return jsonify({'result': 'success'})


@app.route('/register', methods=['POST'])
def register_user():
    return jsonify({'result': 'user registered'})


@app.route('/login', methods=['POST'])
def login_user():
    return jsonify({'result': 'user logged in successfully'})


@app.route('/join', methods=['POST'])
def join_user_home():
    return jsonify({'result': 'user joined home successfully'})


@app.route('/me', methods=['GET'])
def profile():
    return jsonify({'id': '1', 'name': 'conor'})


@app.route('/me', methods=['PUT'])
def users_update():
    return jsonify({'result': 'email updated'})


@app.route('/me', methods=['DELETE'])
def users_delete():
    return jsonify({'result': 'user profile has been deleted'})


@app.route('/users/1/homes/1', methods=['POST'])
def add_homes():
    return jsonify({'result': 'home has been added to the system successfully'})


@app.route('/users/1/homes/1', methods=['PUT'])
def update_homes():
    return jsonify({'result': 'home settings have been successfully changed'})


@app.route('/users/1/homes/1', methods=['DELETE'])
def del_homes():
    return jsonify({'result': 'home has been been deleted successfully'})


app.run()
