from guara.transaction import AbstractTransaction

from tests.pages.login_page import LoginPage


class LoginTransaction(AbstractTransaction):
    def do(self, url: str, username: str, password: str) -> str:
        self._driver.get(url)
        login_page = LoginPage(self._driver)
        login_page.login(username, password)
        if "inventory.html" in self._driver.current_url:
            return self._driver.current_url
        return login_page.error_message()
