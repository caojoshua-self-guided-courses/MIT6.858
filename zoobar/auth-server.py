#!/usr/bin/python

import rpclib
import sys
import auth
from debug import *

class AuthRpcServer(rpclib.RpcServer):
    def rpc_login(self, username, password):
        log("rpc login")
        pass

    def rpc_register(self, username, password):
        return auth.register(username, password)

    def rpc_check_token(self, username, token):
        log("rpc_check_token")
        pass

(_, dummy_zookld_fd, sockpath) = sys.argv

s = AuthRpcServer()
s.run_sockpath_fork(sockpath)
