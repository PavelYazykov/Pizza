

class Base:

    def __init__(self, driver):
        """Инициализация класса"""
        self.driver = driver

    def get_value(self, locator, word):
        """Получение значения локатора"""
        value_word = locator.text
        print(value_word)
        assert value_word == word
        print(word, 'Проверка пройдена успешно')

    def get_current_url(self, url):
        """Получение ссылки"""
        cur_url = self.driver.current_url()
        print(cur_url)
        assert cur_url == url
        print(cur_url, 'Проверка пройдена')

    def promocode_assertion(self, locator, word):
        """Проверка повторного ввода промокода"""
        value_locator = locator.text
        if value_locator == word:
            raise Exception('Купон применен повторно')



