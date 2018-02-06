import logging

from structlog import wrap_logger

from controllers import collection_exercise_controller, collection_instrument_controller, database_controller

logger = wrap_logger(logging.getLogger(__name__))


if __name__ == '__main__':
    logging.info("Adding initial data required for executing collection exercise")
    # Add data required to execute collection exercise
    database_controller.execute_rm_sql('resources/database/set_up_ce_execute.sql')
    # Retrieve collection exercise for BRICKS 2018 and upload collection instrument for it
    bricks_2018_ce = collection_exercise_controller.get_collection_exercise('cb8accda-6118-4d3b-85a3-149e28960c54',
                                                                            '201801')
    ci_path = 'resources/collection_instrument_files/064_0001_201803.xlsx'
    collection_instrument_controller.upload_collection_instrument(bricks_2018_ce['id'], ci_path)
    logging.info("Required collection exercises can be executed")
