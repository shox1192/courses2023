class BasePage:
    def __init__(self, page):
        self.page = page

    def get_locator(self, locator):
        return self.page.locator(locator)
        