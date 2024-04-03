import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.main_page import Main_page
from pages.about_pizza import About_pizza
from pages.cart import Cart
from pages.dessertes import Desserts
from pages.my_account import My_account
from pages.registration import Registration
from pages.checkout import Checkout


@allure.description('Добавление пиццы в корзину со слайдера')
def test_01(selenium):
    driver = selenium

    """Переход на сайт"""
    main_p = Main_page(driver)
    main_p.go_site()

    """Добавление пиццы в корзину"""
    main_p.add_cart_pizza1()
    main_p.go_to_cart()

    """Проверка, пицца добавлена в корзину"""
    cart_p = Cart(driver)
    cart_p.assertion_pizza()


@allure.description('Проверка работы слайдера')
def test_02(selenium):
    driver = selenium

    """Проверка работы слайдера"""
    main_p = Main_page(driver)
    main_p.slider_test()


@allure.description('Просмотр информации о пицце')
def test_03(selenium):
    driver = selenium

    """Переход на сайт"""
    main_p = Main_page(driver)
    main_p.go_site()

    """Просмотр информации о пицце"""
    main_p.pizza_info()

    """Проверка, страница с информацией о пицце открыта"""
    about_pizza_p = About_pizza(driver)
    about_pizza_p.check_pizza_info()


@allure.description('Добавление опций к пицце')
def test_04(selenium):
    driver = selenium

    """Переход на сайт"""
    main_p = Main_page(driver)
    main_p.go_site()

    """Просмотр информации о пицце"""
    main_p.pizza_info()

    """Добавление опций к пицце"""
    about_pizza_p = About_pizza(driver)
    about_pizza_p.add_options_pizza()

    """Переход в корзину"""
    main_p.go_to_cart()

    """Проверка, выбранная пицца в корзине"""
    cart_p = Cart(driver)
    cart_p.assertion_pizza_2()

    """Проверка, сырный борт добавлен"""
    cart_p.assertion_cheese_bort()


@allure.description('Редактирование корзины')
def test_05(selenium):
    driver = selenium

    """Переход на сайт"""
    main_p = Main_page(driver)
    main_p.go_site()

    """Просмотр информации о пицце"""
    main_p.add_cart_pizza1()
    main_p.pizza_info()

    """Добавление опций к пицце"""
    about_pizza_p = About_pizza(driver)
    about_pizza_p.add_options_pizza()

    """Переход в корзину"""
    main_p.go_to_cart()

    """Редактирование товаров в корзине"""
    cart_p = Cart(driver)
    cart_p.edit_cart()


@allure.description('Переход в раздел десерты')
def test_06(selenium):
    driver = selenium

    """Переход на сайт"""
    main_p = Main_page(driver)
    main_p.go_site()

    """Добавление пиццы в корзину"""
    main_p.add_cart_pizza1()

    """Переход в корзину"""
    main_p.go_to_cart()

    """Переход на страницу с десертами"""
    main_p.go_to_dessert()

    """Проверка перехода"""
    dessert_p = Desserts(driver)
    dessert_p.check_dessert()


@allure.description('Настройка фильтров в разделе десерты и добавление в корзину')
def test_07(selenium):
    driver = selenium

    """Переход на сайт"""
    main_p = Main_page(driver)
    main_p.go_site()

    """Переход в раздел десерты"""
    main_p.go_to_dessert()

    """Покупка десерта"""
    dessert_p = Desserts(driver)
    dessert_p.buy_dessert()

    """Переход в корзину"""
    main_p.go_to_cart()

    """Проверка десерт добавлен в корзину"""
    cart_p = Cart(driver)
    cart_p.assert_dessert()


@allure.description('Регистрация пользователя')
def test_08(selenium):
    driver = selenium

    """Переход на сайт"""
    main_p = Main_page(driver)
    main_p.go_site()

    """Переход в раздел мой аккаунт"""
    my_account_p = My_account(driver)
    my_account_p.my_account_reg()

    """Регистрация пользователя"""
    registration_p = Registration(driver)
    registration_p.registration()


@allure.description('Авторизация пользователя')
def test_09(selenium):
    driver = selenium

    """Переход на сайт"""
    main_p = Main_page(driver)
    main_p.go_site()

    """Авторизация пользователя"""
    account_p = My_account(driver)
    account_p.go_my_account()
    account_p.authorization()


@allure.description('Авторизация с пустым полем Логин')
def test_10(selenium):
    driver = selenium

    my_account_p = My_account(driver)
    my_account_p.authorization_empty_login()


@allure.description('Авторизация с пустым полем Пароль')
def test_11(selenium):
    driver = selenium

    my_account_p = My_account(driver)
    my_account_p.authorization_empty_password()


@allure.description('Проверка восстановления пароля')
def test_12(selenium):
    driver = selenium

    my_account_p = My_account(driver)
    my_account_p.check_forget_password_link()


@allure.description('Регистрация с существующим email')
def test_13(selenium):
    driver = selenium

    registration_p = Registration(driver)
    registration_p.registration_exist_email()


@allure.description('Регистрация с пустым полем логин')
def test_14(selenium):
    driver = selenium

    registration_p = Registration(driver)
    registration_p.registration_without_login()


@allure.description('Регистрация с пустым полем пароль')
def test_15(selenium):
    driver = selenium

    registration_p = Registration(driver)
    registration_p.registration_without_password()


@allure.description('Покупка и оформление заказа')
def test_16(selenium):
    driver = selenium

    """Выбор товара, переход в корзину и переход к оформлению заказа"""
    main_p = Main_page(driver)
    main_p.select_pizza()
    main_p.go_to_cart()
    main_p.order_product()

    """Авторизация"""
    account_p = My_account(driver)
    account_p.go_my_account()
    account_p.authorization()

    """Переход в корзину"""
    main_p.go_to_cart()

    """Переход в корзину и к оформлению заказа"""
    cart = Cart(driver)
    cart.order()

    """Оформление заказа"""
    checkout_p = Checkout(driver)
    checkout_p.checkout()
