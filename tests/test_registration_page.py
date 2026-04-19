import allure
import pytest
from conftest import *
from config import *
from locators.login_page_locators import *

@allure.epic("Cтраница регистарции пользователя")
@allure.tag('registration page')
@pytest.mark.gui
class TestRegistrationPage:
    
    @allure.title('Проверка кнопки "Создать аккаунт"')
    def test_registration_page_success_click_create_accaunt_button_redirect_registration_page(self,registration_page):
        '''Тест проверяет корректность работы кнопки "Создать аккаунт", редирект на страницу регистрации пользователя.'''
        page = registration_page
        page.click_button_create_accaunt()
        with allure.step(f"Проверяем редирект на '{REGISTRATION_URL}'"):
            assert page.get_current_url() ==  REGISTRATION_URL , f'Страница "{REGISTRATION_URL}" не открылась'

    @allure.title('Проверка кнопки "Создать аккаунт"')
    def test_registration_page_success_create_user_redirect_login_page(self,registration_page):
        '''Тест проверяет корректность работы страницы "Создать аккаунт", пользователь был создан.'''
        page = registration_page
        page.click_button_create_accaunt()
        page.wait_for_load_registration_page()
        with allure.step(f"Регистрируем пользователя"):
            page.fill_registration_form()
        with allure.step(f"Проверяем редирект на '{LOGIN_URL}'"):
            assert page.is_load(LOGIN_URL) , f'Страница "{LOGIN_URL}" не открылась'
            assert page.is_visible(LOGIN_TITLE), f'Заголовок форма регистрации не появилсь'
        
        
