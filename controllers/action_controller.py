import logging

import requests
from structlog import wrap_logger

from config import Config

logger = wrap_logger(logging.getLogger(__name__))


def create_action_rule(survey_name, period):
    logger.debug('Finding action plan', survey_name=survey_name, period=period)
    url = f'{Config.ACTION_SERVICE}/actionplans'
    response = requests.get(url, auth=Config.BASIC_AUTH)
    response.raise_for_status()

    action_plan_id = [action_plan['id'] for action_plan in response.json() if
                      f'{survey_name} B {period}' in action_plan['name']][0]
    logger.debug('Creating action rule', survey_name=survey_name, period=period)
    url = f'{Config.ACTION_SERVICE}/actionrules'
    json = {
        'actionPlanId': action_plan_id,
        'actionTypeName': 'BSNOT',
        'name': 'BSNOT+0',
        'description': 'Business Pre-notification (+0 days)',
        'daysOffset': 0,
        'priority': 3
    }
    response = requests.post(url, auth=Config.BASIC_AUTH, json=json)
    response.raise_for_status()
    logger.debug('Successfully created action rule', survey_name=survey_name, period=period)
