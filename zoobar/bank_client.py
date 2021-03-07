from debug import *
from zoodb import *
import rpclib

bank_sock = '/banksvc/sock'

def transfer(sender, recipient, zoobars):
    with rpclib.client_connect(bank_sock) as c:
        return c.call('transfer', sender=sender, recipient=recipient, zoobars=zoobars)

def balance(username):
    with rpclib.client_connect(bank_sock) as c:
        return c.call('balance', username=username)

def get_log(username):
    with rpclib.client_connect(bank_sock) as c:
        return c.call('get_log', username=username)
