from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def basket_should_be_empty(self):
        assert self.is_not_element_present(
            *BasketPageLocators.basket_items
        ), 'Cart is not empty, but should be'

    def empty_basket_should_have_message_about_it(self):
        assert self.is_element_present(
            *BasketPageLocators.empty_basket_message
        ), 'Cart should have message that it is empty, but it has not'
