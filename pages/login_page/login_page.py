from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.register_button = "button.auth-modal__register-link"

    def open_registration_form(self):
        self.page.locator(self.register_button).click()