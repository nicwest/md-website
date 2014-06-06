from flask import Flask

#make with the flaskings
app = Flask(__name__)

#load config
app.config.from_object('config')

from app import views
