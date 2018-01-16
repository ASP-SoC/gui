""" basic app initialisation """
# general imports
import os
from flask import Flask

# personal imports

# code
root_dir = os.path.dirname(os.path.realpath(__file__))

f_app = Flask(__name__)
f_app.config.from_object('app.config.DevelopmentConfig')



# get all routes for the system
import app.routes
