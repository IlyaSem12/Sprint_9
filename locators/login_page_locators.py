from selenium.webdriver.common.by import By

# ====================== FORM ======================
LOGIN_FORM = (By.XPATH,"//form[.//input[@name='email'] and .//input[@name='password']]")
# ====================== TITLE ======================
LOGIN_TITLE = (By.XPATH,"//form[.//input[@name='email'] and .//input[@name='password']]/preceding-sibling::h1")
# ====================== INPUTS ======================
LOGIN_EMAIL = (By.NAME, "email")
LOGIN_PASSWORD = (By.NAME, "password")
# ====================== BUTTON ======================
SUBMIT_BUTTON = (By.CSS_SELECTOR, "button")
SUBMIT_BUTTON_DISABLED = (By.CSS_SELECTOR, "button[disabled]")
SUBMIT_BUTTON_ENABLED = (By.CSS_SELECTOR, "button:not([disabled])")