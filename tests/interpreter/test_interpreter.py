import pytest

import interpreter


def test_0():
    assert interpreter.evaluate(' add ( r(1.33, 0.25, "up"), neg(1))') == '0.5'


def test_1():
    assert interpreter.evaluate('trim("Hello " "world" )') == 'Hello world'


def test_2():
    assert interpreter.evaluate('nws({Много пробелов это   плохо})  ') == 'Много пробелов это плохо'


def test_3():
    assert interpreter.evaluate('seq  (/Winter Olympics/, <Winter Olympics>)') == '1'


def test_4():
    assert interpreter.evaluate('trim("  "):-/Unknown value/') == 'Unknown value'


def test_5():
    assert interpreter.evaluate('trim(/  /):+add(2, 2)') == '4'


def test_6():
    assert interpreter.evaluate('trim([ Privet]):+add(2, 2)') == 'Privet'

def test_7():
    assert interpreter.evaluate('bomb()') == interpreter.BOMB
