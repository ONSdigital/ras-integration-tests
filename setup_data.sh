#!/usr/bin/env bash
set -e

rm_tools_repo_url=$1
echo "Setting up initial data required for acceptance tests"
if [ -d tmp_rm_tools ]; then
    echo "tmp_rm_tools exists - pulling";
    cd tmp_rm_tools; git pull; cd -;
else
    git clone --depth 1 ${rm_tools_repo_url} tmp_rm_tools;
fi;
pushd tmp_rm_tools/collex-loader
pipenv run python load.py config/collex-config.json
pipenv run python load_events.py config/event-config.json
popd
rm -rf tmp_rm_tools
pipenv run python set_up_ce_execution.py
echo "Acceptance tests can now be run"
