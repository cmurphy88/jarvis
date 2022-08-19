from deepface import DeepFace


async def find_face(file):
    person = file.read()

    img_path = '/Users/conor.murphy/PycharmProjects/jarvis/pi/images'

    df = DeepFace.find(img_path=person, db_path=img_path)

    df.head()

    match = df.values[0][0]

    match_arr = match.split('/')

    user_id = match_arr[len(match_arr) - 2]

    return user_id
