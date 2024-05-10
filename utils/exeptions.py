class ElementNotFoundError(Exception):
    def __init__(self, locator, timeout):
        text = f'---- Элемент {locator} не стал видимым за {timeout} секунд'
        super().__init__(text)
