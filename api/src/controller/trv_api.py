from flask import Flask, jsonify

app = Flask(__name__);


@app.route('/trvs', methods=['GET'])
def get_trvs():
    return jsonify({'trv_id': '56'},
                   {'trv_id': '778'},
                   {'trv_id': '129'}
                   )


@app.route('/trvs/rooms/<id>', methods=['GET'])
def get_trvs_room(id):
    room_id = id
    return jsonify({'trv_id': '33', 'ip_address': '123:345:567', 'room_id': room_id})


@app.route('/trvs/<id>', methods=['PUT'])
def update_trv(id):
    trv_id = id
    return jsonify({'trv_id': trv_id, 'result': 'trv updated successfully'})


app.run()
