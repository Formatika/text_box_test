from time import sleep

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, WebDriverException

from ..utils.exeptions import ElementNotFoundError
from ..utils.logger import gen_logger

logger = gen_logger(__name__)


class BasePage:
    global_timeout = 10
    wait_timeout = 10

    def __init__(self, browser, timeout=10):
        self.browser = browser
        self.browser.implicitly_wait(timeout)
        self.wait = WebDriverWait(self.browser, self.wait_timeout)
        self.long_wait = WebDriverWait(self.browser, self.global_timeout)

    def open(self, url):
        self.url = url
        if self.url:
            logger.info('Открываем ' + self.url)
            try:
                self.browser.get(self.url)
                sleep(1)
            except ZeroDivisionError:
                raise Exception('Ошибка при открытии страницы')
            except WebDriverException as error:
                logger.error(f'Что-то с вебдрайвером {error.args[0]}')

    def wait_visible(self, locator, timeout=global_timeout):
        logger.info(f"Ожидаем элемент {locator[2]}")
        count = 0

        while count != timeout:
            try:
                element = self.browser.find_element(locator[0], locator[1])

                if element.is_displayed():
                    logger.info(f"---- {locator[2]} найден")
                    return element
            except NoSuchElementException:
                pass
            count += 1
            logger.info(f"---- {count}")
            sleep(1)

        logger.error(f'---- Элемент не стал видимым за {str(timeout)} секунд')
        raise ElementNotFoundError(locator=locator[2], timeout=str(timeout))

    def wait_clickable(self, locator):
        loc = (locator[0], locator[1])
        try:
            return self.wait.until(EC.element_to_be_clickable(loc), 'Элемент не кликабельен или не найден')
        except TypeError:
            return self.wait.until(EC.element_to_be_clickable(loc), 'Элемент не кликабельен или не найден')

    def click(self, locator, waiting=True):
        loc = (locator[0], locator[1])
        try:
            logger.info(f'---- Кликаем на элемент {locator[2]}')
            if waiting is True:
                self.wait_clickable(loc).click()
            else:
                self.browser.find_element(loc).click()
        except:
            raise Exception(f"ERROR!!! Не удалось клинкуть на элемент {locator[2]}")

    def get_text(self, locator):

        try:
            text = self.browser.find_element(locator[0], locator[1]).text
            if text == "":
                sleep(1)
                text = self.browser.find_element(locator[0], locator[1]).text
            return text
        except NoSuchElementException:
            logger.info(f"!!! Текст в {locator[0]} не найден !!!")
            return False

    def get_text_from(self, element, waiting=True, timeout=20):
        if waiting:
            self.wait_visible(element, timeout)
        return self.get_text(element)

    def send_keys(self, locator, text, force_send_keys=False):
        logger.info(f'---- Вводим текст в {locator[2]} = "{text}"')
        locator = (locator[0], locator[1])

        if text is None or text == '':
            raise Exception('Text cannot be blank')

        element = self.wait.until(EC.visibility_of_element_located(locator))
        if force_send_keys is False:
            element.send_keys(text)
            return True
        else:
            element.set_value(text)
            return True

    def input_text(self, element, text, waiting=True, timeout=20):
        if waiting is True:
            self.wait_visible(element, timeout)
        self.send_keys(element, text)
