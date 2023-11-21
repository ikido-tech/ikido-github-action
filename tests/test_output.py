import unittest
import json
from src.output import Output
from .resources.testing_data import Data


class TestOutput(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.data = Data()
        with open(self.data.item_1_path, 'r') as item_1, \
                open(self.data.item_2_path, 'r') as item_2, \
                open(self.data.item_3_path, 'r') as item_3:
            self.item_1 = json.load(item_1)
            self.item_2 = json.load(item_2)
            self.item_3 = json.load(item_3)

    def test_output_risk_3(self):
        output_risk_3 = Output(self.data.output_risk_3, self.data.insights_risk_3)
        self.assertEqual(output_risk_3.ok_count, 1)
        self.assertEqual(output_risk_3.ok_count, len(output_risk_3.ok))
        self.assertEqual(output_risk_3.low_count, 0)
        self.assertEqual(output_risk_3.low_count, len(output_risk_3.low))
        self.assertEqual(output_risk_3.medium_count, 0)
        self.assertEqual(output_risk_3.medium_count, len(output_risk_3.medium))
        self.assertEqual(output_risk_3.high_count, 2)
        self.assertEqual(output_risk_3.high_count, len(output_risk_3.high))
        self.assertEqual(output_risk_3.not_found_count, 0)
        self.assertEqual(output_risk_3.not_found_count, len(output_risk_3.not_found))
        self.assertEqual(output_risk_3.total_count, 3)
        self.assertEqual(output_risk_3.workspace_id, '6544ffa2fe01abe328759491')

        self.assertDictEqual(output_risk_3.high[1], self.item_1)
        self.assertDictEqual(output_risk_3.high[0], self.item_2)
        self.assertDictEqual(output_risk_3.ok[0], self.item_3)

    def test_output_risk_2(self):
        output_risk_2 = Output(self.data.output_risk_2, self.data.insights_risk_2)
        self.item_1['risk'] = '2'
        self.item_2['risk'] = '2'
        self.item_3['risk'] = '1'
        self.assertEqual(output_risk_2.ok_count, 0)
        self.assertEqual(output_risk_2.ok_count, len(output_risk_2.ok))
        self.assertEqual(output_risk_2.low_count, 1)
        self.assertEqual(output_risk_2.low_count, len(output_risk_2.low))
        self.assertEqual(output_risk_2.medium_count, 2)
        self.assertEqual(output_risk_2.medium_count, len(output_risk_2.medium))
        self.assertEqual(output_risk_2.high_count, 0)
        self.assertEqual(output_risk_2.high_count, len(output_risk_2.high))
        self.assertEqual(output_risk_2.not_found_count, 0)
        self.assertEqual(output_risk_2.not_found_count, len(output_risk_2.not_found))
        self.assertEqual(output_risk_2.total_count, 3)
        self.assertEqual(output_risk_2.workspace_id, '6544ffa2fe01abe328759491')

        self.assertDictEqual(output_risk_2.medium[1], self.item_1)
        self.assertDictEqual(output_risk_2.medium[0], self.item_2)
        self.assertDictEqual(output_risk_2.low[0], self.item_3)

    def test_output_risk_1(self):
        output_risk_1 = Output(self.data.output_risk_1, self.data.insights_risk_1)
        self.item_1['risk'] = '1'
        self.item_2['risk'] = '1'
        self.item_3['risk'] = '1'
        self.assertEqual(output_risk_1.ok_count, 0)
        self.assertEqual(output_risk_1.ok_count, len(output_risk_1.ok))
        self.assertEqual(output_risk_1.low_count, 3)
        self.assertEqual(output_risk_1.low_count, len(output_risk_1.low))
        self.assertEqual(output_risk_1.medium_count, 0)
        self.assertEqual(output_risk_1.medium_count, len(output_risk_1.medium))
        self.assertEqual(output_risk_1.high_count, 0)
        self.assertEqual(output_risk_1.high_count, len(output_risk_1.high))
        self.assertEqual(output_risk_1.not_found_count, 0)
        self.assertEqual(output_risk_1.not_found_count, len(output_risk_1.not_found))
        self.assertEqual(output_risk_1.total_count, 3)
        self.assertEqual(output_risk_1.workspace_id, '6544ffa2fe01abe328759491')

        self.assertDictEqual(output_risk_1.low[1], self.item_1)
        self.assertDictEqual(output_risk_1.low[0], self.item_2)
        self.assertDictEqual(output_risk_1.low[2], self.item_3)

    def test_output_risk_0(self):
        output_risk_0 = Output(self.data.output_risk_0, self.data.insights_risk_0)
        self.item_1['risk'] = '0'
        self.item_2['risk'] = '0'
        self.item_3['risk'] = '0'
        self.assertEqual(output_risk_0.ok_count, 3)
        self.assertEqual(output_risk_0.ok_count, len(output_risk_0.ok))
        self.assertEqual(output_risk_0.low_count, 0)
        self.assertEqual(output_risk_0.low_count, len(output_risk_0.low))
        self.assertEqual(output_risk_0.medium_count, 0)
        self.assertEqual(output_risk_0.medium_count, len(output_risk_0.medium))
        self.assertEqual(output_risk_0.high_count, 0)
        self.assertEqual(output_risk_0.high_count, len(output_risk_0.high))
        self.assertEqual(output_risk_0.not_found_count, 0)
        self.assertEqual(output_risk_0.not_found_count, len(output_risk_0.not_found))
        self.assertEqual(output_risk_0.total_count, 3)
        self.assertEqual(output_risk_0.workspace_id, '6544ffa2fe01abe328759491')

        self.assertDictEqual(output_risk_0.ok[1], self.item_1)
        self.assertDictEqual(output_risk_0.ok[0], self.item_2)
        self.assertDictEqual(output_risk_0.ok[2], self.item_3)
