import argparse

from twisted.protocols.ftp import FTPClient
from twisted.internet.endpoints import TCP4ClientEndpoint
from twisted.internet import reactor

from common import *
from ecf import *

class Callback(object):

    def __init__(self):
        self.portDst = None
        self.portSrc = None

    def _stop(self):
        if self.portSrc != None:
            self.portSrc.disconnect()
        if self.portDst != None:
            self.portDst.disconnect()
        reactor.stop()

def destinationConnected():
    log_message('Connected to destination server.')

def dstError():
    log_message('Connection to destination server failed.')

def sourceConnected():
    log_message('Connected to source server.')

def srcError():
    log_message('Connection to source server failed.')
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    for arg in CLIENT_ARGUMENTS:
        parser.add_argument(arg[0], arg[1], action=arg[2], default=arg[3], type=arg[4], required=arg[5], help=arg[6])
    args = parser.parse_args()
    startLogger(args.logfile)
    log_message('Client started.')

    cb = Callback()
    portDst = reactor.connectTCP(args.dest_address, args.dest_port,
        ExtendedClientFactory(cb, args.dest_address, args.source_filepath, args.dest_filepath, args.no_statistics, args.parallel_streams, 'DST'))
    cb.portDst = portDst
    
    portSrc = reactor.connectTCP(args.source_address, args.source_port,
        ExtendedClientFactory(cb, args.dest_address, args.source_filepath, args.dest_filepath, args.no_statistics, args.parallel_streams, 'SRC'))
    cb.portSrc = portSrc

    reactor.run()