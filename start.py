from mpd import MPDClient
client = MPDClient()               # create client object
# network timeout in seconds (floats allowed), default: None
client.timeout = 10
# timeout for fetching the result of the idle command is handled
# seperately, default: None
client.idletimeout = None
client.connect("localhost", 6600)  # connect to localhost:6600
print(client.mpd_version)          # print the MPD version
# print result of the command "find any house"
print(client.find("any", "house"))
# command list的机制现在还不理解,在把python-mpd2的动态方法改成静态方法的过程中,command list暂且还不能好好处理
# client.command_list_ok_begin()       # start a command list
client.update()                      # insert the update command into the list
client.status()                      # insert the status command into the list
print(client.status())
print(client.stats())
# results = client.command_list_end()  # results will be a list with the results
# print((results))
client.iterate = True
for song in client.playlistinfo():
    #print( song["file"])
    pass
client.iterate = False
client.send_idle()
events = client.fetch_idle()
print(events)
print(client.status())
client.close()                     # send the close command
client.disconnect()                # disconnect from the server
# client.delete((1,))     # delete all songs, but the first.
