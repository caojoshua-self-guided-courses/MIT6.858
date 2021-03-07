#!/usr/bin/python

import rpclib
import sys
import auth
from debug import *

class BankRpcServer(rpclib.RpcServer):
    def rpc_transfer(self, sender, recipient, zoobars):
        log('rpc transfer')

    def rpc_balance(self, username):
        log('rpc balance')

(_, dummy_zookld_fd, sockpath) = sys.argv

s = BankRpcServer()
s.run_sockpath_fork(sockpath)
