from zoodb import *
from debug import *

import hashlib
import os
import pbkdf2
import random

def newtoken(db, cred):
    hashinput = "%s%.10f" % (cred.password, random.random())
    cred.token = hashlib.md5(hashinput).hexdigest()
    db.commit()
    return cred.token

def login(username, password):
    db = cred_setup()
    cred = db.query(Cred).get(username)
    if not cred:
        return None
    if cred.password == pbkdf2.PBKDF2(password, cred.salt.decode('base-64')).hexread(32):
        return newtoken(db, cred)
    else:
        return None

def register(username, password):
    db = cred_setup()
    person = db.query(Cred).get(username)
    if person:
        return None
    newcred = Cred()
    newcred.username = username
    salt = os.urandom(10)
    newcred.password = pbkdf2.PBKDF2(password, salt).hexread(32)
    newcred.salt = salt.encode('base-64')
    db.add(newcred)
    db.commit()
    return newtoken(db, newcred)

def check_token(username, token):
    db = cred_setup()
    cred = db.query(Cred).get(username)
    if cred and cred.token == token:
        return True
    else:
        return False

