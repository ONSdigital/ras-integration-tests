from controllers.collection_exercise_controller import get_collection_exercise
from controllers.database_controller import get_iac_for_collection_exercise
from controllers.django_oauth_controller import verify_user
from controllers.party_controller import change_respondent_status, get_respondent_details, register_respondent


class RespondentDetails:

    def __init__(self):
        self._respondent_id = None
        self._ru_id = None
        self._ru_ref = None

    @staticmethod
    def _create_respondent():
        collection_exercise_id = get_collection_exercise(
            'cb8accda-6118-4d3b-85a3-149e28960c54',
            '201801')['id']
        enrolment_code = get_iac_for_collection_exercise(collection_exercise_id)
        respondent_party = register_respondent(email_address='respondent@example.com',
                                               first_name='first_name',
                                               last_name='last_name',
                                               password='secret',
                                               phone_number='0187654321',
                                               enrolment_code=enrolment_code)
        verify_user(respondent_party['emailAddress'])
        change_respondent_status(respondent_party['id'])
        return respondent_party['id']

    def _create_respondent_and_get_details(self):
        if not self._respondent_id:
            self._respondent_id = self._create_respondent()
            respondent_details = get_respondent_details(self._respondent_id)
            self._ru_id = respondent_details['associations'][0]['partyId']
            self._ru_ref = respondent_details['associations'][0]['sampleUnitRef']

    def get_respondent_id(self):
        if not self._respondent_id:
            self._create_respondent_and_get_details()
        return self._respondent_id

    def get_ru_id(self):
        if not self._ru_id:
            self._create_respondent_and_get_details()
        return self._ru_id

    def get_ru_ref(self):
        if not self._ru_ref:
            self._create_respondent_and_get_details()
        return self._ru_ref


RESPONDENT_DETAILS = RespondentDetails()
