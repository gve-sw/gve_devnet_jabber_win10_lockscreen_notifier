"""
Copyright (c) 2020 Cisco and/or its affiliates.

This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at

               https://developer.cisco.com/docs/licenses

All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.
"""


# If you wish to compile this python Flask application into a Windows executable
# you can use the pyinstaller library (pip install pyinstaller)
# with the following command: 
# pyinstaller --onefile --add-data 'templates;templates' app.py
#NOTE: you if you create an executable this way you must also package it in a way
#that you can specify that it´s notification settings can be changed to allow notifications
# on a lock screen

from toastify import notify
import time
from flask import Flask, request, jsonify, render_template
import sys, os

if getattr(sys, 'frozen', False):
    template_folder = os.path.join(sys._MEIPASS, 'templates')
    app = Flask(__name__, template_folder=template_folder)
else:
    app = Flask(__name__)



@app.route("/notify_call")
def notify_call():
    call_id=request.args.get('call_id','')
    #time.sleep(5)
    notify (
        BodyText='From: '+call_id,
        AppName='Jabber',
        TitleText='Jabber New Call',
        ImagePath='icon.ico'
    )

    return jsonify(result="notified")

@app.route("/")
def start():
    return render_template("call_notifier.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5500,debug = True)