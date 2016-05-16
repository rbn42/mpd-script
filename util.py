from mpd import MPDClient


def startClient():
    client = MPDClient()               # create client object
    # network timeout in seconds (floats allowed), default: None
    client.timeout = 10
    # timeout for fetching the result of the idle command is handled
    # seperately, default: None
    client.idletimeout = None
    client.connect("localhost", 6600)  # connect to localhost:6600
    return client


def closeClient(client):
    client.close()                     # send the close command
    client.disconnect()                # disconnect from the server
