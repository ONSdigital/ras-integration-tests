import logging

import requests
from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from structlog import wrap_logger

from config import Config

logger = wrap_logger(logging.getLogger(__name__))


def execute_ras_sql(sql_script_file_path=None, sql_string=None, database_uri=Config.DATABASE_URI):
    logger.debug('Executing SQL script', sql_script_file_path=sql_script_file_path)
    engine = create_engine(database_uri)
    connection = engine.connect()
    trans = connection.begin()

    if sql_script_file_path:
        with open(sql_script_file_path, 'r') as sqlScriptFile:
            sql = sqlScriptFile.read().replace('\n', '')
    else:
        sql = sql_string

    try:
        response = connection.execute(sql)
    except IntegrityError:
        logger.info('Script has already been run', sql_script_file_path=sql_script_file_path)
        response = None

    trans.commit()
    logger.debug('Successfully executed SQL script', sql_script_file_path=sql_script_file_path)
    return response


def execute_rm_sql(sql_script_file_path=None, sql_string=None):
    logger.debug('Executing sql with cf database tool', sql_script_file_path=sql_script_file_path)
    url = Config.CF_DATABASE_TOOL + '/sql'
    headers = {
        'Content-Type': 'text/plain'
    }

    if sql_script_file_path:
        with open(sql_script_file_path, 'r') as sqlScriptFile:
            sql = sqlScriptFile.read().replace('\n', '')
    else:
        sql = sql_string

    response = requests.post(url, auth=Config.BASIC_AUTH, headers=headers, data=sql)
    response.raise_for_status()
    logger.debug('Successfully executed sql with cf database tool', sql_script_file_path=sql_script_file_path)
    return response


def select_iac():
    sql_statement = "SELECT c.iac FROM casesvc.case c " \
                    "INNER JOIN iac.iac i ON c.iac = i.code " \
                    "WHERE i.active = TRUE AND i.lastuseddatetime IS NULL AND c.SampleUnitType = 'B' " \
                    "ORDER BY i.createddatetime DESC LIMIT 1;"
    result = execute_rm_sql(sql_string=sql_statement)
    return result.text[4:-1]


def get_iac_for_collection_exercise(collection_exercise_id):
    sql_statement = "SELECT c.iac FROM casesvc.case c " \
                    "INNER JOIN casesvc.casegroup g ON g.id = c.casegroupid " \
                    "WHERE c.statefk = 'ACTIONABLE' AND c.SampleUnitType = 'B' " \
                    f"AND g.collectionexerciseid = '{collection_exercise_id}' " \
                    "ORDER BY c.createddatetime DESC LIMIT 1;"
    result = execute_rm_sql(sql_string=sql_statement)
    return result.text[4:-1]


def get_iac_for_collection_exercise_and_business(collection_exercise_id, business_id):
    sql_statement = "SELECT c.iac FROM casesvc.case c " \
                    "INNER JOIN casesvc.casegroup g ON g.id = c.casegroupid " \
                    "WHERE c.statefk = 'ACTIONABLE' AND c.SampleUnitType = 'B' " \
                    f"AND g.collectionexerciseid = '{collection_exercise_id}'" \
                    f"AND c.partyid = '{business_id}'" \
                    "ORDER BY c.createddatetime DESC LIMIT 1;"
    result = execute_rm_sql(sql_string=sql_statement)
    return result.text[4:-1]


def enrol_party(respondent_uuid):
    # Enrolling respondent for enrolment code that they registered for is a slightly different
    # process that enrolling to a survey when already registered so we use SQL here
    sql_statement_update_enrolment = f"UPDATE partysvc.enrolment SET status = 'ENABLED' WHERE respondent_id = (SELECT id FROM partysvc.respondent WHERE party_uuid = '{respondent_uuid}');"  # NOQA
    execute_ras_sql(sql_string=sql_statement_update_enrolment, database_uri=Config.PARTY_DATABASE_URI)

    sql_delete_pending_enrolment = f"DELETE FROM partysvc.pending_enrolment WHERE respondent_id = (SELECT id FROM partysvc.respondent WHERE party_uuid = '{respondent_uuid}');"  # NOQA
    execute_ras_sql(sql_string=sql_delete_pending_enrolment, database_uri=Config.PARTY_DATABASE_URI)

    sql_get_case_id = f"SELECT case_id FROM partysvc.pending_enrolment WHERE respondent_id = (SELECT id FROM partysvc.respondent WHERE party_uuid = '{respondent_uuid}');"  # NOQA
    result = execute_ras_sql(sql_string=sql_get_case_id, database_uri=Config.PARTY_DATABASE_URI)
    return result[-1]['case_id']
