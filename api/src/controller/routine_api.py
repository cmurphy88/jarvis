from flask import Flask, jsonify

app = Flask(__name__);


@app.route('/routines', methods=['POST'])
def create_routine():
    return jsonify({'result': 'routine created successfully'})


@app.route('/routines', methods=['GET'])
def get_routines():
    return jsonify({'routine_id': '68'},
                   {'routine_id': '7778'},
                   {'routine_id': '90'})


@app.route('/routines/<id>', methods=['GET'])
def get_routine(id):
    routine_id = id
    return jsonify({'routine_id': routine_id})


@app.route('/routines/users/<id>', methods=['GET'])
def get_routine_user(id):
    user_id = id
    return jsonify({'routine_id': '68'},
                   {'routine_id': '7778'},
                   {'routine_id': '90'})


@app.route('/routines/<id>', methods=['PUT'])
def update_routine(id):
    routine_id = id
    return jsonify({'routine_id': routine_id, 'result': 'routine has been updated'})


app.run()
