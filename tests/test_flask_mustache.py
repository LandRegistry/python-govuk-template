import unittest
from flask import Flask
from govuk_template.flask import assets


class TestFlaskMustache(unittest.TestCase):

    def setUp(self):
        self.app = Flask('testCase')
        self.app.register_blueprint(assets.govuk_template)

        self.app.config['TESTING'] = True


    def test_blueprint(self):
        with self.app.test_client() as client:
            res = client.get('/assets/stylesheets/govuk-template.css')

            self.assertEqual(res.status_code, 200)
            self.assertTrue ("text/css" in res.headers['Content-Type'])
