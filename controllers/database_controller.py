import logging
import time

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
    sql_statement = "SELECT a.iac FROM casesvc.caseiacaudit a " \
                    "INNER JOIN casesvc.case c ON a.casefk = c.casepk " \
                    "INNER JOIN iac.iac i ON a.iac = i.code " \
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

    sql_statement = "SELECT a.iac FROM casesvc.caseiacaudit a " \
                    "INNER JOIN casesvc.case c ON a.casefk = c.casepk " \
                    "INNER JOIN iac.iac i ON a.iac = i.code " \
                    "INNER JOIN casesvc.casegroup g ON c.casegroupfk = g.casegrouppk " \
                    f"WHERE c.statefk = 'ACTIONABLE' AND c.SampleUnitType = '{sample_unit_type}'" \
                    f"AND g.collectionexerciseid = '{collection_exercise_id}' " \
                    "AND i.active = TRUE " \
                    "ORDER BY c.createddatetime DESC LIMIT 1; "
    result = execute_sql(sql_string=sql_statement)
    iac = None
    for row in result:
        iac = row['iac']
    return iac


def get_all_iacs_for_collection_exercise(collection_exercise_id, social=False):

    if social:
        sample_unit_type = "H"
    else:
        sample_unit_type = "B"

    sql_statement = "SELECT a.iac FROM casesvc.caseiacaudit a " \
                    "INNER JOIN casesvc.case c ON a.casefk = c.casepk " \
                    "INNER JOIN iac.iac i ON a.iac = i.code " \
                    "INNER JOIN casesvc.casegroup g ON c.casegroupfk = g.casegrouppk " \
                    f"WHERE c.statefk = 'ACTIONABLE' AND c.SampleUnitType = '{sample_unit_type}'" \
                    f"AND g.collectionexerciseid = '{collection_exercise_id}' " \
                    "AND i.active = TRUE " \
                    "ORDER BY c.createddatetime DESC;"
    result = execute_sql(sql_string=sql_statement)
    iacs = []
    for row in result:
        iacs.append(row['iac'])
    return iacs


def poll_collection_exercise_until_state_changed(collection_exercise_id, state):

    for _ in range(60):
        sql = f"SELECT 1 FROM collectionexercise.collectionexercise" \
              f" WHERE id='{collection_exercise_id}' AND statefk = '{state}'"
        result = execute_sql(sql_string=sql)

        if len(result.fetchall()) == 1:
            return True

        time.sleep(2)

    return False
