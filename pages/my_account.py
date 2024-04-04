import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base import Base


class My_account(Base):
    """locators"""

    account_button = '//li[@id="menu-item-30"]'
    registration_button = '//button[@class="custom-register-button"]'
    name_field = '//input[@id="username"]'
    password_field = '//input[@id="password"]'
    auth_button = '//button[@name="login"]'
    field_error = '//ul[@class="woocommerce-error"]/li'
    forget_password = "Забыли пароль?"
    reset_password_field = '//input[@name="user_login"]'
    reset_button = '//button[@value="Reset password"]'
    message = '//div[@class="woocommerce-message"]'

    """Methods"""

    def get_account_button(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.account_button))
        )

    def get_registration_button(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.registration_button))
        )

    def get_name_field(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.name_field))
        )

    def get_password_field(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.password_field))
        )

    def get_auth_button(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.auth_button))
        )

    def get_field_error(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.field_error))
        )

    def get_forget_password(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.LINK_TEXT, self.forget_password))
        )

    def get_reset_password(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.reset_password_field))
        )

    def get_reset_button(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.reset_button))
        )

    def get_message(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.message))
        )

    """Actions"""

    def click_account_button(self):
        self.get_account_button().click()
        print('Переход в раздел "Мой аккаунт"')

    def click_registration_button(self):
        self.get_registration_button().click()
        print('Переход на страницу "Регистрация"')

    def send_name_field(self):
        self.get_name_field().send_keys("pawel")
        print("Введено имя пользователя")

    def send_password_field(self):
        self.get_password_field().send_keys("123456789")
        print("Введен пароль")

    def click_auth_button(self):
        self.get_auth_button().click()
        print("Клик по кнопке авторизации")

    def click_forget_password(self):
        self.get_forget_password().click()
        print("Клик по кнопке восстановления пароля")

    def send_reset_password(self):
        self.get_reset_password().send_keys("pawel")
        print("Введен логин для сброса пароля")

    def click_reset_button(self):
        self.get_reset_button().click()
        print("Клик по кнопке Сброс пароля")

    """Methods"""

    def my_account_reg(self):
        with allure.step('Переход на вкладку "Мой аккаунт" с последующей регистрацией'):
            self.click_account_button()
            self.click_registration_button()

    def go_my_account(self):
        with allure.step("Переход на вкладку Мой аккаунт"):
            self.click_account_button()

    def authorization(self):
        with allure.step("Авторизация"):
            self.send_name_field()
            self.send_password_field()
            self.click_auth_button()

    def authorization_empty_login(self):
        with allure.step("Авторизация c пустым полем логин"):
            self.driver.get("https://pizzeria.skillbox.cc/my-account/")
            self.driver.maximize_window()
            self.send_password_field()
            self.click_auth_button()
            self.get_value(
                self.get_field_error(), "Error: Имя пользователя обязательно."
            )

    def authorization_empty_password(self):
        with allure.step("Авторизация c пустым полем пароль"):
            self.driver.get("https://pizzeria.skillbox.cc/my-account/")
            self.driver.maximize_window()
            self.send_name_field()
            self.click_auth_button()
            self.get_value(self.get_field_error(), "Пароль обязателен.")

    def check_forget_password_link(self):
        self.driver.get("https://pizzeria.skillbox.cc/my-account/")
        self.driver.maximize_window()
        self.click_forget_password()
        time.sleep(2)
        self.send_reset_password()
        self.click_reset_button()
        self.get_value(self.get_message(), "Password reset email has been sent.")
