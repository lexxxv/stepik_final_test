from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty(self):
        self.should_be_not_basket_formset();
        self.should_be_empty_text()

    def return_content_inner_text(self):
        content_inner_text = self.browser.find_element(*BasketPageLocators.CONTENT_INNER)
        return content_inner_text.text

    def should_be_not_basket_formset(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_FORMSET), \
            "Basket formset is presented, but should not be"

    def should_be_empty_text(self):
        content_inner_text = self.return_content_inner_text()
        content_inner_templ = 'Ваша корзина пуста Продолжить покупки'
        assert content_inner_text == content_inner_templ, "content_inner_text is {}, but wait {}".format(content_inner_text,
                                                                                                  content_inner_templ)
