from praktikum.database import Database
from unittest.mock import Mock
from data import *
import pytest

#+
@pytest.fixture
def mocks_bun_first():
    mock_bun_f = Mock()
    mock_bun_f.get_name.return_value = Data_first.bun_name
    mock_bun_f.get_price.return_value = Data_first.bun_price
    return mock_bun_f

##+
@pytest.fixture
def mocks_bun_second():
    mock_bun_s = Mock()
    mock_bun_s.get_name.return_value = Data_second.bun_name
    mock_bun_s.get_price.return_value = Data_second.bun_price
    return mock_bun_s


@pytest.fixture
def mock_sauce():
    mock_sauce = Mock()
    mock_sauce.get_name.return_value = Data_first.sauce_name
    mock_sauce.get_price.return_value = Data_first.sauce_price
    mock_sauce.get_type.return_value = Data_first.sauce_type
    return mock_sauce


@pytest.fixture
def mock_sauce_second():
    mock_sauce_s = Mock()
    mock_sauce_s.get_name.return_value = Data_second.sauce_name
    mock_sauce_s.get_price.return_value = Data_second.sauce_price
    mock_sauce_s.get_type.return_value = Data_second.sauce_type
    return mock_sauce_s


@pytest.fixture
def mock_filling():
    mock_filling = Mock()
    mock_filling.get_name.return_value = Data_first.filling_name
    mock_filling.get_price.return_value = Data_first.filling_price
    mock_filling.get_type.return_value = Data_first.filling_type
    return mock_filling


@pytest.fixture
def mock_filling_second():
    mock_filling_s = Mock()
    mock_filling_s.get_name.return_value = Data_second.filling_name
    mock_filling_s.get_price.return_value = Data_second.filling_price
    mock_filling_s.get_type.return_value = Data_second.filling_type
    return mock_filling_s


@pytest.fixture
def dbase():
    return Database()
