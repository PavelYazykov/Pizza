import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base import Base


class Checkout(Base):

    """locators"""

    name = '//input[@id="billing_first_name"]'
    surname = '//input[@id="billing_last_name"]'
    street = '//input[@id="billing_address_1"]'
    city = '//input[@id="billing_city"]'
    state = '//input[@id="billing_state"]'
    postcode = '//input[@id="billing_postcode"]'
    phone = '//input[@id="billing_phone"]'
    payment = '//input[@id="payment_method_cod"]'
    agreement = '//input[@id="terms"]'
    order_date = '//input[@id="order_date"]'
    order_button = '//button[@id="place_order"]'

    """Getters"""
    def get_name(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(
            (By.XPATH, self.name)))

    def get_surname(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(
            (By.XPATH, self.surname)))

    def get_street(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(
            (By.XPATH, self.street)))

    def get_city(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(
            (By.XPATH, self.city)))

    def get_state(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(
            (By.XPATH, self.state)))

    def get_postcode(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(
            (By.XPATH, self.postcode)))

    def get_phone(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(
            (By.XPATH, self.phone)))

    def get_payment(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(
            (By.XPATH, self.payment)))

    def get_agreement(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(
            (By.XPATH, self.agreement)))

    def get_order_date(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(
            (By.XPATH, self.order_date)))

    def get_order_button(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(
            (By.XPATH, self.order_button)))

    """Actions"""
    def send_name(self):
        self.get_name().clear()
        self.get_name().send_keys('Павел')
        print('Ввод имени')

    def send_surname(self):
        self.get_surname().clear()
        self.get_surname().send_keys('Языков')
        print('Ввод фамилии')

    def send_street(self):
        self.get_street().clear()
        self.get_street().send_keys('Пушкина д.15')
        print('Ввод улицы')

    def send_city(self):
        self.get_city().clear()
        self.get_city().send_keys('Пушкин')
        print('Ввод города')

    def send_state(self):
        self.get_state().clear()
        self.get_state().send_keys('Пушкинская')
        print('Ввод области')

    def send_postcode(self):
        self.get_postcode().clear()
        self.get_postcode().send_keys('353676')
        print('Ввод индекса')

    def send_phone(self):
        self.get_phone().clear()
        self.get_phone().send_keys('+79267777777')
        print('Ввод номера телефона')

    def click_payment(self):
        self.get_payment().click()
        print('Выбор способа оплаты')

    def click_agreement(self):
        self.get_agreement().click()
        print('Пользовательское соглашение')

    def click_order_button(self):
        self.get_order_button().click()
        print('Клик по кнопке "Оформить заказ"')

    def send_order_date(self):
        self.get_order_date().send_keys('25')
        self.get_order_date().send_keys('12')
        self.get_order_date().send_keys('2024')
        print('Ввод даты')

    """Methods"""

    def checkout(self):
        with allure.step('Оформление заказа, ввод данных'):
            self.send_name()
            self.send_surname()
            self.send_street()
            self.send_city()
            self.send_state()
            self.send_postcode()
            self.send_phone()
            self.click_payment()
            self.click_agreement()
            self.send_order_date()
            self.click_order_button()
