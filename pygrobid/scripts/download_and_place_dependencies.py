from clint.textui import progress
import requests, zipfile, io # for java grobid dependency downloading
from os import path

here = path.abspath(path.dirname(__file__))

def get_dependencies():
    GROBID_PARENT_ZIP_URL = ("https://github.com/kermitt2/grobid/releases/"
                             "download/grobid-parent-0.4.1/grobid-grobid-parent-0.4.1.zip")
    TARGET_DIR = path.join(here, '..')

    print("Downloading 'grobid-parent-0.4.1'...")
    r = requests.get(GROBID_PARENT_ZIP_URL, stream=True)
    temp_path = 'temp.zip'
    with open(temp_path, 'wb') as f:
        total_length = int(r.headers.get('content-length'))
        for chunk in progress.bar(r.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1):
            if chunk:
                f.write(chunk)
                f.flush()

    z = zipfile.ZipFile(temp_path)
    print("Extracting 'grobid-parent-0.4.1.zip' into {}".format(here))
    z.extractall(TARGET_DIR)
    print("Finished extracting.")
