# 主要入口
def add2(item, mpc):
    items = listall2(item, mpc)
    items = _filter(items, mpc)
    return items


def _filter(items, mpc):
    occupied = []
    playlists = []
    for item in items:
        if 'playlist' in item:
            try:
                # result+=mpc.listplaylistinfo(item['playlist'])
                occupied += mpc.listplaylist(item['playlist'])
                playlists.append(item)
            except:
                a = 1 / 0
    occupied = set(occupied)
    non_occupied = []
    for item in items:
        if 'file' in item:
            if item['file'] not in occupied:
                non_occupied.append(item)
    return non_occupied + playlists


def listall1(item, mpc):
    if 'directory' in item:
        return mpc.listallinfo(item['directory'])
    else:
        return [item]


def listall2(item, mpc, result=None):
    if None == result:
        result = []
    if 'directory' in item:
        try:
            uri = item['directory']
            if uri == '..':
                return []
            children = mpc.lsinfo(uri)
        except:
            # 可以强制加入utf8编码错误的文件，但是加入后，ncmpy的listview会出错，无法显示。
            children = mpc.listall(item['directory'])
            children = [item for item in children if 'file' in item]
        for child in children:
            listall2(child, mpc, result)
    else:
        result.append(item)
    return result
