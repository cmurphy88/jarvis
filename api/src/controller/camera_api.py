from flask import Flask, jsonify

app = Flask(__name__);


@app.route('/cameras', methods=['POST'])
def create_camera():
    return jsonify({'result': 'camera created successfully'})


@app.route('/cameras/<id>', methods=['GET'])
def get_camera(id):
    camera_id = id
    return jsonify({'camera_id': '33', 'ip_address': '123:345:567'})


@app.route('/cameras/<id>', methods=['PUT'])
def update_camera(id):
    camera_id = id
    return jsonify({'camera_id': '33', 'result': 'camera updated successfully'})


app.run()
