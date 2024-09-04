from data import Urls, OrderData
import requests
import pytest
import allure


class TestCreateOrder:
    @allure.title('Создание заказа с разными цветами самоката')
    @pytest.mark.parametrize('color', OrderData.color)
    def test_create_orders_true(self, color):
        data = OrderData.order_data
        data['color'] = color
        response = requests.post(f'{Urls.BASE_URL}{Urls.ORDERS}', json=data)
        assert response.status_code == 201 and 'track' in response.json()
