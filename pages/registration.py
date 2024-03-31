import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base import Base


class Registration(Base):

    """locator"""

    name_field = '//input[@id="reg_username"]'
    email_field = '//input[@id="reg_email"]'
    password_field = '//input[@id="reg_password"]'
    registration_button = '//button[@name="register"]'
    message = '//ul[@class="woocommerce-error"]/li'

    """Getters"""

    def get_name_field(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(
            (By.XPATH, self.name_field)))

    def get_email_field(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(
            (By.XPATH, self.email_field)))

    def get_password_field(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(
            (By.XPATH, self.password_field)))

    def get_registration_button(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(
            (By.XPATH, self.registration_button)))

    def get_message(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(
            (By.XPATH, self.message)))

    """Actions"""

    def send_name_field(self):
        self.get_name_field().send_keys('pawel')
        print('Ввод имени пользователя')

    def send_email_field(self):
        self.get_email_field().send_keys('pawel@mail.ru')
        print('Ввод email')

    def send_password_field(self):
        self.get_password_field().send_keys('123456789')
        print('Ввод пароля')

    def click_registration_button(self):
        self.get_registration_button().click()
        print('Кликнуть кнопку "Зарегистрироваться"')

    """Methods"""

    def registration(self):
        with allure.step('Регистрация'):
            self.send_name_field()
            self.send_email_field()
            self.send_password_field()
            self.click_registration_button()

    def registration_exist_email(self):
        with allure.step('Регистрация с существующим email'):
            self.driver.get('https://pizzeria.skillbox.cc/register/')
            self.driver.maximize_window()
            self.send_name_field()
            self.send_email_field()
            self.send_password_field()
            self.click_registration_button()
            self.get_value(self.get_message(), 'Error: Учетная запись с такой'
                                               ' почтой уже зарегистировавана. Пожалуйста авторизуйтесь.')

    def registration_without_login(self):
        with allure.step('Регистрация с пустым полем логин'):
            self.driver.get('https://pizzeria.skillbox.cc/register/')
            self.driver.maximize_window()
            self.get_email_field().send_keys('pavel@pavel.ru')
            self.send_password_field()
            self.click_registration_button()
            self.get_value(self.get_message(), 'Error: Пожалуйста введите корректное имя пользователя.')

    def registration_without_password(self):
        with allure.step('Регистрация с пустым полем пароль'):
            self.driver.get('https://pizzeria.skillbox.cc/register/')
            self.driver.maximize_window()
            self.get_name_field().send_keys('pav')
            self.get_email_field().send_keys('pavel@pavel.ru')
            self.click_registration_button()
            self.get_value(self.get_message(), 'Error: Введите пароль для регистрации.')
