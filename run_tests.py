from behave import __main__ as behave_executable
from ras_common_utils.ras_config import ras_config

config_path = 'config/config.yml'
config = ras_config.from_yaml_file(config_path)

secure_messaging_settings = config.service['secure-messaging-service']
SECURE_MESSAGING_SERVICE = '{}://{}:{}'.format(secure_messaging_settings['scheme'],
                                                secure_messaging_settings['host'],
                                                secure_messaging_settings['port'])
SECURE_MESSAGING_SERVICE_API = secure_messaging_settings['api']


if __name__ == '__main__':
    behave_executable.main()

    def before_scenario(context, scenario):
        if "ignore" in scenario.effective_tags:
            scenario.skip("Unimplemented Functionality")
            return
