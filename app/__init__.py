import os
from flask import Flask

f_app = Flask(__name__)
f_app.config.from_object('app.config.DevelopmentConfig')
