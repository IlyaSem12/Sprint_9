from selenium.webdriver.common.by import By

# ====================== PAGE ======================
# Форма регистрации (единственная на странице)
REGISTER_FORM = (By.CSS_SELECTOR, "form")
# Заголовок
REGISTER_TITLE = (By.XPATH, "//form[.//input[@name='email'] and .//input[@name='password']]/preceding-sibling::h1")
# ====================== INPUTS INSIDE REGISTER FORM ======================
INPUT_FIRST_NAME = (By.NAME, "first_name")
INPUT_LAST_NAME = (By.NAME, "last_name")
INPUT_USERNAME = (By.NAME, "username")
INPUT_EMAIL = (By.NAME, "email")
INPUT_PASSWORD = (By.NAME, "password")
# ====================== BUTTON INSIDE REGISTER FORM ======================
REGISTER_BUTTON_CSS = (By.CSS_SELECTOR, "button[type='submit'], button")
REGISTER_BUTTON_DISABLED = (By.CSS_SELECTOR, "button[disabled]")
REGISTER_BUTTON_ENABLED = (By.CSS_SELECTOR, "button:not([disabled])")