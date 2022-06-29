from flask import Flask, jsonify

app = Flask(__name__);


@app.route('/medias', methods=['GET'])
def get_medias():
    return jsonify({'media_id': '56'},
                   {'media_id': '778'},
                   {'media_id': '129'}
                   )


@app.route('/medias/rooms/<id>', methods=['GET'])
def get_medias_room(id):
    room_id = id
    return jsonify({'media_id': '33', 'ip_address': '123:345:567', 'room_id': room_id})


@app.route('/medias/<id>', methods=['PUT'])
def update_media(id):
    media_id = id
    return jsonify({'media_id': media_id, 'result': 'media updated successfully'})


app.run()
