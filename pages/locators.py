from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_BTN_LOCATOR = (By.NAME, "login_submit")
    REGISTER_BTN_LOCATOR = (By.NAME, "registration_submit")
