import Pyro4

"""
Application used to provide remote methods calls to the local storage data.
"""

@Pyro4.expose
class ListDataApp(object):

    def __init__(self):
        self.__storage = Pyro4.Proxy("PYRONAME:mikapod.storage")

    def runOnMainLoop(self):
        tsd = self.__storage.getAllTimeSeriesData()
        for timeSeriesDatum in tsd:
            print(timeSeriesDatum)


if __name__ == "__main__":
    """
    Main entry into the main program.
    """
    app = ListDataApp()
    app.runOnMainLoop()
