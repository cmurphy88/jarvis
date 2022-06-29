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


@app.route('/rooms/546', methods=['GET'])
def get_room():
    return jsonify({'id': 546, 'room_name': 'Living Room', 'home_id': '45'})


app.run()
