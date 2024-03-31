import time
import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base import Base


class Cart(Base):

    """locators"""

    quantity_field = '(//input[@class="input-text qty text"])[1]'
    pizza_1 = 'Пицца "Рай"'
    pizza_2 = 'Пицца "Как у бабушки"'
    pizza_3 = 'Пицца "Ветчина и грибы"'
    options = '//dd[@class="variation-"]'
    del_pizza = '(//a[@aria-label="Remove this item"])[2]'
    dessert = 'Десерт "Морковный каприз"'
    order_button = '//a[contains(text(), "ПЕРЕЙТИ К ОПЛАТЕ")]'
    promocode_field = '//input[@id="coupon_code"]'
    cupon_button = '//button[@name="apply_coupon"]'
    cupon_apply_right = '//div[@class="woocommerce-message"]'
    cupon_apply_wrong = '//ul[@class="woocommerce-error"]'

    """Getters"""

    def get_quantity_field(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(
            (By.XPATH, self.quantity_field)))

    def get_pizza_1(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(
            (By.LINK_TEXT, self.pizza_1)))

    def get_pizza_2(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(
            (By.LINK_TEXT, self.pizza_2)))

    def get_pizza_3(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(
            (By.LINK_TEXT, self.pizza_3)))

    def get_options(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(
            (By.XPATH, self.options)))

    def get_dessert(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(
            (By.LINK_TEXT, self.dessert)))

    def get_del_pizza(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(
            (By.XPATH, self.del_pizza)))

    def get_order_button(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(
            (By.XPATH, self.order_button)))

    def get_promocode_field(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(
            (By.XPATH, self.promocode_field)))

    def get_cupon_button(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(
            (By.XPATH, self.cupon_button)))

    def get_cupon_apply_right(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(
            (By.XPATH, self.cupon_apply_right)))

    def get_cupon_apply_wrong(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(
            (By.XPATH, self.cupon_apply_wrong)))

    """Actions"""

    def edit_quantity(self):
        self.get_quantity_field().click()
        self.get_quantity_field().send_keys(Keys.BACKSPACE)
        self.get_quantity_field().send_keys('2')
        self.get_quantity_field().send_keys(Keys.RETURN)
        print('Количество пицц изменено')

    def remove_pizza(self):
        self.get_del_pizza().click()
        print('Пицца удалена из заказа')

    def click_order_button(self):
        self.get_order_button().click()
        print('Клик по кнопке "Оформить заказ"')

    def send_promocode_field_right(self):
        self.get_promocode_field().send_keys('GIVEMEHALYAVA')
        print('Ввод верного промокода')

    def send_promocode_field_wrong(self):
        self.get_promocode_field().send_keys('DC120')
        print('Ввод ошибочного промокода')

    def click_cupon_button(self):
        self.get_cupon_button().click()
        print('Клик по кнопке применить купон')

    """Methods"""

    def assert_dessert(self):
        with allure.step('Проверка, десерт добавлен в корзине'):
            self.get_value(self.get_dessert(), 'Десерт "Морковный каприз"')

    def order(self):
        with allure.step('Оформить заказ'):
            self.click_order_button()

    def apply_right_promo(self):
        with allure.step('Ввод верного промокода'):
            self.send_promocode_field_right()
            self.click_cupon_button()

    def apply_wrong_promo(self):
        with allure.step('Ввод ошибочного промокода'):
            self.send_promocode_field_wrong()
            self.click_cupon_button()

    def assert_cupon_right(self):
        with allure.step('Проверка применения верного промокода'):
            self.get_value(self.get_cupon_apply_right(), 'Coupon code applied successfully.')

    def assert_cupon_wrong(self):
        with allure.step('Проверка применения ошибочного промокода'):
            self.get_value(self.get_cupon_apply_wrong(), 'Неверный купон.')

    def promocode_assert(self):
        with allure.step('Проверка применения верного промокода'):
            self.promocode_assertion(self.get_cupon_apply_right(), 'Coupon code applied successfully.')

    def assertion_pizza(self):
        with allure.step('Проверка что пицца добавлена в корзину'):
            self.get_value(self.get_pizza_2(), 'Пицца "Как у бабушки"')

    def assertion_pizza_2(self):
        with allure.step('Проверка что пицца добавлена в корзину'):
            self.get_value(self.get_pizza_3(), 'Пицца "Ветчина и грибы"')

    def assertion_cheese_bort(self):
        with allure.step('Проверка, сырный борт добавлен'):
            self.get_value(self.get_options(), 'Сырный борт')

    def edit_cart(self):
        with allure.step('Изменение количества товаров и удаление товара из корзины'):
            # self.get_value(self.get_pizza_1(), 'Пицца "Рай"')
            self.get_value(self.get_pizza_2(), 'Пицца "Как у бабушки"')
            self.get_value(self.get_pizza_3(), 'Пицца "Ветчина и грибы"')
            # self.get_value(self.get_options(), 'Сырный борт')
            self.edit_quantity()
            time.sleep(3)
            self.remove_pizza()
