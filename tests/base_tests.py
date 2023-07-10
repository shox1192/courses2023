import pytest
from playwright.sync_api import sync_playwright

class BaseTest():
    @pytest.fixture(autouse=True)
    def run_before_tests(self):
        with sync_playwright() as p:
            self.generate_page(p)
            yield self.page

    def generate_page(self, page):
        context = page.chromium.launch(channel="chrome", headless=False).new_context()
        self.page = context.new_page()
        return self.page

    def open_page(self, url):
        self.url = url
        self.page.goto(self.url, timeout=300000)
        self.page.wait_for_load_state(state="load", timeout=20000)
