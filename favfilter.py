#!/usr/bin/python
import os.path

KEYS = 'file', 'time', 'title', 'artist', 'album', 'track'  # 'pos'
_data = []


def parse2str(item):
    keys = [k for k in item if k in KEYS]
    keys.sort()
    values = [item[k] for k in keys]
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
