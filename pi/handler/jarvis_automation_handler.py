import time

import requests

while True:

    user_id = int(requests.get('http://localhost:8001/find-faces'))

    if user_id > 0:
        routine = requests.get('https://jarvis-1.5a25j6q6mjvnu.eu-west-1.cs.amazonlightsail.com/')

    print(routine)
    time.sleep(5)
