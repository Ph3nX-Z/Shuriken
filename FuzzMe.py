import os
import re

from flask import Flask, session, request, render_template

app = Flask(__name__)

app.secret_key = os.urandom(24)

@app.route('/', methods=['GET','POST'])
def index():
    return "Not an index"
@app.route('/1', methods=['GET','POST'])
def var_une():
	return ""
@app.route('/register', methods=['GET','POST'])
def register_web():
    return "No register page yet :("
@app.route('/robots.txt', methods=['GET','POST'])
def robots():
    return "I'll be back"
@app.route('/secret', methods=['GET','POST'])
def secret():
    return "it's a secret message"
@app.route('/.passwd', methods=['GET','POST'])
def passwd():
    return "password123"
@app.route('/resetpassword', methods=['GET','POST'])
def rpassd():
    return "No passwords on this site"
@app.route('/thankyou', methods=['GET','POST'])
def thankyou():
    return ":)"
@app.route('/energy', methods=['GET','POST'])
def energy():
    return "ZZZZzzzz"
@app.route('/googlebot', methods=['GET','POST'])
def googlebot():
    return "Yeah i'm a googlebot, so what ?"
app.run(
        threaded=True,
        port=80,
        host="0.0.0.0",
        debug=True

  )
