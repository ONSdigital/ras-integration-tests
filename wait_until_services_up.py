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
def check_status(url):
    try:
        resp = requests.get(f'{url}/info')
        resp.raise_for_status()
    except Exception:
        raise HealthCheckException(url)


if __name__ == '__main__':
    [check_status(v) for k, v in dict(vars(Config)).items() if k.endswith('_SERVICE') or k.endswith('_UI')]
    print('all services are up')
