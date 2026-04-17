import allure
from locators.registration_page_locators import *
from locators.common_locators import *
from pages.base_page import BasePage
from helpers import *
from config import *

class RegistrationPage(BasePage):
    
    @allure.step('Ожидаем загрузку страницы по появлению заголовка "Регистрация"')
    def wait_for_load_registration_page(self):
        self.wait_visible(REGISTER_TITLE, 5)
    
    @allure.step('Нажимаем на кнопку "Создать аккаунт"')
    def click_button_create_accaunt(self):
        self.click(HEADER_SIGNUP_LINK)

    @allure.step('Нажимаем на кнопку регистрации пользователя')
    def click_button_registration(self):
        self.click(REGISTER_BUTTON_CSS)

    @allure.step('Зполняем поле "Имя"')
    def send_firstname_field(self):
        self.send_text(INPUT_FIRST_NAME, generate_name())
    
    @allure.step('Зполняем поле "Фамилия"')
    def send_lastname_field(self):
        self.send_text(INPUT_LAST_NAME, generate_lastname())
    
    @allure.step('Зполняем поле "Имя пользователя"')
    def send_login(self):
        self.send_text(INPUT_USERNAME,generate_login())
    
    @allure.step('Зполняем поле "Пароль"')
    def send_password_field(self):
        self.send_text(INPUT_PASSWORD,generate_random_string(8))
    
    @allure.step('Зполняем поле "Адрес электронной почты"')
    def send_email_field(self):
        self.send_text(INPUT_EMAIL,generate_email())

    @allure.step('Зполняем форму регистрации')
    def fill_registration_form(self):
        self.send_firstname_field()
        self.send_lastname_field()
        self.send_login()
        self.send_email_field()
        self.send_password_field()
        self.click_button_registration()

