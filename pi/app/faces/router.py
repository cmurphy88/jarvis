import os.path, os
from os import path
import glob

from fastapi import File, UploadFile, HTTPException, status, APIRouter
from typing import List

from deepface import DeepFace
from PIL import Image

router = APIRouter(
    tags=['upload']
)

base_dir = "/home/pi/faces/db"
representations_file = '/home/pi/faces/db/representations_vgg_face.pkl'
backends = ["opencv", "ssd", "dlib", "mtcnn"]


@router.post("/upload")
def upload(user_id: int, files: List[UploadFile] = File(...)):
    for file in files:
        image_path = get_image_path(str(user_id), file.filename)
        store_image(image_path, file)
        
    os.remove(representations_file)

    return {"message": f"Successfully uploaded {[file.filename for file in files]}"}


@router.post("/find")
def find(file: UploadFile = File(...)):
    stored_users = '/home/pi/faces/'
    temp_path = stored_users + 'temp/' + file.filename
    store_image(temp_path, file)
    os.remove(representations_file)

    df = DeepFace.find(img_path=temp_path, db_path=stored_users + 'db/')
    if len(df.values) == 0:
        os.remove(temp_path)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='user not found')

    match = df.values[0][0]
    match_arr = match.split('/')
    user_id = match_arr[len(match_arr) - 2]

    os.remove(temp_path)

    return user_id


@router.post("/detect")
def detect():
    detections = '/home/pi/faces/motion/image2.jpg'
    db_path = '/home/pi/faces/db/'

    df = DeepFace.find(img_path=detections, db_path=db_path)
    if len(df.values) == 0:
        os.remove(detections)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='user not found')

    match = df.values[0][0]
    match_arr = match.split('/')
    user_id = match_arr[len(match_arr) - 2]

    # os.remove(detections)

    return user_id


def clear_motion():
    files = glob.glob('/home/pi/faces/motion/*')
    for f in files:
        os.remove(f)


@router.post("/sort-faces")
def match_face():
    os.remove(representations_file)
    files = glob.glob('/home/pi/faces/motion/*')
    user_id = "-1"
    for f in files:
        df = DeepFace.find(img_path=f, db_path='/home/pi/faces/db/', enforce_detection=False)
        if len(df.values) > 0:
            match = df.values[0][0]
            match_arr = match.split('/')
            user_id = match_arr[len(match_arr) - 2]
            break
        else:
            user_id = "-1"
    clear_motion()

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


def store_image_to_captured(img_path: str, file: UploadFile = File(...)):

    try:
        contents = file.file.read()

        with open(img_path, 'wb') as f:
            f.write(contents)
    except Exception:
        return {"message": "There was an error uploading the file(s)"}
    finally:
        file.close()


def get_image_path(user_id: str, file_name: str):
    b_path = base_dir + "/" + user_id
    is_dir = path.exists(b_path)
    if not is_dir:
        os.mkdir(b_path)

    return b_path + "/" + file_name
