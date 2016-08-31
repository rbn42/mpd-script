#!/bin/bash
LOCKFILE="/dev/shm/mpd-script-lock"

ROOT="$0"
ROOT=$(realpath "$ROOT")
ROOT=$(dirname "$ROOT")

export PYTHONPATH="$ROOT/mpd"

LOCK=$(python "$ROOT/lock.py" "$LOCKFILE" 60)
if [ "locked" == "$LOCK" ]
then
#    echo locked
    touch $LOCKFILE
    python3 $(dirname "$0")/add.py "$@"
    #python3 $(dirname "$0")/add.py "$@" --clear
    rm $LOCKFILE
#else
#    echo failed
fi
