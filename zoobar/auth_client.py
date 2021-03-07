from debug import *
from zoodb import *
import rpclib

auth_sock = '/authsvc/sock'

def login(username, password):
    with rpclib.client_connect(auth_sock) as c:
        return c.call('login', username=username, password=password)

def register(username, password):
    with rpclib.client_connect(auth_sock) as c:
        c.call('register', username=username, password=password)

def check_token(username, token):
    with rpclib.client_connect(auth_sock) as c:
        c.call('token', username=username, token=token)
