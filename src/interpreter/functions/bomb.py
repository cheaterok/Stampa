import string
import random

BOMB_STR_LEN = 32

# Генерируется при запуске интерпретатора
BOMB = ''.join(random.choices(string.ascii_uppercase + string.digits, k=BOMB_STR_LEN))


def bomb():
    return BOMB