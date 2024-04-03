import logging.config
import pytest
import logging
from os import path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

log_file_path = path.join(path.dirname(path.abspath(__file__)), 'login.ini')
logging.config.fileConfig(log_file_path)


@pytest.fixture()
def selenium():
    logging.info('Prepare browser...')
    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach', True)
    g = Service()
    driver = webdriver.Chrome(options=options, service=g)
    yield driver
    logging.info('Finality browser....')
    driver.quit()
