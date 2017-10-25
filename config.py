import os


class Config(object):
    # TODO: Find out if we need these
    NAME = os.getenv('NAME', 'ras-integration-tests')
    VERSION = os.getenv('VERSION', '0.1.0')

    RAS_SECURE_MESSAGE_SERVICE_HOST = os.getenv('RAS_SECURE_MESSAGE_SERVICE_HOST', 'localhost')
    RAS_SECURE_MESSAGE_SERVICE_PORT = os.getenv('RAS_SECURE_MESSAGE_SERVICE_PORT', 5050)
    RAS_SECURE_MESSAGE_SERVICE_PROTOCOL = os.getenv('RAS_SECURE_MESSAGE_SERVICE_PROTOCOL', 'http')
    RAS_SECURE_MESSAGE_SERVICE = '{}://{}:{}'.format(RAS_SECURE_MESSAGE_SERVICE_PROTOCOL,
                                                     RAS_SECURE_MESSAGE_SERVICE_HOST,
                                                     RAS_SECURE_MESSAGE_SERVICE_PORT)

    RAS_SECURE_MESSAGE_INFO = RAS_SECURE_MESSAGE_SERVICE + '/info'

    RAS_FRONTSTAGE_SERVICE_HOST = os.getenv('RAS_FRONTSTAGE_SERVICE_HOST', 'localhost')
    RAS_FRONTSTAGE_SERVICE_PORT = os.getenv('RAS_FRONTSTAGE_SERVICE_PORT', 8080)
    RAS_FRONTSTAGE_SERVICE_PROTOCOL = os.getenv('RAS_FRONTSTAGE_SERVICE_PROTOCOL', 'http')
    RAS_FRONTSTAGE_SERVICE = '{}://{}:{}'.format(RAS_FRONTSTAGE_SERVICE_PROTOCOL,
                                                 RAS_FRONTSTAGE_SERVICE_HOST,
                                                 RAS_FRONTSTAGE_SERVICE_PORT)

    RAS_FRONTSTAGE_INFO = RAS_FRONTSTAGE_SERVICE + '/info'

