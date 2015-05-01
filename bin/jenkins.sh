#! /usr/bin/env bash

echo "$HOME"
echo "$USER"
echo "$JENKINS_HOME"
echo "$WORKSPACE"

env_dir="$HOME/.virtualenv/${JOB_NAME// /_}"

#create and activate a virtualenv
virtualenv --clear $env_dir
. $env_dir/bin/activate

#install requirements
pip install -r requirements.txt

#run tests
python tests.py --xml

#deactivate virtualenv
deactivate
