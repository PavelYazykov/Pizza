from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.main_page import Main_page
from pages.bonus_programm import Bonus_program
import allure


@allure.description('Регистрация в бонусной системе')
def test_01():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach', True)
    g = Service()
    driver = webdriver.Chrome(options=options, service=g)

    """Переход в раздел бонусной программы"""
    main_p = Main_page(driver)
    main_p.go_bonus_programm()

    """Регистрация в бонусной программе c проверкой"""
    bonus_program_p = Bonus_program(driver)
    bonus_program_p.get_bonus_card()
