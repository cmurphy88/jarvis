import time
from urllib.request import urlopen
import requests
import json
from datetime import datetime
# import bridge
from huesdk import Hue

# creating the hue bridge object
hue = Hue(bridge_ip='192.168.0.168', username='On7BHR03llq17sPfD6k-0zc5eHMETVQv2mCHH6xv')

# creating the light object
light = hue.get_light(name='Hue white lamp')


def get_user_id():
    user_id = requests.get('http://localhost:8001/find-faces')
    resp = user_id.json()
    return resp
    

def get_routine_info(user_id):
    routine = requests.get('https://jarvis-1.5a25j6q6mjvnu.eu-west-1.cs.amazonlightsail.com/routines/users/' + str(user_id) + '/now' )

    if not routine.json() == 'None':
        resp = routine.json()
        print("Routine found...")
    else:
        print("No routine action required...")
        return None
    return resp


def hue_brightness(brightness):
    hue_bright = (254 * (brightness/100))
    return int(hue_bright)


def handle_devices(routine):
    for x in routine['devices']:
        if x['type'] == 'light':
            print("Setting light device..." + x['name'])
            light = hue.get_light(x['name'])
            hue.change_light_brightness(light, hue_brightness(x['brightness']))
        elif x['type'] == 'media':
            print("Setting media device..." + x['name'])
        elif x['type'] == 'trv':
            print("Setting trv device..." + x['name'])


while True:
    print("Image detection beginning...")

    user_id_string = get_user_id()
    user_id_int = int(user_id_string)

    if user_id_int > 0:
        print("User found: " + user_id_int)
        routine = get_routine_info(user_id_int)

        if routine != None:
            print("Setting devices...")
            handle_devices(routine)
    
    time.sleep(10)
 