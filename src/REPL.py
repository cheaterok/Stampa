from interpreter import evaluate


def REPL():
    try:
        while True:
            code = input("-> ")
            print(evaluate(code))
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    REPL()
