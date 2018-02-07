""" channel mux device """
class InputMuxDevice(object):

	CONST_MODE_CODEC = 1
	CONST_MODE_EXTERN = 2

	def __init__(self, d_id, d_name, d_driverfile):
		self.id = d_id
		self.name = d_name
		self.mode = InputMuxDevice.CONST_MODE_CODEC
		self.__driverfile = d_driverfile

	def update(self, d_mode):
		self.mode = d_mode

	def write_config(self):
		conf_byte = 0

		if self.mode == InputMuxDevice.CONST_MODE_EXTERN:
			conf_byte += 1

		with open(self.__driverfile, 'wb') as dev_file:
			dev_file.write(conf_byte.to_bytes(1, 'big'))

	def toDict(self):
		ret = {}
		ret['id'] = self.id
		ret['name'] = self.name
		ret['model'] = {}
		ret['model']['mode'] = self.mode

		return ret
