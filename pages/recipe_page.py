#./pages/recipe_page.py
import allure
from locators.recipe_page_locators import *
from locators.common_locators import *
from pages.base_page import BasePage
from config import *
from helpers import *


class RecipePage(BasePage):
    
    @allure.step('Открываем страницу "Рецепты"')
    def open_recipe_page(self):
        self.open(RECIPES_URL)
    
    @allure.step('Ожидаем загрузку страницы по появлению заголовка "Рецепты"')
    def wait_for_load_recipe_page(self):
        self.wait_visible(RECIPE_TITLE , 5)
    
    @allure.step('Нажимаем кнопку "Создать рецепт')
    def click_create_recipe_link(self):
        self.click(CREATE_RECIPE)
    
    @allure.step('Нажимаем кнопку "Создать рецепт')
    def click_create_recipe_link(self):
        self.click(CREATE_RECIPE)
    
    @allure.step('Проверяем, что карточка рецепта отображается')
    def is_recipe_card_visible(self, recipe_name: str) -> bool:
        locator = (
            By.XPATH,
            f"//a[starts-with(@href, '/recipes/') and normalize-space()='{recipe_name}']"
            f"/ancestor::div[.//a[starts-with(@href, '/user/')]][1]"
        )
        return self.is_visible(locator, 5)
    
    @allure.step('Получаем название рецепта из карточки')
    def get_recipe_title_text(self, recipe_name: str) -> str:
        locator = (
            By.XPATH,
            f"//a[starts-with(@href, '/recipes/') and normalize-space()='{recipe_name}']"
        )
        return self.get_text(locator) 