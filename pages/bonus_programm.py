import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base import Base


class Bonus_program(Base):

    """locator"""

    name_field = '//input[@id="bonus_username"]'
    phone_field = '//input[@id="bonus_phone"]'
    apply_card_button = '//button[@name="bonus"]'
    apply_card = '//h3[contains(text(), "Ваша карта оформлена!")]'

    """Getters"""

    def get_name_field(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(
            (By.XPATH, self.name_field)))

    def get_phone_field(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(
            (By.XPATH, self.phone_field)))

    def get_apply_card_button(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(
            (By.XPATH, self.apply_card_button)))

    def get_apply_card(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(
            (By.XPATH, self.apply_card)))

    """Actions"""

    def send_name_field(self, word):
        self.get_name_field().send_keys(word)
        print('Ввод имени')

    def send_phone_field(self, phone):
        self.get_phone_field().send_keys(phone)
        print('Ввод номера телефона')

    def click_apply_card_button(self):
        self.get_apply_card_button().click()
        print('Клик по кнопке "Оформить карту"')

    """Methods"""

    def get_bonus_card(self):
        with allure.step('Регистрация в бонусной программе'):
            self.send_name_field('Павел')
            self.send_phone_field('+79999999999')
            self.click_apply_card_button()
            time.sleep(1)
            self.driver.switch_to.alert.accept()
            self.get_value(self.get_apply_card(), 'Ваша карта оформлена!')
