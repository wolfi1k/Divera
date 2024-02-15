import json
import requests
from datetime import date, datetime, timedelta

class DiveraApiClient:
    """
    Divera 247 Divera API
    See https://api.divera247.com
    Currently only implements authentification and retrieving of all news
    """
    base_url = "https://app.divera247.com"

    access_key = ""

    def __init__(self, access_key=None):
        self.access_key = access_key

    def _get_accesskey(self, include_auth=True) -> str:
        if include_auth:
            return { "accesskey": self.access_key }
        else:
            return { }

    def _ensure_success(self, response) -> json:
        try:
            response.raise_for_status()
        except requests.RequestException as exception:
            raise ValueError(exception) from exception

        resp_json = response.json()
        if not resp_json["success"]:
            raise ValueError(resp_json["errors"])

        return resp_json["data"]

    def _get(self, url, include_auth=True) -> json:
        access_key = self._get_accesskey()

        response = requests.get(f"{self.base_url}/{url}", params=access_key)

        return self._ensure_success(response)


    def _post(self, url, data, include_auth=True) -> json:
        access_key = self._get_accesskey()

        response = requests.post(f"{self.base_url}/{url}", json=data, params=access_key)

        return self._ensure_success(response)

    def _already_logged_in(self):
        try:
            self.get_all_news()
            return True
        except:
            return False

    def login(self, user: str, password: str) -> None:
        ''' Authenticates the user if not already logged in. '''
        if self._already_logged_in():
            return

        url = "api/v2/auth/login"
        data={
            "Login":
            {
                "username": user,
                "password": password,
                "jwt": False
            }
        }

        result = self._post(url, include_auth=False, data=data)

        user_data = result["user"]
        self.access_key = user_data["access_token"]

    def get_all_news(self) -> json:
        ''' Queries all non-archived news. '''
        url = "api/v2/news"
        result = self._get(url, include_auth=True)
        return result

class DiveraMessageConverter:

    def divera_news_response_to_news(self, diveraNews: dict) -> list:
        result = []
        news = list(diveraNews["items"].values())
        for newsResult in news:
            if not newsResult["survey"]:
                continue
            dateAndTitle = newsResult["title"]
            id = newsResult["id"]
            date = self._answer_title_to_date(dateAndTitle)
            if date is None:
                title = dateAndTitle
            else:
                title = self._split_date_and_title(dateAndTitle)[1]
            answers = self._divera_answers_to_dict(newsResult["surveys"][0])
            current = News(id, title, date, answers)
            result.append(current)
        return result

    def _divera_answers_to_dict(self, diveraAnswers: dict) -> dict:
        result = { }
        answers = list(diveraAnswers["answers"].values())

        for answer in answers:
            title = answer["title"]
            count = answer["answeredcount"]
            result[title] = count

        return result

    def _answer_title_to_date(self, title: str) -> date:
        possibleDate = self._split_date_and_title(title)[0]
        date_format = "%Y/%m/%d"

        try:
            return datetime.strptime(possibleDate, date_format).date()
        except:
            return None

    def _split_date_and_title(self, title: str) -> tuple:
        return (title[:10], title[11:])


class News:
    id = -1
    name = ""
    date = None
    answers = { }
    sum_answers = 0

    def __init__(self, id: int, name: str, date: date, answers: dict):
        self.id = id
        self.name = name
        self.date = date
        self.answers = answers
        self.sum_answers = self._get_sum(answers)

    def _get_sum(self, answers: dict) -> int:
        answerCounts = list(answers.values())
        return sum(answerCounts)

    def is_tomorrow(self) -> bool:
        return self.date == (datetime.now()+timedelta(1)).date()

    def format(self) -> str:
        message = "Nächster Dienst: " + self.name

        if self.date is not None:
            message = message + " am " + str(self.date.strftime("%d.%m.%Y"))

        message = message + ".\r\n" + "Bisher " + str(self.sum_answers) + " Rückmeldungen:\r\n"


        for answer_key in self.answers:
            message = message + answer_key + ": " + str(self.answers[answer_key]) + "\r\n"

        return message
