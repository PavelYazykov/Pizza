import time
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base import Base


class Desserts(Base):
    """locators"""

    right_slider = (
        '(//span[@class="ui-slider-handle ui-state-default ui-corner-all"])[2]'
    )
    apply_button = '//button[contains(text(), "Применить")]'
    add_cart_button = '(//a[contains(text(), "В корзину")])[2]'
    dessert = '//h1[@class="entry-title ak-container"]'

    """Getters"""

    def get_right_slider(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.right_slider))
        )

    def get_apply_button(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.apply_button))
        )

    def get_add_cart_button(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.add_cart_button))
        )

    def get_dessert(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.dessert))
        )

    """Actions"""

    def move_right_slider(self):
        action = webdriver.ActionChains(self.driver)
        action.drag_and_drop_by_offset(self.get_right_slider(), -200, 0).perform()
        time.sleep(2)
        print("Установка верхней границы цены")

    def click_apply_button(self):
        self.get_apply_button().click()
        print('Клик по кнопке "применить"')

    def click_add_cart(self):
        self.get_add_cart_button().click()
        print('Клик по кнопке "В корзину"')

    """Methods"""

    def buy_dessert(self):
        with allure.step("Настройка фильтров и покупка десерта"):
            self.move_right_slider()
            self.click_apply_button()
            self.click_add_cart()

    def check_dessert(self):
        with allure.step("Проверка перехода в  раздел Десерты"):
            self.get_value(self.get_dessert(), "ДЕСЕРТЫ")
