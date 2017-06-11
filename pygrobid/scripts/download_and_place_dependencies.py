import os
from os import path

here = path.abspath(path.dirname(__file__))

def get_dependencies():
    import subprocess
    subprocess.call(os.path.join(here, "download_deps.sh"), shell=True)
