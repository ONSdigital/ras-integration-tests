from controllers import collection_exercise_controller, collection_instrument_controller, database_controller

if __name__ == '__main__':
    print("Adding initial data required for executing collection exercises")
    # Add data required to execute collection exercises
    database_controller.execute_rm_sql('resources/database/collection_exercise_setup/bricks_201801_setup.sql')
    database_controller.execute_rm_sql('resources/database/collection_exercise_setup/bricks_201812_setup.sql')

    # Retrieve collection exercises upload collection instruments for them
    bricks_201801_ce = collection_exercise_controller.get_collection_exercise('cb8accda-6118-4d3b-85a3-149e28960c54',
                                                                              '201801')
    bricks_201812_ce = collection_exercise_controller.get_collection_exercise('cb8accda-6118-4d3b-85a3-149e28960c54',
                                                                              '201812')
    ci_path = 'resources/collection_instrument_files/064_0001_201803.xlsx'
    collection_instrument_controller.upload_seft_collection_instrument(bricks_201801_ce['id'], ci_path)
    collection_instrument_controller.upload_seft_collection_instrument(bricks_201812_ce['id'], ci_path)

    # upload eQ collection instrument for QBS
    collection_instrument_controller.upload_eq_collection_instrument('02b9c366-7397-42f7-942a-76dc5876d86d',
                                                                     '0001', '2')

    print("Required collection exercises can be executed")
