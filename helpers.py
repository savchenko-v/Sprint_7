from faker import Faker


class TestDataHelper:
    @staticmethod
    def create_courier():
        fake = Faker()
        login = fake.name()
        password = fake.first_name()
        first_name = fake.first_name()

        # собираем тело запроса
        data = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        return data
