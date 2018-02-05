""" Provides Functions to manage data """
# general imports

# personal imports

class DataService(object):

	def cmd_update(id, data):
		print(id)
		print(data)

	def cmd_get():
		ret = []

		elem = {}
		elem['id'] = 0
		elem['name'] = 'One'
		elem['model'] = {}
		elem['model']['usage'] = 1
		elem['model']['exchange'] = 1
		elem['model']['merge'] = 1

		ret.append(elem)

		elem = {}
		elem['id'] = 1
		elem['name'] = 'Two'
		elem['model'] = {}
		elem['model']['usage'] = 2
		elem['model']['exchange'] = 1
		elem['model']['merge'] = 2

		ret.append(elem)
		return ret

class DataFailure(Exception):
	""" Failure during data access """
