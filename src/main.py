def concat(*args: str) -> str:
    return " ".join(args)


def divide(a: int | float | str, b: int | float | str) -> float:
    return float(a) / float(b)


if __name__ == "__main__":
    c = concat("Marcel", "Suleiman", "Third", "haha", "hehe")
    print(c)

    result = divide(10, 5)
    print(result)
