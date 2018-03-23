import logging

import requests
from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from structlog import wrap_logger

from config import Config

logger = wrap_logger(logging.getLogger(__name__))


def execute_sql(sql_script_file_path):
    logger.debug('Executing SQL script', sql_script_file_path=sql_script_file_path)
    engine = create_engine(Config.DATABASE_URI)
    connection = engine.connect()
    trans = connection.begin()

    with open(sql_script_file_path, 'r') as sqlScriptFile:
        reset_party_sql = sqlScriptFile.read().replace('\n', '')

    try:
        connection.execute(reset_party_sql)
    except IntegrityError:
        logger.info('Script has already been run', sql_script_file_path=sql_script_file_path)

    trans.commit()
    logger.debug('Successfully executed SQL script', sql_script_file_path=sql_script_file_path)


def execute_sql_secure_message(sql_script_file_path):
    logger.debug('Executing SQL script', sql_script_file_path=sql_script_file_path)
    engine = create_engine(Config.SECURE_MESSAGE_DATABASE_URI)
    connection = engine.connect()
    trans = connection.begin()

    with open(sql_script_file_path, 'r') as sqlScriptFile:
        reset_party_sql = sqlScriptFile.read().replace('\n', '')

    connection.execute(reset_party_sql)
    trans.commit()
    logger.debug('Successfully executed SQL script', sql_script_file_path=sql_script_file_path)


def select_iac():
    url = Config.CF_DATABASE_TOOL + '/sql'
    headers = {
        'Content-Type': 'text/plain'
    }
    sql_statement = "SELECT c.iac FROM casesvc.case c " \
                    "INNER JOIN iac.iac i ON c.iac = i.code " \
                    "WHERE i.active = TRUE AND i.lastuseddatetime IS NULL AND c.SampleUnitType = 'B' " \
                    "ORDER BY i.createddatetime DESC LIMIT 1;"
    response = requests.post(url, auth=Config.BASIC_AUTH, headers=headers, data=sql_statement)
    return response.text[4:-1]


def get_iac_for_collection_exercise(collection_exercise_id):
    url = Config.CF_DATABASE_TOOL + '/sql'
    headers = {
        'Content-Type': 'text/plain'
    }
    sql_statement = "SELECT c.iac FROM casesvc.case c " \
                    "INNER JOIN casesvc.casegroup g ON g.id = c.casegroupid " \
                    "WHERE c.statefk = 'ACTIONABLE' AND c.SampleUnitType = 'B' " \
                    f"AND g.collectionexerciseid = '{collection_exercise_id}' " \
                    "ORDER BY c.createddatetime DESC LIMIT 1;"
    response = requests.post(url, auth=Config.BASIC_AUTH, headers=headers, data=sql_statement)
    return response.text[4:-1]


def get_iac_for_collection_exercise_and_business(collection_exercise_id, business_id):
    url = Config.CF_DATABASE_TOOL + '/sql'
    headers = {
        'Content-Type': 'text/plain'
    }
    sql_statement = "SELECT c.iac FROM casesvc.case c " \
                    "INNER JOIN casesvc.casegroup g ON g.id = c.casegroupid " \
                    "WHERE c.statefk = 'ACTIONABLE' AND c.SampleUnitType = 'B' " \
                    f"AND g.collectionexerciseid = '{collection_exercise_id}'" \
                    f"AND c.partyid = '{business_id}'" \
                    "ORDER BY c.createddatetime DESC LIMIT 1;"
    response = requests.post(url, auth=Config.BASIC_AUTH, headers=headers, data=sql_statement)
    return response.text[4:-1]


def enrol_party(respondent_uuid):
    case_id = None

    sql_statement_update_enrolment = f"UPDATE partysvc.enrolment SET status = 'ENABLED' WHERE respondent_id = (SELECT id FROM partysvc.respondent WHERE party_uuid = '{respondent_uuid}');"  # NOQA
    sql_get_case_id = f"SELECT case_id FROM partysvc.pending_enrolment WHERE respondent_id = (SELECT id FROM partysvc.respondent WHERE party_uuid = '{respondent_uuid}');"  # NOQA
    sql_delete_pending_enrolment = f"DELETE FROM partysvc.pending_enrolment WHERE respondent_id = (SELECT id FROM partysvc.respondent WHERE party_uuid = '{respondent_uuid}');"  # NOQA

    engine = create_engine(Config.DATABASE_URI)
    connection = engine.connect()

    result = connection.execute(sql_get_case_id)
    for row in result:
        case_id = row['case_id']

    trans = connection.begin()
    connection.execute(sql_statement_update_enrolment)
    connection.execute(sql_delete_pending_enrolment)
    trans.commit()

    return case_id
