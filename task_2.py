
import re
from typing import Callable


def generator_numbers(text: str):
    # Знаходимо дійсні числа, відокремлені пробілами
    pattern = r'(?<!\S)\d+(?:\.\d+)?(?!\S)'

    for number in re.findall(pattern, text):
        yield float(number)


def sum_profit(text: str, func: Callable) -> float:
    # Обчислюємо загальну суму чисел
    return sum(func(text))


# Перевіряємо роботу функцій
text = (
    "Загальний дохід працівника складається з декількох частин: "
    "1000.01 як основний дохід, доповнений додатковими надходженнями "
    "27.45 і 324.00 доларів."
)

total_income = sum_profit(text, generator_numbers)

print(f"Загальний дохід: {total_income}")
