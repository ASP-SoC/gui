""" Provides Functions to manage data """
# general imports

# personal imports
from app import environment

class DataService(object):

	def cmd_update(id, data):

		elem = environment['channel_mux_list'][id]

		elem.update(data['mode'], data['exchange'], data['merge'], data['mute_left'], data['mute_right'])

		elem.write_config()

	def cmd_get():

		ret = []

		for tmp in environment['channel_mux_list']:
			ret.append(tmp.toDict())

		return ret

	def imd_update(id, data):
		elem = environment['input_mux_list'][id]

		elem.update(data['mode'])

		elem.write_config()

	def imd_get():

		ret = []

		for tmp in environment['input_mux_list']:
			ret.append(tmp.toDict())

		return ret

class DataFailure(Exception):
	""" Failure during data access """
