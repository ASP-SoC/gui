""" Provides functions to check request parameters """
# general imports
import json

class RequestService(object):

	def checkRequestParameters(params, param_list):

		if not params:
			raise ValueError('Parameters required')

		request_data = json.loads(params)

		if not all (param in request_data for param in param_list):
			raise ValueError('Parameters invalid')

		return request_data

	def dataHasKey(params, key):

		if not params:
			raise ValueError('Parameters required')

		request_data = json.loads(params)

		return key in request_data
