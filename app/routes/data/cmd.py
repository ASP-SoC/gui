""" Routes for the channel mux device """
# general imports
import os
from flask import request, jsonify
from flask_api import status

# personal imports
from app import f_app, root_dir
from app.services import RequestService, DataService, DataFailure

@f_app.route('/api/v0.1/cmd/update', methods=['POST'])
def cmd_update():
	param_list = ['id', 'model']

	ret = {}
	ret['success'] = True

	try:
		request_data = RequestService.checkRequestParameters(request.data, param_list)

		DataService.cmd_update(request_data['id'], request_data['model'])
	except ValueError as err:
		return str(err), status.HTTP_400_BAD_REQUEST
	except DataFailure as err:
		ret['msg'] = str(err)
		ret['success'] = False

	return jsonify(ret)


@f_app.route('/api/v0.1/cmd/get', methods=['POST'])
def cmd_get():
	ret = {}
	ret['success'] = True

	try:
		ret['data'] = DataService.cmd_get()
	except ValueError as err:
		return str(err), status.HTTP_400_BAD_REQUEST
	except DataFailure as err:
		ret['msg'] = str(err)
		ret['success'] = False

	return jsonify(ret)
