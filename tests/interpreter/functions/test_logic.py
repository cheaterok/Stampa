import pytest

from interpreter.functions.logical import *


class TestAnd:
    """
    Логическое И
    !!! Необходимо уточнить (что возвращает, для каких чисел)
    """

    def test_equ_val(self):
        assert _and(10, 10) == 10 and 10

    def test_neq_val(self):
        assert _and(10, 1) == 10 and 1

    def test_letters(self):
        assert _and("ab", "ab") == "ab" and "ab"

    def test_typeerror(self):
        with pytest.raises(TypeError):
            _and(10, "a")


class TestOr:
    """
    Логическое ИЛИ
    !!! Необходимо уточнить (что возвращает, для каких чисел)
    """

    def test_equ_val(self):
        assert _or(17, 17) == 17 or 17

    def test_neq_val(self):
        assert _or(15, 1) == 15 or 1

    def test_letters(self):
        assert _or("ab", "ab") == "ab" or "ab"

    def test_typeerror(self):
        with pytest.raises(TypeError):
            _or(7, "d")


class TestNot:
    """
    Логическое НЕ
    !!! Необходимо уточнить (что возвращает, для каких чисел)
    """

    def test_not_one(self):
        assert _not(1) == 0

    def test_not_zero(self):
        assert _not(0) == 1

    def test_typeerror(self):
        with pytest.raises(TypeError):
            _not("two")


class TestSeq:
    """
    "Строковая операция РАВНО" (1 - равно, 0 - не равно)
    !!! Необходимо уточнить (что возвращает)
    """

    def test_seq1(self):
        assert seq("Winter Olympics", "Winter Olympics") == 1

    def test_seq2(self):
        assert seq("Very_cold99 ", "Very_cold99     ") == 0

    def test_seq3(self):
        assert seq("Winter Olympics", "Winter ( Olympics") == 0

    def test_typeerror(self):
        with pytest.raises(TypeError):
            seq(1, "a")


class TestSne:
    """
    "Строковая операция НЕ РАВНО" (1 - не равно, 0 - равно)
    !!! Необходимо уточнить (что возвращает)
    """

    def test_sne1(self):
        assert sne("Summer Olympics", "Summer   Olympics") == 1

    def test_sne2(self):
        assert sne("Эти строки не равны", "эти строки не ровны") == 1

    def test_sne3(self):
        assert sne("Три два один", "Три два один") == 0

    def test_typeerror(self):
        with pytest.raises(TypeError):
            sne(1, "a")


class TestSgt:
    """
     "Строковая операция БОЛЬШЕ" (1 - больше, 0 - меньше)
    !!! Необходимо уточнить (что возвращает)
    """

    def test_sgt1(self):
        assert sgt("abc", "acb") == 1

    def test_sgt2(self):
        assert sgt("Привет мир", "Hello world") == "Привет мир" > 1

    def test_sgt3(self):
        assert sgt("1000", "0000") == 0

    def test_typeerror(self):
        with pytest.raises(TypeError):
            sgt(1, "da")


class TestSge:
    """
    "Строковая операция БОЛЬШЕ ИЛИ РАВНО" (1 - больше или равно, 0 - меньше)
    !!! Необходимо уточнить (что возвращает)
    """

    def test_sge1(self):
        assert sge("qwe", "qew") == 1

    def test_sge2(self):
        assert sge("Привет мир", "Hello world") == 1

    def test_sge3(self):
        assert sge("Winter Olympics", "winter Olympics") == 0

    def test_typeerror(self):
        with pytest.raises(TypeError):
            sge(10, "aga")


class TestSlt:
    """
    "Строковая операция МЕНЬШЕ" (1 - меньше, 0 - больше)
    !!! Необходимо уточнить (что возвращает)
    """

    def test_slt1(self):
        assert slt("hello", "привет") == 1

    def test_slt2(self):
        assert slt("12345", "12354") == 1

    def test_slt3(self):
        assert slt("эти строки не равны", "Эти строки не равны") == 0

    def test_typeerror(self):
        with pytest.raises(TypeError):
            slt("hello", 777)


class TestSle:
    """
    "Строковая операция МЕНЬШЕ ИЛИ РАВНО" (1 - меньше или равно, 0 - больше)
    """

    def test_slt1(self):
        assert sle("hello", "привет") == 1

    def test_slt2(self):
        assert sle("12354", "12345") == 0

    def test_slt3(self):
        assert sle("123", "123") == 1

    def test_slt4(self):
        assert sle("эти строки равны", "эти строки равны") == 1

    def test_typeerror(self):
        with pytest.raises(TypeError):
            sle("hello", 12)


class TestNeq:
    """
    Числовая операция РАВНО (1 - равно, 0 - не равно)
    !!! Необходимо уточнить (что возвращает)
    """

    def test_negative(self):
        assert neq(-1, -1) == 1

    def test_positive(self):
        assert neq(107, 107) == 1

    def test_not_eq(self):
        assert neq(-5, 5) == 0

    def test_int_float(self):
        assert neq(5, 5.0) == 1

    def test_typeerror(self):
        with pytest.raises(TypeError):
            neq("hello", 12)


class TestNne:
    """
    Числовая операция НЕ РАВНО (1 - не равно, 0 - равно)
    !!! Необходимо уточнить (что возвращает)
    """

    def test_negative(self):
        assert nne(-1, 1) == 1

    def test_positive(self):
        assert nne(1, 107) == 1

    def test_not_eq(self):
        assert nne(-5, -5) == 0

    def test_int_float(self):
        assert nne(1.0, 1) == 0

    def test_typeerror(self):
        with pytest.raises(TypeError):
            nne("hello", 12)


class TestNgt:
    """
    Числовая операция БОЛЬШЕ (1 - больше, 0 - меньше)
    !!! Необходимо уточнить (что возвращает)
    """

    def test_int_float(self):
        assert ngt(1, 1.000000001) == 0

    def test_eq(self):
        assert ngt(23, 22) == 1

    def test_typeerror(self):
        with pytest.raises(TypeError):
            ngt("hello", 12)


class TestNge:
    """
    Числовая операция БОЛЬШЕ ИЛИ РАВНО(1 - больше или равно, 0 - меньше)
    !!! Необходимо уточнить (что возвращает)
    """

    def test_int_float(self):
        assert nge(1, 1.000000001) == 1

    def test_eq(self):
        assert nge(2, 2) == 1

    def test_smaller(self):
        assert nge(3, 5) == 0

    def test_typeerror(self):
        with pytest.raises(TypeError):
            nge("hello", 12)


class TestNlt:
    """
    Числовая операция МЕНЬШЕ(1 - меньше, 0 - больше)
    !!! Необходимо уточнить (что возвращает)
    """

    def test_int_float(self):
        assert nlt(1, 1.000000001) == 0

    def test_eq(self):
        assert nlt(2, 3) == 1

    def test_typeerror(self):
        with pytest.raises(TypeError):
            nlt("hello", 12)


class TestNle:
    """
    Числовая операция МЕНЬШЕ ИЛИ РАВНО(1 - меньше или равно, 0 - больше)
    !!! Необходимо уточнить (что возвращает)
    """

    def test_int_float(self):
        assert nle(1, 1.000000001) == 1

    def test_eq(self):
        assert nle(2, 2) == 1

    def test_larger(self):
        assert nle(3, 5) == 0

    def test_typeerror(self):
        with pytest.raises(TypeError):
            nle("hello", 12)


class TestEven:
    """
    Првека, что число четное (1 - четное, 0 - нечетное)
    !!! Необходимо уточнить (что возвращает)
    """

    def test_even(self):
        assert even(10) == 1

    def test_odd(self):
        assert even(11) == 0

    def test_typeerror(self):
        with pytest.raises(TypeError):
            even("hello")


class TestOdd:
    """
    Првека, что число нечетное (1 - нечетное, 0 - четное)
    !!! Необходимо уточнить (что возвращает)
    """

    def test_even(self):
        assert odd(101) == 1

    def test_odd(self):
        assert odd(-110) == 0

    def test_typeerror(self):
        with pytest.raises(TypeError):
            even("hello")
