from praktikum.burger import Burger
from conftest import *
from data import *
import pytest
import allure

#+
class TestBurger:
    @allure.title('Проверка добавления булки в бургер')
    def test_enter_bun(self, mocks_bun_first):
        burger = Burger()
        burger.set_buns(mocks_bun_first)
        assert burger.bun == mocks_bun_first
#+
    @allure.title('Проверка добавления ингредиентов в бургер')
    @pytest.mark.parametrize('ingredients, added_ingredient', [
        [Data_first.sauce_name, Data_first.sauce_name],
        [Data_first.filling_name, Data_first.filling_name],
        [Data_second.filling_name, Data_second.filling_name]
        ]
    )
    def test_enter_ingredients(self, ingredients, added_ingredient):
        burger = Burger()
        burger.add_ingredient(ingredients)
        assert burger.ingredients == [added_ingredient] and len(burger.ingredients) == 1
#+
    @allure.title('Проверка удаления ингредиентов из бургера')
    @pytest.mark.parametrize('ingredients, removed_ingredient', [
        [Data_first.sauce_name, Data_first.sauce_name],
        [Data_second.filling_name, Data_second.filling_name]
        ]
    )
    def test_remove_ingredients(self, ingredients, removed_ingredient, mock_filling):
        burger = Burger()
        burger.add_ingredient(mock_filling)
        burger.add_ingredient(ingredients)
        burger.remove_ingredient(1)
        assert removed_ingredient not in burger.ingredients and mock_filling in burger.ingredients
#+
    @allure.title('Проверка смены ингредиентытов бургера')
    def test_change_ingredients(self, mock_sauce, mock_filling):
        burger = Burger()
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        burger.move_ingredient(0, 1)
        assert len(burger.ingredients) == 2
        assert burger.ingredients[0] == mock_filling and burger.ingredients[1] == mock_sauce
#+
    @allure.title('Проверка расчета стоимости')
    def test_price_burgers(self, mocks_bun_second, mock_sauce_second, mock_filling_second):
        burger = Burger()
        burger.set_buns(mocks_bun_second)
        burger.add_ingredient(mock_sauce_second)
        burger.add_ingredient(mock_filling_second)
        assert burger.get_price() == Data_second.burger_final_cost
#??????????????????!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1
    @allure.title('Проверка рецета бургера')
    def test_receipt_burger(self, mocks_bun_first, mock_sauce, mock_filling, mock_filling_second):
        burger = Burger()
        burger.set_buns(mocks_bun_first)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        burger.add_ingredient(mock_filling_second)
        assert burger.get_receipt() == ('(==== Флюоресцентная булка R2-D3 ====)\n'
                                        '= sauce Соус традиционный галактический =\n'
                                        '= filling Мясо бессмертных моллюсков Protostomia =\n'
                                        '= filling Сыр с астероидной плесенью =\n'
                                        '(==== Флюоресцентная булка R2-D3 ====)\n'
                                        '\n'
                                        f'Price: {burger.get_price()}')
