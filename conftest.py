import pytest
import allure
from config import *
from selenium import webdriver 
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from pages.recipe_page import RecipePage
from pages.create_recipe_page import CreateRecipePage
from utils.webdriver_factory import BrowserFactory
from locators.login_page_locators import *
from locators.common_locators import *
from locators.recipe_page_locators import *
from utils.api_client import ApiClient
from helpers import *


@pytest.fixture
def browser():
    '''Фикструа для получения инстанса драйвера'''
    with allure.step("Окрываем браузер"):
        driver = BrowserFactory.get_driver()
    yield driver
    with allure.step("Закрываем браузер"):
        driver.quit()

@pytest.fixture
def api():
    """Фикстура для создания объекта класса ApiClient"""
    with allure.step('Открываем сессию api'):
        client = ApiClient()
    yield client
    with allure.step('Закрываем сессию api'):
        client.close()

@pytest.fixture
def registration_user(api):
    """Фикстура предварительной регистрации пользователя"""
    user = registration_new_user_and_return_user_data(api)
    return user

@pytest.fixture
def login_user(api, registration_user):
    """Фикстура предварительной авторизации пользователя"""
    token = login_user_and_return_auth_token(api, registration_user)
    return token

@pytest.fixture()
def authorized_browser(browser, login_user):
    """Фикстура для добавления токена авторизации в local storage """
    browser.get(BASE_URL)
    browser.execute_script(
        """window.localStorage.setItem('token', arguments[0]);""",
        login_user,
    )

@pytest.fixture()
def login_page(browser):
    """Фикстура для создания объекта класса страницы заказа"""
    page = LoginPage(browser)#Создаем объект класса LoginPage
    page.open(BASE_URL) #переходим по ссылке
    return page

@pytest.fixture()
def registration_page(browser):
    """Фикстура для создания объекта класса страницы заказа"""
    #Создаем объект класса RegistrationPage
    page = RegistrationPage(browser)
    page.open(BASE_URL)#переходим по ссылке
    return page

@pytest.fixture()
def recipe_page(browser, authorized_browser):
    """Фикстура для создания объекта класса страницы заказа"""
    page = RecipePage(browser)#Создаем объект класса RecipePage
    page.open(BASE_URL) #переходим по ссылке
    page.wait_for_load_recipe_page()#добавляем явное ожиданяие для прогрузки страницы
    return page

@pytest.fixture()
def create_recipe_page(browser):
    """Фикстура для создания объекта класса страницы заказа"""
    page = CreateRecipePage(browser)#Создаем объект класса RecipePage
    return page