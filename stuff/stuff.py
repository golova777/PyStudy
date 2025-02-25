from typing import Any

def divide_it(divisible: int | float, divider: int | float) -> float:
    result: Any = None
    try:
        if type(divisible) is not type(divider):
            raise ArithmeticError(
                f"типы параметров не совпадают, divisible: {type(divisible)}, divider: {type(divider)}"
            )

        result = divisible / divider

    except ZeroDivisionError as e:
        raise
    else:
        return result


