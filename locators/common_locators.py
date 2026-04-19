from selenium.webdriver.common.by import By

#======================Локаторы header======================
# Ссылка "Рецепты"
HEADER_RECIPES_LINK = (By.CSS_SELECTOR, "a[href='/recipes']")
# Ссылка "Войти"
HEADER_SIGNIN_LINK = (By.CSS_SELECTOR, "a[href='/signin']")
# Ссылка "Создать аккаунт"
HEADER_SIGNUP_LINK = (By.CSS_SELECTOR, "a[href='/signup']")
# Активная страница (через aria-current)
CHANGE_PASSWORD = (By.CSS_SELECTOR, "a[href='/change-password']")
# "Выход" — без href → только через позицию
LOGOUT = (By.XPATH,"//div[.//a[@href='/change-password']]//a[not(@href)]")
# Основные ссылки
SUBSCRIPTIONS = (By.CSS_SELECTOR, "a[href='/subscriptions']")
CREATE_RECIPE = (By.CSS_SELECTOR, "a[href='/recipes/create']")
# Активная ссылка (текущая страница)
ACTIVE_LINK = (By.CSS_SELECTOR, "a[aria-current='page']")