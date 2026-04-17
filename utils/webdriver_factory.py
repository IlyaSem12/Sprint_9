import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class BrowserFactory:
    @staticmethod
    def get_driver(headless: bool = False):
        remote_url = os.getenv("SELENIUM_REMOTE_URL")

        options = Options()
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")

        if headless:
            options.add_argument("--headless=new")

        if remote_url:
            options.set_capability("browserName", "chrome")
            options.set_capability(
                "selenoid:options",
                {
                    "enableVNC": True,
                    "enableVideo": False
                }
            )
            return webdriver.Remote(
                command_executor=remote_url,
                options=options
            )

        return webdriver.Chrome(options=options)