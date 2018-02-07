""" Routes for the channel mux device """
# general imports
import os
from flask import request, jsonify
from flask_api import status

# personal imports
from app import f_app, root_dir
from app.services import RequestService, DataService, DataFailure

@f_app.route('/api/v0.1/imd/update', methods=['POST'])
def imd_update():
	param_list = ['id', 'model']
	sub_param_list = ['mode']

	ret = {}
	ret['success'] = True

	try:
		request_data = RequestService.checkRequestParameters(request.data, param_list)

		DataService.imd_update(request_data['id'], request_data['model'])
	except ValueError as err:
		return str(err), status.HTTP_400_BAD_REQUEST
	except DataFailure as err:
		ret['msg'] = str(err)
		ret['success'] = False

	return jsonify(ret)


@f_app.route('/api/v0.1/imd/get', methods=['POST'])
def imd_get():
	ret = {}
	ret['success'] = True

	try:
		ret['data'] = DataService.imd_get()
	except ValueError as err:
		return str(err), status.HTTP_400_BAD_REQUEST
	except DataFailure as err:
		ret['msg'] = str(err)
		ret['success'] = False

	return jsonify(ret)
