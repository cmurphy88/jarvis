from flask import Flask, jsonify

app = Flask(__name__);


@app.route('/homes', methods=['POST'])
def create_home():
    return jsonify({'result': 'home created successfully'})


@app.route('/homes/<id>', methods=['PUT'])
def update_home(id):
    home_id = id
    return jsonify({'home_id': '456', 'result': 'home updated successfully'})


@app.route('/homes', methods=['GET'])
def get_homes():
    return jsonify({'home_id': '456', 'home_name': 'My Belfast Home'},
                   {'home_id': '554', 'home_name': 'My Fermanagh Home'},
                   {'home_id': '888', 'home_name': 'My Third Home'}
                   )


@app.route('/homes/<id>', methods=['GET'])
def get_home(id):
    home_id = id
    return jsonify({'home_id': '456', 'home_name': 'Conors Home'})


@app.route('/homes/<id>/users', methods=['GET'])
def get_home_users(id):
    home_id = id
    return jsonify({'home_id': '456', 'user_id': '556', 'first_name': 'Conor'},
                   {'home_id': '456', 'user_id': '778', 'first_name': 'Nate'},
                   {'home_id': '456', 'user_id': '112', 'first_name': 'Chris'}
                   )


@app.route('/homes/<id>/rooms', methods=['GET'])
def get_home_rooms(id):
    home_id = id
    return jsonify({'home_id': '456', 'room_id': '556', 'room_name': 'Kitchen'},
                   {'home_id': '456', 'room_id': '778', 'room_name': 'Living Room'}
                   )


app.run()
