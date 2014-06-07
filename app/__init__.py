from flask import Flask
from flask.ext.cache import Cache

#make with the flaskings
app = Flask(__name__)

#load config
app.config.from_object('config')
cache = Cache(app,config={'CACHE_TYPE': 'simple'})

from app import views
