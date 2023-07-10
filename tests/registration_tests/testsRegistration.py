import pytest
import time
from playwright.sync_api import expect
from tests.base_tests import BaseTest
from pages.login_page.login_page import LoginPage
from pages.refistration_page.registration_page import RegistrationPage
from pages.home_page.home_page import HomePage

class TestRegistration(BaseTest):
    @pytest.fixture(autouse=True)

    def test_registration_success(self):
        self.open_page("https://rozetka.com.ua/ua/")
        HomePage(self.page).open_login_form()
        time.sleep(3)
        LoginPage(self.page).open_registration_form()
        time.sleep(3)
        RegistrationPage(self.page).fill_all_inputs_and_submit()
        time.sleep(3)
        expect(
            RegistrationPage(self.page).check_success_registration_popup()
        ).to_be_visible()
        expect(
            RegistrationPage(self.page).check_success_registration_popup()
        ).to_have_text("Підтвердження номера телефону")