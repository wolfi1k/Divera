import unittest
from datetime import date, datetime, timedelta
from Divera import News
from Divera import Answer

class test_News(unittest.TestCase):

    def test_init_valid_input_creates_expected(self):
        id = 10
        name = "TestName"
        recipients = 20
        date = datetime.now().date()
        answers = [ Answer(0,  "FirstAnswer", 5), Answer(31, "SecondAnswer", 10) ]
        number_of_answers = 15

        dut = News(id, name, date, recipients, answers)

        self.assertEqual(dut.id, id)
        self.assertEqual(dut.name, name)
        self.assertEqual(dut.date, date)
        self.assertEqual(dut.recipients, recipients)
        self.assertEqual(dut.answers, answers)
        self.assertEqual(dut.sum_answers, number_of_answers)

    def test_format_valid_input_returns_expected(self):
        id = 10
        name = "TestName"
        date = datetime(2024, 2, 15).date()
        recipients = 20
        answers = [ Answer(0,  "FirstAnswer", 5), Answer(31, "SecondAnswer", 10) ]
        number_of_answers = 15
        dut = News(id, name, date, recipients, answers)
        expected = "Nächster Dienst: TestName am 15.02.2024.\r\nBisher 15 von 20 Rückmeldungen:\r\nFirstAnswer: 5\r\nSecondAnswer: 10\r\nBitte meldet euch zurück."

        actual = dut.format()

        self.assertEqual(actual, expected)

    def test_format_date_is_None_returns_expected(self):
        id = 10
        name = "TestName"
        date = None
        recipients = 20
        answers = [ Answer(id=0,  name="FirstAnswer", count=5), Answer(id=31, name="SecondAnswer", count=10) ]
        number_of_answers = 15
        dut = News(id, name, date, recipients, answers)
        expected = "Nächster Dienst: TestName.\r\nBisher 15 von 20 Rückmeldungen:\r\nFirstAnswer: 5\r\nSecondAnswer: 10\r\nBitte meldet euch zurück."

        actual = dut.format()

        self.assertEqual(actual, expected)


    def test_is_tomorrow_date_is_today_returns_false(self):
        today = datetime.now().date()
        dut = News(0, "", today, 0, [])

        actual = dut.is_tomorrow()

        self.assertFalse(actual)

    def test_is_tomorrow_date_is_tomorrow_returns_true(self):
        tomorrow = (datetime.now() + timedelta(1)).date()
        dut = News(0, "", tomorrow, 0, [])

        actual = dut.is_tomorrow()

        self.assertTrue(actual)
