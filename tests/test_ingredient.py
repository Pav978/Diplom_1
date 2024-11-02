from conftest import *
import allure


class TestIngredients:
    @allure.title('Проверка получения имени соуса')#
    def test_receiving_name_sauces(self, mock_sauce):
        assert mock_sauce.get_name() == Data_first.sauce_name

    @allure.title('Проверка получения имени начиники')
    def test_receiving_name_fillings(self, mock_filling):
        assert mock_filling.get_name() == Data_first.filling_name

    @allure.title('Проверка расчета стоимости')
    def test_receiving_price(self, mock_sauce_second):
        assert mock_sauce_second.get_price() == Data_second.sauce_price

    @allure.title('Проверка стоимости начинки')
    def test_receiving_price_fillings(self, mock_filling_second):
        assert mock_filling_second.get_price() == Data_second.filling_price

    @allure.title('Проверка получения ингридиента соуса')
    def test_receiving_sauces(self, mock_sauce):
        assert mock_sauce.get_type() == Data_first.sauce_type

    @allure.title('Проверка ингредиента начинки')
    def test_receiving_fillings(self, mock_filling):
        assert mock_filling.get_type() == Data_first.filling_type
