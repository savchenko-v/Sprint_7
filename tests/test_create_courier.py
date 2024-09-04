from helpers import TestDataHelper
from data import Urls
import requests
import pytest
import allure


class TestCreateCourier:

    @allure.title('Успешное создание курьера')
    def test_create_courier_success(self):
        data = TestDataHelper.create_courier()
        response = requests.post(f'{Urls.BASE_URL}{Urls.COURIER}', json=data)
        assert response.status_code == 201 and response.json() == {'ok': True}

    @allure.title('Нельзя создать двух одинаковых курьеров')
    def test_create_same_courier_error(self):
        data = TestDataHelper.create_courier()
        requests.post(f'{Urls.BASE_URL}{Urls.COURIER}', json=data)
        response = requests.post(f'{Urls.BASE_URL}{Urls.COURIER}', json=data)
        assert response.status_code == 409 and response.json()["message"] == ("Этот логин уже используется. "
                                                                              "Попробуйте другой.")
        # Баг в документации. Написано, что возвращается другой текст: "message": "Этот логин уже используется"

    @allure.title('Создание курьера с незаполненным полем логина или пароля')
    @pytest.mark.parametrize('delete_field', ['login', 'password'])
    def test_create_courier_without_required_field_error(self, delete_field):
        data = TestDataHelper.create_courier()
        del data[delete_field]  # удаляем поле из словаря
        response = requests.post(f'{Urls.BASE_URL}{Urls.COURIER}', json=data)
        assert response.status_code == 400 and response.json()["message"] == ("Недостаточно данных для создания"
                                                                              " учетной записи")
