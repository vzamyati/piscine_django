#!/bin/bash

# to run the script correctly you have to do this commands first in the root of your project
# python3 -m venv venv
# source "./venv/bin/activate"


pip3 --version
pip3 install -t local_lib --upgrade git+https://github.com/jaraco/path.py.git > logs.log
python3 my_program.py