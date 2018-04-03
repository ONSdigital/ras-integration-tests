from controllers import database_controller

if __name__ == '__main__':
    print('Clearing down database')
    database_controller.execute_rm_sql('resources/database/database_reset_rm.sql')
    database_controller.reset_ras_database()
    database_controller.reset_secure_message_database()
