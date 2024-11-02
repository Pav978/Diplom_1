from conftest import *
from data import *
import allure


class TestBun:
#+
    @allure.title('Проверка полученного названия булки')
    def test_bun(self, mocks_bun_first):
        assert mocks_bun_first.get_name() == Data_first.bun_name
#+
    @allure.title('Проверка полученной стоимости булки')
    def test_bun_price(self, mocks_bun_second):
        assert mocks_bun_second.get_price() == Data_second.bun_price
