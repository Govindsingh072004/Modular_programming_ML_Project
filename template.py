import os,sys
from pathlib import Path
import logging

list_of_files=[
    "src/__init__.py",
    "src/components/__init__.py",
    "src/config/__init__.py",
    "src/constants/__init__.py",
    "src/entity/__init__.py",
    "src/exception/__init__.py",
    "src/logger/__init__.py",
    "src/pipeline/__init__.py",
    "src/utils/__init__.py",
    "config/config.yaml",
    "schema.py",
    "main.py",
    "app.py",
    "logs.py",
    "exception.py",
    "setup.py"


]

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)

    if filedir!="":
        os.makedirs(filedir,exist_ok=True)

    if(not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass

    else:
        logging.info(f"the file is already present at: {filepath}")