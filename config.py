import os


class Config(object):
    # TODO: Find out if we need these
    NAME = os.getenv('NAME', 'ras-integration-tests')
    VERSION = os.getenv('VERSION', '0.1.0')
    RAS_PROTOCOL = os.getenv('RAS_PROTOCOL', 'http')

    RAS_SECURE_MESSAGE_SERVICE_HOST = os.getenv('RAS_SECURE_MESSAGE_SERVICE_HOST', 'localhost')
    RAS_SECURE_MESSAGE_SERVICE_PORT = os.getenv('RAS_SECURE_MESSAGE_SERVICE_PORT', 5050)
    RAS_SECURE_MESSAGE_SERVICE = '{}://{}:{}'.format(RAS_PROTOCOL,
                                                     RAS_SECURE_MESSAGE_SERVICE_HOST,
                                                     RAS_SECURE_MESSAGE_SERVICE_PORT)

    RAS_SECURE_MESSAGE_INFO = RAS_SECURE_MESSAGE_SERVICE + '/info'

    RAS_FRONTSTAGE_SERVICE_HOST = os.getenv('RAS_FRONTSTAGE_SERVICE_HOST', 'localhost')
    RAS_FRONTSTAGE_SERVICE_PORT = os.getenv('RAS_FRONTSTAGE_SERVICE_PORT', 8080)
    RAS_FRONTSTAGE_SERVICE = '{}://{}:{}'.format(RAS_PROTOCOL,
                                                 RAS_FRONTSTAGE_SERVICE_HOST,
                                                 RAS_FRONTSTAGE_SERVICE_PORT)

    RAS_FRONTSTAGE_INFO = RAS_FRONTSTAGE_SERVICE + '/info'

    RAS_BACKSTAGE_SERVICE_HOST = os.getenv('RAS_BACKSTAGE_SERVICE_HOST', 'localhost')
    RAS_BACKSTAGE_SERVICE_PORT = os.getenv('RAS_BACKSTAGE_SERVICE_PORT', 5001)
    RAS_BACKSTAGE_SERVICE = '{}://{}:{}'.format(RAS_PROTOCOL,
                                                RAS_BACKSTAGE_SERVICE_HOST,
                                                RAS_BACKSTAGE_SERVICE_PORT)

    RAS_BACKSTAGE_INFO = RAS_BACKSTAGE_SERVICE + '/info'

    RAS_PARTY_SERVICE_HOST = os.getenv('RAS_PARTY_SERVICE_HOST', 'localhost')
    RAS_PARTY_SERVICE_PORT = os.getenv('RAS_PARTY_SERVICE_PORT', 8081)
    RAS_PARTY_SERVICE = '{}://{}:{}'.format(RAS_PROTOCOL,
                                            RAS_PARTY_SERVICE_HOST,
                                            RAS_PARTY_SERVICE_PORT)

    RAS_PARTY_INFO = RAS_PARTY_SERVICE + '/info'

    RAS_COLLECTION_INSTRUMENT_SERVICE_HOST = os.getenv('RAS_COLLECTION_INSTRUMENT_SERVICE_HOST', 'localhost')
    RAS_COLLECTION_INSTRUMENT_SERVICE_PORT = os.getenv('RAS_COLLECTION_INSTRUMENT_SERVICE_PORT', 8082)
    RAS_COLLECTION_INSTRUMENT_SERVICE = '{}://{}:{}'.format(RAS_PROTOCOL,
                                                            RAS_COLLECTION_INSTRUMENT_SERVICE_HOST,
                                                            RAS_COLLECTION_INSTRUMENT_SERVICE_PORT)

    RAS_COLLECTION_INSTRUMENT_INFO = RAS_COLLECTION_INSTRUMENT_SERVICE + '/info'

    RAS_DJANGO_SERVICE_HOST = os.getenv('RAS_DJANGO_SERVICE_HOST', 'localhost')
    RAS_DJANGO_SERVICE_PORT = os.getenv('RAS_DJANGO_SERVICE_PORT', 8040)
    RAS_DJANGO_SERVICE = '{}://{}:{}'.format(RAS_PROTOCOL,
                                             RAS_DJANGO_SERVICE_HOST,
                                             RAS_DJANGO_SERVICE_PORT)

    RAS_DJANGO_INFO = RAS_DJANGO_SERVICE + '/info'

    RAS_API_GATEWAY_SERVICE_HOST = os.getenv('RAS_API_GATEWAY_SERVICE_HOST', 'localhost')
    RAS_API_GATEWAY_SERVICE_PORT = os.getenv('RAS_API_GATEWAY_SERVICE_PORT', 8083)
    RAS_API_GATEWAY_SERVICE = '{}://{}:{}'.format(RAS_PROTOCOL,
                                                  RAS_API_GATEWAY_SERVICE_HOST,
                                                  RAS_API_GATEWAY_SERVICE_PORT)

    RAS_API_GATEWAY_INFO = RAS_API_GATEWAY_SERVICE + '/info'
