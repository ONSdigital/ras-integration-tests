import json

import requests

from config import Config


def generate_access_token(client_id, client_secret):
    headers = {'Content-Type': 'application/x-www-form-urlencoded',
               'Accept': 'application/json'}

    payload = {'grant_type': 'client_credentials',
               'response_type': 'token',
               'token_format': 'opaque'}

    response = requests.post(url=f'{Config.UAA_SERVICE_URL}/oauth/token',
                             headers=headers,
                             params=payload,
                             auth=(client_id, client_secret))

    response.raise_for_status()

    return response.json().get('access_token')


def create_user(access_token, username, password, email, first_name, last_name):
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

    response = requests.post(url=f'{Config.UAA_SERVICE_URL}/Users',
                             data=json.dumps(user),
                             headers=headers)

    response.raise_for_status()

    return response
