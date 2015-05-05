#! /usr/bin/env bash

env_dir="$JENKINS_HOME/virtualenv/${JOB_NAME// /_}"

#create and activate a virtualenv
virtualenv $env_dir
. $env_dir/bin/activate

#install requirements
pip install -r requirements.txt

#install the govuk_template files
python run.py

#run tests
python tests.py --xml

test_pass=$?

if $test_pass; then
  HOME=$JENKINS_HOME python setup.py sdist upload -r pypi
fi

exit $test_result
