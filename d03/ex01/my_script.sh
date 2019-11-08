#!/bin/bash

pip3 --version
pip3 install -t local_lib --upgrade git+https://github.com/jaraco/path.py.git > logs.log
python3 my_program.py