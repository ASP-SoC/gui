""" contains configuration objects for the application """
# general imports
import os

class Config(object):
	DEBUG = False
	TESTING = False
	CSRF_ENABLED = True
	SECRET_KEY = os.urandom(32)

class ProductionConfig(Config):
	DEBUG = False

class StagingConfig(Config):
	DEVELOPMENT = True
	DEBUG = True

class DevelopmentConfig(Config):
	DEVELOPMENT = True
	DEBUG = True

class TestingConfig(Config):
	TESTING = True
