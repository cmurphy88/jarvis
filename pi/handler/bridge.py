import time
from turtle import delay
from huesdk import Hue

# creating the hue bridge object
hue = Hue(bridge_ip='192.168.0.10', username='LckczTpYzebKvDeueCoUVUs1SpDaA6FDy4f6be2r')

# creating the light object
light = hue.get_light(name='Hue white lamp')

# methods for controlling the lights
def connect_hue():
    username = Hue.connect(bridge_ip='192.168.0.10')
    print(username)


def change_light_brightness(light, brightness):
    if brightness > 254:
        brightness = 254
    elif brightness < 0:
        brightness = 0
        
    light.set_brightness(brightness)


def turn_light_on(light):
    light.on()


def turn_light_off(light):
    light.off(transition=100)


def get_all_lights():
    lights = hue.get_lights()

    # for x in lights:
    #     print(x.name)
    #     print(x.bri)


def make_light_blink(light):
    counter = 0
    while counter <= 10:
        light.off()
        time.sleep(1)
        light.on()
        light.set_brightness(254)
        time.sleep(1)
        counter = counter + 1
        print(counter)


# turn_light_on(light)
# change_light_brightness(light, 254)
connect_hue()
