from selenium.webdriver.common.by import By

# ====================== PAGE ROOT ======================
# Контейнер страницы рецептов:
RECIPE_PAGE = (By.XPATH,"//div[.//a[starts-with(@href, '/recipes/')]]")
# Заголовок страницы
RECIPE_TITLE = (By.XPATH,"//div[.//a[starts-with(@href, '/recipes/')]]//h1")
# ====================== CARDS LIST ======================
# Контейнер списка карточек
CARDS_LIST = (By.XPATH,"//div[./div[.//a[starts-with(@href, '/recipes/')]]]")
FIRST_RECIPE_CARD = (By.XPATH,"(//div[./a[starts-with(@href, '/recipes/')] and .//a[starts-with(@href, '/user/')]])[1]")
# ====================== CARD INNER ELEMENTS ======================
FIRST_RECIPE_CARD_TITLE = (By.XPATH,"((//div[./a[starts-with(@href, '/recipes/')] and .//a[starts-with(@href, '/user/')]])[1]//a[starts-with(@href, '/recipes/')])[2]")
