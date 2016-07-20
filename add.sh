#!/bin/bash
export PYTHONPATH=$(dirname "$0")/mpd
python3 $(dirname "$0")/add.py "$@"
