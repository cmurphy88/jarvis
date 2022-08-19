import os.path
from os import path

from fastapi import File, UploadFile, APIRouter
from typing import List

router = APIRouter(
    tags=['upload']
)

base_dir = "images"


@router.post("/upload")
def upload(user_id: int, files: List[UploadFile] = File(...)):
    for file in files:
        try:
            contents = file.file.read()

            image_path = get_image_path(str(user_id), file.filename)
            with open(image_path, 'wb') as f:
                f.write(contents)
        except Exception:
            return {"message": "There was an error uploading the file(s)"}
        finally:
            file.file.close()

    return {"message": f"Successfully uploaded {[file.filename for file in files]}"}


def get_image_path(user_id: str, file_name: str):
    b_path = base_dir + "/" + user_id
    is_dir = path.exists(b_path)
    if not is_dir:
        os.mkdir(b_path)

    return b_path + "/" + file_name
