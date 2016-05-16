#!/bin/bash
#mpd
#mpc volume 40
#mpc repeat on
#mpc random on
#mpc single off
#mpc consume off
#ncmpcpp
export PYTHONPATH=~/git/ncmpy/:~/git/python-mpd2
/usr/bin/env python3 $1
