from selenium.webdriver.common.by import By


class TextBoxLocators():
    NAME_FIELD = (By.XPATH, '//input[@id="userName"]', 'Поле ввода "Full Name"')
    EMAIL_FIELD = (By.XPATH, '//input[@id="userEmail"]', 'Поле ввода "Email"')
    CURRENT_ADDRESS_FIELD = (By.XPATH, '//textarea[@id="currentAddress"]', 'Поле ввода "Current Address"')
    PERMANENT_ADDRESS_FIELD = (By.XPATH, '//textarea[@id="permanentAddress"]', 'Поле ввода "Permanent Address"')
    SUBMIT_BUTTON = (By.XPATH, '//button[@id="submit"]', 'Кнопка "Submit"')

    NAME_OUTPUT = (By.XPATH, '//p[@id="name"]', 'Строка  "Name"')
    EMAIL_OUTPUT = (By.XPATH, '//p[@id="email"]', 'Cтрока "Email"')
    CURRENT_ADDRESS_OUTPUT = (By.XPATH, '//p[@id="currentAddress"]', 'Строка "Current Address"')
    PERMANENT_ADDRESS_OUTPUT = (By.XPATH, '//p[@id="permanentAddress"]', 'Строка "Permananet Address"')
