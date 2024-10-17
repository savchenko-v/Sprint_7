from data import Urls, Responses
import requests
import allure
from helpers import TestDataHelper


class TestAcceptOrder:
    @allure.title('Принять заказ')  # иногда падает, вероятно баг сервера
    def test_accept_order_success(self, create_courier_for_login):
        courier_id = TestDataHelper.get_courier_id(create_courier_for_login)
        order_id = TestDataHelper.create_order_and_get_id()
        response = requests.put(f'{Urls.BASE_URL}{Urls.ACCEPT_ORDER}{order_id}?courierId={courier_id}')
        assert response.status_code == 200 and response.json() == Responses.OK_TRUE

    @allure.title('Принять заказ без id курьера')
    def test_accept_order_without_courier_id(self):
        order_id = TestDataHelper.create_order_and_get_id()
        courier_id = ''
        response = requests.put(f'{Urls.BASE_URL}{Urls.ACCEPT_ORDER}{order_id}?courierId={courier_id}')
        assert response.status_code == 400 and response.json()["message"] == Responses.ACCEPT_ORDER_WITHOUT_ID

    @allure.title('Принять заказ без id заказа')
    def test_accept_order_without_order_id(self, create_courier_for_login):
        courier_id = TestDataHelper.get_courier_id(create_courier_for_login)
        order_id = ''
        response = requests.put(f'{Urls.BASE_URL}{Urls.ACCEPT_ORDER}{order_id}courierId={courier_id}')
        assert response.status_code == 400 and response.json()["message"] == Responses.ACCEPT_ORDER_WITHOUT_ID

    @allure.title('Принять заказ с неверным id курьера')
    def test_accept_order_invalid_courier_id(self):
        order_id = TestDataHelper.create_order_and_get_id()
        courier_id = '-1'
        response = requests.put(f'{Urls.BASE_URL}{Urls.ACCEPT_ORDER}{order_id}?courierId={courier_id}')
        assert response.status_code == 404 and response.json()["message"] == Responses.ACCEPT_ORDER_INVALID_COURIER_ID

    @allure.title('Принять заказ с неверным id')
    def test_accept_order_invalid_courier_id(self, create_courier_for_login):
        order_id = '-1'
        courier_id = TestDataHelper.get_courier_id(create_courier_for_login)
        response = requests.put(f'{Urls.BASE_URL}{Urls.ACCEPT_ORDER}{order_id}?courierId={courier_id}')
        assert response.status_code == 404 and response.json()["message"] == Responses.ACCEPT_ORDER_INVALID_ID

    @allure.title('Принять заказ, который уже был в работе')
    def test_accept_order_conflict(self, create_courier_for_login):
        order_id = '1'  # методом проб и ошибок выяснила, что этот заказ уже был в работе
        courier_id = TestDataHelper.get_courier_id(create_courier_for_login)
        response = requests.put(f'{Urls.BASE_URL}{Urls.ACCEPT_ORDER}{order_id}?courierId={courier_id}')
        assert response.status_code == 409 and response.json()["message"] == Responses.ACCEPT_ORDER_CONFLICT
