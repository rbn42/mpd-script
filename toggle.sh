#!/bin/bash
export MSG=`mpc toggle`
export SCRIPT="""
import sys
msg=sys.argv[1]
msgs=msg.split('\n')
state,title=msgs[1].split()[0],msgs[0]
print(state)
"""
export MSG2=`python -c "$SCRIPT" "$MSG"`
echo $MSG2

#notify-send "$MSG2"


#暂且没有好的指示ui,就用vol来顶替了
#notify本身不够好,因为toggle多按几次,旧消息不会消失,就会搞不清播放状态了
if [ "[playing]" == $MSG2 ];
then
    volnoti-show 100 
else
    volnoti-show 0 -m
fi


