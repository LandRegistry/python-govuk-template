#! /usr/bin/env bash

env_dir="$JENKINS_HOME/virtualenv/${JOB_NAME// /_}"

echo "build_number = '${BUILD_NUMBER:0}'" > govuk_template/VERSION.py

#create and activate a virtualenv
virtualenv $env_dir
. $env_dir/bin/activate

HOME=$JENKINS_HOME python setup.py sdist upload -r pypi
