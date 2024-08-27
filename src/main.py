def concat(a: str, b: str) -> str:
    return f"{a}{b}"


def divide(a: int | float | str, b: int | float | str) -> float:
    try:
        return float(a) / float(b)
    except ZeroDivisionError:
        raise ZeroDivisionError("Divide by ZERO is not allowed!")


if __name__ == "__main__":
    c = concat("Marcel", "Suleiman")
    print(c)

    result = divide(10, 5)
    print(result)
