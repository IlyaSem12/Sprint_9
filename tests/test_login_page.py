import allure
import pytest
from conftest import *
from config import *
from locators.login_page_locators import *

@allure.epic("Cтраница авторизации пользователя")
@allure.tag('login page')
@pytest.mark.gui
class TestLoginPage:
    
    @allure.title('Проверка кнопки "Войти"')
    def test_login_page_success_click_signin_button_redirect_login_page(self,login_page):
        '''Тест проверяет корректность работы кнопки "Войти", редирект на страницу авторизации пользователя.'''
        page = login_page
        page.open(RECIPES_URL)
        page.click_button_signin()
        with allure.step(f"Проверяем редирект на '{LOGIN_URL}'"):
            assert page.get_current_url() == LOGIN_URL , f'Страница "{LOGIN_URL}" не открылась'

    @allure.title('Проверка авторизации пользователя')
    def test_login_page_success_signin_user_redirect_recipes_page(self,login_page,registration_user):
        '''Тест проверяет корректность работы страницы "Войти на сайт", пользователь был автаризован.'''
        page = login_page
        page.click_button_signin()
        with allure.step(f"Авторизовываем пользователя"):
            page.fill_login_form(registration_user)
        with allure.step(f"Проверяем редирект на '{RECIPES_URL}'"):
            assert page.is_load(RECIPES_URL) , f'Страница "{RECIPES_URL}" не открылась'
            assert page.is_visible(LOGOUT), f'Кнопка выхода не появилась'