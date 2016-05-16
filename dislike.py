import util
client=util.startClient()
#output identity to record this song
song=client.currentsong()
#identity={'file':song.get('file'),'track':song.get('track')}
#print(identity)
print(song)
#delete song
client.deleteid(song['id'])
util.closeClient(client)
