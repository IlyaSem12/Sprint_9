#./pages/base_page.py
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from config import *


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def open(self, url: str):
        '''Метод открытия страницы'''
        self.browser.get(url)
    
    def wait_text_not_empty(self, locator, timeout: int = 10):
        return WebDriverWait(self.browser, timeout).until(
            lambda driver: driver.find_element(*locator).text.strip() != ""
        )
    
    def wait_presence(self, locator, timeout: int = 10):
        """Метод ожидания появления элемента в DOM"""
        return WebDriverWait(self.browser, timeout).until(
            expected_conditions.presence_of_element_located(locator)
        )
    
    def find(self, locator):
        """Метод поиска списка элементов"""
        return self.browser.find_elements(*locator)

    def wait_visible(self, locator, timeout: int = 10):
        '''Метод ожидания появления элемента'''
        return WebDriverWait(self.browser, timeout).until(expected_conditions.visibility_of_element_located(locator))

    def wait_url_to_be(self, url, timeout=10):
        '''Метод ожидает появление ссылки'''
        WebDriverWait(self.browser, timeout).until(expected_conditions.url_to_be(url))
    
    def is_visible(self, locator, timeout=5):
        '''Метод проверяет, что элемент появился'''
        try:
            self.wait_visible(locator, timeout)
            return True
        except TimeoutException:
            return False
    
    def is_load(self, url, timeout=10):
        '''Метод проверяет, что ссылка появилась'''
        try:
            self.wait_url_to_be(url, timeout)
            return True
        except TimeoutException:
            return False
    
    def click(self, locator, timeout: int = 10):
        '''Метод для нажатия по элементу'''
        element = WebDriverWait(self.browser, timeout).until(expected_conditions.element_to_be_clickable(locator))
        try:
            element.click()
        except ElementClickInterceptedException:
            self.browser.execute_script("arguments[0].click();", element)
    
    def get_text(self,locator, timeout: int = 10):
        '''Метод полчения текста элемента '''
        return self.wait_visible(locator, timeout).text.strip()
    
    def send_text(self, locator, text, timeout: int = 10):
        '''Метод вставки текста в поле ввода'''
        self.wait_visible(locator, timeout).send_keys(text)
    
    def get_current_url(self):
        '''Метод для получения текучшего url'''
        return self.browser.current_url
