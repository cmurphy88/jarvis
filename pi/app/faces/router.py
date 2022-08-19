import os.path
from os import path

from fastapi import File, UploadFile, HTTPException, status, APIRouter
from typing import List

from deepface import DeepFace
from PIL import Image

router = APIRouter(
    tags=['upload']
)

base_dir = "images/db"
representations_file = '/Users/conor.murphy/PycharmProjects/jarvis/pi/images/db/representations_vgg_face.pkl'


@router.post("/upload")
def upload(user_id: int, files: List[UploadFile] = File(...)):
    for file in files:
        image_path = get_image_path(str(user_id), file.filename)
        store_image(image_path, file)
        os.remove(representations_file)

    return {"message": f"Successfully uploaded {[file.filename for file in files]}"}


@router.post("/find")
def find(file: UploadFile = File(...)):
    stored_users = '/Users/conor.murphy/PycharmProjects/jarvis/pi/images/'
    temp_path = stored_users + 'temp/' + file.filename
    store_image(temp_path, file)

    df = DeepFace.find(img_path=temp_path, db_path=stored_users + 'db/')
    if len(df.values) == 0:
        os.remove(temp_path)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='user not found')

    match = df.values[0][0]
    match_arr = match.split('/')
    user_id = match_arr[len(match_arr) - 2]

    os.remove(temp_path)

    return user_id


def store_image(img_path: str, file: UploadFile = File(...)):

    try:
        contents = file.file.read()

        with open(img_path, 'wb') as f:
            f.write(contents)
    except Exception:
        return {"message": "There was an error uploading the file(s)"}
    finally:
        file.file.close()


def get_image_path(user_id: str, file_name: str):
    b_path = base_dir + "/" + user_id
    is_dir = path.exists(b_path)
    if not is_dir:
        os.mkdir(b_path)

    return b_path + "/" + file_name
