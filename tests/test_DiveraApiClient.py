import unittest
from Divera import DiveraApiClient

class test_DiveraApiClient(unittest.TestCase):

    def test_get_accesskey_input_false_returns_empty_dict(self):
        dut = DiveraApiClient()
        expected = { }

        actual = dut._get_accesskey(False)

        self.assertEqual(actual, expected)

    def test_get_accesskey_input_true_returns_access_key(self):
        access_key = "TestKey"
        dut = DiveraApiClient(access_key=access_key)
        expected = { "accesskey": access_key }

        actual = dut._get_accesskey(True)

        self.assertEqual(actual, expected)

