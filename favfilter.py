#!/usr/bin/python
import os.path

KEYS = 'time', 'title', 'artist', 'album', 'track'  # 'pos'
_data = []


def parse2str(item):
    # 2016-12-05 09:44:13 Mon NZDT
    # path取末尾两级,这样移动文件,改变目录结构的时候可以提供容错
    # 因为有time标记做保险,即使有重名文件存在,撞车的概率应该也不会很大
    path = item['file']
    path = '/'.join(path.split('/')[-2:])

    keys = sorted([k for k in item if k in KEYS])
    values = [path] + [item[k] for k in keys]
    return str(values)
    _str = ','.join(values)
    return _str


def getData():
    path = os.path.expanduser('~/.mpd/dislike')
    f = open(path)
    l = [eval(s) for s in f]

    result = []
    for item in l:
        _str = parse2str(item)
        result.append(_str)
    return set(result)


def dislike(item):
    # if len(_data) < 1:
    #    _data.append(getData())
    _str = parse2str(item)
    return _str in getData()
    return _str in _data[0]


if __name__ == '__main__':
    print(getData())
