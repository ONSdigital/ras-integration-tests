import json

import requests

from common import survey_utilities
from config import Config


def create_internal_user_login_account(user_name):
    tokenUrl = f'{Config.UAA_SERVICE}/oauth/token'

    access_token = generate_access_token(client_id=Config.UAA_CLIENT_ID, client_secret=Config.UAA_SECRET, url=tokenUrl)

    userUrl = f'{Config.UAA_SERVICE}/Users'
    email = survey_utilities.make_email_address(user_name, user_name)

    return create_user(access_token, user_name, Config.UAA_DEFAULT_USER_PASSWORD, email, user_name, user_name, userUrl)


def generate_access_token(client_id, client_secret, url):
    headers = {'Content-Type': 'application/x-www-form-urlencoded',
               'Accept': 'application/json'}

    payload = {'grant_type': 'client_credentials',
               'response_type': 'token',
               'token_format': 'opaque'}

    response = requests.post(url=url, headers=headers,
                             params=payload,
                             auth=(client_id, client_secret))

    response.raise_for_status()

    return response.json().get('access_token')


def create_user(access_token, username, password, email, first_name, last_name, url):
    user = {
        "userName": username,
        "name": {
            "formatted": f'{first_name} {last_name}',
            "givenName": first_name,
            "familyName": last_name
        },
        "emails": [{
            "value": email,
            "primary": False
        }],
        "active": True,
        "verified": True,
        "password": password
    }

    headers = {'Content-Type': 'application/json',
               'Accept': 'application/json',
               'Authorization': f'Bearer {access_token}'}

    response = requests.post(url, data=json.dumps(user),
                             headers=headers)

    response.raise_for_status()

    return response
