#!/bin/bash
export PYTHONPATH=~/git/python-mpd2
python3 $(dirname "$0")/add.py "$@"
