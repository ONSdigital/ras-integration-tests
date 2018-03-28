from controllers import collection_instrument_controller, database_controller

if __name__ == '__main__':
    print("Adding initial data required for executing collection exercises")
    # Add data required to execute collection exercises
    database_controller.execute_rm_sql('resources/database/collection_exercise_setup/bricks_201801_setup.sql')
    database_controller.execute_rm_sql('resources/database/collection_exercise_setup/bricks_201812_setup.sql')
    database_controller.execute_rm_sql('resources/database/collection_exercise_setup/qbs_1809_setup.sql')
    database_controller.execute_rm_sql('resources/database/collection_exercise_setup/ashe_201803_setup.sql')
    database_controller.execute_rm_sql('resources/database/collection_exercise_setup/rsi_201812_setup.sql')

    # Upload eQ collection instrument for QBS
    collection_instrument_controller.upload_eq_collection_instrument(survey_id='02b9c366-7397-42f7-942a-76dc5876d86d',
                                                                     form_type='0001', eq_id='2')
    print("Required collection exercises can be executed")
