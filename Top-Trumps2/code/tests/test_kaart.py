import pytest
from ..kaart import Kaart

def test_kaart_initialization():
    kaart = Kaart("A", [1, 2, 3, 4])
    assert kaart.naam == "a"
    assert kaart.attr_list == [1, 2, 3, 4]

def test_kaart_initialization_with_different_case():
    kaart = Kaart("B", [1, 2, 3, 4])
    assert kaart.naam == "b"

def test_kaart_attribute_access():
    kaart = Kaart("A", [1, 2, 3, 4])
    assert kaart.attr_list[0] == 1
    assert kaart.attr_list[1] == 2
    assert kaart.attr_list[2] == 3
    assert kaart.attr_list[3] == 4




def test_isgelijk():
    kaart1 = Kaart("A", [1, 2, 3, 4])
    kaart2 = Kaart("B", [1, 2, 3, 4])

    assert kaart1.isgelijk(kaart2, 1) == True
    assert kaart1.isgelijk(kaart2, 2) == True
    assert kaart1.isgelijk(kaart2, 3) == True
    assert kaart1.isgelijk(kaart2, 4) == True

def test_isgroter():
    kaart1 = Kaart("A", [1, 2, 3, 4])
    kaart2 = Kaart("B", [0, 1, 2, 3])

    assert kaart1.isgroter(kaart2, 1) == True
    assert kaart1.isgroter(kaart2, 2) == True
    assert kaart1.isgroter(kaart2, 3) == True
    assert kaart1.isgroter(kaart2, 4) == True

def test_inequality():
    kaart1 = Kaart("A", [1, 2, 3, 4])
    kaart2 = Kaart("B", [1, 2, 3, 4])

    assert kaart1.isgelijk(kaart2, 1) == False
    assert kaart1.isgroter(kaart2, 1) == False

    assert kaart1.isgelijk(kaart2, 2) == False
    assert kaart1.isgroter(kaart2, 2) == False

    assert kaart1.isgelijk(kaart2, 3) == False
    assert kaart1.isgroter(kaart2, 3) == False

    assert kaart1.isgelijk(kaart2, 4) == False
    assert kaart1.isgroter(kaart2, 4) == False
