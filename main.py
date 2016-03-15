#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request
import config
from r3bot import r3bot

app = Flask(__name__)
bot = r3bot(config.APITOKEN)
bot.initHook(config.HOOKURL)


@app.route('/hook/', methods=['POST'])
def hook():
    bot.processHookRequest(request)
    return "OK"


@app.route("/")
def index():
    return "Yay! realraum Telegram Hook working!"

if __name__ == "__main__":
    app.run()
