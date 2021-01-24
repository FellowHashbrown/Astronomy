from flask import Flask, render_template, redirect
from random import randint
from threading import Thread

# # # # # # # # # # # # # # # # # # # # 

app = Flask("Fellow Hashbrown APIs")

# # # # # # # # # # # # # # # # # # # # 

@app.route("/")
def home():
    pass

@app.route("/favicon")
@app.route("/favicon.ico")
def favicon():
    return redirect("/static/favicon.ico"), 302

# # # # # # # # # # # # # # # # # # # # 

def run():
    app.run(
        host = '0.0.0.0', 
        port = randint(1000, 9999))

t = Thread(target = run)
t.start()
