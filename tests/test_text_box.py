import allure
from ..utils.data_generator import generate_name, generate_fake_email, generate_address
from ..fixtures.setup_teardowns import text_box_page


@allure.feature('Тесты на страницу Text Box')
class TestNegativeRegistration:

    @allure.story('Сравнение, что данные, введенные в форму, соответствуют данным, которые отображаются на странице после отправки формы')
    def test_comparison_of_entered_data(self, text_box_page):
        name, email, current_address, permanent_address = generate_name(), generate_fake_email(), generate_address(), generate_address()
        with allure.step("Ввод имени, почты, текущего адреса, постоянного адреса"):
            text_box_page.fill_form_with_random_data(name, email, current_address, permanent_address)

        with allure.step('Клик на кнопку "Submit"'):
            text_box_page.click_button_submit()

        with allure.step('Проверка отображения введенных данных'):
            assert text_box_page.get_text_from_string_name() == f"Name:{name}"
            assert text_box_page.get_text_from_string_email() == f"Email:{email}"
            assert text_box_page.get_text_from_string_current_address() == f"Current Address :{current_address}"
            assert text_box_page.get_text_from_string_permananet_address() == f"Permananet Address :{permanent_address}"
