from flask import g, render_template, request

from login import requirelogin
from zoodb import *
from debug import *
import bank
import traceback

@catch_err
@requirelogin
def transfer():
    warning = None
    try:
        if 'recipient' in request.form:
            if request.form['recipient'] == g.user.person.username:
                raise ValueError('sender and recipient are the same: ' + g.user.person.username)
            zoobars = symint(request.form['zoobars'])
            if zoobars < 0:
                raise ValueError('attempted to send negative zoobars: ' + str(zoobars))
            bank.transfer(g.user.person.username,
                          request.form['recipient'], zoobars)
            warning = "Sent %d zoobars" % zoobars
    except (KeyError, ValueError, AttributeError) as e:
        traceback.print_exc()
        warning = "Transfer to %s failed" % request.form['recipient']

    return render_template('transfer.html', warning=warning)
