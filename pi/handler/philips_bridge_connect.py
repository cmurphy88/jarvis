from huesdk import Hue
username = Hue.connect(bridge_ip='192.168.0.168')
print(username)
