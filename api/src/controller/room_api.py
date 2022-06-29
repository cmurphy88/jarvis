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
def update_room():
    return jsonify({'result': 'room details updates successfully'})


@app.route('/rooms/<id>', methods=['DELETE'])
def delete_room():
    return jsonify({'result': 'room has been deleted successfully'})


app.run()
