import random
from pages.base_page import BasePage

class RegistrationPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.first_name_input = "#registerUserName"
        self.last_name_input = "#registerUserSurname"
        self.phone_number_input = "#registerUserPhone"
        self.email_input = "#registerUserEmail"
        self.password_input = "#registerUserPassword"
        self.submit_button = "button.auth-modal__submit"
        self.success_registration_popup = "form.auth-modal__form"

    def fill_all_inputs_and_submit(self):
        self.page.fill(self.first_name_input, "Шщшкоушк")
        self.page.fill(self.last_name_input, "Нруоіароуаи")
        self.page.fill(self.phone_number_input, ("0668893762"))
        self.page.fill(self.email_input, "iyreu@ureh.com")
        self.page.fill(self.password_input, "123Qweasd")
        self.page.locator(self.submit_button).click()

    def check_success_registration_popup(self):
        return self.page.locator(self.success_registration_popup)



