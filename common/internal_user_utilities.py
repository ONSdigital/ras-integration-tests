import common.respondent_utilities
from config import Config
from controllers.uaa_controller import create_user, generate_access_token


def create_internal_user_login_account(user_name):
    access_token = generate_access_token(client_id=Config.UAA_CLIENT_ID, client_secret=Config.UAA_SECRET)
    email = common.respondent_utilities.make_email_address(user_name, user_name)

    return create_user(access_token, user_name, Config.UAA_DEFAULT_USER_PASSWORD, email, user_name, user_name)
