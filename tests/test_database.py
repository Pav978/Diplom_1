from data import TestDataBase
from conftest import dbase
import pytest
import allure

#+
class TestDataBase:
    @allure.title('Проверка получения списка булок')
    @pytest.mark.parametrize('number_bun, name_bun, price_bun', TestDataBase.test_data_base_buns)
    def test_receiving_list_buns(self, dbase, number_bun, name_bun, price_bun):
        data_bun= dbase.available_buns()
        assert data_bun[number_bun].get_name() == name_bun and data_bun[number_bun].get_price() == price_bun
#+
    @allure.title('Проверка работы метода available_ingredients, получающего список доступных ингредиентов из базы')
    @pytest.mark.parametrize('ing_number, ing_type, ing_name, ing_price',
                             TestDataBase.test_data_base_ingredients)
    def test_receiving_ingredients_buns(self, dbase, ing_number, ing_type, ing_name, ing_price):
        data_ingredients = dbase.available_ingredients()
        assert (data_ingredients[ing_number].get_name() == ing_name and
                data_ingredients[ing_number].get_type() == ing_type and
                data_ingredients[ing_number].get_price() == ing_price)
