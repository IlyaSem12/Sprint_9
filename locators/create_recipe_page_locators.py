from selenium.webdriver.common.by import By


# ====================== FORM ======================
FORM_CREATE_RECIPE = (By.XPATH, "//form[.//textarea and .//input[@type='file']]")
# ====================== TITLE ======================
TITLE_CREATE_RECIPE = (By.XPATH,"//form[.//textarea and .//input[@type='file']]/preceding-sibling::h1")
# ====================== INPUTS ======================
# Название рецепта (первый input в форме)
RECIPE_NAME = (By.XPATH,".//input[@type='text'][1]")
# Поле ингредиента: первый text input в блоке ингредиентов
INGREDIENT_NAME = (By.XPATH,"(//form[.//textarea and .//input[@type='file']]//input[@type='text'])[2]")
# Количество ингредиента: второй text input в блоке ингредиентов
INGREDIENT_AMOUNT = (By.XPATH,"(//form[.//textarea and .//input[@type='file']]//input[@type='text'])[3]")
COOKING_TIME = (By.XPATH,"(//form[.//textarea and .//input[@type='file']]//input[@type='text'])[last()]")
# ====================== INGREDIENT DROPDOWN ======================
INGREDIENT_OPTION = (By.XPATH,"//div[./div and not(.//input) and not(.//textarea)]/div")
FIRST_INGREDIENT_OPTION = (By.XPATH,"(//input[@type='text'])[2]/ancestor::label/ancestor::div/following-sibling::div[last()]//div")
ADD_INGREDIENT_BUTTON = (By.XPATH, "//form[.//textarea and .//input[@type='file']]""//div[./div[.//input[@type='text']] and ./div[2] and ./div[3]]/div[3]")
# ====================== TEXTAREA ======================
DESCRIPTION = (By.XPATH,".//textarea")
# ====================== FILE INPUT ======================
FILE_INPUT = (By.CSS_SELECTOR,"input[type='file']")
# ====================== BUTTON ======================
SUBMIT_BUTTON = (By.XPATH,"//form[.//textarea and .//input[@type='file']]//button[@disabled or not(@type)]")

