import pytest

from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert 'login' in self.browser.current_url

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_BTN_LOCATOR), "Login button is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_BTN_LOCATOR), "Register button is not presented"

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        email_field.send_keys(email)
        password_field1 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD)
        password_field2 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASS_AGAIN)
        password_field1.send_keys(password)
        password_field2.send_keys(password)
        reg_button = self.browser.find_element(*LoginPageLocators.REGISTER_BTN_LOCATOR)
        reg_button.click()
