
URLS = {
    "tokyo_xs": "https://drive.google.com/file/d/1Wzj-uPw1-InOaos5AB6VyLRWwYgjijU2/view?usp=share_link",
    "sf_xs": "https://drive.google.com/file/d/1JIh4C021DekwmBcJM2ltlpzTkzgZKjrc/view?usp=share_link",
    "gsv_xs": "https://drive.google.com/file/d/1-2181mWsGjlwr1DSIBboWB6Hf4DFLb6A/view?usp=share_link"
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

