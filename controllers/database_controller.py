import logging

import requests
from sqlalchemy import create_engine
from structlog import wrap_logger

from config import Config


logger = wrap_logger(logging.getLogger(__name__))


def execute_rm_sql(sql_script_file_path):
    logger.debug('Executing SQL script', sql_script=sql_script_file_path)

    url = Config.CF_DATABASE_TOOL + '/sql'
    headers = {
        'Content-Type': 'text/plain'
    }
    with open(sql_script_file_path, 'r') as sqlScriptFile:
        sql_script = sqlScriptFile.read().replace('\n', '')

    response = requests.post(url, auth=Config.BASIC_AUTH, headers=headers, data=sql_script)

    # The response from the database tool as of 16/02/18 always comes back with 201 regardless
    # of whether the sql execution succeded or failed.  If tests are failing, check the database tool's
    # logs for any sqlExceptions.
    if response.status_code != 201:
        logger.error('SQL execution failed', status=response.status_code, sql_script=sql_script_file_path)

    logger.debug('Executed SQL script', sql_script=sql_script_file_path)
    return response.text


def reset_ras_database():
    logger.info("Putting party database into known state")
    engine = create_engine(Config.PARTY_DATABASE_URI)
    connection = engine.connect()
    trans = connection.begin()

    with open('resources/database/database_reset_party.sql', 'r') as sqlScriptFile:
        reset_party_sql = sqlScriptFile.read().replace('\n', '')

    connection.execute(reset_party_sql)
    trans.commit()

    logger.info("Putting django database into known state")
    engine = create_engine(Config.DJANGO_OAUTH_DATABASE_URI)
    connection = engine.connect()
    trans = connection.begin()

    with open('resources/database/database_reset_oauth.sql', 'r') as sqlScriptFile:
        reset_oauth_sql = sqlScriptFile.read().replace('\n', '')

    connection.execute(reset_oauth_sql)
    trans.commit()


def reset_secure_message_database():
    logger.info("Clearing down secure message database")
    engine = create_engine(Config.SECURE_MESSAGE_DATABASE_URI)
    connection = engine.connect()
    trans = connection.begin()

    with open('resources/database/database_reset_secure_message.sql', 'r') as sqlScriptFile:
        sql = sqlScriptFile.read().replace('\n', '')

    connection.execute(sql)
    trans.commit()
    connection.close()


def select_iac():
    url = Config.CF_DATABASE_TOOL + '/sql'
    headers = {
        'Content-Type': 'text/plain'
    }
    sql_statement = "SELECT c.iac FROM casesvc.case c " \
                    "INNER JOIN iac.iac i ON c.iac = i.code " \
                    "WHERE i.active = true AND i.lastuseddatetime IS NULL AND c.SampleUnitType = 'B' " \
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


def enrol_party(respondent_uuid):
    case_id = None

    sql_statement_update_enrolment = f"UPDATE partysvc.enrolment SET status = 'ENABLED' WHERE respondent_id = (SELECT id FROM partysvc.respondent WHERE party_uuid = '{respondent_uuid}');"  # NOQA
    sql_get_case_id = f"SELECT case_id FROM partysvc.pending_enrolment WHERE respondent_id = (SELECT id FROM partysvc.respondent WHERE party_uuid = '{respondent_uuid}');"  # NOQA
    sql_delete_pending_enrolment = f"DELETE FROM partysvc.pending_enrolment WHERE respondent_id = (SELECT id FROM partysvc.respondent WHERE party_uuid = '{respondent_uuid}');"  # NOQA

    engine = create_engine(Config.PARTY_DATABASE_URI)
    connection = engine.connect()

    result = connection.execute(sql_get_case_id)
    for row in result:
        case_id = row['case_id']

    trans = connection.begin()
    connection.execute(sql_statement_update_enrolment)
    connection.execute(sql_delete_pending_enrolment)
    trans.commit()

    return case_id
