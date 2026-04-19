#./pages/main_page.py
import allure
from locators.login_page_locators import *
from locators.common_locators import *
from pages.base_page import BasePage
from config import *


class LoginPage(BasePage):
    
    @allure.step(f"Преходим на страницу авторизации: '{LOGIN_URL}'")
    def open_login_page(self):
        self.open(LOGIN_URL)

    @allure.step('Ожидаем загрузку страницы авторизации по появлению заголовка "Войти на сайт"')
    def wait_for_load_login_page(self):
        self.wait_visible(LOGIN_TITLE, 5)
    
    @allure.step('Нажимаем на кнопку "Войти" на навигациронной панели')
    def click_button_signin(self):
        self.click(HEADER_SIGNIN_LINK)
    
    @allure.step('Нажимаем на кнопку "Войти"')
    def click_button_login(self):
        self.click(SUBMIT_BUTTON)

    @allure.step('Зполняем поле "Пароль"')
    def send_password_field(self, data:str):
        self.send_text(LOGIN_PASSWORD, data)
    
    @allure.step('Зполняем поле "Адрес электронной почты"')
    def send_email_field(self, data:str):
        self.send_text(LOGIN_EMAIL, data)
    
    @allure.step('Зполняем форму авторизации')
    def fill_login_form(self, data:dict):
        self.send_email_field(data['username'])
        self.send_password_field(data["password"])
        self.click_button_login()
