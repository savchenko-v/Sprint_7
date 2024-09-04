from data import Urls
import requests
import allure


class TestOrdersList:
    @allure.title('Получение списка заказов')
    def test_get_orders_list_success(self):
        response = requests.get(f'{Urls.BASE_URL}{Urls.ORDERS}')
        assert response.status_code == 200 and 'orders' in response.json()
