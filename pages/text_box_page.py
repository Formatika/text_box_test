from ..pages.base_page import BasePage
from ..pages.locators import TextBoxLocators


class TextBoxPage(BasePage):

    def enter_name_in_name_field(self, text):
        """Ввести текст в поле ввода 'Full Name'"""
        self.input_text(TextBoxLocators().NAME_FIELD, text)

    def enter_email_in_email_field(self, text):
        """Ввести текст в поле ввода 'Email'"""
        self.input_text(TextBoxLocators().EMAIL_FIELD, text)

    def enter_addres_in_current_addres_field(self, text):
        """Ввести текст в поле ввода 'Current Address'"""
        self.input_text(TextBoxLocators().CURRENT_ADDRESS_FIELD, text)

    def enter_addres_in_permanent_addres_field(self, text):
        """Ввести текст в поле ввода 'Permanent Address'"""
        self.input_text(TextBoxLocators().PERMANENT_ADDRESS_FIELD, text)

    def click_button_submit(self):
        """Нажать на кнопку 'Submit'"""
        self.click(TextBoxLocators().SUBMIT_BUTTON)

    def get_text_from_string_name(self):
        """Получить значение из строки 'Name'"""
        return self.get_text_from(TextBoxLocators().NAME_OUTPUT)

    def get_text_from_string_email(self):
        """Получить значение из строки 'Email'"""
        return self.get_text_from(TextBoxLocators().EMAIL_OUTPUT)

    def get_text_from_string_current_address(self):
        """Получить значение из строки 'Current Address'"""

        return self.get_text_from(TextBoxLocators().CURRENT_ADDRESS_OUTPUT)

    def get_text_from_string_permananet_address(self):
        """Получить значение из строки 'Permananet Address'"""
        return self.get_text_from(TextBoxLocators().PERMANENT_ADDRESS_OUTPUT)

    def fill_form_with_random_data(self, name, email, current_address, permanent_address):
        self.enter_name_in_name_field(name)
        self.enter_email_in_email_field(email)
        self.enter_addres_in_current_addres_field(current_address)
        self.enter_addres_in_permanent_addres_field(permanent_address)
