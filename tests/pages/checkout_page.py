from selenium.webdriver.common.by import By

from tests.pages.base_page import BasePage


class CheckoutPage(BasePage):
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    ERROR_MESSAGE = (By.CSS_SELECTOR, '[data-test="error"]')
    FINISH_BUTTON = (By.ID, "finish")
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")

    def enter_customer_details(
        self, first_name: str, last_name: str, postal_code: str
    ) -> None:
        if first_name:
            self.type_text(self.FIRST_NAME, first_name)
        if last_name:
            self.type_text(self.LAST_NAME, last_name)
        if postal_code:
            self.type_text(self.POSTAL_CODE, postal_code)

    def continue_checkout(self) -> None:
        self.click(self.CONTINUE_BUTTON)

    def error_message(self) -> str:
        return self.text(self.ERROR_MESSAGE)

    def finish_order(self) -> str:
        self.click(self.FINISH_BUTTON)
        return self.text(self.COMPLETE_HEADER)
