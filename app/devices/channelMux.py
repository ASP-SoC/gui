""" channel mux device """
class ChannelMuxDevice(object):

	CONST_MODE_EXCHANGE = 1
	CONST_MODE_MERGE = 2

	CONST_EXCHANGE_STRAIGHT = 1
	CONST_EXCHANGE_CROSS = 2

	CONST_MERGE_LEFT = 1
	CONST_MERGE_RIGHT = 2

	def __init__(self, d_id, d_name, d_driverfile):
		self.id = d_id
		self.name = d_name
		self.mode = 1
		self.exchange = 1
		self.merge = 1
		self.mute_left = False
		self.mute_right = False
		self.__driverfile = d_driverfile

	def update(self, d_mode, d_exchange, d_merge, d_mute_left, d_mute_right):
		self.mode = d_mode
		self.exchange = d_exchange
		self.merge = d_merge
		self.mute_left = d_mute_left
		self.mute_right = d_mute_right


	def write_config(self):
		conf_byte = 0

		if self.mode == ChannelMuxDevice.CONST_MODE_EXCHANGE:
			if self.exchange == ChannelMuxDevice.CONST_EXCHANGE_CROSS:
				conf_byte += 1

		elif self.mode == ChannelMuxDevice.CONST_MODE_MERGE:
			conf_byte += 2

			if self.merge == ChannelMuxDevice.CONST_MERGE_RIGHT:
				conf_byte += 1

		if self.mute_right:
			conf_byte += 4

		if self.mute_left:
			conf_byte += 8

		with open(self.__driverfile, 'wb') as dev_file:
			dev_file.write(conf_byte.to_bytes(1, 'big'))

	def toDict(self):
		ret = {}
		ret['id'] = self.id
		ret['name'] = self.name
		ret['model'] = {}
		ret['model']['mode'] = self.mode
		ret['model']['exchange'] = self.exchange
		ret['model']['merge'] = self.merge
		ret['model']['mute_left'] = self.mute_left
		ret['model']['mute_right'] = self.mute_right

		return ret
