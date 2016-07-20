#!/bin/bash
export PYTHONPATH=$(dirname "$0")/mpd
python3 ~/git/mpd-script/dislike.py >> ~/.mpd/dislike
