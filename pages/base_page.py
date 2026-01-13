from playwright.sync_api import Page


class BasePage:
    """
    Базовый класс для всех Page Object.

    Хранит объект Page от Playwright и предоставляет
    общий интерфейс для работы с браузером.
    """

    def __init__(self, page: Page):
        """
        Конструктор базовой страницы.

        Принимает объект Page от Playwright и сохраняет его,
        чтобы дочерние Page Object могли взаимодействовать
        с браузером (клики, ввод текста, навигация и т.д.).

        :param page: Объект Playwright Page, представляющий текущую вкладку браузера
        """
        self.page = page
