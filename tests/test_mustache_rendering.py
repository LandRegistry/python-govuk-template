import unittest
from flask import Flask
from govuk_template.flask.mustache import GovukTemplate
from lxml.html import document_fromstring


def with_context(test):
    def wrapped_test(self):
        with self.app.app_context():
            with self.app.test_request_context():
                test(self)
    return wrapped_test


class TestMustacheRendering(unittest.TestCase):

    def setUp(self):
        self.app = Flask('testCase')
        self.app.config['TESTING'] = True

    @with_context
    def test_can_render_template(self):
        text = GovukTemplate().render()
        html = document_fromstring(text)

        header = ''.join(html.xpath('//header//a/text()'))
        self.assertTrue('GOV.UK' in header)

    @with_context
    def test_can_inject_context(self):
        text = GovukTemplate().render(pageTitle="My wicked title")
        html = document_fromstring(text)

        title = html.xpath('//title/text()')
        self.assertEqual(title, ["My wicked title"])

    @with_context
    def test_can_render_from_object(self):
        class MyClass(object):
            bodyClasses = "my-class"

            def __init__(self, title):
                self.pageTitle = title

            def content(self):
                return "<div class='my-div'>My Div</div>"

        myObj = MyClass("My Title")
        text = GovukTemplate().render(myObj)
        html = document_fromstring(text)

        title = html.xpath('//title/text()')
        div = html.xpath('//div[@class="my-div"]/text()')
        bodyClasses = html.xpath('//body/@class')

        self.assertEqual(title, ['My Title'])
        self.assertEqual(div, ['My Div'])
        self.assertEqual(bodyClasses, ['my-class'])
