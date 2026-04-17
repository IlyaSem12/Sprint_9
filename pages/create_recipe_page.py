#./pages/create_recipe_page.py
import allure
from locators.create_recipe_page_locators import *
from locators.common_locators import *
from pages.base_page import BasePage
from config import *
from helpers import *


class CreateRecipePage(BasePage):
    
    @allure.step('Ожидаем загрузку страницы по появлению заголовка "Рецепты"')
    def wait_for_load_crete_recipe_page(self):
        self.wait_visible(TITLE_CREATE_RECIPE , 5)
    
    @allure.step('Нажимаем кнопку "Создать рецепт')
    def click_button_create_recipe(self):
        self.click(SUBMIT_BUTTON)
    
    @allure.step('Нажимаем кнопку "Добавить ингредиент')
    def click_button_add_ingredient(self):
        self.click(ADD_INGREDIENT_BUTTON)
    
    @allure.step('Зполняем поле "Название рецепта"')
    def send_name_recipe_field(self, name:str):
        self.send_text(RECIPE_NAME, name) 
    
    @allure.step('Зполняем поле с колличеством ингридиентов')
    def send_ingredient_amount_field(self, amount:str):
        self.send_text(INGREDIENT_AMOUNT, amount)
    
    @allure.step('Зполняем поле "Время приготовления"')
    def send_cooking_time_field(self, time:str):
        self.send_text(COOKING_TIME , time)
    
    @allure.step('Зполняем поле "Описание рецепта"')
    def send_description_field(self,text:str):
        self.send_text(DESCRIPTION, text)
    
    @allure.step('Загружаем фото рецепта')
    def upload_recipe_image(self, file_path: str):
        element = self.wait_presence(FILE_INPUT, 10)
        element.send_keys(file_path)

    @allure.step('Вводим ингредиент и выбираем его из списка')
    def select_ingredient_from_dropdown(self, ingredient_name: str):
        self.send_text(INGREDIENT_NAME, ingredient_name)
        self.wait_text_not_empty(FIRST_INGREDIENT_OPTION, 10)
        self.click(FIRST_INGREDIENT_OPTION)

    @allure.step('Заполняем форму создания рецепта')
    def fill_create_recipe_form(self, recipe_data: dict):
        self.send_name_recipe_field(recipe_data['name_recipe'])
        self.select_ingredient_from_dropdown(recipe_data['ingredient'])
        self.send_ingredient_amount_field(recipe_data['ingredient_amount'])
        self.click_button_add_ingredient()
        self.send_cooking_time_field(recipe_data['cooking_time'])
        self.send_description_field(recipe_data['description'])
        self.upload_recipe_image(recipe_data['image_path'])
        self.click_button_create_recipe()
