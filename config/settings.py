from ras_common_utils.ras_config import ras_config


_config_path = 'config/config.yml'
_config = ras_config.from_yaml_file(_config_path)

SECURE_MESSAGING_SERVICE = '{}://{}:{}'.format(_config.service['secure-messaging-service']['scheme'],
                                               _config.service['secure-messaging-service']['host'],
                                               _config.service['secure-messaging-service']['port'])
SECURE_MESSAGING_SERVICE_API = _config.service['secure-messaging-service']['api']
