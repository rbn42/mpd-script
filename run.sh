#!/bin/bash
#mpd
#mpc volume 40
#mpc repeat on
#mpc random on
#mpc single off
#mpc consume off
#ncmpcpp
#export PYTHONPATH=~/git/ncmpy/:~/git/python-mpd2
export PYTHONPATH=$(dirname "$0")/mpd
/usr/bin/env python3 $1
