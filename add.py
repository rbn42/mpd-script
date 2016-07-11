#!/usr/bin/python
# -*- coding: UTF-8 -*-
import util
import database
import sys


def main(client):
    path = sys.argv[1]
    l = client.find('filename', path)
    if len(l) > 0:
        item = l[0]
    else:
        item = {'directory': path}

    _list = database.add2(item, client)
    if len(_list) < 0:
        return

    """
    playlist不可以拆散后加入,必须要通过client.load才能加载到必要的信息.
    所以如果playlist中有dislike的项目,那么只能加入后再删除了.

    因此,只能第一次add全部加入,然后再读取playlist,删掉dislike的部分.
    """
    client.clear()
    for item in _list:
        if 'file' in item:
            client.add(item['file'])
        elif 'playlist' in item:
            try:
                client.load(item['playlist'])
            except mpd.CommandError as e:
                pass
            else:
                pass

    # 添加完毕后再消除.
    l = client.playlistinfo()
    from favfilter import dislike
    for item in l:
        if dislike(item):
            client.deleteid(item['id'])

    client.next()
    client.play()


client = util.startClient()
main(client)
util.closeClient(client)
