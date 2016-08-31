#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
Hello.

Usage:
  main.py [--type=<type>] [--debug] [--clear] <path>

Options:
  -h --help     Show this screen.
"""
import util
import database
import sys
import logger
import logging


def main(client):
    from docopt import docopt
    arguments = docopt(__doc__)
    path = arguments['<path>']
    type_ = arguments['--type']
    if arguments['--debug']:
        logfile = '/tmp/mpdscript.log'  # LogFile.strip()
        logger.init(logfile)
    logging.info('add %s:%s' % (type_, path))

    if type_ in ('directory', 'playlist'):
        item = {type_: path}
    else:
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
    if arguments['--clear']:
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

    if arguments['--clear']:
        client.next()
    client.play()

    # 添加完毕后再消除.
    # 逐个删除操作消耗很大,相比之下添加几乎一瞬间就完成了.不过似乎不存在批量删除的api
    # 不过这点消耗在容忍范围内
    # 所以播放可以提前到前面.小概率事件播放中的曲目可能会被下面代码删除掉.完善的做法是后面加一个播放中检查.
    l = client.playlistinfo()
    from favfilter import dislike
    for item in l:
        if dislike(item):
            client.deleteid(item['id'])

    # 检查下是否播放停了.
    song = client.currentsong()
    if None == song:
        client.next()
    client.play()


client = util.startClient()
main(client)
util.closeClient(client)
