import unittest
import json
from datetime import date, datetime
from Divera import News
from Divera import Answer
from Divera import DiveraMessageConverter

class test_DiveraMessageConverter(unittest.TestCase):

    def test_divera_news_response_to_news(self):
        input = '{"items":{"additionalProp1":{"id":123,"foreign_id":"2019-1023","author_id":123456789,"date":0,"title":"Neue Dienstanweisung","text":"Rückwärtsfahren nur mit Einweiser","address":"Raum 1.23","cluster":[0],"group":[0],"user_cluster_relation":[0],"private_mode":true,"notification_type":0,"send_push":true,"send_sms":true,"send_call":true,"send_mail":true,"send_pager":true,"survey":true,"surveys":[{"id":0,"title":"Mit wie vielen Personen nehmt ihr am Sommerfest teil?","show_result_count":0,"show_result_names":0,"access_count":true,"access_names":true,"multiple_answers":true,"custom_answers":true,"response_until":true,"ts_response":0,"answers":{},"answerSorting":["string",0]}],"new":true,"editable":true,"answerable":true,"hidden":true,"deleted":true,"ucr_adressed":[0],"ucr_answered":[0],"ucr_self_addressed":true,"count_recipients":0,"count_read":0,"ts_publish":0,"archive":true,"ts_archive":0,"ts_create":0,"ts_update":0},"additionalProp2":{"id":123,"foreign_id":"2019-1023","author_id":123456789,"date":0,"title":"2095/06/03 Neue Dienstanweisung","text":"Rückwärtsfahren nur mit Einweiser","address":"Raum 1.23","cluster":[0],"group":[0],"user_cluster_relation":[0],"private_mode":true,"notification_type":0,"send_push":true,"send_sms":true,"send_call":true,"send_mail":true,"send_pager":true,"survey":true,"surveys":[{"id":0,"title":"Mit wie vielen Personen nehmt ihr am Sommerfest teil?","show_result_count":0,"show_result_names":0,"access_count":true,"access_names":true,"multiple_answers":true,"custom_answers":true,"response_until":true,"ts_response":0,"answers":{},"answerSorting":["string",0]}],"new":true,"editable":true,"answerable":true,"hidden":true,"deleted":true,"ucr_adressed":[0],"ucr_answered":[0],"ucr_self_addressed":true,"count_recipients":0,"count_read":0,"ts_publish":0,"archive":true,"ts_archive":0,"ts_create":0,"ts_update":0},"additionalProp3":{"id":123,"foreign_id":"2019-1023","author_id":123456789,"date":0,"title":"2020/07/23 Neue Dienstanweisung","text":"Rückwärtsfahren nur mit Einweiser","address":"Raum 1.23","cluster":[0],"group":[0],"user_cluster_relation":[0],"private_mode":true,"notification_type":0,"send_push":true,"send_sms":true,"send_call":true,"send_mail":true,"send_pager":true,"survey":true,"surveys":[{"id":0,"title":"Mit wie vielen Personen nehmt ihr am Sommerfest teil?","show_result_count":0,"show_result_names":0,"access_count":true,"access_names":true,"multiple_answers":true,"custom_answers":true,"response_until":true,"ts_response":0,"answers":{},"answerSorting":["string",0]}],"new":true,"editable":true,"answerable":true,"hidden":true,"deleted":true,"ucr_adressed":[0],"ucr_answered":[0],"ucr_self_addressed":true,"count_recipients":0,"count_read":0,"ts_publish":0,"archive":true,"ts_archive":0,"ts_create":0,"ts_update":0}},"sorting":[0]}'
        input_json = json.loads(input)
        expected_number_of_news = 3
        expected_first_id = 123
        expected_first_name = "Neue Dienstanweisung"
        expected_first_date = None
        expected_first_recipients = 0
        expected_first_answers = [ ]
        expected_first_number_of_answers = 0
        expected_second_id = 123
        expected_second_name = "Neue Dienstanweisung"
        expected_second_date = date(2095, 6, 3)
        expected_second_recipients = 0
        expected_second_answers = [ ]
        expected_second_number_of_answers = 0
        expected_third_id = 123
        expected_third_name = "Neue Dienstanweisung"
        expected_third_date = date(2020, 7, 23)
        expected_third_recipients = 0
        expected_third_answers = [ ]
        expected_third_number_of_answers = 0

        actual = DiveraMessageConverter().divera_news_response_to_news(input_json)

        self.assertEqual(len(actual), expected_number_of_news)
        actual_first = actual[0]
        self.assertEqual(actual_first.id, expected_first_id)
        self.assertEqual(actual_first.name, expected_first_name)
        self.assertEqual(actual_first.date, expected_first_date)
        self.assertEqual(actual_first.recipients, expected_first_recipients)
        self.assertEqual(actual_first.answers, expected_first_answers)
        self.assertEqual(actual_first.sum_answers, expected_first_number_of_answers)
        actual_second = actual[1]
        self.assertEqual(actual_second.id, expected_second_id)
        self.assertEqual(actual_second.name, expected_second_name)
        self.assertEqual(actual_second.date, expected_second_date)
        self.assertEqual(actual_second.recipients, expected_second_recipients)
        self.assertEqual(actual_second.answers, expected_second_answers)
        self.assertEqual(actual_second.sum_answers, expected_second_number_of_answers)
        actual_third = actual[2]
        self.assertEqual(actual_third.id, expected_third_id)
        self.assertEqual(actual_third.name, expected_third_name)
        self.assertEqual(actual_third.date, expected_third_date)
        self.assertEqual(actual_third.recipients, expected_third_recipients)
        self.assertEqual(actual_third.answers, expected_third_answers)
        self.assertEqual(actual_third.sum_answers, expected_third_number_of_answers)

    def test__divera_answers_to_dict_includes_custom_answer_ignores_custom_answer(self):
        input = '{"id":84004,"title":"Rückmeldung","show_result_count":2,"show_result_names":2,"multiple_answers":true,"custom_answers":true,"answers":{"0":{"id":0,"title":"Freitext","note":"","answeredlist":[],"answeredcount":[],"custom_answers":[{"id":123456,"note":"1 Erwachsener, 2 Kinder, davon 0 Vegetarier","ts":1719848211},{"id":2345678,"note":"2 Erwachsene 2 Kinder wie bringen für die Kinder Würstchen mit","ts":1719848494},{"id":987654,"note":"2 Erwachsene, keine Veggies","ts":1719848514},{"id":1000000,"note":"Gesamt 2 davon 1x Veggi","ts":1719850758},{"id":1000000,"note":"2 Erwachsene, 2 Kinder, 2 davon Vegetarier","ts":1719853383},{"id":100000,"note":"Plus 1 ","ts":1719857088},{"id":1000000,"note":"2 Erwachsene","ts":1720076435},{"id":10000,"note":"2 Personen, 0 Veggy","ts":1720199248}]},"212230":{"id":212230,"title":"Komme","checked":true,"answeredlist":[],"answeredcount":21},"216747":{"id":216747,"title":"Nehme nicht teil","checked":false,"answeredlist":[123456,7654321],"answeredcount":2} },"answerSorting":[111111,222222],"response_until":false,"ts_response":0,"access_count":true,"access_names":true}'
        expected_number_of_answers = 2
        input_json = json.loads(input)

        actual = DiveraMessageConverter()._divera_answers_to_dict(input_json)

        self.assertEqual(len(actual), expected_number_of_answers)

    def test_divera_news_response_to_news_has_custom_answers_ignores_custom_answers(self):
        input = '{"items":{"first":{"id":111111,"author_id":111111,"cluster_id":111111,"message_channel_id":0,"foreign_id":"","title":"2024/07/20 (Sa) Familiensommerfest 16-20 Uhr","text":"Familiensommerfest","archive":false,"date":1704063600,"ts_archive":0,"new":false,"editable":true,"answerable":true,"notification_type":2,"group":[],"cluster":[],"user_cluster_relation":[],"hidden":false,"deleted":false,"message_channel":false,"attachment_count":0,"count_recipients":50,"count_read":40,"survey":true,"ucr_addressed":[],"ucr_read":[],"ucr_self_addressed":true,"private_mode":false,"surveys":[{"id":111111,"title":"Rückmeldung","show_result_count":2,"show_result_names":2,"multiple_answers":true,"custom_answers":true,"answers":{"0":{"id":0,"title":"Freitext","note":"","answeredlist":[],"answeredcount":[],"custom_answers":[{"id":111111,"note":"1 Erwachsener, 2 Kinder, davon 0 Vegetarier","ts":1719848211},{"id":111111,"note":"2 Erwachsene 2 Kinder wie bringen für die Kinder Würstchen mit","ts":1719848494},{"id":111111,"note":"2 Erwachsene, keine Veggies","ts":1719848514},{"id":111111,"note":"Gesamt 2 davon 1x Veggi","ts":1719850758},{"id":111111,"note":"2 Erwachsene, 2 Kinder, 2 davon Vegetarier","ts":1719853383},{"id":111111,"note":"Plus 1 ","ts":1719857088},{"id":111111,"note":"2 Erwachsene","ts":1720076435},{"id":111111,"note":"2 Personen, 0 Veggy","ts":1720199248}]},"111111":{"id":111111,"title":"Komme","checked":true,"answeredlist":[],"answeredcount":21},"222222":{"id":222222,"title":"Nehme nicht teil","checked":false,"answeredlist":[],"answeredcount":12} },"answerSorting":[111111,222222],"response_until":false,"ts_response":0,"access_count":true,"access_names":true}],"ts_publish":1704063600,"ts_create":1702981656,"ts_update":1720349336,"send_mail":false,"send_push":false,"send_sms":false,"send_call":false,"send_pager":false} } }'
        input_json = json.loads(input)
        expected_number_of_news = 1
        expected_first_id = 111111
        expected_first_name = "(Sa) Familiensommerfest 16-20 Uhr"
        expected_first_date = date(2024, 7, 20)
        expected_first_recipients = 50
        expected_first_answers = [ Answer(id= 111111, name='Komme', count=21),  Answer(id=222222, name='Nehme nicht teil', count=12) ]
        expected_first_number_of_answers = 33

        actual = DiveraMessageConverter().divera_news_response_to_news(input_json)
        print(actual)
        self.assertEqual(len(actual), expected_number_of_news)
        actual_first = actual[0]
        self.assertEqual(actual_first.id, expected_first_id)
        self.assertEqual(actual_first.name, expected_first_name)
        self.assertEqual(actual_first.date, expected_first_date)
        self.assertEqual(actual_first.recipients, expected_first_recipients)
        self.assertEqual(actual_first.answers, expected_first_answers)
        self.assertEqual(actual_first.sum_answers, expected_first_number_of_answers)
