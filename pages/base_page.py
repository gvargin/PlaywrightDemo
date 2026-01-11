from playwright.sync_api import Page


class BasePage:

    def __init__(self, page: Page):
        """
        Constructor, get object Page and store it for Page Objects
        :param page: Playwrigh Page for work with browser
        """

        self.page = page
