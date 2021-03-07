from debug import *
from zoodb import *
import rpclib

auth_sock = '/banksvc/sock'

def transfer(sender, recipient, zoobars):
    with rpclib.client_connect(auth_sock) as c:
        return c.call('transfer', sender=sender, recipient=recipient, zoobars=zoobars)

def balance(username):
    with rpclib.client_connect(auth_sock) as c:
        return c.call('balance', username=username)
