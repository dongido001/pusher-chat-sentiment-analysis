# app.py

from flask import Flask, request, jsonify, render_template, redirect
import os
import json
import pusher

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify("Pong!")


# run Flask app
if __name__ == "__main__":
    app.run()
