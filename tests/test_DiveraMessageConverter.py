import unittest
import json
from datetime import date, datetime
from Divera import News
from Divera import DiveraMessageConverter

class test_DiveraMessageConverter(unittest.TestCase):

    def test_divera_news_response_to_news(self):
        input = '{"items":{"additionalProp1":{"id":123,"foreign_id":"2019-1023","author_id":123456789,"date":0,"title":"Neue Dienstanweisung","text":"Rückwärtsfahren nur mit Einweiser","address":"Raum 1.23","cluster":[0],"group":[0],"user_cluster_relation":[0],"private_mode":true,"notification_type":0,"send_push":true,"send_sms":true,"send_call":true,"send_mail":true,"send_pager":true,"survey":true,"surveys":[{"id":0,"title":"Mit wie vielen Personen nehmt ihr am Sommerfest teil?","show_result_count":0,"show_result_names":0,"access_count":true,"access_names":true,"multiple_answers":true,"custom_answers":true,"response_until":true,"ts_response":0,"answers":{},"answerSorting":["string",0]}],"new":true,"editable":true,"answerable":true,"hidden":true,"deleted":true,"ucr_adressed":[0],"ucr_answered":[0],"ucr_self_addressed":true,"count_recipients":0,"count_read":0,"ts_publish":0,"archive":true,"ts_archive":0,"ts_create":0,"ts_update":0},"additionalProp2":{"id":123,"foreign_id":"2019-1023","author_id":123456789,"date":0,"title":"2095/06/03 Neue Dienstanweisung","text":"Rückwärtsfahren nur mit Einweiser","address":"Raum 1.23","cluster":[0],"group":[0],"user_cluster_relation":[0],"private_mode":true,"notification_type":0,"send_push":true,"send_sms":true,"send_call":true,"send_mail":true,"send_pager":true,"survey":true,"surveys":[{"id":0,"title":"Mit wie vielen Personen nehmt ihr am Sommerfest teil?","show_result_count":0,"show_result_names":0,"access_count":true,"access_names":true,"multiple_answers":true,"custom_answers":true,"response_until":true,"ts_response":0,"answers":{},"answerSorting":["string",0]}],"new":true,"editable":true,"answerable":true,"hidden":true,"deleted":true,"ucr_adressed":[0],"ucr_answered":[0],"ucr_self_addressed":true,"count_recipients":0,"count_read":0,"ts_publish":0,"archive":true,"ts_archive":0,"ts_create":0,"ts_update":0},"additionalProp3":{"id":123,"foreign_id":"2019-1023","author_id":123456789,"date":0,"title":"2020/07/23 Neue Dienstanweisung","text":"Rückwärtsfahren nur mit Einweiser","address":"Raum 1.23","cluster":[0],"group":[0],"user_cluster_relation":[0],"private_mode":true,"notification_type":0,"send_push":true,"send_sms":true,"send_call":true,"send_mail":true,"send_pager":true,"survey":true,"surveys":[{"id":0,"title":"Mit wie vielen Personen nehmt ihr am Sommerfest teil?","show_result_count":0,"show_result_names":0,"access_count":true,"access_names":true,"multiple_answers":true,"custom_answers":true,"response_until":true,"ts_response":0,"answers":{},"answerSorting":["string",0]}],"new":true,"editable":true,"answerable":true,"hidden":true,"deleted":true,"ucr_adressed":[0],"ucr_answered":[0],"ucr_self_addressed":true,"count_recipients":0,"count_read":0,"ts_publish":0,"archive":true,"ts_archive":0,"ts_create":0,"ts_update":0}},"sorting":[0]}'
        input_json = json.loads(input)
        expected_number_of_news = 3
        expected_first_id = 123
        expected_first_name = "Neue Dienstanweisung"
        expected_first_date = None
        expected_first_answers = { }
        expected_first_number_of_answers = 0
        expected_second_id = 123
        expected_second_name = "Neue Dienstanweisung"
        expected_second_date = date(2095, 6, 3)
        expected_second_answers = { }
        expected_second_number_of_answers = 0
        expected_third_id = 123
        expected_third_name = "Neue Dienstanweisung"
        expected_third_date = date(2020, 7, 23)
        expected_third_answers = { }
        expected_third_number_of_answers = 0

        actual = DiveraMessageConverter().divera_news_response_to_news(input_json)

        self.assertEqual(len(actual), expected_number_of_news)
        actual_first = actual[0]
        self.assertEqual(actual_first.id, expected_first_id)
        self.assertEqual(actual_first.name, expected_first_name)
        self.assertEqual(actual_first.date, expected_first_date)
        self.assertEqual(actual_first.answers, expected_first_answers)
        self.assertEqual(actual_first.sum_answers, expected_first_number_of_answers)
        actual_second = actual[1]
        self.assertEqual(actual_second.id, expected_second_id)
        self.assertEqual(actual_second.name, expected_second_name)
        self.assertEqual(actual_second.date, expected_second_date)
        self.assertEqual(actual_second.answers, expected_second_answers)
        self.assertEqual(actual_second.sum_answers, expected_second_number_of_answers)
        actual_third = actual[2]
        self.assertEqual(actual_third.id, expected_third_id)
        self.assertEqual(actual_third.name, expected_third_name)
        self.assertEqual(actual_third.date, expected_third_date)
        self.assertEqual(actual_third.answers, expected_third_answers)
        self.assertEqual(actual_third.sum_answers, expected_third_number_of_answers)
