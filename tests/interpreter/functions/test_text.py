import pytest

from interpreter.functions.text import *


class TestTrim:

    def test_trim(self):
        assert trim("       so  much    spaces       ") == "so  much    spaces"

    def test_empty(self):
        assert trim("                ") == ""

    def test_typeerror(self):
        with pytest.raises(TypeError):
            trim(42)


class TestTrimt:

    def test_trimt(self):
        assert trimt("       so  much    spaces       ") == "       so  much    spaces"

    def test_empty(self):
        assert trimt("                ") == ""

    def test_typeerror(self):
        with pytest.raises(TypeError):
            trimt(42)


class TestTriml:

    def test_trimt(self):
        assert triml("       so  much    spaces       ") == "so  much    spaces       "

    def test_empty(self):
        assert triml("                ") == ""

    def test_typeerror(self):
        with pytest.raises(TypeError):
            triml(42)


class TestPart:

    def test_part(self):
        assert part("SomeRandomTextHere", 4, 3) == "xtHe"

    def test_empty(self):
        with pytest.raises(IndexError):
            part("", 100, 100)

    def test_typeerror(self):
        with pytest.raises(TypeError):
            part(42, "32", "Much text")


class TestNws:

    def test_nws(self):
        assert nws("       so  much    spaces       ") == "so much spaces"

    def test_empty(self):
        assert nws("                ") == ""

    def test_typeerror(self):
        with pytest.raises(TypeError):
            nws(42)


class TestSed:
    pass


class TestTr:
    pass


class TestUc:

    def test_uc(self):
        assert uc("hEllO") == "HELLO"

    def test_uc_rus(self):
        assert uc("пРиФФФки))))") == "ПРИФФФКИ))))"

    def test_empty(self):
        assert uc("") == ""

    def test_typeerror(self):
        with pytest.raises(TypeError):
            uc(42)


class TestLc:

    def test_lc(self):
        assert lc("ByeBye") == "byebye"

    def test_lc_rus(self):
        assert lc("чЕгО ГРустНеньКиЙ ТаКой((((") == "чего грустненький такой(((("

    def test_empty(self):
        assert lc("") == ""

    def test_typeerror(self):
        with pytest.raises(TypeError):
            lc(42)


class TestF:

    def test_f(self):
        assert f("int=%d, float=%f, string=%s", 45, -30.2, "testing") == "int=45, float=-30.200000, string=testing"

    def test_typeerror(self):
        with pytest.raises(TypeError):
            f("%d, %f", "not int", "not float")
