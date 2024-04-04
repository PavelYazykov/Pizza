import time
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base import Base


class Main_page(Base):
    """Locators"""

    url = "https://pizzeria.skillbox.cc/"
    pizza_descr = '(//div[@class="item-img"])[8]'
    pizza1_hover = '(//div[@class="item-img"])[6]'
    pizza2_hover = '(//div[@class="item-img"])[7]'
    pizza1_add_cart = '(//a[@class="button product_type_simple add_to_cart_button ajax_add_to_cart"])[6]'
    pizza2_add_cart = '(//a[@class="button product_type_simple add_to_cart_button ajax_add_to_cart"])[7]'
    left_slider = '//a[@class="slick-prev"]'
    right_slider = '//a[@class="slick-next"]'
    go_cart = '(//a[contains(text(), "Корзина")])[1]'
    menu = '//li[@id="menu-item-389"]'
    desserte = '//li[@id="menu-item-391"]'
    order = '//li[@id="menu-item-31"]'
    bonus_programm = '//li[@id="menu-item-363"]'

    """Getters"""

    def get_pizza_descr(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.pizza_descr))
        )

    def get_pizza1_hover(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.pizza1_hover))
        )

    def get_pizza2_hover(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.pizza2_hover))
        )

    def get_pizza1_add_cart(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.pizza1_add_cart))
        )

    def get_pizza2_add_cart(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.pizza2_add_cart))
        )

    def get_left_slider(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.left_slider))
        )

    def get_right_slider(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.right_slider))
        )

    def get_go_cart(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.go_cart))
        )

    def get_menu(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.menu))
        )

    def get_desserte(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.desserte))
        )

    def get_order(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.order))
        )

    def get_bonus_programm(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.bonus_programm))
        )

    """Actions"""

    def click_pizza_descr(self):
        self.get_pizza_descr().click()
        print("Получение информации о пицце")

    def add_cart_pizza1(self):
        action = webdriver.ActionChains(self.driver)
        action.move_to_element(self.get_pizza1_hover()).perform()
        time.sleep(1)
        self.get_pizza1_add_cart().click()
        time.sleep(1)
        print("Добавление в корзину первой пиццы")

    def add_cart_pizza2(self):
        action = webdriver.ActionChains(self.driver)
        action.move_to_element(self.get_pizza2_hover()).perform()
        time.sleep(1)
        self.get_pizza2_add_cart().click()
        print("Добавление в корзину второй пиццы")

    def click_left_slider(self):
        self.get_left_slider().click()
        print("Перемещение слайдера влево")

    def click_right_slider(self):
        self.get_right_slider().click()
        print("Перемещение слайдера впправо")

    def click_go_cart(self):
        self.get_go_cart().click()
        print("Переход в корзину")

    def click_menu(self):
        action = webdriver.ActionChains(self.driver)
        action.move_to_element(self.get_menu()).perform()
        time.sleep(1)
        self.get_desserte().click()
        print("Переход в раздел десерты")

    def click_order(self):
        self.get_order().click()
        print('Клик по кнопке "Оформление заказа"')

    def click_bonus_programm(self):
        self.get_bonus_programm().click()
        print('Клик по кнопке "Бонусная программа"')

    """Methods"""

    def select_pizza(self):
        with allure.step("Выбор пиццы"):
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.add_cart_pizza1()
            time.sleep(1)

    def order_product(self):
        with allure.step("Переход на страницу оформления заказа"):
            self.click_order()

    def go_bonus_programm(self):
        with allure.step("Переход на страницу бонусной программы"):
            self.driver.get("https://pizzeria.skillbox.cc/")
            self.driver.maximize_window()
            self.click_bonus_programm()
            time.sleep(1)

    def go_site(self):
        with allure.step("Переход на сайт"):
            self.driver.get("https://pizzeria.skillbox.cc/")
            self.driver.maximize_window()

    def add_pizza(self):
        with allure.step("Добавление пиццы в корзину"):
            self.add_cart_pizza1()

    def go_to_cart(self):
        with allure.step("Переход в корзину"):
            self.click_go_cart()
            time.sleep(1)

    def slider_test(self):
        with allure.step("Прокрутка слайдера влево и вправо"):
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.add_cart_pizza1()
            self.click_right_slider()
            time.sleep(1)
            self.click_left_slider()

    def pizza_info(self):
        with allure.step("Получение информации о пицце"):
            self.click_pizza_descr()

    def go_to_dessert(self):
        with allure.step("Переход в раздел десерты"):
            self.click_menu()
