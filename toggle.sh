#!/bin/bash
export MSG=`mpc toggle`
export SCRIPT="""
import sys
msg=sys.argv[1]
msgs=msg.split('\n')
msg=msgs[1].split()[0]+' '+msgs[0]
print(msg)
"""
export MSG2=`python -c "$SCRIPT" "$MSG"`
echo $MSG2
notify-send "$MSG2"
