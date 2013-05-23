
from twisted.internet.protocol import ClientFactory

from cp import *

class ExtendedClientFactory(ClientFactory):
    
    def __init__(self, parent, destIP, sourceFile, destFile, nos, streams, serverType):
    	self.parent     = parent
        self.destIP     = destIP
        self.sourceFile = sourceFile
        self.destFile   = destFile
        self.nos        = nos
        self.streams    = streams
        self.serverType = serverType

    def buildProtocol(self, addr):
        return ClientProtocol(self.parent, self.destIP, self.sourceFile, self.destFile, self.nos, self.streams, self.serverType)
