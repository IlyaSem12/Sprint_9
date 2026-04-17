import allure
import pytest
from conftest import *
from config import *
from locators.recipe_page_locators import *

@allure.epic("Cтраница создания рецепта")
@allure.tag('create recipe page')
@pytest.mark.gui
class TestCreateRecipePage:
    
    @allure.title('Проверка что авторизованный пользователь может создать рецепт')
    def test_create_recipe_page_authorized_user_can_create_recipe_view_card_recipe(browser,create_recipe_page,
        recipe_page):
        """Проверяем, что после заполнения формы создания рецепта отображается карточка нового рецепта с корректным названием"""
        with allure.step('Переходим на страницу создания рецепта'):
            recipe_page.click_create_recipe_link()
            create_recipe_page.wait_for_load_crete_recipe_page()
        create_recipe_page.fill_create_recipe_form(recipe_data)
        create_recipe_page.click_button_create_recipe()
        with allure.step('Ожидаем открытие страницы рецептов'):
            recipe_page.open_recipe_page()
            recipe_page.wait_for_load_recipe_page()
        with allure.step('Проверяем, что карточка нового рецепта отображается'):
            assert recipe_page.is_recipe_card_visible(recipe_data["name_recipe"]), f"Карточка рецепта '{recipe_data['name_recipe']}' не отображается"
        with allure.step('Проверяем, что название карточки соответствует введённому'):
            actual_title = recipe_page.get_recipe_title_text(recipe_data["name_recipe"])
            assert actual_title == recipe_data["name_recipe"], f"Ожидалось название '{recipe_data['name_recipe']}', получено '{actual_title}'"
        
