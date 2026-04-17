from helpers import generate_recipe_name
import os


#================WEB URLS================
BASE_URL = 'https://foodgram-frontend-1.prakticum-team.ru/'
LOGIN_URL = f'{BASE_URL}signin'
REGISTRATION_URL = f'{BASE_URL}signup'
RECIPES_URL = f'{BASE_URL}recipes'
#================API URLS================
BASE_URL_API = 'https://foodgram-backend-1.prakticum-team.ru/'
REGISTRATION_API_URL = f'api/users/'
LOGIN_API_URL = f'api/auth/token/login/'
#================CONSTANT DATA================
recipe_data = {
    "name_recipe": generate_recipe_name(),
    "ingredient": "тальятелле-гнезда",
    "ingredient_amount": "2",
    "cooking_time": "15",
    "description": "Автотестовый рецепт",
    "image_path": os.path.abspath("./img/test_img_01.jpg"),
}