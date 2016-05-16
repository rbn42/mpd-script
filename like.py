import util
client=util.startClient()
song=client.currentsong()
print(song)
util.closeClient(client)
