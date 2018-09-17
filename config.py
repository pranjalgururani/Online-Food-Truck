import os

class Config(object):
    SECRET_KEY = 'I am here'
    DYNAMO_ENABLE_LOCAL = True
    DYNAMO_LOCAL_HOST = 'localhost'
    DYNAMO_LOCAL_PORT = 8000