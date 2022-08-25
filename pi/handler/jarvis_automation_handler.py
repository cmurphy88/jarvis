import time
from urllib.request import urlopen
import requests
import json

while True:

    def get_user_id():
        user_id = requests.get('http://localhost:8001/find-faces')
        resp = user_id.json()
        return resp
        
    
    def get_routine_info(user_id):
        routine = requests.get('https://jarvis-1.5a25j6q6mjvnu.eu-west-1.cs.amazonlightsail.com/routines/users/' + str(user_id))
        resp = routine.json()
        return resp


    user_id = get_user_id()
    id = int(user_id)
    print(user_id)

    if id > 0:
        routine = get_routine_info(id)
        print(routine)
    
    
    time.sleep(5)
