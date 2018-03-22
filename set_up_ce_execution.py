from controllers import collection_exercise_controller, collection_instrument_controller, database_controller

if __name__ == '__main__':
    print("Adding initial data required for executing collection exercises")
    # Add data required to execute collection exercises
    database_controller.execute_rm_sql('resources/database/collection_exercise_setup/bricks_201801_setup.sql')
    database_controller.execute_rm_sql('resources/database/collection_exercise_setup/bricks_201812_setup.sql')
    database_controller.execute_rm_sql('resources/database/collection_exercise_setup/qbs_1809_setup.sql')

    # Upload eQ collection instrument for QBS
    # We can't upload eQ collection instruments through the UI
    qbs_1809_ce = collection_exercise_controller.get_collection_exercise('02b9c366-7397-42f7-942a-76dc5876d86d',
                                                                         '1809')
    collection_instrument_controller.upload_eq_collection_instrument('02b9c366-7397-42f7-942a-76dc5876d86d',
                                                                     '0001', '2')
    ci = collection_instrument_controller.get_collection_instruments_by_classifier(
        survey_id='02b9c366-7397-42f7-942a-76dc5876d86d',
        form_type='0001')
    collection_instrument_controller.link_collection_instrument_to_exercise(ci[0]['id'], qbs_1809_ce['id'])

    print("Required collection exercises can be executed")
