import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.main_page import Main_page
from pages.cart import Cart
from pages.my_account import My_account
from pages.checkout import Checkout
import re
from playwright.sync_api import Page, expect
import allure


@allure.description('Проверка применения верного промокода')
def test_01(selenium):
    driver = selenium

    """Выбор пиццы и переход в корзину"""
    main_p = Main_page(driver)
    main_p.select_pizza()
    main_p.go_to_cart()

    """Применение промокода"""
    cart_p = Cart(driver)
    cart_p.apply_right_promo()

    """Проверка"""
    cart_p.assert_cupon_right()


@allure.description('Проверка применения ошибочного промокода')
def test_02(selenium):
    driver = selenium

    """Выбор пиццы и переход в корзину"""
    main_p = Main_page(driver)
    main_p.select_pizza()
    main_p.go_to_cart()

    """Применение промокода"""
    cart_p = Cart(driver)
    cart_p.apply_wrong_promo()

    """Проверка"""
    cart_p.assert_cupon_wrong()


@allure.description('Проверка применения промокода при сбоях сервера')
def test_03(page: Page):
    page.goto('https://pizzeria.skillbox.cc/')
    pizza_add_cart = page.wait_for_selector('(//a[@class="button product_type_simple add_to_cart_button'
                                            ' ajax_add_to_cart"])[6]')
    time.sleep(1)
    pizza_add_cart.click()
    time.sleep(1)
    go_cart = page.wait_for_selector('(//a[contains(text(), "Корзина")])[1]')
    go_cart.click()
    promo_field = page.wait_for_selector('//input[@id="coupon_code"]')
    promo_field.fill('GIVEMEHALYAVA')
    time.sleep(10)
    promo_button = page.wait_for_selector('//button[@name="apply_coupon"]')
    page.route("https://pizzeria.skillbox.cc/?wc-ajax=apply_coupon", lambda route: route.abort())
    promo_button.click()
    time.sleep(10)


@allure.description('Проверка повторного применения промокода')
def test_04(selenium):
    driver = selenium

    """Добавление пиццы в корзину и переход на страницу оформдения заказа"""
    main_p = Main_page(driver)
    main_p.select_pizza()
    main_p.go_to_cart()
    main_p.order_product()

    """Переход в раздел мой аккаунт"""
    account_p = My_account(driver)
    account_p.go_my_account()

    """Авторизация пользователя"""
    account_p.authorization()

    """Переход в корзину"""
    main_p.go_to_cart()

    """Применение промокода"""
    cart_p = Cart(driver)
    time.sleep(1)
    cart_p.apply_right_promo()

    """Оформить заказ"""
    cart_p.order()

    """Оформление заказа"""
    checkout_p = Checkout(driver)
    checkout_p.checkout()
    time.sleep(5)

    """Повторный выбор пиццы"""
    main_p = Main_page(driver)
    main_p.select_pizza()
    main_p.go_to_cart()

    """Повторное применение промоода"""
    cart_p.apply_right_promo()
    cart_p.promocode_assert()
