from flask import Flask, jsonify

app = Flask(__name__);


@app.route('/rooms', methods=['POST'])
def room_create():
  return jsonify({'result': 'room created successfully'})


@app.route('/rooms', methods=['GET'])
def get_rooms():
    return jsonify([
        {'id': 546, 'room_name': 'Living Room', 'home_id': '45'},
        {'id': 894, 'room_name': 'Kitchen', 'home_id': '45'},
        {'id': 326, 'room_name': 'Bedroom', 'home_id': '97'}
    ])


@app.route('/rooms/<id>', methods=['GET'])
def get_room(id):
    room_id = id
    return jsonify({'id': room_id, 'room_name': 'Living Room', 'home_id': '45'})


@app.route('/rooms/<id>', methods=['PUT'])
def update_room(id):
    room_id = id
    return jsonify({'result': 'room details updates successfully'})


@app.route('/rooms/<id>', methods=['POST'])
def add_user_room(id):
    room_id = id
    return jsonify([
        {'room_id': room_id},
        {'result': 'user added to the room'}
    ])


@app.route('/rooms/<id>/routines', methods=['GET'])
def get_room_routine(id):
    room_id = id
    return jsonify({'routine_id': '23'},
                   {'user_id': '564'},
                   {'temperature': '50'},
                   {'media': 'https://youtube.com'},
                   {'light': '80'},
                   {'start_time': '10:00'},
                   {'end_time': '10:59'})


app.run()
