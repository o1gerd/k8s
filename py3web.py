#!/usr/bin/python3

import os
from bottle import run, get, post, request, error
import datetime

"""
If you want to run this script in standalone mode
you can replace this ip to ip-address of external interface.
Then you don`t need proxy-pass. So you can use "0.0.0.0" to any
interface listen.
"""
ip = '0.0.0.0'

@error(404)
def error404(error):
        return 'URL not defined!'

@get('/')
def action_req():
        return '''
                <form action="/" method="post">
                        Make a request: <input name="new_req" type="text" />
                        <input value="Submit" type="submit" />
                </form>
                <p>You can use the following values:</p>
                <p> <b>uname</b> - OS information</p>
                <p> <b>date</b> - current date and time</p>
                <p> <b>ping</b> - return "pong"</p>
        '''

@post('/')
def do_req():
        new_req = str(request.forms.get('new_req'))
        if new_req == 'uname':
                return(str(os.uname()))
        elif new_req == 'date':
                return(str(datetime.datetime.today()))
        elif new_req == 'ping':
                return 'pong'
        else:
                return 'Wrong value!'

run(host=ip, port=32400)
