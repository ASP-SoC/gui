""" basic app initialisation """
# general imports
import os
from flask import Flask
from app.devices import ChannelMuxDevice

# personal imports
from app.driver_files import Driverfile

# code
root_dir = os.path.dirname(os.path.realpath(__file__))

f_app = Flask(__name__)
f_app.config.from_object('app.config.ProductionConfig')


# setup environment

environment = {}

environment['channel_mux_list'] = []
for i in range(0, (Driverfile.CHANNEL_MUX_CNT)):
	tmp = ChannelMuxDevice(i, str(i + 1), Driverfile.CHANNEL_MUX[i])
	environment['channel_mux_list'].append(tmp)


# get all routes for the system
import app.routes
