from faker import Faker
from data import Urls, OrderData
import requests


class TestDataHelper:
    @staticmethod
    def create_courier():
        fake = Faker()
        login = fake.name()
        password = fake.first_name()
        first_name = fake.first_name()

        # собираем тело запроса
        data = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        return data

    @staticmethod
    def get_courier_id(create_courier_for_login):
        data = create_courier_for_login
        response = requests.post(f'{Urls.BASE_URL}{Urls.LOGIN_COURIER}', json=data)
        courier_id = response.json()["id"]
        return courier_id


    @staticmethod
    def create_order_and_get_id():
        data = OrderData.order_data
        data['color'] = ["GREY"]
        response = requests.post(f'{Urls.BASE_URL}{Urls.ORDERS}', json=data)
        order_id = response.json()['track']
        return order_id
