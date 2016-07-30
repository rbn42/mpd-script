#!/bin/bash
export PYTHONPATH=$(dirname "$0")/mpd

export LOCKFILE="/dev/shm/mpd-script-lock"
if [ -f "$LOCKFILE" ]
then
    echo locked
else
    touch $LOCKFILE
    python3 $(dirname "$0")/add.py "$@"
    rm $LOCKFILE
fi

