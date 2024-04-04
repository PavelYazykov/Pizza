import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from base.base import Base


class About_pizza(Base):
    """locators"""

    choose_bort = '//select[@id="board_pack"]'
    cheese_bort = '"55.00"'
    add_cart_button = '//button[@name="add-to-cart"]'
    go_cart = '(//a[contains(text(), "Корзина")])[1]'
    descr = '//li[@id="tab-title-description"]'

    """Getters"""

    def get_choose_bort(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.choose_bort))
        )

    def get_add_cart_button(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.add_cart_button))
        )

    def get_go_cart(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.go_cart))
        )

    def get_descr(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.descr))
        )

    """Actions"""

    def click_cheese_bort(self):
        select = Select(self.get_choose_bort())
        select.select_by_visible_text("Сырный - 55.00 р.")
        print("Выбран сырной борт")

    def click_add_cart_button(self):
        self.get_add_cart_button().click()
        print("Пицца добавлена в корзину")

    def click_go_cart(self):
        self.get_go_cart().click()
        print("Переход в корзину")

    """Methods"""

    def add_options_pizza(self):
        with allure.step("Просмотр информации о товаре и добавление опций"):
            self.click_cheese_bort()
            self.click_add_cart_button()
            # self.click_go_cart()

    def check_pizza_info(self):
        with allure.step("Проверка перехода к описанию пиццы"):
            self.get_value(self.get_descr(), "ОПИСАНИЕ")
