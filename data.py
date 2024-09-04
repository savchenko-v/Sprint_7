class Urls:
    BASE_URL = 'https://qa-scooter.praktikum-services.ru/api/v1/'
    COURIER = 'courier'
    LOGIN_COURIER = 'courier/login'
    ORDERS = 'orders'


class Responses:
    CREATE_COURIER = {'ok': True}
    CREATE_SAME_COURIER = "Этот логин уже используется. Попробуйте другой."
    CREATE_COURIER_WITHOUT_FIELD = "Недостаточно данных для создания учетной записи"

    LOGIN_COURIER = 'id'
    LOGIN_COURIER_INVALID_FIELD = "Учетная запись не найдена"
    LOGIN_COURIER_EMPTY_FIELD = "Недостаточно данных для входа"
    LOGIN_COURIER_NOT_FOUND = "Учетная запись не найдена"

    CREATE_ORDERS = 'track'
    ORDER_LIST = 'orders'


class OrderData:
    order_data = {
                    "firstName": "Philipp",
                    "lastName": "Kirkorov",
                    "address": "Moscow, Red Square",
                    "metroStation": 4,
                    "phone": "+7 800 555 35 35",
                    "rentTime": 5,
                    "deliveryDate": "2024-09-03",
                    "comment": "Philipp, come back to Russia"
                }
    color = [["BLACK"], ["GREY"], ["BLACK", "GREY"], []]
