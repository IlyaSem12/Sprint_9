import allure
import requests
from requests import Session
from config import *


class ApiClient:
    
    def __init__(self,*, headers:dict = None, verify: bool = True) :
        self.base_url = BASE_URL_API.rstrip("/")
        self.verify = verify
        self.session: Session = requests.Session()
        if headers is None:
            headers = {
                "Accept": "*/*",
                "Content-Type": "application/json",
            }
        self.session.headers = headers

    def url(self, path: str) -> str:
        """Метод формирования полного url"""
        return f"{self.base_url}/{path.lstrip('/')}"

    def post(self, path: str, **kwargs):
        """Метод для POST-запроса"""
        with allure.step(f"Отправляем POST-запрос на '{path}'"):
            return self.session.post(self.url(path), **kwargs)

    def close(self):
        self.session.close()