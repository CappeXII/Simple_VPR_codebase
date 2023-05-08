
URLS = {
    "tokyo_xs": "https://drive.google.com/file/d/1LSD-jbka6ZeV1WVzoSf9oW01GXU4AVjH/view?usp=share_link",
    "sf_xs": "https://drive.google.com/file/d/1RxpuhHqYtOOTlGiJuPQ0RhvGLK6trjqe/view?usp=share_link",
    "gsv_xs": "https://drive.google.com/file/d/1n3t3fJAay0mzHhhr_CurLiyw5aXCrhTU/view?usp=share_link"
}

import os
import gdown
import shutil

os.makedirs("data", exist_ok=True)
for dataset_name, url in URLS.items():
    print(f"Downloading {dataset_name}")
    zip_filepath = f"data/{dataset_name}.zip"
    gdown.download(url, zip_filepath, fuzzy=True)
    shutil.unpack_archive(zip_filepath, extract_dir="data")
    os.remove(zip_filepath)

