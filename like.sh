#!/bin/bash
export PYTHONPATH=$(dirname "$0")/mpd
python3 ~/git/mpd-script/like.py >> ~/.mpd/like
