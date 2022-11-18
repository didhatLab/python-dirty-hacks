def main(x: int):
    funcs = [lambda a: a * i for i in range(x)]

    for func in funcs:
        print(func(2))


if __name__ == "__main__":
    main(4)
