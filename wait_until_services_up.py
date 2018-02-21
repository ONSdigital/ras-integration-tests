import requests
from requests import RequestException
from retrying import retry

from config import Config


class HealthCheckException(Exception):
    def __init__(self, url):
        self.port = url

    def __str__(self) -> str:
        return f'Healthcheck fails for {self.port}'


def retry_if_http_error(exception):
    print(f'error has occurred: {str(exception)}')
    return isinstance(exception, RequestException) or isinstance(exception, HealthCheckException)


@retry(retry_on_exception=retry_if_http_error, wait_fixed=10000, stop_max_delay=600000, wrap_exception=True)
def check_services():
    for url in [Config.ACTION_SERVICE, Config.ACTION_EXPORTER,
                 Config.BACKSTAGE_SERVICE, Config.CASE_SERVICE,
                 Config.COLLECTION_EXERCISE, Config.COLLECTION_INSTRUMENT_SERVICE,
                 Config.DJANGO_SERVICE, Config.FRONTSTAGE_API_SERVICE,
                 Config.FRONTSTAGE_SERVICE, Config.IAC_SERVICE, Config.NOTIFY_GATEWAY_SERVICE,
                 Config.PARTY_SERVICE, Config.RESPONSE_OPERATIONS_UI, Config.SAMPLE_SERVICE,
                 Config.SECURE_MESSAGE_SERVICE, Config.SURVEY_SERVICE]:
        try:
            resp = requests.get(f'{url}/info')
            resp.raise_for_status()
        except Exception:
            raise HealthCheckException(url)


if __name__ == '__main__':
    check_services()
    print('all services are up')
