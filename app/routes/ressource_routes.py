""" routes to access html elements """
# general imports
import os
from flask import send_from_directory, make_response

# personal imports
from app import f_app, root_dir

@f_app.route('/')
def index():
	return make_response(open('app/base/index.htm').read())

# directives to get js, css, html and plugin files
@f_app.route('/js/<path:filename>')
def serve_static_js(filename):
	return send_from_directory(os.path.join(root_dir, 'static', 'js'), filename)

@f_app.route('/css/<path:filename>')
def serve_static_css(filename):
	return send_from_directory(os.path.join(root_dir, 'static', 'css'), filename)

@f_app.route('/html/<path:filename>')
def serve_static_html(filename):
	return send_from_directory(os.path.join(root_dir, 'static', 'html'), filename)

@f_app.route('/pics/<path:filename>')
def serve_static_pics(filename):
	return send_from_directory(os.path.join(root_dir, 'static', 'pics'), filename)

@f_app.route('/plugin/<path:filename>')
def service_static_plugin(filename):
	return send_from_directory(os.path.join(root_dir, 'static', 'plugin'), filename)

@f_app.route('/favicon.ico')
def service_favicon():
	return send_from_directory(os.path.join(root_dir, 'static', 'pics'), 'favicon.ico')
