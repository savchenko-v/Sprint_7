class Urls:
    BASE_URL = 'https://qa-scooter.praktikum-services.ru/api/v1/'
    COURIER = 'courier'
    LOGIN_COURIER = 'courier/login'
    ORDERS = 'orders'
    ACCEPT_ORDER = 'orders/accept/'
    ORDERS_TRACK = 'orders/track'


class Responses:
    OK_TRUE = {'ok': True}
    CREATE_SAME_COURIER = "Этот логин уже используется. Попробуйте другой."
    CREATE_COURIER_WITHOUT_FIELD = "Недостаточно данных для создания учетной записи"

    LOGIN_COURIER = 'id'
    LOGIN_COURIER_INVALID_FIELD = "Учетная запись не найдена"
    LOGIN_COURIER_EMPTY_FIELD = "Недостаточно данных для входа"
    LOGIN_COURIER_NOT_FOUND = "Учетная запись не найдена"

    CREATE_ORDERS = 'track'
    ORDER_LIST = 'orders'

    DELETE_COURIER_WITHOUT_ID = "Not Found."
    DELETE_COURIER_INVALID_ID = "Курьера с таким id нет."

    ACCEPT_ORDER_WITHOUT_ID = "Недостаточно данных для поиска"
    ACCEPT_ORDER_INVALID_COURIER_ID = "Курьера с таким id не существует"
    ACCEPT_ORDER_INVALID_ID = "Заказа с таким id не существует"
    ACCEPT_ORDER_CONFLICT = "Этот заказ уже в работе"

    GET_ORDER = 'order'
    GET_ORDER_INVALID_NUMBER = "Заказ не найден"


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
