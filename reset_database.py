from requests.exceptions import HTTPError

from config import Config
from controllers import database_controller
from controllers import survey_controller

def reset_database():
    print('Resetting databases')
    print('Resetting various rm services')
    database_controller.execute_sql('resources/database/database_reset_rm.sql')
    print('Resetting case')
    database_controller.execute_sql('resources/database/database_reset_rm_case.sql')
    print('Resetting action')
    database_controller.execute_sql('resources/database/database_reset_rm_action.sql')
    print('Resetting action exporter')
    database_controller.execute_sql('resources/database/database_reset_rm_action_exporter.sql')
    print('Resetting party')
    database_controller.execute_sql('resources/database/database_reset_party.sql',
                                    database_uri=Config.PARTY_DATABASE_URI)
    print('Resetting auth')
    database_controller.execute_sql('resources/database/database_reset_oauth.sql',
                                    database_uri=Config.AUTH_DATABASE_URI)
    print('Resetting secure message')
    database_controller.execute_sql('resources/database/database_reset_secure_message.sql',
                                    database_uri=Config.SECURE_MESSAGE_DATABASE_URI)
    print('Resetting collection instrument')
    database_controller.execute_sql('resources/database/database_reset_ras_ci.sql',
                                    database_uri=Config.COLLECTION_INSTRUMENT_DATABASE_URI)
    print('Successfully reset databases')

    print('Creating vacancies surveys')
    # If getting a survey isn't found, it raises an HTTPError (as raise_for_status considers it a failure).
    # When this happens, we create the survey.  If it comes back with a 200 then it's already there.
    try:
        survey_controller.get_survey_by_short_name('VACS2')
    except HTTPError:
        survey_controller.create_survey('182', 'VACS2', 'Quarterly Vacancy Survey', 'STA1947')

    try:
        survey_controller.get_survey_by_short_name('VACS3')
    except HTTPError:
        survey_controller.create_survey('183', 'VACS3', 'Quarterly Vacancy Survey', 'STA1947')

    try:
        survey_controller.get_survey_by_short_name('VACS4')
    except HTTPError:
        survey_controller.create_survey('184', 'VACS4', 'Quarterly Vacancy Survey', 'STA1947')

    try:
        survey_controller.get_survey_by_short_name('VACS5')
    except HTTPError:
        survey_controller.create_survey('185', 'VACS5', 'Monthly Vacancy Survey', 'STA1947')
    print('vacancies surveys completed')


if __name__ == '__main__':
    reset_database()
