from flask import Flask, jsonify

app = Flask(__name__);


@app.route('/lights', methods=['GET'])
def get_lights():
    return jsonify({'light_id': '56'},
                   {'light_id': '778'},
                   {'light_id': '129'}
                   )


@app.route('/lights/rooms/<id>', methods=['GET'])
def get_light_room(id):
    room_id = id
    return jsonify({'light_id': '33', 'ip_address': '123:345:567', 'room_id': room_id})


@app.route('/lights/<id>', methods=['PUT'])
def update_light(id):
    light_id = id
    return jsonify({'light_id': light_id, 'result': 'light updated successfully'})


app.run()
