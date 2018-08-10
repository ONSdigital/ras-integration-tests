import logging
from datetime import datetime

import requests
import tzlocal
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
    trigger_time = datetime.now(tzlocal.get_localzone()).isoformat()
    json = {
        'actionPlanId': action_plan_id,
        'actionTypeName': 'BSNOT',
        'name': 'BSNOT+0',
        'description': 'Business Pre-notification (+0 days)',
        'triggerDateTime': trigger_time,
        'priority': 3
    }
    url = f'{Config.ACTION_SERVICE}/actionrules'
    response = requests.post(url, auth=Config.BASIC_AUTH, json=json)
    response.raise_for_status()
    logger.debug('Successfully created action rule', survey_name=survey_name, period=period)


def create_social_action_rule(survey_name, period):
    # Get action plan id
    logger.debug('Finding action plan', survey_name=survey_name, period=period)
    url = f'{Config.ACTION_SERVICE}/actionplans'
    response = requests.get(url, auth=Config.BASIC_AUTH)
    response.raise_for_status()

    action_plan_id = [action_plan['id'] for action_plan in response.json() if
                      f'{survey_name} H {period}' in action_plan['name']][0]
    logger.debug('Printing action plan id', action_plan_id=action_plan_id, survey_name=survey_name)

    # Post action rules
    logger.debug('Creating action rule', survey_name=survey_name, period=period)
    trigger_time = datetime.now(tzlocal.get_localzone()).isoformat()
    action_rule_pre_not = {
        'actionPlanId': action_plan_id,
        'actionTypeName': 'SOCIALPRENOT',
        'name': 'OHSSOCIALPRENOT+0',
        'description': 'OHS Social Pre-notification (+0 days)',
        'triggerDateTime': trigger_time,
        'priority': 3
    }

    action_rule_not = {
        'actionPlanId': action_plan_id,
        'actionTypeName': 'SOCIALNOT',
        'name': 'OHSSOCIALNOT +0',
        'description': 'OHS Social Notification (+0 days)',
        'triggerDateTime': trigger_time,
        'priority': 3
    }
    pre_not_response = requests.post(url=f'{Config.ACTION_SERVICE}/actionrules',
                                     json=action_rule_pre_not,
                                     auth=Config.BASIC_AUTH)

    pre_not_response.raise_for_status()
    not_response = requests.post(url=f'{Config.ACTION_SERVICE}/actionrules',
                                 json=action_rule_not,
                                 auth=Config.BASIC_AUTH)

    not_response.raise_for_status()
    logger.debug('Successfully created action rule', survey_name=survey_name, period=period)
