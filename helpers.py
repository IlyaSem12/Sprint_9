import random
import uuid
import string
import allure
import config

# метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
@allure.step('Генерируем рандомную строку')
def generate_random_string(length:str = 10) -> str:
    """Функция для генерации строки"""
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string

@allure.step('Генерируем имя')
def generate_name() -> str:
    """Функция для генерации имени пользователя"""
    return f"firstname_{uuid.uuid4().hex[:8]}"

@allure.step('Генерируем фамилию')
def generate_lastname() -> str:
    """Функция для генерации фамилии пользователя"""
    return f"lastname_{uuid.uuid4().hex[:8]}"

@allure.step('Генерируем логин')
def generate_login() -> str:
    """Функция для генерации логина"""
    return f"test_user_{uuid.uuid4().hex[:8]}"

@allure.step('Генерируем почту')
def generate_email() -> str:
    """Функция для генерации почты"""
    return f"test_{uuid.uuid4().hex[:8]}@email.ru"

@allure.step('Генерируем название рецепта')
def generate_recipe_name() -> str:
    """Функция для генерации имени пользователя"""
    return f"test_{uuid.uuid4().hex[:4]}_recept"

def registration_new_user_and_return_user_data(api) -> dict:
    """Функция для регистрации пользователя"""
    with allure.step(f'Регистрируем пользоваетля'):
        payload = {
            "email":generate_email(),
            "first_name":generate_name(),
            "last_name":generate_lastname(),
            "password":generate_random_string(8),
            "username":generate_login()
        }# собираем тело запроса
        # отправляем запрос на регистрацию пользователя и сохраняем ответ в переменную response
        with allure.step('Отправляем POST запрос для регистрации пользователя'):
            api.post(path = config.REGISTRATION_API_URL, json = payload)
    return payload

def login_user_and_return_auth_token(api, user:dict) -> str:
    """Функция для регистрации пользователя"""
    with allure.step(f'Производим авторизацию'):
        payload = {
            "email":user["username"],
            "password":user["password"],
        }# собираем тело запроса
        # отправляем запрос на регистрацию пользователя и сохраняем ответ в переменную response
        with allure.step('Отправляем POST запрос для авторизации пользователя'):
            response = api.post(path = config.LOGIN_API_URL, json = payload)
            body = response.json()
    return body.get("auth_token")
