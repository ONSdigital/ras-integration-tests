from config import Config
from controllers import database_controller


def reset_database():
    print('Resetting databases')
    print('Resetting various rm services')
    database_controller.execute_sql('resources/database/database_reset_rm.sql')
    print('Resetting case')
    database_controller.execute_sql('resources/database/database_reset_rm_case.sql')
    print('Resetting action')
    database_controller.execute_sql('resources/database/database_reset_rm_action.sql')
    print('Resetting action exporter')
    database_controller.execute_sql('resources/database/database_reset_rm_action_exporter.sql')
    print('Resetting party')
    database_controller.execute_sql('resources/database/database_reset_party.sql',
                                    database_uri=Config.PARTY_DATABASE_URI)
    print('Resetting auth')
    database_controller.execute_sql('resources/database/database_reset_oauth.sql',
                                    database_uri=Config.AUTH_DATABASE_URI)
    print('Resetting secure message')
    database_controller.execute_sql('resources/database/database_reset_secure_message.sql',
                                    database_uri=Config.SECURE_MESSAGE_DATABASE_URI)
    print('Resetting collection instrument')
    database_controller.execute_sql('resources/database/database_reset_ras_ci.sql',
                                    database_uri=Config.COLLECTION_INSTRUMENT_DATABASE_URI)
    print('Successfully reset databases')


if __name__ == '__main__':
    reset_database()
