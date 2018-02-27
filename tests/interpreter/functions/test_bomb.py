import pytest

import interpreter
from interpreter.functions.bomb import *


def test_bomb():
    assert interpreter.BOMB == bomb()
