import logging

from sqlalchemy import create_engine
from structlog import wrap_logger

from config import Config

logger = wrap_logger(logging.getLogger(__name__))


def execute_sql(sql_script_file_path=None, sql_string=None, database_uri=Config.DATABASE_URI):
    logger.debug('Executing SQL script', sql_script_file_path=sql_script_file_path)
    engine = create_engine(database_uri)
    connection = engine.connect()
    trans = connection.begin()

    if sql_script_file_path:
        with open(sql_script_file_path, 'r') as sqlScriptFile:
            sql = sqlScriptFile.read().replace('\n', '')
    else:
        sql = sql_string

    response = connection.execute(sql)

    trans.commit()
    logger.debug('Successfully executed SQL script', sql_script_file_path=sql_script_file_path)
    return response


def select_iac():
    sql_statement = "SELECT c.iac FROM casesvc.case c " \
                    "INNER JOIN iac.iac i ON c.iac = i.code " \
                    "WHERE i.active = TRUE AND i.lastuseddatetime IS NULL AND c.SampleUnitType = 'B' " \
                    "ORDER BY i.createddatetime DESC LIMIT 1;"
    result = execute_sql(sql_string=sql_statement)
    iac = None
    for row in result:
        iac = row['iac']
    return iac


def get_iac_for_collection_exercise(collection_exercise_id, social=False):

    if social:
        sample_unit_type = "H"
    else:
        sample_unit_type = "B"

    sql_statement = "SELECT c.iac FROM casesvc.case c " \
                    "INNER JOIN casesvc.casegroup g ON g.id = c.casegroupid " \
                    "INNER JOIN iac.iac i ON c.iac = i.code " \
                    f"WHERE c.statefk = 'ACTIONABLE' AND c.SampleUnitType = '{sample_unit_type}'" \
                    f"AND g.collectionexerciseid = '{collection_exercise_id}' " \
                    "AND i.active = TRUE " \
                    "ORDER BY c.createddatetime DESC LIMIT 1;"
    result = execute_sql(sql_string=sql_statement)
    iac = None
    for row in result:
        iac = row['iac']
    return iac


def get_iac_for_collection_exercise_and_business(collection_exercise_id, business_id):
    sql_statement = "SELECT c.iac FROM casesvc.case c " \
                    "INNER JOIN casesvc.casegroup g ON g.id = c.casegroupid " \
                    "INNER JOIN iac.iac i ON c.iac = i.code " \
                    "WHERE c.statefk = 'ACTIONABLE' AND c.SampleUnitType = 'B' " \
                    f"AND g.collectionexerciseid = '{collection_exercise_id}' " \
                    "AND i.active = TRUE " \
                    f"AND c.partyid = '{business_id}' " \
                    "ORDER BY c.createddatetime DESC LIMIT 1;"
    result = execute_sql(sql_string=sql_statement)
    iac = None
    for row in result:
        iac = row['iac']
    return iac


def enrol_party(respondent_uuid):
    # Enrolling respondent for enrolment code that they registered for is a slightly different
    # process that enrolling to a survey when already registered so we use SQL here
    sql_statement_update_enrolment = f"UPDATE partysvc.enrolment SET status = 'ENABLED' WHERE respondent_id = (SELECT id FROM partysvc.respondent WHERE party_uuid = '{respondent_uuid}');"  # NOQA
    execute_sql(sql_string=sql_statement_update_enrolment, database_uri=Config.PARTY_DATABASE_URI)

    sql_get_case_id = f"SELECT case_id FROM partysvc.pending_enrolment WHERE respondent_id = (SELECT id FROM partysvc.respondent WHERE party_uuid = '{respondent_uuid}');"  # NOQA
    result = execute_sql(sql_string=sql_get_case_id, database_uri=Config.PARTY_DATABASE_URI)
    case_id = None
    for row in result:
        case_id = row['case_id']

    sql_delete_pending_enrolment = f"DELETE FROM partysvc.pending_enrolment WHERE respondent_id = (SELECT id FROM partysvc.respondent WHERE party_uuid = '{respondent_uuid}');"  # NOQA
    execute_sql(sql_string=sql_delete_pending_enrolment, database_uri=Config.PARTY_DATABASE_URI)

    return case_id
