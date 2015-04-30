#create and activate a virtualenv
virtualenv .env
. .env/bin/activate

#install requirements
pip install -r requirements.txt

#run tests
python tests.py --xml

#deactivate virtualenv
deactivate
