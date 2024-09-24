import sys
import os
sys.path.insert(0, "/home/${username}/pdf_compressor")

path = open("/home/${username}/pdf_compressor/env_path.txt").read().strip()
activate_this = path+"/bin/activate_this.py"

with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

from app import app as application