import requests
from requests import RequestException
from retrying import retry

from config import Config


class HealthCheckException(Exception):
    def __init__(self, port):
        self.port = port

    def __str__(self) -> str:
        return f'Healthcheck fails on port {self.port}'


def retry_if_http_error(exception):
    print(f'error has occurred: {str(exception)}')
    return isinstance(exception, RequestException) or isinstance(exception, HealthCheckException)


@retry(retry_on_exception=retry_if_http_error, wait_fixed=10000, stop_max_delay=400000, wrap_exception=True)
def check_services():
    for port in [Config.ACTION_SERVICE_PORT, Config.BACKSTAGE_SERVICE_PORT,
                 Config.CASE_SERVICE_PORT, Config.COLLECTION_EXERCISE_SERVICE_PORT,
                 Config.COLLECTION_INSTRUMENT_SERVICE_PORT, Config.DJANGO_SERVICE_PORT,
                 Config.FRONTSTAGE_API_SERVICE_PORT,
                 Config.IAC_SERVICE_PORT, Config.NOTIFY_GATEWAY_SERVICE_PORT, Config.PARTY_SERVICE_PORT,
                 Config.FRONTSTAGE_SERVICE_PORT,
                 Config.SURVEY_SERVICE_PORT, Config.SAMPLE_SERVICE_PORT, Config.SECURE_MESSAGE_SERVICE_PORT,
                 Config.ACTION_EXPORTER_PORT,
                 Config.RESPONSE_OPERATIONS_UI_PORT]:
        try:
            resp = requests.get(f'http://localhost:{port}/info')
            resp.raise_for_status()
        except Exception:
            raise HealthCheckException(port)


if __name__ == '__main__':
    check_services()
    print('all services are up')
