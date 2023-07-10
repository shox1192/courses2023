from pages.base_page import BasePage

class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.login_button = "li.header-actions__item--user"

    def open_login_form(self):
        self.page.locator(self.login_button).click()