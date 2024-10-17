from helpers import TestDataHelper
from data import Urls, Responses
import requests
import pytest
import allure


class TestLoginCourier:

    @allure.title('Успешная авторизация курьера')
    def test_login_courier_success(self, create_courier_for_login):
        data = create_courier_for_login
        response = requests.post(f'{Urls.BASE_URL}{Urls.LOGIN_COURIER}', json=data)
        assert response.status_code == 200 and Responses.LOGIN_COURIER in response.json()

    @allure.title('Авторизация с неправильно указанным логином или паролем')
    @pytest.mark.parametrize('invalid_field', ['login', 'password'])
    def test_login_invalid_field_error(self, create_courier_for_login, invalid_field):
        data = create_courier_for_login
        data[invalid_field] += 'aaa'
        response = requests.post(f'{Urls.BASE_URL}{Urls.LOGIN_COURIER}', json=data)
        assert response.status_code == 404 and response.json()["message"] == Responses.LOGIN_COURIER_INVALID_FIELD

    @allure.title('Авторизация с пустым логином или паролем')
    @pytest.mark.parametrize('empty_field', ['login', 'password'])
    def test_login_empty_field_error(self, create_courier_for_login, empty_field):
        data = create_courier_for_login
        data[empty_field] = ''
        response = requests.post(f'{Urls.BASE_URL}{Urls.LOGIN_COURIER}', json=data)
        assert response.status_code == 400 and response.json()["message"] == Responses.LOGIN_COURIER_EMPTY_FIELD

    @allure.title('Авторизация под несуществующим пользователем')
    def test_login_courier_not_found_error(self):
        data = TestDataHelper.create_courier()
        response = requests.post(f'{Urls.BASE_URL}{Urls.LOGIN_COURIER}', json=data)
        assert response.status_code == 404 and response.json()["message"] == Responses.LOGIN_COURIER_NOT_FOUND
