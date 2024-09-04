import requests
from data import Urls
from helpers import TestDataHelper
import pytest


@pytest.fixture(scope='function')
def create_courier_for_login():
    data = TestDataHelper.create_courier()
    del data['firstName']
    requests.post(f'{Urls.BASE_URL}{Urls.COURIER}', json=data)

    return data
