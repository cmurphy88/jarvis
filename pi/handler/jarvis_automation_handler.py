import time
from urllib.request import urlopen
import requests
import json
from datetime import datetime
# import bridge
from huesdk import Hue

# creating the hue bridge object
hue = Hue(bridge_ip='192.168.0.36', username='Dk36xjaPYdGzPr1PMinYXeQGhAq5rN7MWB9mZx8i')

# creating the light object
light = hue.get_light(name='Hue white lamp')

room_id = 1

def change_light_brightness(light, brightness):
    hue_bright = (254 * (brightness/100))
    light.set_brightness(hue_bright)


def get_user_id():
    user_id = requests.get('http://localhost:8001/find-faces')
    resp = user_id.json()
    return resp
    

def get_routine_info(user_id):
    routine = requests.get('https://jarvis-1.5a25j6q6mjvnu.eu-west-1.cs.amazonlightsail.com/routines/rooms/' + str(room_id) + '/users/' + str(user_id))

    if not routine.json() == 'None':
        resp = routine.json()
        print("Routine found..." + resp[0]['name'])
    else:
        print("No routine action required...")
        return None
    return resp


def handle_light_settings(x):
    if x['is_active'] == True:
        light.on()
        print(x['brightness'])
        change_light_brightness(light, x['brightness'])


def handle_devices(routine):
    for x in routine[0]['devices']:
        if x['type'] == 'light':
            print("Setting light device..." + x['name'])
            handle_light_settings(x)

        elif x['type'] == 'media':
            print("Setting media device..." + x['name'])

        elif x['type'] == 'trv':
            print("Setting trv device..." + x['name'])


while True:
    print("Image detection beginning...")

    user_id_string = get_user_id()
    user_id_int = int(user_id_string)

    if user_id_int > 0:
        print("User found: " + str(user_id_int))
        routine = get_routine_info(user_id_int)

        if routine != None:
            print("Setting devices...")
            handle_devices(routine)
    
    time.sleep(5)
 