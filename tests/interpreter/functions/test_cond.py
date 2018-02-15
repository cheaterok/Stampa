import pytest

from interpreter.functions.conditional import *


class TestIf:
    """
    Выбор по логическому условию
    """

    def test_if1(self):
        assert if_(1, 100, 200) == 100

    def test_if2(self):
        assert if_(0, 100, 200) == 200


class TestNcase0:
    """
    Выбор по индексу от нуля
    """
    
    def test_ncase1(self):
        assert ncase0(0, 100, 4, 5, 6, 7) == 4

    def test_ncase2(self):
        assert ncase0(2, 100, 4, 5, 6, 7) == 6

    def test_ncase3(self):
        assert ncase0(9, 100, 4, 5, 6, 7) == 100


class TestNcase1:
    """
    Выбор по индексу от единицы
    """

    def test_ncase1(self):
        assert ncase1(0, 100, 4, 5, 6, 7) == 100

    def test_ncase2(self):
        assert ncase1(1, 100, 4, 5, 6, 7) == 4

    def test_ncase3(self):
        assert ncase1(2, 100, 4, 5, 6, 7) == 5

    def test_ncase4(self):
        assert ncase1(9, 100, 4, 5, 6, 7) == 100


class TestRcase:
    """
    Выбор по диапазонам V(n) >= S < V(n+1)
    """

    def test_rcase1(self):
        assert rcase(-20, "Very cold", -10, "Cold", 5, "Norm", 40, "Hot") == "Very cold"

    def test_rcase2(self):
        assert rcase(-10, "Very cold", -10, "Cold", 5, "Norm", 40, "Hot") == "Cold"

    def test_rcase3(self):
        assert rcase(7, "Very cold", -10, "Cold", 5, "Norm", 40, "Hot") == "Norm"

    def test_rcase4(self):
        assert rcase(500, "Very cold", -10, "Cold", 5, "Norm", 40, "Hot") == "Hot"


class TestLcase:
    """
    Выбор по диапазонам V(n) > S =< V(n+1)
    """

    def test_lcase1(self):
        assert lcase(-20, "Very cold", -10, "Cold", 5, "Norm", 40, "Hot") == "Very cold"

    def test_lcase2(self):
        assert lcase(-10, "Very cold", -10, "Cold", 5, "Norm", 40, "Hot") == "Very cold"

    def test_lcase3(self):
        assert lcase(7, "Very cold", -10, "Cold", 5, "Norm", 40, "Hot") == "Norm"

    def test_lcase4(self):
        assert lcase(500, "Very cold", -10, "Cold", 5, "Norm", 40, "Hot") == "Hot"


class TestTcase:
    """
    Выбор значения по ключу
    !!! Необходимо уточнить (могут ли быть строки)
    !!! уточнить про tcase_v2
    """

    def test_tcase1(self):
        assert tcase(2, 1, 100, 2, 200, 3, 300) == 200

    def test_tcase2(self):
        assert tcase(7, 1, 100, 2, 200, 3, 300) == ''
