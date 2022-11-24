from datetime import datetime
from flask import Flask

app = Flask(__name__)
pageViews = 0


@app.route("/")
def welcome():
  return "Welcome to my Flash Cards application!"

@app.route("/date")
def date():
  return "This page was served at " + str(datetime.now())

@app.route("/views")
def views():
  global pageViews
  pageViews += 1
  return "This page has been viewed " + str(pageViews) + " times"