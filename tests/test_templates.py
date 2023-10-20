import unittest
from src.templates import *
from .resources.testing_data import Data


class TestTemplates(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.data = Data()

    def test_base_report(self):
        with open(self.data.base_report, 'r') as file:
            test_report = file.read()
        output = Output(self.data.output_risk_3, self.data.insights_risk_3)
        report = base_report(output, 'user', 'https://github.com/commit_url', '659620')
        self.assertEqual(test_report, report)

    def test_risk_table_report(self):
        with open(self.data.risk_table_report, 'r') as file:
            test_report = file.read()
        output = Output(self.data.output_risk_3, self.data.insights_risk_3)
        report = risk_table_report(output)
        self.assertEqual(test_report, report)

    def test_check_output(self):
        title = 'title'
        summary = 'summary'
        text = 'text'
        test_output = {
            "title": title,
            "summary": summary,
            "text": text
        }

        output = check_output(title, summary, text)
        self.assertDictEqual(test_output, output)
