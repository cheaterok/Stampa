import pytest

from interpreter.functions.math import *


class TestAdd:

    def test_positive(self):
        assert add(5, 6) == 5 + 6

    def test_negative(self):
        assert add(-10, 5) == -10 + 5

    def test_float(self):
        assert add(10.59, -43.145) == 10.59 + (-43.145)

    def test_typeerror(self):
        with pytest.raises(TypeError):
            add("Million", 3)


class TestSub:

    def test_positive(self):
        assert sub(40, 25) == 40 - 25

    def test_negative(self):
        assert sub(1, 400) == 1 - 400

    def test_float(self):
        assert sub(-3.33, 49.932) == -3.33 - 49.932

    def test_typeerror(self):
        with pytest.raises(TypeError):
            sub(49.214, "Two parrots")


class TestMul:

    def test_positive(self):
        assert mul(40, 25) == 40 * 25

    def test_negative(self):
        assert mul(-1, 400) == -1 * 400

    def test_float(self):
        assert mul(-3.33, 49.932) == -3.33 * 49.932

    def test_typeerror(self):
        with pytest.raises(TypeError):
            mul(52.12, "Thrice the power")


class TestDiv:

    def test_positive(self):
        assert div(5, 6) == 5 / 6

    def test_negative(self):
        assert div(-10, 5) == -10 / 5

    def test_float(self):
        assert div(10.59, -43.145) == 10.59 / (-43.145)

    def test_zerodivision(self):
        with pytest.raises(ZeroDivisionError):
            div(100, 0)

    def test_typeerror(self):
        with pytest.raises(TypeError):
            div("One love", 2)


class TestRem:

    def test_positive(self):
        assert rem(40, 25) == 40 % 25

    def test_negative(self):
        assert rem(-1, 400) == -1 % 400

    def test_float(self):
        assert rem(-3.33, 49.932) == -3.33 % 49.932

    def test_zerodivision(self):
        with pytest.raises(ZeroDivisionError):
            rem(100, 0)

    def test_typeerror(self):
        with pytest.raises(TypeError):
            rem(52.12, "Something heavy")


class TestMod:

    def test_positive(self):
        assert mod(5, 6) == 5 // 6

    def test_negative(self):
        assert mod(-10, 5) == -10 // 5

    def test_float(self):
        assert mod(10.59, -43.145) == 10.59 // (-43.145)

    def test_zerodivision(self):
        with pytest.raises(ZeroDivisionError):
            mod(100, 0)

    def test_typeerror(self):
        with pytest.raises(TypeError):
            mod(34.28, "Half of halfling")


class TestAbs:

    def test_zero(self):
        assert abs_(0) == abs(0)

    def test_positive(self):
        assert abs_(400) == abs(400)

    def test_negative(self):
        assert abs_(-3.33) == abs(-3.33)

    def test_typeerror(self):
        with pytest.raises(TypeError):
            abs_("Your self esteem")


class TestNeg:

    def test_zero(self):
        assert neg(0) == -0

    def test_positive(self):
        assert neg(400) == -400

    def test_negative(self):
        assert neg(-3.33) == -(-3.33)

    def test_typeerror(self):
        with pytest.raises(TypeError):
            neg("Infinity")


class TestR:

    def test_up(self):
        assert r(1.33, 0.25, "up") == 1.50

    def test_down(self):
        assert r(1.33, 0.25, "down") == 1.25

    def test_nearest(self):
        assert r(1.33, 0.25, "nearest") == 1.25

    def test_typeerror(self):
        with pytest.raises(TypeError):
            r("14 bottles of rum", 1, "nearest")

    def test_unknowndirection(self):
        with pytest.raises(TypeError):
            r(1.33, 0.25, "somewhere")
