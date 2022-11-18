def func_with_error():
    a = 10 / 0
    return a


if __name__ == "__main__":

    try:
        func_with_error()
    except (Exception,):
        pass

    print("Handle all exceptions with one except and cheat PEP")
    print("IDE has not anny complains about this code :)")
    print("Sometimes it is usefull, when you need to write your code fast")
    print("However it is really dirty!")
