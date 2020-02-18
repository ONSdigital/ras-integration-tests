#!/usr/bin/env bash
set -e

echo "Setting up initial data required for acceptance tests"

collection_exercise_host=${COLLECTION_EXERCISE_SERVICE_HOST:-localhost}
collection_exercise_port=${COLLECTION_EXERCISE_SERVICE_PORT:-8145}
collection_exercise_user=${SECURITY_USER_NAME:-admin}
collection_exercise_password=${SECURITY_USER_PASSWORD:-secret}
pushd collex-loader

pipenv run python load.py config/collex-config.json --posturl=http://${collection_exercise_host}:${collection_exercise_port}/collectionexercises \
    --user=${collection_exercise_user} --password ${collection_exercise_password}

pipenv run python load_events.py config/event-config.json \
    --posturl=http://${collection_exercise_host}:${collection_exercise_port}/collectionexercises/{id}/events \
    --geturl=http://${collection_exercise_host}:${collection_exercise_port}/collectionexercises/{exercise_ref}/survey/{survey_ref} \
    --user=${collection_exercise_user} --password ${collection_exercise_password}
popd
pipenv run python set_up_ce_execution.py
echo "Acceptance tests can now be run"
