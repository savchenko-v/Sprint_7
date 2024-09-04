from data import Urls, Responses
from helpers import TestDataHelper
import requests
import allure


class TestDeleteCourier:
    @allure.title("Успешное удаление курьера")
    def test_delete_courier_success(self, create_courier_for_login):
        courier_id = TestDataHelper.get_courier_id(create_courier_for_login)
        response = requests.delete(f'{Urls.BASE_URL}{Urls.COURIER}/{courier_id}')

        assert response.status_code == 200 and response.json() == Responses.OK_TRUE

    @allure.title("Удаление курьера без id")
    def test_delete_courier_without_id_error(self):
        courier_id = ""
        response = requests.delete(f'{Urls.BASE_URL}{Urls.COURIER}/{courier_id}')

        assert response.status_code == 404 and response.json()["message"] == Responses.DELETE_COURIER_WITHOUT_ID
        # Баг документации. Возвращается 404 : Not Found. Вместо 400 : "Недостаточно данных для удаления курьера"

    @allure.title("Удаление курьера с несуществующим id")
    def test_delete_courier_invalid_id_error(self):
        courier_id = 1
        response = requests.delete(f'{Urls.BASE_URL}{Urls.COURIER}/{courier_id}')

        assert response.status_code == 404 and response.json()["message"] == Responses.DELETE_COURIER_INVALID_ID
