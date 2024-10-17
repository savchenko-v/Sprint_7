from data import Urls, Responses
import requests
import allure
from helpers import TestDataHelper


class TestGetOrderByNumber:

    @allure.title('Получить заказ по его номеру')
    def test_get_order_by_number(self):
        order_id = TestDataHelper.create_order_and_get_id()
        response = requests.get(f'{Urls.BASE_URL}{Urls.ORDERS_TRACK}?t={order_id}')
        assert response.status_code == 200 and Responses.GET_ORDER in response.json()

    @allure.title('Получить заказ без номера')
    def test_get_order_without_number(self):
        response = requests.get(f'{Urls.BASE_URL}{Urls.ORDERS_TRACK}')
        assert response.status_code == 400 and response.json()["message"] == Responses.ACCEPT_ORDER_WITHOUT_ID

    @allure.title('Получить заказ с несуществующим номером')
    def test_get_order_invalid_number(self):
        response = requests.get(f'{Urls.BASE_URL}{Urls.ORDERS_TRACK}?t=0')
        assert response.status_code == 404 and response.json()["message"] == Responses.GET_ORDER_INVALID_NUMBER
