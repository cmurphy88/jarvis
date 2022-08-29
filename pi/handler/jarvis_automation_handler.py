import time
from urllib.request import urlopen
import requests
import json
from datetime import datetime

while True:

    def get_user_id():
        user_id = requests.get('http://localhost:8001/find-faces')
        resp = user_id.json()
        return resp
        
    
    def get_routine_info(user_id):
        routine = requests.get('https://jarvis-1.5a25j6q6mjvnu.eu-west-1.cs.amazonlightsail.com/routines/users/' + str(user_id) + '/now' )
        resp = routine.json()
        print(datetime.now())
        return resp


    user_id_string = get_user_id()
    user_id_int = int(user_id_string)

    if user_id_int > 0:
        print(user_id_int)
        routine = get_routine_info(user_id_int)
        print(routine)
        print("Getting the light settings for that time...")
    else:
        print("No users found...")
    
    time.sleep(10)
 