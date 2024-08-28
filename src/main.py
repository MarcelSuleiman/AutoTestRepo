def concat(*args: str) -> str:
    return " ".join(args)


def divide(a: int | float | str, b: int | float | str) -> float:
    try:
        return float(a) / float(b)
    except ZeroDivisionError:
        raise ZeroDivisionError("Divide by ZERO is not allowed!")


if __name__ == "__main__":
    c = concat("Marcel", "Suleiman", "Third", "haha", "hehe")
    print(c)

    result = divide(10, 5)
    print(result)

    # Extra comment
