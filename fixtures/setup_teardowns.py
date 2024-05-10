import pytest
from ..url import TEXT_BOX_URL
from ..pages.text_box_page import TextBoxPage


@pytest.fixture(scope='class')
def text_box_page(browser):
    page = TextBoxPage(browser)
    page.open(TEXT_BOX_URL)
    return page
