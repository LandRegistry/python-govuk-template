import unittest
from flask import Flask
from govuk_template.flask.mustache import GovukTemplate
from lxml.html import document_fromstring


class TestMustacheRendering(unittest.TestCase):

    def setUp(self):
        self.app = Flask('testCase')
        self.app.config['TESTING'] = True

    def test_can_render_template(self):
        with self.app.app_context():
            with self.app.test_request_context():
                text = GovukTemplate().render()
                html = document_fromstring(text)

                header = ''.join(html.xpath('//header//a/text()'))
                self.assertTrue('GOV.UK' in header)
