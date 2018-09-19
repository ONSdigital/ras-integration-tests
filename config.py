import os


class Config(object):
    STANDALONE = os.getenv('STANDALONE', 'False')
    RESET_DATABASE = os.getenv('RESET_DATABASE', 'False')

    PROTOCOL = os.getenv('PROTOCOL', 'http')
    INFO = '/info'

    # todo redundant when all converted
    RESPONDENT_USERNAME = os.getenv('RESPONDENT_USERNAME', 'example@example.com')

    RESPONDENT_PASSWORD = os.getenv('RESPONDENT_PASSWORD', 'password')

    INTERNAL_USERNAME = os.getenv('INTERNAL_USERNAME', 'uaa_user')
    INTERNAL_PASSWORD = os.getenv('INTERNAL_PASSWORD', 'password')

    ACTION_SERVICE_HOST = os.getenv('ACTION_SERVICE_HOST', 'localhost')
    ACTION_SERVICE_PORT = os.getenv('ACTION_SERVICE_PORT', 8151)
    ACTION_SERVICE = f'{PROTOCOL}://{ACTION_SERVICE_HOST}:{ACTION_SERVICE_PORT}'

    ACTION_EXPORTER_HOST = os.getenv('ACTION_EXPORTER_HOST', 'localhost')
    ACTION_EXPORTER_PORT = os.getenv('ACTION_EXPORTER_PORT', 8141)
    ACTION_EXPORTER_SERVICE = f'{PROTOCOL}://{ACTION_EXPORTER_HOST}:{ACTION_EXPORTER_PORT}'

    CASE_SERVICE_HOST = os.getenv('CASE_SERVICE_HOST', 'localhost')
    CASE_SERVICE_PORT = os.getenv('CASE_SERVICE_PORT', 8171)
    CASE_SERVICE = f'{PROTOCOL}://{CASE_SERVICE_HOST}:{CASE_SERVICE_PORT}'

    COLLECTION_EXERCISE_SERVICE_HOST = os.getenv('COLLECTION_EXERCISE_SERVICE_HOST', 'localhost')
    COLLECTION_EXERCISE_SERVICE_PORT = os.getenv('COLLECTION_EXERCISE_SERVICE_PORT', 8145)
    COLLECTION_EXERCISE_SERVICE = f'{PROTOCOL}://{COLLECTION_EXERCISE_SERVICE_HOST}:{COLLECTION_EXERCISE_SERVICE_PORT}'

    COLLECTION_INSTRUMENT_SERVICE_HOST = os.getenv('COLLECTION_INSTRUMENT_SERVICE_HOST', 'localhost')
    COLLECTION_INSTRUMENT_SERVICE_PORT = os.getenv('COLLECTION_INSTRUMENT_SERVICE_PORT', 8002)
    COLLECTION_INSTRUMENT_SERVICE = f'{PROTOCOL}://{COLLECTION_INSTRUMENT_SERVICE_HOST}:' \
                                    f'{COLLECTION_INSTRUMENT_SERVICE_PORT}'

    DJANGO_SERVICE_HOST = os.getenv('DJANGO_SERVICE_HOST', 'localhost')
    DJANGO_SERVICE_PORT = os.getenv('DJANGO_SERVICE_PORT', 8040)
    DJANGO_SERVICE = f'{PROTOCOL}://{DJANGO_SERVICE_HOST}:{DJANGO_SERVICE_PORT}'

    FRONTSTAGE_SERVICE_HOST = os.getenv('FRONTSTAGE_SERVICE_HOST', 'localhost')
    FRONTSTAGE_SERVICE_PORT = os.getenv('FRONTSTAGE_SERVICE_PORT', 8082)
    FRONTSTAGE_SERVICE = f'{PROTOCOL}://{FRONTSTAGE_SERVICE_HOST}:{FRONTSTAGE_SERVICE_PORT}'

    IAC_SERVICE_HOST = os.getenv('IAC_SERVICE_HOST', 'localhost')
    IAC_SERVICE_PORT = os.getenv('IAC_SERVICE_PORT', 8121)
    IAC_SERVICE = f'{PROTOCOL}://{IAC_SERVICE_HOST}:{IAC_SERVICE_PORT}'

    NOTIFY_GATEWAY_SERVICE_HOST = os.getenv('NOTIFY_GATEWAY_SERVICE_HOST', 'localhost')
    NOTIFY_GATEWAY_SERVICE_PORT = os.getenv('NOTIFY_GATEWAY_SERVICE_PORT', 8181)
    NOTIFY_GATEWAY_SERVICE = f'{PROTOCOL}://{NOTIFY_GATEWAY_SERVICE_HOST}:{NOTIFY_GATEWAY_SERVICE_PORT}'

    PARTY_SERVICE_HOST = os.getenv('PARTY_SERVICE_HOST', 'localhost')
    PARTY_SERVICE_PORT = os.getenv('PARTY_SERVICE_PORT', 8081)
    PARTY_SERVICE = f'{PROTOCOL}://{PARTY_SERVICE_HOST}:{PARTY_SERVICE_PORT}'

    RESPONSE_OPERATIONS_UI_HOST = os.getenv('RESPONSE_OPERATIONS_UI_HOST', 'localhost')
    RESPONSE_OPERATIONS_UI_PORT = os.getenv('RESPONSE_OPERATIONS_UI_PORT', 8085)
    RESPONSE_OPERATIONS_UI = f'{PROTOCOL}://{RESPONSE_OPERATIONS_UI_HOST}:{RESPONSE_OPERATIONS_UI_PORT}'

    RESPONDENT_HOME_UI_HOST = os.getenv('RESPONDENT_HOME_UI_HOST', 'localhost')
    RESPONDENT_HOME_UI_PORT = os.getenv('RESPONDENT_HOME_UI_PORT', 9092)
    RESPONDENT_HOME_UI = f'{PROTOCOL}://{RESPONDENT_HOME_UI_HOST}:{RESPONDENT_HOME_UI_PORT}'

    SAMPLE_SERVICE_HOST = os.getenv('SAMPLE_SERVICE_HOST', 'localhost')
    SAMPLE_SERVICE_PORT = os.getenv('SAMPLE_SERVICE_PORT', 8125)
    SAMPLE_SERVICE = f'{PROTOCOL}://{SAMPLE_SERVICE_HOST}:{SAMPLE_SERVICE_PORT}'

    SECURE_MESSAGE_SERVICE_HOST = os.getenv('SECURE_MESSAGE_SERVICE_HOST', 'localhost')
    SECURE_MESSAGE_SERVICE_PORT = os.getenv('SECURE_MESSAGE_SERVICE_PORT', 5050)
    SECURE_MESSAGE_SERVICE = f'{PROTOCOL}://{SECURE_MESSAGE_SERVICE_HOST}:{SECURE_MESSAGE_SERVICE_PORT}'

    SURVEY_SERVICE_HOST = os.getenv('SURVEY_SERVICE_HOST', 'localhost')
    SURVEY_SERVICE_PORT = os.getenv('SURVEY_SERVICE_PORT', 8080)
    SURVEY_SERVICE = f'{PROTOCOL}://{SURVEY_SERVICE_HOST}:{SURVEY_SERVICE_PORT}'

    SECURITY_USER_NAME = os.getenv('SECURITY_USER_NAME', 'admin')
    SECURITY_USER_PASSWORD = os.getenv('SECURITY_USER_PASSWORD', 'secret')
    BASIC_AUTH = (SECURITY_USER_NAME, SECURITY_USER_PASSWORD)

    SFTP_HOST = os.getenv('SFTP_HOST', 'localhost')
    SFTP_PORT = os.getenv('SFTP_PORT', '122')
    SFTP_USERNAME = os.getenv('SFTP_USERNAME', 'centos')
    SFTP_PASSWORD = os.getenv('SFTP_PASSWORD', 'JLibV2&XD,')
    SFTP_DIR = os.getenv('SFTP_DIR', 'Documents/sftp')

    OAUTH_CLIENT_ID = os.getenv('OAUTH_CLIENT_ID', 'ons@ons.gov')
    OAUTH_CLIENT_SECRET = os.getenv('OAUTH_CLIENT_SECRET', 'password')

    DATABASE_URI = os.getenv('DATABASE_URI', "postgres://postgres:postgres@localhost:6432/postgres")
    DJANGO_OAUTH_DATABASE_URI = os.getenv('DJANGO_OAUTH_DATABASE_URI', DATABASE_URI)
    PARTY_DATABASE_URI = os.getenv('PARTY_DATABASE_URI', DATABASE_URI)
    COLLECTION_INSTRUMENT_DATABASE_URI = os.getenv('COLLECTION_INSTRUMENT_DATABASE_URI', DATABASE_URI)
    SECURE_MESSAGE_DATABASE_URI = os.getenv('SECURE_MESSAGE_DATABASE_URI', DATABASE_URI)
